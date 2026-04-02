# Bookmark Summary 
读取 bookmark-collection 中的书签，使用 jina reader 获取文本内容，然后使用 LLM 总结文本。详细实现请参见 process_changes.py。需要和 bookmark-collection 中的 Github Action 一起使用。

## Latest 10 Summaries

- (2026-04-02) [Building More Resilient Local-First Software with atproto | jakelazaroff.com](202604/2026-04-02-building-more-resilient-local-first-software-with-atproto-jakelazaroff.com.md)
  - 本文探讨利用 atproto 协议构建本地优先软件，通过 CRDT 与个人数据服务器（PDS）实现无服务器的实时协作文本编辑。方案结合持久化、同步与实时机制，但也指出 Jetstream 等局限性。作者认为 atproto 与本地优先理念契合，并提供了简化实现的 npm 包。
  - Tags: #read #deepdive

- (2026-04-01) [解码 Agent Harness — Claude Code 架构深度剖析](202604/2026-04-01-%E8%A7%A3%E7%A0%81-agent-harness-%E2%80%94-claude-code-%E6%9E%B6%E6%9E%84%E6%B7%B1%E5%BA%A6%E5%89%96%E6%9E%90.md)
  - 本文介绍了Claude Code的架构设计，重点解析了其核心组件Agent Harness。该框架通过模块化设计实现AI代理的灵活配置与高效执行，支持代码生成、自动化测试等场景，具备可扩展性和易用性。
  - Tags: #book #agent

- (2026-04-01) [The Claude Code Source Leak: fake tools, frustration regexes, undercover mode, and more](202604/2026-04-01-the-claude-code-source-leak-fake-tools%2C-frustration-regexes%2C-undercover-mode%2C-and-more.md)
  - Anthropic因意外泄露Claude Code源代码，暴露了反蒸馏机制、隐蔽模式等技术细节及未发布产品KAIROS，核心损害在于泄露战略路线图，而非代码本身。
  - Tags: #read #agent #deepdive

- (2026-03-31) [一行代码的事，Web 为什么做了三十年还没做到](202603/2026-03-31-%E4%B8%80%E8%A1%8C%E4%BB%A3%E7%A0%81%E7%9A%84%E4%BA%8B%EF%BC%8Cweb-%E4%B8%BA%E4%BB%80%E4%B9%88%E5%81%9A%E4%BA%86%E4%B8%89%E5%8D%81%E5%B9%B4%E8%BF%98%E6%B2%A1%E5%81%9A%E5%88%B0.md)
  - 本文探讨了网页布局设计的权衡，对比了固定、流式、弹性、网格及响应式等策略的优缺点，强调需根据项目需求平衡用户体验、性能与维护性，并提供实践建议以优化开发效率。
  - Tags: #read

- (2026-03-30) [杀死那个手工程序员 - Tw93](202603/2026-03-30-%E6%9D%80%E6%AD%BB%E9%82%A3%E4%B8%AA%E6%89%8B%E5%B7%A5%E7%A8%8B%E5%BA%8F%E5%91%98---tw93.md)
  - AI技术正重塑软件开发行业，降低门槛的同时可能导致质量下降。未来程序员的核心价值将转向系统能力、工程深度与创新，而非单纯编码速度。选择做什么比如何做更重要。
  - Tags: #read #career

- (2026-03-30) [Rewriting pycparser with the help of an LLM - Eli Bendersky's website](202603/2026-03-30-rewriting-pycparser-with-the-help-of-an-llm---eli-bendersky%27s-website.md)
  - 作者使用Codex重写pycparser，将其从PLY库转为手写递归下降解析器，提升了性能并解决了维护问题。LLM显著提高了效率（4-5小时完成），但代码仍需人工审查。
  - Tags: #read #agent

- (2026-03-29) [We Rewrote JSONata with AI in a Day, Saved $500K/Year](202603/2026-03-29-we-rewrote-jsonata-with-ai-in-a-day%2C-saved-%24500k-year.md)
  - Reco公司采用AI辅助方法，用Go重写JSONata引擎，实现性能提升与成本节约，验证了AI代码生成在生产环境的可行性。
  - Tags: #read

- (2026-03-29) [The Code Agent Orchestra - what makes multi-agent coding work](202603/2026-03-29-the-code-agent-orchestra---what-makes-multi-agent-coding-work.md)
  - 本文介绍了多智能体编码从单智能体同步协作转向异步协同的范式转变，提出了三种模式（子智能体、团队、大规模编排）及质量保障、工具生态和实践方法，旨在提升编码效率与质量。
  - Tags: #read #agent

- (2026-03-29) [Using the Browser’s <canvas> for Data Compression](202603/2026-03-29-using-the-browser%E2%80%99s-canvas-for-data-compression.md)
  - 本文介绍利用  元素将数据编码为像素并导出为 PNG 图像，以实现前端数据压缩的方法。该方案适用于旧版浏览器，通过 PNG 格式压缩特性减小体积，支持压缩与解压操作，并提供完整代码示例。
  - Tags: #read #frontend #hack

- (2026-03-28) [我是如何构建一个 AI 原生量化系统的](202603/2026-03-28-%E6%88%91%E6%98%AF%E5%A6%82%E4%BD%95%E6%9E%84%E5%BB%BA%E4%B8%80%E4%B8%AA-ai-%E5%8E%9F%E7%94%9F%E9%87%8F%E5%8C%96%E7%B3%BB%E7%BB%9F%E7%9A%84.md)
  - 策引系统通过DSL将用户意图转化为透明策略，由引擎执行决策，强调可理解性与信任，避免AI直接生成信号带来的不确定性。
  - Tags: #read #agent #deepdive

## Monthly Archive

- [2026-04](202604/monthly-index.md) (3 entries)
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
