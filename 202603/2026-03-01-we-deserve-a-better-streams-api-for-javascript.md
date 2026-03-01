# We deserve a better streams API for JavaScript
- URL: https://blog.cloudflare.com/a-better-web-streams-api/
- Added At: 2026-03-01 08:20:35
- Tags: #read #deepdive #frontend #api

## TL;DR
本文剖析了 JavaScript Web Streams API 的设计缺陷，如过度仪式感、锁机制复杂、BYOB 低效、背压脱节及 Promise 开销大，导致性能与易用性问题。作者认为需基于现代语言特性重构，以提供更高效的替代方案。

## Summary
这篇文章深入剖析了当前 JavaScript Web Streams API（WHATWG Streams Standard）存在的根本性问题，并提出了一个基于现代 JavaScript 语言特性的替代方案。作者认为，Web Streams 的设计受限于其制定时的技术背景（如缺乏 `async iteration`），导致其在易用性、性能和资源管理上存在难以通过增量改进修复的缺陷。

文章的核心观点与问题总结如下：

### 1. Web Streams 的设计缺陷

*   **过度的仪式感（Excessive Ceremony）**：
    *   由于 Web Streams 标准制定早于 ES2018 的 `for await...of`，其原生 API 强制开发者手动管理 Reader、锁（Lock）和 `{ value, done }` 协议。
    *   虽然后来通过 `for await...of` 支持了异步迭代，但这只是在原有复杂架构上的“补丁”，并未解决底层的复杂性，且高级功能（如 BYOB 读取）仍无法通过迭代器使用。

*   **锁机制（The Locking Problem）**：
    *   Web Streams 使用显式的锁模型（`getReader()`/`releaseLock()`）来防止多消费者读取。
    *   **易错性**：忘记释放锁会导致流永久锁定，且错误信息难以追踪。
    *   **复杂性**：锁的状态管理（包括与 `pipeTo` 的交互）给实现者带来了巨大的内部簿记开销和边缘情况处理负担。

*   **BYOB（Bring Your Own Buffer）的复杂性**：
    *   旨在优化内存的 BYOB 读取，实际上引入了极高的复杂性（专用的 Reader 类型、`ArrayBuffer` 分离语义）。
    *   **低回报**：由于 API 复杂且无法与迭代器结合，实际采用率极低。
    *   **实现负担**：实现者必须同时处理默认读取和 BYOB 读取路径，导致代码极其冗长且容易出错。

*   **背压（Backpressure）机制的理论与实践脱节**：
    *   **缺乏强制力**：`desiredSize` 仅是建议值，`controller.enqueue()` 即使在缓冲区溢出时仍能成功执行。
    *   **特定 API 的缺陷**：`tee()` 操作在分支读取速度不一致时会导致无界内存增长；`TransformStream` 的背压信号传递存在间隙，容易导致管道阻塞。
    *   **开发者忽视**：由于背压信号是非强制的，许多开发者选择忽略它，导致在高负载下性能恶化。

*   **隐藏的 Promise 开销**：
    *   Web Streams 在热路径（hot paths）中大量创建 Promise，用于缓冲管理、协调和背压信号。
    *   **性能杀手**：在高频率流处理（如视频、网络包）或管道传输中，Promise 的分配和垃圾回收（GC）开销巨大。
    *   **对比**：作者引用 Vercel 的研究指出，原生 Web Streams 的 `pipeThrough` 性能可能比优化后的 Node.js `pipeline` 低 12 倍，主要差距就在于 Promise 和对象分配。

### 2. 现实世界中的失败案例

*   **资源耗尽**：`fetch()` 返回的响应体是流，如果未显式消费或取消，可能持有底层连接引用，导致连接池耗尽（如 Node.js `undici` 曾出现的问题）。`Request.clone()` 会隐式调用 `tee()`，进一步加剧了资源管理的复杂性。
*   **内存悬崖**：`tee()` 的内部缓冲机制在分支消费速度不一致时会导致内存激增，不同浏览器和运行时的实现策略各异，缺乏统一的内存限制。
*   **SSR（服务端渲染）中的 GC 抖动**：在流式 SSR 中，成千上万的小 HTML 片段通过流传输，每个片段都会触发 Promise 创建和对象分配，导致严重的 GC 压力，甚至可能抵消流式传输的性能优势。

### 3. 运行时的“优化跑步机”与合规负担

*   **非标准优化**：为了获得可用的性能，Node.js、Deno、Bun 和 Cloudflare Workers 都不得不实施非标准的内部优化（如 Bun 的 "Direct Streams"、Cloudflare 的 `IdentityTransformStream`）。
*   **碎片化**：这些优化导致了运行时之间的行为不一致，破坏了代码的可移植性。
*   **合规负担**：复杂的规范导致了庞大的测试套件（Web Platform Tests），实现者需要花费大量精力来通过合规性测试，而不是专注于性能和易用性。

### 结论

作者认为，Web Streams 的设计决策（锁模型、Promise 依赖、推式背压等）是其性能和易用性问题的根源。虽然运行时可以通过内部优化来缓解，但这导致了碎片化和不可持续的复杂性。

文章最后暗示，需要一种**从根本上不同的设计**，利用现代 JavaScript 语言原生特性（如原生异步迭代），来构建一个更高效、更符合直觉的流 API，从而摆脱当前的“优化跑步机”。
