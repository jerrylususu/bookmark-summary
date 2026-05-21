# Claw Patrol - The security firewall for agents
- URL: https://clawpatrol.dev/
- Added At: 2026-05-21 14:41:07
- Tags: #tools #agent #security

## TL;DR
Claw Patrol 是一个为 AI 代理设计的安全防火墙，通过凭证管理、流量解析和审批流程，解决代理访问生产环境的安全与审计问题。它支持规则引擎、完整审计日志，并提供开源工具，确保端到端安全。

## Summary
Claw Patrol 是一个为 AI 代理设计的安全防火墙，旨在解决代理访问生产环境时的安全与审计问题。它通过以下核心功能实现安全控制：

1. **问题背景**：
   - 传统访问控制（如 OAuth、IAM、RBAC）仅限制代理能连接哪些服务，但无法控制其连接后的具体操作。
   - 代理持有凭证时，若被提示注入攻击，凭证可能泄露。
   - 代理操作分散在多个服务（如数据库、Kubernetes、GitHub），难以统一审计。

2. **核心功能**：
   - **凭证管理**：代理的凭证由 Claw Patrol 持有，代理本身无法访问，避免泄露风险。
   - **流量解析与规则引擎**：在协议层（HTTP、SQL、Kubernetes API 等）解析代理流量，并根据用户编写的规则（如 HTTP 方法、SQL 语句、Kubernetes 资源）动态允许或拒绝操作。
   - **审批流程**：支持人类（通过 Slack 等）或 LLM 法官对模糊请求进行审批，确保敏感操作经过审核。
   - **完整审计日志**：记录代理的所有操作，便于追溯和分析。

3. **使用方式**：
   - 通过 WireGuard 或 Tailscale 连接网关，无需修改代理代码。
   - 安装命令：`curl -fsSL https://clawpatrol.dev/install.sh | sh`
   - 运行命令：`clawpatrol join <网关URL>` 和 `clawpatrol run <代理名称>`

4. **规则示例**：
   - **HTTP 规则**：检查请求方法、路径、头部等，可集成 LLM 法官扫描内容。
   - **SQL 规则**：解析 Postgres/ClickHouse 语句，禁止危险函数（如文件读取）。
   - **Kubernetes 规则**：控制 pod 执行命令，通过 LLM 法官审核命令内容。

5. **测试与部署**：
   - 支持回归测试：录制真实操作，通过 `clawpatrol test` 在 CI 中验证规则变更，确保策略一致性。
   - 提供管理仪表盘，实时监控设备和请求。

6. **优势对比**：
   - 相比仅监控 LLM 调用或工具调用的工具，Claw Patrol 在协议层全面监控代理操作，并持有凭证，实现端到端安全。
   - 开源（MIT 许可），确保可审计性。

7. **快速开始**：
   - 访问 [demo.clawpatrol.dev](https://demo.clawpatrol.dev/) 体验管理界面。
   - 详细文档和插件扩展见 [Claw Patrol 文档](https://clawpatrol.dev/docs/plugins/)。
