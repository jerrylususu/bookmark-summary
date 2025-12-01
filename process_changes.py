import argparse
import json
import logging
import os
import re
import time
from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from functools import wraps
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Tuple
from urllib.parse import quote

# Optional dependency: enables more robust Markdown parsing when present. Falls back
# to a regex-based parser when unavailable so backfill/dry-run still work without it.
try:
    import mistune
except ImportError:  # pragma: no cover - fallback when optional dependency missing
    mistune = None  # type: ignore[assignment]

# Required for network operations (fetching article content via Jina reader and
# calling OpenAI). Backfill mode can run without it because no new content is fetched.
try:
    import requests
except ImportError:  # pragma: no cover - fallback when optional dependency missing
    requests = None  # type: ignore[assignment]

# Optional: lets us snapshot URLs in the Wayback Machine. Workflow continues if
# missing; we simply skip archival when summarizing new bookmarks.
try:
    from waybackpy import WaybackMachineSaveAPI
except ImportError:  # pragma: no cover - fallback when optional dependency missing
    WaybackMachineSaveAPI = None  # type: ignore[assignment]

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
    format="%(asctime)s - %(filename)s:%(lineno)d - %(funcName)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)


def log_execution_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        logging.info("Entering %s", func.__name__)
        start_time = time.time()
        result = func(*args, **kwargs)
        elapsed_time = time.time() - start_time
        logging.info("Exiting %s - Elapsed time: %.4f seconds", func.__name__, elapsed_time)
        return result

    return wrapper


@dataclass
class SummarizedBookmark:
    month: str  # yyyyMM
    title: str
    url: str
    timestamp: int  # unix timestamp
    tags: List[str] = field(default_factory=list)


@dataclass
class IngestionResult:
    bookmark: SummarizedBookmark
    summary_markdown: str
    raw_text: str
    summary_path: Path
    raw_path: Path
    one_sentence: str


CURRENT_MONTH: str = datetime.now(timezone.utc).strftime("%Y%m")
CURRENT_DATE: str = datetime.now(timezone.utc).strftime("%Y-%m-%d")
CURRENT_DATE_AND_TIME: str = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S")

SUMMARY_ROOT = Path(BOOKMARK_SUMMARY_REPO_NAME)
if not SUMMARY_ROOT.exists():
    SUMMARY_ROOT = Path(".")

DATA_PATH = SUMMARY_ROOT / "data.json"
SUMMARY_README_PATH = SUMMARY_ROOT / "README.md"

COLLECTION_ROOT = Path(BOOKMARK_COLLECTION_REPO_NAME)
COLLECTION_README_PATH = COLLECTION_ROOT / "README.md"


def ensure_directory(path: Path, dry_run: bool = False) -> None:
    if dry_run:
        logging.info("Dry-run: would ensure directory %s", path)
        return
    path.mkdir(parents=True, exist_ok=True)


def format_month(month: str) -> str:
    try:
        return datetime.strptime(month, "%Y%m").strftime("%Y-%m")
    except ValueError:
        return month


def normalize_tag(tag: str) -> str:
    return tag if tag.startswith("#") else f"#{tag}"


def format_tags(tags: Iterable[str]) -> str:
    return " ".join(normalize_tag(tag.strip()) for tag in tags if tag.strip())


def bookmark_identity(bookmark: SummarizedBookmark) -> Tuple[str, str, int]:
    return (bookmark.month, bookmark.title, bookmark.timestamp)


def write_text_file(path: Path, content: str, dry_run: bool = False) -> None:
    if dry_run:
        logging.info(
            "Dry-run: would write %s (%d bytes)", path, len(content.encode("utf-8"))
        )
        return
    ensure_directory(path.parent, dry_run=False)
    with path.open("w", encoding="utf-8") as handle:
        handle.write(content)


def load_summarized_bookmarks() -> List[SummarizedBookmark]:
    if not DATA_PATH.exists():
        logging.info("No data.json found at %s, starting with empty dataset.", DATA_PATH)
        return []

    with DATA_PATH.open("r", encoding="utf-8") as handle:
        raw_entries = json.load(handle)

    bookmarks: List[SummarizedBookmark] = []
    for entry in raw_entries:
        tags = entry.get("tags") or []
        bookmarks.append(
            SummarizedBookmark(
                month=entry["month"],
                title=entry["title"],
                url=entry["url"],
                timestamp=entry["timestamp"],
                tags=tags,
            )
        )
    return bookmarks


def save_summarized_bookmarks(
    bookmarks: Iterable[SummarizedBookmark], dry_run: bool = False
) -> None:
    payload = [asdict(bookmark) for bookmark in bookmarks]
    if dry_run:
        logging.info(
            "Dry-run: would write %s with %d entries.", DATA_PATH, len(payload)
        )
        return

    ensure_directory(DATA_PATH.parent, dry_run=False)
    with DATA_PATH.open("w", encoding="utf-8") as handle:
        json.dump(payload, handle, indent=2, ensure_ascii=False)


def read_bookmark_collection_lines() -> List[str]:
    if not COLLECTION_README_PATH.exists():
        logging.warning(
            "'%s' not found; skipping new bookmark ingestion.",
            COLLECTION_README_PATH,
        )
        return []

    with COLLECTION_README_PATH.open("r", encoding="utf-8") as handle:
        return handle.readlines()


def extract_tags_from_line(line: str) -> List[str]:
    closing_paren_index = line.find(")")
    if closing_paren_index == -1:
        return []
    trailing = line[closing_paren_index + 1 :]
    raw_tags = re.findall(r"#([^\s#]+)", trailing)

    tags: List[str] = []
    nosummary = NO_SUMMARY_TAG.lstrip("#")
    for raw_tag in raw_tags:
        cleaned = raw_tag.strip().rstrip(",.;:!?")
        if not cleaned or cleaned == nosummary:
            continue
        tags.append(cleaned)
    return tags


def build_url_tag_lookup(bookmark_lines: Iterable[str]) -> Dict[str, List[str]]:
    lookup: Dict[str, List[str]] = {}
    for line in bookmark_lines:
        match = re.search(r"-\s*\[(.*?)\]\((.*?)\)", line)
        if not match:
            continue
        url = match.group(2).strip()
        lookup[url] = extract_tags_from_line(line)
    return lookup


def slugify(text: str) -> str:
    invalid_fs_chars: str = '/\\:*?"<>|'
    return re.sub(r"[" + re.escape(invalid_fs_chars) + r"\s]+", "-", text.lower()).strip("-")


def get_summary_file_path(
    title: str,
    timestamp: int,
    month: Optional[str] = None,
    in_readme_md: bool = False,
) -> Path:
    date_str = datetime.fromtimestamp(timestamp, tz=timezone.utc).strftime("%Y-%m-%d")
    summary_filename: str = f"{date_str}-{slugify(title)}.md"
    if in_readme_md:
        if month is None:
            raise ValueError("Month must be provided when in_readme_md is True")
        root = Path(month)
        summary_filename = f"{date_str}-{quote(slugify(title))}.md"
    else:
        if month is None:
            month = datetime.fromtimestamp(timestamp, tz=timezone.utc).strftime("%Y%m")
        root = SUMMARY_ROOT / month
    return root / summary_filename


def get_text_content_path(
    title: str,
    month: Optional[str] = None,
    in_summary_md: bool = False,
) -> Path:
    text_content_filename: str = f"{CURRENT_DATE}-{slugify(title)}_raw.md"
    if in_summary_md:
        root = Path(".")
    else:
        if month is None:
            month = CURRENT_MONTH
        root = SUMMARY_ROOT / month
    return Path(root, text_content_filename)


def build_summary_file(
    title: str,
    url: str,
    summary: str,
    one_sentence: str,
    tags: List[str],
    month: str,
) -> str:
    tag_line = ""
    if tags:
        tag_line = f"- Tags: {format_tags(tags)}\n"

    link_to_text = get_text_content_path(title, month=month, in_summary_md=True).name
    return (
        f"# {title}\n"
        f"- URL: {url}\n"
        f"- Added At: {CURRENT_DATE_AND_TIME}\n"
        f"{tag_line}- [Link To Text]({link_to_text})\n\n"
        f"## TL;DR\n{one_sentence}\n\n"
        f"## Summary\n{summary}\n"
    )


@log_execution_time
def submit_to_wayback_machine(url: str):
    if WaybackMachineSaveAPI is None:
        logging.info(
            "WaybackMachineSaveAPI not available; skipping submission for %s.",
            url,
        )
        return

    user_agent = (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"
    )
    try:
        save_api = WaybackMachineSaveAPI(url, user_agent)
        wayback_url = save_api.save()
        logging.info("Wayback Saved: %s", wayback_url)
    except Exception as error:  # noqa: BLE001 - allow any failure without raising
        logging.warning(
            "submit to wayback machine failed, skipping, url=%s", url
        )
        logging.exception(error)


@log_execution_time
def get_text_content(url: str) -> str:
    if requests is None:
        raise RuntimeError("requests package not available; cannot fetch content.")

    jina_url: str = f"https://r.jina.ai/{url}"

    for attempt in range(MAX_RETRIES):
        try:
            response: requests.Response = requests.get(jina_url)
            content = response.text.strip()

            if len(content) < MIN_CONTENT_LENGTH:
                if "upstream connect error" in content.lower() or "connection termination" in content.lower():
                    error_msg = f"Connection error detected (attempt {attempt + 1}/{MAX_RETRIES})"
                else:
                    error_msg = (
                        f"Content too short ({len(content)} chars, minimum {MIN_CONTENT_LENGTH}) "
                        f"- attempt {attempt + 1}/{MAX_RETRIES}"
                    )

                logging.warning(error_msg)

                if attempt < MAX_RETRIES - 1:
                    wait_time = 2**attempt
                    logging.info("Retrying in %d seconds...", wait_time)
                    time.sleep(wait_time)
                    continue
                raise Exception(
                    f"All {MAX_RETRIES} retry attempts failed. Last error: {error_msg}"
                )

            if len(content) > MAX_CONTENT_LENGTH:
                logging.warning(
                    "Content length (%d) exceeds maximum (%d), truncating...",
                    len(content),
                    MAX_CONTENT_LENGTH,
                )
                content = content[:MAX_CONTENT_LENGTH]

            logging.info("Successfully fetched content with %d characters", len(content))
            return content

        except requests.RequestException as error:
            logging.warning(
                "Request failed (attempt %d/%d): %s",
                attempt + 1,
                MAX_RETRIES,
                error,
            )
            if attempt < MAX_RETRIES - 1:
                wait_time = 2**attempt
                logging.info("Retrying in %d seconds...", wait_time)
                time.sleep(wait_time)
            else:
                raise Exception(
                    f"All {MAX_RETRIES} retry attempts failed. Last error: {error}"
                ) from error


@log_execution_time
def call_openai_api(prompt: str, content: str) -> str:
    if requests is None:
        raise RuntimeError("requests package not available; cannot call OpenAI API.")

    model: str = os.environ.get("OPENAI_API_MODEL", "gpt-4o-mini")
    headers: dict = {
        "Authorization": f"Bearer {os.environ['OPENAI_API_KEY']}",
        "Content-Type": "application/json",
    }
    data: dict = {
        "model": model,
        "messages": [
            {"role": "system", "content": prompt},
            {"role": "user", "content": content},
        ],
    }
    api_endpoint: str = os.environ.get(
        "OPENAI_API_ENDPOINT", "https://api.openai.com/v1/chat/completions"
    )

    logging.info("Calling OpenAI API with model: %s", model)
    logging.info("API endpoint: %s", api_endpoint)

    response: requests.Response = requests.post(
        api_endpoint, headers=headers, data=json.dumps(data)
    )

    logging.info("Response status code: %d", response.status_code)
    response_json = response.json()
    logging.debug("Response content: %s", json.dumps(response_json, ensure_ascii=False))

    if response.status_code != 200:
        error_msg = f"OpenAI API request failed with status {response.status_code}"
        logging.error(error_msg)
        logging.error("Error response: %s", response_json)
        raise Exception(error_msg)

    if "choices" not in response_json:
        error_msg = "Response does not contain 'choices' field"
        logging.error(error_msg)
        logging.error("Full response: %s", response_json)
        raise Exception(error_msg)

    return response_json["choices"][0]["message"]["content"]


@log_execution_time
def summarize_text(text: str) -> str:
    prompt: str = """
结构化总结这篇文章。输出时使用简体中文。
输出时直接给出总结内容，不需要附带“以下是总结”的开始文字或额外的标题。
"""
    return call_openai_api(prompt, text)


@log_execution_time
def one_sentence_summary(text: str) -> str:
    prompt: str = (
        "以下是对一篇长文的列表形式总结。"
        "请基于此输出对该文章的简短总结，长度不超过100个字。总是使用简体中文输出。"
    )
    return call_openai_api(prompt, text)


def extract_tldr_from_markdown(file_path: str) -> str:
    def extract_tldr_with_regex(content: str) -> str:
        match = re.search(r"##\s*TL;DR\s+(.*?)\n##\s", content, re.DOTALL)
        if not match:
            match = re.search(r"##\s*TL;DR\s+(.*)", content, re.DOTALL)
        if not match:
            return ""
        extracted = match.group(1).strip()
        return re.sub(r"\s+", " ", extracted)

    try:
        with open(file_path, "r", encoding="utf-8") as handle:
            content = handle.read()
    except Exception as error:  # noqa: BLE001 - tolerate read failures
        logging.warning("Could not read TL;DR from %s: %s", file_path, error)
        return ""

    if not content:
        return ""

    if mistune is None:
        return extract_tldr_with_regex(content)

    try:
        markdown = mistune.create_markdown(renderer=None)
        ast = markdown(content)
    except Exception as error:  # noqa: BLE001 - fallback to regex parser
        logging.warning(
            "Mistune parsing failed for %s: %s. Falling back to regex parser.",
            file_path,
            error,
        )
        return extract_tldr_with_regex(content)

    tldr_content: List[str] = []
    found_tldr = False

    for token in ast:
        if token["type"] == "heading" and token.get("attrs", {}).get("level") == 2:
            if "TL;DR" in str(token.get("children", [])):
                found_tldr = True
                continue
            if found_tldr:
                break
        elif found_tldr and token["type"] == "paragraph":
            def extract_text(children):
                parts: List[str] = []
                for child in children:
                    if child["type"] == "text":
                        parts.append(child["raw"])
                    elif "children" in child:
                        parts.extend(extract_text(child["children"]))
                return parts

            text_parts = extract_text(token.get("children", []))
            tldr_content.append("".join(text_parts))

    if not tldr_content:
        return extract_tldr_with_regex(content)

    return "\n".join(tldr_content).strip()


def render_bookmark_lines(
    bookmark: SummarizedBookmark,
    link: str,
    tldr: str,
) -> List[str]:
    date_str = datetime.fromtimestamp(
        bookmark.timestamp, tz=timezone.utc
    ).strftime("%Y-%m-%d")
    lines = [f"- ({date_str}) [{bookmark.title}]({link})"]
    if tldr:
        lines.append(f"  - {tldr}")
    if bookmark.tags:
        lines.append(f"  - Tags: {format_tags(bookmark.tags)}")
    return lines


def build_monthly_index_markdown(
    month: str,
    bookmarks: List[SummarizedBookmark],
    tldr_lookup: Dict[Tuple[str, str, int], str],
) -> str:
    lines: List[str] = [f"# {format_month(month)} Monthly Index", ""]

    for bookmark in bookmarks:
        link = get_summary_file_path(
            title=bookmark.title,
            timestamp=bookmark.timestamp,
            month=bookmark.month,
            in_readme_md=True,
        ).name
        key = bookmark_identity(bookmark)
        lines.extend(render_bookmark_lines(bookmark, link, tldr_lookup.get(key, "")))
        lines.append("")

    return "\n".join(lines).strip() + "\n"


def build_summary_readme_md(
    summarized_bookmarks: List[SummarizedBookmark],
    grouped_bookmarks: Dict[str, List[SummarizedBookmark]],
    tldr_lookup: Dict[Tuple[str, str, int], str],
) -> str:
    initial_prefix = """# Bookmark Summary 
读取 bookmark-collection 中的书签，使用 jina reader 获取文本内容，然后使用 LLM 总结文本。详细实现请参见 process_changes.py。需要和 bookmark-collection 中的 Github Action 一起使用。
"""

    lines: List[str] = [initial_prefix.rstrip(), "", "## Latest 10 Summaries", ""]

    latest_entries = sorted(
        summarized_bookmarks, key=lambda b: b.timestamp, reverse=True
    )[:10]
    if latest_entries:
        for bookmark in latest_entries:
            link = get_summary_file_path(
                title=bookmark.title,
                timestamp=bookmark.timestamp,
                month=bookmark.month,
                in_readme_md=True,
            ).as_posix()
            key = bookmark_identity(bookmark)
            lines.extend(render_bookmark_lines(bookmark, link, tldr_lookup.get(key, "")))
            lines.append("")
    else:
        lines.append("- _No summaries available yet._")
        lines.append("")

    lines.append("## Monthly Archive")
    lines.append("")

    sorted_months = sorted(grouped_bookmarks.keys(), reverse=True)
    if sorted_months:
        for month in sorted_months:
            link = Path(month, "monthly-index.md").as_posix()
            count = len(grouped_bookmarks[month])
            lines.append(f"- [{format_month(month)}]({link}) ({count} entries)")
    else:
        lines.append("- _Archive will appear after the first summary._")

    return "\n".join(lines).strip() + "\n"


def build_all_summary_md(
    summarized_bookmarks: List[SummarizedBookmark],
    tldr_lookup: Dict[Tuple[str, str, int], str],
) -> str:
    lines: List[str] = [
        "# All Bookmarks Summary",
        "",
    ]

    for bookmark in sorted(summarized_bookmarks, key=lambda b: b.timestamp, reverse=True):
        date_str = datetime.fromtimestamp(
            bookmark.timestamp, tz=timezone.utc
        ).strftime("%Y-%m-%d")
        key = bookmark_identity(bookmark)
        tldr = tldr_lookup.get(key, "").strip()
        tags_str = format_tags(bookmark.tags) if bookmark.tags else ""

        summary_file_path = get_summary_file_path(
            title=bookmark.title,
            timestamp=bookmark.timestamp,
            month=bookmark.month,
            in_readme_md=True,
        )
        github_link = summary_file_path.as_posix()

        title_with_link = f"[{bookmark.title}]({github_link})"

        lines.append(f"- ({date_str}) {title_with_link}")
        if tags_str:
            lines.append(f"  - Tags: {tags_str}")
        if tldr:
            lines.append(f"  - Summary: {tldr}")
        lines.append("")

    return "\n".join(lines).strip() + "\n"


def collect_tldrs(
    bookmarks: Iterable[SummarizedBookmark],
    overrides: Optional[Dict[Tuple[str, str, int], str]] = None,
) -> Dict[Tuple[str, str, int], str]:
    overrides = overrides or {}
    lookup: Dict[Tuple[str, str, int], str] = {}

    for bookmark in bookmarks:
        key = bookmark_identity(bookmark)
        if key in overrides:
            lookup[key] = overrides[key]
            continue

        summary_file_path = get_summary_file_path(
            title=bookmark.title,
            timestamp=bookmark.timestamp,
            month=bookmark.month,
            in_readme_md=False,
        )
        lookup[key] = extract_tldr_from_markdown(str(summary_file_path))

    return lookup


def group_bookmarks_by_month(
    bookmarks: Iterable[SummarizedBookmark],
) -> Dict[str, List[SummarizedBookmark]]:
    grouped: Dict[str, List[SummarizedBookmark]] = {}
    for bookmark in bookmarks:
        grouped.setdefault(bookmark.month, []).append(bookmark)

    for month in grouped:
        grouped[month].sort(key=lambda b: b.timestamp, reverse=True)

    return grouped


def write_monthly_indexes(
    grouped_bookmarks: Dict[str, List[SummarizedBookmark]],
    tldr_lookup: Dict[Tuple[str, str, int], str],
    dry_run: bool = False,
) -> None:
    for month in sorted(grouped_bookmarks.keys(), reverse=True):
        month_dir = SUMMARY_ROOT / month
        if not month_dir.exists():
            ensure_directory(month_dir, dry_run=dry_run)

        content = build_monthly_index_markdown(
            month=month,
            bookmarks=grouped_bookmarks[month],
            tldr_lookup=tldr_lookup,
        )
        output_path = month_dir / "monthly-index.md"
        write_text_file(output_path, content, dry_run=dry_run)


@log_execution_time
def process_bookmark_file():
    raise RuntimeError(
        "process_bookmark_file has been superseded by process_changes(). "
        "Invoke main() or process_changes() with explicit arguments."
    )


def find_next_bookmark_to_process(
    bookmark_lines: Iterable[str], summarized_urls: Iterable[str]
) -> Optional[Tuple[str, str, List[str]]]:
    summarized_url_set = set(summarized_urls)
    for line in bookmark_lines:
        match: Optional[re.Match[str]] = re.search(r"-\s*\[(.*?)\]\((.*?)\)", line)
        if not match:
            continue

        title, url = match.groups()
        if url in summarized_url_set:
            continue
        if NO_SUMMARY_TAG in line:
            logging.debug(
                "Skipping bookmark with %s tag: %s", NO_SUMMARY_TAG, match.group(1)
            )
            continue

        tags = extract_tags_from_line(line)
        return title, url, tags

    return None


def ingest_bookmark(title: str, url: str, tags: List[str]) -> IngestionResult:
    submit_to_wayback_machine(url)
    text_content: str = get_text_content(url)
    summary: str = summarize_text(text_content)
    one_sentence: str = one_sentence_summary(summary)

    timestamp = int(datetime.now(timezone.utc).timestamp())
    month = datetime.fromtimestamp(timestamp, tz=timezone.utc).strftime("%Y%m")
    summary_file_content: str = build_summary_file(
        title, url, summary, one_sentence, tags, month
    )
    summary_path = get_summary_file_path(title, timestamp=timestamp, month=month)
    raw_path = get_text_content_path(title, month=month)

    bookmark = SummarizedBookmark(
        month=month,
        title=title,
        url=url,
        timestamp=timestamp,
        tags=tags,
    )
    return IngestionResult(
        bookmark=bookmark,
        summary_markdown=summary_file_content,
        raw_text=text_content,
        summary_path=summary_path,
        raw_path=raw_path,
        one_sentence=one_sentence,
    )


def process_changes(backfill: bool = False, dry_run: bool = False) -> None:
    summarized_bookmarks = load_summarized_bookmarks()
    summarized_urls = [bookmark.url for bookmark in summarized_bookmarks]

    bookmark_lines = read_bookmark_collection_lines()
    url_tag_lookup = build_url_tag_lookup(bookmark_lines)
    if url_tag_lookup:
        for bookmark in summarized_bookmarks:
            if bookmark.url in url_tag_lookup:
                bookmark.tags = url_tag_lookup[bookmark.url]

    overrides: Dict[Tuple[str, str, int], str] = {}

    ingestion_result: Optional[IngestionResult] = None
    # Backfill rebuilds derived files from stored bookmarks only. Dry-run keeps the
    # entire pipeline side-effect-free, so both branches skip ingesting fresh content.
    if backfill:
        logging.info(
            "Backfill mode enabled; rebuilding summaries/indexes from existing data only."
        )
    elif dry_run:
        logging.info(
            "Dry-run mode enabled; simulating pipeline without fetching new bookmarks or writing files."
        )
    elif requests is None:
        logging.warning(
            "requests dependency missing; cannot ingest new bookmarks. "
            "Run with --backfill or install optional dependencies."
        )
    else:
        next_bookmark = find_next_bookmark_to_process(bookmark_lines, summarized_urls)

        if next_bookmark:
            title, url, tags = next_bookmark
            logging.info("Processing new bookmark: %s", title)
            ingestion_result = ingest_bookmark(title, url, tags)
            summarized_bookmarks.append(ingestion_result.bookmark)

            if dry_run:
                logging.info(
                    "Dry-run: skipping writes for %s and %s",
                    ingestion_result.summary_path,
                    ingestion_result.raw_path,
                )
            else:
                write_text_file(
                    ingestion_result.summary_path,
                    ingestion_result.summary_markdown,
                    dry_run=False,
                )
                write_text_file(
                    ingestion_result.raw_path,
                    ingestion_result.raw_text,
                    dry_run=False,
                )

            overrides[bookmark_identity(ingestion_result.bookmark)] = (
                ingestion_result.one_sentence
            )
        else:
            logging.info("No new bookmarks to process.")

    save_summarized_bookmarks(summarized_bookmarks, dry_run=dry_run)

    grouped = group_bookmarks_by_month(summarized_bookmarks)
    tldr_lookup = collect_tldrs(
        summarized_bookmarks,
        overrides=overrides,
    )

    write_monthly_indexes(grouped, tldr_lookup, dry_run=dry_run)

    readme_content = build_summary_readme_md(
        summarized_bookmarks,
        grouped,
        tldr_lookup,
    )
    write_text_file(SUMMARY_README_PATH, readme_content, dry_run=dry_run)

    all_summary_content = build_all_summary_md(
        summarized_bookmarks,
        tldr_lookup,
    )
    all_summary_path = SUMMARY_ROOT / "all_summary.md"
    write_text_file(all_summary_path, all_summary_content, dry_run=dry_run)

    if dry_run:
        logging.info("Dry-run complete; no files were written.")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Update bookmark summaries.")
    parser.add_argument(
        "--backfill",
        action="store_true",
        help="Rebuild README and monthly indexes without ingesting new bookmarks.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Run the pipeline without writing changes to disk.",
    )
    args = parser.parse_args()

    env_dry_run = os.getenv("BOOKMARK_SUMMARY_DRY_RUN", "").lower() in (
        "1",
        "true",
        "yes",
    )
    if env_dry_run:
        args.dry_run = True

    return args


def main():
    args = parse_args()
    process_changes(backfill=args.backfill, dry_run=args.dry_run)


if __name__ == "__main__":
    main()
