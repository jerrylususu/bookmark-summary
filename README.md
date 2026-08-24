# Bookmark Summary 
读取 bookmark-collection 中的书签，使用 jina reader 获取文本内容，然后使用 LLM 总结文本。详细实现请参见 process_changes.py。需要和 bookmark-collection 中的 Github Action 一起使用。

## Latest 10 Summaries

- (2026-08-24) [Anger, Anxiety and Agency](202608/2026-08-24-anger%2C-anxiety-and-agency.md)
  - 文章讨论面对AI不确定性时应持的态度：区分焦虑与愤怒，指出愤怒易错误归因，因为行业领导者同样迷茫。作者主张以好奇和实验替代愤怒，通过实践获得判断力与真实选择能力，而非虚假行动感，最终赢得能动性。
  - Tags: #read

- (2026-08-23) [Fast and Hard Code](202608/2026-08-23-fast-and-hard-code.md)
  - LLM降低了编程语言转换成本，使更多开发者敢于选择Rust、Zig等性能更好但更难的语言及DWARF、eBPF等底层技术。这可能带来两极分化：既产生更多低质量代码，也催生更多追求极致性能和小体积的开发者与项目。
  - Tags: #read #llm

- (2026-08-22) [Stop Making TUIs — Quarrelsome](202608/2026-08-22-stop-making-tuis-%E2%80%94-quarrelsome.md)
  - 文章认为，AI编程助手已让原生GUI开发变得容易，不应再继续构建终端用户界面（TUI）。作者逐一反驳TUI的密度、SSH、可访问性等优势，并展示用AI生成的macOS应用，呼吁开发者更新默认选择，转向原生GUI。
  - Tags: #read #ui

- (2026-08-21) [Introducing Dashboard Touch, a build-your-own version of Touch ID - Anil Dash](202608/2026-08-21-introducing-dashboard-touch%2C-a-build-your-own-version-of-touch-id---anil-dash.md)
  - Anil Dash 因不想受苹果键盘束缚，基于 tinyTouch 开发开源项目 Dashboard Touch，用低成本指纹传感器和微控制器自制 USB 指纹认证装置，模拟键盘自动输入密码。密码与指纹均存本地，仅适合安全环境个人使用。他也分享了动手制作的乐趣，希望社区改进。
  - Tags: #read

- (2026-08-20) [OpenTelemetry Tracing in 200 lines of code | Jeremy Morrell](202608/2026-08-20-opentelemetry-tracing-in-200-lines-of-code-jeremy-morrell.md)
  - 本文用约200行极简实现揭示分布式追踪本质：Span是带ID的日志，Trace靠ID关联，上下文传播用traceparent头，仪器化即包装代码。OpenTelemetry虽庞大但只是在此核心上增加工程化健壮性。
  - Tags: #read #deepdive #observability

- (2026-08-20) [Working with Dynamic Workers | Jeremy Morrell](202608/2026-08-20-working-with-dynamic-workers-jeremy-morrell.md)
  - Cloudflare推出Dynamic Workers，可在隔离沙箱中安全运行用户代码，避免eval的线程、内存和网络风险。它支持CPU限制、禁用网络、自定义绑定及对象能力控制，并提供日志捕获，让普通Web应用低成本实现用户可编程扩展。
  - Tags: #read #guide #deepdive

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

## Monthly Archive

- [2026-08](202608/monthly-index.md) (27 entries)
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
