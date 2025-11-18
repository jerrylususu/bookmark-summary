# Bookmark Summary 
读取 bookmark-collection 中的书签，使用 jina reader 获取文本内容，然后使用 LLM 总结文本。详细实现请参见 process_changes.py。需要和 bookmark-collection 中的 Github Action 一起使用。

## Latest 10 Summaries

- (2025-11-18) [Memory leaks: the forgotten side of web performance](202511/2025-11-18-memory-leaks-the-forgotten-side-of-web-performance.md)
  - 本文强调Web开发中常被忽视的内存泄漏问题，指出其不易察觉但可能积累导致崩溃，修复性价比高。现有诊断工具尚不完善，作者开发的工具`fuite`提供改进，建议行业关注预防性修复以提升应用质量。
  - Tags: #read #perf

- (2025-11-18) [The fate of “small” open source](202511/2025-11-18-the-fate-of-%E2%80%9Csmall%E2%80%9D-open-source.md)
  - 文章讨论了AI代码生成工具对小而精的开源库的冲击。作者认为，虽然AI提高了效率，却削弱了代码的教育意义，并可能带来依赖转移问题。未来开源应聚焦于AI难以替代的复杂创新领域，以此保持人类创造力的独特价值。
  - Tags: #read #llm

- (2025-11-17) [Only three kinds of AI products actually work](202511/2025-11-17-only-three-kinds-of-ai-products-actually-work.md)
  - 当前有效的AI产品主要分为聊天机器人、自动补全和智能体三类，其中通用模型（如ChatGPT）占主导，而智能体在编程等领域展现出自主任务执行的潜力。其他方向如AI内容流和游戏仍处探索期，未来发展需突破对聊天界面的依赖，打造更贴合需求的产品形态。
  - Tags: #read #llm

- (2025-11-17) [超越DRY：AI原生软件工程的思考](202511/2025-11-17-%E8%B6%85%E8%B6%8Adry%EF%BC%9Aai%E5%8E%9F%E7%94%9F%E8%BD%AF%E4%BB%B6%E5%B7%A5%E7%A8%8B%E7%9A%84%E6%80%9D%E8%80%83.md)
  - AI时代软件工程从交付成品变为提供“生成内核”，强调设计支持AI生成代码的基础套件。新原则注重透明性、细粒度控制和知识引导，鼓励个性化需求的“有意义重复”，开发者角色转向为AI创造力搭建舞台。
  - Tags: #read #llm #deepdive

- (2025-11-17) [基于动态拓扑的Agent编排，原理解析+源码下载 - 铁蕾的个人博客](202511/2025-11-17-%E5%9F%BA%E4%BA%8E%E5%8A%A8%E6%80%81%E6%8B%93%E6%89%91%E7%9A%84agent%E7%BC%96%E6%8E%92%EF%BC%8C%E5%8E%9F%E7%90%86%E8%A7%A3%E6%9E%90%2B%E6%BA%90%E7%A0%81%E4%B8%8B%E8%BD%BD---%E9%93%81%E8%95%BE%E7%9A%84%E4%B8%AA%E4%BA%BA%E5%8D%9A%E5%AE%A2.md)
  - Bridgic框架通过静态、动态和自主编排三级动态性，支持从固定工作流到LLM驱动的动态拓扑调整。核心基于动态有向图机制实现执行调度，并通过声明式和Core API提供编排能力。当前在组件化表达上存在局限，作者未来将优化该特性。
  - Tags: #read #llm #deepdive

- (2025-11-15) [Using the Web Monetization API for fun and profit](202511/2025-11-15-using-the-web-monetization-api-for-fun-and-profit.md)
  - Web Monetization API 允许用户按浏览时长或一次性支付来资助内容创作者。用户需安装扩展并配置钱包，发布者通过在网页中添加标签接收款项。该功能支持动态内容调整，有潜力推动网络小额支付发展。
  - Tags: #read #money

- (2025-11-15) [Digital hygiene](202511/2025-11-15-digital-hygiene.md)
  - 《数字卫生》文章从密码管理、身份验证、设备安全到通信隐私等多方面，提供实用建议以提升网络安全性。强调使用密码管理器、硬件密钥、加密工具和隐私优先服务，倡导自律防护以减少数据泄露和欺诈风险。
  - Tags: #read #security

- (2025-11-15) [Can you save on LLM tokens using images instead of text?](202511/2025-11-15-can-you-save-on-llm-tokens-using-images-instead-of-text.md)
  - 研究探索了将文本转为图像以减少大语言模型提示令牌消耗的方法。实验发现，图像输入虽能节省部分提示令牌，但多数模型会生成更多高成本的完成令牌，且处理时间翻倍，综合性价比低，实际价值有限。
  - Tags: #read #llm

- (2025-11-15) [Welcome, the entire land](202511/2025-11-15-welcome%2C-the-entire-land.md)
  - 作者在布莱顿参会后受启发，将编程传统“Hello World”译为古埃及象形文字，最终设计成T恤图案并免费分享，以趣味方式连接古老文化与现代技术。
  - Tags: #read

- (2025-11-15) [Language Agnostic Programming: Why you may still need code](202511/2025-11-15-language-agnostic-programming-why-you-may-still-need-code.md)
  - 文章探讨了AI在代码生成中的作用与局限，提出语言无关编程的设想：AI可能生成一种精确代码（如Rust），但开发者可通过语言模型实时转换为熟悉语言进行调试。该模式有望降低编程门槛，但仍面临技术挑战，未来关系尚不确定。
  - Tags: #read #llm

## Monthly Archive

- [2025-11](202511/monthly-index.md) (55 entries)
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
