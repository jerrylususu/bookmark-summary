# Introducing RSC Explorer — overreacted
- URL: https://overreacted.io/introducing-rsc-explorer/
- Added At: 2025-12-19 14:24:37
- Tags: #read #deepdive #frontend

## TL;DR
本文介绍了开源工具RSC Explorer，它通过可视化方式帮助开发者理解React Server Components协议。该工具模拟RSC通信，展示组件序列化、异步渲染、动态组件加载及服务器动作调用等场景，旨在提供无需网络请求的教育体验。

## Summary
本文介绍了作者发布的工具 RSC Explorer，旨在帮助开发者直观理解 React Server Components（RSC）协议的工作原理。RSC 协议是 React 用于序列化和反序列化组件树的内部格式，但由于其未公开文档化，开发者往往难以深入理解。

作者指出，近期 RSC 的安全漏洞事件引发了对该协议的关注，促使他开发了 RSC Explorer。该工具是一个开源的单页应用，完全在浏览器中运行，模拟 RSC 的通信过程，无需网络请求，使用真实的 React 包进行协议读写。

文章通过多个示例演示工具功能：
- **Hello World**：展示如何将 JSX 元素（如 `<h1>Hello</h1>`）通过 RSC 协议传输并在客户端重构。
- **异步组件**：体现流式渲染，使用 `<Suspense>` 处理组件加载状态，显示“Pending”占位符直至数据填充。
- **计数器**：说明 RSC 发送的是“虚拟 DOM”（如 `<Counter>` 组件），而非静态 HTML，客户端通过模块引用动态加载代码。
- **表单操作**：演示客户端调用服务器端动作（Server Action），如异步函数 `greet` 的交互过程。
- **路由刷新**：展示无框架下的 RSC 实现，通过服务器动作刷新内容，保留客户端状态（如计时器状态不变，仅更新属性）。

工具还提供其他示例链接，如分页、错误处理和漏洞演示（CVE-2025-55182），并支持代码嵌入和共享。作者鼓励社区贡献更多案例，强调工具为业余项目，旨在教育目的。
