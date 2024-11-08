# Building My Resume in HTML using Eleventy by Michael Engen
- URL: https://michaelengen.com/posts/my-eleventy-resume/
- Added At: 2024-11-08 14:20:20
- [Link To Text](2024-11-08-building-my-resume-in-html-using-eleventy-by-michael-engen_raw.md)

## TL;DR
作者通过HTML和CSS构建简历，利用Eleventy生成器和JSON数据，实现灵活布局和可访问性，并自动化PDF生成，项目已开源。

## Summary
1. **简历构建动机**：
   - 作者多年来多次重构简历，尝试了多种方法，包括LaTeX和可视化编辑器。
   - 寻找满足以下条件的简历构建方式：
     - 开发体验愉快。
     - 内容和布局适合版本控制。
     - 输出易于访问。

2. **技术选择**：
   - 选择HTML和CSS作为简历构建技术，因为它们是网页原生技术，允许灵活的布局和良好的可访问性。
   - CSS的最新进展，如CSS嵌套和基于网格的布局，增强了开发和格式化能力。

3. **HTML和CSS的优势**：
   - 网页原生文档允许在线托管简历，适应各种浏览器和字体大小。
   - HTML的语义元素提供有意义的文档结构，有助于可访问性。
   - CSS的广泛使用和社区热情带来了丰富的文档和指南。

4. **PDF生成**：
   - 尽管Indeed等求职平台不接受HTML文档，但可以通过浏览器打印为PDF，使用CSS的打印样式调整布局。

5. **构建过程**：
   - 使用Eleventy静态站点生成器，分为三个主要步骤：
     1. 编写简历数据。
     2. 使用HTML结构化数据。
     3. 使用CSS样式化结构。

6. **数据处理**：
   - 使用JSON格式存储简历数据，符合JSON Resume schema。
   - 数据通过Eleventy的数据瀑布机制注入HTML模板。

7. **模板使用**：
   - 使用Liquid模板语言，通过`{{ myVariable }}`和`{% include "file.ext" %}`语法插入数据和文件内容。
   - 简历分为四个部分：头部/联系信息、摘要、相关工作经验和正式教育。
   - 每个部分使用独立的模板，传递所需数据。

8. **设计布局**：
   - 设计单列内容布局，保持主要内容宽度适中，不影响可读性。
   - 使用CSS网格布局，将部分标签放在页面左侧的沟槽中。
   - 通过CSS子网格实现标签和内容的列对齐。
   - 使用媒体查询调整窄视口下的布局。

9. **开发体验**：
   - 使用Eleventy生成简历HTML文件，通过本地服务器实时预览和编辑。
   - 使用Puppeteer自动化工具从命令行打印PDF。

10. **项目分享**：
    - 项目已上传至GitHub，供感兴趣的人参考。
    - 提供了其他HTML简历构建方法的参考链接。
