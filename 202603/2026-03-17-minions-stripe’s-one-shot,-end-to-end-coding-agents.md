# Minions: Stripe’s one-shot, end-to-end coding agents
- URL: https://stripe.dev/blog/minions-stripes-one-shot-end-to-end-coding-agents
- Added At: 2026-03-17 14:05:35
- Tags: #read #agent

## TL;DR
Minions是Stripe自研的无人值守编码代理系统，通过Slack等入口自动完成代码修改、测试和合并请求，每周处理超千个任务。它基于定制代理和内部工具链，适应Stripe复杂环境，提升开发效率。

## Summary
Minions 是 Stripe 自研的完全无人值守、端到端的编码代理系统，专为一次性完成任务而设计。每周有超过一千个由 Minions 生成的代码合并请求，这些代码虽经人工审查，但完全由代理生成。

**核心特点与使用方式**
- **入口集成**：工程师可通过 Slack、CLI、Web 界面或内部应用（如文档平台、工单系统）启动 Minions，最常用的是 Slack 直接调用。
- **工作流程**：从 Slack 消息开始，Minions 在隔离的开发环境（devbox）中运行，自动完成代码修改、测试、提交分支、生成符合模板的合并请求，全程无需人工干预。
- **并行化**：工程师可同时启动多个 Minions 并行处理不同任务，尤其适用于值班期间快速解决多个小问题。
- **迭代与审查**：完成后，工程师可在 Web 界面查看代理的决策和操作，若代码不完美，可手动迭代或要求 Minions 修正。

**技术实现概览**
- **环境与工具**：Minions 运行在预热的隔离 devbox 中，与 Stripe 人类工程师使用相同的开发工具链（如源码控制、CI、代码生成等），确保符合 Stripe 的复杂代码库和合规要求。
- **代理核心**：基于 Block 的开源编码代理 Goose 进行定制，混合智能代理循环与确定性操作（如 Git、测试、linting），确保遵循 Stripe 的开发规范。
- **上下文与工具**：通过 MCP（模型上下文协议）连接内部 MCP 服务器 Toolshed，获取 400 多个内部和 SaaS 工具的上下文，如文档、工单、代码搜索等。
- **反馈机制**：采用“左移反馈”策略，本地快速 lint（<5 秒），失败时自动修复；CI 阶段最多运行两轮测试，避免资源浪费，平衡速度与完整性。

**背景与动机**
Stripe 的代码库规模庞大（数亿行代码）、技术栈独特（Ruby + Sorbet）、依赖复杂，且涉及高风险金融交易。通用 LLM 代理难以直接适应，因此 Stripe 基于自身开发者生产力基础设施构建了 Minions，使其能有效处理 Stripe 特有的约束和最佳实践。

**未来展望**
Minions 已重塑 Stripe 的编码体验，证明了无人值守编码代理的可行性。Stripe 将继续探索代理编码的未来，并在第二部分深入技术实现细节。
