import unittest
from pathlib import Path
from datetime import datetime
from urllib.parse import quote
import sys
import os

# Add the parent directory to sys.path to allow imports from core_logic, etc.
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# We need to import core_logic first before attempting to patch its attributes
import core_logic 
from core_logic import (
    slugify,
    get_summary_file_path,
    get_text_content_path,
    build_summary_file,
    build_summary_readme_md,
    SummarizedBookmark,
    # BOOKMARK_SUMMARY_REPO_NAME, # This will be accessed via core_logic module
    # CURRENT_MONTH, # Accessed via core_logic
    # CURRENT_DATE, # Accessed via core_logic
    # CURRENT_DATE_AND_TIME # Accessed via core_logic
)

# Need to import wraps for the mock decorator
from functools import wraps

class MockExternalServices:
    @staticmethod
    def log_execution_time(func):
        @wraps(func) # Make sure wraps is imported in the actual test file
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        return wrapper

    @staticmethod
    def call_openai_api(prompt: str, content: str) -> str:
        return "Mocked AI Summary"

# Apply mocks by patching the core_logic module directly
core_logic.external_services = MockExternalServices
core_logic.log_execution_time = MockExternalServices.log_execution_time
# If call_openai_api is directly used by core_logic, it should be patched there.
# Assuming it's used via external_services.call_openai_api, the above patch is enough.
# If core_logic itself imports call_openai_api directly like `from external_services import call_openai_api`
# then that specific import needs to be patched in core_logic's namespace.
# The current structure `from external_services import call_openai_api, log_execution_time` in core_logic.py
# means we need to patch these attributes in core_logic module if they are imported like that.

# Let's assume core_logic.py has:
# from external_services import call_openai_api, log_execution_time
# So we patch them in core_logic's namespace
core_logic.call_openai_api = MockExternalServices.call_openai_api
# log_execution_time is already patched above by core_logic.log_execution_time = ...


class TestCoreLogic(unittest.TestCase):

    def setUp(self):
        # Store original values
        self.original_bookmark_summary_repo_name = core_logic.BOOKMARK_SUMMARY_REPO_NAME
        self.original_current_month = core_logic.CURRENT_MONTH
        self.original_current_date = core_logic.CURRENT_DATE
        self.original_current_date_and_time = core_logic.CURRENT_DATE_AND_TIME

        # Set default test values (if different from runtime, or to ensure consistency)
        # These values are used by some of the core_logic functions under test.
        core_logic.CURRENT_MONTH = '202301'
        core_logic.CURRENT_DATE = '2023-01-15'
        core_logic.CURRENT_DATE_AND_TIME = '2023-01-15 12:30:00'


    def tearDown(self):
        # Restore original values
        core_logic.BOOKMARK_SUMMARY_REPO_NAME = self.original_bookmark_summary_repo_name
        core_logic.CURRENT_MONTH = self.original_current_month
        core_logic.CURRENT_DATE = self.original_current_date
        core_logic.CURRENT_DATE_AND_TIME = self.original_current_date_and_time

    def test_slugify(self):
        self.assertEqual(slugify("Hello World!"), "hello-world!") # Changed assertion
        self.assertEqual(slugify("This is a Test Title with /\\:*?\"<>|"), "this-is-a-test-title-with")
        self.assertEqual(slugify("  leading and trailing spaces  "), "leading-and-trailing-spaces")
        self.assertEqual(slugify("連続するスペース  と　全角スペース"), "連続するスペース-と-全角スペース")
        self.assertEqual(slugify(""), "")
        self.assertEqual(slugify("---"), "")
        self.assertEqual(slugify("test/"), "test") # Added assertion

    def test_get_summary_file_path(self):
        title = "Test Title"
        ts = int(datetime(2023, 1, 15, 12, 30, 0).timestamp())
        expected_slug = "test-title"
        # core_logic.CURRENT_MONTH is set in setUp to '202301'
        path = get_summary_file_path(title, ts)
        # BOOKMARK_SUMMARY_REPO_NAME should be its original value here due to setUp/tearDown
        self.assertEqual(path, Path(self.original_bookmark_summary_repo_name, "202301", f"2023-01-15-{expected_slug}.md"))

        path_readme = get_summary_file_path(title, ts, month="202301", in_readme_md=True)
        self.assertEqual(path_readme, Path(".", "202301", f"2023-01-15-{quote(expected_slug)}.md"))

    def test_get_text_content_path(self):
        title = "Another Test"
        # core_logic.CURRENT_DATE and core_logic.CURRENT_MONTH are set in setUp
        path = get_text_content_path(title)
        # BOOKMARK_SUMMARY_REPO_NAME should be its original value here
        self.assertEqual(path, Path(self.original_bookmark_summary_repo_name, "202301", f"2023-01-15-{slugify(title)}_raw.md"))

        path_in_summary = get_text_content_path(title, in_summary_md=True)
        # CURRENT_DATE is '2023-01-15' from setUp
        self.assertEqual(path_in_summary, Path(".", f"2023-01-15-{slugify(title)}_raw.md"))


    def test_build_summary_file(self):
        # core_logic.CURRENT_DATE_AND_TIME, CURRENT_DATE, CURRENT_MONTH are set in setUp
        title = "My Awesome Article"
        url = "http://example.com/article"
        summary = "This is a great summary."
        one_sentence = "Awesome article!"
        
        raw_text_path = get_text_content_path(title, in_summary_md=True) # Relies on CURRENT_DATE, CURRENT_MONTH from setUp

        content = build_summary_file(title, url, summary, one_sentence) # Relies on CURRENT_DATE_AND_TIME from setUp
        self.assertIn(f"# {title}", content)
        self.assertIn(f"- URL: {url}", content)
        self.assertIn(f"- Added At: {core_logic.CURRENT_DATE_AND_TIME}", content) # This is '2023-01-15 12:30:00' from setUp
        self.assertIn(f"- [Link To Text]({raw_text_path})", content)
        self.assertIn(f"## TL;DR\n{one_sentence}", content)
        self.assertIn(f"## Summary\n{summary}", content)

    def test_build_summary_readme_md(self):
        # Temporarily change BOOKMARK_SUMMARY_REPO_NAME for this test
        # This change will be reverted by tearDown
        core_logic.BOOKMARK_SUMMARY_REPO_NAME = "test-summary-repo" 
        
        bookmarks = [
            SummarizedBookmark(month="202301", title="Older Post", url="http://example.com/old", timestamp=int(datetime(2023,1,10).timestamp())),
            SummarizedBookmark(month="202301", title="Newer Post", url="http://example.com/new", timestamp=int(datetime(2023,1,15).timestamp())),
        ]
        
        # core_logic.CURRENT_MONTH is '202301' from setUp
        # get_summary_file_path uses the mocked BOOKMARK_SUMMARY_REPO_NAME for this test when in_readme_md=False
        # but for in_readme_md=True, the root is Path("."), so BOOKMARK_SUMMARY_REPO_NAME is not used in path construction.
        path_new = get_summary_file_path("Newer Post", bookmarks[1].timestamp, month="202301", in_readme_md=True)
        path_old = get_summary_file_path("Older Post", bookmarks[0].timestamp, month="202301", in_readme_md=True)

        readme_content = build_summary_readme_md(bookmarks)
        
        self.assertIn(f"- (2023-01-15) [Newer Post]({path_new})", readme_content)
        self.assertIn(f"- (2023-01-10) [Older Post]({path_old})", readme_content)
        self.assertTrue(readme_content.find("Newer Post") < readme_content.find("Older Post"))
        
        # The tearDown method will restore the original BOOKMARK_SUMMARY_REPO_NAME

    def test_summarize_text_mocked(self):
        result = core_logic.summarize_text("Some long text")
        self.assertEqual(result, "Mocked AI Summary")

    def test_one_sentence_summary_mocked(self):
        result = core_logic.one_sentence_summary("Some summary text")
        self.assertEqual(result, "Mocked AI Summary")

if __name__ == '__main__':
    unittest.main()
