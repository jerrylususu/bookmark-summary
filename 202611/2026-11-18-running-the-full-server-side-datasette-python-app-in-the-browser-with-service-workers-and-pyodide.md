# Running the full server-side Datasette Python app in the browser with service workers and Pyodide
- URL: https://simonwillison.net/2026/Nov/17/datasette-lite/
- Added At: 2026-11-18 15:15:20
- Tags: #read

## TL;DR
文章讲 Datasette Lite 用 Service Worker 重写，可在浏览器运行完整 Datasette，支持指定版本、插件和 SQLite，便于演示和复现 bug，并展望 Python 应用的 WebAssembly 预览。

## Summary
这篇文章讲的是 Simon Willison 把 Datasette 这个服务端 Python 应用完整搬进浏览器运行的项目 Datasette Lite，以及它的一次彻底重写。

**核心结论**：Datasette Lite 现在用 Service Worker 架构重写，效果几乎和真正的服务端 Datasette 无法区分。你只需要一个精心构造的 URL，就能在浏览器里跑起完整的 Datasette，包括插件、特定版本、甚至特定版本的 SQLite。

**它能做什么**。通过 `lite.datasette.io` 上的 URL 参数，你可以：加载任意 SQLite 数据库、JSON、CSV 或 SQL 脚本；指定从 PyPI 加载某个已发布的 Datasette 版本；从 GitHub 仓库加载特定 commit、tag 或分支；从 100 多个 SQLite 版本中挑一个；以及从 PyPI 或 wheel 文件 URL 安装额外插件（包括 JavaScript 可视化插件）。因为能锁定版本、插件和 SQLite 版本，它特别适合用来给进行中的功能做演示、或者复现 bug，而不必真的起一台服务器。

**文章给了一个很典型的示例 URL**，拆开看是这样的：`?install=datasette-maplibre` 从 PyPI 安装地图插件，可以重复传多次来装多个插件；`&url=.../demo.db` 从给定 URL 加载 SQLite 数据库，这些 URL 必须带开放的 CORS 头，作者习惯放在 Gist 上；`&metadata=.../metadata.yml` 加载元数据文件，给表和首页加 HTML 描述；最后的 `#/demo/capitals_and_countries%23map=0/4.2/180&color=continent` 是一个 fragment hash，先转成 Datasette 内部路径，再附加第二个 fragment（`%23` 是 URL 编码的 `#`），用来告诉地图插件缩放到某个位置、按 `continent` 列给图形上色。这个技巧叫“URL 可寻址的 Pyodide Python 环境”，作者去年专门写过。

**作者已经在开发流程里用它**。文章举了一个分页 bug 的例子：他用 `?ref=1.0a42` 和 `?ref=1.0a43` 两个链接，分别展示旧版本出错（翻到第二页是空的）和新版本修复后的行为，直接贴在 GitHub issue 评论里。

**为什么重写：旧版的 hack 路线**。2022 年第一版其实是个玩笑式项目，做法是在 Pyodide 的 web worker 里跑 Datasette，模拟请求，再把生成的 HTML 用 `innerHTML` 注入顶层页面。问题是 `innerHTML` 里的 script 标签不会执行，所以任何依赖 JavaScript 的功能都失效，额外的 JS/CSS 也加载不了。

**新架构：Service Worker**。Service Worker 能拦截页面对新页面和资源的 HTTP 请求，改由客户端代码返回响应。Datasette Lite 为整个 `lite.datasette.io` 域名注册一个 service worker，父页面再创建一个 iframe，向形如 `/app/aa94e6851595/...` 的 URL 发请求——这些就是正常的 Datasette URL，只是加了 `/app/<session>/` 前缀。

**为什么要 session 前缀**：service worker 在所有标签页之间共享。如果所有标签页都路由到同一个 Datasette 实例，那么不同 URL 想加载不同插件、不同配置就会互相打架。所以父页面为每个标签页生成一个随机 session ID 作前缀，service worker 据此把请求路由回对应标签页，再转给该 session 专属的 web worker 里运行的 Datasette 实例。

**为什么还要 web worker**：因为 Pyodide 直接跑在 service worker 里，状态大概撑不过 30 秒（取决于浏览器），所以必须把 Python 运行时放在 web worker 里保持状态。作者感叹这里“活动部件太多了”。

**完整请求链路**（文中配了一张架构图）：1）iframe 请求 `/app/session/...`；2）`sw.js` 拦截并 post 给所属标签页；3）`shell.js` 转发给 web worker；4）Python 加上 cookie 调用 Datasette，Datasette 查询 SQLite；5）状态码、头、响应体返回页面；6）经 MessagePort 回到 `sw.js`；7）`sw.js` 交给浏览器一个 Response，iframe 渲染出来。

**这个系统的来历**：2026 年 5 月它只是用 Claude Opus 4.8 生成的一个 AI 研究 spike，直到 11 月（用 Claude Fable 5.2）作者才觉得足够熟悉、敢上生产。

**附加功能：自选 SQLite 版本**。Datasette 声称支持 3.25（2018 年 9 月）以来的任何 SQLite 版本，之后又发布了 87 个版本。作者建了 `datasette/pysqlite3-wasm-wheels` 仓库，为 163 个 SQLite 版本编译了 pysqlite3 的 WebAssembly Python wheel，文件名类似 `pysqlite3-0.6.2-3.54.1-cp314-cp314-pyemscripten_2026_0_wasm32.whl`。Datasette Lite 新增 `?sqlite=3.54.1` 参数，会解析出对应 wheel、下载、装进 Pyodide，并让 Datasette 使用它。这个功能是作者调查一个疑似 SQLite bug 时的副产物。

**配套对比工具**：作者还让 Claude 做了个工具，可以选多个 SQLite 版本跑同一条 SQL 并对比结果。示例是 `select json_object('a', (select json_array(1)))`：在 3.54.1 里，键 `a` 的值是带双引号的字符串形式的数组；在 3.54.0 里则是真正的数组。工具会标出“版本间结果不同”。

**更大的意义**：这套做法并不专属于 Datasette，几乎所有 Python 应用都能用同样方式在浏览器里跑，作为廉价的预览环境、功能演示和 bug 复现手段。以前 C 和 Rust 扩展是障碍，但现在 coding agent 能把它们编译成 Pyodide 兼容的 WebAssembly，而且 2026 年 4 月的 PEP 783 之后还能直接发布到 PyPI。唯一明显的坑是数据库：SQLite 完全没问题，但在 WebAssembly 里跑 PostgreSQL 或 MySQL 虽然可行，仍是少有人走的路。作者希望这种 WebAssembly 预览环境能成为 Python 生态的常见模式。
