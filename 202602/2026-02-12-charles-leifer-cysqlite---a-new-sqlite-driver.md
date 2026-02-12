# charles leifer | cysqlite - a new sqlite driver
- URL: https://charlesleifer.com/blog/cysqlite---a-new-sqlite-driver/
- Added At: 2026-02-12 15:02:07
- Tags: #read #python

## TL;DR
cysqlite 是一个全新的 DB-API 兼容 SQLite 驱动，旨在替代标准库 sqlite3 和 pysqlite3。它简化了事务处理，支持高级功能如虚拟表，并为 Peewee ORM 提供了更好的集成，解决了标准库在事务和数据类型处理上的不足。

## Summary
cysqlite 是一个全新的、DB-API 兼容的 SQLite 驱动，由 Charles Leifer 开发，旨在替代 pysqlite3 并解决标准库 sqlite3 模块在事务处理和数据类型处理上的不足。

**核心动机与背景**
- 作者对标准库 sqlite3 的事务处理方式（如 `autocommit` 和 `LEGACY_` 常量）感到不满，认为其行为不一致且可能导致锁问题。
- pysqlite3 项目因维护困难且与 Peewee ORM 的 C 扩展存在兼容性问题而陷入停滞。
- 作者希望有一个更稳定、可控的驱动，用于支持 Peewee 的高级功能（如虚拟表）。

**主要特性**
1. **简化的事务处理**：
   - 遵循 SQLite 默认行为：除非显式开始事务，否则每条语句在独立事务中执行（自动提交）。
   - 提供 `begin()`、`commit()`、`rollback()` 方法及 `atomic()` 上下文管理器，避免隐式事务和锁问题。
   - 移除了 `isolation_level`、`autocommit` 等复杂配置。

2. **数据类型处理**：
   - 支持标准 SQLite 类型（NULL、INTEGER、REAL、TEXT、BLOB）。
   - 对 Python 对象提供合理默认转换（如 `datetime` 转为 ISO 格式字符串），并允许用户自定义转换。

3. **扩展功能**：
   - 集成了用户定义虚拟表、BM25 排序算法等高级功能。
   - 支持 SQLite 回调（提交/回滚、更新、授权等）、备份 API 和 Blob I/O。
   - 提供丰富的内省工具（如获取表、视图、索引等信息）。

4. **兼容性与易用性**：
   - 完全兼容 DB-API 2.0，并提供便捷方法（如 `execute_one`、`execute_scalar`）。
   - 可轻松与静态链接的 SQLite 或 SQLCipher 一起构建。
   - 性能与标准库 sqlite3 相当，迭代结果集更快，但创建游标稍慢。

**目标用户**
- 需要更灵活事务控制或高级 SQLite 功能的开发者。
- Peewee ORM 用户，可直接集成 cysqlite 以使用扩展功能。
- 对标准库 sqlite3 行为不满或希望避免 apsw 复杂性的用户。

**总结**
cysqlite 提供了一个简洁、可控且功能丰富的 SQLite 驱动，解决了标准库的痛点，并为高级用例提供了稳定基础。目前项目已稳定，作者已在多个生产环境中使用，并推荐感兴趣者查阅文档或尝试集成。
