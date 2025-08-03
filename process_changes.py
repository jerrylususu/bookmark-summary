import re
from typing import List, Optional
import requests
import json
from datetime import datetime, timezone
from pathlib import Path
from dataclasses import dataclass, asdict
import os
import logging
import time
from functools import wraps
from urllib.parse import quote
from waybackpy import WaybackMachineSaveAPI
import mistune

# -- configurations begin --
BOOKMARK_COLLECTION_REPO_NAME: str = "bookmark-collection"
BOOKMARK_SUMMARY_REPO_NAME: str = "bookmark-summary"
MAX_CONTENT_LENGTH: int = 32 * 1024  # 32KB
MIN_CONTENT_LENGTH: int = 200  # Minimum content length to consider valid
MAX_RETRIES: int = 3  # Maximum retry attempts for fetching content
NO_SUMMARY_TAG: str = "#nosummary"
# -- configurations end --

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(filename)s:%(lineno)d - %(funcName)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

def log_execution_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        logging.info(f'Entering {func.__name__}')
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        elapsed_time = end_time - start_time
        logging.info(f'Exiting {func.__name__} - Elapsed time: {elapsed_time:.4f} seconds')
        return result
    return wrapper

@dataclass
class SummarizedBookmark:
    month: str  # yyyyMM
    title: str
    url: str
    timestamp: int  # unix timestamp

CURRENT_MONTH: str = datetime.now(timezone.utc).strftime('%Y%m')
CURRENT_DATE: str = datetime.now(timezone.utc).strftime('%Y-%m-%d')
CURRENT_DATE_AND_TIME: str = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S')

@log_execution_time
def submit_to_wayback_machine(url: str):
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"
    try:
        save_api = WaybackMachineSaveAPI(url, user_agent)
        wayback_url = save_api.save()
        logging.info(f'Wayback Saved: {wayback_url}')
    except Exception as e:
        # 非关键路径，容忍失败
        logging.warning(f"submit to wayback machine failed, skipping, url={url}")
        logging.exception(e)

@log_execution_time
def get_text_content(url: str) -> str:
    """
    Fetch text content from URL with retry logic and minimum length validation.
    
    Args:
        url: The URL to fetch content from
        
    Returns:
        str: The fetched text content
        
    Raises:
        Exception: If all retry attempts fail or content is too short
    """
    jina_url: str = f"https://r.jina.ai/{url}"
    
    for attempt in range(MAX_RETRIES):
        try:
            response: requests.Response = requests.get(jina_url)
            content = response.text.strip()
            
            # Check if content is too short (likely an error message)
            if len(content) < MIN_CONTENT_LENGTH:
                if "upstream connect error" in content.lower() or "connection termination" in content.lower():
                    error_msg = f"Connection error detected (attempt {attempt + 1}/{MAX_RETRIES})"
                else:
                    error_msg = f"Content too short ({len(content)} chars, minimum {MIN_CONTENT_LENGTH}) - attempt {attempt + 1}/{MAX_RETRIES}"
                
                logging.warning(error_msg)
                
                if attempt < MAX_RETRIES - 1:
                    # Exponential backoff: wait 2^attempt seconds before retrying
                    wait_time = 2 ** attempt
                    logging.info(f"Retrying in {wait_time} seconds...")
                    time.sleep(wait_time)
                    continue
                else:
                    raise Exception(f"All {MAX_RETRIES} retry attempts failed. Last error: {error_msg}")
            
            # Content is valid length, proceed with processing
            if len(content) > MAX_CONTENT_LENGTH:
                logging.warning(f"Content length ({len(content)}) exceeds maximum ({MAX_CONTENT_LENGTH}), truncating...")
                content = content[:MAX_CONTENT_LENGTH]
            
            logging.info(f"Successfully fetched content with {len(content)} characters")
            return content
            
        except requests.RequestException as e:
            logging.warning(f"Request failed (attempt {attempt + 1}/{MAX_RETRIES}): {e}")
            if attempt < MAX_RETRIES - 1:
                wait_time = 2 ** attempt
                logging.info(f"Retrying in {wait_time} seconds...")
                time.sleep(wait_time)
            else:
                raise Exception(f"All {MAX_RETRIES} retry attempts failed. Last error: {e}")

@log_execution_time
def call_openai_api(prompt: str, content: str) -> str:
    model: str = os.environ.get('OPENAI_API_MODEL', 'gpt-4o-mini')
    headers: dict = {
        "Authorization": f"Bearer {os.environ['OPENAI_API_KEY']}",
        "Content-Type": "application/json"
    }
    data: dict = {
        "model": model,
        "messages": [
            {"role": "system", "content": prompt},
            {"role": "user", "content": content}
        ]
    }
    api_endpoint: str = os.environ.get('OPENAI_API_ENDPOINT', 'https://api.openai.com/v1/chat/completions')
    
    # 添加请求相关日志
    logging.info(f"Calling OpenAI API with model: {model}")
    logging.info(f"API endpoint: {api_endpoint}")
    
    response: requests.Response = requests.post(api_endpoint, headers=headers, data=json.dumps(data))
    
    # 添加响应相关日志
    logging.info(f"Response status code: {response.status_code}")
    response_json = response.json()
    logging.debug(f"Response content: {json.dumps(response_json, ensure_ascii=False)}")
    
    # 错误处理
    if response.status_code != 200:
        error_msg = f"OpenAI API request failed with status {response.status_code}"
        logging.error(error_msg)
        logging.error(f"Error response: {response_json}")
        raise Exception(error_msg)
    
    if 'choices' not in response_json:
        error_msg = "Response does not contain 'choices' field"
        logging.error(error_msg)
        logging.error(f"Full response: {response_json}")
        raise Exception(error_msg)
        
    return response_json['choices'][0]['message']['content']

@log_execution_time
def summarize_text(text: str) -> str:
    prompt: str = """
结构化总结这篇文章。输出时使用简体中文。
输出时直接给出总结内容，不需要附带“以下是总结”的开始文字或额外的标题。
"""
    return call_openai_api(prompt, text)

@log_execution_time
def one_sentence_summary(text: str) -> str:
    prompt: str = f"以下是对一篇长文的列表形式总结。请基于此输出对该文章的简短总结，长度不超过100个字。总是使用简体中文输出。"
    return call_openai_api(prompt, text)

def slugify(text: str) -> str:
    # replace invalid fs chars with -
    invalid_fs_chars: str = '/\\:*?"<>|'
    return re.sub(r'[' + re.escape(invalid_fs_chars) + r'\s]+', '-', text.lower()).strip('-')

def get_summary_file_path(title: str, timestamp: int, month: Optional[str] = None, in_readme_md: bool = False) -> Path:
    date_str = datetime.fromtimestamp(timestamp, tz=timezone.utc).strftime('%Y-%m-%d')
    summary_filename: str = f"{date_str}-{slugify(title)}.md"
    if in_readme_md:
        if month is None:
            raise ValueError("Month must be provided when in_readme_md is True")
        root: Path = Path(".", month)
        summary_filename = f"{date_str}-{quote(slugify(title))}.md"
    else:
        if month is None:
            month = CURRENT_MONTH
        root: Path = Path(BOOKMARK_SUMMARY_REPO_NAME, month)
    summary_path: Path = Path(root, summary_filename)
    return summary_path

def get_text_content_path(title: str, in_summary_md: bool = False) -> Path:
    text_content_filename: str = f"{CURRENT_DATE}-{slugify(title)}_raw.md"
    root: Path = Path(BOOKMARK_SUMMARY_REPO_NAME, CURRENT_MONTH)
    if in_summary_md:
        root = Path(".")
    text_content_path: Path = Path(root, text_content_filename)
    return text_content_path

def build_summary_file(title: str, url: str, summary: str, one_sentence: str) -> str:
    return f"""# {title}
- URL: {url}
- Added At: {CURRENT_DATE_AND_TIME}
- [Link To Text]({get_text_content_path(title, in_summary_md=True)})

## TL;DR
{one_sentence}

## Summary
{summary}
"""

def extract_tldr_from_markdown(file_path: str) -> str:
    """Extract TL;DR content from a markdown file using mistune AST parser."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Create mistune markdown parser for AST
        markdown = mistune.create_markdown(renderer=None)
        ast = markdown(content)
        
        tldr_content = []
        found_tldr = False
        
        for token in ast:
            if token['type'] == 'heading' and token.get('attrs', {}).get('level') == 2:
                # Check if this is the TL;DR heading
                if 'TL;DR' in str(token.get('children', [])):
                    found_tldr = True
                    continue
                elif found_tldr:
                    # Next H2 heading, stop collecting
                    break
            elif found_tldr and token['type'] == 'paragraph':
                # Collect paragraph content
                def extract_text(children):
                    text_parts = []
                    for child in children:
                        if child['type'] == 'text':
                            text_parts.append(child['raw'])
                        elif 'children' in child:
                            text_parts.extend(extract_text(child['children']))
                    return text_parts
                
                text_parts = extract_text(token.get('children', []))
                tldr_content.append(''.join(text_parts))
        
        return '\n'.join(tldr_content).strip()
    except Exception as e:
        logging.warning(f"Could not read TL;DR from {file_path}: {e}")
    return ""

def build_summary_readme_md(summarized_bookmarks: List[SummarizedBookmark]) -> str:
    initial_prefix: str = """# Bookmark Summary 
读取 bookmark-collection 中的书签，使用 jina reader 获取文本内容，然后使用 LLM 总结文本。详细实现请参见 process_changes.py。需要和 bookmark-collection 中的 Github Action 一起使用。

"""
    
    # Group bookmarks by month
    bookmarks_by_month = {}
    for bookmark in summarized_bookmarks:
        month_key = bookmark.month
        if month_key not in bookmarks_by_month:
            bookmarks_by_month[month_key] = []
        bookmarks_by_month[month_key].append(bookmark)
    
    # Sort each month's bookmarks by timestamp (newest first)
    for month in bookmarks_by_month:
        bookmarks_by_month[month].sort(key=lambda b: b.timestamp, reverse=True)
    
    # Sort months in reverse chronological order
    sorted_months = sorted(bookmarks_by_month.keys(), reverse=True)
    
    readme_content = initial_prefix
    
    for month in sorted_months:
        # Add month header
        month_display = datetime.strptime(month, '%Y%m').strftime('%Y-%m')
        readme_content += f"## {month_display}\n\n"
        
        # Add bookmarks for this month
        for bookmark in bookmarks_by_month[month]:
            summary_file_path = get_summary_file_path(
                title=bookmark.title,
                timestamp=bookmark.timestamp,
                month=bookmark.month,
                in_readme_md=True
            )
            
            # Read TL;DR from the markdown file
            summary_file_path_for_tldr = get_summary_file_path(
                title=bookmark.title,
                timestamp=bookmark.timestamp,
                month=bookmark.month,
                in_readme_md=False
            )
            tldr = extract_tldr_from_markdown(str(summary_file_path_for_tldr))
            
            date_str = datetime.fromtimestamp(bookmark.timestamp, tz=timezone.utc).strftime('%Y-%m-%d')
            readme_content += f"- ({date_str}) [{bookmark.title}]({summary_file_path})\n"
            
            if tldr:
                readme_content += f"  - {tldr}\n"
        
        readme_content += "\n"

    return readme_content

@log_execution_time
def process_bookmark_file():
    bookmark_lines: List[str] = []
    try:
        with open(f'{BOOKMARK_COLLECTION_REPO_NAME}/README.md', 'r', encoding='utf-8') as f:
            bookmark_lines = f.readlines()
    except FileNotFoundError:
        logging.warning(f"'{BOOKMARK_COLLECTION_REPO_NAME}/README.md' not found, skipping new bookmark processing.")

    with open(f'{BOOKMARK_SUMMARY_REPO_NAME}/data.json', 'r', encoding='utf-8') as f:
        summarized_bookmark_dicts = json.load(f)
        summarized_bookmarks = [SummarizedBookmark(**bookmark) for bookmark in summarized_bookmark_dicts]

    summarized_urls = set([bookmark.url for bookmark in summarized_bookmarks])

    # find the first unprocessed && summary-not-present bookmark
    title: Optional[str] = None
    url: Optional[str] = None
    for line in bookmark_lines:
        match: re.Match = re.search(r'-\s*\[(.*?)\]\((.*?)\)', line)
        if match and match.group(2) not in summarized_urls:
            if NO_SUMMARY_TAG in line:
                logging.debug(f"Skipping bookmark with {NO_SUMMARY_TAG} tag: {match.group(1)}")
                continue
            title, url = match.groups()
            break

    if title and url:
        # Create folder for month if it doesn't exist
        Path(f'{BOOKMARK_SUMMARY_REPO_NAME}/{CURRENT_MONTH}').mkdir(parents=True, exist_ok=True)

        # process the bookmark
        submit_to_wayback_machine(url)
        text_content: str = get_text_content(url)
        summary: str = summarize_text(text_content)
        one_sentence: str = one_sentence_summary(summary)
        summary_file_content: str = build_summary_file(title, url, summary, one_sentence)
        timestamp = int(datetime.now(timezone.utc).timestamp())
        
        with open(get_text_content_path(title), 'w', encoding='utf-8') as f:
            f.write(text_content)

        with open(get_summary_file_path(title, timestamp=timestamp), 'w', encoding='utf-8') as f:
            f.write(summary_file_content)
        
        # Update data.json
        summarized_bookmarks.append(SummarizedBookmark(
            month=CURRENT_MONTH,
            title=title,
            url=url,
            timestamp=timestamp
        ))
        with open(f'{BOOKMARK_SUMMARY_REPO_NAME}/data.json', 'w', encoding='utf-8') as f:
            json.dump([asdict(bookmark) for bookmark in summarized_bookmarks], f, indent=2, ensure_ascii=False)

    # Update bookmark-summary/README.md
    with open(f'{BOOKMARK_SUMMARY_REPO_NAME}/README.md', 'w', encoding='utf-8') as f:
        f.write(build_summary_readme_md(summarized_bookmarks))

def main():
    process_bookmark_file()

if __name__ == "__main__":
    main()