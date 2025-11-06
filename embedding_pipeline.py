"""Utilities for preparing bookmark documents for embedding generation.

This module focuses on extracting relevant text segments (summary, TL;DR, raw
content chunks), computing stable hashes, and coordinating embedding requests.

It is intentionally stateless: callers are expected to provide storage and
orchestration layers (see `embedding_store.py` and `scripts/embedding_runner.py`).
"""

from __future__ import annotations

from collections import deque
from dataclasses import dataclass
from datetime import datetime, timedelta
import hashlib
import logging
import os
from pathlib import Path
import re
import time
from typing import Callable, Dict, Iterable, Iterator, List, Optional, Sequence, Set, Tuple

import numpy as np
import requests
from dotenv import load_dotenv

try:  # Optional but preferred for consistent chunking.
    import tiktoken
except Exception:  # pragma: no cover - fallback when tiktoken missing
    tiktoken = None  # type: ignore[assignment]

from process_changes import slugify  # Reuse existing slug logic for stability.


LOGGER = logging.getLogger(__name__)

DEFAULT_API_URL = "https://api.siliconflow.cn/v1/embeddings"
ENV_API_KEY = "SF_TOKEN"
ENV_EMBED_MODEL = "EMBED_MODEL"

# Chunking configuration tuned for BAAI/bge-m3 default token limits.
MAX_RAW_CHUNK_TOKENS = 700
RAW_CHUNK_OVERLAP = 100
SUMMARY_CHUNK_TOKENS = 400

DEFAULT_SPECIAL_TOKENS_AS_TEXT: Set[str] = {
    "<|fim_prefix|>",
    "<|fim_middle|>",
    "<|fim_suffix|>",
}


@dataclass(frozen=True)
class BookmarkMetadata:
    """Structured metadata for a bookmark entry sourced from data.json."""

    month: str
    title: str
    url: str
    timestamp: int
    tags: Tuple[str, ...]

    @property
    def slug(self) -> str:
        return slugify(self.title)

    @property
    def date_prefix(self) -> str:
        return time.strftime(
            "%Y-%m-%d", time.gmtime(self.timestamp)
        )  # data.json timestamp stored in UTC


@dataclass
class BookmarkDocument:
    """Represents the files backing a bookmark summary + raw article."""

    metadata: BookmarkMetadata
    summary_path: Path
    raw_path: Optional[Path]

    @property
    def document_id(self) -> str:
        """Stable identifier derived from month/timestamp/title slug."""
        meta = self.metadata
        return f"{meta.month}:{meta.timestamp}:{meta.slug}"


@dataclass
class ChunkInput:
    """A chunk that needs embedding."""

    document_id: str
    chunk_type: str  # "summary", "tldr", "raw"
    chunk_index: int
    heading: Optional[str]
    content: str
    token_count: int
    text_sha: str


@dataclass
class EmbeddingConfig:
    api_key: str
    model: str
    api_url: str = DEFAULT_API_URL
    request_timeout: int = 60
    max_batch: int = 16  # SiliconFlow allows up to 32; stay conservative.
    max_retries: int = 3
    retry_backoff: float = 2.0


class TokenSplitter:
    """Helper to measure token counts and break text into overlapping chunks."""

    def __init__(
        self,
        encoding_name: str = "cl100k_base",
        special_tokens_as_text: Optional[Iterable[str]] = None,
    ) -> None:
        self.encoding_name = encoding_name
        self._encoding = None
        tokens_as_text = (
            set(special_tokens_as_text)
            if special_tokens_as_text is not None
            else set(DEFAULT_SPECIAL_TOKENS_AS_TEXT)
        )
        self._disallowed_special: Set[str] = set()
        if tiktoken is not None:
            try:
                self._encoding = tiktoken.get_encoding(encoding_name)
            except Exception:  # pragma: no cover - invalid encoding name
                LOGGER.warning(
                    "Unable to load tiktoken encoding '%s'; falling back to char-based chunking.",
                    encoding_name,
                )
                self._encoding = None
        if self._encoding is not None:
            try:
                special_tokens = set(self._encoding.special_tokens_set)
            except Exception:  # pragma: no cover - mismatch between tiktoken versions
                special_tokens = set()
            allowed_as_text = tokens_as_text & special_tokens
            self._disallowed_special = special_tokens - allowed_as_text
        else:
            self._disallowed_special = set()

    def count(self, text: str) -> int:
        if not text:
            return 0
        if self._encoding is not None:
            return len(self._encode_tokens(text))
        # Rough approximation: assume 4 characters per token.
        return max(1, len(text) // 4)

    def chunk_text(
        self,
        text: str,
        max_tokens: int,
        overlap_tokens: int = 0,
    ) -> Iterator[Tuple[str, int]]:
        """Yield (chunk_text, token_count) windows that respect token limits."""
        text = text.strip()
        if not text:
            return iter(())

        if self._encoding is None:
            return self._chunk_by_chars(text, max_tokens, overlap_tokens)
        return self._chunk_by_tokens(text, max_tokens, overlap_tokens)

    def _chunk_by_tokens(
        self, text: str, max_tokens: int, overlap_tokens: int
    ) -> Iterator[Tuple[str, int]]:
        tokens = self._encode_tokens(text)
        total = len(tokens)
        if total == 0:
            return iter(())

        def generator() -> Iterator[Tuple[str, int]]:
            start = 0
            while start < total:
                end = min(start + max_tokens, total)
                chunk_tokens = tokens[start:end]
                yield (self._encoding.decode(chunk_tokens), len(chunk_tokens))
                if end >= total:
                    break
                start = max(0, end - overlap_tokens)

        return generator()

    def _chunk_by_chars(
        self, text: str, max_tokens: int, overlap_tokens: int
    ) -> Iterator[Tuple[str, int]]:
        # Translate token budget into character budget for approximation.
        max_chars = max_tokens * 4
        overlap_chars = overlap_tokens * 4
        total = len(text)

        def generator() -> Iterator[Tuple[str, int]]:
            start = 0
            while start < total:
                end = min(start + max_chars, total)
                chunk = text[start:end]
                token_estimate = max(1, len(chunk) // 4)
                yield (chunk, token_estimate)
                if end >= total:
                    break
                start = max(0, end - overlap_chars)

        return generator()

    def _encode_tokens(self, text: str) -> List[int]:
        assert self._encoding is not None
        try:
            return self._encoding.encode(
                text,
                disallowed_special=self._disallowed_special,
            )
        except ValueError as exc:
            match = re.search(r"special token '([^']+)'", str(exc))
            if not match:
                raise
            token = match.group(1)
            if token in getattr(self._encoding, "special_tokens_set", set()):
                LOGGER.debug(
                    "Treating special token '%s' as plain text for encoding.",
                    token,
                )
                self._disallowed_special.discard(token)
                return self._encoding.encode(
                    text,
                    disallowed_special=self._disallowed_special,
                )
            raise


def load_embedding_config(env_path: Optional[Path] = None) -> EmbeddingConfig:
    """Load API credentials and model from environment variables."""
    if env_path is None:
        env_path = Path(".env")

    load_dotenv(dotenv_path=env_path, override=False)

    api_key = os.environ.get(ENV_API_KEY)
    model = os.environ.get(ENV_EMBED_MODEL)

    if not api_key:
        raise RuntimeError(
            f"Environment variable {ENV_API_KEY} is required for embedding requests."
        )
    if not model:
        raise RuntimeError(
            f"Environment variable {ENV_EMBED_MODEL} is required to select the embedding model."
        )

    api_url = os.environ.get("EMBED_API_URL", DEFAULT_API_URL)

    return EmbeddingConfig(api_key=api_key, model=model, api_url=api_url)


def load_bookmark_metadata(repo_root: Path) -> List[BookmarkMetadata]:
    """Load bookmark records from data.json."""
    data_path = repo_root / "data.json"
    if not data_path.exists():
        raise FileNotFoundError(f"data.json not found at {data_path}")

    items: List[BookmarkMetadata] = []
    payload = data_path.read_text(encoding="utf-8")
    import json

    raw_entries = json.loads(payload)

    for entry in raw_entries:
        tags = tuple(entry.get("tags") or [])
        items.append(
            BookmarkMetadata(
                month=entry["month"],
                title=entry["title"],
                url=entry["url"],
                timestamp=int(entry["timestamp"]),
                tags=tags,
            )
        )
    return items


def build_documents(repo_root: Path) -> List[BookmarkDocument]:
    """Construct bookmark documents mapped to their summary/raw files."""
    metadata_items = load_bookmark_metadata(repo_root)
    documents: List[BookmarkDocument] = []

    for meta in metadata_items:
        summary_filename = f"{meta.date_prefix}-{meta.slug}.md"
        summary_path = repo_root / meta.month / summary_filename
        raw_filename = f"{meta.date_prefix}-{meta.slug}_raw.md"
        raw_path = repo_root / meta.month / raw_filename
        if not summary_path.exists():
            LOGGER.debug("Summary file missing for '%s' (%s)", meta.title, summary_path)
            continue

        documents.append(
            BookmarkDocument(
                metadata=meta,
                summary_path=summary_path,
                raw_path=raw_path if raw_path.exists() else None,
            )
        )

    return documents


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def extract_summary_sections(markdown_text: str) -> Dict[str, str]:
    """Return normalized content for TL;DR and Summary sections."""
    sections = {}
    for heading in ("TL;DR", "Summary"):
        sections[heading.lower()] = _extract_markdown_section(markdown_text, heading)
    return sections


def _extract_markdown_section(markdown_text: str, heading: str) -> str:
    """Extract the body of a second-level markdown heading."""
    import re

    pattern = re.compile(
        rf"^##\s+{re.escape(heading)}\s*$", re.IGNORECASE | re.MULTILINE
    )
    match = pattern.search(markdown_text)
    if not match:
        return ""
    start = match.end()
    # Find the next `##` heading to delimit the section.
    next_heading = re.compile(r"^##\s+", re.MULTILINE)
    following = next_heading.search(markdown_text, start)
    end = following.start() if following else len(markdown_text)
    section = markdown_text[start:end].strip()
    return section


@dataclass
class MarkdownSection:
    heading: Optional[str]
    level: int
    body: str


def split_markdown_sections(markdown_text: str) -> List[MarkdownSection]:
    """Split markdown into sections keyed by headings.

    Supports both ATX (`## Heading`) and Setext (`Heading\n-----`) styles.
    """
    sections: List[MarkdownSection] = []
    current_heading: Optional[str] = None
    current_level: int = 1
    buffer: List[str] = []

    lines = markdown_text.splitlines()
    total_lines = len(lines)
    idx = 0

    def flush() -> None:
        if not buffer and current_heading is None:
            return
        body = "\n".join(buffer).strip()
        sections.append(
            MarkdownSection(
                heading=current_heading,
                level=current_level,
                body=body,
            )
        )

    while idx < total_lines:
        line = lines[idx]
        stripped = line.strip()
        if stripped.startswith("#"):
            import re

            match = re.match(r"^(#{1,6})\s+(.*)$", stripped)
            if match:
                flush()
                buffer = []
                current_heading = match.group(2).strip()
                current_level = len(match.group(1))
                idx += 1
                continue
        if idx + 1 < total_lines:
            next_line = lines[idx + 1].strip()
            if next_line and set(next_line) <= {"-", "="} and len(next_line) >= 3:
                flush()
                buffer = []
                current_heading = stripped
                current_level = 1 if next_line[0] == "=" else 2
                idx += 2
                continue
        buffer.append(line)
        idx += 1

    flush()
    return sections


class RequestRateLimiter:
    """Simple sliding-window limiter for requests and tokens per minute."""

    WINDOW_SECONDS = 60.0

    def __init__(
        self,
        requests_per_minute: Optional[int] = None,
        tokens_per_minute: Optional[int] = None,
        logger: Optional[logging.Logger] = None,
    ) -> None:
        if requests_per_minute is not None and requests_per_minute <= 0:
            raise ValueError("requests_per_minute must be positive.")
        if tokens_per_minute is not None and tokens_per_minute <= 0:
            raise ValueError("tokens_per_minute must be positive.")
        self.requests_per_minute = requests_per_minute
        self.tokens_per_minute = tokens_per_minute
        self._request_times: deque[float] = deque()
        self._token_events: deque[Tuple[float, int]] = deque()
        self._token_total = 0
        self._logger = logger or LOGGER

    def _prune(self, now: float) -> None:
        window = self.WINDOW_SECONDS
        if self.requests_per_minute is not None:
            while self._request_times and now - self._request_times[0] >= window:
                self._request_times.popleft()
        if self.tokens_per_minute is not None:
            while self._token_events and now - self._token_events[0][0] >= window:
                _, amount = self._token_events.popleft()
                self._token_total -= amount

    def acquire(self, tokens: int) -> None:
        tokens = max(tokens, 0)
        while True:
            now = time.monotonic()
            self._prune(now)
            wait_for = 0.0
            wait_reasons: List[Tuple[str, float]] = []

            if (
                self.requests_per_minute is not None
                and len(self._request_times) >= self.requests_per_minute
            ):
                earliest = self._request_times[0]
                wait_time = self.WINDOW_SECONDS - (now - earliest)
                if wait_time > 0:
                    wait_for = max(wait_for, wait_time)
                    wait_reasons.append(("requests_per_minute", wait_time))

            if (
                self.tokens_per_minute is not None
                and self._token_total + tokens > self.tokens_per_minute
            ):
                excess = self._token_total + tokens - self.tokens_per_minute
                consumed = 0
                for ts, amount in self._token_events:
                    consumed += amount
                    if consumed >= excess:
                        wait_time = self.WINDOW_SECONDS - (now - ts)
                        if wait_time > 0:
                            wait_for = max(wait_for, wait_time)
                            wait_reasons.append(("tokens_per_minute", wait_time))
                        break

            if wait_for <= 0.0:
                break

            reason_labels = {
                "requests_per_minute": "请求频率 (rpm)",
                "tokens_per_minute": "Token 频率 (tpm)",
            }
            human_reasons = ", ".join(
                reason_labels.get(reason, reason)
                for reason in sorted({reason for reason, _ in wait_reasons})
            ) or "unknown"
            recovery_eta = datetime.now().astimezone() + timedelta(seconds=wait_for)
            self._logger.info(
                "Rate limit triggered (%s); pausing for %.2fs until %s.",
                human_reasons,
                wait_for,
                recovery_eta.strftime("%Y-%m-%d %H:%M:%S%z"),
            )
            time.sleep(wait_for)
            self._logger.info(
                "Rate limit recovered (%s) at %s.",
                human_reasons,
                datetime.now().astimezone().strftime("%Y-%m-%d %H:%M:%S%z"),
            )

        timestamp = time.monotonic()
        if self.requests_per_minute is not None:
            self._request_times.append(timestamp)
        if self.tokens_per_minute is not None:
            self._token_events.append((timestamp, tokens))
            self._token_total += tokens


class EmbeddingClient:
    """Thin wrapper over the SiliconFlow embedding API."""

    def __init__(self, config: EmbeddingConfig) -> None:
        self.config = config
        self._session = requests.Session()
        self._session.headers.update(
            {
                "Authorization": f"Bearer {config.api_key}",
                "Content-Type": "application/json",
            }
        )

    def embed(self, texts: Sequence[str]) -> List[List[float]]:
        if not texts:
            return []
        if len(texts) > self.config.max_batch:
            raise ValueError(
                f"Batch size {len(texts)} exceeds configured maximum {self.config.max_batch}"
            )

        payload = {
            "model": self.config.model,
            "input": list(texts),
        }

        attempt = 0
        while True:
            try:
                response = self._session.post(
                    self.config.api_url,
                    json=payload,
                    timeout=self.config.request_timeout,
                )
                response.raise_for_status()
            except requests.HTTPError as exc:
                attempt += 1
                status = exc.response.status_code if exc.response else "?"
                if (
                    attempt < self.config.max_retries
                    and status in (429, 500, 502, 503, 504)
                ):
                    backoff = self.config.retry_backoff**attempt
                    LOGGER.warning(
                        "Embedding request failed with status %s (attempt %d/%d). Retrying in %.1fs.",
                        status,
                        attempt,
                        self.config.max_retries,
                        backoff,
                    )
                    time.sleep(backoff)
                    continue
                raise
            except requests.RequestException:
                attempt += 1
                if attempt < self.config.max_retries:
                    backoff = self.config.retry_backoff**attempt
                    LOGGER.warning(
                        "Embedding request connection error (attempt %d/%d). Retrying in %.1fs.",
                        attempt,
                        self.config.max_retries,
                        backoff,
                    )
                    time.sleep(backoff)
                    continue
                raise

            break

        payload = response.json()
        data = payload.get("data", [])
        if not data:
            raise RuntimeError("Embedding API returned no data.")
        # Ensure order matches inputs by sorting on index.
        data_sorted = sorted(data, key=lambda item: item.get("index", 0))
        embeddings = [item["embedding"] for item in data_sorted]
        return embeddings

    def close(self) -> None:
        self._session.close()


def build_summary_chunks(
    document: BookmarkDocument,
    sections: Dict[str, str],
    splitter: TokenSplitter,
) -> List[ChunkInput]:
    chunks: List[ChunkInput] = []
    for chunk_type, heading in (("tldr", "tl;dr"), ("summary", "summary")):
        raw_text = sections.get(heading, "").strip()
        if not raw_text:
            continue
        for idx, (chunk_text, token_count) in enumerate(
            splitter.chunk_text(raw_text, SUMMARY_CHUNK_TOKENS, overlap_tokens=50)
        ):
            chunks.append(
                ChunkInput(
                    document_id=document.document_id,
                    chunk_type=chunk_type,
                    chunk_index=idx,
                    heading=heading.upper(),
                    content=chunk_text,
                    token_count=token_count,
                    text_sha=sha256_text(chunk_text),
                )
            )
    return chunks


def build_raw_chunks(
    document: BookmarkDocument,
    raw_text: str,
    splitter: TokenSplitter,
) -> List[ChunkInput]:
    sections = split_markdown_sections(raw_text)
    chunks: List[ChunkInput] = []
    chunk_index = 0
    for section in sections:
        section_text = section.body.strip()
        if not section_text:
            continue
        heading_text = section.heading.strip() if section.heading else None
        payload_text = (
            f"{heading_text}\n\n{section_text}" if heading_text else section_text
        )
        for chunk_text, token_count in splitter.chunk_text(
            payload_text, MAX_RAW_CHUNK_TOKENS, RAW_CHUNK_OVERLAP
        ):
            chunks.append(
                ChunkInput(
                    document_id=document.document_id,
                    chunk_type="raw",
                    chunk_index=chunk_index,
                    heading=heading_text,
                    content=chunk_text,
                    token_count=token_count,
                    text_sha=sha256_text(chunk_text),
                )
            )
            chunk_index += 1
    return chunks


def embed_chunks(
    client: EmbeddingClient,
    chunks: Sequence[ChunkInput],
    batch_size: Optional[int] = None,
    progress_callback: Optional[Callable[[int], None]] = None,
    rate_limiter: Optional[RequestRateLimiter] = None,
) -> List[np.ndarray]:
    """Embed chunks in batches, returning vectors aligned with the inputs."""
    if not chunks:
        return []
    if batch_size is None:
        batch_size = client.config.max_batch

    vectors: List[np.ndarray] = []
    for index in range(0, len(chunks), batch_size):
        batch_chunks = chunks[index : index + batch_size]
        batch = [chunk.content for chunk in batch_chunks]
        if rate_limiter is not None:
            token_budget = sum(chunk.token_count for chunk in batch_chunks)
            rate_limiter.acquire(token_budget)
        embeddings = client.embed(batch)
        vectors.extend(np.asarray(embeddings, dtype=np.float32))
        if progress_callback is not None:
            progress_callback(len(batch))
    return vectors


def summarise_hashes(sections: Dict[str, str]) -> str:
    """Combine TL;DR and Summary sections into a single hash string."""
    joined = "\n\n".join(
        value.strip() for key, value in sorted(sections.items()) if value.strip()
    )
    return sha256_text(joined)
