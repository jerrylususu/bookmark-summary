# Cross-Site Request Forgery
- URL: https://words.filippo.io/csrf/
- Added At: 2026-05-02 14:42:55
- Tags: #read #security

## TL;DR
本文介绍CSRF攻击原理及防御方法，重点推荐利用现代浏览器的Fetch元数据（如Sec-Fetch-Site头）结合Origin头实现高效防护，替代传统令牌机制，并提供2025年的实践方案与兼容性建议。

## Summary
跨站请求伪造（CSRF）是一种利用用户浏览器凭据或网络位置发起恶意请求的攻击。文章介绍了CSRF的基本概念、浏览器允许此类请求的历史原因，以及如何通过现代技术（如Fetch元数据）简化防御措施。

### CSRF攻击原理
- 攻击者通过恶意网页诱导用户浏览器向目标站点发送请求，利用用户的认证凭据（如Cookie）执行非授权操作。
- 例如，攻击者可构造一个表单，自动提交转账请求，而浏览器会携带用户Cookie发送。

### 防御挑战
- 浏览器因兼容性原因允许跨站请求，但禁用第三方Cookie会影响单点登录（SSO）等流程。
- CSRF防御需平衡安全与功能，避免误拦合法请求。

### 关键概念：同站与同源
- **同站（Same-Site）**：基于域名（如`example.com`），但不同子域（如`app.example.com`和`marketing.example.com`）可能信任级别不同。
- **同源（Same-Origin）**：包括协议、域名和端口。HTTP与HTTPS被视为不同源，存在中间人攻击风险。
- 浏览器对“同站”的定义不一致：Cookie通常采用无方案定义（HTTP=HTTPS），而`Sec-Fetch-Site`头采用有方案定义（HTTP≠HTTPS）。

### 防御措施
1. **CSRF令牌**：
   - 经典方法：在请求中嵌入随机令牌，与服务器会话或Cookie比对。
   - 缺点：需开发者在所有表单中手动实现，且可能被跨站泄漏攻击利用。

2. **Origin头**：
   - 浏览器自动添加`Origin`头，标识请求来源。可拒绝非安全方法（如POST）的跨源请求。
   - 问题：需配置应用自身源，且旧浏览器可能不发送该头。

3. **SameSite Cookie**：
   - 设置Cookie的`SameSite`属性为`Lax`或`Strict`，可阻止跨站请求携带Cookie。
   - 但默认 rollout 失败，因SSO流程常被破坏；部分浏览器采用宽松策略，效果有限。

4. **非简单请求**：
   - CORS对非简单请求（如带自定义头）进行预检，但无法防御简单请求（如表单提交）。

5. **Fetch元数据**：
   - 现代浏览器提供`Sec-Fetch-Site`头，标识请求是否为跨站（`cross-site`）、同站（`same-site`）或同源（`same-origin`）。
   - 自2023年起，主流浏览器均支持，是推荐的高效防御方式。

### 2025年推荐防御方案
文章提出一个结合Fetch元数据和Origin头的算法，优先使用浏览器提供的元数据，避免传统令牌的复杂性：
1. **允许所有安全方法**：GET、HEAD、OPTIONS请求默认放行。
2. **检查Origin头**：若匹配信任源列表，允许请求。
3. **检查Sec-Fetch-Site头**：
   - 若值为`same-origin`或`none`，允许请求。
   - 否则拒绝。
4. **缺失头时的处理**：
   - 若无`Sec-Fetch-Site`或`Origin`头，允许请求（非现代浏览器）。
   - 若`Origin`头的主机与`Host`头匹配，允许请求（HTTP源或旧浏览器）。
5. **边缘情况**：对HTTP源通过反向代理的场景，可添加到信任列表；旧浏览器可能存在HTTP→HTTPS漏洞，建议用HSTS缓解。

### 实践建议
- 应用程序或框架应实现上述算法，Go 1.25已引入`CrossOriginProtection`中间件。
- 为SSO等例外情况提供严格范围的绕过机制。
- 避免使用签名令牌，除非绑定用户身份，否则易被攻击者利用。

### 总结
现代浏览器通过Fetch元数据简化了CSRF防御，无需依赖传统令牌。开发者应优先使用`Sec-Fetch-Site`和`Origin`头，结合算法实现高效保护，同时注意兼容性和例外处理。
