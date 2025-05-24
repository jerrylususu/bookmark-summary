import re
from typing import List, Optional
from datetime import datetime
from pathlib import Path
from dataclasses import dataclass, asdict
from urllib.parse import quote
import logging # Added for log_execution_time if it's used here directly

# Assuming external_services.py will have log_execution_time and call_openai_api
from external_services import call_openai_api, log_execution_time

# -- configurations begin --
BOOKMARK_SUMMARY_REPO_NAME: str = "bookmark-summary" # Moved from process_changes.py
# -- configurations end --

# Define current time-based constants
CURRENT_MONTH: str = datetime.now().strftime('%Y%m')
CURRENT_DATE: str = datetime.now().strftime('%Y-%m-%d')
CURRENT_DATE_AND_TIME: str = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

@dataclass
class SummarizedBookmark:
    month: str  # yyyyMM
    title: str
    url: str
    timestamp: int  # unix timestamp

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
    date_str = datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d')
    summary_filename: str = f"{date_str}-{slugify(title)}.md"
    if in_readme_md:
        if month is None:
            raise ValueError("Month must be provided when in_readme_md is True")
        root: Path = Path(".", month)
        summary_filename = f"{date_str}-{quote(slugify(title))}.md" # quote is used here
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
    # Sort by timestamp descending
    sorted_summarized_bookmarks = sorted(summarized_bookmarks, key=lambda bookmark: bookmark.timestamp, reverse=True)
   
    for bookmark in sorted_summarized_bookmarks:
        summary_file_path = get_summary_file_path(
            title=bookmark.title,
            timestamp=bookmark.timestamp,
            month=bookmark.month,
            in_readme_md=True
        )
        summary_list += f"- ({datetime.fromtimestamp(bookmark.timestamp).strftime('%Y-%m-%d')}) [{bookmark.title}]({summary_file_path})\n"

    return initial_prefix + summary_list
