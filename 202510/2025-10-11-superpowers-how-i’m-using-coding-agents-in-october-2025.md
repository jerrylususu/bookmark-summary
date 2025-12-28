# Superpowers: How I’m using coding agents in October 2025
- URL: https://simonwillison.net/2025/Oct/10/superpowers/
- Added At: 2025-10-11 13:40:18

## TL;DR
Jesse Vincent开发了Superpowers插件，通过TDD、流程图、情感日志等系统化方法优化Claude Code使用。该插件轻量开源，支持根因追踪等功能，帮助开发者提升编码效率。

## Summary
开发者在代码编程过程中，借助Claude Code这类编码助手，通过系统化方法提升效率。文章重点介绍了Jesse Vincent的经验和工具Superpowers插件，内容可总结为以下要点。

1. **Jesse的创新实践**
   - 采用高效流程，包括TDD（先验证测试失败）、步骤规划、自更新笔记和使用“情感日志”。
   - 大量实验Graphviz DOT图，以流程图形式指导Claude处理调试任务。

2. **Superpowers插件的发布**
   - 基于Claude Code新插件功能，将Jesse的技巧打包为开源插件。
   - 安装方式简单：通过命令行添加插件源并安装。
   - 插件包含多种技能，如根因追踪，帮助开发者逆向追踪bug源头。

3. **Token使用优化**
   - 插件核心轻量，仅占用少量token，通过脚本按需加载内容。
   - 使用子代理处理高token任务（如实现代码），以控制上下文长度。

4. **额外发现**
   - 文中提及Claude的`/mnt/skills/public`文件夹功能，可用于扩展技能。

总体而言，Jesse的实践展示了编码助手的高级用法，Superpowers插件为社区提供了实用工具，值得开发者借鉴。
