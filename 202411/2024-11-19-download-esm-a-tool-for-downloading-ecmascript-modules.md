# download-esm: a tool for downloading ECMAScript modules
- URL: https://simonwillison.net/2023/May/2/download-esm/
- Added At: 2024-11-19 16:48:18

## TL;DR
`download-esm`是一个CLI工具，用于下载ECMAScript模块版本的npm包及其依赖，并重写导入语句。作者开发此工具以简化开发流程，避免依赖CDN和本地构建脚本的问题。工具通过Python编写，支持安装和使用简单，已成功测试多个包，并欢迎社区参与改进。

## Summary
1. **工具介绍**：
   - **download-esm**：一个CLI工具，用于下载ECMAScript模块版本的npm包及其所有依赖，并重写所有导入语句以指向本地副本。

2. **开发动机**：
   - **个人偏好**：作者不喜欢使用本地构建脚本，因为依赖更新和工具过时问题频繁。
   - **简化开发**：希望直接将`.js`文件放入目录，加载到HTML文件中开始编码。
   - **依赖管理**：希望在项目中包含JavaScript依赖，而不是依赖CDN的可用性。

3. **ECMAScript模块**：
   - **优点**：支持浏览器多年，允许按需加载代码，模块间可相互导入，浏览器会并行下载并缓存。
   - **挑战**：从CDN下载这些文件并存储在本地非常繁琐，特别是当模块有多个嵌套依赖时。

4. **灵感来源**：
   - **Observable Plot**：作者在Observable Plot仓库提出问题，希望在没有CDN的情况下使用Vanilla JS。
   - **Mike Bostock的建议**：建议编写一个工具，从CDN下载编译的ES模块并重写导入语句为相对路径。

5. **工具功能**：
   - **安装**：可通过`pip install download-esm`或`pipx install download-esm`安装。
   - **使用**：下载指定npm包及其依赖，重写导入语句并保存到指定目录。
   - **示例**：下载`@observablehq/plot`及其依赖，生成`index.html`文件并启动本地服务器进行测试。

6. **工作原理**：
   - **代码量**：仅100行Python代码，主要通过正则表达式完成大部分工作。
   - **测试**：已成功用于`preact`、`htm`、`codemirror`，部分用于`monaco-editor`。

7. **社区参与**：
   - **开放问题**：邀请用户帮助测试其他包，并分享使用经验。
   - **贡献欢迎**：作者希望工具能更健壮，欢迎社区贡献代码和反馈。
