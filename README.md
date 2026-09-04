# Bookmark Summary 
读取 bookmark-collection 中的书签，使用 jina reader 获取文本内容，然后使用 LLM 总结文本。详细实现请参见 process_changes.py。需要和 bookmark-collection 中的 Github Action 一起使用。

## Latest 10 Summaries

- (2026-09-04) [How we make AI coding more cost efficient without sacrificing task quality](202609/2026-09-04-how-we-make-ai-coding-more-cost-efficient-without-sacrificing-task-quality.md)
  - GitHub Copilot通过四项优化降低编码代理成本：选择性压缩噪声、移除行号、精简提示词、直接返回后台任务结果。强调从整体任务完成衡量，局部省token可能引发更多恢复操作。改动均经离线与在线实验验证，核心是移除模型不必要工作。
  - Tags: #read #agent

- (2026-09-04) [What Makes LLM Tokenization Slow?](202609/2026-09-04-what-makes-llm-tokenization-slow.md)
  - 文章通过优化GPT-2分词器发现，性能瓶颈在于海量微小操作而非单步复杂度。采用直接处理字节、利用token ID与排名关系及边界向量后，BPE合并开销大幅下降，正则匹配成为新瓶颈。流式分词与并行化收益有限。
  - Tags: #read #llm

- (2026-09-02) [Sing-song: a speakable encoding for long numbers and keys](202609/2026-09-02-sing-song-a-speakable-encoding-for-long-numbers-and-keys.md)
  - 文章介绍了 Sing-song 编码方案，用 16 辅音×4 元音组成 CV 音节表示 6 比特，具有可逆、前缀稳定、自定长度和可发音等特点，适合人类朗读与记忆，并应用于 Nostr 用户名生成等场景。
  - Tags: #read

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

## Monthly Archive

- [2026-09](202609/monthly-index.md) (5 entries)
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
