"""SQLite-backed manifest and embedding storage."""

from __future__ import annotations

import json
import sqlite3
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Sequence, Tuple

import numpy as np


@dataclass
class DocumentRecord:
    document_id: str
    month: str
    title: str
    url: str
    timestamp: int
    tags: Tuple[str, ...]
    summary_hash: str
    raw_hash: Optional[str]
    embed_model: str


@dataclass
class ChunkRecord:
    document_id: str
    chunk_type: str
    chunk_index: int
    heading: Optional[str]
    text_sha: str
    token_count: int
    embedding: np.ndarray
    embed_model: str
    content: str


class EmbeddingStore:
    """Simple SQLite helper around the manifest & chunk tables."""

    def __init__(self, database_path: Path) -> None:
        self.database_path = database_path
        if database_path.parent and not database_path.parent.exists():
            database_path.parent.mkdir(parents=True, exist_ok=True)
        self.connection = sqlite3.connect(database_path)
        self.connection.row_factory = sqlite3.Row
        self.connection.execute("PRAGMA foreign_keys = ON;")
        self._initialize()

    def close(self) -> None:
        self.connection.close()

    def _initialize(self) -> None:
        self.connection.executescript(
            """
            CREATE TABLE IF NOT EXISTS documents (
                document_id TEXT PRIMARY KEY,
                month TEXT NOT NULL,
                title TEXT NOT NULL,
                url TEXT NOT NULL,
                timestamp INTEGER NOT NULL,
                tags TEXT NOT NULL,
                summary_hash TEXT NOT NULL,
                raw_hash TEXT,
                embed_model TEXT NOT NULL,
                created_at TEXT NOT NULL DEFAULT (datetime('now')),
                updated_at TEXT NOT NULL DEFAULT (datetime('now'))
            );

            CREATE TABLE IF NOT EXISTS chunks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                document_id TEXT NOT NULL,
                chunk_type TEXT NOT NULL,
                chunk_index INTEGER NOT NULL,
                heading TEXT,
                text_sha TEXT NOT NULL,
                token_count INTEGER NOT NULL,
                embedding BLOB NOT NULL,
                embed_model TEXT NOT NULL,
                content TEXT NOT NULL,
                dimension INTEGER NOT NULL,
                created_at TEXT NOT NULL DEFAULT (datetime('now')),
                updated_at TEXT NOT NULL DEFAULT (datetime('now')),
                UNIQUE(document_id, chunk_type, chunk_index, embed_model),
                FOREIGN KEY(document_id) REFERENCES documents(document_id) ON DELETE CASCADE
            );

            CREATE INDEX IF NOT EXISTS idx_chunks_doc_model
                ON chunks(document_id, embed_model);
            """
        )
        self.connection.commit()

    def get_document(self, document_id: str) -> Optional[sqlite3.Row]:
        cursor = self.connection.execute(
            "SELECT * FROM documents WHERE document_id = ?", (document_id,)
        )
        return cursor.fetchone()

    def upsert_document(self, record: DocumentRecord) -> None:
        now = datetime.now(timezone.utc).isoformat()
        tags_payload = json.dumps(list(record.tags), ensure_ascii=False)
        self.connection.execute(
            """
            INSERT INTO documents (
                document_id, month, title, url, timestamp, tags,
                summary_hash, raw_hash, embed_model, created_at, updated_at
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ON CONFLICT(document_id) DO UPDATE SET
                month = excluded.month,
                title = excluded.title,
                url = excluded.url,
                timestamp = excluded.timestamp,
                tags = excluded.tags,
                summary_hash = excluded.summary_hash,
                raw_hash = excluded.raw_hash,
                embed_model = excluded.embed_model,
                updated_at = excluded.updated_at;
            """,
            (
                record.document_id,
                record.month,
                record.title,
                record.url,
                int(record.timestamp),
                tags_payload,
                record.summary_hash,
                record.raw_hash,
                record.embed_model,
                now,
                now,
            ),
        )
        self.connection.commit()

    def get_chunk_signatures(
        self, document_id: str, embed_model: str
    ) -> Dict[Tuple[str, int], str]:
        cursor = self.connection.execute(
            """
            SELECT chunk_type, chunk_index, text_sha FROM chunks
            WHERE document_id = ? AND embed_model = ?
            """,
            (document_id, embed_model),
        )
        return {
            (row["chunk_type"], row["chunk_index"]): row["text_sha"] for row in cursor
        }

    def upsert_chunks(self, records: Sequence[ChunkRecord]) -> None:
        if not records:
            return
        now = datetime.now(timezone.utc).isoformat()
        payloads = [
            (
                record.document_id,
                record.chunk_type,
                record.chunk_index,
                record.heading,
                record.text_sha,
                record.token_count,
                record.embedding.astype(np.float32).tobytes(),
                record.embed_model,
                record.content,
                int(record.embedding.size),
                now,
                now,
            )
            for record in records
        ]
        self.connection.executemany(
            """
            INSERT INTO chunks (
                document_id, chunk_type, chunk_index, heading, text_sha,
                token_count, embedding, embed_model, content, dimension,
                created_at, updated_at
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ON CONFLICT(document_id, chunk_type, chunk_index, embed_model)
            DO UPDATE SET
                heading = excluded.heading,
                text_sha = excluded.text_sha,
                token_count = excluded.token_count,
                embedding = excluded.embedding,
                content = excluded.content,
                dimension = excluded.dimension,
                updated_at = excluded.updated_at;
            """,
            payloads,
        )
        self.connection.commit()

    def prune_chunks(
        self,
        document_id: str,
        embed_model: str,
        valid_keys: Iterable[Tuple[str, int]],
    ) -> None:
        valid = set(valid_keys)
        if not valid:
            # Remove all chunks for the document+model combination.
            self.connection.execute(
                "DELETE FROM chunks WHERE document_id = ? AND embed_model = ?",
                (document_id, embed_model),
            )
            self.connection.commit()
            return

        placeholders = ", ".join(["(?, ?)"] * len(valid))
        params: List[object] = []
        for chunk_type, chunk_index in valid:
            params.extend([chunk_type, chunk_index])

        query = f"""
            DELETE FROM chunks
            WHERE document_id = ?
              AND embed_model = ?
              AND (chunk_type, chunk_index) NOT IN (
                    {placeholders}
                )
        """
        self.connection.execute(query, [document_id, embed_model, *params])
        self.connection.commit()
