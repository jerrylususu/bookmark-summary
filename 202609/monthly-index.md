# 2026-09 Monthly Index

- (2026-09-04) [How we make AI coding more cost efficient without sacrificing task quality](2026-09-04-how-we-make-ai-coding-more-cost-efficient-without-sacrificing-task-quality.md)
  - GitHub Copilot通过四项优化降低编码代理成本：选择性压缩噪声、移除行号、精简提示词、直接返回后台任务结果。强调从整体任务完成衡量，局部省token可能引发更多恢复操作。改动均经离线与在线实验验证，核心是移除模型不必要工作。
  - Tags: #read #agent

- (2026-09-04) [What Makes LLM Tokenization Slow?](2026-09-04-what-makes-llm-tokenization-slow.md)
  - 文章通过优化GPT-2分词器发现，性能瓶颈在于海量微小操作而非单步复杂度。采用直接处理字节、利用token ID与排名关系及边界向量后，BPE合并开销大幅下降，正则匹配成为新瓶颈。流式分词与并行化收益有限。
  - Tags: #read #llm

- (2026-09-02) [Sing-song: a speakable encoding for long numbers and keys](2026-09-02-sing-song-a-speakable-encoding-for-long-numbers-and-keys.md)
  - 文章介绍了 Sing-song 编码方案，用 16 辅音×4 元音组成 CV 音节表示 6 比特，具有可逆、前缀稳定、自定长度和可发音等特点，适合人类朗读与记忆，并应用于 Nostr 用户名生成等场景。
  - Tags: #read

- (2026-09-01) [The story of Bram Cohen and the BitTorrent protocol](2026-09-01-the-story-of-bram-cohen-and-the-bittorrent-protocol.md)
  - 本文讲述布拉姆·科恩发明BitTorrent的故事。该协议本为解决带宽难题，却颠覆文件分享。尽管公司商业化屡遭失败，协议本身却广泛用于合法分发与文化保存，证明开放协议的影响力远胜商业包装。
  - Tags: #read

- (2026-09-01) [Unit testing with wrapture - Graham Dumpleton](2026-09-01-unit-testing-with-wrapture---graham-dumpleton.md)
  - 文章通过订单服务测试对比了unittest.mock与wrapture。wrapture主张包装真实代码而非替换，可记录真实调用、断言私有方法、参数及顺序，并在真实逻辑上微调；mock则因替换无法观察内部调用且签名宽松。wrapture更严格，但可与mock共存。
  - Tags: #read #python
