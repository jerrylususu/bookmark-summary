# Learn OAuth 2.0 by Building Your Own OAuth Client
- URL: https://annotate.dev/p/hello-world/learn-oauth-2-0-by-building-your-own-oauth-client-U2HaZNtvQojn4F
- Added At: 2024-08-12 07:55:44
- [Link To Text](2024-08-12-learn-oauth-2.0-by-building-your-own-oauth-client_raw.md)

## TL;DR
本文介绍了如何通过构建OAuth 2.0客户端实现“使用Google登录”功能，详细讲解了OAuth的工作流程、设置OAuth凭证、重定向到Google征求用户同意、与Google交换代码以及获取用户信息的具体步骤，并解释了相关术语。最后，讨论了自行开发OAuth客户端的必要性和学习意义，并建议下一步探索OpenID Connect。

## Summary
1. **OAuth 2.0简介**：OAuth是一种标准协议，允许用户安全地与网站服务器共享其信息（如Google账户中的电子邮件地址），而无需暴露其Google登录凭证。

2. **学习目标**：通过构建自己的OAuth客户端来学习OAuth 2.0，具体实现“使用Google登录”功能，使用TypeScript和Express技术。

3. **OAuth工作流程**：
   - **用户选择使用Google登录**：用户访问网站并点击“使用Google登录”按钮。
   - **网站请求Google许可**：网站将用户重定向到Google，并附带一个客户端ID以识别网站。
   - **Google征求用户同意**：Google显示同意屏幕，询问用户是否同意与网站共享其Google信息。
   - **用户同意并获得授权码**：用户同意后，Google将用户重定向回网站，并在URL的查询参数中附带授权码。
   - **网站与Google交换代码**：网站服务器将授权码和客户端密钥发送给Google，以验证身份，Google返回访问令牌。
   - **网站服务器获取用户信息**：使用访问令牌，网站服务器可以向Google请求用户信息，如电子邮件和姓名，用于认证用户。

4. **设置OAuth凭证**：
   - **获取CLIENT_ID和CLIENT_SECRET**：访问Google的身份验证设置指南，获取这些令牌。
   - **安全管理凭证**：使用环境变量管理凭证，避免硬编码。

5. **用户选择使用Google登录**：通过简单的HTML锚元素实现“使用Google登录”选项，将用户浏览器重定向到`/oauth/google`。

6. **重定向到Google征求用户同意**：
   - **构建重定向URL**：在`/oauth/google`端点响应中，将用户重定向到Google，并附带特定查询参数。
   - **参数解释**：包括`response_type=code`、`client_id`、`redirect_uri`、`scope`和`state`等参数。

7. **Google征求用户同意**：用户在Google的同意屏幕上选择其Google账户并同意共享指定数据。

8. **与Google交换代码**：
   - **浏览器重定向到回调URL**：用户同意后，Google将用户重定向到指定的`redirect_uri`，并附带`code`和`state`。
   - **验证和交换代码**：服务器提取代码和状态，验证状态匹配后，使用`exchangeCodeForToken`函数交换代码为访问令牌。

9. **网站服务器获取用户信息**：使用`getUserInfo`辅助函数，传递新获取的`accessToken`，向Google的用户信息端点发送请求，获取用户电子邮件。

10. **术语解释**：
    - **资源所有者**：数据所有者，即用户。
    - **用户代理**：浏览器或其他交互接口。
    - **OAuth提供者**：如Google，管理OAuth流程和凭证。
    - **客户端**：请求访问用户数据的网站服务器。
    - **授权服务器**：Google的一部分，发放授权码和访问令牌。
    - **资源服务器**：Google的一部分，返回用户信息。

11. **结论和下一步**：
    - **是否应自行开发OAuth客户端**：通常不建议，应使用经过测试的开源OAuth客户端。
    - **学习意义**：理解OAuth客户端内部工作原理有助于配置选项、故障排除和学习其他OAuth流程。
    - **下一步**：探索OpenID Connect（OIDC），了解其解决的问题和所需的最小代码调整。
