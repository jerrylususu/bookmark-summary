# Previewing Claude Code for web branches with GitHub Pages
- URL: https://til.simonwillison.net/claude-code/preview-github-pages
- Added At: 2026-01-23 13:01:36
- Tags: #read #tips

## TL;DR
作者西蒙·威利森通过GitHub Pages部署私有仓库分支，解决了在Claude Code中开发HTML时预览困难的问题。该方法支持持续会话、自动刷新预览，且无时间限制，实用方便。

## Summary
作者西蒙·威利森主要使用 Claude Code 的网页版，特别是通过 iPhone 应用进行代码开发。然而，这种方法的一个缺点是，在迭代代码时难以实时预览工作成果，尤其是对于 HTML 项目。为解决这个问题，他开始利用 GitHub Pages 部署私有仓库的分支来实现预览功能。

具体步骤如下：首先，创建一个新的私有 GitHub 仓库并初始化；然后，在 Claude Code 中针对该仓库启动任务，并指定构建要求，如使用自包含的 HTML 文件、纯 JavaScript 和 CDN 加载依赖；Claude Code 会自动创建一个分支；接着，在仓库设置中配置 GitHub Pages 部署到此分支，并等待部署完成，即可通过秘密 URL 预览代码。

这种方法的关键优势在于：Claude Code 会话可持续运行，作者可以随时请求更改并推送更新，预览会自动刷新；没有已知的会话时间限制，可以长期使用。此外，GitHub Pages 没有内容安全策略（CSP）限制，支持与其他域的 JSON API 交互。虽然其他服务如 Cloudflare Pages 也可用，但 GitHub Pages 集成度高、方便实用。最后，提醒在合并拉取请求后，需将 Pages 设置切换回主分支。
