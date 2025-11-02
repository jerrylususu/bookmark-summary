# Scraping Next.js web sites in 2025 – Trickster Dev
- URL: https://www.trickster.dev/post/scraping-nextjs-web-sites-in-2025/
- Added At: 2025-11-02 11:12:07
- [Link To Text](2025-11-02-scraping-next.js-web-sites-in-2025-–-trickster-dev_raw.md)

## TL;DR
文章介绍了使用Python库njsparser抓取Next.js网站的方法，重点解析其Flight Data等数据序列化格式。工具可简化从HTML中提取分块数据的过程，适用于现代前端框架的数据抓取场景。

## Summary
本文讨论了2025年如何抓取使用Next.js构建的网站，重点解析了Next.js特有的数据序列化方式及其处理方法。

### Next.js与数据序列化背景
- **React与Next.js**：React是主流前端框架，用于构建交互式UI。Next.js是基于React的全栈框架，提供路由、性能优化和服务器端渲染（SSR）等功能。SSR在初始页面加载时将数据嵌入HTML，以支持客户端React的水合过程。
- **数据嵌入方式**：
  - 传统方法：页面常包含`<script id="__NEXT_DATA__">`标签，内含完整JSON数据，便于抓取。
  - 新方法：使用React Server Components时，数据被分块序列化为React特有的线路格式，通过`self.__next_f.push()`函数调用嵌入页面，这称为Next.js Flight Data，结构更复杂。

### 数据抓取与解析方法
- **挑战**：Flight Data的格式非标准JSON，直接解析困难。
- **解决方案**：使用开源Python库**njsparser**（项目地址：https://github.com/novitae/njsparser）。该库专为解析Next.js Flight Data设计，可提取分块数据。
- **代码示例**：
  - 基础用法：通过`njsparser.BeautifulFD()`解析HTML，使用`find_iter()`迭代数据块（如`njsparser.T.Data`类型），提取目标字段（如用户信息）。
  - 扩展功能：支持代理设置和URL动态输入，便于测试和调试。解析后数据为嵌套Python对象，需遍历结构提取所需内容。
- **CLI工具**：njsparser附带命令行工具，可检测页面是否包含Flight Data或`__NEXT_DATA__`，并列出相关页面路径。

### 总结
- 对于依赖Next.js的网站，抓取者需适应其数据嵌入方式。njsparser库简化了Flight Data的解析，使Python爬虫能有效提取结构化数据。作者以非前端开发者视角，提供了实用工具和代码示例，助开发者应对现代Web抓取挑战。
