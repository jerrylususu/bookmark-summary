# Setting up a codebase for working with coding agents
- URL: https://simonwillison.net/2025/Oct/25/coding-agent-tips/
- Added At: 2025-10-27 14:10:31
- [Link To Text](2025-10-27-setting-up-a-codebase-for-working-with-coding-agents_raw.md)

## TL;DR
为提高AI编程效率，需要优化代码库设置，包括自动化测试、交互式测试、问题管理、轻量文档、代码质量工具和详细错误信息，这些措施同时提升项目的可维护性。

## Summary
为提高AI编程工具效率，需要优化代码库设置，重点关注以下几点：

1. **自动化测试**：采用如pytest等工具，使AI能选择性运行相关测试，并在修改后执行完整测试套件。
2. **交互式测试能力**：提供开发环境启动指南（如Web项目服务器），支持使用Playwright或curl进行实时测试。
3. **问题管理**：维护GitHub issues，并直接向AI工具（如Claude Code）提供issue链接以辅助开发。
4. **轻文档依赖**：大型语言模型可通过阅读代码快速理解项目，但文档有助于AI检查更新需求。
5. **代码质量工具**：集成linter、类型检查器和自动格式化工具，帮助AI优化代码。
6. **详细错误信息**：测试失败时，在错误消息或断言中添加详细信息，以提升AI调试效率。

总体而言，提升代码库的人类可维护性措施同样有益于AI代理。
