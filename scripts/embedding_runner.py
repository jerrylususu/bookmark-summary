#!/usr/bin/env python3
"""Command-line entrypoint for generating bookmark embeddings."""

from __future__ import annotations

import argparse
import logging
from pathlib import Path
import sys
from typing import Dict, List, Optional, Tuple

try:  # Prefer tqdm for real-time progress, but allow fallback without it.
    from tqdm.auto import tqdm
except Exception:  # pragma: no cover - tqdm is optional at runtime
    tqdm = None  # type: ignore[assignment]

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from embedding_pipeline import (
    BookmarkDocument,
    ChunkInput,
    EmbeddingClient,
    EmbeddingConfig,
    TokenSplitter,
    build_documents,
    build_raw_chunks,
    build_summary_chunks,
    embed_chunks,
    RequestRateLimiter,
    extract_summary_sections,
    load_embedding_config,
    sha256_text,
    summarise_hashes,
)
from embedding_store import ChunkRecord, DocumentRecord as StoreDocumentRecord, EmbeddingStore


LOGGER = logging.getLogger("embedding_runner")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Bookmark embedding runner")
    parser.add_argument(
        "--repo-root",
        type=Path,
        default=Path("."),
        help="Path to the bookmark-summary repository root.",
    )
    parser.add_argument(
        "--database",
        type=Path,
        default=Path("embeddings.sqlite"),
        help="SQLite database path used to persist embeddings.",
    )
    parser.add_argument(
        "--env-file",
        type=Path,
        default=None,
        help="Optional .env file path. Defaults to <repo-root>/.env",
    )
    parser.add_argument(
        "--batch-size",
        type=int,
        default=None,
        help="Override embedding batch size (default taken from config).",
    )
    parser.add_argument(
        "--max-docs",
        type=int,
        default=None,
        help="Limit processing to the first N documents (useful for smoke tests).",
    )
    parser.add_argument(
        "--skip-summary",
        action="store_true",
        help="Skip summary + TL;DR embeddings.",
    )
    parser.add_argument(
        "--skip-raw",
        action="store_true",
        help="Skip raw content embeddings.",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Force regeneration even when hashes match.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show planned work without calling the API or writing to the database.",
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Enable verbose logging output.",
    )
    parser.add_argument(
        "--rpm",
        type=int,
        default=None,
        help="Limit embedding API requests per minute.",
    )
    parser.add_argument(
        "--tpm",
        type=int,
        default=None,
        help="Limit embedding API tokens per minute.",
    )
    return parser.parse_args()


def configure_logging(verbose: bool) -> None:
    logging.basicConfig(
        level=logging.DEBUG if verbose else logging.INFO,
        format="%(asctime)s - %(levelname)s - %(name)s: %(message)s",
    )


def load_config(repo_root: Path, env_file: Optional[Path]) -> EmbeddingConfig:
    if env_file is None:
        env_file = repo_root / ".env"
    return load_embedding_config(env_file)


def compute_chunk_plan(
    document: BookmarkDocument,
    skip_summary: bool,
    skip_raw: bool,
    splitter: TokenSplitter,
) -> Tuple[List[ChunkInput], Dict[str, List[ChunkInput]], str, Optional[str]]:
    summary_md = document.summary_path.read_text(encoding="utf-8")
    summary_sections = extract_summary_sections(summary_md)
    summary_hash = summarise_hashes(summary_sections)

    raw_hash = None
    raw_chunks: List[ChunkInput] = []
    if not skip_raw and document.raw_path and document.raw_path.exists():
        raw_text = document.raw_path.read_text(encoding="utf-8")
        raw_hash = sha256_text(raw_text)
        raw_chunks = build_raw_chunks(document, raw_text, splitter)

    summary_chunks: List[ChunkInput] = []
    if not skip_summary:
        summary_chunks = build_summary_chunks(document, summary_sections, splitter)

    # Include TL;DR text (if present) for hash tracking.
    return (
        summary_chunks + raw_chunks,
        {
            "summary": [chunk for chunk in summary_chunks if chunk.chunk_type == "summary"],
            "tldr": [chunk for chunk in summary_chunks if chunk.chunk_type == "tldr"],
            "raw": raw_chunks,
        },
        summary_hash,
        raw_hash,
    )


def main() -> None:
    args = parse_args()
    configure_logging(args.verbose)

    repo_root = args.repo_root.resolve()
    if not repo_root.exists():
        raise SystemExit(f"Repository root not found: {repo_root}")

    config = load_config(repo_root, args.env_file)
    LOGGER.info("Using embedding model: %s", config.model)

    documents = build_documents(repo_root)
    if args.max_docs is not None:
        documents = documents[: args.max_docs]
    LOGGER.info("Loaded %d documents from data.json", len(documents))

    splitter = TokenSplitter()

    store = EmbeddingStore(args.database)
    client: Optional[EmbeddingClient] = None
    rate_limiter: Optional[RequestRateLimiter] = None
    if args.rpm is not None and args.rpm <= 0:
        raise SystemExit("--rpm must be a positive integer.")
    if args.tpm is not None and args.tpm <= 0:
        raise SystemExit("--tpm must be a positive integer.")
    if args.rpm is not None or args.tpm is not None:
        rate_limiter = RequestRateLimiter(
            requests_per_minute=args.rpm,
            tokens_per_minute=args.tpm,
        )
        LOGGER.info(
            "Enabled rate limiting: rpm=%s, tpm=%s",
            args.rpm if args.rpm is not None else "∞",
            args.tpm if args.tpm is not None else "∞",
        )
    if not args.dry_run:
        client = EmbeddingClient(config)

    processed = 0
    skipped = 0
    total_chunks_embedded = 0

    doc_progress = None
    chunk_progress = None
    if tqdm is not None:
        doc_progress = tqdm(
            total=len(documents),
            desc="Embedding documents",
            unit="doc",
        )
        if not args.dry_run:
            chunk_progress = tqdm(
                total=0,
                desc="Embedding chunks",
                unit="chunk",
                leave=False,
            )

    try:
        for document in documents:
            all_chunks, grouped_chunks, summary_hash, raw_hash = compute_chunk_plan(
                document,
                skip_summary=args.skip_summary,
                skip_raw=args.skip_raw,
                splitter=splitter,
            )

            existing_doc = store.get_document(document.document_id)
            existing_signatures = store.get_chunk_signatures(
                document.document_id,
                config.model,
            )

            model_mismatch = (
                existing_doc is not None
                and existing_doc["embed_model"] != config.model
            )

            pending_chunks: List[ChunkInput] = []
            new_keys_by_type: Dict[str, set[int]] = {}

            if not args.skip_summary:
                new_keys_by_type.setdefault("summary", set())
                new_keys_by_type.setdefault("tldr", set())

            if not args.skip_raw and grouped_chunks["raw"]:
                new_keys_by_type.setdefault("raw", set())
            elif not args.skip_raw and document.raw_path:
                # Raw file exists but produced no chunks (e.g., empty). Mark as processed.
                new_keys_by_type.setdefault("raw", set())

            for chunk in all_chunks:
                key = (chunk.chunk_type, chunk.chunk_index)
                new_keys_by_type.setdefault(chunk.chunk_type, set()).add(chunk.chunk_index)
                existing_sha = existing_signatures.get(key)
                should_embed = (
                    args.force
                    or model_mismatch
                    or existing_sha != chunk.text_sha
                    or existing_doc is None
                )
                if should_embed:
                    pending_chunks.append(chunk)

            if not pending_chunks and not args.force and not model_mismatch:
                skipped += 1
                if doc_progress is not None:
                    doc_progress.update(1)
                    doc_progress.refresh()
                continue

            if args.dry_run:
                LOGGER.info(
                    "[dry-run] %s -> %d chunk(s) would be (re)embedded",
                    document.document_id,
                    len(pending_chunks),
                )
                processed += 1
                if doc_progress is not None:
                    doc_progress.update(1)
                    doc_progress.refresh()
                continue

            if not client:
                raise RuntimeError("Embedding client not initialised.")

            progress_callback = None
            if chunk_progress is not None and pending_chunks:
                chunk_progress.total += len(pending_chunks)
                chunk_progress.refresh()

                def progress_callback(batch_size: int) -> None:
                    chunk_progress.update(batch_size)
                    chunk_progress.refresh()

            vectors = embed_chunks(
                client,
                pending_chunks,
                batch_size=args.batch_size,
                progress_callback=progress_callback,
                rate_limiter=rate_limiter,
            )
            chunk_records = [
                ChunkRecord(
                    document_id=chunk.document_id,
                    chunk_type=chunk.chunk_type,
                    chunk_index=chunk.chunk_index,
                    heading=chunk.heading,
                    text_sha=chunk.text_sha,
                    token_count=chunk.token_count,
                    embedding=vectors[idx],
                    embed_model=config.model,
                    content=chunk.content,
                )
                for idx, chunk in enumerate(pending_chunks)
            ]

            doc_record = StoreDocumentRecord(
                document_id=document.document_id,
                month=document.metadata.month,
                title=document.metadata.title,
                url=document.metadata.url,
                timestamp=document.metadata.timestamp,
                tags=document.metadata.tags,
                summary_hash=summary_hash,
                raw_hash=raw_hash,
                embed_model=config.model,
            )
            store.upsert_document(doc_record)

            if chunk_records:
                store.upsert_chunks(chunk_records)
                total_chunks_embedded += len(chunk_records)

            # Determine which chunk keys should remain after this run.
            keys_to_keep = set(existing_signatures.keys())
            for chunk_type, indices in new_keys_by_type.items():
                # Remove previous keys of this type, replace with new set.
                keys_to_keep = {
                    key
                    for key in keys_to_keep
                    if key[0] != chunk_type
                }
                keys_to_keep.update((chunk_type, index) for index in indices)

            store.prune_chunks(document.document_id, config.model, keys_to_keep)

            processed += 1
            if doc_progress is not None:
                doc_progress.update(1)
                doc_progress.refresh()

        LOGGER.info(
            "Finished run: processed %d document(s), skipped %d, embedded %d chunk(s).",
            processed,
            skipped,
            total_chunks_embedded,
        )
    finally:
        if chunk_progress is not None:
            chunk_progress.close()
        if doc_progress is not None:
            doc_progress.close()
        store.close()
        if client:
            client.close()


if __name__ == "__main__":
    main()
    RequestRateLimiter,
