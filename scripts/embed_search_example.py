#!/usr/bin/env python3
"""Interactive semantic search demo for bookmark summaries."""

from __future__ import annotations

import argparse
import logging
from dataclasses import dataclass
from pathlib import Path
import sys
from textwrap import shorten
from typing import List, Sequence

import numpy as np

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from embedding_pipeline import (  # noqa: E402
    BookmarkDocument,
    EmbeddingClient,
    EmbeddingConfig,
    build_documents,
    extract_summary_sections,
    load_embedding_config,
)


LOGGER = logging.getLogger("embed_search_example")


@dataclass
class IndexEntry:
    document: BookmarkDocument
    text: str
    vector: np.ndarray
    norm: float


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Embed a small set of bookmark summaries and run semantic search."
    )
    parser.add_argument(
        "--repo-root",
        type=Path,
        default=REPO_ROOT,
        help="Path to the bookmark-summary repository root.",
    )
    parser.add_argument(
        "--env-file",
        type=Path,
        default=None,
        help="Optional .env path for API credentials (defaults to <repo-root>/.env).",
    )
    parser.add_argument(
        "--max-docs",
        type=int,
        default=10,
        help="Number of documents to index (defaults to 10).",
    )
    parser.add_argument(
        "--top-k",
        type=int,
        default=5,
        help="Number of results to show for each query.",
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Enable debug logging.",
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


def embed_texts(client: EmbeddingClient, texts: Sequence[str]) -> List[np.ndarray]:
    """Embed arbitrary texts respecting the API batch size."""
    if not texts:
        return []
    vectors: List[np.ndarray] = []
    batch_size = client.config.max_batch
    for start in range(0, len(texts), batch_size):
        batch = texts[start : start + batch_size]
        LOGGER.debug("Requesting embeddings for batch of %d texts.", len(batch))
        payload = client.embed(batch)
        vectors.extend(np.asarray(vector, dtype=np.float32) for vector in payload)
    return vectors


def build_summary_index(
    documents: Sequence[BookmarkDocument],
    client: EmbeddingClient,
) -> List[IndexEntry]:
    texts: List[str] = []
    anchors: List[BookmarkDocument] = []
    for document in documents:
        summary_md = document.summary_path.read_text(encoding="utf-8")
        sections = extract_summary_sections(summary_md)
        joined = "\n\n".join(
            section.strip()
            for section in (sections.get("tldr"), sections.get("summary"))
            if section and section.strip()
        ).strip()
        if not joined:
            LOGGER.debug("Skipping %s (no TL;DR or Summary).", document.document_id)
            continue
        texts.append(joined)
        anchors.append(document)

    if not texts:
        LOGGER.warning("No documents contained summary content; index is empty.")
        return []

    vectors = embed_texts(client, texts)
    index: List[IndexEntry] = []
    for document, text, vector in zip(anchors, texts, vectors, strict=False):
        norm = float(np.linalg.norm(vector))
        if norm == 0.0:
            LOGGER.debug("Skipping %s due to zero embedding norm.", document.document_id)
            continue
        index.append(
            IndexEntry(
                document=document,
                text=text,
                vector=vector,
                norm=norm,
            )
        )
    return index


def cosine_similarity(a: np.ndarray, b: np.ndarray, norm_a: float, norm_b: float) -> float:
    if norm_a == 0.0 or norm_b == 0.0:
        return 0.0
    return float(np.dot(a, b) / (norm_a * norm_b))


def interactive_loop(index: Sequence[IndexEntry], client: EmbeddingClient, top_k: int) -> None:
    if not index:
        LOGGER.error("Index is empty; aborting interactive search.")
        return

    print("输入查询内容，按 Ctrl-D 退出。")
    while True:
        try:
            query = input("> ").strip()
        except EOFError:
            print("\n结束搜索会话。")
            break
        except KeyboardInterrupt:
            print("\n用户中断。")
            break

        if not query:
            continue

        query_vector = embed_texts(client, [query])
        if not query_vector:
            print("无法获取查询向量，请重试。")
            continue

        q_vec = query_vector[0]
        q_norm = float(np.linalg.norm(q_vec))
        scored = [
            (
                cosine_similarity(entry.vector, q_vec, entry.norm, q_norm),
                entry,
            )
            for entry in index
        ]
        scored.sort(key=lambda item: item[0], reverse=True)
        print(f"Top {min(top_k, len(scored))} 结果：")
        for rank, (score, entry) in enumerate(scored[:top_k], start=1):
            meta = entry.document.metadata
            snippet = shorten(entry.text.replace("\n", " "), width=160, placeholder="…")
            print(
                f"{rank}. 相似度 {score:0.3f} | {meta.title} ({meta.month})\n"
                f"   URL: {meta.url}\n"
                f"   摘要：{snippet}"
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
    LOGGER.info("Loaded %d documents for indexing.", len(documents))

    if not documents:
        raise SystemExit("No documents available to index.")

    client = EmbeddingClient(config)
    try:
        index = build_summary_index(documents, client)
        LOGGER.info("Built index with %d documents.", len(index))
        interactive_loop(index, client, args.top_k)
    finally:
        client.close()


if __name__ == "__main__":
    main()
