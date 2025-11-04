# 2025-11 Monthly Index

- (2025-11-04) [Grapheme Clusters and Terminal Emulators](2025-11-04-grapheme-clusters-and-terminal-emulators.md)
  - 终端模拟器在处理Unicode字符如表情符号时，宽度计算常出现光标移动错误。问题源于传统方案依赖单字符宽度函数，无法正确处理多码位组合。解决方案是采用字形簇技术和Mode 2027协议，确保跨终端的兼容性和对全球语言支持。建议程序优先启用新模式，并动态计算文本宽度。
  - Tags: #read

- (2025-11-04) [State of Terminal Emulators in 2025: The Errant Champions · Articles](2025-11-04-state-of-terminal-emulators-in-2025-the-errant-champions-%C2%B7-articles.md)
  - 2023年测试的后续更新：使用改进的ucs-detect工具评估终端Unicode支持。Ghostty和Kitty表现最佳，但终端处理零宽度字符等问题仍存挑战。文本尺寸协议有望改善复杂脚本显示，推动超越等宽限制。测试发现性能和兼容性存在差异。
  - Tags: #read #guide

- (2025-11-04) [The Case Against pgvector | Alex Jacobs](2025-11-04-the-case-against-pgvector-alex-jacobs.md)
  - 文章总结了pgvector在生产环境中的核心问题：索引选择困难（IVFFlat需重建、HNSW消耗大）、实时搜索性能差、查询优化复杂、功能缺失（如混合搜索需自行实现）。作者认为尽管pgvector适合少数有专家团队的场景，但多数情况下专用向量数据库更简单经济。
  - Tags: #read #db #deepdive

- (2025-11-03) [Absurd Workflows: Durable Execution With Just Postgres](2025-11-03-absurd-workflows-durable-execution-with-just-postgres.md)
  - Absurd是一个轻量级持久化执行库，仅依赖Postgres实现可靠的工作流和AI代理。它将任务分解为步骤，利用Postgres的队列和状态存储功能，在故障时支持任务重试和状态恢复，无需第三方服务，简化部署和运维。
  - Tags: #read #distributed #hack

- (2025-11-03) [New prompt injection papers: Agents Rule of Two and The Attacker Moves Second](2025-11-03-new-prompt-injection-papers-agents-rule-of-two-and-the-attacker-moves-second.md)
  - 两篇AI安全论文指出提示注入仍是未解难题：Meta提出“规则二”限制AI代理权限组合以降低风险；多机构研究显示现有防御在自适应攻击下成功率超90%，验证了通过设计而非依赖防御的实用安全思路。
  - Tags: #read #llm #security

- (2025-11-03) [Using Assisted-by commit footers instead of banning AI tools](2025-11-03-using-assisted-by-commit-footers-instead-of-banning-ai-tools.md)
  - 反对全面禁止AI投稿，建议要求贡献者用“Assisted-by”脚注公开使用的AI工具，便于审查与追踪，平衡创新与风险。
  - Tags: #read #llm

- (2025-11-02) [The Linux Boot Process: From Power Button to Kernel](2025-11-02-the-linux-boot-process-from-power-button-to-kernel.md)
  - 计算机启动过程从CPU复位、固件自检开始，逐步解压并加载内核，切换运行模式（实模式到保护模式再到长模式），最终移交控制权给操作系统内核。
  - Tags: #read #linux #deepdive

- (2025-11-02) [Building Multi-Agent Systems (Part 2)](2025-11-02-building-multi-agent-systems-%28part-2%29.md)
  - 自多智能体系统系列首篇发布以来，基于LLM的智能体架构在工具调用能力和长时间运行方面显著进步，其核心思想——任务分解和协作——已成为标准，但架构设计变得更加灵活。重点从复杂流程设计转向提供上下文和目标的“上下文工程”，使智能体更加自主。同时，新挑战出现在系统控制、安全性和长时间任务的用户体验上。
  - Tags: #read #llm

- (2025-11-02) [How I Use Every Claude Code Feature](2025-11-02-how-i-use-every-claude-code-feature.md)
  - 本文总结了Claude Code的高效使用方法，重点包括：通过CLAUDE.md文件维护项目规范，利用上下文管理保持会话连贯，避免过度依赖自定义命令与子代理。建议结合钩子机制优化工作流，使用SDK快速开发工具，并集成GitHub Actions实现自动化。强调以实际产出为导向，逐步完善AI辅助的工程流程。
  - Tags: #read #llm #tips

- (2025-11-02) [Scraping Next.js web sites in 2025 – Trickster Dev](2025-11-02-scraping-next.js-web-sites-in-2025-%E2%80%93-trickster-dev.md)
  - 文章介绍了使用Python库njsparser抓取Next.js网站的方法，重点解析其Flight Data等数据序列化格式。工具可简化从HTML中提取分块数据的过程，适用于现代前端框架的数据抓取场景。
  - Tags: #read #frontend
