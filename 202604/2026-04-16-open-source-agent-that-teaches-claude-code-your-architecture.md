# Open-Source Agent That Teaches Claude Code Your Architecture
- URL: https://jonno.nz/posts/open-source-agent-that-teaches-claude-code-your-architecture/
- Added At: 2026-04-16 13:24:50
- Tags: #read #agent

## TL;DR
domain-agents 是一个开源工具，通过静态分析 TypeScript 代码库识别业务域并生成上下文，帮助 AI 编程助手理解系统架构和依赖关系，提升代码的可扩展性。它采用五种信号分析合并域簇，并与 Claude Code 和 Cursor 集成，实现自动上下文加载，支持 AI 辅助开发的规模化。

## Summary
本文介绍了一个名为 domain-agents 的开源工具，旨在解决 AI 编程助手在构建软件时缺乏架构意识的问题。作者指出，当前 AI 工具（如 Claude Code、Cursor）虽然能高效定位代码，但无法理解业务域之间的关系和系统演化路径，导致生成的代码难以适应未来的扩展需求。

domain-agents 通过静态分析 TypeScript 代码库，识别业务域并生成上下文文件，使 AI 助手在开发时能加载相关域的架构信息（如依赖关系、耦合度、扩展阶段）。工具采用五种信号分析（结构、导入图、命名模式、依赖映射、接口检测）来合并域簇，并通过 glob 规则和 MCP 服务器与 Claude Code 和 Cursor 集成，实现自动上下文加载。

作者强调，这种域代理模型模拟了工程团队的所有权模式，随着产品增长，代理可按业务域拆分，帮助 AI 辅助开发规模化。工具已通过端到端测试验证准确性，并支持零运行时开销的自动激活。
