# Litestream VFS
- URL: https://fly.io/blog/litestream-vfs/
- Added At: 2025-12-12 13:12:07
- Tags: #read #db
- [Link To Text](2025-12-12-litestream-vfs_raw.md)

## TL;DR
Litestream VFS 是一项功能，允许用户通过SQLite的插件接口直接查询对象存储（如S3）中的SQLite备份，而无需下载整个文件。它利用LTX格式和索引优化，仅按需加载查询所需的数据页，支持历史时间点查询和快速恢复，适用于云环境临时数据库访问和容错场景。该功能只读，写操作仍由独立进程处理。

## Summary
Litestream VFS 是 Litestream 的一个功能，允许用户直接从对象存储（如 AWS S3）查询 SQLite 数据库的备份，而无需完整下载数据库。它通过 SQLite 的 VFS（虚拟文件系统）插件接口实现，提供快速的点播恢复和实时查询能力。

### 核心功能
- **直接查询备份**：用户可以通过加载 Litestream 的共享库，在 SQLite 中打开远程备份文件（如 `file:///my.db?vfs=litestream`），并执行 SQL 查询。
- **点播恢复**：使用 `PRAGMA litestream_time` 设置特定时间点（如 "5 minutes ago"），即可查询历史数据，无需完整恢复数据库。
- **部分数据读取**：Litestream VFS 仅下载查询所需的数据库页面，而不是整个文件，利用 S3 的 Range 请求和 LRU 缓存优化性能。

### 技术原理
- **基于 LTX 格式**：Litestream 使用 LTX 格式存储备份，该格式通过压缩冗余页面（如仅保留页面的最新版本）加速恢复。
- **分层备份结构**：备份数据按时间分层（如 L0 每秒备份，L1 每 30 秒），通过合并不同层级的 LTX 文件实现高效的点播恢复。
- **索引优化**：LTX 文件包含页面索引（占文件约 1%），VFS 通过读取索引构建页面映射表，直接定位所需页面在 S3 中的位置。
- **近实时同步**：VFS 可轮询 S3 路径，增量更新索引，实现接近实时的副本查询。

### 优势与场景
- **快速启动**：适用于临时服务器或云环境，无需预下载数据库即可查询。
- **容错恢复**：如误操作（如忘记 WHERE 子句的 UPDATE）后，可快速回滚到历史状态。
- **轻量集成**：VFS 作为 SQLite 插件，不依赖特定 SQLite 版本，保持 Litestream 原有非侵入式特性。

### 注意事项
- Litestream VFS 仅处理读操作，写操作仍由独立的 Litestream 进程处理。
- 用户需加载 VFS 库才能使用此功能，但 Litestream 的核心备份功能不依赖 VFS。

总之，Litestream VFS 通过智能索引和部分读取技术，将对象存储变为可查询的数据库源，简化了数据恢复和查询流程。
