# Living dangerously with Claude
- URL: https://simonwillison.net/2025/Oct/22/living-dangerously-with-claude/
- Added At: 2025-10-23 05:19:03
- [Link To Text](2025-10-23-living-dangerously-with-claude_raw.md)

## TL;DR
YOLO模式让AI编码代理在无人监督下高效完成复杂任务，但存在数据泄露风险。关键在于使用沙盒环境隔离运行，严格管控文件与网络访问，在保障安全前提下充分发挥其效率优势。

## Summary
这篇文章基于作者Simon Willison在2025年10月22日于旧金山“Claude Code Anonymous”活动上的演讲，探讨了使用Claude Code等编码代理时的“危险模式”（即YOLO模式，原名`--dangerously-skip-permissions`）的双重性。

**YOLO模式的优势：**
- **高效性与便利性**：YOLO模式允许编码代理在无人监督下自主完成任务，用户可并行处理其他事务。作者举例说明，在48小时内完成了三个项目，包括在NVIDIA Spark上部署DeepSeek-OCR模型、使用Pyodide在Node.js中运行Python代码，以及将25年前的Perl工具SLOCCount移植到WebAssembly。这些项目均作为“支线任务”，展示了YOLO模式处理复杂问题的能力。
- **产品体验差异**：对比默认模式（需逐步审批操作），YOLO模式更像一个独立产品，能大幅提升开发效率。

**YOLO模式的风险：**
- **提示注入攻击**：作者强调，放任代理访问未经验证的内容可能导致安全漏洞。攻击者可通过恶意提示（如伪造的HTML文件）诱骗代理泄露敏感数据（如环境变量中的API密钥）。
- **致命三重威胁**：当系统同时具备**访问私有数据**、**暴露于不可信内容**和**外部通信能力**时，极易发生数据泄露。作者指出，这类攻击在现实中非常普遍。

**安全解决方案：**
- **沙盒环境是关键**：作者认为，依赖AI检测攻击不可靠，唯一有效的方法是使用沙盒隔离运行环境。推荐利用第三方沙盒服务（如OpenAI Codex Cloud、Claude Code网页版等），以限制潜在损害。
- **网络与文件系统控制**：沙盒需严格管控文件读写和网络连接，尤其要阻断数据外泄通道。作者提到Claude Code新引入的沙盒功能（基于macOS的`sandbox-exec`命令），但指出该工具已过时，呼吁苹果更新支持。

**结论：**
作者鼓励在确保安全的前提下（即使用沙盒）积极尝试YOLO模式，以发挥编码代理的最大价值，同时规避风险。全文强调平衡效率与安全的重要性，为AI辅助开发提供了实践指导。
