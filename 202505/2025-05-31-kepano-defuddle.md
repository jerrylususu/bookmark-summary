# kepano/defuddle
- URL: https://github.com/kepano/defuddle
- Added At: 2025-05-31 11:10:20
- [Link To Text](2025-05-31-kepano-defuddle_raw.md)

## TL;DR


Defuddle是一个基于MIT协议的网页内容提取工具，支持清理冗余元素生成干净HTML或Markdown，特别优化数学公式、代码块和脚注。相比Mozilla Readability更宽容，保留结构数据并提取标题、作者、发布时间等元信息。兼容浏览器（无依赖）和Node.js环境（需jsdom），提供多种配置选项如选择器过滤和格式转换，项目持续维护中。

## Summary


Defuddle是一个用于提取网页主要内容的工具，采用MIT许可证，目前在GitHub上获得2k星标和48个Forks。它通过去除广告、侧边栏、页脚等冗余元素，生成更易阅读的干净HTML文档，尤其注重为Obsidian Web Clipper等工具提供优化的输入。项目支持多种环境，可通过Playground在线体验（https://kepano.github.io/defuddle/）。

**核心功能**：  
支持提取文章标题、作者、描述、发布时间、主要图片及元数据（包括schema.org数据），并可输出带单词统计和解析耗时的信息。相比Mozilla Readability，Defuddle更宽容，保留更多结构元素，利用移动版样式推测冗余内容，并优化数学公式、代码块和脚注的标准化输出。

**使用场景与安装**：  
- 浏览器环境：直接引入无依赖的`defuddle`核心包。  
- Node.js环境：需额外安装`jsdom`，使用`defuddle/node`.bundle。  
可通过npm安装：`npm install defuddle`。

**使用方式**：  
1. 在浏览器中导入并解析当前页面：  
   ```javascript
   import Defuddle from 'defuddle';
   const result = new Defuddle(document).parse();
   ```  
2. 在Node中通过JSDOM解析URL或HTML字符串：  
   ```javascript
   import { JSDOM } from 'jsdom';
   import { Defuddle } from 'defuddle/node';
   const dom = await JSDOM.fromURL('https://example.com');
   const result = await Defuddle(dom);
   ```

**输出内容结构**：  
返回对象包含文章标题、正文、作者、描述、域名、favicon地址、主要图片、元标签、解析耗时、发布时间、网站名称、schema元数据等属性，其中正文默认输出为HTML格式，支持转换为Markdown。

**bundle类型**：  
- **核心版**：基础功能，适合大多数用例，不包含数学公式转换依赖。  
- **完整版**：支持MathML与LaTeX互转（依赖`mathml-to-latex`等库）。  
- **Node适配版**：专为服务器环境设计，通过JSDOM解析网页。

**配置选项**：  
包括启用调试日志（`debug`）、指定原始URL（`url`）、输出Markdown格式（`markdown`或`separateMarkdown`）、过滤特定选择器（`removeExactSelectors`/`removePartialSelectors`）。

**HTML标准化规则**：  
- 标题：自动降级H1为H2，若首级标题与页面标题重复则删除。  
- 代码块：剥离高亮样式及行号，添加语言标识的class和data属性。  
- 脚注：统一转换为特定HTML格式，便于后续处理。  
- 数学公式：标准化为MathML格式，保留原始LaTeX表达式供调用。

**项目状态**：  
当前版本为May 19, 2025的0.6.4，支持TypeScript开发，主分支为`main`。已进行多次功能迭代，包括数学公式处理、元数据提取等优化。项目由10位贡献者维护，主要实现语言为TypeScript（95.8%）。
