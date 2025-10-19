# Diskcache, more than caching
- URL: https://www.bitecode.dev/p/diskcache-more-than-caching
- Added At: 2025-10-19 13:40:42
- [Link To Text](2025-10-19-diskcache,-more-than-caching_raw.md)

## TL;DR
Diskcache是基于SQLite的Python键值存储库，支持缓存、事务、标签、队列、锁等高级功能，适用于多进程并发环境。具备函数缓存、防惊群机制和流量控制等工具，轻量高效，适合中小型应用开发。

## Summary
Diskcache 是一个基于 SQLite 的 Python 本地键值存储库，不仅能提供高效的缓存功能，还支持事务、标签、队列、锁等高级特性，适用于多进程并发环境。

**核心功能：**
- **基础缓存**：支持键值存储、自动序列化、过期时间和透明键淘汰，访问速度快（微秒级）。
- **事务支持**：通过 `cache.transact()` 实现原子操作，避免并发竞态条件。
- **标签与元数据**：可为键添加标签（如 "odd"/"even"），并基于标签批量操作（如淘汰特定标签的键）。
- **队列和双端队列**：提供类似列表的 push/pull 操作，以及 `Deque` 类支持高效首尾访问和旋转。
- **多进程并发**：通过 `FanoutCache` 分片机制避免 SQLite 写入锁冲突，支持多 worker 场景（如 FastAPI、Django）。

**高级工具：**
- **函数缓存**：`@cache.memoize()` 装饰器缓存函数结果，`memoize_stampede` 避免缓存失效时的惊群效应（多个进程同时重算）。
- **锁机制**：提供互斥锁、可重入锁、信号量等，确保资源安全访问。
- **流量控制**：`@diskcache.throttle` 限制函数调用频率（如每 3 秒一次）。

**应用场景：**
- 快速脚本、中小型网站缓存（内置 Django 后端）。
- 组合使用锁和队列实现简易任务队列，或通过键过期和布隆过滤器构建防滥用系统。

Diskcache 结合 SQLite 的稳健性和丰富功能，为轻量级应用提供了可组合的解决方案，无需引入复杂系统即可应对常见并发需求。
