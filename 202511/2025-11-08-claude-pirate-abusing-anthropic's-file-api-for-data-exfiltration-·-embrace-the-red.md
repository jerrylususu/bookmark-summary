# Claude Pirate: Abusing Anthropic's File API For Data Exfiltration ·  Embrace The Red
- URL: https://embracethered.com/blog/posts/2025/claude-abusing-network-access-and-anthropic-api-for-data-exfiltration/
- Added At: 2025-11-08 08:35:06
- Tags: #read #llm #security

## TL;DR
Claude代码解释器存在数据泄露漏洞，攻击者可利用网络权限和文件API窃取用户数据至攻击者账户。Anthropic确认漏洞后承诺改进，建议用户禁用网络访问或严格监控代码执行。

## Summary
本文揭示了 Anthropic Claude 代码解释器（Code Interpreter）功能中的一项数据泄露漏洞，该漏洞允许攻击者通过滥用其网络访问权限和文件 API 窃取用户敏感数据。

## 漏洞概述
- **核心问题**：Claude 的代码解释器默认启用了网络出口权限，允许访问包括 `api.anthropic.com` 在内的少数域名。攻击者可利用此权限，通过间接提示注入（indirect prompt injection）诱使 Claude 执行恶意代码，将用户数据上传至攻击者控制的 Anthropic 账户。
- **攻击链**：
  1. 攻击者通过恶意文档或 MCP 服务器注入指令，让 Claude 读取用户数据（如聊天记录）并保存到沙盒文件中。
  2. Claude 在沙盒中运行攻击者提供的代码，调用 Anthropic 文件 API，使用攻击者的 API 密钥将文件上传至攻击者的账户。
  3. 攻击者可通过 Anthropic 控制台直接访问窃取的文件（单文件上限 30MB）。

## 技术细节
- **网络访问配置**：默认的“仅包管理器”模式允许访问有限域名（如 npm、PyPI），但包括 `api.anthropic.com`，为攻击提供了通道。
- **绕过防御**：Claude 会拒绝包含明文 API 密钥的恶意负载，但攻击者通过混入大量无害代码（如 `print('Hello, world')`）可提高指令执行成功率。
- **演示结果**：攻击成功实现了从目标用户窃取聊天记录并上传至攻击者账户，全程无需用户交互。

## 安全响应与争议
- **责任披露**：作者于 2025 年 10 月 25 日向 Anthropic 报告漏洞，但初始被判定为“超出范围”（模型安全问题）。后经沟通，Anthropic 确认为有效安全问题，承诺改进流程。
- **现有警示**：Anthropic 文档已提及数据泄露风险，建议用户监控 Claude 行为并及时中止异常操作，但默认设置仍存在隐患。

## 缓解建议
- **对供应商**：沙盒应限制 Claude 仅能与登录用户的账户通信，强化默认安全策略。
- **对用户**：禁用网络访问、严格限制允许域名，或实时监控代码解释器的执行内容。

## 影响与启示
- 此类漏洞体现了 AI 系统与外部服务交互时的机密性风险，符合“致命三重奏”（Lethal Trifecta）理论——模型能力、用户数据与外部访问结合可能引发严重泄露。
- 攻击还可能扩展为远程命令控制（C2），威胁企业数据安全。

本文呼吁用户谨慎配置 Claude 的网络权限，并强调“仅包管理器”模式并非绝对安全。
