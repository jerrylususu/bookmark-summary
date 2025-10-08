Title: 为什么OpenAI Apps SDK对MCP的支持反而是MCP的危机

URL Source: https://grapeot.me/mcp-revisited.html

Markdown Content:
我们之前就[介绍过](https://grapeot.me/mcp.html)MCP的历史，缺陷和争议。半年过去，MCP发展如火如荼，昨天 OpenAI 又发布了 Apps SDK。这个 SDK 允许用户用一个扩展版的 MCP 在ChatGPT里面构建GUI App。这看起来是继 ChatGPT Connector 和 Gemini 支持 MCP 之后，MCP 这个开放协议取得的又一胜利。但是在研读了 Apps SDK 的一些细节之后，我反而觉得它的发布是一个危险的信号。它未必预示着 MCP 的中兴，相反，反而可能带来了一场危机。所以正好趁这个机会，复盘和阐述一下我更多的思考。

MCP Dialect的分裂
--------------

要想理解这个危机埋藏在哪里，我们得先了解一下Apps SDK是如何利用 MCP 的。之前ChatGPT已经支持了一个叫Connector的功能：开发者自己部署一个 MCP 服务器，OpenAI 和这个服务器完全使用 MCP 进行通信。这样当用户手动启用了某个 connector 并且 GPT 决策这个 connector 可以用来回答用户当前的问题的时候，它就会用 MCP 来和开发者的服务器通信。在这个基础上，Apps SDK 额外增加了 GUI 的功能，让 MCP 返回的信息不仅可以作为纯文本被 LLM 解读，而且还可以被 OpenAI 的 GUI 引擎解读和渲染，在 ChatGPT 界面里面显示一个小卡片。

![Image 1: OpenAI的官方示例](https://developers.openai.com/images/apps-sdk/inline_display_mode.png)

这些设计本身都没有问题，问题在为了实现这一点，Apps SDK 对MCP做了一个拓展，在标准的 MCP 协议之外额外添加了一个 meta 域：

*   _meta – Arbitrary JSON passed only to the component. Use it for data that should not influence the model’s reasoning, like the full set of locations that backs a dropdown. _meta is never shown to the model.

在OpenAI的文档和给的示例里，把这个域玩出了花，在里面填充了各种复杂的结构，并且定义了 `openai/*` 这样带有嵌套结构的 key-value pair。通过这个域，用户可以绕过 LLM 的 context window，传递和 GUI 相关的各种信息。这是一种非常务实而聪明的做法，规避了MCP的限制，满足了工程要求。但也是个危险的信号：这说明 MCP 最大的用户之一已经在发明协议的 dialect 了。这有点像是在标准SQL之上，各家会有不同的 dialect。MSSQL，DataBricks彼此之间互相不兼容，让标准名存实亡。而且更危险的是，SQL dialect里大家做的还是锦上添花的事情，可以通过标准的修订加以改良。但 ChatGPT 做的这件事从根本上就违反了 MCP 的祖宗之法，设计哲学。

象牙塔里发明的优雅协议
-----------

MCP是Anthropic 顶尖的 AI 科学家设计的。它发明的初衷是让科学家们在实验室里可以快速地对 Agentic AI 进行迭代。因此它的所有设计都围绕着一个核心问题：如果我们让 LLM 可以调用很多种工具，AI 可以发展成什么样？它会给人类带来哪些意想不到的好处？这种好处的边界在哪里？这是一个雄心勃勃而且确实产生了巨大影响的研究领域。也正因为它是一个面向科研而不是面向工程的协议，MCP 从诞生开始就有很多优雅的设计思想。比如：LLM 应当是所有决策的核心，它对所有工具的调用和结果应当有完整的决策权和可见性（visibility）。换言之，所有信息的交换都必须通过 LLM 的 context window。

这个设计思想是非常合理的。一方面，它有效地支撑了探索LLM能力边界的核心任务：如果一个LLM都不知道自己工具调用的结果如何，它跟LLM能力研究就没关系，我们也没必要关心这种情况了。另一方面，它也非常聪明地把状态管理这个工程界的老大难问题和协议本身解耦了。状态管理完全由LLM负责，通过context window实现，而协议本身是无状态的。

但是像我们下面要举的很多例子一样，这种优美的设计思想在实验室里效果很好，有力地帮助了科学家们探索Agentic AI的各种应用。但当它来到现实的工程世界以后，立刻就水土不服了。举个例子，比如我要做一个机票查询的app，用MCP的话流程类似这样：

1.   用户：帮我搜索明天西雅图去旧金山的机票
2.   LLM：理解用户意图，通过MCP调用机票搜索工具
3.   MCP：做搜索，返回了一个json。
4.   LLM：读取结果，向用户描述：有三班飞机，分别是几点。

当LLM用自然语言与用户沟通时，这种方法看起来没问题。但当我们想要引入 GUI时，比如第四步需要向用户渲染一个 HTML 来让他浏览，这个时候“所有信息都要经过 context window”这一设计立刻就成了一个巨大的掣肘。

第一，不论这个 HTML 是 MCP 生成的还是 LLM 自己生成的，它都会非常臃肿，信息密度很低，会污染 context window，从而降低 LLM 的智能，也会增加推理的成本。

第二，对于动辄十几 K 甚至几十 K 的输出而言，保证其中没有任何语法或细节错误，对现在的 LLM 来说仍然是一个挑战。即使是原样转述一个由程序生成的 HTML，LLM 也可能会偷懒或者弄错一两个字符。这对于自然语言来说可能没什么，但对于界面渲染之类对确定性要求很高的场合就会导致任务失败。

第三，在整个过程中，用户其实也不需要 LLM 的智能。因为将一个 JSON 文件渲染成一个 HTML 是一个确定的、使用程序就能完美做到的事情。

所以对于类似 GUI 这种用传统电脑程序就能解决的场合，强行让所有信息都流经 LLM 的 context window，反而会带来不确定性、降低任务成功率、降低 LLM 的智能、提升推理成本。有百害而无一利。这也是为什么OpenAI在MCP上开了一个洞，用 `_meta`这个域来绕过context window，传递一些LLM不可见的工程状态的原因。

整件事情的根源就在于 MCP 诞生的初衷是为了做 Agentic AI 的科研。像这种传统电脑程序就能解决的问题，本身就不在科学家的兴趣内，MCP自然也无需支持这样的场合。但问题在于 MCP 从诞生伊始就获得了过多来自投资和工程界的关注。在媒体和舆论的裹挟下，诸多开发者开始使用 MCP 来开发相关的应用。这逼着 MCP 以一个不成熟的状态被迫承担了太多在它设计目标之外的应用，也让整个领域都非常痛苦。

磕绊中的挣扎发展
--------

事实上，类似的痛苦与挣扎也不是第一次了。MCP 一直有诸多围绕是否适合实际工程应用的争论。有三个例子也许最为知名：

第一是它早期的交互用的是stdio。这从工程角度来说是一个业余到震惊的选择，彻底排除了remote server的可能，后来在一两年后终于被社区修正。

第二是它从头就没有考虑过authentication和authorization，这在科研背景下是合理的，但是给后续工程应用带来了巨大的混乱。首先是大家各自实现了自己的auth的方法，造成了MCP的分裂，然后官方试图引入OAuth 2.1修复这个问题，结果一方面暴露了过多的实现细节，让开发体验非常差；一方面也[引入了很多安全漏洞](https://www.docker.com/blog/mpc-horror-stories-cve-2025-49596-local-host-breach/)。当时有很多drama，直到后来它又引入了一个[breaking change](https://modelcontextprotocol.io/specification/2025-06-18/changelog)，在解决（其实是转移了）大部分问题的同时，也给很多已经使用了MCP的企业带来了额外的迁移成本。

第三是它基于JSON RPC本身没有任何类型检查，所有错误都要到运行时才暴露，也没有tracing、ID等等分布式系统关于observability和debuggability的标准设计，调试起来非常痛苦。

就总之，它的设计思想本身很美很优雅，但是在[重走整个工程界关于RPC这几十年的老路](https://julsimon.medium.com/why-mcps-disregard-for-40-years-of-rpc-best-practices-will-burn-enterprises-8ef85ce5bc9b)，至少在目前，工程上远不能称为成熟。

当然标准并不是一个纯技术问题，并不是说技术最好的标准就能取得成功。但是MCP基础设计上没有工程考量，在初期又有了巨大的媒体关注度，吸引了大量投入。这导致大家没办法另起炉灶，就只能像OpenAI一样在标准上打洞，发明新的dialect。这就像当时的浏览器大战和SQL语言大战一样，厂商通过自己的特殊实现锁定客户，倒逼标准发展。

而这也是OpenAI和Anthropic角力的一种方式。通过引入这个私有的`_meta`域，OpenAI现在就有了自己对MCP（变种）的定义权。在这个域里加入`openai/*`的协议，从政治斗争的角度来说，给了OpenAI定义AI能力和格式的权力，一定程度上架空了Anthropic对MCP的控制。比如开发者一旦深度使用了`openai/*`这个`_meta`结构，他的应用就不再是一个通用的MCP应用，而是一个高度绑定的ChatGPT App。这个App变成也从一个开放标准的实现，变成了OpenAI这个公司自己的护城河。

MCP的未来藏在别的开放标准的历史里
------------------

下面一个自然的问题就是，MCP的未来在哪里呢？我想说，太阳下面没有新鲜事，我们也许可以看一下四个开放标准的例子。

第一个例子是 HTTP 协议，它是一个开放的标准的协议，基本上没有任何 dialect，大家会在它的基础上构建应用，但不会说我这个协议兼容 HTTP 协议同时增加了一些其他功能。

第二个例子是 USB 接口，它本身有很多变种，比如 2.0、3.0 等等，但是除了 Thunderbolt 以外也极少有厂商说我做了一个兼容 USB 口的协议，补全了一些功能。

第三个例子是 SQL 这门语言，这个语言本身是标准的，但是不论是 Databricks、MS SQL Server 还是其他的服务提供商都会有各自的 dialect，它会兼容传统的 SQL 语言，但也会加入自己的私货，让它变得彼此不兼容。比如 Databricks 上面写的特化 SQL 放到 MS SQL 上是跑不起来的。

第四个例子是 CSS，CSS 本身是个标准的东西，但是 Webkit、Mozilla 等等浏览器分别对它有特化，形成了自己的 dialect，即使一个 CSS 在 Webkit 浏览器上能正常渲染，你把它挪到另一个体系里，比如Firefox 里面，它也无法正常渲染。

上面的这四个例子都有一个共同特征，它们都是一个看起来标准的、人人都支持的技术接口。但它们又可以分为两类。一类是管道本质，可以即插即用的。比如 A 厂商的 USB 口插到 B 厂商的主板里，现在基本百分之百都能用。Windows 的 HTTP 协议栈接受来自 Linux client 的 HTTP 请求，Nginx解析和操纵来自Apache的HTTP头，也百分之百都能成功响应。而另一类同样是开放标准，却更注重表达性，也因此产生了各种分裂的变种。Databricks 的 SQL 放到 MySQL 上却跑不起来，Mozilla 特化的 CSS 放到 Chrome 上也不能正常渲染。

我比较悲观地认为MCP更像是后者。一方面，它是一种表达性的，跟内容相关的协议。今天要支持GUI，明天要支持视频直播，天生就有分裂的倾向。另一方面，它的过早爆火让它还没来得及脱掉学术气息就承担了工程的责任。在过去一年里，我们看到整个Agentic AI领域在MCP这个理想化、科研式的设计理念和框架下挣扎着向前发展。而现在，已经出现了厂商开始违背最基本的设计思想，通过私有dialect来暗渡陈仓。标准的分裂已经成了一个隐蔽的现实。

所以，OpenAI的这个协议看起来是MCP的胜利，其实潜伏着更深层的危机。我对未来也有几种预测。一种可能是OpenAI架空MCP，类似IE6成为事实上的CSS标准。一种可能是类似SQL各种dialect把大家逼疯了，出现了更高层次的抽象协议比如JDBC/ODBC。那又会出现一个MCP的MCP，负责把一个统一的语义协议翻译成OpenAI的Apps MCP，Anthropic的原教旨MCP，Google的A2A等等。结果如何，得看各家的技术和政治斗争了。