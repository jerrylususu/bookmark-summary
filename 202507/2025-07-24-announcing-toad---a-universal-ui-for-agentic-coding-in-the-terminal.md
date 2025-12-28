# Announcing Toad - a universal UI for agentic coding in the terminal
- URL: http://willmcgugan.github.io/announcing-toad/
- Added At: 2025-07-24 15:06:49

## TL;DR


Will McGugan开发的Toad基于Textual库，通过局部刷新技术解决Claude Code和Gemini CLI界面卡顿、文本选择困难等问题。采用Python+Textual构建前端，支持多语言后端并用JSON通信，反驳Python性能质疑。架构分离前后端，可扩展至桌面/移动端，当前孵化中提供赞助体验，计划开源并探索商业化。

## Summary


Will McGugan宣布开发终端AI编码代理工具Toad，基于其之前开发的Textual库技术，旨在解决Anthropic和Google同类产品存在的界面问题。认为Claude Code和Gemini CLI因采用低效终端更新方式导致闪烁、文本选择困难及界面卡顿（jank），而Toad通过局部刷新技术实现无闪烁交互，支持精准文本选择和与历史内容互动，同时兼容多语言后端（Python+Textual构建前端，后端可自由选择）并通过JSON通信。反驳关于Python性能的质疑，认为其完全胜任终端应用，并强调Textual在TUI开发中的优势。项目采用前端后端分离架构，支持未来扩展桌面、移动或远程服务端模式。当前为孵化阶段，开源前接受赞助提前体验，计划通过社区协作完善功能，并探索商业化可能性。
