# How I Vibe Coding?
- URL: https://xuanwo.io/2025/03-how-i-vibe-coding/
- Added At: 2025-06-26 14:45:27

## TL;DR


开源Rust工程师Xuanwo基于Zed编辑器和Claude Code构建AI辅助编码工作流，通过Docker部署并配置快捷指令"claudex"简化使用。他将AI视为需指导的初级开发者，分时段管理日程：上午用Obsidian整理思路，下午通过Zed处理代码并用git worktree协作。强调代码审查与Rust工具链验证，建议采用Claude 4（因工具使用能力），拒绝MCP架构设计，保持开发自主性，推荐相关实践指南。

## Summary


作者是开源Rust工程师（Xuanwo），基于自身背景（开源、Rust语言特性、工程师职业需求），构建了稳定的AI辅助编码工作流。其核心工具是Zed编辑器与Claude Code，通过Docker容器部署Claude Code并配置目录挂载（`claudex`别名简化使用）。将AI视为初级开发者，强调需提供上下文和方向指导，自身承担最终责任。每日分两阶段：上午用Obsidian整理思路，下午通过Zed运行Claude Code处理代码，使用`git worktree`管理协作。注重代码审查（聚焦API设计与复杂逻辑），依赖Rust的工具链（cargo check/test等）辅助验证。关键建议包括：Claude 4是当前最优编码模型（因工具使用能力），拒绝MCP架构（推荐直接调用本地工具），保持工作流自主性而非迁就AI工具。推荐阅读包含两位工程师的实操经验总结。
