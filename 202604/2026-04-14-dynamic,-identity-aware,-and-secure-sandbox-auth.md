# Dynamic, identity-aware, and secure Sandbox auth
- URL: https://blog.cloudflare.com/sandbox-auth/
- Added At: 2026-04-14 13:32:38
- Tags: #read #agent #security

## TL;DR
Cloudflare为Sandbox和Containers推出“出站Worker”功能，通过代理拦截和零信任凭证注入，提升AI代理认证的安全性与灵活性，支持动态控制和深度集成。

## Summary
本文介绍了Cloudflare为Sandbox和Containers新增的“出站Worker”功能，旨在提升代理工作负载的认证安全性与灵活性。核心内容如下：

1. **背景与需求**  
   随着AI代理在沙箱中运行的场景增多，传统认证方法（如API令牌、OIDC令牌、自定义代理）存在安全风险、灵活性不足或复杂度高等问题。理想认证机制需满足零信任、简单、灵活、身份感知、可观测、高性能、透明和动态等特性。

2. **出站Worker的核心机制**  
   - **代理与拦截**：通过JavaScript代码拦截沙箱的出站HTTP/HTTPS请求，支持按域名、IP等条件动态处理。  
   - **零信任凭证注入**：在代理层安全注入密钥，沙箱本身无法访问凭证，实现零信任环境。  
   - **动态控制**：可实时修改网络策略（如允许特定域名后锁定出站），支持条件化响应。  
   - **TLS解密**：通过临时CA证书实现HTTPS流量透明代理，确保内容可被安全处理。

3. **实践示例**  
   - **基础控制**：限制请求方法（如仅允许GET）并记录日志。  
   - **身份感知认证**：根据沙箱ID动态注入不同凭证。  
   - **集成Cloudflare生态**：直接调用R2、KV等绑定服务，无需手动管理令牌。  
   - **动态策略调整**：例如先允许依赖下载，后锁定网络。

4. **技术实现**  
   - 通过`ctx.container`新增方法（如`interceptOutboundHttp`）设置代理，支持本地开发与生产环境一致。  
   - 代理进程与沙箱同机运行，确保低延迟和安全性。  
   - 支持通配符域名、IP范围等灵活匹配规则。

5. **优势总结**  
   出站Worker提供了零信任、动态、可观测且高性能的认证方案，简化了代理工作负载的安全管理，同时深度集成Cloudflare开发者平台。

用户可通过文档快速上手，当前版本已支持Containers和Sandbox。
