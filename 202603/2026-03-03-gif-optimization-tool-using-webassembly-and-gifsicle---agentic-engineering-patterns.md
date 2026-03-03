# GIF optimization tool using WebAssembly and Gifsicle - Agentic Engineering Patterns
- URL: https://simonwillison.net/guides/agentic-engineering-patterns/gif-optimization/
- Added At: 2026-03-03 14:13:48
- Tags: #read #agent

## TL;DR
作者利用Claude Code代理工具，基于Gifsicle构建了支持拖拽上传、参数调整和预览下载的GIF优化网页应用。通过自然语言提示高效完成开发、测试与集成，展示了AI代理在复杂任务中的实用性。

## Summary
本文介绍了作者如何利用Claude Code代理工具，基于Gifsicle工具构建一个基于WebAssembly的GIF优化网页应用。作者首先说明了自己常使用GIF动画演示，但GIF文件通常较大，因此选择Gifsicle作为优化工具。由于Gifsicle是命令行工具，作者希望有一个网页界面以便在浏览器中预览和调整设置。

作者通过向Claude Code提供简要提示，成功生成了一个完整的网页应用。该应用支持拖拽上传GIF、展示多种优化设置下的预览效果，并提供下载功能。此外，应用还包含手动调整参数的控件，如优化级别、颜色数量、损失压缩等。

作者还强调了代理工具在调试和测试中的优势，例如使用Rodney工具进行浏览器自动化测试，帮助发现并修复了CSS显示问题。最后，作者补充了后续提示，要求包含构建脚本、WASM捆绑包以及对Gifsicle的致谢，确保项目完整且符合开源规范。

整个过程展示了如何通过自然语言提示高效利用AI代理工具完成复杂开发任务，包括编译C代码到WebAssembly、构建用户界面以及集成测试。
