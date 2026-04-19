# How I run multiple $10K MRR companies on a $20/month tech stack
- URL: https://stevehanov.ca/blog/how-i-run-multiple-10k-mrr-companies-on-a-20month-tech-stack
- Added At: 2026-04-19 13:16:05
- Tags: #read #arch

## TL;DR
作者以每月20美元成本运营多家月入超万美元公司，核心是坚持“精益”原则：使用廉价VPS、Go语言、本地AI处理、OpenRouter接入模型、GitHub Copilot编程及SQLite数据库，避免昂贵云服务，专注业务增长。

## Summary
这篇文章分享了作者如何以每月20美元的极低成本运营多家月收入超1万美元的公司，核心在于坚持“精益”原则，避免过度依赖昂贵的云服务和复杂架构。

**核心策略总结：**

1.  **使用廉价VPS服务器**：放弃AWS等复杂云服务，选择Linode或DigitalOcean等提供商的单台VPS（每月5-10美元），专注于服务而非基础设施维护。
2.  **采用Go语言开发后端**：Go编译为单一静态二进制文件，部署简单，性能高，内存占用低，适合在资源受限的服务器上运行。
3.  **利用本地AI处理批量任务**：使用家中闲置的GPU（如RTX 3090）运行VLLM等本地AI模型，避免云API费用，通过Ollama起步，VLLM提升生产环境性能。
4.  **使用OpenRouter接入前沿模型**：通过OpenRouter统一调用Claude、ChatGPT等模型，实现自动故障转移，无需管理多个API密钥。
5.  **善用GitHub Copilot编程**：利用Copilot的按请求计费模式（而非按令牌），通过详细提示让AI代理长时间工作，大幅降低开发成本。
6.  **以SQLite作为主数据库**：启用WAL模式后，SQLite可高效处理高并发，性能远超远程数据库，配合作者开源的认证库简化用户管理。

**结论**：通过上述技术栈，创业者可以极低成本启动并扩展业务，获得更长的跑道和更少的压力，专注于解决用户问题而非烧钱。
