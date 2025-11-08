# Bookmark Summary 
读取 bookmark-collection 中的书签，使用 jina reader 获取文本内容，然后使用 LLM 总结文本。详细实现请参见 process_changes.py。需要和 bookmark-collection 中的 Github Action 一起使用。

## Latest 10 Summaries

- (2025-11-08) [Claude Pirate: Abusing Anthropic's File API For Data Exfiltration ·  Embrace The Red](202511/2025-11-08-claude-pirate-abusing-anthropic%27s-file-api-for-data-exfiltration-%C2%B7-embrace-the-red.md)
  - Claude代码解释器存在数据泄露漏洞，攻击者可利用网络权限和文件API窃取用户数据至攻击者账户。Anthropic确认漏洞后承诺改进，建议用户禁用网络访问或严格监控代码执行。
  - Tags: #read #llm #security

- (2025-11-07) [How I use AI (Oct 2025)](202511/2025-11-07-how-i-use-ai-%28oct-2025%29.md)
  - 2025年软件工程师总结AI应用：在代码补全、概念解释和文档摘要方面效果显著，但复杂算法、准确搜索和风格化写作表现不足。AI虽有用，仍需人工干预与技术完善。
  - Tags: #read #llm #guide

- (2025-11-07) [You Should Write An Agent](202511/2025-11-07-you-should-write-an-agent.md)
  - 通过构建简易Agent可深入理解其原理：仅需少量代码实现对话和工具调用，上下文管理决定性能上限。无需依赖复杂框架，动手实践能快速验证创新思路。当前技术仍处探索期，个人开发者具备低成本快速迭代的优势。
  - Tags: #read #llm

- (2025-11-06) [我妈妈被电信诈骗95万元的全过程-月光博客](202511/2025-11-06-%E6%88%91%E5%A6%88%E5%A6%88%E8%A2%AB%E7%94%B5%E4%BF%A1%E8%AF%88%E9%AA%9795%E4%B8%87%E5%85%83%E7%9A%84%E5%85%A8%E8%BF%87%E7%A8%8B-%E6%9C%88%E5%85%89%E5%8D%9A%E5%AE%A2.md)
  - 作者母亲遭遇电信诈骗损失95万元，案例揭示了骗子通过恐吓、伪造证件、木马操控等手法针对老年人行骗。反思指出仅靠技术拦截不足，需采取手机号隔离、设备升级及加强家人沟通等综合防范措施。
  - Tags: #read

- (2025-11-06) [Making XML human-readable without XSLT](202511/2025-11-06-making-xml-human-readable-without-xslt.md)
  - 本文指出XSLT在现代浏览器中已趋于淘汰，建议优先使用服务器端将XML转换为HTML。若需客户端处理，可用JavaScript动态生成HTML，或通过CSS简单样式化XML，但功能有限。
  - Tags: #read #frontend

- (2025-11-05) [Immutable by Design: The Deep Tech Behind Tigris Bucket Forking | Tigris Object Storage](202511/2025-11-05-immutable-by-design-the-deep-tech-behind-tigris-bucket-forking-tigris-object-storage.md)
  - Tigris对象存储的核心技术“存储桶分叉”基于数据不可变性设计，利用快照、写入前日志和有序键结构实现高效时间旅行和数据隔离。该技术支持TB级数据瞬间分叉，提供高安全性和性能，适用于AI实验等场景，未来将扩展功能以突破现有限制。
  - Tags: #read #deepdive

- (2025-11-05) [人类在环智能体源码展示：企业报销工作流举例（附源码下载） - 铁蕾的个人博客](202511/2025-11-05-%E4%BA%BA%E7%B1%BB%E5%9C%A8%E7%8E%AF%E6%99%BA%E8%83%BD%E4%BD%93%E6%BA%90%E7%A0%81%E5%B1%95%E7%A4%BA%EF%BC%9A%E4%BC%81%E4%B8%9A%E6%8A%A5%E9%94%80%E5%B7%A5%E4%BD%9C%E6%B5%81%E4%B8%BE%E4%BE%8B%EF%BC%88%E9%99%84%E6%BA%90%E7%A0%81%E4%B8%8B%E8%BD%BD%EF%BC%89---%E9%93%81%E8%95%BE%E7%9A%84%E4%B8%AA%E4%BA%BA%E5%8D%9A%E5%AE%A2.md)
  - 文章介绍如何利用Bridgic开源框架，在企业报销流程中实现“人类在环”机制。通过工作流设计、代码实现和执行恢复机制，展示如何中断工作流等待人工审批后再继续处理，无需长连接会话。
  - Tags: #read #llm #deepdive

- (2025-11-05) [MCP Colors: Systematically deal with prompt injection risk](202511/2025-11-05-mcp-colors-systematically-deal-with-prompt-injection-risk.md)
  - 文章提出MCP Colors方法应对提示注入风险：通过红（不可信内容）蓝（关键操作）颜色标记隔离风险操作，简化安全评估。需人工参与威胁建模，强调安全无法完全自动化，但为通用代理提供可行路径。
  - Tags: #read #llm #security

- (2025-11-05) [Code execution with MCP: building more efficient AI agents](202511/2025-11-05-code-execution-with-mcp-building-more-efficient-ai-agents.md)
  - 通过代码执行优化AI代理效率，将MCP工具转为代码API，使代理按需加载工具、本地处理数据。该方法大幅减少令牌消耗（如从15万降至2千），提升响应速度并增强隐私保护，但需平衡安全沙箱等实施成本。
  - Tags: #read #llm

- (2025-11-05) [A new SQL-powered permissions system in Datasette 1.0a20](202511/2025-11-05-a-new-sql-powered-permissions-system-in-datasette-1.0a20.md)
  - Datasette 1.0a20 重构了权限系统，将权限检查从逐条函数调用改为基于SQLite查询，提升效率。新系统支持层次化权限、插件扩展和资源批量过滤，并增加调试工具。版本变更较大，提供升级指南与AI辅助开发工具，目标在社区升级插件后发布1.0正式版。
  - Tags: #read #llm #tips

## Monthly Archive

- [2025-11](202511/monthly-index.md) (20 entries)
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
