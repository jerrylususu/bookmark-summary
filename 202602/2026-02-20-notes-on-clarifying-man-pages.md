# Notes on clarifying man pages
- URL: https://jvns.ca/blog/2026/02/18/man-pages/
- Added At: 2026-02-20 00:27:00
- Tags: #read

## TL;DR
本文探讨了改进 man pages 可读性和实用性的设计思路，包括选项摘要、分类组织、丰富示例、目录链接和表格化数据等方法，旨在提升信息检索效率和用户体验。

## Summary
本文探讨了如何改进 man pages（手册页）的可读性和实用性。作者通过分析多个优秀 man pages 的案例，总结出以下设计思路：

1. **选项摘要（OPTIONS SUMMARY）**  
   - 在 SYNOPSIS 部分保持简洁，另设 OPTIONS SUMMARY 用一行简短说明每个选项，避免冗长的选项列表。
   - 示例：rsync man page 的设计。

2. **按类别组织选项**  
   - 将选项按功能分类（如“通用”、“启动”、“追踪”等），而非按字母顺序排列，便于用户按场景查找。
   - 示例：strace man page 的结构。

3. **内置速查表（cheat sheet）**  
   - 在 man page 中直接提供语法速查表，浓缩关键用法。
   - 示例：perlcheat man page 的 SYNTAX 部分。

4. **丰富的示例（EXAMPLES）**  
   - 提供常见用例的示例，甚至为每个选项单独举例。
   - 示例：OpenBSD 的 tail man page 和 curl man page（每个选项都有示例）。

5. **目录和内部链接**  
   - 在 HTML 版本中添加目录和超链接，方便跳转到特定章节。
   - 示例：Git man pages 的 HTML 版本（使用 AsciiDoc 生成）。

6. **表格化数据展示**  
   - 对结构化数据（如 ASCII 表）使用表格格式，提升可扫描性。
   - 示例：man ascii。

7. **GNU 的替代方案**  
   - GNU 项目倾向于维护 info 手册而非 man pages，尤其对于复杂工具（如 Bash、C 库），HTML 版本的参考手册更易用。

8. **周边工具**  
   - **tldr.sh**：社区维护的示例数据库，提供简洁用法。
   - **Dash**：Mac 文档浏览器，提供带目录的 man page 查看器。
   - **fish shell**：可自动生成 man page 补全脚本。

9. **思考与局限**  
   - man pages 格式受限，但正是这种约束激发了创意设计。
   - 作者强调示例的重要性，并邀请读者分享其他优秀 man page 案例。

总结：优秀的 man pages 应通过选项摘要、分类组织、丰富示例、目录链接和表格化数据等方式，提升信息检索效率和用户体验。
