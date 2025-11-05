# Bookmark Summary 
读取 bookmark-collection 中的书签，使用 jina reader 获取文本内容，然后使用 LLM 总结文本。详细实现请参见 process_changes.py。需要和 bookmark-collection 中的 Github Action 一起使用。

## Latest 10 Summaries

- (2025-11-05) [Code execution with MCP: building more efficient AI agents](202511/2025-11-05-code-execution-with-mcp-building-more-efficient-ai-agents.md)
  - 通过代码执行优化AI代理效率，将MCP工具转为代码API，使代理按需加载工具、本地处理数据。该方法大幅减少令牌消耗（如从15万降至2千），提升响应速度并增强隐私保护，但需平衡安全沙箱等实施成本。
  - Tags: #read #llm

- (2025-11-05) [A new SQL-powered permissions system in Datasette 1.0a20](202511/2025-11-05-a-new-sql-powered-permissions-system-in-datasette-1.0a20.md)
  - Datasette 1.0a20 重构了权限系统，将权限检查从逐条函数调用改为基于SQLite查询，提升效率。新系统支持层次化权限、插件扩展和资源批量过滤，并增加调试工具。版本变更较大，提供升级指南与AI辅助开发工具，目标在社区升级插件后发布1.0正式版。
  - Tags: #read #llm #tips

- (2025-11-04) [Grapheme Clusters and Terminal Emulators](202511/2025-11-04-grapheme-clusters-and-terminal-emulators.md)
  - 终端模拟器在处理Unicode字符如表情符号时，宽度计算常出现光标移动错误。问题源于传统方案依赖单字符宽度函数，无法正确处理多码位组合。解决方案是采用字形簇技术和Mode 2027协议，确保跨终端的兼容性和对全球语言支持。建议程序优先启用新模式，并动态计算文本宽度。
  - Tags: #read

- (2025-11-04) [State of Terminal Emulators in 2025: The Errant Champions · Articles](202511/2025-11-04-state-of-terminal-emulators-in-2025-the-errant-champions-%C2%B7-articles.md)
  - 2023年测试的后续更新：使用改进的ucs-detect工具评估终端Unicode支持。Ghostty和Kitty表现最佳，但终端处理零宽度字符等问题仍存挑战。文本尺寸协议有望改善复杂脚本显示，推动超越等宽限制。测试发现性能和兼容性存在差异。
  - Tags: #read #guide

- (2025-11-04) [The Case Against pgvector | Alex Jacobs](202511/2025-11-04-the-case-against-pgvector-alex-jacobs.md)
  - 文章总结了pgvector在生产环境中的核心问题：索引选择困难（IVFFlat需重建、HNSW消耗大）、实时搜索性能差、查询优化复杂、功能缺失（如混合搜索需自行实现）。作者认为尽管pgvector适合少数有专家团队的场景，但多数情况下专用向量数据库更简单经济。
  - Tags: #read #db #deepdive

- (2025-11-03) [Absurd Workflows: Durable Execution With Just Postgres](202511/2025-11-03-absurd-workflows-durable-execution-with-just-postgres.md)
  - Absurd是一个轻量级持久化执行库，仅依赖Postgres实现可靠的工作流和AI代理。它将任务分解为步骤，利用Postgres的队列和状态存储功能，在故障时支持任务重试和状态恢复，无需第三方服务，简化部署和运维。
  - Tags: #read #distributed #hack

- (2025-11-03) [New prompt injection papers: Agents Rule of Two and The Attacker Moves Second](202511/2025-11-03-new-prompt-injection-papers-agents-rule-of-two-and-the-attacker-moves-second.md)
  - 两篇AI安全论文指出提示注入仍是未解难题：Meta提出“规则二”限制AI代理权限组合以降低风险；多机构研究显示现有防御在自适应攻击下成功率超90%，验证了通过设计而非依赖防御的实用安全思路。
  - Tags: #read #llm #security

- (2025-11-03) [Using Assisted-by commit footers instead of banning AI tools](202511/2025-11-03-using-assisted-by-commit-footers-instead-of-banning-ai-tools.md)
  - 反对全面禁止AI投稿，建议要求贡献者用“Assisted-by”脚注公开使用的AI工具，便于审查与追踪，平衡创新与风险。
  - Tags: #read #llm

- (2025-11-02) [The Linux Boot Process: From Power Button to Kernel](202511/2025-11-02-the-linux-boot-process-from-power-button-to-kernel.md)
  - 计算机启动过程从CPU复位、固件自检开始，逐步解压并加载内核，切换运行模式（实模式到保护模式再到长模式），最终移交控制权给操作系统内核。
  - Tags: #read #linux #deepdive

- (2025-11-02) [Building Multi-Agent Systems (Part 2)](202511/2025-11-02-building-multi-agent-systems-%28part-2%29.md)
  - 自多智能体系统系列首篇发布以来，基于LLM的智能体架构在工具调用能力和长时间运行方面显著进步，其核心思想——任务分解和协作——已成为标准，但架构设计变得更加灵活。重点从复杂流程设计转向提供上下文和目标的“上下文工程”，使智能体更加自主。同时，新挑战出现在系统控制、安全性和长时间任务的用户体验上。
  - Tags: #read #llm

## Monthly Archive

- [2025-11](202511/monthly-index.md) (12 entries)
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
