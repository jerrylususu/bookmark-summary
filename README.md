# Bookmark Summary 
读取 bookmark-collection 中的书签，使用 jina reader 获取文本内容，然后使用 LLM 总结文本。详细实现请参见 process_changes.py。需要和 bookmark-collection 中的 Github Action 一起使用。

## Latest 10 Summaries

- (2026-09-01) [The story of Bram Cohen and the BitTorrent protocol](202609/2026-09-01-the-story-of-bram-cohen-and-the-bittorrent-protocol.md)
  - 本文讲述布拉姆·科恩发明BitTorrent的故事。该协议本为解决带宽难题，却颠覆文件分享。尽管公司商业化屡遭失败，协议本身却广泛用于合法分发与文化保存，证明开放协议的影响力远胜商业包装。
  - Tags: #read

- (2026-09-01) [Unit testing with wrapture - Graham Dumpleton](202609/2026-09-01-unit-testing-with-wrapture---graham-dumpleton.md)
  - 文章通过订单服务测试对比了unittest.mock与wrapture。wrapture主张包装真实代码而非替换，可记录真实调用、断言私有方法、参数及顺序，并在真实逻辑上微调；mock则因替换无法观察内部调用且签名宽松。wrapture更严格，但可与mock共存。
  - Tags: #read #python

- (2026-08-31) [Just a rumour of a bug is enough to find a security exploit these days](202608/2026-08-31-just-a-rumour-of-a-bug-is-enough-to-find-a-security-exploit-these-days.md)
  - AI代理让漏洞利用自动化，开源安全禁运模式失效：攻击者仅凭漏洞传闻即可在几分钟内复现利用。作者以自身OCaml库为例，提出超级私密补丁、无禁运持续发布、协议层主动防护等思路，呼吁重建安全响应流程。
  - Tags: #read #security

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

## Monthly Archive

- [2026-09](202609/monthly-index.md) (2 entries)
- [2026-08](202608/monthly-index.md) (39 entries)
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
