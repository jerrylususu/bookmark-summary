# Using GitHub Spark to reverse engineer GitHub Spark
- URL: https://simonwillison.net/2025/Jul/24/github-spark/
- Added At: 2025-07-25 13:42:16

## TL;DR


GitHub Spark是GitHub推出的支持自然语言生成全栈应用的工具，需GitHub账户认证，提供数据存储API和LLM调用（用户付费）。作者通过反向工程揭示其系统提示文本、Linux运行环境及美学设计规范。建议改进包括用户级存储隔离、集成GitHub API及开源核心库。作者认为其成功依赖详尽的提示工程与工程化技术整合。

## Summary


GitHub Spark是GitHub推出的基于自然语言构建全栈智能应用的工具，支持用户通过提示词生成完整工作Web应用。其核心功能包括：**认证访问**（需GitHub账户）、**数据存储**（提供持久化键值存储API）、**LLM调用**（可直接调用语言模型，费用由用户承担）。用户可迭代优化应用，通过Codespaces编辑代码，或部署至GitHub托管平台。

作者通过反向工程深入分析了Spark内部机制：
1. **系统提示分析**：利用Spark自身生成文档，提取隐藏的系统提示文本。该提示包含详细API说明，包括**持久化存储、用户身份、LLM调用**接口，以及开发规范（如使用shadcn组件库、Tailwind CSS等）。
2. **工具能力探究**：通过`bash`和`npm`工具发现 Spark运行环境为Debian Linux，提供780+系统工具（如`rg`、`jq`）。平台支持自动生成开发建议（如“添加搜索功能”）。
3. **设计哲学**：系统提示强调美学与功能性结合，包含排版规范（字体、间距、层次）、颜色理论应用、组件设计原则（如优先使用shadcn v4组件库）。

**改进建议**：
- **用户隔离存储**：当前键值存储为全局共享，需增加用户级存储（如`userkv`命名空间）以提升安全性。
- **GitHub API集成**：允许应用调用认证后的GitHub API，例如通过`spark.user.githubToken()`获取访问凭证。
- **开放开发模式**：提供开源版本的`@github/spark`库，便于独立构建与部署。

作者认为Spark工程设计优异，系统的5,000字提示文本是其高质量输出的关键。其工程化实现（如编辑器、部署、API支持）展现了构建此类工具所需的复杂技术整合。
