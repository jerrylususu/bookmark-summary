# Bookmark Summary 
读取 bookmark-collection 中的书签，使用 jina reader 获取文本内容，然后使用 LLM 总结文本。详细实现请参见 process_changes.py。需要和 bookmark-collection 中的 Github Action 一起使用。

## Latest 10 Summaries

- (2026-08-20) [Extensible Software in the age of LLMs | Jeremy Morrell](202608/2026-08-20-extensible-software-in-the-age-of-llms-jeremy-morrell.md)
  - LLM 让用户用自然语言生成扩展，Web 软件应从封闭产品转向“可扩展平台”。关键是提供稳定核心与安全隔离，采用对象能力而非暴露凭证，并借助 V8 Isolates、MicroVM、WASM 等原语控制成本与风险。
  - Tags: #read #deepdive #agent #design

- (2026-08-20) [smol machines — the same smol machine on your laptop, in the cloud, or self-hosted](202608/2026-08-20-smol-machines-%E2%80%94-the-same-smol-machine-on-your-laptop%2C-in-the-cloud%2C-or-self-hosted.md)
  - smol machines 是基于 libkrun 的轻量虚拟机项目，提供硬件隔离、快速启动（<200ms）的 Linux 微VM。工件 .smolmachine 可在本地、云和自托管一致运行，支持沙箱不可信代码、打包便携可执行文件、持久化开发机及 GPU 加速。
  - Tags: #tools

- (2026-08-20) [What Is Reasoning](202608/2026-08-20-what-is-reasoning.md)
  - 大模型“推理”并不神秘：推理痕迹只是用特殊标记分隔的普通文本，推理努力仅是系统提示中的一句话，禁用思考靠预填充或阻止采样推理token实现。本质是通过特殊token、系统提示和训练约定来管理文本生成。
  - Tags: #read #llm

- (2026-08-18) [Agent开发手记：agent架构的一个发展趋势 - 铁蕾的个人博客](202608/2026-08-18-agent%E5%BC%80%E5%8F%91%E6%89%8B%E8%AE%B0%EF%BC%9Aagent%E6%9E%B6%E6%9E%84%E7%9A%84%E4%B8%80%E4%B8%AA%E5%8F%91%E5%B1%95%E8%B6%8B%E5%8A%BF---%E9%93%81%E8%95%BE%E7%9A%84%E4%B8%AA%E4%BA%BA%E5%8D%9A%E5%AE%A2.md)
  - 文章认为 agent 架构正从一次性客户端转向可长期存续的云端服务，需前后端分离、可中断持久化恢复，生命周期与内存状态解耦；Bridgic Agent 的“Agent引导人”设计已接近该架构。
  - Tags: #read #agent

- (2026-08-17) [Thinking about tests: assertions and matchers](202608/2026-08-17-thinking-about-tests-assertions-and-matchers.md)
  - 文章探讨测试框架中“断言”与“匹配器”的设计演变，指出将匹配器独立为可组合对象能提升测试代码的可读性、扩展性与维护性。作者认为这种低层次 API 设计在 AI 辅助开发时代反而更关键，因表达性强的测试代码更易审查、节省 token，并强调测试措辞会影响开发者思维与代码质量。
  - Tags: #read

- (2026-08-17) [Book the Meeting Before You Need It](202608/2026-08-17-book-the-meeting-before-you-need-it.md)
  - 文章指出公司变大后跨团队协作瓶颈是约会议时间，提议固定每日预留时段用于按需跨职能对齐，由资深人员主持，避免取消后改异步，必要时果断停掉，也可兼作一对一沟通。
  - Tags: #read #people #tips

- (2026-08-17) [And then the men with guns tell you to do it anyway](202608/2026-08-17-and-then-the-men-with-guns-tell-you-to-do-it-anyway.md)
  - 文章以埃及革命中运营商被迫发送亲政府短信为例，探讨紧急警报系统在及时预警与防止滥用间的根本矛盾。作者认为技术防护无法抵御国家强制（“持枪者”），不存在完美设计，关键在于制度约束与权力制衡，而非仅靠工程安全机制。
  - Tags: #read

- (2026-08-15) [Don’t classify. Hallucinate!](202608/2026-08-15-don%E2%80%99t-classify.-hallucinate%21.md)
  - 文章提出用大模型分类时，不让模型严格输出合法类目，而是放任其自由编造“假分类”，再用向量相似度映射回真实分类。这样省去每次发送巨大合法列表的token开销，突破schema限制，可用更小更便宜的模型，适合类别繁多的分类场景。
  - Tags: #read #tips

- (2026-08-13) [AI is removing the middle class of software engineering](202608/2026-08-13-ai-is-removing-the-middle-class-of-software-engineering.md)
  - 文章指出AI未消除工程判断力，反而放大“写代码”与“做对决策”的差距。实现成本骤降，缺乏判断力的工程师高速制造技术债务，难以雇佣；能控制复杂度、评估AI输出的人更稀缺值钱，薪资两极分化。
  - Tags: #read

- (2026-08-13) [The Same Side of the Table](202608/2026-08-13-the-same-side-of-the-table.md)
  - 管理者在会议中须始终与下属同一立场，不当众指责、撇清或围攻。下属失误时，应接棒引导、暂停或共担责任，会后辅导；提前承诺救场能增强安全感。这是避免恐惧文化，也是管理者荣誉，真正支持是压力下不背弃。
  - Tags: #read #people

## Monthly Archive

- [2026-08](202608/monthly-index.md) (21 entries)
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
