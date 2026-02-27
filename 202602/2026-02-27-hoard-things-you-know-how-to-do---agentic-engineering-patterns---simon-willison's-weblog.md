# Hoard things you know how to do - Agentic Engineering Patterns - Simon Willison's Weblog
- URL: https://simonwillison.net/guides/agentic-engineering-patterns/hoard-things-you-know-how-to-do/
- Added At: 2026-02-27 13:21:09
- Tags: #read #agent #tips

## TL;DR
本文介绍了“囤积已知技能”的代理工程模式，建议开发者系统收集和记录已解决的技术问题及代码示例，建立个人知识库。通过向编码代理提供已有代码参考，可快速组合生成新解决方案，从而更高效地利用AI代理加速开发过程。

## Summary
本文介绍了“囤积已知技能”这一代理工程模式。作者Simon Willison指出，软件开发的核心能力之一是了解哪些技术方案可行，并掌握实现思路。他建议开发者系统性地收集和记录已解决的技术问题及其代码示例，例如通过个人博客、GitHub仓库或LLM辅助工具（如HTML工具集）来建立自己的知识库。

这种做法的价值在于，当需要构建新工具时，可以向编码代理提供已有的工作代码作为参考，通过组合多个示例快速生成解决方案。文中以开发一个基于浏览器的PDF OCR工具为例，展示了如何将PDF转图像和图像OCR两个现有代码片段结合，通过提示词引导AI生成完整工具。随着编码代理（如Claude Code）的发展，这种模式变得更加强大，因为代理可以主动搜索、克隆代码库并复用已有技巧，使得开发者只需解决一次问题，就能通过文档和示例让代理在未来复用。

核心思想是：通过囤积可复用的代码片段和解决方案，开发者能更高效地利用AI代理，加速开发过程并拓展解决问题的可能性。
