# Bookmark Summary 
读取 bookmark-collection 中的书签，使用 jina reader 获取文本内容，然后使用 LLM 总结文本。详细实现请参见 process_changes.py。需要和 bookmark-collection 中的 Github Action 一起使用。

## Latest 10 Summaries

- (2025-12-22) [A Year Of Vibes](202512/2025-12-22-a-year-of-vibes.md)
  - 作者回顾2025年，AI编程工具彻底改变其工作方式，从编码者转为工程领导。他体验了多款AI代理工具，扩展至日常管理，但也反思人机关系风险与行业分歧。未来需解决版本控制、代码审查及AI生成代码的伦理问题，呼吁行业关注工具演化与人机协作边界。
  - Tags: #read

- (2025-12-22) [The Shape of AI: Jaggedness, Bottlenecks and Salients](202512/2025-12-22-the-shape-of-ai-jaggedness%2C-bottlenecks-and-salients.md)
  - 文章探讨了人工智能能力的三个特性：参差不齐（AI在不同任务表现差异大），瓶颈（AI能因固有限制或流程因素难以自动化），以及突出部（关键瓶颈突破可促进AI跃进。总体认为AI扩展将带来人机协作，而非全替代，未来应关注瓶颈变化来预测发展。
  - Tags: #read #llm

- (2025-12-20) [Prompt caching: 10x cheaper LLM tokens, but how? | ngrok blog](202512/2025-12-20-prompt-caching-10x-cheaper-llm-tokens%2C-but-how-ngrok-blog.md)
  - 文章介绍了提示缓存如何通过复用语言模型的K和V矩阵，避免重复计算输入令牌，从而降低成本90%并减少延迟。OpenAI和Anthropic的缓存策略不同，但均显著提升效率，适用于长提示场景。
  - Tags: #read #llm #explainer

- (2025-12-20) [【开源】智能体编程语言ASL——重构智能体开发体验 - 铁蕾的个人博客](202512/2025-12-20-%E3%80%90%E5%BC%80%E6%BA%90%E3%80%91%E6%99%BA%E8%83%BD%E4%BD%93%E7%BC%96%E7%A8%8B%E8%AF%AD%E8%A8%80asl%E2%80%94%E2%80%94%E9%87%8D%E6%9E%84%E6%99%BA%E8%83%BD%E4%BD%93%E5%BC%80%E5%8F%91%E4%BD%93%E9%AA%8C---%E9%93%81%E8%95%BE%E7%9A%84%E4%B8%AA%E4%BA%BA%E5%8D%9A%E5%AE%A2.md)
  - ASL是一种新型智能体编程语言，专注于直观描述智能体内部结构、多智能体组合及动态工作流。其声明式语法支持嵌套模块与动态编排，解决了传统语言在结构表达上的不足，提升了开发效率和代码复用性。ASL基于Bridgic框架，将执行逻辑与结构分离，适用于动态自主系统的构建。
  - Tags: #read #llm #language

- (2025-12-20) [2025 LLM Year in Review](202512/2025-12-20-2025-llm-year-in-review.md)
  - 2025年LLM领域六大趋势：强化学习可验证奖励(RLVR)提升推理能力，智能具有不均衡性，Cursor等应用拓宽垂直领域，Claude Code推动本地化AI发展，自然语言编程降低技术门槛，以及视觉交互模型成为新方向。领域整体快速发展，潜力与挑战并存。
  - Tags: #read #llm

- (2025-12-19) [Programmers and software developers lost the plot on naming their tools](202512/2025-12-19-programmers-and-software-developers-lost-the-plot-on-naming-their-tools.md)
  - 文章批评软件工具命名过于随意，主张命名应清晰描述功能，回归专业标准，减少认知负担。
  - Tags: #read

- (2025-12-19) [GraphQL: the enterprise honeymoon is over](202512/2025-12-19-graphql-the-enterprise-honeymoon-is-over.md)
  - 文章认为GraphQL在企业应用中优势有限。尽管旨在减少数据过度获取，但多数场景已被BFF架构解决。GraphQL反而带来更高实现复杂度、可观测性差、缓存脆弱及维护成本。企业更需稳定和效率，而非技术优雅，因此GraphQL适用面窄。
  - Tags: #read

- (2025-12-19) [The Architecture of "Not Bad": Decoding the Chinese Source Code of the Void](202512/2025-12-19-the-architecture-of-not-bad-decoding-the-chinese-source-code-of-the-void.md)
  - 中文倾向以否定间接肯定（如“没错”），英语则偏好直接肯定（如“great”）。这种差异塑造了灰度思维与直接分类的认知模式，并影响社会互动与商业策略。语言不仅是表达工具，更潜在地决定了现实认知方式。
  - Tags: #read

- (2025-12-19) [AI agents are starting to eat SaaS](202512/2025-12-19-ai-agents-are-starting-to-eat-saas.md)
  - AI代理正颠覆SaaS行业，使企业更易自建定制化工具替代通用SaaS，导致后者客户增长和收入保留率下降。高可用性、网络效应等护城河强的SaaS受影响较小，但后台类工具风险最高。SaaS市场将面临重组，企业需评估技术能力以应对变化。
  - Tags: #read

- (2025-12-19) [Introducing RSC Explorer — overreacted](202512/2025-12-19-introducing-rsc-explorer-%E2%80%94-overreacted.md)
  - 本文介绍了开源工具RSC Explorer，它通过可视化方式帮助开发者理解React Server Components协议。该工具模拟RSC通信，展示组件序列化、异步渲染、动态组件加载及服务器动作调用等场景，旨在提供无需网络请求的教育体验。
  - Tags: #read #deepdive #frontend

## Monthly Archive

- [2025-12](202512/monthly-index.md) (54 entries)
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
