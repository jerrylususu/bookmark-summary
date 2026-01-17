# My Claude Code Workflow And Personal Tips
- URL: https://thegroundtruth.substack.com/p/my-claude-code-workflow-and-personal-tips
- Added At: 2026-01-17 06:54:00
- Tags: #read #llm #guide

## TL;DR
本文介绍作者使用Claude Code和Cursor的AI编码工作流程，核心是通过ROADMAP.md文件进行结构化规划，结合任务管理和实用技巧，提升开发效率。

## Summary
本文介绍了作者使用Claude Code（及Cursor）的编程工作流程和个人技巧。文章基于作者的实践经验，旨在提供高效利用AI编码代理的详细方法。

**核心工作流程**：作者强调使用ROADMAP.md文件作为项目规划的核心。该文件位于reference文件夹中，描述整体开发流程和每个任务的高层次概述。通过Claude Code的@语法或Cursor规则显式导入，确保代理拥有完整上下文。工作流程包括任务规划、任务创建、任务实现和路线图更新四个步骤。对于大功能，先更新ROADMAP.md添加任务概要，然后创建详细任务文件在tasks文件夹中，再让代理分步或连续实现。任务文件类似PRD和系统设计，包含背景、实现步骤、文件修改和验收标准。

**文件结构**：项目文件夹包括reference文件夹（含ROADMAP.md、AD_HOC_TASKS.md、REFACTORS.md等）和tasks文件夹（存放单个任务计划文件）。这种结构便于代理和人类访问。

**临时任务处理**：小规模增强或重构记录在AD_HOC_TASKS.md或REFACTORS.md中，可让代理逐个处理，建议每任务使用新会话以避免上下文混乱。

**个人技巧**：作者推荐使用键盘快捷键（如Option+箭头跳词）、自定义斜杠命令快速触发常用操作、通过--dangerously-skip-permissions标志绕过权限确认、利用Cursor IDE的源控制选项卡进行代码审查。Claude Code能自主工作10-20分钟，适合中等复杂度任务，但UI调试仍有局限。

**工具集成**：配合使用Cursor IDE提供诊断支持、Wispr Flow用于语音输入、ccusage监控API用量。文章还提及Claude Code的新功能如hooks，并推荐相关项目和资源，如GitHub上的示例文件。

整体上，工作流程注重规划与自动化平衡，通过结构化文件引导代理，辅以实用技巧提升效率。
