# Bookmark Summary 
读取 bookmark-collection 中的书签，使用 jina reader 获取文本内容，然后使用 LLM 总结文本。详细实现请参见 process_changes.py。需要和 bookmark-collection 中的 Github Action 一起使用。

## Latest 10 Summaries

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

- (2026-03-28) [SD存储卡越用越慢？教你一招免费修复，瞬间省下上千元 - 少数派](202603/2026-03-28-sd%E5%AD%98%E5%82%A8%E5%8D%A1%E8%B6%8A%E7%94%A8%E8%B6%8A%E6%85%A2%EF%BC%9F%E6%95%99%E4%BD%A0%E4%B8%80%E6%8B%9B%E5%85%8D%E8%B4%B9%E4%BF%AE%E5%A4%8D%EF%BC%8C%E7%9E%AC%E9%97%B4%E7%9C%81%E4%B8%8B%E4%B8%8A%E5%8D%83%E5%85%83---%E5%B0%91%E6%95%B0%E6%B4%BE.md)
  - 本文介绍使用SD Card Formatter免费修复SD卡变慢问题的方法，通过覆盖格式化恢复性能，适用于非物理损坏的卡，能节省更换成本。
  - Tags: #read #tips

- (2026-03-28) [将 VS Code 打造成跨平台 Markdown「草稿本」](202603/2026-03-28-%E5%B0%86-vs-code-%E6%89%93%E9%80%A0%E6%88%90%E8%B7%A8%E5%B9%B3%E5%8F%B0-markdown%E3%80%8C%E8%8D%89%E7%A8%BF%E6%9C%AC%E3%80%8D.md)
  - 本文介绍如何利用 VS Code 的配置文件、代码片段和任务功能，将其打造成跨平台 Markdown 草稿本，实现快速记录、自动保存及多端同步。
  - Tags: #read #tips

- (2026-03-26) [OpenClaw：技术解读和给 AI 应用开发的启示（2026）](202603/2026-03-26-openclaw%EF%BC%9A%E6%8A%80%E6%9C%AF%E8%A7%A3%E8%AF%BB%E5%92%8C%E7%BB%99-ai-%E5%BA%94%E7%94%A8%E5%BC%80%E5%8F%91%E7%9A%84%E5%90%AF%E7%A4%BA%EF%BC%882026%EF%BC%89.md)
  - OpenClaw是一个面向真实工作流的AI助手基础设施层，整合LLM、Agent、工具与记忆机制，通过架构设计与实践案例，为AI应用开发提供可扩展、安全的个人助手框架参考。
  - Tags: #read #agent #deepdive

## Monthly Archive

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
