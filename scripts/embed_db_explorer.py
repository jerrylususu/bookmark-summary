#!/usr/bin/env python3
"""Inspect and export statistics from the embeddings SQLite database."""

from __future__ import annotations

import argparse
import csv
import json
import sqlite3
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Optional

try:  # Rich provides nicer terminal tables; fall back gracefully if unavailable.
    from rich import box
    from rich.console import Console
    from rich.table import Table
except Exception:  # pragma: no cover - rich is optional at runtime
    Console = None  # type: ignore[assignment]
    Table = None  # type: ignore[assignment]
    box = None  # type: ignore[assignment]


@dataclass
class DocumentStats:
    document_id: str
    month: str
    title: str
    embed_model: str
    summary_chunks: int
    tldr_chunks: int
    raw_chunks: int
    other_chunks: int

    @property
    def total_chunks(self) -> int:
        return self.summary_chunks + self.tldr_chunks + self.raw_chunks + self.other_chunks

    def as_dict(self) -> Dict[str, object]:
        return {
            "document_id": self.document_id,
            "month": self.month,
            "title": self.title,
            "embed_model": self.embed_model,
            "summary_chunks": self.summary_chunks,
            "tldr_chunks": self.tldr_chunks,
            "raw_chunks": self.raw_chunks,
            "other_chunks": self.other_chunks,
            "total_chunks": self.total_chunks,
        }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Explore chunk statistics stored in embeddings.sqlite."
    )
    parser.add_argument(
        "--database",
        type=Path,
        default=Path("embeddings.sqlite"),
        help="SQLite 数据库路径（默认：embeddings.sqlite）。",
    )
    parser.add_argument(
        "--embed-model",
        dest="embed_model",
        default=None,
        help="仅统计指定 embed_model 的记录。",
    )
    parser.add_argument(
        "--format",
        choices=("table", "json", "csv"),
        default="table",
        help="输出格式：table/json/csv。",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=None,
        help="当 format=csv/json 时写入的文件路径；未指定则输出到标准输出。",
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=None,
        help="仅展示前 N 条文档统计（table 输出时常用）。",
    )
    return parser.parse_args()


def open_connection(database: Path) -> sqlite3.Connection:
    connection = sqlite3.connect(database)
    connection.row_factory = sqlite3.Row
    return connection


def fetch_document_stats(connection: sqlite3.Connection, embed_model: Optional[str]) -> List[DocumentStats]:
    cursor = connection.execute(
        """
        SELECT
            d.document_id,
            d.month,
            d.title,
            d.embed_model,
            COALESCE(SUM(CASE WHEN c.chunk_type = 'summary' THEN 1 ELSE 0 END), 0) AS summary_chunks,
            COALESCE(SUM(CASE WHEN c.chunk_type = 'tldr' THEN 1 ELSE 0 END), 0) AS tldr_chunks,
            COALESCE(SUM(CASE WHEN c.chunk_type = 'raw' THEN 1 ELSE 0 END), 0) AS raw_chunks,
            COALESCE(
                SUM(
                    CASE
                        WHEN c.chunk_type NOT IN ('summary', 'tldr', 'raw') AND c.chunk_type IS NOT NULL
                        THEN 1 ELSE 0
                    END
                ),
                0
            ) AS other_chunks
        FROM documents AS d
        LEFT JOIN chunks AS c
               ON c.document_id = d.document_id
              AND c.embed_model = d.embed_model
        WHERE (:embed_model IS NULL OR d.embed_model = :embed_model)
        GROUP BY d.document_id
        ORDER BY d.month ASC, d.document_id ASC
        """,
        {"embed_model": embed_model},
    )

    results: List[DocumentStats] = []
    for row in cursor:
        results.append(
            DocumentStats(
                document_id=row["document_id"],
                month=row["month"],
                title=row["title"],
                embed_model=row["embed_model"],
                summary_chunks=int(row["summary_chunks"]),
                tldr_chunks=int(row["tldr_chunks"]),
                raw_chunks=int(row["raw_chunks"]),
                other_chunks=int(row["other_chunks"]),
            )
        )
    return results


def compute_totals(stats: List[DocumentStats]) -> Dict[str, int]:
    return {
        "documents": len(stats),
        "summary_chunks": sum(item.summary_chunks for item in stats),
        "tldr_chunks": sum(item.tldr_chunks for item in stats),
        "raw_chunks": sum(item.raw_chunks for item in stats),
        "other_chunks": sum(item.other_chunks for item in stats),
        "total_chunks": sum(item.total_chunks for item in stats),
    }


def render_table(stats: List[DocumentStats], totals: Dict[str, int], limit: Optional[int]) -> None:
    if Console is None or Table is None:
        print("rich 库未安装，无法渲染表格。请使用 --format json/csv 或安装 rich。")
        return

    console = Console()
    display_stats = stats if limit is None else stats[:limit]

    console.print(
        f"[bold]文档总数：[/bold]{totals['documents']} | "
        f"[bold]Chunk 总计：[/bold]{totals['total_chunks']} "
        f"(summary {totals['summary_chunks']}, tldr {totals['tldr_chunks']}, raw {totals['raw_chunks']}, 其他 {totals['other_chunks']})"
    )

    table = Table(
        title="嵌入数据库文档统计",
        box=box.SIMPLE_HEAVY if box else None,
        header_style="bold",
    )
    table.add_column("文档 ID", style="cyan", no_wrap=True)
    table.add_column("月份", style="green", no_wrap=True)
    table.add_column("标题", style="magenta")
    table.add_column("模型", style="yellow")
    table.add_column("Summary", justify="right")
    table.add_column("TL;DR", justify="right")
    table.add_column("Raw", justify="right")
    show_other = any(item.other_chunks for item in display_stats)
    if show_other:
        table.add_column("其他", justify="right")
    table.add_column("总计", justify="right")

    for item in display_stats:
        row = [
            item.document_id,
            item.month,
            item.title,
            item.embed_model,
            str(item.summary_chunks),
            str(item.tldr_chunks),
            str(item.raw_chunks),
        ]
        if show_other:
            row.append(str(item.other_chunks))
        row.append(str(item.total_chunks))
        table.add_row(*row)

    if display_stats != stats:
        console.print(f"[dim]已截断为前 {len(display_stats)} 篇文档。使用 --limit N 调整或移除限制。[/dim]")

    console.print(table)


def export_json(stats: List[DocumentStats], totals: Dict[str, int], output: Optional[Path]) -> None:
    payload = {
        "totals": totals,
        "documents": [item.as_dict() for item in stats],
    }
    serialized = json.dumps(payload, ensure_ascii=False, indent=2)
    if output:
        output.write_text(serialized, encoding="utf-8")
    else:
        print(serialized)


def export_csv(stats: List[DocumentStats], output: Optional[Path]) -> None:
    fieldnames = [
        "document_id",
        "month",
        "title",
        "embed_model",
        "summary_chunks",
        "tldr_chunks",
        "raw_chunks",
        "other_chunks",
        "total_chunks",
    ]
    if output:
        with output.open("w", newline="", encoding="utf-8") as handle:
            writer = csv.DictWriter(handle, fieldnames=fieldnames)
            writer.writeheader()
            for item in stats:
                writer.writerow(item.as_dict())
    else:
        writer = csv.DictWriter(
            _StdoutWriter(), fieldnames=fieldnames, lineterminator="\n"
        )
        writer.writeheader()
        for item in stats:
            writer.writerow(item.as_dict())


class _StdoutWriter:
    """Helper to provide a write() API with UTF-8 encoding for csv.DictWriter."""

    def write(self, data: str) -> int:  # pragma: no cover - trivial passthrough
        import sys

        return sys.stdout.write(data)


def main() -> None:
    args = parse_args()
    database_path = args.database.resolve()

    if not database_path.exists():
        raise SystemExit(f"数据库不存在：{database_path}")

    connection = open_connection(database_path)
    try:
        stats = fetch_document_stats(connection, args.embed_model)
    finally:
        connection.close()

    if not stats:
        print("数据库中尚无嵌入文档记录。")
        return

    totals = compute_totals(stats)

    if args.format == "json":
        export_json(stats, totals, args.output)
    elif args.format == "csv":
        export_csv(stats, args.output)
    else:
        render_table(stats, totals, args.limit)


if __name__ == "__main__":
    main()
