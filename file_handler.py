import json
import logging
from pathlib import Path
from typing import List, Dict # Changed from List[dict] to List[Dict] for consistency

from external_services import log_execution_time

# Configure basic logging if not already configured by other modules
# This is important if file_handler.py could be run or tested independently.
if not logging.getLogger().hasHandlers():
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(filename)s:%(lineno)d - %(funcName)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

@log_execution_time
def read_bookmark_collection_readme(repo_path: str) -> List[str]:
    """Reads the README.md file from the bookmark collection repository."""
    readme_path = Path(repo_path, "README.md")
    try:
        with open(readme_path, 'r', encoding='utf-8') as f:
            return f.readlines()
    except FileNotFoundError:
        logging.error(f"README.md not found at {readme_path}")
        return [] # Or raise an exception, depending on desired error handling

@log_execution_time
def read_summarized_bookmarks_data(data_json_path: Path) -> List[Dict]:
    """Reads the data.json file containing summarized bookmark data."""
    try:
        with open(data_json_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        logging.warning(f"data.json not found at {data_json_path}, returning empty list.")
        return [] # Return empty list if not found, as process_changes.py handles this
    except json.JSONDecodeError:
        logging.error(f"Error decoding JSON from {data_json_path}, returning empty list.")
        return []


@log_execution_time
def write_text_content(file_path: Path, content: str):
    """Writes the raw text content to a file."""
    try:
        file_path.parent.mkdir(parents=True, exist_ok=True) # Ensure directory exists
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        logging.info(f"Text content written to {file_path}")
    except IOError as e:
        logging.error(f"Error writing text content to {file_path}: {e}")

@log_execution_time
def write_summary_file(file_path: Path, content: str):
    """Writes the summary content to a file."""
    try:
        file_path.parent.mkdir(parents=True, exist_ok=True) # Ensure directory exists
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        logging.info(f"Summary file written to {file_path}")
    except IOError as e:
        logging.error(f"Error writing summary file to {file_path}: {e}")

@log_execution_time
def update_summary_readme(readme_path: Path, content: str):
    """Updates the summary README.md file."""
    try:
        readme_path.parent.mkdir(parents=True, exist_ok=True) # Ensure directory exists
        with open(readme_path, 'w', encoding='utf-8') as f:
            f.write(content)
        logging.info(f"Summary README updated at {readme_path}")
    except IOError as e:
        logging.error(f"Error updating summary README at {readme_path}: {e}")

@log_execution_time
def update_bookmarks_data(data_json_path: Path, data: List[Dict]):
    """Updates the data.json file with the list of bookmark dictionaries."""
    try:
        data_json_path.parent.mkdir(parents=True, exist_ok=True) # Ensure directory exists
        with open(data_json_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        logging.info(f"Bookmarks data updated at {data_json_path}")
    except IOError as e:
        logging.error(f"Error updating bookmarks data at {data_json_path}: {e}")
    except TypeError as e: # Catch errors from json.dump if data is not serializable
        logging.error(f"TypeError during JSON serialization for {data_json_path}: {e}")


@log_execution_time
def ensure_month_directory_exists(dir_path: Path):
    """Ensures that the specified directory for the month exists."""
    try:
        dir_path.mkdir(parents=True, exist_ok=True)
        logging.info(f"Directory ensured at {dir_path}")
    except OSError as e:
        logging.error(f"Error creating directory at {dir_path}: {e}")
