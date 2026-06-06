# Bookmark Summary 
读取 bookmark-collection 中的书签，使用 jina reader 获取文本内容，然后使用 LLM 总结文本。详细实现请参见 process_changes.py。需要和 bookmark-collection 中的 Github Action 一起使用。

## Latest 10 Summaries

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

- (2026-05-30) [统计十讲](202605/2026-05-30-%E7%BB%9F%E8%AE%A1%E5%8D%81%E8%AE%B2.md)
  - 本文批评当前统计教育重理论轻实践，提出以“数据=模型+误差”为核心，通过“统计十讲”系列文章，以问题导向和模拟演示帮助读者理解统计概念，提升数据分析能力，并计划扩展为完整教材。
  - Tags: #read #deepdive #books

- (2026-05-29) [Give your agents disposable environments in Go | Tigris Object Storage](202605/2026-05-29-give-your-agents-disposable-environments-in-go-tigris-object-storage.md)
  - 本文介绍在Go中为AI代理创建可丢弃沙盒环境，利用Tigris桶分叉技术实现文件系统隔离，集成WebAssembly工具并验证POSIX兼容性，确保安全隔离与自动销毁。
  - Tags: #read #agent

- (2026-05-29) [Dancing mad with sandboxing](202605/2026-05-29-dancing-mad-with-sandboxing.md)
  - Kefka是一个Go原生沙箱，模拟操作系统环境，通过虚拟文件系统和WebAssembly技术安全运行不受信任的代码（如AI代理），支持Python等工具，确保隔离与兼容性。
  - Tags: #read #deepdive

- (2026-05-29) [AI 裁员潮卑鄙生存指南 The Unethical Guide to Surviving AI Layoffs](202605/2026-05-29-ai-%E8%A3%81%E5%91%98%E6%BD%AE%E5%8D%91%E9%84%99%E7%94%9F%E5%AD%98%E6%8C%87%E5%8D%97-the-unethical-guide-to-surviving-ai-layoffs.md)
  - 文章以讽刺手法，提出一套在AI裁员潮中“卑鄙生存”的指南，核心是主动拥抱并利用AI热潮保全自己，包括成为激进拥护者、发起转型、举办工作坊、争取资源、停止实际工作等策略，最终呼吁读者加入这场表演以求生存。
  - Tags: #read

- (2026-05-27) [用好AI的第二步：先写Skill再执行](202605/2026-05-27-%E7%94%A8%E5%A5%BDai%E7%9A%84%E7%AC%AC%E4%BA%8C%E6%AD%A5%EF%BC%9A%E5%85%88%E5%86%99skill%E5%86%8D%E6%89%A7%E8%A1%8C.md)
  - 该错误源于参数验证问题，系统无法解析域名“skill-first.html”，属客户端请求错误（代码40001，状态码400）。建议检查URL拼写及域名有效性。
  - Tags: #read #agent

## Monthly Archive

- [2026-06](202606/monthly-index.md) (2 entries)
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
