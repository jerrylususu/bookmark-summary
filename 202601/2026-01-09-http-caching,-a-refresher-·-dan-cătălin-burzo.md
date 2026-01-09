# HTTP caching, a refresher · Dan Cătălin Burzo
- URL: https://danburzo.ro/http-caching-refresher/
- Added At: 2026-01-09 14:32:02
- Tags: #read #deepdive

## TL;DR
本文基于RFC 9111标准，解析了HTTP缓存的运行机制，包括缓存新鲜度判断、存储控制、关键Cache-Control指令及其应用场景。文章强调缓存默认启用，但需结合浏览器和中间件的实际兼容性谨慎配置。

## Summary
本文是对 RFC 9111 HTTP 缓存标准的重新梳理，重点解析缓存机制、关键指令和应用场景。以下是结构化的总结：

### 概述
HTTP 缓存通过 `Cache-Control` 头控制缓存行为，适用于浏览器私有缓存、代理和 CDN 等共享缓存。标准强调缓存应默认启用，但优先使用 `MUST NOT` 等指令防止不当存储。

### 缓存新鲜度
- **新鲜度判断**：缓存通过比较响应年龄（从服务器生成或验证起的时间）与新鲜时间线（由服务器或启发式设定）决定是否重用响应。
- **时间线来源**：优先级依次为 `max-age` 指令、`Expires` 与 `Date` 头差值、或基于 `Last-Modified` 的启发式计算。共享缓存优先使用 `s-maxage`。
- **过期处理**：过期响应可通过条件请求（如 `If-Modified-Since` 或 `If-None-Match`）验证，避免重复传输数据。

### 缓存存储机制
- **缓存键**：基于 URL 和 HTTP 方法，浏览器还引入双重键控（如顶级站点和框架来源）以保护隐私。
- **可变响应**：`Vary` 头指定影响内容的请求头（如 `Accept-Language`），确保不同变体单独缓存。但 `Vary` 可能导致低效，CDN 可能忽略或规范化它。替代方案（如 `Key` 头或 HTTP Response Variants）已被搁置，新提案 HTTP Availability Hints 正在探索。
- **去重优化**：`No-Vary-Search` 头允许忽略无关查询参数，提升缓存效率，目前仅 Chromium 浏览器支持。

### Cache-Control 响应指令
- **基础指令**：
  - `max-age`：定义新鲜时间。
  - `must-revalidate`：过期响应必须验证。
  - `no-cache`：所有响应均需验证。
  - `no-store`：禁止存储响应，但非绝对安全。
- **特殊用途**：
  - `private`：限制共享缓存，保护用户专有内容。
  - `public`：允许共享缓存存储认证响应。
  - `s-maxage`：仅作用于共享缓存的新鲜时间。
  - `immutable`：新鲜期内避免验证，但现代浏览器软重载策略已减少其必要性。
- **扩展指令**：如 `stale-while-revalidate` 和 `stale-if-error` 允许临时使用过期响应，但支持有限。

### Cache-Control 请求指令
客户端通过请求头表达偏好，如：
- `max-age`、`min-fresh`：要求响应新鲜。
- `max-stale`：接受一定程度的过期。
- `no-cache`、`no-store`：禁止使用或存储缓存。
- `only-if-cached`：仅从缓存获取响应。

### 浏览器刷新行为
- **软重载**：主流浏览器对主资源进行条件请求，子资源按缓存策略加载。
- **硬重载**：所有资源使用 `no-cache` 指令跳过缓存。
- 历史问题促使 `immutable` 指令提出，但现代浏览器已优化重载策略，降低了其必要性。

### 认证请求的缓存
共享缓存默认不存储含 `Authorization` 头的响应，除非响应包含 `public`、`s-maxage` 或 `must-revalidate` 指令。`private` 指令可反向确保认证响应不被共享缓存存储。

### 结论
文章整合了 RFC 9111 和多个实践指南，旨在澄清缓存指令的交互与用途。尽管标准演进，仍需考虑浏览器和中间件的兼容性，建议参考 HTTP Caching Tests 评估实际支持情况。
