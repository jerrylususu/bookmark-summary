# Migrating the GitHub Copilot runtime to Rust, using Copilot
- URL: https://github.blog/ai-and-ml/generative-ai/migrating-the-github-copilot-runtime-to-rust-using-copilot/
- Added At: 2026-09-17 14:26:01
- Tags: #read #deepdive #engineering

## TL;DR
GitHub 将 Copilot agent runtime 从 TypeScript/Node.js 重写为 Rust，产出超 80 万行代码，多由 AI 编写，分 128 个增量 PR 原子替换完成。一人数月完成原需团队一两年的工程，性能提升数个数量级，并通过 C ABI 与 napi 双入口支撑六个语言 SDK。

## Summary
GitHub 把 Copilot agent runtime 从 TypeScript/Node.js/V8 重写成了 Rust。最终规模超过 80 万行生产 Rust：832,378 行生产代码、468,689 行 Rust 单元测试，另有 174,675 行 TypeScript 端到端测试；六个语言 SDK 仓库还增加了约 13 万行 E2E 测试。大部分代码由 AI agent 编写，横跨 128 个合入 main 的 PR，并且不是最后一次性切换，而是边移植、边发布、边验证。结果是把原本可能要一个团队做一两年的项目，变成主要由一个开发者在几个月内完成，同时 runtime 性能提升了几个数量级。

这件事的起点是：Copilot agent runtime 不只支撑 Copilot CLI，还支撑 Copilot app、SDK、VS Code、Visual Studio、CCA、Copilot Code Review、Copilot Cowork、Copilot Studio，以及 Excel、Outlook、PowerPoint、Word 等越来越多产品。这些产品不想各自实现一套 agent loop，而是想共用同一个 runtime，把智能、安全、可靠性和性能集中维护。问题在于，原来的共享方式不理想。

原来的 CLI 逻辑上是“TUI + agent loop”，整套用 TypeScript、Node.js、V8、Ink、React 实现。对终端应用来说这很合理，但对要嵌入其他环境、要求快速启动和低内存占用的场景就不合理。更麻烦的是架构：TUI 和 runtime 交织，没有清晰分层；后来需要 SDK 时，又把 SDK 叠在 CLI 上，而不是反过来。于是 SDK 要工作时，会启动一个 headless CLI 子进程，通过 stdin/stdout 或 socket 走 JSON-RPC。每次 `new CopilotClient()` 都可能意味多起一个进程，加载 Node 和 V8，解析 JavaScript，生成字节码，承担 V8 内存开销，继承 Node 线程模型，所有事件和消息跨进程边界，崩溃还会带走会话。每个 SDK 消费者至少多背约 100 MB 工作集和两个要监督的进程。

所以目标很明确：runtime 要成为独立库，不再包含 TUI；TUI 和其他应用应该叠在它上面；它要依赖少、开销低、能进程内嵌入；性能、扩展性、可靠性要好；要适合 FFI，让 C#、TypeScript、Python、Rust、Go、Java 六个 SDK 都能用；工具链还要更现代、供应链风险更低。最终他们选 Rust。文章也强调，这不是说所有大型 TypeScript 都该转 Rust，而是他们的需求特别看重 C ABI 嵌入、低启动和稳态开销、可预测资源使用。代价是生命周期和共享状态必须显式表达，后来也出现了一些生命周期相关回归。

迁移策略是“原地、原子替换”，不是大爆炸，也不是长期维护 TS/Rust 两套 A/B 版本。每个 PR 把某个组件从 TypeScript 换成 Rust：保留一个薄薄的 TS shim 调 Rust，删掉旧实现，然后让现有 E2E 测试继续跑。这样 main 始终可发布，没人停工，改动可审查，回归能快速发现。文章认为 A/B 并行维护两版代码在这里不现实，因为代码库每周几百个 PR 快速演化，而且 session orchestration 这类子系统有可变状态、双向回调、贯穿几乎所有子系统，强行“跑两版对比”可能引入更多问题。有效移植单位往往不是“一个组件”，而是一波相关行为：先移纯逻辑，再移状态所有权，再移编排，再移除 fallback，最后简化 Rust。

数字上，最初估计 runtime 约 13 万行 TypeScript，但实际约有 43 万行生产 TypeScript 经过端口。期间 runtime 吸收约 30 万行生产 TypeScript、移除约 43 万行；进入约 120 万行生产 Rust、离开约 36.5 万行。所以图表上 TypeScript 行数一度看起来稳定甚至增加，其实隐藏了大量 churn。8 月 21 日，runtime 达到 100% 生产 Rust。14 个半星期内，main 发布了 135 个版本，其中 100 个预发布、35 个稳定版，平均每天约 1.3 个版本；端口 PR 也大约每天 1.3 个。预发布在 npm 样本中只占 10.5% 下载，说明初期暴露有限，问题更容易关联到近期改动并快速修复。

互操作分两层。第一层是临时的内部互操作：Rust 函数要被还没移植的 TypeScript 调用，Rust 也要回调 TypeScript，比如 hook、权限、模型推理。这里用 napi-rs，Rust 函数加 `#[napi]` 就能变成 JS 可调用函数，`async fn` 变 Promise，`#[napi(object)]` 变普通对象；反向则用 threadsafe functions，让 Rust Tokio 工作线程回到 Node 主线程调 JS。这个临时缝隙在 8 月 3 日达到峰值：2,019 个内部 N-API 导出、3,356 个 TypeScript 调用点；完成时归零。CLI 仍有少量直接访问 runtime 内部，但不算在这部分里，完全移到 SDK 公共面仍在进行。

第二层是永久的 SDK 面。六个语言 SDK 原本都通过启动 CLI 子进程、走 JSON-RPC 来访问 runtime。移植后，`runtime.node` 本质是普通平台共享库，`.dll`/`.so`/`.dylib` 加 Node 原生扩展约定。它现在有两个入口：napi 门给 Node 进程作为原生插件加载；C ABI 门给任何语言通过 FFI 在自己进程内加载。各语言分别用 P/Invoke、purego、JNA、cffi、libloading、koffi 选择进程内连接。C ABI 门非常小，只有 19 个导出函数：4 个服务器生命周期、4 个会话注册和配置、8 个连接、3 个嵌入式宿主。背后共享契约有 364 条 dispatch route，其中 340 条可由 SDK 消费者调用，24 条是 runtime 到 SDK 的回调。

有意思的是，进程内调用仍然保留 JSON-RPC。原因不是偷懒，而是让进程内托管变成 drop-in：每个 SDK 已有 JSON-RPC 客户端，包含分帧、请求响应关联、服务端到客户端处理器。把 FFI 当成底层另一种 transport，字节路径从 pipe/socket 变成函数调用，上层完全不用改。否则每个 API 方法都要加 typed C 函数，每个 SDK 都要第二套绑定，每新增方法要补六个绑定，ABI 还会变成要版本管理的二进制兼容面。保留 JSON-RPC 也方便真正远程的 runtime，无论是子进程还是 TCP。代价是进程内仍付序列化开销，但推理为主的工作负载里，相比模型往返通常不算大；未来也可以换 MessagePack 或给热路径加 typed export，而不影响现有导出。

AI 参与的数据也很能说明问题。整个移植会话日志有 12,760,995 个事件、31,247 条 user-role 消息、1,385,214 条 assistant 消息、6,438,562 个 hook 起止事件、1,857,409 次工具启动、23,096 次编译、19,485 次测试、2,496 次 rebase、7,410 次 commit、5,554 次 push、5,116 次压缩。31,247 条用户消息不都是作者亲手输入，包含技能指令、自动合并、跨会话和子代理流量；作者本人大概输入或说了 2,600 条，约十二分之一。工具调用 1,130,921 次，其中 61% 来自子代理。人类消息意图里，31% 集中在 review、测试和 CI，17.4% 是挑战技术或设计决策，15% 是推动完整性。作者的角色不是“派任务然后等”，而是操作控制回路：检查结果、质疑设计、执行质量门、在 agent 把中间停点当终点时继续推。

整体理解：这不是简单的“用 AI 写代码重写项目”，而是一个大型系统迁移工程案例。成功关键包括：先明确架构边界，把 TUI 和 runtime 分开；把 runtime 做成可嵌入的 Rust 库；用 C ABI 和 napi 双入口适配多语言；用增量原子替换保持 main 可发布；用完整 E2E 测试和预发布验证控制风险；临时互操作层明确可删；人类负责判断、审查和质量控制。AI agent 承担了海量机械但需要上下文的移植工作，但人类仍在控制循环里。性能、内存、启动和部署形态都因此改善，同时也有代价：生命周期和共享状态更显式，进程内托管目前仍是 opt-in，JSON-RPC 开销仍在，CLI 完全走 SDK 公共面也还没完成。
