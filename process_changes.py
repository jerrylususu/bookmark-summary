import re
from typing import List, Optional
import requests
import json
from datetime import datetime
from pathlib import Path
from dataclasses import dataclass, asdict
import os
import logging
import time
from functools import wraps
from urllib.parse import quote

# -- configurations begin --
BOOKMARK_COLLECTION_REPO_NAME: str = ""
BOOKMARK_SUMMARY_REPO_NAME: str = "."
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

CURRENT_MONTH: str = datetime.now().strftime('%Y%m')
CURRENT_DATE: str = datetime.now().strftime('%Y-%m-%d')
CURRENT_DATE_AND_TIME: str = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

@log_execution_time
def get_text_content(url: str) -> str:
    jina_url: str = f"https://r.jina.ai/{url}"
    response: requests.Response = requests.get(jina_url)
    return response.text

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
    response: requests.Response = requests.post(api_endpoint, headers=headers, data=json.dumps(data))
    return response.json()['choices'][0]['message']['content']

@log_execution_time
def summarize_text(text: str) -> str:
    prompt: str = """
请用markdown列表格式**详细**总结我发送给你的文本。充分合理使用缩进和子列表，如果有需要可以使用多层子列表，或是在子列表中包含多个条目（3个或以上）。在每个总结项开头，用简短的词语描述该项。忽略和文章主体无关的内容（如广告）。无论原文语言为何，总是使用中文进行总结。

示例如下：

1. **Trello简介**：Trello是Fog Creek Software推出的100%基于云端的团队协作工具，自发布以来获得了积极的反馈和强劲的用户增长。

2. **开发模式转变**：Trello的开发标志着Fog Creek转向完全的云服务，不再提供安装版软件，开发过程中未使用Visual Basic，体现了开发流程的现代化。

3. **产品定位**：Trello是一款横跨多行业的产品，与之前主要针对软件开发者的垂直产品不同，它适用于各行各业的用户。

4. **横纵对比**：
   - **横向产品**：适用于广泛用户群体，如Word处理器和Web浏览器，难以定价过高，风险与回报并存。
   - **垂直产品**：针对特定行业，如牙医软件，用户定位明确，利润空间大，适合初创企业。

5. **Excel故事**：通过Excel的使用案例说明，大多数用户使用Excel实际上是作为列表工具，而非复杂的计算，引出“杀手级应用实际上是高级数据结构”的观点。

6. **Trello的核心**：Trello是一个高度灵活的数据结构应用，不仅限于敏捷开发的Kanban板，适用于规划婚礼、管理招聘流程等多种场景。

7. **产品特性**：
   - **持续交付**：新功能不断推出，无重大或次要版本的区别。
   - **快速迭代与修复**：测试不求面面俱到，但快速响应修复。
   - **公共透明**：开发过程公开，用户可参与反馈和投票。
   - **快速扩张策略**：目标是大规模用户增长，初期免费，优先消除采用障碍。
   - **API优先**：鼓励通过API和插件扩展功能，用户和第三方参与建设。

8. **技术选择**：采用前沿技术如MongoDB、WebSockets、CoffeeScript和Node.js，虽然有挑战，但有利于吸引顶尖程序员并为长期发展做准备。

9. **总结**：Trello及其开发策略体现了现代互联网产品的开发趋势，注重用户基础的快速扩展，技术的前沿性，以及通过社区参与和反馈来不断优化产品。
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
    date_str = datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d')
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

def build_summary_readme_md(summarized_bookmarks: List[SummarizedBookmark]) -> str:
    initial_prefix: str = """# Bookmark Summary 
读取 bookmark-collection 中的书签，使用 jina reader 获取文本内容，然后使用 LLM 总结文本。详细实现请参见 process_changes.py。需要和 bookmark-collection 中的 Github Action 一起使用。
    
## Summarized Bookmarks
"""
    summary_list: str = ""
    sorted_summarized_bookmarks = sorted(summarized_bookmarks, key=lambda bookmark: bookmark.timestamp, reverse=True)
   
    for bookmark in sorted_summarized_bookmarks:
        summary_file_path = get_summary_file_path(
            title=bookmark.title,
            timestamp=bookmark.timestamp,
            month=bookmark.month,  # 传递书签的月份
            in_readme_md=True
        )
        summary_list += f"- ({datetime.fromtimestamp(bookmark.timestamp).strftime('%Y-%m-%d')}) [{bookmark.title}]({summary_file_path})\n"

    return initial_prefix + summary_list

@log_execution_time
def process_bookmark_file():
    # with open(f'{BOOKMARK_COLLECTION_REPO_NAME}/README.md', 'r', encoding='utf-8') as f:
    #     bookmark_lines: List[str] = f.readlines()

    with open(f'{BOOKMARK_SUMMARY_REPO_NAME}/data.json', 'r', encoding='utf-8') as f:
        summarized_bookmark_dicts = json.load(f)
        summarized_bookmarks = [SummarizedBookmark(**bookmark) for bookmark in summarized_bookmark_dicts]

    summarized_urls = set([bookmark.url for bookmark in summarized_bookmarks])

    # find the first unprocessed && summary-not-present bookmark
    # title: Optional[str] = None
    # url: Optional[str] = None
    # for line in bookmark_lines:
    #     match: re.Match = re.search(r'- \[(.*?)\]\((.*?)\)', line)
    #     if match and match.group(2) not in summarized_urls:
    #         title, url = match.groups()
    #         break

    if True:
        # Create folder for month if it doesn't exist
        # Path(f'{BOOKMARK_SUMMARY_REPO_NAME}/{CURRENT_MONTH}').mkdir(parents=True, exist_ok=True)

        # # process the bookmark
        # text_content: str = get_text_content(url)
        # summary: str = summarize_text(text_content)
        # one_sentence: str = one_sentence_summary(summary)
        # summary_file_content: str = build_summary_file(title, url, summary, one_sentence)
        # timestamp = int(datetime.now().timestamp())
        
        # with open(get_text_content_path(title), 'w', encoding='utf-8') as f:
        #     f.write(text_content)

        # with open(get_summary_file_path(title, timestamp=timestamp), 'w', encoding='utf-8') as f:
        #     f.write(summary_file_content)
        
        # # Update bookmark-summary/README.md
        # summarized_bookmarks.append(SummarizedBookmark(
        #     month=CURRENT_MONTH,
        #     title=title,
        #     url=url,
        #     timestamp=timestamp
        # ))

        with open(f'{BOOKMARK_SUMMARY_REPO_NAME}/README.md', 'w', encoding='utf-8') as f:
            f.write(build_summary_readme_md(summarized_bookmarks))

        # Update data.json
        with open(f'{BOOKMARK_SUMMARY_REPO_NAME}/data.json', 'w', encoding='utf-8') as f:
            json.dump([asdict(bookmark) for bookmark in summarized_bookmarks], f, indent=2, ensure_ascii=False)    

def main():
    process_bookmark_file()
    # local_debug()

if __name__ == "__main__":
    main()