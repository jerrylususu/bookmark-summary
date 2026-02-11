# Introducing Showboat and Rodney, so agents can demo what they’ve built
- URL: https://simonwillison.net/2026/Feb/10/showboat-and-rodney/
- Added At: 2026-02-11 12:16:29
- Tags: #read #agent

## TL;DR
本文介绍了两个新工具Showboat和Rodney，用于帮助编码代理向人类展示其构建成果。Showboat通过生成包含命令输出和图像的Markdown文档来演示工作，而Rodney则是一个CLI浏览器自动化工具，用于网页交互和截图。这两个工具旨在弥补自动化测试的不足，通过手动验证增强对代理工作成果的信任。

## Summary
本文介绍了作者为解决编码代理（coding agents）演示其构建成果的挑战而开发的两个新工具：Showboat 和 Rodney。

**核心问题**：在使用编码代理时，如何让它们不仅测试自己构建的软件，还能向人类监督者有效演示成果。这需要超越自动化测试的工件，以清晰展示代理生成软件的实际能力。

**Showboat**：
- 是一个 CLI 工具（Go 二进制文件，可选 Python 包装），帮助代理构建 Markdown 文档来演示其工作。
- 通过命令序列（如 `init`、`note`、`exec`、`image`）逐步创建文档，自动包含命令输出和图像。
- 设计为代理使用，通过 `--help` 提供完整使用说明，代理可自行学习使用。
- 示例展示了如何用它演示 curl、jq 等功能，以及在其他项目中的应用。
- 注意：代理可能作弊直接编辑 Markdown 文件，而非通过工具执行命令。

**Rodney**：
- 一个 CLI 浏览器自动化工具，专为与 Showboat 协同工作而设计。
- 基于 Go 库 Rod（Chrome DevTools 协议封装），提供 CLI 接口，支持启动 Chrome、打开页面、执行 JavaScript、点击元素、截图等操作。
- 同样为代理设计，通过 `--help` 提供使用说明。
- 示例展示了如何用它进行网页交互和截图，并集成到 Showboat 文档中。

**测试与手动验证**：
- 尽管测试驱动开发（TDD）有助于代理编写必要代码，但自动化测试通过并不保证软件实际工作。
- Showboat 和 Rodney 旨在提供手动验证的途径，让开发者亲眼看到软件运行。

**开发背景**：
- 两个工具均通过 Claude iPhone 应用在手机上开发，体现了移动设备在编码代理辅助下的开发潜力。
- 工具最初为异步编码代理环境（如 Claude Code for the web）设计，目前效果良好。

**总结**：Showboat 和 Rodney 通过生成演示文档和浏览器自动化，帮助编码代理向人类展示其构建成果，弥补了自动化测试的不足，增强了对代理工作成果的信任。
