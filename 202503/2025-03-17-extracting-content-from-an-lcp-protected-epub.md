# Extracting content from an LCP "protected" ePub
- URL: https://shkspr.mobi/blog/2025/03/towards-extracting-content-from-an-lcp-protected-epub/
- Added At: 2025-03-17 14:12:37

## TL;DR


该文介绍通过调试Electron框架的Thorium阅读器破解LCP加密EPUB的方法：启用调试模式后提取已解密的HTML、图片等资源，重组为DRM-free电子书。作者强调此举仅用于合法购书用户的格式转换，但引发伦理争议，Readium联盟警告可能因此升级DRM限制。文中指出当前LCP方案限制用户设备选择且增加开发者成本，作者坚持技术缺陷需公开以维护用户权益。

## Summary


该文章介绍了如何通过调试LCP（Logon-based Content Protection）加密的EPUB电子书阅读器Thorium，提取其未加密内容的方法。步骤如下：

1. **技术背景**  
   LCP虽采用密码学保护，但需用户输入密码解锁，应用本身会在本地存储解密密钥。通过调试Electron框架的Thorium阅读器，可直接获取已解密内容，无需破解加密算法。

2. **操作步骤**  
   - **准备Thorium**：将AppImage格式的Thorium解包并启用调试模式（`--remote-debugging-port=9223`），通过Chrome访问调试界面（`http://localhost:9223`）。  
   - **提取内容**：在调试窗口的“Content”标签中查看HTML、图片等资源，通过JavaScript `fetch`命令获取Base64编码的文件内容：  
     - 图片：使用`fetch("httpsr2://.../image.jpg")`转换为Base64后保存。  
     - CSS/HTML：直接获取文本内容，但发现Thorium注入了额外样式和脚本。  
     - 元数据（如`content.opf`）：直接提取与原文件大小一致的明文。  
     - 字体文件：通过类似图片的Base64提取方法。  
   - **重组EPUB**：将提取的文件按原EPUB目录结构重组并压缩为ZIP后重命名，生成DRM-free电子书。PDF文件通过类似方式提取。

3. **伦理争议**  
   - 作者强调方法仅用于合法购书的个人研究，且未破解加密或侵犯知识产权。  
   - Readium联盟（LCP开发者）警告此举可能导致更严苛DRM出现，并试图通过情感施压阻止公开方法。作者反驳称：  
     - LCP限制用户选择阅读设备（如旧设备、Kobo不支持）。  
     - 开源阅读器因认证费用高无法适配。  
     - 用户应有权在任意平台阅读已购内容。

4. **法律与风险**  
   - 作者提醒该方法手动操作复杂，不可自动化。  
   - Readium可能因技术缺陷加强加密，触发法律维权。作者坚持发表以警示DRM缺陷，维护用户权利。

此方法依赖Thorium内置的调试功能，未涉及逆向工程或密钥窃取，但强调仅用于合法用途。
