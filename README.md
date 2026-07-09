# Bookmark Summary 
读取 bookmark-collection 中的书签，使用 jina reader 获取文本内容，然后使用 LLM 总结文本。详细实现请参见 process_changes.py。需要和 bookmark-collection 中的 Github Action 一起使用。

## Latest 10 Summaries

- (2026-07-09) [Rewriting Bun in Rust | Bun Blog](202607/2026-07-09-rewriting-bun-in-rust-bun-blog.md)
  - Bun团队利用Claude AI在11天内将50余万行Zig代码重写为Rust，通过全部测试并根除内存安全问题，总费用16.5万美元。
  - Tags: #read #agent #deepdive

- (2026-07-09) [Clickhouse is winning the Observability Wars](202607/2026-07-09-clickhouse-is-winning-the-observability-wars.md)
  - 作者认为ClickHouse在日志可观测性中胜出，因其列式存储、高压缩比和线性扩展能力。无论数据量从1TB到10TB/日，架构几乎不变，成本可控，而其他方案或架构畸形或成本失控。前期付出换来长期简单，使其能随团队共同成长。
  - Tags: #read #arch #observability

- (2026-07-07) [Agentic Autonomy Levels](202607/2026-07-07-agentic-autonomy-levels.md)
  - 文章提出AI智能体自主性与编排双维六级框架，强调根据任务风险与可逆性校准自主性，并以证据验证为基础实现安全演进。
  - Tags: #read #agent

- (2026-07-07) [The Agent-Era Career](202607/2026-07-07-the-agent-era-career.md)
  - 本文指出，AI 擅长标准答案，而职业未来在于无标准答案之事：选择正确问题、判断产出好坏、承担最终责任，并在 AI 能力边界外继续深耕。专注不可自动化、不可打分的“难事”，是工程师最重要的策略。
  - Tags: #read #career

- (2026-07-06) [Vibe Coding 时代的角色与架构](202607/2026-07-06-vibe-coding-%E6%97%B6%E4%BB%A3%E7%9A%84%E8%A7%92%E8%89%B2%E4%B8%8E%E6%9E%B6%E6%9E%84.md)
  - AI辅助编程快速但不可替代思考、架构与协作；省时若不用来强化质量，反而加速代码腐化。人的共情、责任与系统掌控力无法被替代，真正的价值在于提出好问题、把控设计方向。
  - Tags: #read #agent

- (2026-07-05) [Better Models: Worse Tools](202607/2026-07-05-better-models-worse-tools.md)
  - 新 Claude 模型调用 Pi 工具时，常添加虚构字段导致格式错误，但内容正确。原因在于后训练过度适应 Claude Code 工具生态，对非标准 schema 适应性变差。启用严格模式或主动贴合主流惯例可缓解问题。
  - Tags: #read #agent

- (2026-07-05) [[译] 大模型训练的中场叙事：从 Reasoning Thinking 转向 Agentic Thinking (2026)](202607/2026-07-05-%5B%E8%AF%91%5D-%E5%A4%A7%E6%A8%A1%E5%9E%8B%E8%AE%AD%E7%BB%83%E7%9A%84%E4%B8%AD%E5%9C%BA%E5%8F%99%E4%BA%8B%EF%BC%9A%E4%BB%8E-reasoning-thinking-%E8%BD%AC%E5%90%91-agentic-thinking-%282026%29.md)
  - 文章指出，大模型焦点从深度推理转向智能体式行动，思考围绕行动展开；训练重心从模型本身转向模型与环境的闭环；基础设施和奖励设计是新挑战。
  - Tags: #read #agent

- (2026-07-03) [Markdown's Big Brother: Say Hello to AsciiDoc](202607/2026-07-03-markdown%27s-big-brother-say-hello-to-asciidoc.md)
  - 文章介绍AsciiDoc标记语言，它比Markdown更强，原生支持表格、条件输出等高级功能，支持模块化与变量重用。结合adoc Studio和Git，可高效协作、一键导出多格式，实现文档即代码。
  - Tags: #read #tips

- (2026-07-03) [Design Patterns Suck](202607/2026-07-03-design-patterns-suck.md)
  - 本文批评将设计模式奉为教条，指出多数模式只是弥补语言表达力不足的补丁。在灵活语言中它们自然消失，其唯一价值是作为团队沟通术语。真正的好设计在于简洁直接。
  - Tags: #read

- (2026-07-03) [Group chats rule the world](202607/2026-07-03-group-chats-rule-the-world.md)
  - 科技圈讨论正从公开平台转入私密群聊，如同餐厅后厨与永不打烊的晚宴。好的群聊需园丁式管理、精细配客、冷却棒调控、规模修剪和共同仪式，核心在于持续注入新意与幽默。
  - Tags: #read #people

## Monthly Archive

- [2026-07](202607/monthly-index.md) (13 entries)
- [2026-06](202606/monthly-index.md) (33 entries)
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
