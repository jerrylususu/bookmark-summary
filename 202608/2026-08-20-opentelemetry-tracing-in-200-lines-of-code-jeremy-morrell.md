# OpenTelemetry Tracing in 200 lines of code | Jeremy Morrell
- URL: https://jeremymorrell.dev/blog/minimal-js-tracing/
- Added At: 2026-08-20 14:01:25
- Tags: #read #deepdive #observability

## TL;DR
本文用约200行极简实现揭示分布式追踪本质：Span是带ID的日志，Trace靠ID关联，上下文传播用traceparent头，仪器化即包装代码。OpenTelemetry虽庞大但只是在此核心上增加工程化健壮性。

## Summary
这篇文章的核心观点是：**分布式追踪（Tracing）并没有想象中那么神秘，它本质上就是“花哨的日志”加上“上下文传播”**。作者通过一个约200行的最小化 JavaScript 实现，逐步展示了如何从零构建一个能工作的 tracing 库，并解释了 OpenTelemetry 背后的基本概念。

---

### 1. 从日志到 Span

开发者对日志非常熟悉。日志通常是一行带时间戳和若干键值对的记录。如果你曾经写过类似这样的辅助函数：

```js
log("user-authenticated", { userId, remainingRateLimit });
```

输出类似：
```json
{ "timestamp": ..., "name": "user-authenticated", "userId": "1234", "remainingRateLimit": 100 }
```

如果再进一步，记录某个子任务的耗时：

```js
logTiming("query-user-info", () => { db.fetchUserInfo(); });
```

那你就已经接近了 **Span** 的概念。

**Span（跨度）** 是 tracing 的基本单元，它本质上也是一组键值对，但必须有以下几个字段：

- **name**：操作名称
- **startTime** 和 **duration**：开始时间和耗时
- **trace ID**、**span ID**、**parent span ID**：用于关联和构建调用链

其他自定义属性可以放在 `attributes` 映射中。所以 Span 可以简单地用一个类来表示，并在结束时计算耗时，然后输出为 JSON。

---

### 2. Trace 是 Span 的集合

当我们处理一个请求时，会生成多个 Span（比如“处理请求”、“查询数据库”、“调用外部 API”）。这些 Span 共享同一个 **Trace ID**，但每个 Span 有自己的 **Span ID**，并且通过 **Parent Span ID** 指明自己的父 Span。这样，收集所有 Span 后就可以还原出一棵调用树（在 UI 上通常显示为瀑布图）。

在代码中，上下文（Context）只需要保存两个值：`traceID` 和当前 `spanID`。创建新 Span 时继承 `traceID`，将当前的 `spanID` 作为父 Span ID，然后生成新的 `spanID` 并更新上下文。

---

### 3. 上下文传播

上下文需要在异步操作中传递。在 Node.js 中可以使用 `AsyncLocalStorage` 来隐式地传递上下文，而不必手动传参。作者用 `startSpan` 包装一个异步函数，自动管理上下文的进入和退出，并在结束后输出 Span。

---

### 4. 分布式追踪：跨服务传递上下文

当请求从一个服务发到另一个服务时，需要把 Trace ID 和当前 Span ID 传过去。W3C 定义了 `traceparent` HTTP 头，格式为：

```
00-{trace-id}-{parent-span-id}-01
```

我们只需要在发送 HTTP 请求时添加这个头，并在接收请求时解析它，就可以跨服务串联起整个调用链。

---

### 5. 仪器化（Instrumentation）就是包装代码

“仪器化”听起来复杂，其实就是**把现有的代码包一层**，以便自动创建 Span 和传递上下文。作者展示了两个例子：

- **Hono 框架中间件**：在请求进入时解析 `traceparent`，创建根 Span，记录请求方法、路径、响应状态码等信息。
- **包装 `fetch`**：替换全局 `fetch`，自动添加 `traceparent` 头，并包裹在 Span 中，记录 URL 和响应码。

这样，开发者不需要在每个地方手动埋点，只需使用包装后的函数。

---

### 6. 导出数据：从 Honeycomb 到 OTLP

最初，作者将 Span 直接发送到 Honeycomb 的旧版 Events API，因为那只需要发送一个 JSON 对象，字段对应好即可。这再次印证了 Span 就是带有特定 ID 的日志行。

但为了与更多工具兼容，作者展示了如何将 Span 转换为 **OTLP（OpenTelemetry Protocol）** 格式。OTLP 是 OpenTelemetry 定义的标准数据格式，基于 Protobuf，也有 JSON 映射。虽然结构稍复杂（多了 resource、scope 等层级），但核心数据仍然是那些 ID、时间戳、名称和属性。

使用 OTLP 后，数据可以发送到任何支持 OpenTelemetry 的后端（如 Honeycomb、Baselime），甚至可以在本地用 `otel-desktop-viewer` 或 `otel-tui` 可视化。

---

### 7. 为什么官方 OpenTelemetry SDK 那么大？

作者用不到 200 行代码就实现了基本功能，但官方 SDK 比这大得多，因为它需要处理：

- **批量发送和缓冲**：生产环境不能每个 Span 发一次 HTTP 请求
- **跨环境支持**：浏览器和 Node.js
- **健壮的错误处理**
- **高度可配置性**
- **自动仪器化大量流行库**
- **性能优化**
- **遵循语义约定**
- **同时支持 metrics 和 logs**

这些生产级需求导致了代码量的膨胀。但核心思想并没有变：**Span 就是带有 ID 的日志，Trace 就是通过 ID 关联起来的 Span 集合，上下文传播就是把这些 ID 在服务间传递**。

---

### 总结

这篇文章的核心是破除对 tracing 的畏惧心理。通过一个极简实现，作者展示了 tracing 的本质：**花哨的日志 + 上下文传递**。理解了这一点，再看 OpenTelemetry 的复杂 API 和 SDK 就会觉得它们只是在这个简单模型上增加了工程化的健壮性、标准化和自动化。
