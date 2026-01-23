# SSH has no Host header - exe.dev blog
- URL: https://blog.exe.dev/ssh-host-header
- Added At: 2026-01-23 12:58:22
- Tags: #read #hack

## TL;DR
exe.dev平台SSH协议缺乏Host头，无法区分虚拟机。解决方案是采用共享IPv4地址池，通过DNS CNAME记录和用户公钥与IP组合路由连接。该定制方案确保域名行为一致，适用于其特定需求。

## Summary
该文章讨论了 exe.dev 平台在 SSH 协议中缺乏 Host 头的问题及其解决方案。文章由 David Crawshaw 于 2026 年 1 月 22 日发布。

**问题背景**：  
exe.dev 使用相同域名（如 undefined-behavior.exe.xyz）同时支持 HTTPS 和 SSH 访问虚拟机（VM）。HTTPS 可通过 HTTP 请求中的 Host 头区分不同 VM，但 SSH 协议没有类似机制。由于成本原因，exe.dev 无法为每个 VM 分配唯一 IPv4 地址，也无法仅使用 IPv6（以避免部分互联网无法访问），因此必须共享 IP 地址，但 SSH 无法直接路由到正确 VM。

**解决方案：SSH IP 共享**  
exe.dev 采用共享 IPv4 地址池策略。每个 VM 被分配一个相对于其所有者唯一的地址，通过 DNS CNAME 记录实现（如域名映射到共享 IP s003.exe.xyz）。同一用户的 VM 使用不同 IP，但不同用户的 VM 可共享同一 IP。

**工作原理**：  
当用户通过 SSH 连接时，提供公钥和连接 IP 地址。公钥标识用户，{用户, IP} 元组唯一确定目标 VM。代理根据此信息路由连接。实施需要定制管理软件处理 IP 分配和云环境中的 NAT 问题。

**结论**：  
该方案并非通用，但确保了域名行为的统一性和可预测性，适用于 exe.dev 的特定需求。
