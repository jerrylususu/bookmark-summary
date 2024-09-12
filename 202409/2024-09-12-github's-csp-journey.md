# GitHub's CSP journey
- URL: https://github.blog/engineering/platform-security/githubs-csp-journey/
- Added At: 2024-09-12 14:28:54
- [Link To Text](2024-09-12-github's-csp-journey_raw.md)

## TL;DR
GitHub通过引入子资源完整性和内容安全策略（CSP）来增强安全性，防止内容注入和跨站脚本攻击。CSP策略包括限制JavaScript、对象、图像、连接和表单提交的源，以及防止点击劫持和插件滥用。GitHub计划继续优化CSP策略，并关注浏览器安全特性的发展。

## Summary
1. **背景介绍**：
   - GitHub在几个月前推出了[子资源完整性](http://githubengineering.com/subresource-integrity/)，以减少被攻击的CDN提供恶意JavaScript的风险。
   - 尽管这是一个重大胜利，但这并未解决GitHub.com本身可能存在的相关内容注入问题。
   - GitHub在过去几年中一直在解决这个问题，并认为分享他们的经验可能既有趣又有用。

2. **内容注入的定义**：
   - **跨站脚本（XSS）**：这是过去、现在和可预见的未来中最常见的网络漏洞。许多开发者熟悉XSS及其明显的安全后果。
   - **无脚本攻击**：这是一个更复杂的问题，通常被忽视，因为人们忙于防御XSS。但如Michal Zalewski和Mario Heiderich等人的研究显示，防止XSS并不能解决所有内容注入问题。

3. **GitHub的防御措施**：
   - 使用自动转义模板、代码审查和静态分析来防止这些漏洞的引入。
   - 历史表明，这些漏洞是不可避免的，因此GitHub决定采取预防和检测相结合的策略，并增加额外的防御措施，使内容注入漏洞更难被攻击者利用。

4. **内容安全策略（CSP）**：
   - **CSP简介**：CSP是一个HTTP头，允许站点使用声明性策略来设置对Web资源（如JavaScript、CSS、表单提交等）的限制。
   - **GitHub的CSP历程**：GitHub是CSP的早期采用者，大约三年前推出了初始实现。
   - **初始策略**：
     ```
     CONTENT-SECURITY-POLICY:
       default-src *;
       script-src 'self' assets-cdn.github.com jobs.github.com ssl.google-analytics.com secure.gaug.es;
       style-src 'self' assets-cdn.github.com 'unsafe-inline';
       object-src 'self' assets-cdn.github.com;
     ```
   - **当前策略**：
     ```
     CONTENT-SECURITY-POLICY:
       default-src 'none';
       base-uri 'self';
       block-all-mixed-content;
       child-src render.githubusercontent.com;
       connect-src 'self' uploads.github.com status.github.com api.github.com www.google-analytics.com wss://live.github.com;
       font-src assets-cdn.github.com;
       form-action 'self' github.com gist.github.com;
       frame-ancestors 'none';
       frame-src render.githubusercontent.com;
       img-src 'self' data: assets-cdn.github.com identicons.github.com www.google-analytics.com collector.githubapp.com *.gravatar.com *.wp.com *.githubusercontent.com;
       media-src 'none';
       object-src assets-cdn.github.com;
       plugin-types application/x-shockwave-flash;
       script-src assets-cdn.github.com;
       style-src 'unsafe-inline' assets-cdn.github.com
     ```

5. **重要CSP指令**：
   - **script-src**：仅从CDN获取JavaScript，避免使用`self`作为源，以防止潜在的JSONP端点和内容嗅探问题。
   - **object-src**：限制对象和嵌入标签的源，防止Flash文件的执行。
   - **img-src**：限制图像源，减少敏感数据通过图像标签泄露的风险。
   - **connect-src**：限制JavaScript连接的域，减少攻击面。
   - **form-action**：限制表单提交的域，防止CSRF攻击。
   - **child-src/frame-src**：限制iframe的源，防止嵌套上下文中的安全问题。
   - **frame-ancestors**：防止GitHub.com内容被嵌入到其他站点，缓解点击劫持等攻击。
   - **base-uri**：限制`base`标签的源，防止攻击者修改所有相对URL。
   - **plugin-types**：限制插件类型，减少注入的`object`或`embed`标签的影响。

6. **未来计划**：
   - 继续扩展动态CSP策略的使用，为GitHub.com上的每个端点实现“最小权限”策略。
   - 关注[w3c/webappsec](https://github.com/w3c/webappsec)，以获取更多浏览器特性来进一步加强安全措施。
   - 尽管CSP策略非常严格，但GitHub仍保持谦逊，知道总会有CSP无法阻止的内容注入攻击向量。

7. **作者**：
   - 文章由Patrick Toomey撰写。
