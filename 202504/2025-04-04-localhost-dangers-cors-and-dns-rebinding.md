# Localhost dangers: CORS and DNS rebinding
- URL: https://github.blog/security/application-security/localhost-dangers-cors-and-dns-rebinding/
- Added At: 2025-04-04 07:31:01
- [Link To Text](2025-04-04-localhost-dangers-cors-and-dns-rebinding_raw.md)

## TL;DR


本文探讨了CORS配置错误与DNS重绑定攻击的风险及防御策略。CORS若错误设置通配符、宽松域名匹配或允许`null`来源，可能导致凭证泄露或权限提升；DNS重绑定攻击则通过动态DNS切换绕过浏览器限制，访问内网服务。防御需严格精确配置CORS参数，强制关键接口身份验证，验证`Host`头，并禁止本地服务暴露敏感功能。近年案例如Cognita与Tamagui漏洞均因配置疏漏引发严重安全后果。（99字）

## Summary


本文讨论了CORS配置错误和DNS重绑定攻击的安全风险，并提供了防范策略。关键内容如下：

**CORS机制与常见错误**
- CORS通过响应头`Access-Control-Allow-Origin`和`Access-Control-Allow-Credentials`放宽同源策略，允许跨域访问。错误配置会导致权限提升或数据泄露。
- **常见错误**：
  1. 配置`Access-Control-Allow-Origin: *`与`Access-Control-Allow-Credentials: true`组合，使浏览器误传凭证。
  2. 使用`endsWith`（如允许`stripe.com`时，可能接受`attackerstripe.com`）或`startsWith`（如`https://stripe.com.attacker.com`）导致域名匹配漏洞。
  3. 允许`null`来源，可能被恶意沙箱iframe利用。
- **正确做法**：精确匹配域名，子域名需以`.`开头（如`.stripe.com`），禁用`null`来源，优先使用安全库并严格阅读文档。

**攻击利用与影响**
- 攻击者可利用CORS配置错误冒充用户或管理员，执行敏感操作（如修改配置、RCE）。
- 浏览器防护差异：Chrome默认`SameSite=Lax`缓解部分漏洞，但Firefox/Safari仍可被绕过（如PTSecurity研究的跟踪保护规避技术）。
- 漏洞可与任意文件写入等缺陷结合，进一步扩大影响。例如：
  - **Cognita案例**：FastAPI中`allow_origins`设为通配符且开启凭证，结合上传接口的路径遍历漏洞，引发RCE。
  - **Tamagui案例**：使用`endsWith`匹配域名，攻击者可伪造来源发起恶意请求，可能窃取支付信息或创建后门。

**DNS重绑定攻击**
- 攻击原理：通过快速切换DNS记录IP地址，使浏览器误认为合法来源，访问本地或内网服务（如`localhost`）。
- 工具示例：NCCGroup的Singularity可自动化构造攻击请求。
- **防御关键**：
  - 身份验证：攻击无法传递目标网站的Cookie，因此核心接口需强制认证。
  - 主机验证：检查`Host`头是否匹配预期域名或本地地址（如验证代码示例），拒绝非授权主机。

**最佳实践建议**
1. 严格配置CORS，禁用通配符或宽泛域名匹配。
2. 确保关键接口添加身份验证，并验证`Host`头。
3. 使用工具（如GitHub Code Security）检测CORS漏洞及DNS重绑定防御缺失。
4. 避免在缺乏防护的本地服务（如`localhost`）运行敏感应用，防止跨域访问滥用。
