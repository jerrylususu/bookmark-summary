# Replacing a 3 GB SQLite database with a 10 MB FST (finite state transducer) binary
- URL: https://til.andrew-quinn.me/posts/replacing-a-3-gb-sqlite-database-with-a-7-mb-fst-finite-state-trandsucer-binary/
- Added At: 2026-05-11 14:09:49
- Tags: #read #hack

## TL;DR
作者用 Rust 和 FST 库重写芬兰语-英语词典应用，将体积从 3GB 压缩至 10MB，实现 300 倍空间优化，同时保持搜索性能。

## Summary
作者开发了一个芬兰语-英语词典应用 `tsk`，最初使用 Go 语言和 Trie 数据结构实现前缀搜索，但受限于芬兰语的复杂屈折变化，Trie 在处理数千万词条时内存占用过高（约 60 MB）。为解决此问题，作者曾临时采用 SQLite 数据库存储词形变化，导致应用体积膨胀至 3 GB。

经过九个月的软件工程实践，作者决定用 Rust 重写，并利用 BurntSushi 开发的 `fst` 库（有限状态转换器）。FST 通过共享前后缀压缩数据，特别适合芬兰语这类高度黏着语的词形变化。最终，应用体积从 3 GB 缩减至 10 MB，实现了 300 倍的空间优化，同时保持了快速搜索性能。

这一改进得益于 FST 的静态数据加载特性，避免了运行时内存开销。作者强调，早期采用“不完美但可行”的 SQLite 方案为后续优化奠定了基础，体现了“解决问题两次”的价值——通过实践积累经验，最终找到更优解。
