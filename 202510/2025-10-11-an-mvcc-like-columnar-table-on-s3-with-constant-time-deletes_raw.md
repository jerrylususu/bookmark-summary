Title: An MVCC-like columnar table on S3 with constant-time deletes

URL Source: https://www.shayon.dev/post/2025/277/an-mvcc-like-columnar-table-on-s3-with-constant-time-deletes/

Published Time: 2025-10-04

Markdown Content:
Parquet is excellent for analytical workloads. Columnar layout, aggressive compression, predicate pushdown, but deletes require rewriting entire files. Systems like Apache Iceberg and Delta Lake solve this by adding metadata layers that track delete files separately from data files. But what if, for fun, we built something (arguably) simpler? S3 now has conditional writes (`If-Match`, `If-None-Match`) that enable atomic operations without external coordination. Let’s explore how we might build a columnar table format on S3 that gets most of Parquet’s benefits while supporting constant-time deletes.

The delete problem with immutable formats
-----------------------------------------

Parquet files are immutable by design. When we write a Parquet file and later need to delete row say `id = 500`, we have three options:

1.   Rewrite the entire file without that row
2.   Mark the file as deleted and write a new file with the remaining rows
3.   Track deletes separately and filter at read time

Most production systems choose option 3. Iceberg maintains manifest files that reference data files and delete files. Delta Lake uses a transaction log that tracks which files contain deleted rows. Both require careful coordination to ensure readers see consistent snapshots.

The core challenge is maintaining ACID semantics without a traditional database. When multiple writers append data or delete rows concurrently, how do we ensure they don’t create inconsistent state? This is where S3’s conditional writes become interesting.

S3 conditional writes for coordination
--------------------------------------

S3 introduced conditional write support using HTTP precondition headers:

*   `If-None-Match: "*"` — only succeed if object doesn’t exist (create-only)
*   `If-Match: <etag>` — only succeed if object hasn’t changed (compare-and-swap, or CAS)

Compare-and-swap (CAS) is a fundamental concurrency primitive where we provide the expected current value (the ETag), and the update only succeeds if that value hasn’t changed. If someone else modified the object, we get a `412 Precondition Failed` response instead of silently overwriting their work. This lets multiple writers coordinate without locks and whoever wins the CAS race commits their version, losers retry with the new state.

These primitives are sufficient to build a distributed commit protocol without external coordination. Let’s consider a simple pointer object that references the current table state:

```
S3 Bucket: mytable/
├── _latest_manifest              ← mutable pointer (CAS only)
│   {"version": 123}
│
├── manifest/v00000123.json       ← immutable snapshot
│   {
│     "version": 123,
│     "previous": 122,
│     "data_files": [...],
│     "tombstones": [...]
│   }
│
├── data/2025/10/04/14/
│   ├── f81d4fae.parquet          ← Parquet file (multiple row groups)
│   ├── a1b2c3d4.parquet          ← Parquet file (multiple row groups)
│   └── ...
│
└── tombstone/2025/10/04/14/
    └── abc123.del                ← delete markers
```

The `_latest_manifest` object acts as a single-object transaction log. Writers compete to update it using compare-and-swap, providing serializable commit ordering without locks or external databases.

Object layout and immutability
------------------------------

Everything is write-once except the pointer. This design principle simplifies reasoning about consistency through something like this:

```
WRITE-ONCE OBJECTS                     COMMIT POINTER
  (If-None-Match: "*")                    (If-Match: etag)
┌──────────────────────────────┐      ┌──────────────────────────┐
│ data/YYYY/MM/DD/HH/          │      │ _latest_manifest         │
│   <uuid>.parquet             │      │  {"version": 123}        │
│   (256 MB, ~60 row groups)   │      │  ETag: "abc123def456"    │
│                              │      │                          │
│ tombstone/YYYY/MM/DD/HH/     │◀─────│ CAS token enables        │
│   <uuid>.del                 │      │ atomic manifest updates  │
│                              │      │                          │
│ manifest/v*.json             │      └──────────────────────────┘
└──────────────────────────────┘
```

When a writer wants to append data or record deletes, it follows a protocol that ensures atomicity:

1.   Upload new immutable objects (data files, tombstones)
2.   Fetch `_latest_manifest` to get current version + ETag
3.   Build new manifest pointing to all visible objects
4.   CAS-write new manifest (fails if someone else committed)
5.   Retry from step 2 on conflict

This optimistic concurrency pattern should feel familiar if we’ve worked with etags in distributed systems or MVCC in databases.

Parquet file layout
-------------------

Rather than inventing a custom columnar format, we use standard Parquet files. Each Parquet file contains multiple row groups, with all table columns stored in columnar format within each row group. For a table with columns `id`, `event_time`, and `payload`, we might see:

```
data/2025/10/04/14/f81d4fae.parquet  (256 MB, ~60 row groups)
data/2025/10/04/14/a1b2c3d4.parquet  (256 MB, ~60 row groups)
data/2025/10/04/14/b5e6f7g8.parquet  (256 MB, ~60 row groups)
```

Each file is a standard Parquet file with columnar encoding (dictionary, RLE, bit-packing) and compression (ZSTD). The footer includes per-row-group, per-column statistics that enable predicate pushdown. Internally, Parquet stores each column’s data separately within each row group, so readers can use HTTP range requests to fetch only the columns and row groups they need.

We target files of 256-512 MB with row groups of 1-4 MB compressed. This balances parallelism (many files can be read concurrently) with overhead (fewer manifest entries, fewer S3 requests). The row group size determines HTTP range request granularity.

```
f81d4fae.parquet (256 MB compressed)
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Row Group 0       Row Group 1       Row Group 2      ...  ┃
┃ offset: 1024      offset: 4194304   offset: 8388608       ┃
┃ rows: 200K        rows: 200K        rows: 200K            ┃
┃ size: 4 MB        size: 4 MB        size: 4 MB            ┃
┃                                                           ┃
┃ Columns within each row group:                            ┃
┃ ┌────────────────────────────────────────────────────┐    ┃
┃ │ id column       (compressed INT64)                 │    ┃
┃ │   min: 1000000, max: 1199999                       │    ┃
┃ ├────────────────────────────────────────────────────┤    ┃
┃ │ event_time      (compressed timestamp)             │    ┃
┃ │   min: 2025-10-04T13:00:00Z                        │    ┃
┃ │   max: 2025-10-04T13:05:00Z                        │    ┃
┃ ├────────────────────────────────────────────────────┤    ┃
┃ │ payload         (compressed binary)                │    ┃
┃ └────────────────────────────────────────────────────┘    ┃
┃                                                           ┃
┃ Footer: schema, row group directory, column statistics    ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
```

The footer metadata tells readers which row groups to fetch based on predicates, and which byte ranges to request for needed columns. If a query filters on `id BETWEEN 1000000 AND 1100000` and only needs the `event_time` column, it can skip Row Groups 1 and 2 entirely, and within Row Group 0, fetch only the `event_time` column bytes.

Manifest structure and snapshot isolation
-----------------------------------------

The manifest is a JSON document (or binary format like MessagePack for compactness) that describes a complete table snapshot:

```
{
  "version": 123,
  "previous": 122,
  "created_at": "2025-10-04T13:45:12Z",
  "schema": {
    "columns": [
      { "name": "id", "type": "int64" },
      { "name": "event_time", "type": "timestamp[us]" },
      { "name": "payload", "type": "binary" }
    ]
  },
  "data_files": [
    {
      "path": "s3://mytable/data/2025/10/04/13/f81d4fae.parquet",
      "size_bytes": 268435456,
      "row_group_count": 60,
      "total_rows": 12000000,
      "min": { "event_time": "2025-10-04T13:00:00Z", "id": 1000000 },
      "max": { "event_time": "2025-10-04T13:30:00Z", "id": 12999999 }
    },
    {
      "path": "s3://mytable/data/2025/10/04/13/a1b2c3d4.parquet",
      "size_bytes": 268435456,
      "row_group_count": 60,
      "total_rows": 12000000,
      "min": { "event_time": "2025-10-04T13:30:00Z", "id": 13000000 },
      "max": { "event_time": "2025-10-04T14:00:00Z", "id": 24999999 }
    }
  ],
  "tombstones": ["s3://mytable/tombstone/2025/10/04/13/abc123.del"]
}
```

Readers always start by fetching `_latest_manifest` to discover the current version, then fetch that manifest. This gives them a consistent snapshot where all data files and tombstones referenced by that manifest version represent a single point-in-time view.

The `previous` pointer creates a linked list of versions, enabling time travel within the retention window. Want to see the table as it was 10 versions ago? Fetch `manifest/v00000113.json` directly, assuming it hasn’t been garbage collected yet. Manifests are cheap to keep (200-500 bytes per data file entry), so retaining 30-90 days of history costs almost nothing.

### Snapshot isolation semantics

A reader sees the table state at the moment they fetch `_latest_manifest`. If deletes or appends commit while the reader is scanning data files, those changes remain invisible to that reader. This is standard MVCC behavior where each reader operates on a frozen snapshot. There is technically no “stale read” problem in the consistency sense; readers simply see an earlier committed version, which is the correct snapshot isolation guarantee.

Constant-time deletes with tombstones
-------------------------------------

Deletes don’t touch data files. Instead, we write small tombstone files that mark which rows or row groups should be filtered out at read time:

```
// tombstone/2025/10/04/13/abc123.del
{"file": "f81d4fae.parquet", "row_group": 0}
{"file": "f81d4fae.parquet", "row_group": 5}
{"file": "a1b2c3d4.parquet", "pk_min": 15000000, "pk_max": 15999999}
```

Each line in the tombstone file represents a delete operation:

*   `{"file": "...", "row_group": N}` marks an entire row group within a file as deleted
*   `{"file": "...", "pk_min": ..., "pk_max": ...}` marks a range of primary keys as deleted

For truly row-level deletes within a row group, we can also add:

```
{ "file": "f81d4fae.parquet", "row_group": 3, "deleted_rows": [0, 5, 17, 1042] }
```

Tombstone files are kept small (typically ≤32 MB) to ensure fast reads. When a writer needs to delete rows:

1.   Determine which files and row groups are affected
2.   Write a new tombstone file with delete markers
3.   Fetch `_latest_manifest` + ETag
4.   Build `manifest_vNext` with the new tombstone added to `.tombstones[]`
5.   CAS-write the new manifest

This takes one small PUT plus two tiny PUTs with no data rewrite required. The delete latency is bounded by S3 request latency, not data volume.

Read protocol and delete filtering
----------------------------------

Readers implement a straightforward protocol:

1.   GET `_latest_manifest` to discover current version and ETag
2.   GET the manifest JSON to get the list of data files and tombstones
3.   Filter data files by predicate using min/max stats cached in the manifest. For `WHERE id BETWEEN 15M AND 16M`, we can prune files whose id range doesn’t overlap.
4.   Fetch tombstones and build a bitmap of deleted row groups and rows
5.   Read Parquet footer for each kept file, filter row groups by stats, and issue HTTP range requests for only the needed columns from non-deleted row groups
6.   Decode Parquet data, apply row-level tombstone filters if needed, and project only requested columns

The tombstones are typically much smaller than data files. Even with 100 tombstone files, the total size might be only a few MB. Readers can fetch and parse them quickly, then apply the deletion mask during Parquet decoding. With regular compaction, the list of tombstone files stays small.

For efficient filtering, we can use roaring bitmaps to represent deleted rows. A roaring bitmap compresses sparse deletions extremely well, deleting 1% of rows in a 1M row group might take only a few KB.

Append protocol with CAS retry
------------------------------

When multiple writers try to append new rows (as Parquet files) simultaneously, we need a way to ensure they don’t overwrite each other’s commits or create inconsistent table states. Each writer uploads their Parquet file independently, but then they race to update the manifest pointer. The append protocol uses compare-and-swap on `_latest_manifest` to serialize commits and whoever wins the CAS race commits their version, losers retry by merging their changes with the new state:

```
Writer A                        Writer B                    S3
   │ (sees v122)                   │ (sees v122)            │
   │ Writes file uuid1.parquet     │ Writes file uuid2.parquet
   │                               │                        │
   │ Attempts CAS to v123...       │                        │
   │ PUT _latest_manifest          │                        │
   │ If-Match: "etag_v122"         │                        │
   │──────────────────────────────────────────────────────▶ │
   │◀─────────────────────────────────────────────── 200 OK │
   │ (Commit of v123 succeeds)     │                        │
   │                               │ Attempts CAS to v123...│
   │                               │ PUT _latest_manifest   │
   │                               │ If-Match: "etag_v122"  │
   │                               │───────────────────────▶│
   │                               │◀────────── 412 CONFLICT│
   │                               │                        │
   │                               │ Retry logic begins...  │
   │                               │ GET _latest_manifest   │
   │                               │◀───────────────────────│ (sees v123)
   │                               │                        │
   │                               │ Attempts CAS to v124...│
   │                               │ PUT _latest_manifest   │
   │                               │ If-Match: "etag_v123"  │
   │                               │───────────────────────▶│
   │                               │◀───────────────── 200 OK│
   │                               │ (Commit of v124 succeeds)
```

**EDIT (Oct 6 2025): Updated sequence diagram to be more accurate**

This retry loop provides serializable isolation. Data file uploads happen in parallel with no contention, but manifest commits are linearized through the CAS pointer thus giving us concurrent writes with consistent snapshots.

The Table API
-------------

I have a small POC going for this concept and the public API I have in mind for now is something like the following. It abstracts these details behind simple operations, like:

```
type Table struct {
    Bucket string
    Prefix string
    s3     *s3.Client
}

func Open(bucket, prefix string, cfg aws.Config) *Table

// Append writes new row groups and commits a new manifest version
func (t *Table) Append(ctx context.Context,
                       cols []arrow.Array,
                       opts AppendOptions) error

// Delete marks rows as deleted without rewriting data files
func (t *Table) Delete(ctx context.Context,
                       predicate DeletePredicate) error

// Scan returns an Arrow RecordReader with column projection
// and predicate pushdown
type Scanner struct {
    Columns []string
    Filter  arrow.Expression
}

func (t *Table) Scan(ctx context.Context,
                     opt Scanner) (arrow.RecordReader, error)
```

Behind the scenes:

*   `Append` builds Parquet column files, follows the seven-step CAS protocol, retries on conflict.
*   `Delete` materializes affected row groups, writes a tombstone, updates the manifest atomically.
*   `Scan` fetches the current manifest, prunes row groups by statistics, fetches tombstones, downloads column ranges in parallel, and filters deleted rows.

The caller doesn’t need to understand manifests, tombstones, or CAS semantics. They just append, delete, and scan.

Cost and scalability
--------------------

Consider a typical analytics workload with high-volume ingestion (append-heavy), occasional bulk deletes for retention or GDPR compliance, and scans that filter by time range and project a subset of columns. Most queries read recent data, and writes far outnumber reads. This pattern maps well to S3 pricing where PUTs dominate the request count, but they’re cheap, and data transfer only happens on reads.

The design minimizes both requests and data transfer:

| Operation | S3 Requests | Data Transfer | Notes |
| --- | --- | --- | --- |
| Append 12M rows | 3 PUTs | 256 MB up | 1 Parquet file + manifest + pointer |
| Delete 100K rows | 3 PUTs | ~10 KB up | Tombstone + manifest + pointer |
| Scan 1M rows (2 cols) | 3-5 GETs + range GETs | ~20 MB down | Manifest + tombstones + column ranges |

For a workload ingesting 6 TB/day with 2 TB of deletes and 50K queries/day:

*   PUT requests: ~380K/day (≈4 req/s) = $1.88/day
*   GET requests: highly variable, depends on partitioning effectiveness
    *   Best case (good time-based partitioning): ~100K-200K/day = $0.04-$0.08/day
    *   Worst case (poor partitioning, scanning many files): ~2M/day = $0.80/day

*   Storage: $0.023/GB/month for data plus manifests

For a typical example like the one above the manifests remain small (typically <32 MB even with thousands of data files) because they only store metadata, not data. Tombstones are even smaller and a tombstone marking 1M deleted rows might be only 4 KB if stored as a roaring bitmap. Request costs stay well under $3/day even with aggressive query patterns.

Note: This cost estimation was done with the help of LLM model, after I fed it some rough numbers.

Concurrency and failure semantics
---------------------------------

| Scenario | Behavior | Recovery |
| --- | --- | --- |
| Writer crashes after data upload, before manifest commit | Orphaned data files | Garbage collected later (unreferenced) |
| Writer crashes during CAS retry | Partial manifest written | Next writer’s CAS succeeds; orphan GC’d |
| Two writers commit simultaneously | One succeeds, one gets 412 | Loser retries with new ETag |
| Reader fetches manifest mid-write | Sees old snapshot | Consistent; new writes invisible until committed |

The failure model is simple where either a manifest version is committed (visible to all readers) or it isn’t. There’s no partial visibility. Uncommitted data files are harmless and they’re garbage until referenced by a manifest.

Garbage collection runs periodically to clean up orphaned objects and old manifests. Starting from `_latest_manifest`, walk backwards through the `previous` chain for the retention window (e.g., 30 days or 1000 versions). Mark all data files and tombstones referenced by kept manifests. Delete any unreferenced data files older than 7 days (orphaned from failed writes). Optionally delete manifests and their referenced objects beyond the retention window.

### Optional compaction

Deletes accumulate in tombstone files over time. Eventually we would want to coalesce 100 small tombstone files into one and /or rewrite data files if a row group has >50% rows deleted, resulting in further compaction.

Compaction in this design would be a background job that reads the current manifest, rewrites selected row groups, and commits a new manifest pointing to the new files. The old files remain until a GC pass removes them.

Wrapping up
-----------

This has been a hypothetical exploration of building a columnar table format using Parquet and S3 primitives with conditional writes for coordination, tombstones for constant-time deletes, and a single-object transaction pointer for snapshot isolation. Will you run production workloads on this instead of a proper database? You tell me :D. I think it’s possible for certain append-heavy analytical workloads, but I’m sure I’m overlooking key concerns around operational complexity, failure modes, or edge cases (schema evolution being one) that only show up at scale.

The trade-offs become clear when we compare alternatives. Against Iceberg or Delta Lake, we strip away the external catalog, metastore, and lock service, though we lose mature schema evolution and battle-tested operational tooling in the process. Compared to raw Parquet, we add constant-time deletes and MVCC by taking on manifest management and compaction overhead. Against PostgreSQL, we trade sub-second point lookups and complex transactions for elastic storage and simpler operations (though this depends heavily on your data patterns and operational challenges like autovacuum).

The sweet spot is append-heavy analytical workloads with occasional bulk deletes—think event logs, time-series data, or CDC streams where you need to apply deletes from upstream systems without rewriting history.

The design has natural scaling limits. Manifests grow linearly with file count and eventually need hierarchical structure. Tombstones accumulate over time and need periodic compaction. The single pointer can become a hotspot under extreme write concurrency. But for moderate-scale analytics workloads, I think there are solid primitives here worth exploring.

That said, I do think there’s room to improve the state of the art (for some of the scaling blockers above). Systems like Iceberg and Delta Lake have proven the architecture works, and I for one am genuinely curious about an architecture that has fewer moving pieces at the same time.

If nothing else, it’s a fun design exercise that shows how far you can push object storage primitives.

Until next time.