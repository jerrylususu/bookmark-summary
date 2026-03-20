# AprilNEA - Full Stack Engineer
- URL: https://aprilnea.me/zh/blog/reverse-engineering-claude-code-antspace
- Added At: 2026-03-20 16:10:43
- Tags: #read #agent #deepdive

## TL;DR
本文通过逆向工程分析Claude Code Web，揭示Anthropic未公开的基础设施架构，包括Firecracker微虚拟机运行环境、内部技术栈、Antspace PaaS平台及BYOC支持，展现其构建垂直整合AI应用平台的战略野心。

## Summary
本文通过逆向工程分析了Claude Code Web的运行环境，揭示了Anthropic未公开的基础设施架构。作者在自己的Claude Code Web会话中使用标准Linux工具（如strace、strings、go tool objdump）对未strip的Go二进制文件进行分析，发现了以下关键信息：

1. **运行环境**：Claude Code Web运行在Firecracker微虚拟机中，硬件规格为4核vCPU、16GB内存、252GB磁盘，内核版本为Linux 6.18.5。进程树精简，PID 1为自研的init进程和WebSocket API网关。

2. **二进制分析**：`/usr/local/bin/environment-runner`是一个未strip的Go二进制文件，保留完整调试符号，构建自Anthropic的私有monorepo。提取的内部包结构显示了Anthropic的完整技术栈，包括API客户端、认证、Claude执行、会话管理、MCP服务器等。

3. **Antspace平台**：在部署模块中发现了AntspaceClient，揭示了一个未公开的PaaS平台。Antspace采用完整的部署协议，包括创建部署、上传构建产物和流式状态更新。与Vercel相比，Antspace采用整体tar.gz上传、本地构建和流式NDJSON状态获取。该平台在公开互联网上无任何信息，表明是Anthropic的战略性投资。

4. **Baku环境**：内部代号Baku是Claude.ai上Web应用构建器的环境，使用Vite+React+TypeScript模板，自动配置Supabase数据库，并集成MCP工具。默认部署目标为Antspace，而非Vercel。

5. **BYOC支持**：Anthropic提供“自带云”环境，允许企业在自己的基础设施中运行environment-runner，同时由Anthropic API控制会话编排。支持Kubernetes集成和多种认证方式。

6. **战略全景**：Anthropic正在构建一个垂直整合的AI应用平台，从自然语言需求到应用生成、数据库配置和部署，全程在Anthropic生态内完成。这使其直接竞争Vercel、Netlify、Replit、Supabase等平台，但拥有从大语言模型到运行时再到托管平台的完整技术栈优势。

7. **方法论**：所有发现均通过标准Linux工具在自有会话中获得，未利用漏洞或跨越网络边界。二进制未混淆或strip，使分析过程简单高效。

结论指出，Antspace可能仍处于早期阶段，但部署协议已成熟。Anthropic的野心不止于AI模型和Agent公司，而是构建一个应用可被“说出”来的世界所需的基础设施，并希望掌控技术栈的每一层。
