# The AI engineering stack we built internally — on the platform we ship
- URL: https://blog.cloudflare.com/internal-ai-engineering-stack/
- Added At: 2026-04-21 13:51:55
- Tags: #read #agent #engineering

## TL;DR
Cloudflare 内部 AI 工程栈基于自身平台，覆盖平台、知识、执行三层，93% R&D 组织使用 AI 编码工具，提升开发效率并支持未来背景代理等方向。

## Summary
Cloudflare 内部构建的 AI 工程栈基于其自身平台，已实现 93% 的 R&D 组织使用 AI 编码工具。该栈由 iMARS 团队主导开发，涵盖平台层、知识层和执行层，全部使用 Cloudflare 已发布的产品构建。

### 平台层
- **认证与路由**：通过 Cloudflare Access 进行零信任认证，所有 LLM 请求经 AI Gateway 统一路由，实现密钥管理、成本跟踪和数据保留控制。
- **推理服务**：使用 Workers AI 运行开源模型，降低延迟和成本；同时支持 Frontier 模型（如 OpenAI、Anthropic）处理复杂任务。
- **MCP 服务器门户**：聚合 13 个生产 MCP 服务器，提供 182+ 工具，通过单一 OAuth 和 Cloudflare Access 统一管理访问。
- **Code Mode**：在门户层实现工具发现和调用，减少上下文令牌开销，提升效率。

### 知识层
- **Backstage 服务目录**：作为知识图谱，存储 2,055 个服务、依赖关系、团队所有权等结构化数据，供 AI 代理查询上下文。
- **AGENTS.md 文件**：在 3,900+ 仓库中生成，提供代码库结构、约定和边界信息，帮助 AI 代理理解本地上下文。

### 执行层
- **AI 代码审查器**：集成到 GitLab CI，自动审查所有合并请求，分类输出安全、代码质量等发现，并引用工程标准规则。
- **工程标准（Codex）**：将工程规范转化为 AI 可执行的规则，支持本地查询和代码审查合规性检查。

### 成果与数据
- **用户规模**：3,683 名活跃用户（占公司 60%，R&D 93%），295 个团队使用 AI 工具。
- **流量统计**：过去 30 天，AI Gateway 处理 20.18M 请求、241.37B 令牌；Workers AI 处理 51.83B 令牌。
- **开发效率**：合并请求量季度环比增长显著，4 周滚动平均从 ~5,600/周升至 8,700+/周。

### 未来方向
- **背景代理**：基于 Durable Objects 和 Agents SDK，支持云端长运行代理，用于克隆仓库、运行测试等任务。
- **工具与资源**：提供 Agents SDK、Sandbox SDK 等工具，开发者可通过 `npx create-cloudflare@latest --template cloudflare/agents-starter` 快速启动。
