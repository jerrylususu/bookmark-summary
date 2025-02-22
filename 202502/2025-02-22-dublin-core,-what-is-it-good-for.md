# Dublin Core, what is it good for?
- URL: https://www.thisdaysportion.com/posts/dublin-core-what-is-it-good-for/
- Added At: 2025-02-22 10:56:20
- [Link To Text](2025-02-22-dublin-core,-what-is-it-good-for_raw.md)

## TL;DR
文章讨论了多种元数据模式（如Dublin Core、Schema.org、Microformats、Open Graph）及其应用场景，指出Open Graph在社交媒体中的广泛支持，而Schema.org在搜索和学术服务中表现良好。建议根据具体需求支持多种模式，以覆盖不同的服务和使用场景。

## Summary
1. **概述**：
   - 文章讨论了几种流行的元数据模式（如Dublin Core、Schema.org、Microformats和Open Graph）及其用途，指出Open Graph可能是最广泛支持的，但如果要被特定服务抓取，可能需要做一些研究，或者支持多种模式。

2. **元数据模式的定义**：
   - 元数据模式允许我们在网页中嵌入结构化信息，如文章、博客文章或书评的详细信息。
   - 这些信息包括发布日期、作者等基本信息，以及出版商、版权、类别和关键词等扩展信息。
   - 元数据使计算机更容易找到这些信息，并且可以添加一些不总是显示在页面上的信息，如版权。

3. **如何添加元数据**：
   - 有两种基本方法可以将文档信息添加到HTML中：
     - **添加到文档头部**：使用`<meta>`标签，添加`name`和`content`对来设置元数据。标准的非技术项目包括`description`、`author`和`keywords`。
     - **使用属性或类添加到HTML**：使用Microformats通过定义的类在HTML中添加元数据，或者使用Schema.org的`itemscope`、`itemtype`和`itemprop`属性。

4. **可用的元数据模式**：
   - **主要模式**：
     - Schema.org
     - Microformats
     - Dublin Core
     - Open Graph
     - HTML默认值
   - 选择的模式决定了如何添加元数据，Dublin Core和Open Graph将数据添加到文档头部，Microformats使用HTML类，而Schema.org可以在头部和正文中使用。

5. **元数据的使用场景**：
   - 元数据在许多服务中被使用，包括：
     - 稍后阅读服务（如Pocket、Instapaper、Omnivore）
     - Google搜索和社交媒体链接片段
     - 启用webmentions（一种自动化独立网站与社交媒体账户之间通信的协议）
     - 学术服务（如Zotero，一个参考文献和书目应用程序）

6. **实际使用中的元数据支持情况**：
   - 通过测试不同版本的同一文档，发现不同服务对元数据模式的支持各不相同。
   - **Instapaper**：仅部分支持Schema.org的`itemprop`属性。
   - **Omnivore**：支持主要的元数据模式，包括Schema.org的`json`。
   - **Zotero**：对Dublin Core和Open Graph有较好的支持。

7. **社交网络和搜索结果中的元数据使用**：
   - 社交媒体主要使用Open Graph元数据来格式化链接。
   - 谷歌搜索结果主要依赖页面`<title>`和`<meta name="description">`来构建摘要。

8. **选择元数据模式的建议**：
   - 答案取决于具体需求，可能需要支持多种元数据模式。
   - 如果要在社交媒体上生成格式化的链接，Open Graph是首选。
   - 如果支持Schema.org，建议在正文中使用`itemprop`属性，因为其支持度在样本测试中更好。
   - 由于存在多种元数据模式和不同年龄的服务，要覆盖所有需求可能需要添加大量元数据。
