# Using GitHub Pages as a URL shortener / redirection service | Christian Heilmann
- URL: https://christianheilmann.com/2025/08/11/using-github-pages-as-a-url-shortener-redirection-service/
- Added At: 2025-08-12 15:13:14
- [Link To Text](2025-08-12-using-github-pages-as-a-url-shortener-redirection-service-christian-heilmann_raw.md)

## TL;DR


该文介绍通过GitHub Pages与Jekyll搭建免费URL缩短服务的方法，使用插件jekyll-redirect-from实现直接跳转，结合自定义模板添加延迟跳转功能，并用JavaScript增强用户交互（倒计时/进度条/取消按钮），项目已开源，支持自定义域名及深浅模式适配。

## Summary


本文介绍了利用GitHub Pages搭建免费的URL缩短与重定向服务的方法，替代付费或存在垃圾信息的第三方服务。步骤如下：

1. **基础配置**
   - 使用Jekyll插件`jekyll-redirect-from`，在站点配置文件`_config.yml`中加载插件并设置白名单：
     ```yml
     gems: - jekyll-redirect-from
     plugins: - jekyll-redirect-from
     ```
   - 创建Markdown文件（如`offwego.md`），通过Frontmatter指定重定向目标：
     ```markdown
     ---
     redirect_to: https://christianheilmann.com
     ---
     ```
   - 该设置实现直接服务器跳转，用户无法取消。

2. **增强功能：带延迟的可控重定向**
   - 创建集合`_go`管理重定向链接，配置`_config.yml`启用输出：
     ```yml
     collections: go: output: true
     ```
   - 设计自定义模板`redirect.html`，通过HTML的`<meta refresh>`标签实现延时跳转，Frontmatter可定义延迟时间和目标URL：
     ```html
     <meta http-equiv="refresh" content="{{page.delay}}; url={{page.goto}}">
     ```
     示例Frontmatter：
     ```yml
     goto: https://christianheilmann.com
     layout: redirect
     delay: 10
     ```

3. **JavaScript控制与进度条**
   - 通过JavaScript替代元标签，提供用户交互：
     - 显示倒计时和进度条（`progressBar`元素）。
     - 加入取消按钮，点击后停止跳转并展示目标链接。
     - 支持浅色/深色模式适配。
   - 示例脚本逻辑：每秒更新倒计时，延迟结束触发跳转，按钮事件清除计时器并展示取消结果。

4. **项目资源**
   - 完整实现已开源：[GitHub仓库](https://github.com/codepo8/gh-pages-urlshortener)
   - 实际演示：通过`clxi.org/go/...`或`codepo8.github.io/gh-pages-urlshortener/go/...`访问。
   - 功能特点：免费、自定义域名、带取消选项的延迟跳转、多模式适配。

此方案结合静态站点生成器Jekyll与GitHub Pages，实现低成本可控的URL缩短服务。
