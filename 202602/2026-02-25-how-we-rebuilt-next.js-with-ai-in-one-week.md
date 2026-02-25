# How we rebuilt Next.js with AI in one week
- URL: https://blog.cloudflare.com/vinext/
- Added At: 2026-02-25 15:03:02
- Tags: #read #agent #deepdive

## TL;DR
Cloudflare 工程师利用 AI 在一周内基于 Vite 重构了 Next.js，开发出 vinext。该框架性能更优（构建快 4.4 倍，包体积小 57%），并创新引入流量感知预渲染技术。项目证明了 AI 在严格规范下能高效重构复杂系统，目前处于实验阶段。

## Summary
**背景与动机**
Next.js 是流行的 React 框架，但在 serverless 生态中部署存在挑战。现有方案如 OpenNext 通过适配 Next.js 的构建输出来解决，但这种方式脆弱且维护成本高。Next.js 自身的适配器 API 仍处于早期，且开发环境（`next dev`）仅限于 Node.js，无法直接测试 Cloudflare 平台特定 API。

**解决方案：vinext**
Cloudflare 工程师使用 AI 在一周内重建了 Next.js，项目名为 **vinext**。它是一个直接基于 Vite 的替代实现，而非包装器。它提供了与 Next.js 相同的 API 表面（路由、SSR、RSC、中间件等），并利用 Vite 的环境 API 实现跨平台运行。用户只需将 `next` 替换为 `vinext`，即可无缝使用现有项目结构。

**性能表现**
早期基准测试显示，在相同应用下：
*   **构建速度**：使用 Vite 8（Rolldown）时，比 Next.js 16 快 4.4 倍。
*   **客户端包大小**：比 Next.js 小 57%。
*   **部署**：单命令 `vinext deploy` 即可构建并部署到 Cloudflare Workers，支持 ISR（增量静态再生）和 Cloudflare KV 缓存。

**创新特性：流量感知预渲染 (TPR)**
针对 Next.js 构建时预渲染所有页面导致的构建时间过长问题，vinext 引入了 **Traffic-aware Pre-Rendering**。它在部署时分析 Cloudflare 的流量数据，仅预渲染实际访问量大的页面（例如覆盖 90% 流量的 184 个页面），其余页面按需 SSR 并缓存。这显著减少了构建时间，尤其适用于拥有大量页面的站点。

**AI 如何实现这一挑战**
*   **可行性**：Next.js 拥有完善的文档、庞大的用户基础和详尽的测试套件，为 AI 提供了清晰的规范。Vite 作为坚实的基础，处理了复杂的构建工具链。
*   **开发过程**：一名工程师通过与 AI（Claude）协作，定义架构并分配任务。AI 编写了几乎所有代码，但工程师负责架构决策、优先级排序和纠错。项目建立了严格的测试（1700+ Vitest，380+ Playwright E2E）、类型检查和代码审查流程。
*   **成本与效率**：整个项目耗时不到一周，API 令牌成本约 1100 美元。这证明了在拥有良好规范和测试套件的前提下，AI 能够高效重构复杂软件系统。

**现状与展望**
vinext 目前处于实验阶段，已通过大量测试并有客户在生产环境使用。它支持 ISR，但暂不支持构建时静态预渲染（已在路线图中）。Cloudflare 希望与其他托管提供商合作，扩展 vinext 的部署目标。该项目展示了 AI 如何减少对人类认知辅助层（中间框架）的依赖，直接基于规范和基础工具构建软件。
