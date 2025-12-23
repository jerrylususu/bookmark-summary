# Bookmark Summary 
读取 bookmark-collection 中的书签，使用 jina reader 获取文本内容，然后使用 LLM 总结文本。详细实现请参见 process_changes.py。需要和 bookmark-collection 中的 Github Action 一起使用。

## Latest 10 Summaries

- (2025-12-23) [从Python异步编程的剖析中体会智能体并发编程模式 - 铁蕾的个人博客](202512/2025-12-23-%E4%BB%8Epython%E5%BC%82%E6%AD%A5%E7%BC%96%E7%A8%8B%E7%9A%84%E5%89%96%E6%9E%90%E4%B8%AD%E4%BD%93%E4%BC%9A%E6%99%BA%E8%83%BD%E4%BD%93%E5%B9%B6%E5%8F%91%E7%BC%96%E7%A8%8B%E6%A8%A1%E5%BC%8F---%E9%93%81%E8%95%BE%E7%9A%84%E4%B8%AA%E4%BA%BA%E5%8D%9A%E5%AE%A2.md)
  - 本文介绍Bridgic智能体框架的并发设计，区分并发与并行，并基于Python的asyncio和多线程机制处理异步、I/O和计算任务。框架通过异步与同步Worker混合编排，简化开发并支持未来多进程扩展。
  - Tags: #read #python

- (2025-12-23) [Advent of Slop: A Guest Post by Claude](202512/2025-12-23-advent-of-slop-a-guest-post-by-claude.md)
  - AI独立解决2025年AoC编程挑战，重点优化了多个复杂算法（如几何搜索、高斯消元），将总运行时间压至1秒内，并编写了输入生成器。Claude反思了解题与优化的不同思维模式，并探讨了完成挑战时的成就感。
  - Tags: #read #llm

- (2025-12-22) [Advice For Individual Contributors](202512/2025-12-22-advice-for-individual-contributors.md)
  - 个人贡献者应通过利用自身优势、展现领导力、明确责任、定期汇报和主动与高层沟通，来实现突破性成果并提升工作影响力与职业发展。
  - Tags: #read #people

- (2025-12-22) [blog/2025/12/an-svg-is-all-you-need.mld](202512/2025-12-22-blog-2025-12-an-svg-is-all-you-need.mld.md)
  - SVG格式在科学数据可视化中具有巨大潜力，尤其适合构建持久、可交互的知识系统。它能实现数据探索和即时反馈，无需服务器支持，并与版本控制、权限管理等原则天然契合，增强了科学传播的交互性和持久性。
  - Tags: #read

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

## Monthly Archive

- [2025-12](202512/monthly-index.md) (58 entries)
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
