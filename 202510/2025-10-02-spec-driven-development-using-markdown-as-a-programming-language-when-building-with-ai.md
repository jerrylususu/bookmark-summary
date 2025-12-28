# Spec-driven development: Using Markdown as a programming language when building with AI
- URL: https://github.blog/ai-and-ml/generative-ai/spec-driven-development-using-markdown-as-a-programming-language-when-building-with-ai/
- Added At: 2025-10-02 13:53:53

## TL;DR
本文提出一种基于Markdown的规格驱动开发模式，用Markdown编写应用需求与设计作为AI编程代理（如 Copilot）的输入，自动生成代码。这种方法提升文档代码一致性、支持跨语言移植，但在规模扩展和测试方面仍存挑战。

## Summary
该文章提出一种基于规格驱动的开发方法，主张使用 Markdown 作为编程语言来指导 AI 编程代理（如 GitHub Copilot）构建应用程序。传统开发流程中，开发者通过迭代式的自然语言指令与 AI 代理交互，但 AI 容易遗忘上下文或忽略先前决策。通过将应用的目的、设计决策和功能规格用 Markdown 编写成规格文件（如 `copilot-instructions.md`），AI 代理可在代码生成时持续参考该文件，提升开发的一致性。

文章以作者构建的 GitHub Brain MCP Server（Go 语言项目）为例，详细介绍了采用 Markdown 规格驱动的开发流程：

1.  **核心文件结构**：项目包含 `README.md`（用户文档）、`main.md`（AI 规格文件，描述应用逻辑和功能）、`compile.prompt.md`（触发 AI 编译 Markdown 为代码的提示文件）以及最终的 `main.go`（生成的 Go 代码）。

2.  **开发流程**：开发者编辑 `main.md` 或 `README.md` 来定义或修改应用功能，通过 AI 代理（如使用 GitHub Copilot 的 `/` 命令调用 `compile.prompt.md`）将 Markdown 规格“编译”为实际代码，然后测试运行。若出现问题，迭代更新规格文件而非直接修改代码。

3.  **优势与挑战**：
    - **优势**：确保文档与代码同步；减少重复指令；支持跨语言移植（理论上可重新生成其他语言代码）。
    - **挑战**：随着代码规模增长，编译速度可能下降；测试仍需额外处理（规格描述行为，但需测试验证）；编写清晰、无歧义的 Markdown 规格具有一定难度。

4.  **扩展工具**：文章还介绍了使用 `lint.prompt.md` 提示文件让 AI 代理优化 Markdown 规格的清晰度和一致性，类似代码整理（linting）。

5.  **未来方向**：作者计划探索将规格拆分为多模块以改善编译效率，尝试完全丢弃生成代码并跨语言重新生成应用，以及集成测试流程。

总结：这种方法将 Markdown 转变为一种“编程语言”，通过 AI 代理实现从规格到代码的自动化转换，强调声明式、文档驱动的开发模式，适用于快速迭代和跨语言项目，但仍需解决规模扩展和测试集成等实际问题。
