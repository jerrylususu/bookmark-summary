# Making XML human-readable without XSLT
- URL: https://jakearchibald.com/2025/making-xml-human-readable-without-xslt/
- Added At: 2025-11-06 14:08:44
- Tags: #read #frontend
- [Link To Text](2025-11-06-making-xml-human-readable-without-xslt_raw.md)

## TL;DR
本文指出XSLT在现代浏览器中已趋于淘汰，建议优先使用服务器端将XML转换为HTML。若需客户端处理，可用JavaScript动态生成HTML，或通过CSS简单样式化XML，但功能有限。

## Summary
本文讨论了在不使用XSLT的情况下，使XML数据在浏览器中可读的多种方法，重点在于XSLT的现状、替代方案和客户端转换技术。

### XSLT的现状
- **XSLT简介**：XSLT是一种用于转换XML的语言，可将XML转换为HTML等非XML格式，浏览器原生支持约25年前的XSLT版本。
- **使用率低**：XSLT在现代浏览器中使用率极低，甚至低于已移除的功能（如突变事件和Flash），且常引发安全漏洞。
- **浏览器立场**：Chrome、Safari和Firefox均支持从浏览器引擎中移除XSLT，因维护成本高且需求不足。

### XSLT的替代方案
- **服务器端转换**：最佳实践是在服务器或构建过程中将XML转换为HTML，优势包括：
  - 提高爬虫和抓取工具的可见性。
  - 支持流式渲染，提升用户体验。
  - 工具选择灵活，不受浏览器限制。
- **示例**：作者博客通过`<link rel="alternate">`标签提供RSS feed，同时发布HTML和XML版本。

### 客户端转换方法
1. **仅用CSS样式化XML**：
   - 使用`<?xml-stylesheet type="text/css" href="styles.css"?>`可应用CSS，但功能有限（无法动态插入内容或处理语义）。
   - 适用于简单场景，如显示提示信息（如RSS feed的友好提示）。
2. **JavaScript转换**：
   - **原理**：在XML文档中嵌入HTML脚本元素（需指定`xmlns`属性），通过JavaScript解析XML数据并动态生成HTML。
   - **步骤**：
     - 获取XML根元素。
     - 创建HTML元素并替换原XML内容。
     - 使用模板函数（如作者的自定义`html`函数）生成HTML结构，确保元素语义和可访问性。
   - **注意事项**：需使用`createElementNS`创建HTML元素（而非`createElement`），以避免生成无效的XML元素。
   - **优势**：调试方便，工具支持完善，可替代XSLT实现相同效果。

### 总结
- 客户端XSLT转换可能被浏览器弃用，建议优先选择服务器端处理。
- 若必须在客户端处理，JavaScript方案更灵活可靠，但需注意元素命名空间等细节。
- 作者提供了完整演示代码，展示如何用JavaScript实现XML到HTML的转换。
