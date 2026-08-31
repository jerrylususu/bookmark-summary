# Bookmark Summary 
读取 bookmark-collection 中的书签，使用 jina reader 获取文本内容，然后使用 LLM 总结文本。详细实现请参见 process_changes.py。需要和 bookmark-collection 中的 Github Action 一起使用。

## Latest 10 Summaries

- (2026-08-31) [Breaking Claude Code Opus 5 Auto Mode ·  Embrace The Red](202608/2026-08-31-breaking-claude-code-opus-5-auto-mode-%C2%B7-embrace-the-red.md)
  - 作者披露针对 Claude Code Opus 5 自动模式的提示注入攻击链，借模块遮蔽实现远程代码执行，成功率 60%-80%，质疑 Anthropic 声称的 0% 注入率仅限固定基准，呼吁隔离与监控。
  - Tags: #read #agent #security

- (2026-08-31) [Selling out](202608/2026-08-31-selling-out.md)
  - 文章探讨软件工程师在职场中“出卖自己”的含义。作者分析异化、角色扮演与自欺等理论，认为应区分工作人格与真实自我，有意识地妥协并保留内心独立，避免彻底出卖灵魂或无谓牺牲。
  - Tags: #read

- (2026-08-31) [Understanding ChatGPT Work](202608/2026-08-31-understanding-chatgpt-work.md)
  - Simon Willison 通过大量实验揭示，ChatGPT Work 并非简单升级版，而是拥有开放联网、代码执行、无头浏览器、持久存储、建站、子代理和定时任务的强大云端代理环境。但 OpenAI 只谈用途不谈能力，且隐藏细节，加上提示注入风险，使其功能强大却令人困惑。
  - Tags: #read #llm #agent

- (2026-08-31) [You have to beat the models at something](202608/2026-08-31-you-have-to-beat-the-models-at-something.md)
  - 文章认为，AI编程能力提升下，工程师必须聚焦AI难以替代的价值：深度熟悉代码库与系统，纠正AI因缺乏上下文产生的无知或偏执错误；同时具备清晰有说服力的技术沟通能力。切勿只做转交AI输出的“肉代理”，否则将被淘汰。
  - Tags: #read #llm

- (2026-08-31) [WorkBuddy 成功，是因为腾讯办公套件太烂了 | 虹线](202608/2026-08-31-workbuddy-%E6%88%90%E5%8A%9F%EF%BC%8C%E6%98%AF%E5%9B%A0%E4%B8%BA%E8%85%BE%E8%AE%AF%E5%8A%9E%E5%85%AC%E5%A5%97%E4%BB%B6%E5%A4%AA%E7%83%82%E4%BA%86-%E8%99%B9%E7%BA%BF.md)
  - 文章认为 WorkBuddy 的成功源于腾讯办公“三强但散装”的结构性缺陷：会议、文档、企业微信互不从属，留下跨工具真空。它作为跨软件 Agent 补缝，从 C 端切入，腾讯 To B 弱势反而给它自由。危险在于未来被重新整合成套件。
  - Tags: #read #deepdive

- (2026-08-29) [Is Having Agents in the Room Meant to Be Chaotic? — Raft](202608/2026-08-29-is-having-agents-in-the-room-meant-to-be-chaotic-%E2%80%94-raft.md)
  - 文章以计数游戏说明现有工作空间不适配代理：代理回合制导致推理与房间变化脱节。提出代理原生空间Raft与代理体验设计AX，通过“代理收件箱”和“保留草稿”让代理自主决定注意力与发送，并强调感知同理心与行动显式化两条原则。
  - Tags: #read #agent

- (2026-08-27) [Copy-on-write git worktrees](202608/2026-08-27-copy-on-write-git-worktrees.md)
  - 利用文件系统写时复制（reflink）特性，让多个 Git worktree 共享工作文件，从而节省磁盘空间。作者通过先  创建 worktree，再以 reflink 复制已有文件，最后检出完成，并封装为  工具。
  - Tags: #read #tips

- (2026-08-26) [The end of programming — Paul Dix](202608/2026-08-26-the-end-of-programming-%E2%80%94-paul-dix.md)
  - 作者判断传统“人手写代码、逐行审查”的软件开发模式正走向终结。Bun用AI主导重写超百万行Rust、GitHub代码量指数增长等表明，AI可产出并迭代复杂软件。未来开发者将转向定义问题、设计架构和构建验证闭环，只验收最终运行结果，而非阅读代码本身。
  - Tags: #read

- (2026-08-24) [Building a software factory for AI SDK](202608/2026-08-24-building-a-software-factory-for-ai-sdk.md)
  - Vercel团队为AI SDK构建“软件工厂”，用多个专职agent自动处理issue和PR，运行于隔离沙箱，人类保留最终审批。四周后，工厂贡献25-35%合并PR，关闭超75% issues，积压大幅下降，验证了以人为核心的自动化维护模式。
  - Tags: #read #agent

- (2026-08-24) [Human judgment doesn't leave the software factory. It relocates.](202608/2026-08-24-human-judgment-doesn%27t-leave-the-software-factory.-it-relocates..md)
  - 软件工厂将重复编码交给 AI，但人类判断并未消失，而是被重新定位到定义意图、设计系统、设定质量门槛、解读验证和最终上线负责。验证不是越多越好，认知带宽有限，需动态调整自主性并保留人类所有权。代码能上线，仍需人的品味与责任。
  - Tags: #read #agent

## Monthly Archive

- [2026-08](202608/monthly-index.md) (38 entries)
- [2026-07](202607/monthly-index.md) (30 entries)
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
