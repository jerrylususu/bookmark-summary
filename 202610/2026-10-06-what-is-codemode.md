# What is Codemode
- URL: https://lucumr.pocoo.org/2026/10/6/codemode/
- Added At: 2026-10-06 15:23:47
- Tags: #read #agent

## TL;DR
Armin Ronacher 介绍 Pi 1.0 的 Codemode：让 LLM 在 harness 侧用代码编排工具调用，而非把工具输出塞进上下文，从而支持组合、并发与状态暂存。作者认为这是 MCP 的自然归宿。

## Summary
这篇文章是 Armin Ronacher（Flask 作者、Sentry 联合创始人）2026 年 10 月发的博客，讲的是 Pi 1.0 引入的 **Codemode** 功能。它表面上是解释一个新特性，实际上是对"LLM 应该怎么调用工具"这个问题的一次系统性梳理。下面按文章的脉络讲。

---

**背景：作者一年前的立场**

作者一年多前写过两篇文章，核心主张是：**不要把自定义工具（或 MCP 服务器）一股脑塞进 LLM 的上下文，而是让模型多写脚本**。一篇叫《Code Is All You Need》，一篇讲《MCP needs code》。现在 Pi 1.0 反过来加了 MCP 支持，但方式是通过 Codemode——所以他说这是"迟早的事",但对一些人来说可能有点意外。他想借这篇更新一下想法。

---

**一、什么是"工具"，以及 bash 的边界**

像 Pi 这样的 harness（智能体外壳）给 LLM 提供工具，这些工具定义会翻译成服务端的 token 结构。模型是否被鼓励去调用某个工具，是强化学习的结果——模型在训练中就学会了文件系统怎么运作，所以它调 `echo foo > /tmp/test.txt` 时，也知道之后 `/tmp` 里会多出一个 `test.txt`。

作者强烈偏好 CLI 和 bash，因为**调用容易组合**。但 bash 有一个根本限制：它只能组合"能运行的程序"。有些东西不是程序，却是 LLM 的原生工具，必须由 harness 直接提供：

- `read` / `view_image`：多模态模型要看图，不能用 `cat`，因为 harness 得把真正的图像 payload 注入到 LLM 协议里。
- **子 agent**：spawn 和编排子 agent 很难绕开 harness 提供的工具。理论上可以用 CLI + 环境变量 + Unix socket 和外部 harness 通信，但很粗糙。

---

**二、大脑与手：为什么要区分**

要理解 Codemode，得先想清楚各个部件在哪里运行。通常有两个系统：

- **大脑（harness）**：运行在一台机器上，是**可信的**。
- **手（执行环境）**：工具真正执行的地方。在 Pi 里叫 execution environment。

关键是两者之间有一条**分界线**：它们文件系统不同、信任级别不同。比如用 Gondolin 这类沙盒方案，bash 会被沙盒隔离，但 harness 本身不会。

---

**三、Codemode 到底做什么**

Codemode 让 LLM 在 **harness 侧**表达和编排复杂操作，而不是在执行环境侧。它运行在 harness 自己的沙盒里。在 Pi 中就是 WASM 里跑 QuickJS，**故意限制**：没有网络、没有文件系统、没有定时器、内存有限。唯一的出口就是调用更多工具。理论上也可以换成 Scheme 等语言。

说白了，Codemode 就是**用某种编程语言（这里是 JavaScript）来发起工具调用**。它的价值在于：

- **绕开 LLM 上下文做组合**。普通 bash 工具调用只把尾部 2000 行塞进上下文，想看更多得自己去翻溢出文件；而通过 Codemode 调用，输出会**结构化**地送到 Codemode 侧。
- **并发和工作流**。因为是 JS，可以写并发操作和基本工作流。常见套路：先探测 5–10 个项目看响应长什么样，再写脚本批量处理剩下的 n 个。
- **状态可以存进 transcript**。一次 Codemode 调用可以把数据 `store()` 起来，会话里下一次调用再读回来——而且这是在 harness 主机上，不是沙盒里。
- **暴露一些传统工具里没意义的能力**。比如用图像模型生成图片、用 one-shot 分类器分类文本——这些如果做成普通工具只会浪费上下文，所以只在 Codemode 里暴露。

命名来自 Cloudflare。

---

**四、几个真实例子**

文章强调：下面的代码都不是人写的，是 Pi 真实会话里的，只是重新缩进了。Codemode 默认只在启用 MCP 时开启，可以用 `"defaultTools": ["+codemode"]` 打开。

1. **生成图像**：调用 `models.getAvailableOfType("image")` 拿到画家模型，`models.generateImages` 生成，再用 `image()` 把图作为图像内容发回给 LLM，同时落盘成临时工件，方便后面传给 bash。

2. **分类**：用 Jev 分类模型批量处理 GitHub issues 做情感分析。它用 `gh issue list` 拉数据，`Promise.all` 并发跑分类（Pi 自己把并发限制在 4 个，其余排队），最后 `store("sentiment_results", ...)` 把结果存进会话，供后续调用读取。

3. **驱动游戏引擎调试**：它知道用户的 `tankctl` 命令，自己搭了个 30 步循环——每一步从游戏引擎拿文本状态，再交给 Jev 决定下一步动作（攻击、接近、闪避、捡道具），然后执行命令并记录日志。

4. **调用 MCP 服务器**：因为不把 MCP 工具直接暴露给 LLM，agent 先在 Codemode 里用 API 做 tool search 做**渐进式发现**。例子是直接调用 Sentry MCP 的 `find_organizations`、`find_projects`。

---

**五、现代 MCP 是一场战斗**

MCP 协议本身很受益于 Codemode，但现实问题是：**很多 MCP 服务器针对的是还没用 Codemode 的 harness**。

于是出现了一种临时权宜之计——像 Cloudflare 那样，**在 MCP 服务器内部再做一层 Codemode**。结果就是"Codemode 套 Codemode"：双重 JSON 转义、小模型容易晕、内层代码还调不到外层的工具。作者觉得这不理想，但可以理解为什么会这样。文章给了一段用 Cloudflare MCP 的 `execute` 工具、里面再写 JS 的例子来说明这种别扭。

---

**六、对 MCP 的期望**

要让 Codemode 和 MCP 配合得好，作者提了几条建议：

- **结构化内容**：Codemode 希望返回格式良好的 JSON，MCP 的 `outputSchema` 很适合这个。
- **一致的结果**：有的服务器会根据结果集大小做 token 优化，导致先探测 5 条成功、换成最大批量就失败。这种不一致很坑。
- **大二进制数据**：MCP 目前还不支持，很多有意思的场景跑不通，只能搞预签名 URL 之类的弯弯绕。
- **可组合的工具搜索**：MCP 服务器可能比客户端更清楚哪个工具合适，但目前没有机制让 harness 跨多个 MCP 服务器扇出搜索，全靠涌现行为，多服务器时扩展性差。

---

**七、Codemode 的未来**

作者不认为这是对一年前"多用 CLI"主张的反转。恰恰相反，**MCP 生态正在采纳他当年指出的方向——代码**。而 Codemode 走得更远：它能在 harness 内部作为一套机制，给 agent 更多表达自由。

但还有问题没解决：

- **持久性**更难，可能得借鉴 durable workflow 引擎，对调用做快照；或者干脆用 **Starlark** 这类确定性更强的语言替代 JavaScript。
- **图像、二进制数据**，以及**小模型根本用不好这套模式**，都还需要继续打磨。

结论：还不是完美方案，但已经是个相当有用的模式，作者预计会被更多采用。

---

**一句话总结**

Codemode 的本质是：**让模型在 harness 侧用代码（JS）来编排工具调用，而不是把一堆工具的原始输出塞进 LLM 上下文**。它把"大脑"和"手"分开，让组合、并发、状态暂存都发生在受限的 WASM 沙盒里，唯一的出口还是调用工具。作者认为这既是 MCP 的自然归宿，也超出了 MCP——是给 agent 表达能力的又一次升级。
