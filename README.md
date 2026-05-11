# Bookmark Summary 
读取 bookmark-collection 中的书签，使用 jina reader 获取文本内容，然后使用 LLM 总结文本。详细实现请参见 process_changes.py。需要和 bookmark-collection 中的 Github Action 一起使用。

## Latest 10 Summaries

- (2026-05-11) [Index 1,600,000,000 Keys with Automata and Rust - Andrew Gallant's Blog](202605/2026-05-11-index-1%2C600%2C000%2C000-keys-with-automata-and-rust---andrew-gallant%27s-blog.md)
  - 本文介绍基于有限状态机（FSM）的高效字符串索引方法，通过Rust的`fst`库实现有序集合与映射的压缩存储与快速查询。实验表明，该技术在压缩率和查询速度上优于传统工具，适用于静态大规模数据，但不支持频繁更新。
  - Tags: #read #data #deepdive #rust

- (2026-05-11) [Replacing a 3 GB SQLite database with a 10 MB FST (finite state transducer) binary](202605/2026-05-11-replacing-a-3-gb-sqlite-database-with-a-10-mb-fst-%28finite-state-transducer%29-binary.md)
  - 作者用 Rust 和 FST 库重写芬兰语-英语词典应用，将体积从 3GB 压缩至 10MB，实现 300 倍空间优化，同时保持搜索性能。
  - Tags: #read #hack

- (2026-05-09) [OpenAI's WebRTC Problem - Media over QUIC](202605/2026-05-09-openai%27s-webrtc-problem---media-over-quic.md)
  - 本文批评OpenAI在语音AI中使用WebRTC，指出其在产品适配、缓冲、扩展性等方面存在根本问题，主张短期用WebSocket、长期采用基于QUIC的协议（如MoQ）作为更优替代方案。
  - Tags: #read #backend

- (2026-05-09) [The unreasonable effectiveness of HTML — examples](202605/2026-05-09-the-unreasonable-effectiveness-of-html-%E2%80%94-examples.md)
  - 本文介绍了20个针对不同工作场景的HTML文件，将传统文档转化为交互式网页，涵盖探索规划、代码审查、设计等九大类，提升可读性与实用性。
  - Tags: #read #agent #tips

- (2026-05-08) [Improving token efficiency in GitHub Agentic Workflows](202605/2026-05-08-improving-token-efficiency-in-github-agentic-workflows.md)
  - 本文介绍了GitHub优化Agentic Workflows令牌使用的方法，包括统一数据收集、自动审计与改进建议。通过移除未用工具和替换数据获取操作，令牌使用量显著下降，如Auto-Triage Issues减少62%。文章还提出有效令牌指标以标准化成本计算，最终实现显著成本节约。
  - Tags: #read #agent

- (2026-05-08) [Behind the Scenes Hardening Firefox with Claude Mythos Preview – Mozilla Hacks - the Web developer blog](202605/2026-05-08-behind-the-scenes-hardening-firefox-with-claude-mythos-preview-%E2%80%93-mozilla-hacks---the-web-developer-blog.md)
  - Mozilla利用Claude Mythos Preview等AI模型构建智能代理测试框架，结合模糊测试动态生成可复现用例，在Firefox 150版本中发现271个漏洞（含180个高危），显著提升漏洞检测效率，为软件安全提供新策略。
  - Tags: #read #security #agent #llm

- (2026-05-08) [Agent pull requests are everywhere. Here's how to review them.](202605/2026-05-08-agent-pull-requests-are-everywhere.-here%27s-how-to-review-them..md)
  - AI代理生成的PR激增，审查需警惕技术债务。建议结构化流程：检查CI、代码重复、关键路径逻辑，并借助工具辅助，平衡效率与质量。
  - Tags: #read #guide

- (2026-05-08) [用Agent评测思路管理AI Coding —— 31万行代码AI重构的实践](202605/2026-05-08-%E7%94%A8agent%E8%AF%84%E6%B5%8B%E6%80%9D%E8%B7%AF%E7%AE%A1%E7%90%86ai-coding-%E2%80%94%E2%80%94-31%E4%B8%87%E8%A1%8C%E4%BB%A3%E7%A0%81ai%E9%87%8D%E6%9E%84%E7%9A%84%E5%AE%9E%E8%B7%B5.md)
  - 美团技术团队通过Agent评测完成31万行代码重构，核心经验包括：先团队共识再AI约束、技术债渐进式消化、工程师角色转向设计AI工程环境。行动指南涵盖盘清技术债、制定规范、主R打样推广及建立Pre-PR机制。
  - Tags: #read #agent #deepdive #guide

- (2026-05-08) [一根上流滚动条的诞生](202605/2026-05-08-%E4%B8%80%E6%A0%B9%E4%B8%8A%E6%B5%81%E6%BB%9A%E5%8A%A8%E6%9D%A1%E7%9A%84%E8%AF%9E%E7%94%9F.md)
  - 作者为博客设计了自定义滚动条，采用Canvas绘制提升性能，加入平滑动画、触屏优化及目录嵌入功能，同时反思了可访问性问题，分享了开发挑战与未来展望，但暂不计划开源。
  - Tags: #read #frontend #design

- (2026-05-08) [Notes on incidents](202605/2026-05-08-notes-on-incidents.md)
  - 文章指出事件处理应避免仓促干预，优先依靠系统自愈能力，采取简单措施并依赖深入的系统知识。强调冷静、果断与团队协作，而非英雄主义，以赢得政治信誉并提升效率。
  - Tags: #read

## Monthly Archive

- [2026-05](202605/monthly-index.md) (34 entries)
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
