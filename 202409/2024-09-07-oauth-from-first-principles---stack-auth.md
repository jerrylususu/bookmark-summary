# OAuth from First Principles - Stack Auth
- URL: https://stack-auth.com/blog/oauth-from-first-principles
- Added At: 2024-09-07 10:44:45

## TL;DR
文章通过分析一个有缺陷的OAuth实现，详细解释了OAuth的工作原理及其安全改进措施，包括访问令牌、授权码流程、PKCE等，最终建议不要自行实现OAuth客户端，推荐阅读相关RFC文档。

## Summary
1. **学习目的**：作者希望通过逐步分析和攻击一个有缺陷的OAuth实现，来帮助读者理解OAuth的工作原理。

2. **初始实现**：
   - **简单授权**：Big Head使用Pied Piper应用压缩文件，Pied Piper需要访问他的Hooli云驱动器。最简单的方法是Pied Piper要求Big Head提供Hooli的用户名和密码。
   - **问题暴露**：Big Head的凭证完全暴露，Pied Piper可以访问他的整个Hooli账户，包括邮件、聊天等，且如果Pied Piper被黑，密码会以明文形式泄露。

3. **改进方案**：
   - **访问令牌**：引入访问令牌，限制Pied Piper的权限，但这种方法不用户友好，Big Head需要手动生成令牌。
   - **自动化**：Pied Piper可以代表Big Head请求Hooli生成访问令牌，但存在安全问题，任何人都可以冒充任何人。

4. **安全改进**：
   - **确认请求**：Hooli需要Big Head确认请求，通常通过重定向到`hooli.com`域名页面进行验证。
   - **命名流程**：早期OAuth实现称为隐式流（Implicit Flow），通过URL查询参数传递信息。

5. **攻击与防御**：
   - **重定向URI操纵**：恶意竞争者Endframe可以通过操纵重定向URI窃取访问令牌，解决方案是要求Pied Piper预注册所有可能的重定向URI。
   - **跨站请求伪造（CSRF）**：Endframe可以通过生成恶意链接诱导Big Head登录，解决方案是使用随机字符串（state）防止CSRF攻击。
   - **窃听访问令牌**：Endframe可以通过窃听浏览器历史记录获取访问令牌，解决方案是使用授权码流程（Authorization Code Flow），避免在URL中传递访问令牌。
   - **窃听授权码**：Endframe可以实时窃听授权码并快速交换为访问令牌，解决方案是使用代码交换的证明密钥（PKCE），确保只有初始请求者可以交换授权码。
   - **信任URI操纵**：即使保护了重定向URI，Endframe仍可能通过拦截请求修改URI，解决方案是客户端在交换授权码时再次发送当前URI，Hooli验证其与原始请求匹配。

6. **最终流程**：
   - **OAuth 2.0授权码流程与PKCE**：这是当前浏览器中第三方认证的标准方法，包括生成随机字符串、重定向、验证、授权码交换和访问令牌生成等步骤。

7. **总结与建议**：
   - **非正式解释**：本文是对OAuth流程的非正式解释，实际规范更复杂，涉及客户端密钥、刷新令牌、客户端凭证流等。
   - **不建议自行实现**：由于安全细节复杂，建议不要自行实现OAuth客户端，推荐阅读相关RFC文档。
