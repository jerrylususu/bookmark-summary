# Bookmark Summary 
读取 bookmark-collection 中的书签，使用 jina reader 获取文本内容，然后使用 LLM 总结文本。详细实现请参见 process_changes.py。需要和 bookmark-collection 中的 Github Action 一起使用。

## Latest 10 Summaries

- (2025-12-15) [JustHTML is a fascinating example of vibe engineering in action](202512/2025-12-15-justhtml-is-a-fascinating-example-of-vibe-engineering-in-action.md)
  - Emil利用AI工具开发的JustHTML库实现了纯Python的高质量HTML解析器，展示了“氛围工程”理念：程序员专注架构设计与测试验证，AI承担编码实现，提升开发效率与代码可靠性。
  - Tags: #read #llm

- (2025-12-15) [Justified](202512/2025-12-15-justified.md)
  - 任务运行器“just”通过.justfile定义项目命令，实现跨平台任务自动化。支持变量、平台适配等高级功能，简化开发流程，是轻量高效的标准化工具。
  - Tags: #read

- (2025-12-14) [Jubilant: Python subprocess and Go codegen](202512/2025-12-14-jubilant-python-subprocess-and-go-codegen.md)
  - Jubilant 是利用 Python 封装 Juju CLI 的项目，通过 subprocess.run 调用 CLI 简化架构，使用代码生成确保数据模型一致，并基于 uv 和 Make 管理开发流程，体现了简洁实用的设计思路。
  - Tags: #read

- (2025-12-14) [My gift to the rustdoc team](202512/2025-12-14-my-gift-to-the-rustdoc-team.md)
  - Arborium 是为 Rust 文档网站 docs.rs 开发的语法高亮工具，支持 96 种语言，通过 tree-sitter 实现高性能解析。文章分析了三种集成方案，推荐在 docs.rs 构建时进行后端处理以兼顾性能和安全。该项目已在 GitHub 开源，旨在提升 Rust 文档的可读性。
  - Tags: #read #deepdive

- (2025-12-14) [What happens when the coding becomes the least interesting part of the work](202512/2025-12-14-what-happens-when-the-coding-becomes-the-least-interesting-part-of-the-work.md)
  - 编程代理将改变软件开发，编码不再是核心挑战，重点转向资深工程师的思考能力：问题分析、决策与权衡。资深工程师借助AI提升效率，行业结构或将精简，初级工程师面临替代风险。未来一年，即使AI停滞，变革仍将加速。
  - Tags: #read #llm

- (2025-12-14) [Skills vs Dynamic MCP Loadouts](202512/2025-12-14-skills-vs-dynamic-mcp-loadouts.md)
  - 本文比较了AI工具调用中的技能系统和MCP协议，指出技能通过简短摘要和AI自适应使用现有工具，比依赖静态定义和正则匹配的MCP更灵活高效。作者基于实践经验，倾向让AI自主维护技能，避免MCP的兼容性和成本问题，认为技能系统在当前更具优势。
  - Tags: #read #llm

- (2025-12-14) [我的独立开发者书单 2025 版 - 白宦成](202512/2025-12-14-%E6%88%91%E7%9A%84%E7%8B%AC%E7%AB%8B%E5%BC%80%E5%8F%91%E8%80%85%E4%B9%A6%E5%8D%95-2025-%E7%89%88---%E7%99%BD%E5%AE%A6%E6%88%90.md)
  - 这份2025年独立开发者书单强调务实创业，推荐七本书，涵盖财富创造、产品全流程、SEO、App开发、创业管理、小型企业运营及网站盈利，旨在帮助开发者规避错误、低成本启动并实现持续盈利。建议关注作者社交媒体获取更新。
  - Tags: #read

- (2025-12-12) [Litestream VFS](202512/2025-12-12-litestream-vfs.md)
  - Litestream VFS 是一项功能，允许用户通过SQLite的插件接口直接查询对象存储（如S3）中的SQLite备份，而无需下载整个文件。它利用LTX格式和索引优化，仅按需加载查询所需的数据页，支持历史时间点查询和快速恢复，适用于云环境临时数据库访问和容错场景。该功能只读，写操作仍由独立进程处理。
  - Tags: #read #db

- (2025-12-11) [Useful patterns for building HTML tools](202512/2025-12-11-useful-patterns-for-building-html-tools.md)
  - 该文介绍了HTML工具的定义和开发模式，强调单一文件结构，避免复杂框架，并使用CDN和浏览器原生功能实现轻量化开发。建议通过LLM辅助快速构建实用工具，并分享了具体实现技巧和示例。
  - Tags: #read #tips #deepdive #frontend

- (2025-12-09) [Prediction: AI will make formal verification go mainstream — Martin Kleppmann’s blog](202512/2025-12-09-prediction-ai-will-make-formal-verification-go-mainstream-%E2%80%94-martin-kleppmann%E2%80%99s-blog.md)
  - AI将推动形式化验证从边缘技术走向主流。原本因高成本和难度仅见于研究，但AI能大幅降低验证成本，并因自动代码生成而产生验证需求。未来挑战在于定义规范和文化接受，但形式化验证有望成为软件开发标准。
  - Tags: #read

## Monthly Archive

- [2025-12](202512/monthly-index.md) (34 entries)
- [2025-11](202511/monthly-index.md) (78 entries)
- [2025-10](202510/monthly-index.md) (67 entries)
- [2025-09](202509/monthly-index.md) (40 entries)
- [2025-08](202508/monthly-index.md) (46 entries)
- [2025-07](202507/monthly-index.md) (77 entries)
- [2025-06](202506/monthly-index.md) (75 entries)
- [2025-05](202505/monthly-index.md) (65 entries)
- [2025-04](202504/monthly-index.md) (61 entries)
- [2025-03](202503/monthly-index.md) (49 entries)
- [2025-02](202502/monthly-index.md) (32 entries)
- [2025-01](202501/monthly-index.md) (41 entries)
- [2024-12](202412/monthly-index.md) (45 entries)
- [2024-11](202411/monthly-index.md) (57 entries)
- [2024-10](202410/monthly-index.md) (34 entries)
- [2024-09](202409/monthly-index.md) (46 entries)
- [2024-08](202408/monthly-index.md) (31 entries)
- [2024-07](202407/monthly-index.md) (12 entries)
