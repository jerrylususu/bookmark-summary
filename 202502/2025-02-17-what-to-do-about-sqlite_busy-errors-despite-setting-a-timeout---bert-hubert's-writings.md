# What to do about SQLITE_BUSY errors despite setting a timeout - Bert Hubert's writings
- URL: https://berthub.eu/articles/posts/a-brief-post-on-sqlite3-database-locked-despite-timeout/
- Added At: 2025-02-17 14:19:03

## TL;DR
文章讨论了SQLite中的SQLITE_BUSY错误，尤其是在WAL模式下的事务升级问题，并提供了避免该错误的解决方案，如使用BEGIN IMMEDIATE和减少写操作。

## Summary
1. **问题背景**：
   - 作者是SQLite的忠实用户，最近在项目中遇到了SQLITE_BUSY错误，尽管设置了超时。
   - 有人建议使用“真正的数据库”（PostgreSQL），但作者认为SQLite和PostgreSQL都是优秀的项目。

2. **问题描述**：
   - 在WAL模式下，SQLite允许多个读操作同时进行，但只有一个写操作。
   - 尽管设置了超时，仍然可能出现SQLITE_BUSY错误，尤其是在升级事务时。

3. **SQLite事务机制**：
   - SQLite允许在事务开始时不指定事务类型（读或写），而是在执行第一个语句时决定。
   - 如果不指定“immediate”，可能会导致事务从只读升级为读写，从而引发SQLITE_BUSY错误。

4. **问题示例**：
   - 通过示例代码展示了在并发情况下，如果一个事务尝试从只读升级为读写，会立即引发SQLITE_BUSY错误。
   - 这种错误无法通过超时设置解决，因为SQLite的序列化隔离模式不允许这种升级。

5. **SQLite与PostgreSQL的对比**：
   - PostgreSQL在序列化模式下也会遇到类似问题，尽管它支持多种隔离级别。
   - PostgreSQL的默认隔离级别“Read Committed”允许在事务中看到其他事务的更改，而SQLite和MySQL则不会。

6. **解决方案**：
   - 避免事务升级为读写，使用BEGIN IMMEDIATE或在事务开始时就进行写操作。
   - 减少事务中的写操作，避免长时间保持事务打开。
   - 使用连接池控制活动连接数。

7. **特殊情况**：
   - 在程序启动时打开多个SQLite连接可能会引发SQLITE_BUSY_RECOVERY错误，建议逐个打开连接。

8. **进一步阅读**：
   - 提供了一些相关文档和文章链接，包括SQLite事务、SQLITE_BUSY错误、数据库隔离级别等。
