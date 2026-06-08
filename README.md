# Bookmark Summary 
读取 bookmark-collection 中的书签，使用 jina reader 获取文本内容，然后使用 LLM 总结文本。详细实现请参见 process_changes.py。需要和 bookmark-collection 中的 Github Action 一起使用。

## Latest 10 Summaries

- (2026-06-08) [Working with product managers](202606/2026-06-08-working-with-product-managers.md)
  - 文章指出工程师与产品经理因视角差异易陷入信任危机，导致恶性循环。建立良好关系需工程师理解对方立场、可靠交付并尊重其政治角色，最终实现互信协作，避免操纵与谎言。
  - Tags: #read #career

- (2026-06-08) [Loop Engineering](202606/2026-06-08-loop-engineering.md)
  - 循环工程通过自动化提示和管理AI代理，构建递归目标循环以迭代完成任务。它包含自动化、工作树、技能、插件、子代理和记忆六大组件，虽能提升效率，但仍需人工验证与理解，避免过度依赖自动化。
  - Tags: #read #agent

- (2026-06-08) [Doing nothing at work](202606/2026-06-08-doing-nothing-at-work.md)
  - 这篇文章主张工程师应保持80%利用率，留出20%时间远离电脑，以抓住高影响力机会、避免低效忙碌。核心观点包括：保持松弛状态以关注关键任务、拒绝非优先工作，并强调在正确时间做正确事比工作时长更重要。
  - Tags: #read #career

- (2026-06-06) [AI Job Grief: The Unnamed Psychological Crisis Hitting Tech Workers](202606/2026-06-06-ai-job-grief-the-unnamed-psychological-crisis-hitting-tech-workers.md)
  - 文章探讨了AI驱动就业替代引发的“AI职业哀伤”，指出这是一种针对职业身份丧失的深层悲痛，尤其影响认知型工作者。由于缺乏社会认可和疏导机制，这种哀伤被压抑并加剧个人与组织问题。文章呼吁建立社会共识和制度支持，以应对这一系统性困境。
  - Tags: #read

- (2026-06-06) [在香港骑共享单车：访客视角的经验](202606/2026-06-06-%E5%9C%A8%E9%A6%99%E6%B8%AF%E9%AA%91%E5%85%B1%E4%BA%AB%E5%8D%95%E8%BD%A6%EF%BC%9A%E8%AE%BF%E5%AE%A2%E8%A7%86%E8%A7%92%E7%9A%84%E7%BB%8F%E9%AA%8C.md)
  - 本文介绍香港共享单车的使用经验，涵盖LocoBike和HelloRide两种类型、收费及骑行区域，重点说明新界单车径网络、导航方式、交通规则与注意事项，并推荐五条适合探索的骑行路线。
  - Tags: #read

- (2026-06-06) [Running Python code in a sandbox with MicroPython and WASM](202606/2026-06-06-running-python-code-in-a-sandbox-with-micropython-and-wasm.md)
  - 作者开发了 micropython-wasm 包，基于 MicroPython 和 WebAssembly 实现 Python 代码的安全沙箱执行，支持资源限制与会话持久化，目前已在 PyPI 发布 alpha 版本并用于 Datasette 项目。
  - Tags: #read #agent #security

- (2026-06-03) [AI enthusiasts are in a race against time, AI skeptics are in a race against entropy (xpost)](202606/2026-06-03-ai-enthusiasts-are-in-a-race-against-time%2C-ai-skeptics-are-in-a-race-against-entropy-%28xpost%29.md)
  - 文章讨论了AI在软件开发中引发的两极分化：爱好者追求快速迭代，怀疑者担忧代码质量。双方因体验和代价不同而缺乏信任。解决方案包括共享完整故事、工程化解决分歧、建立共同现实及发挥领导力作用，强调通过协作在创新与稳定间找到平衡。
  - Tags: #read #agent

- (2026-05-31) [The holes that kill you are the ones you never tested — jonno.nz](202605/2026-05-31-the-holes-that-kill-you-are-the-ones-you-never-tested-%E2%80%94-jonno.nz.md)
  - 瑞士奶酪模型虽能解释系统失效，但过度强调冗余会忽视未测试的漏洞。作者指出，冗余在故障相关时无效，可靠性受限于最不可靠依赖。建议通过混沌工程、无指责分析主动暴露漏洞，并将可靠性视为可管理预算，最终依靠文化层面的坦诚改进。
  - Tags: #read

- (2026-05-31) [Build agents, not pipelines](202605/2026-05-31-build-agents%2C-not-pipelines.md)
  - 文章对比了LLM在程序中的两种应用方式：管道（代码控制流程）和智能体（LLM自主管理）。管道更可预测、成本可控，适合简单任务；智能体更灵活，能处理复杂场景但成本不可控。建议根据任务复杂度、上下文需求和成本限制选择，不确定时优先智能体。
  - Tags: #read #agent

- (2026-05-30) [邸报 v0.1.0：一个很旧的东西新生了 | 虹线](202605/2026-05-30-%E9%82%B8%E6%8A%A5-v0.1.0%EF%BC%9A%E4%B8%80%E4%B8%AA%E5%BE%88%E6%97%A7%E7%9A%84%E4%B8%9C%E8%A5%BF%E6%96%B0%E7%94%9F%E4%BA%86-%E8%99%B9%E7%BA%BF.md)
  - 邸报 v0.1.0 是一款开源 RSS 阅读器，支持本地部署与算法推荐，优化阅读顺序并提供可解释理由。它强调数据自主，存储于本地，无需依赖中心化服务，旨在辅助用户发现内容而非替代判断。项目源于对算法主导信息分发的不满，鼓励用户参与反馈。
  - Tags: #read #tools

## Monthly Archive

- [2026-06](202606/monthly-index.md) (7 entries)
- [2026-05](202605/monthly-index.md) (70 entries)
- [2026-04](202604/monthly-index.md) (57 entries)
- [2026-03](202603/monthly-index.md) (70 entries)
- [2026-02](202602/monthly-index.md) (58 entries)
- [2026-01](202601/monthly-index.md) (67 entries)
- [2025-12](202512/monthly-index.md) (68 entries)
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
