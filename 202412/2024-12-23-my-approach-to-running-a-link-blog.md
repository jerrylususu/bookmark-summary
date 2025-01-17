# My approach to running a link blog
- URL: https://simonwillison.net/2024/Dec/22/link-blog/
- Added At: 2024-12-23 15:11:54
- [Link To Text](2024-12-23-my-approach-to-running-a-link-blog_raw.md)

## TL;DR
作者从2003年开始运营链接博客，记录发现的内容并附上评论。2024年升级支持Markdown，增加创作者信息、引用段落等，提升内容丰富性。技术上基于Django，实现图片处理、搜索和草稿功能。鼓励通过链接博客分享有趣内容，为社区贡献价值。

## Summary
1. **链接博客的起源**：
   - 作者从2003年11月开始在个人域名上运行一个基本的链接博客，发布带有标题、URL、简短评论和“via”链接的“blogmarks”。
   - 至今已发布7,607篇链接博客文章。

2. **链接博客的升级**：
   - 2024年4月，作者升级了链接博客以支持Markdown，使其功能更加丰富。

3. **链接博客的使用指南**：
   - **写作内容**：链接博客的目的是记录作者发现的内容，结合公共书签和个人评论。
   - **添加额外内容**：
     - 作者尝试在链接博客中加入更多内容，如创作者的姓名、相关背景信息、引用段落、代码链接等。
     - 目标是让读者在阅读链接博客后，即使不点击链接也能获得有用的信息。
     - 作者还会引用视频的片段、提供截图或短片，以增强内容的丰富性。
   - **技术实现**：
     - 链接博客基于Django应用程序，使用Django Admin进行创建和编辑。
     - 图片处理方面，作者使用自定义工具将图片转换为较小的JPEG格式，并上传到S3存储桶，通过Cloudflare免费服务提供图片。
     - 搜索功能使用Django和PostgreSQL实现，支持分面搜索。
     - 作者还实现了草稿模式，允许在发布前预览内容。
     - 每周发送的电子邮件通讯直接复制博客内容，使用Substack平台。

4. **鼓励更多人参与**：
   - 作者认为分享有趣的链接并附上评论是一种低成本、高价值的方式，可以为互联网社区做出贡献。
   - 社交媒体平台如Twitter、LinkedIn等通过算法减少了链接的分享，而Bluesky和Mastodon则没有这种限制。
   - 作者希望更多人能够通过链接博客或社交媒体分享有趣的链接。
