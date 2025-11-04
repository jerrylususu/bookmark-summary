#!/usr/bin/env python3
"""Semantic search CLI backed by the persisted embeddings database."""

from __future__ import annotations

import argparse
import logging
import sqlite3
from dataclasses import dataclass
from pathlib import Path
import sys
from textwrap import shorten
from typing import Iterable, List, Sequence

import numpy as np


REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from embedding_pipeline import (  # noqa: E402
    EmbeddingClient,
    EmbeddingConfig,
    load_embedding_config,
)


LOGGER = logging.getLogger("embed_search_db")


@dataclass
class ChunkEntry:
    document_id: str
    title: str
    url: str
    month: str
    chunk_type: str
    chunk_index: int
    heading: str | None
    content: str
    vector: np.ndarray
    norm: float


VALID_CHUNK_TYPES = ("summary", "tldr", "raw")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Run semantic search against stored bookmark embeddings."
    )
    parser.add_argument(
        "query",
        help="Query text to embed and search for (required).",
    )
    parser.add_argument(
        "--repo-root",
        type=Path,
        default=REPO_ROOT,
        help="Path to the bookmark-summary repository root (defaults to script location).",
    )
    parser.add_argument(
        "--database",
        type=Path,
        default=REPO_ROOT / "embeddings.sqlite",
        help="SQLite database path containing persisted embeddings.",
    )
    parser.add_argument(
        "--env-file",
        type=Path,
        default=None,
        help="Optional .env path for API credentials (defaults to <repo-root>/.env).",
    )
    parser.add_argument(
        "--top-k",
        type=int,
        default=5,
        help="Number of top results to display (default: 5).",
    )
    parser.add_argument(
        "--chunk-type",
        action="append",
        dest="chunk_types",
        choices=VALID_CHUNK_TYPES,
        help=(
            "Limit search to the specified chunk type(s). Can be supplied multiple times. "
            "Defaults to all chunk types."
        ),
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Enable debug logging output.",
    )
    return parser.parse_args()


def configure_logging(verbose: bool) -> None:
    logging.basicConfig(
        level=logging.DEBUG if verbose else logging.INFO,
        format="%(asctime)s - %(levelname)s - %(name)s: %(message)s",
    )


def load_config(repo_root: Path, env_file: Path | None) -> EmbeddingConfig:
    if env_file is None:
        env_file = repo_root / ".env"
    return load_embedding_config(env_file)


def read_index(
    database: Path,
    model: str,
    chunk_types: Sequence[str] | None,
) -> List[ChunkEntry]:
    if not database.exists():
        raise SystemExit(f"Database not found: {database}")

    connection = sqlite3.connect(database)
    try:
        connection.row_factory = sqlite3.Row
        placeholders = ""
        params: List[object] = [model]
        if chunk_types:
            placeholders = ", ".join(["?"] * len(chunk_types))
            params.extend(chunk_types)

        query = [
            "SELECT",
            "  c.document_id, c.chunk_type, c.chunk_index, c.heading,",
            "  c.content, c.embedding, c.dimension,",
            "  d.title, d.url, d.month",
            "FROM chunks AS c",
            "JOIN documents AS d ON d.document_id = c.document_id",
            "WHERE c.embed_model = ?",
        ]
        if placeholders:
            query.append(f"  AND c.chunk_type IN ({placeholders})")
        query.append("ORDER BY c.document_id, c.chunk_type, c.chunk_index")
        sql = "\n".join(query)

        cursor = connection.execute(sql, params)
        entries: List[ChunkEntry] = []
        for row in cursor:
            vector = np.frombuffer(row["embedding"], dtype=np.float32)
            if vector.size != row["dimension"]:
                LOGGER.warning(
                    "Skipping %s chunk %s[%d]: mismatched dimension (%d vs %d).",
                    row["document_id"],
                    row["chunk_type"],
                    row["chunk_index"],
                    vector.size,
                    row["dimension"],
                )
                continue
            norm = float(np.linalg.norm(vector))
            if norm == 0.0:
                LOGGER.debug(
                    "Skipping %s chunk %s[%d]: zero vector norm.",
                    row["document_id"],
                    row["chunk_type"],
                    row["chunk_index"],
                )
                continue
            entries.append(
                ChunkEntry(
                    document_id=row["document_id"],
                    title=row["title"],
                    url=row["url"],
                    month=row["month"],
                    chunk_type=row["chunk_type"],
                    chunk_index=int(row["chunk_index"]),
                    heading=row["heading"],
                    content=row["content"],
                    vector=vector,
                    norm=norm,
                )
            )
        return entries
    finally:
        connection.close()


def embed_query(client: EmbeddingClient, query: str) -> np.ndarray:
    payload = client.embed([query])
    if not payload:
        raise SystemExit("Failed to obtain embedding for query.")
    return np.asarray(payload[0], dtype=np.float32)


def cosine_similarity(a: np.ndarray, b: np.ndarray, norm_a: float, norm_b: float) -> float:
    if norm_a == 0.0 or norm_b == 0.0:
        return 0.0
    return float(np.dot(a, b) / (norm_a * norm_b))


def rank_chunks(query_vector: np.ndarray, entries: Iterable[ChunkEntry]) -> List[tuple[float, ChunkEntry]]:
    q_norm = float(np.linalg.norm(query_vector))
    scored: List[tuple[float, ChunkEntry]] = []
    for entry in entries:
        score = cosine_similarity(entry.vector, query_vector, entry.norm, q_norm)
        scored.append((score, entry))
    scored.sort(key=lambda item: item[0], reverse=True)
    return scored


def display_results(results: Sequence[tuple[float, ChunkEntry]], top_k: int) -> None:
    if not results:
        print("数据库中没有可用的嵌入数据。")
        return

    limit = min(top_k, len(results))
    print(f"Top {limit} 条结果：")
    for rank, (score, entry) in enumerate(results[:top_k], start=1):
        snippet = shorten(entry.content.replace("\n", " "), width=160, placeholder="…")
        heading = entry.heading or "(无标题)"
        print(
            f"{rank}. 相似度 {score:0.3f} | {entry.title} ({entry.month})\n"
            f"   Chunk: {entry.chunk_type}[{entry.chunk_index}] | Heading: {heading}\n"
            f"   URL: {entry.url}\n"
            f"   内容片段：{snippet}"
        )


def main() -> None:
    args = parse_args()
    configure_logging(args.verbose)

    repo_root = args.repo_root.resolve()
    database = args.database.resolve()

    if not repo_root.exists():
        raise SystemExit(f"Repository root not found: {repo_root}")

    config = load_config(repo_root, args.env_file)
    LOGGER.info("Using embedding model: %s", config.model)

    entries = read_index(database, config.model, args.chunk_types)
    if not entries:
        raise SystemExit("数据库中没有匹配模型的嵌入记录。")

    client = EmbeddingClient(config)
    try:
        query_vector = embed_query(client, args.query)
        results = rank_chunks(query_vector, entries)
        display_results(results, args.top_k)
    finally:
        client.close()


if __name__ == "__main__":
    main()

