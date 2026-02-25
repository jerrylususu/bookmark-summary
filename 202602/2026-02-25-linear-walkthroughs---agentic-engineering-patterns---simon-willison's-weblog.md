# Linear walkthroughs - Agentic Engineering Patterns - Simon Willison's Weblog
- URL: https://simonwillison.net/guides/agentic-engineering-patterns/linear-walkthroughs/
- Added At: 2026-02-25 14:52:46
- Tags: #read #agent #tips

## TL;DR
本文介绍了使用编码代理（如Claude Code）结合Showboat工具进行线性代码库走查的工程模式。通过实际案例，作者展示了如何自动读取SwiftUI应用代码、生成包含代码片段的文档，从而避免手动错误并深入理解代码结构和语言细节。该模式不仅适用于代码理解，还能将小型项目转化为学习新生态系统和技巧的机会。

## Summary
本文介绍了使用编码代理进行线性代码库走查的工程模式。作者通过一个实际案例展示了如何利用Claude Code和Showboat工具，对一个自己通过“vibe coding”创建的SwiftUI演示应用进行代码理解。具体步骤包括：让代理读取源代码并规划详细的线性走查，然后使用Showboat的`note`和`exec`命令生成包含代码片段的文档。这种方法有效避免了手动复制代码可能带来的错误，并帮助作者深入理解了SwiftUI应用结构和Swift语言细节。文章强调，这种模式不仅能帮助理解现有代码，还能将即使是小型项目转化为学习新生态系统和技巧的机会。
