# Understanding ChatGPT Work
- URL: https://simonwillison.net/2026/Aug/30/understanding-chatgpt-work/
- Added At: 2026-08-31 09:33:20
- Tags: #read #llm #agent

## TL;DR
Simon Willison 通过大量实验揭示，ChatGPT Work 并非简单升级版，而是拥有开放联网、代码执行、无头浏览器、持久存储、建站、子代理和定时任务的强大云端代理环境。但 OpenAI 只谈用途不谈能力，且隐藏细节，加上提示注入风险，使其功能强大却令人困惑。

## Summary
Simon Willison 在 2026 年 8 月 30 日的文章里，通过大量实验试图搞清楚 OpenAI 推出的 ChatGPT Work 到底是什么。他的核心结论是：这个产品功能非常强大，但也极其令人困惑。

ChatGPT Work 实际上包含两个产品。一个是在云端运行的版本，可以通过 chatgpt.com 或 ChatGPT 手机应用访问，文章称它为 Work Cloud。另一个是桌面应用版本，也就是以前叫 Codex 的那个应用，安装后可以访问你电脑上的文件和程序，被称为 Work Local，更像是换了个不那么吓人的名字的 Codex。文章后面只讨论 Work Cloud。

目前 ChatGPT Work 只对付费用户开放，至少需要每月 20 美元及以上的订阅。免费用户和每月 8 美元的 Go 用户都用不了。

Work 和普通的 ChatGPT Chat 最本质的区别不在于“用途”，而在于它多了一堆 Chat 没有的功能。OpenAI 官方说 Chat 用于回答问题、头脑风暴、写简短草稿，Work 用于完成有明确结果的任务，比如做简报、分析、定期更新、工作流或可交付文件。但 Simon 认为这个说法几乎没用，因为他多年来一直用普通 Chat 干这些事。

他通过大量测试，总结出 Work 独有的功能主要有以下几点：

**模型选择更丰富**  
在 Work 里可以选 GPT-5.6 的 Sol、Luna 或 Terra，每种模型都有从 Light、Medium、High、Extra High、Max 到 Ultra 的推理级别。也可以选 GPT-5.5。这些看起来和 OpenAI API 里提供的模型一样。而普通 Chat 只提供 5.6 Instant、Medium、High、Extra High 和 Pro，其中 Extra High 和 Pro 只对每月 100 美元以上的用户开放，20 美元用户最高只能到 High。Chat 不告诉你这些是 Sol、Luna 还是 Terra，作者猜是 Sol。5.6 Pro 似乎是 Chat 独占，Work 里没有。另外，Work 会话消耗的是 Codex 的额度，Chat 会话另有独立额度，这可能是两者模型选项不同的原因之一。

**带互联网访问的代码执行环境**  
这是 Simon 最兴奋的功能。ChatGPT Chat 的代码解释器不能访问外网，无法安装额外软件包或调用外部 API，会被容器代理拦截。而 Work 的代码执行环境默认可以访问整个互联网，也可以配置成只允许特定域名。这意味着你可以让它克隆 GitHub 仓库、安装依赖，然后用这些工具去和网络上的其他服务交互。相比之下，Claude 的同类容器虽然也有受限互联网访问，但域名白名单非常短，基本只能从 PyPI、NPM 装包和克隆 GitHub 仓库。Work 的能力要开放得多。

**完整的无头 Chrome 浏览器**  
Work 可以启动一个真实的 Chrome 实例，加载网页、填写表单、截图。如果网站需要登录，浏览器可以提示你接管操作，手动输入密码和两步验证码，这些凭据不会经过模型本身。它甚至可以在加载的页面上运行 JavaScript，操作 DOM。Simon 举了个例子，他让 Work 加载 simonwillison.net 并用 JavaScript 提取所有标题，Work 真的启动了浏览器并执行了代码。这感觉很像他自己的 shot-scraper javascript 工具，但现在在手机上也能用了。

**持久共享的文件系统**  
普通 Chat 的每个会话都有一个全新的临时文件系统，会话之间无法互相访问。而 Work 的每个会话有自己的 scratch 文件夹，比如 `/workspace/scratch/e00a0a017944`，这些文件夹会跨会话保留，所以你可以访问之前聊天里产生的文件。Simon 说他的 `/workspace/scratch` 下已经有 171 个文件夹。而且，目前所有正在运行的 Work 会话似乎挂载的是同一个 `/workspace` 卷，一个会话里做的文件修改，其他会话能立刻看到。但它们不共享进程空间，一个会话里运行的 localhost 服务器无法被另一个会话访问。

**ChatGPT Sites**  
Work 可以构建并部署完整的网站，底层用的是 Cloudflare Workers。这些网站可以有 HTML、JavaScript，还能运行服务端功能，包括使用 Cloudflare D1 和 R2 实现有状态的功能。网站默认是私有的，只对创建者可见，但可以设为公开，或者在团队计划里分享给特定的人。Simon 举了一个例子：他让 Work 找出伦敦所有有“虔诚鹈鹕”宗教图像的地方，生成 JSON 文件，然后建一个网站。这个网站就是 london-pelicans-in-her-piety.simonw.chatgpt.site。

**子代理**  
ChatGPT Chat 不能运行子代理，Work 可以。这是一个面向高级用户的功能，如果项目很复杂，需要多个并行代理协作，Work 就能派上用场。在 Work 里，子代理可以使用 Sol、Luna 和 Terra 这些模型。

**定时提示自动化**  
你可以设置定时任务，例如“每天早上 8 点搜索一下 Waymo 有没有宣布 Half Moon Bay 的发布日期”。这些定时提示可以自己判断有没有新情况，然后决定是否通知你。Simon 后来更新说，这个功能其实在普通 Chat 里也有，但它在 Work 里仍然值得注意，因为可以和 Work 独占的其他功能结合，比如让定时任务每小时更新一个 ChatGPT Site。

**安全担忧**  
Simon 提出了他的“致命三合一”模型：任何代理系统如果同时具备以下三点就很危险——能访问私有数据、暴露在不可信内容中、有办法把窃取的信息传回攻击者。ChatGPT Work 三点全占。他很想听 OpenAI 讲清楚他们如何保护 Work 会话免受提示注入攻击。他猜测答案可能和 Codex 的自动审查机制一样。

**产品令人困惑的原因**  
Simon 认为，搞清楚这一切花了太多力气，问题主要有两个：第一，OpenAI 解释 Work 时讲的是“它用来干什么”，而不是“它实际能做什么”；第二，OpenAI 仍然坚持隐藏系统提示词和工具描述。如果文档里直接给出 Work 的系统提示词和工具描述，他就不需要写这篇文章了。

**工具和技能清单**  
文章发布后不久，Simon 又想到一个主意：他开了一个新的 Work 会话，让它建一个网站，列出自己的每一个工具，并按类别分组，解释每个工具的作用，尽量准确复制参数和描述。这个网站是 codex-tool-reference.simonw.chatgpt.site，里面列出了 223 个已注册工具，其中 6 个来自他自己的个人 MCP，通过 datasette-mcp 提供。

他还注意到工具列表里和浏览器相关的主要是 `web.run`，这并不能完全解释无头浏览器自动化的全部能力。于是他让 Work 把每个技能的完整内容也加到网站上，结果发现 Work 使用了 44 个技能。其中 `control-browser` 技能解释了浏览器如何工作：通过 Node REPL 的 `js` 工具运行浏览器设置代码，实际交互通过 `browser-client` 运行时暴露的 `agent.browsers.*` API 完成，使用前必须先读取 `await browser.documentation()` 返回的完整文档。Simon 又让 Work 把这份浏览器文档的完整输出加到了 `/skills/control-browser` 页面底部。其他值得注意的技能包括：创建 `.docx` 文件的 `documents`、图像生成技巧的 `imagegen`、读写 PDF 的 `pdf`、处理 Excel/CSV 的 `spreadsheets`、构建 ChatGPT Sites 的 `sites:sites-building`、回答自身问题的 `openai-docs`，以及构建数据仪表板的 `data-analytics:build-dashboard`。

总的来说，这篇文章的核心是：ChatGPT Work 不是一个简单的 Chat 升级版，而是一个在云端拥有开放互联网访问、真实浏览器、持久存储、建站能力、子代理和定时任务的强大执行环境。但它被 OpenAI 包装得非常模糊，用户很难直观理解它到底能做什么，只能靠自己做实验去发现。
