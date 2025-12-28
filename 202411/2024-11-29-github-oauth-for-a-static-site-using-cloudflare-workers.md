# GitHub OAuth for a static site using Cloudflare Workers
- URL: https://til.simonwillison.net/cloudflare/workers-github-oauth
- Added At: 2024-11-29 13:28:45

## TL;DR
作者通过Cloudflare Workers实现GitHub OAuth，解决了静态站点无法完全在客户端实现OAuth的问题，展示了如何利用Cloudflare Workers和Claude生成代码快速实现复杂的OAuth流程。

## Summary
1. **项目背景**：
   - 作者的[tools.simonwillison.net](https://tools.simonwillison.net/)站点是一个静态HTML和JavaScript应用的集合，托管在GitHub Pages上。
   - 许多工具利用外部API（如OpenAI、Anthropic和Google Gemini），得益于`access-control-allow-origin: *` CORS头。
   - 作者希望构建与GitHub API交互的工具，例如将数据保存到Gist。

2. **OAuth需求**：
   - 为了与GitHub API交互，需要实现OAuth，重定向用户到GitHub请求权限，并在浏览器`localStorage`中存储访问令牌。
   - 由于GitHub OAuth依赖于服务器端持有的密钥，无法完全在客户端实现。

3. **解决方案**：
   - 作者的站点通过Cloudflare账户服务于`simonwillison.net`域名，因此考虑使用Cloudflare Workers实现GitHub OAuth。
   - 通过Cloudflare Workers创建一个服务器端脚本，处理OAuth流程。

4. **实现过程**：
   - **Claude生成代码**：
     - 作者使用Claude生成一个简单的OAuth流程代码，重定向用户到GitHub，然后交换`?code=`获取访问令牌并写入`localStorage`。
     - Claude生成的代码几乎完美，只需微调`redirectUri`。
   - **最终代码**：
     - 代码包括检查`code`参数、交换代码获取令牌、返回HTML存储令牌并关闭窗口。
     - 如果没有`code`，则重定向到GitHub OAuth。

5. **部署步骤**：
   - **配置GitHub OAuth应用**：获取客户端ID和密钥。
   - **创建Cloudflare Worker**：在Cloudflare仪表板中创建并部署Worker。
   - **设置环境变量**：配置`GITHUB_CLIENT_ID`、`GITHUB_CLIENT_SECRET`和`GITHUB_REDIRECT_URI`。
   - **配置URL**：在Cloudflare中设置路由，将`tools.simonwillison.net/github-auth*`映射到Worker。

6. **应用集成**：
   - OAuth流程在`localStorage`中设置`github_token`，JavaScript代码检查该令牌并进行API调用。
   - 示例代码展示了如何通过点击“Authenticate with GitHub”链接启动OAuth流程，并轮询`localStorage`以检查令牌是否已设置。

7. **错误处理**：
   - 初始代码缺少错误处理，Claude生成的代码包含详细的错误处理，但稍显冗长。
   - 作者进一步简化代码，添加了更简洁的HTML生成和错误处理逻辑，并部署了更新。

8. **总结**：
   - 通过Cloudflare Workers实现GitHub OAuth，解决了静态站点无法完全在客户端实现OAuth的问题。
   - 整个项目展示了如何利用Cloudflare Workers和Claude生成代码，快速实现复杂的OAuth流程。
