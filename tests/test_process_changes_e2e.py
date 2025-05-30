import unittest
from unittest.mock import patch, mock_open, call, MagicMock
import sys
import os
from pathlib import Path
import json
from urllib.parse import quote # Needed for README assertion
from datetime import datetime # Needed for fromtimestamp

# Add the parent directory to sys.path to allow imports
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Import the main function/script to test and its dependencies
import process_changes
import core_logic # Make sure core_logic module itself is imported
from core_logic import SummarizedBookmark # For constructing expected objects

# Original constants from modules that might be needed for assertions
ORIG_BOOKMARK_COLLECTION_REPO_NAME = process_changes.BOOKMARK_COLLECTION_REPO_NAME
ORIG_NO_SUMMARY_TAG = process_changes.NO_SUMMARY_TAG
# process_changes.py imports BOOKMARK_SUMMARY_REPO_NAME from core_logic directly into its namespace
ORIG_CORE_BOOKMARK_SUMMARY_REPO_NAME = process_changes.BOOKMARK_SUMMARY_REPO_NAME

class TestProcessChangesE2E(unittest.TestCase):

    def setUp(self):
        # Store and mock constants at their correct module locations
        # CURRENT_MONTH is imported into process_changes.py and also used by core_logic.py
        self.original_pc_current_month = process_changes.CURRENT_MONTH
        process_changes.CURRENT_MONTH = '202307'
        
        self.original_cl_current_month = core_logic.CURRENT_MONTH # Store original core_logic.CURRENT_MONTH
        core_logic.CURRENT_MONTH = '202307' # Mock core_logic.CURRENT_MONTH

        # CURRENT_DATE is used by core_logic.get_text_content_path
        self.original_cl_current_date = core_logic.CURRENT_DATE
        core_logic.CURRENT_DATE = '2023-07-25'
        
        # CURRENT_DATE_AND_TIME is used by core_logic.build_summary_file
        self.original_cl_current_date_and_time = core_logic.CURRENT_DATE_AND_TIME
        core_logic.CURRENT_DATE_AND_TIME = '2023-07-25 10:00:00'
        

    def tearDown(self):
        # Restore original date/time constants
        process_changes.CURRENT_MONTH = self.original_pc_current_month
        core_logic.CURRENT_MONTH = self.original_cl_current_month # Restore core_logic.CURRENT_MONTH
        core_logic.CURRENT_DATE = self.original_cl_current_date
        core_logic.CURRENT_DATE_AND_TIME = self.original_cl_current_date_and_time


    @patch('process_changes.read_bookmark_collection_readme')
    @patch('process_changes.read_summarized_bookmarks_data')
    @patch('process_changes.write_text_content')
    @patch('process_changes.write_summary_file')
    @patch('process_changes.update_summary_readme')
    @patch('process_changes.update_bookmarks_data')
    @patch('process_changes.ensure_month_directory_exists')
    @patch('process_changes.submit_to_wayback_machine')
    @patch('process_changes.get_text_content')
    @patch('process_changes.summarize_text') 
    @patch('process_changes.one_sentence_summary')
    @patch('process_changes.datetime') # Because process_changes.py uses `from datetime import datetime` and then `datetime.now()`
    def test_process_new_bookmark(
        self, mock_pc_datetime, mock_pc_one_sentence_summary, mock_pc_summarize_text,
        mock_pc_get_text_content, mock_pc_submit_to_wayback, mock_pc_ensure_dir,
        mock_pc_update_bookmarks_data, mock_pc_update_summary_readme,
        mock_pc_write_summary_file, mock_pc_write_text_content,
        mock_pc_read_summarized_data, mock_pc_read_collection_readme
    ):
        # --- Arrange ---
        # Mock inputs from file_handler (now accessed via process_changes namespace)
        mock_pc_read_collection_readme.return_value = [
            "- [Existing Bookmark](http://example.com/existing)",
            "- [New Bookmark Title](http://example.com/new-url)"
        ]
        mock_pc_read_summarized_data.return_value = [
            {"month": "202306", "title": "Existing Bookmark", "url": "http://example.com/existing", "timestamp": 1686787200}
        ]

        # Mock outputs from external_services and core_logic's summarization (now accessed via process_changes namespace)
        mock_pc_get_text_content.return_value = "This is the full text content of the new bookmark."
        mock_pc_summarize_text.return_value = "This is the detailed summary."
        mock_pc_one_sentence_summary.return_value = "This is the TL;DR."
        mock_pc_submit_to_wayback.return_value = None 
        mock_pc_ensure_dir.return_value = None

        # Mock datetime.now() for a predictable timestamp (now accessed via process_changes.datetime)
        mock_now = MagicMock()
        # Ensure the timestamp is an integer, as it would be from datetime.now().timestamp()
        mock_now.timestamp.return_value = 1690279200 
        mock_pc_datetime.now.return_value = mock_now
        
        # Expected path constants based on mocked dates in setUp
        expected_month_str = process_changes.CURRENT_MONTH # Mocked in process_changes
        expected_date_str = core_logic.CURRENT_DATE      # Mocked in core_logic
        expected_datetime_str = core_logic.CURRENT_DATE_AND_TIME # Mocked in core_logic
        expected_title_slug = "new-bookmark-title" # from core_logic.slugify("New Bookmark Title")

        # --- Act ---
        process_changes.process_bookmark_file()

        # --- Assert ---
        mock_pc_submit_to_wayback.assert_called_once_with("http://example.com/new-url")
        mock_pc_get_text_content.assert_called_once_with("http://example.com/new-url")
        mock_pc_summarize_text.assert_called_once_with("This is the full text content of the new bookmark.")
        mock_pc_one_sentence_summary.assert_called_once_with("This is the detailed summary.")

        expected_month_dir = Path(ORIG_CORE_BOOKMARK_SUMMARY_REPO_NAME, expected_month_str)
        mock_pc_ensure_dir.assert_called_once_with(expected_month_dir)

        expected_raw_text_path = Path(ORIG_CORE_BOOKMARK_SUMMARY_REPO_NAME, expected_month_str, f"{expected_date_str}-{expected_title_slug}_raw.md")
        mock_pc_write_text_content.assert_called_once_with(expected_raw_text_path, "This is the full text content of the new bookmark.")

        self.assertEqual(mock_pc_write_summary_file.call_count, 1)
        args_summary_file, _ = mock_pc_write_summary_file.call_args
        written_summary_path = args_summary_file[0]
        written_summary_content = args_summary_file[1]

        # Path for summary: <BOOKMARK_SUMMARY_REPO_NAME>/<CURRENT_MONTH>/<YYYY-MM-DD>-<slug>.md
        # The date in the filename comes from the timestamp
        timestamp_date_str = datetime.fromtimestamp(int(mock_now.timestamp())).strftime('%Y-%m-%d') # Ensure int for fromtimestamp
        self.assertEqual(written_summary_path, Path(ORIG_CORE_BOOKMARK_SUMMARY_REPO_NAME, expected_month_str, f"{timestamp_date_str}-{expected_title_slug}.md"))
        
        link_to_raw_text = Path('.', f"{expected_date_str}-{expected_title_slug}_raw.md")
        
        # Using a sequence of f-strings as requested
        expected_summary_file_content = (
            f"# New Bookmark Title\n"
            f"- URL: http://example.com/new-url\n"
            f"- Added At: {expected_datetime_str}\n" 
            f"- [Link To Text]({link_to_raw_text})\n\n"
            f"## TL;DR\n"
            f"This is the TL;DR.\n\n"
            f"## Summary\n"
            f"This is the detailed summary.\n"
        )
        self.assertEqual(written_summary_content, expected_summary_file_content)

        self.assertEqual(mock_pc_update_bookmarks_data.call_count, 1)
        args_data_json, _ = mock_pc_update_bookmarks_data.call_args
        written_data_json_path = args_data_json[0]
        written_data_json_content = args_data_json[1]
        
        self.assertEqual(written_data_json_path, Path(ORIG_CORE_BOOKMARK_SUMMARY_REPO_NAME, 'data.json'))
        self.assertEqual(len(written_data_json_content), 2)
        self.assertEqual(written_data_json_content[1]['title'], "New Bookmark Title")
        self.assertEqual(written_data_json_content[1]['url'], "http://example.com/new-url")
        self.assertEqual(written_data_json_content[1]['month'], expected_month_str)
        self.assertEqual(written_data_json_content[1]['timestamp'], int(mock_now.timestamp())) # Ensure int for comparison

        self.assertEqual(mock_pc_update_summary_readme.call_count, 1)
        args_readme, _ = mock_pc_update_summary_readme.call_args
        written_readme_path = args_readme[0]
        written_readme_content = args_readme[1]

        self.assertEqual(written_readme_path, Path(ORIG_CORE_BOOKMARK_SUMMARY_REPO_NAME, 'README.md'))
        self.assertIn("New Bookmark Title", written_readme_content)
        self.assertIn("Existing Bookmark", written_readme_content)
        # The date in the link also comes from the timestamp
        self.assertIn(f"({timestamp_date_str}) [New Bookmark Title]({Path('.', expected_month_str, f'{timestamp_date_str}-{quote(expected_title_slug)}.md')})", written_readme_content)

if __name__ == '__main__':
    unittest.main()
