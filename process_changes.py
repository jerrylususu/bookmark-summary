import re # Still needed for process_bookmark_file
from typing import List, Optional # Still needed
# import requests # No longer directly needed, external_services.py handles its own import
# import json # No longer directly used, file_handler.py handles json operations
from datetime import datetime # Still needed for timestamp
from pathlib import Path # Still needed for Path object construction
from dataclasses import asdict # Still needed for asdict(bookmark)
# import os # No longer needed
import logging
import time # Still needed for log_execution_time
from functools import wraps # Still needed for log_execution_time
# from urllib.parse import quote # Moved to core_logic.py

from external_services import (
    submit_to_wayback_machine,
    get_text_content,
    MAX_CONTENT_LENGTH,
    log_execution_time, 
)
from core_logic import (
    SummarizedBookmark,
    summarize_text,
    one_sentence_summary,
    get_summary_file_path,
    get_text_content_path,
    build_summary_file,
    build_summary_readme_md,
    BOOKMARK_SUMMARY_REPO_NAME, 
    CURRENT_MONTH, 
)
from file_handler import (
    read_bookmark_collection_readme,
    read_summarized_bookmarks_data,
    write_text_content,
    write_summary_file,
    update_summary_readme,
    update_bookmarks_data,
    ensure_month_directory_exists,
)

# -- configurations begin --
BOOKMARK_COLLECTION_REPO_NAME: str = "bookmark-collection" # Stays here
NO_SUMMARY_TAG: str = "#nosummary"
# -- configurations end --

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(filename)s:%(lineno)d - %(funcName)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

# log_execution_time is now imported from external_services.py
# def log_execution_time(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         logging.info(f'Entering {func.__name__}')
#         start_time = time.time()
#         result = func(*args, **kwargs)
#         end_time = time.time()
#         elapsed_time = end_time - start_time
#         logging.info(f'Exiting {func.__name__} - Elapsed time: {elapsed_time:.4f} seconds')
#         return result
#     return wrapper

# SummarizedBookmark dataclass moved to core_logic.py
# CURRENT_MONTH, CURRENT_DATE, CURRENT_DATE_AND_TIME moved to core_logic.py
# Functions summarize_text, one_sentence_summary, slugify, 
# get_summary_file_path, get_text_content_path, build_summary_file, 
# build_summary_readme_md moved to core_logic.py

@log_execution_time
def process_bookmark_file():
    # Use file_handler to read bookmark collection README
    bookmark_lines: List[str] = read_bookmark_collection_readme(BOOKMARK_COLLECTION_REPO_NAME)

    # Use file_handler to read summarized bookmarks data
    data_json_path = Path(BOOKMARK_SUMMARY_REPO_NAME, 'data.json')
    summarized_bookmark_dicts = read_summarized_bookmarks_data(data_json_path)
    
    # SummarizedBookmark is imported from core_logic
    # Handle case where data.json might be empty or not found by file_handler
    if not summarized_bookmark_dicts:
        summarized_bookmarks = []
    else:
        summarized_bookmarks = [SummarizedBookmark(**bookmark) for bookmark in summarized_bookmark_dicts]

    summarized_urls = set([bookmark.url for bookmark in summarized_bookmarks])

    # find the first unprocessed && summary-not-present bookmark
    title: Optional[str] = None
    url: Optional[str] = None
    for line in bookmark_lines:
        # re is still imported and used here
        match: re.Match = re.search(r'- \[(.*?)\]\((.*?)\)', line)
        if match and match.group(2) not in summarized_urls:
            if NO_SUMMARY_TAG in line: # NO_SUMMARY_TAG is still a local config
                logging.debug(f"Skipping bookmark with {NO_SUMMARY_TAG} tag: {match.group(1)}")
                continue
            title, url = match.groups()
            break

    if title and url:
        # Ensure month directory exists using file_handler
        month_dir_path = Path(BOOKMARK_SUMMARY_REPO_NAME, CURRENT_MONTH)
        ensure_month_directory_exists(month_dir_path)

        # process the bookmark
        submit_to_wayback_machine(url) # From external_services
        text_content: str = get_text_content(url) # From external_services
        
        # summarize_text and one_sentence_summary are now imported from core_logic
        summary: str = summarize_text(text_content)
        one_sentence: str = one_sentence_summary(summary)
        
        # build_summary_file is now imported from core_logic
        # CURRENT_DATE_AND_TIME is defined in core_logic and used by build_summary_file
        summary_file_content: str = build_summary_file(title, url, summary, one_sentence)
        
        timestamp = int(datetime.now().timestamp()) # datetime is still imported
        
        # Use file_handler to write text content
        text_content_file_path = get_text_content_path(title) # from core_logic
        write_text_content(text_content_file_path, text_content)

        # Use file_handler to write summary file
        summary_file_path_val = get_summary_file_path(title, timestamp=timestamp) # from core_logic
        write_summary_file(summary_file_path_val, summary_file_content)
        
        # Update list of summarized bookmarks
        summarized_bookmarks.append(SummarizedBookmark(
            month=CURRENT_MONTH, # CURRENT_MONTH from core_logic
            title=title,
            url=url,
            timestamp=timestamp
        ))

        # Use file_handler to update summary README
        summary_readme_path = Path(BOOKMARK_SUMMARY_REPO_NAME, 'README.md')
        readme_content = build_summary_readme_md(summarized_bookmarks) # from core_logic
        update_summary_readme(summary_readme_path, readme_content)

        # Use file_handler to update data.json
        bookmarks_data_for_json = [asdict(bookmark) for bookmark in summarized_bookmarks] # asdict from dataclasses
        update_bookmarks_data(data_json_path, bookmarks_data_for_json)

def main():
    process_bookmark_file()

if __name__ == "__main__":
    main()