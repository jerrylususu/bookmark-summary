# Using LLMs and Cursor to become a finisher
- URL: https://zohaib.me/using-llms-and-cursor-for-finishing-projects-productivity/
- Added At: 2025-01-05 02:50:43
- [Link To Text](2025-01-05-using-llms-and-cursor-to-become-a-finisher_raw.md)

## TL;DR
作者在2024年通过使用LLMs和Cursor IDE显著提升了业余项目的开发效率，完成了多个项目的v1版本。他分享了项目开发流程和技巧，强调通过细化需求、快速初始化和迭代开发来保持动力，并建议读者尝试这些工具以提升项目完成效率。

## Summary
1. **背景介绍**：
   - **职业转变**：作者五年前转为工程经理，日常工作不再涉及编程，但通过业余项目保持编程技能。
   - **项目进展**：过去由于时间有限，业余项目进展缓慢，许多项目未完成。但在2024年，作者在业余项目上取得了显著进展，完成了多个项目的v1版本。

2. **项目示例**：
   - **jsonplayground.com**：一个JSON格式化工具，使用WASM在浏览器中运行JQ，确保数据不离开本地机器。
   - **webtomarkdown.com**：一个将网页内容转换为Markdown的工具，用于将内容传递给LLMs。
   - **Evergreen Soaring页面改版**：为作者志愿参与的滑翔俱乐部页面进行改版（尚未部署）。
   - **Chrome浏览器扩展**：自动化处理滑翔俱乐部收到的公共消息。
   - **fitinterval.com**：一个用于锻炼的间隔计时器。

3. **LLMs和Cursor IDE的作用**：
   - **生产力提升**：LLMs（特别是Cursor IDE）显著提升了作者在业余项目中的生产力。
   - **工具选择**：Cursor IDE是一个适合使用LLMs进行编码的编辑器。

4. **项目开发流程**：
   - **项目规划**：
     - **使用ChatGPT细化需求**：通过与ChatGPT对话，细化项目需求，生成详细的项目规格说明书（SPEC.md）。
     - **技术选择**：明确使用TypeScript、React和Tailwind CSS等技术栈。
   - **项目初始化**：
     - **使用Vite初始化项目**：通过Vite快速搭建项目基础结构。
     - **使用Cursor Agent生成初始代码**：将SPEC.md作为上下文，使用Cursor Agent生成初始代码。
   - **迭代开发**：
     - **小步迭代**：将功能拆分为小任务，逐步迭代开发。
     - **修复Bug和改进UX**：通过Cursor Composer逐步修复Bug并改进用户体验。
     - **部署设置**：使用GitHub Actions实现自动化部署。

5. **开发技巧总结**：
   - **使用LLMs细化项目细节**：通过LLMs生成详细的项目规格说明书，并存储为SPEC.md。
   - **项目初始化工具**：使用Vite等工具快速搭建项目基础结构。
   - **Cursor Composer的使用**：利用Cursor Composer（Agent模式）生成初始代码。
   - **模型选择**：结合使用o1和Claude-3.5-sonnet模型，o1用于初步功能设计，Claude-3.5-sonnet用于细节迭代。
   - **模式选择**：根据需求选择Chat、Composer（普通模式）或Composer（Agent模式）。
   - **提供上下文**：尽可能提供相关上下文（如文件、文档链接等），以提高代码生成质量。
   - **存储Markdown文件**：将项目相关的Markdown文件存储为上下文，便于后续使用。
   - **使用.cursorrules文件**：在项目目录中创建.cursorrules文件，指定代码生成时的偏好设置。
   - **理解代码**：确保对代码有高层次的理解，避免代码混乱难以调试。

6. **总结**：
   - **项目完成与部署**：通过LLMs和Cursor IDE的帮助，作者能够快速完成并部署项目的v1版本。
   - **保持动力**：通过将未完成的项目转化为已完成的项目，作者能够保持动力并逐步增加项目功能。
   - **建议**：作者建议读者尝试使用这些工具，找到适合自己的使用方式，从而提升项目完成效率。
