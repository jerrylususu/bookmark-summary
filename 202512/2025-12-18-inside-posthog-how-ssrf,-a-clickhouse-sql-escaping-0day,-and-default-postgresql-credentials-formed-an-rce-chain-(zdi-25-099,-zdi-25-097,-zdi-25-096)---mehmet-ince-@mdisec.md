# Inside PostHog: How SSRF, a ClickHouse SQL Escaping 0day, and Default PostgreSQL Credentials Formed an RCE Chain (ZDI-25-099, ZDI-25-097, ZDI-25-096) - Mehmet Ince @mdisec
- URL: https://mdisec.com/inside-posthog-how-ssrf-a-clickhouse-sql-escaping-0day-and-default-postgresql-credentials-formed-an-rce-chain-zdi-25-099-zdi-25-097-zdi-25-096/
- Added At: 2025-12-18 15:38:50
- Tags: #read #deepdive #security
- [Link To Text](2025-12-18-inside-posthog-how-ssrf,-a-clickhouse-sql-escaping-0day,-and-default-postgresql-credentials-formed-an-rce-chain-(zdi-25-099,-zdi-25-097,-zdi-25-096)---mehmet-ince-@mdisec_raw.md)

## TL;DR
本文披露PostHog平台中存在一条组合漏殻链，利用SSRF、ClickHouse SQL注入0day与PostgreSQL默认凭证，实现远程代码执行。攻击可绕过前端验证，将Webhook重定向至内部服务并执行任意命令。漏洞已通过ZDI协调披露，凸显了系统纵深防御的多重失效。

## Summary
本文详细分析了PostHog平台中一个由多个安全漏洞构成的远程代码执行（RCE）攻击链。攻击链始于服务器端请求伪造（SSRF）漏洞，结合了ClickHouse SQL注入0day和默认PostgreSQL凭据，最终实现RCE。以下是关键点总结：

1. **背景与架构**：  
   - PostHog是一个开源自托管产品分析平台，使用ClickHouse作为主要分析后端，并支持大量外部集成。  
   - 作者在评估PostHog时，通过源码审计发现漏洞。

2. **SSRF漏洞（CVE-2024-9710、CVE-2025-1522、CVE-2025-1521）**：  
   - Webhook功能在测试端点（如`test_slack_webhook`）进行了SSRF验证，但保存配置的端点未重复验证。  
   - 通过直接发送PATCH请求绕过前端，可存储指向内部地址（如localhost）的Webhook URL，形成持久SSRF。  
   - Rust实现的Webhook工作器在处理请求时信任已保存的URL，且支持HTTP重定向（POST转GET），为后续攻击提供条件。

3. **ClickHouse SQL注入0day**：  
   - ClickHouse的PostgreSQL表函数（如`postgresql()`）允许查询远程PostgreSQL数据库，但存在转义错误：使用反斜杠而非单引号转义单引号，导致SQL注入。  
   - 通过注入恶意负载，可突破ClickHouse的HTTP GET只读限制，在PostgreSQL上执行任意SQL。

4. **RCE链组合**：  
   - 利用SSRF将请求重定向至ClickHouse的HTTP API（端口8123）。  
   - 通过SQL注入在PostgreSQL中执行`COPY FROM PROGRAM`命令，实现操作系统命令执行（如反弹shell）。  
   - 攻击链依赖默认配置：ClickHouse容器名（`db`）和PostgreSQL默认凭据（`posthog/posthog`）在自托管环境中常见。

5. **漏洞影响与修复**：  
   - 单个漏洞危害较低，但组合后可导致全面RCE。  
   - 作者通过Zero Day Initiative（ZDI）协调披露，漏洞于2025年2月公开。

整个过程展示了深度防御失效：前端验证遗漏、内部服务信任边界模糊、数据库转义机制缺陷，最终形成高危攻击链。
