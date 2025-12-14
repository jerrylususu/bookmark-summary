# Bookmark Summary 
读取 bookmark-collection 中的书签，使用 jina reader 获取文本内容，然后使用 LLM 总结文本。详细实现请参见 process_changes.py。需要和 bookmark-collection 中的 Github Action 一起使用。

## Latest 10 Summaries

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

- (2025-12-09) [使用Nano Banana Pro生成整套PPT：疯狂，挑战和工作流](202512/2025-12-09-%E4%BD%BF%E7%94%A8nano-banana-pro%E7%94%9F%E6%88%90%E6%95%B4%E5%A5%97ppt%EF%BC%9A%E7%96%AF%E7%8B%82%EF%BC%8C%E6%8C%91%E6%88%98%E5%92%8C%E5%B7%A5%E4%BD%9C%E6%B5%81.md)
  - 本文介绍了使用Nano Banana Pro生成PPT的工作流，从传统拼凑转向整体渲染，解决了风格不一致、内容不可靠等问题。通过工程化方法构建可复用的生成引擎，交付生成能力而非静态成品，实现高效、统一的幻灯片制作。
  - Tags: #read #llm #guide

- (2025-12-08) [Adding unpack syntax to RCL](202512/2025-12-08-adding-unpack-syntax-to-rcl.md)
  - RCL v0.11.0引入解包功能，通过（列表/集合）和（字典）语法简化数据结构拼接。设计解决了推导冗长与联合运算符格式化问题，在保持简洁性的同时明确了集合与字典的语义差异，提升了代码可读性。
  - Tags: #read #language #design

- (2025-12-08) [576 - Using LLMs at Oxide / RFD / Oxide](202512/2025-12-08-576---using-llms-at-oxide-rfd-oxide.md)
  - 文章总结了大型语言模型在阅读、编辑、写作、代码审查、调试和编程等场景下的应用，强调LLM应作为辅助工具而非替代品。关键在于平衡效益与风险，注意数据隐私、内容真实性和人类主导作用，避免过度依赖。
  - Tags: #read #llm #guide

- (2025-12-08) [EchoGram: The Hidden Vulnerability Undermining AI Guardrails](202512/2025-12-08-echogram-the-hidden-vulnerability-undermining-ai-guardrails.md)
  - 新型攻击EchoGram可绕过AI护栏检测，通过在提示中添加少量翻转令牌序列，可误导防御模型错误放行恶意内容或产生误报。其漏洞源于公共数据训练缺陷，广泛影响主流模型。研究呼吁开发动态防御机制，减少对静态训练数据的依赖。
  - Tags: #read #llm #security

- (2025-12-08) [Pluralistic: The Reverse-Centaur’s Guide to Criticizing AI (05 Dec 2025) – Pluralistic: Daily links from Cory Doctorow](202512/2025-12-08-pluralistic-the-reverse-centaur%E2%80%99s-guide-to-criticizing-ai-%2805-dec-2025%29-%E2%80%93-pluralistic-daily-links-from-cory-doctorow.md)
  - Cory Doctorow指出，AI热炒的背后是大型科技公司为维持股市增长制造的泡沫，而非真实创新。AI技术可能导致人类沦为机器附庸，且因统计模型本质存在局限。他反对技术取代人力的宿命论，主张通过抵制劣质AI产品和阶级合作应对危害，而非依赖版权限制。
  - Tags: #read

## Monthly Archive

- [2025-12](202512/monthly-index.md) (29 entries)
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
