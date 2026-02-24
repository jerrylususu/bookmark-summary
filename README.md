# Bookmark Summary 
读取 bookmark-collection 中的书签，使用 jina reader 获取文本内容，然后使用 LLM 总结文本。详细实现请参见 process_changes.py。需要和 bookmark-collection 中的 Github Action 一起使用。

## Latest 10 Summaries

- (2026-02-24) [我的退休计划：把无期变成有期](202602/2026-02-24-%E6%88%91%E7%9A%84%E9%80%80%E4%BC%91%E8%AE%A1%E5%88%92%EF%BC%9A%E6%8A%8A%E6%97%A0%E6%9C%9F%E5%8F%98%E6%88%90%E6%9C%89%E6%9C%9F.md)
  - 这篇文章批判传统“安全”观念，提出通过建立可转移资产和财务规划，将上班视为“无期徒刑”的状态转变为可量化的“有期”退休目标，核心是摆脱被迫出卖时间的雇佣关系，实现时间与劳动的定价权自由。
  - Tags: #read #money

- (2026-02-24) [CLAUDE.md: Best Practices Learned from Optimizing Claude Code with Prompt Learning](202602/2026-02-24-claude.md-best-practices-learned-from-optimizing-claude-code-with-prompt-learning.md)
  - 本文介绍了通过Prompt Learning技术优化Claude Code系统提示的方法。该方法利用LLM分析训练集表现并生成详细反馈，通过元提示迭代优化系统提示。实验表明，在SWE Bench基准测试中，优化后的提示使通用编码能力提升5.19%，针对特定代码库的优化效果更显著，提升达10.87%。该方法无需修改底层模型，仅通过优化提示即可提升性能。
  - Tags: #read #agent

- (2026-02-24) [Stop Using /init for AGENTS.md](202602/2026-02-24-stop-using-init-for-agents.md.md)
  - 本文批判自动生成的做法，指出其信息冗余会降低代理性能并增加成本。文章主张采用分层结构，仅包含非可发现信息，并建议将其视为动态的“活清单”以推动代码库改进，而非静态配置。
  - Tags: #read #llm #agent #tips

- (2026-02-24) [We hid backdoors in ~40MB binaries and asked AI + Ghidra to find them - Quesma Blog](202602/2026-02-24-we-hid-backdoors-in-~40mb-binaries-and-asked-ai-%2B-ghidra-to-find-them---quesma-blog.md)
  - 该研究评估AI代理在二进制逆向工程中检测后门的能力。通过构建BinaryAudit基准测试，发现最佳模型检测成功率仅49%，且误报率高达28%，表明当前AI辅助分析仍不成熟，无法作为生产环境的可靠安全工具，但可为开发者提供初步审计支持。
  - Tags: #read #agent #security

- (2026-02-24) [What's so hard about continuous learning?](202602/2026-02-24-what%27s-so-hard-about-continuous-learning.md)
  - 连续学习指模型部署后持续更新权重，但面临技术难题、微调无效、安全风险和可移植性差等障碍，核心难点在于自动避免性能退化，目前仍需人工干预，尚未成熟。
  - Tags: #read #llm

- (2026-02-24) [Writing about Agentic Engineering Patterns](202602/2026-02-24-writing-about-agentic-engineering-patterns.md)
  - Simon Willison启动了“代理工程模式”项目，旨在系统化记录使用编码代理（如Claude Code）进行软件开发的实践。该项目与“氛围编程”区分，聚焦专业工程师如何利用代理提升效率。目前发布了两章，探讨代码生成成本和测试驱动开发，并计划以每周1-2章的速度更新，内容由作者撰写，使用LLM辅助校对。
  - Tags: #read #agent #books

- (2026-02-21) [以一个简单任务为例看AI落地的关键决策](202602/2026-02-21-%E4%BB%A5%E4%B8%80%E4%B8%AA%E7%AE%80%E5%8D%95%E4%BB%BB%E5%8A%A1%E4%B8%BA%E4%BE%8B%E7%9C%8Bai%E8%90%BD%E5%9C%B0%E7%9A%84%E5%85%B3%E9%94%AE%E5%86%B3%E7%AD%96.md)
  - 该错误表明URL参数无效，因域名无法解析，通常因缺少协议或域名格式错误。建议检查并修正URL格式，确保其为完整有效地址。
  - Tags: #read #llm #agent

- (2026-02-20) [The First 10-Year Evolution of Stripe’s Payments API](202602/2026-02-20-the-first-10-year-evolution-of-stripe%E2%80%99s-payments-api.md)
  - Stripe支付API历经十年演变，从简单信用卡支付起步，逐步支持多种支付方式。为应对复杂性，Stripe先后推出Source API和PaymentMethod/PaymentIntent新架构，通过统一状态机简化集成。这一过程揭示了API设计需平衡易用性与功能，并强调避免产品债务、保持一致性等原则，最终实现简单性与强大功能的统一。
  - Tags: #read #api #deepdive

- (2026-02-20) [bliki: Open Space](202602/2026-02-20-bliki-open-space.md)
  - Open Space 是一种自组织会议方法，由 Harrison Owen 开发，核心是提供基本框架，由参与者自行提议和安排主题，强调自主性和流动性，适用于不同规模的活动，能提高参与度并减少组织工作。
  - Tags: #read

- (2026-02-20) [Fragments: February 18](202602/2026-02-20-fragments-february-18.md)
  - Martin Fowler在2026年2月18日的“Fragments”系列文章中，探讨了AI对软件开发的影响。文章指出AI是现有流程的“加速器”，会放大优缺点，因此传统工程实践（如TDD）更为关键。文章总结了行业现状、工作模式转变（更看重通才）、代码质量与安全的重要性、开发流程的调整以及未来成本的不确定性。作者强调开发者应冷静应对，专注于最大化AI效益并控制成本。
  - Tags: #read

## Monthly Archive

- [2026-02](202602/monthly-index.md) (48 entries)
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
