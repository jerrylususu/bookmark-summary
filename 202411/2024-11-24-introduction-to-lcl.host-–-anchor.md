# Introduction to lcl.host – Anchor
- URL: https://anchor.dev/docs/lcl-host/why-lcl
- Added At: 2024-11-24 04:36:17
- [Link To Text](2024-11-24-introduction-to-lcl.host-–-anchor_raw.md)

## TL;DR
lcl.host是Anchor团队开发的本地HTTPS设置工具，通过私有CA技术确保开发与生产环境一致性，解决混合内容、CORS错误等问题。它支持HTTP/2、安全Cookies、OAuth回调等需求，提供自动证书配置和续订，简化开发流程。

## Summary
1. **lcl.host简介**：
   - lcl.host是一个由Anchor团队开发的工具，通过简单的命令即可在本地环境中设置HTTPS。
   - 该工具使用Anchor团队生产级别的私有证书颁发机构（CA）技术，适用于开发环境。

2. **本地HTTPS需求**：
   - **混合内容**：在生产环境中，安全网页可能请求非安全内容，本地环境需模拟这种情况。
   - **CORS错误**：多源内容加载时，浏览器安全上下文变化可能导致CORS错误，本地HTTPS可复现和调试。
   - **HTTP/2**：HTTP/2和HTTP/3需要TLS，本地HTTPS支持这些协议的测试。
   - **安全Cookies**：浏览器在localhost处理安全Cookies的方式与生产环境不同，本地HTTPS保持一致性。
   - **OAuth和第三方安全端点**：许多外部组织要求HTTPS回调，本地开发需切换到HTTPS。
   - **本地应用和市场**：某些本地工具和市场（如Heroku、Slack、AWS）开发应用时需要HTTPS。
   - **工具要求**：某些开发工具需要HTTPS以确保功能正常。

3. **开发场景**：
   - **公共网络**：生产环境使用公共证书，本地环境需模拟。
   - **SaaS**：连接互联网的服务（如Ruby on Rails SaaS项目）需要HTTPS。
   - **微服务**：React应用与独立后端API通信，设置Cookies和API请求需HTTPS。

4. **lcl.host优势**：
   - **开发/生产环境一致性**：保持开发和生产环境尽可能相似，减少环境差异。
   - **安全上下文**：浏览器将lcl.host子域视为普通安全域，无需注册或维护。
   - **WebRTC和Web Workers**：某些功能需要HTTPS，即使是在localhost。
   - **gRPC**：需要HTTP/2建立双向流，需TLS。

5. **anchor lcl功能**：
   - **配置本地证书存储**：信任Anchor提供的证书。
   - **检测应用名称和语言/服务器类型**：通过Anchor API配置应用服务和资源。
   - **颁发证书**：为应用或服务颁发证书，写入应用目录。
   - **添加CA证书**：将WebPKI验证的CA证书添加到文件系统。
   - **ACME自动配置**：自动续订证书，减少手动操作。

6. **lcl.host子域工作原理**：
   - **解析到回环地址**：lcl.host子域始终解析到127.0.0.1，可替代localhost地址。

7. **常见问题**：
   - **TLS和需求**：TLS确保数据和用户安全，加密客户端和服务器之间的流量。
   - **证书共享**：个人项目免费，团队项目可创建组织账户。
   - **生产或暂存环境**：生产环境需使用Anchor.dev设置证书。
   - **ACME自动配置**：自动续订证书，减少手动操作。
   - **新员工设置**：已添加ACME包的项目，新员工需运行`anchor lcl`并配置环境变量。
   - **开发VM或容器**：VM和容器需在主机系统上配置信任存储。
   - **自定义域**：`anchor lcl`不支持自定义域，但可创建开发工作区。
   - **项目名称唯一性**：子域始终路由到本地系统，项目名称无需唯一。
   - **开发环境公开访问**：开发环境仅在本地机器上安全访问。
   - **.pem文件**：PEM文件用于公钥基础设施（PKI），包含证书和密钥。
   - **FQDN vs localhost**：lcl.host保持安全上下文，易于设置。
   - **与自签名证书工具的区别**：`anchor lcl`使用私有CA颁发证书，支持ACME自动续订。
   - **lcl.host不工作**：检查域名有效性或DNS重绑定保护，尝试公共DNS服务器或编辑/etc/hosts文件。
