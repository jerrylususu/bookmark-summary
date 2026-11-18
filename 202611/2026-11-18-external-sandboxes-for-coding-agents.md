# External sandboxes for coding agents
- URL: https://blog.primeradiant.com/external-sandboxes-for-coding-agents/
- Added At: 2026-11-18 15:13:21
- Tags: #read #agent

## TL;DR
文章介绍“外部沙箱”：代理留在主机，命令和文件操作转入独立Linux沙箱，仅见挂载目录、默认断网，经白名单代理联网并可替换凭证；给出三种原型和Claude Code、Codex、Pi接入，强调尚属实验。

## Summary
文章介绍了一种叫“外部沙箱”（external sandboxes）的模式：编码代理仍然运行在你的电脑上，但它执行的命令和文件操作会被转发到一个独立的 Linux 沙箱里执行。沙箱默认只能看到你显式挂载的目录，默认不能联网；需要联网时，通过一个带 allow-list 的 HTTP/HTTPS 代理放行，并且可以在代理层做凭证替换，让代理看不到真实 API key。

作者先解释动机。编码代理会犯错，而它能读写的东西都可能被破坏或泄露。理想情况是让代理在安全环境里工作，现实却是很多人给代理整台电脑和完整网络的权限，然后祈祷不出事。逐条手动批准每个动作也不可行：太慢，而且很快会导致“决策疲劳”，人开始不假思索地全部批准。Claude Code 的 auto mode 和 Codex 的 auto-review 用额外 AI 判断来帮忙，但仍然依赖模型判断；沙箱则是不依赖任何模型判断的硬边界。作者尤其担心较弱或本地运行的模型，它们更容易出错，也更容易被提示注入攻击。因此目标是：稳健、可信、易用，让代理只能读写选定文件、只能发起允许的网络请求。

架构上有两种做法：一是让代理本身跑在沙箱里，比如 Fly 的 Sprites；二是代理在沙箱外，把命令发给独立的沙箱。作者选择第二种，因为这样可以避免代理修改自身或其直接环境，沙箱边界更清晰、更容易审计。“外部”是相对代理而言，不是相对电脑而言：代理和沙箱可以跑在同一台机器上。

他们做了三个可互操作的原型。`external-sandbox-v86` 是一个 Node.js 进程，用 WebAssembly 版的 v86 模拟 x86，运行 Alpine Linux，npm 包里直接带了完整的 Linux 发行版；`external-sandbox-container` 用 Python 包装 Apple Containers 跑 Linux 容器；`external-sandbox-quicksand` 用 Python 和微软的 Quicksand 跑完整 QEMU 虚拟机，QEMU 和 Alpine 镜像以 Python wheel 形式提供。三者实现同一套 localhost Web API 和协议，默认端口分别是 8686、8687、8688，可以同时运行。他们还发布了协议规范和一一致性测试工具，方便别人基于其他技术实现兼容沙箱。

最简单的试用只需要两条命令。第一条在项目目录启动沙箱，把当前目录以读写方式挂载，并用 `--preserve-paths` 保留宿主机路径，让命令里出现的原路径在沙箱内也能用：

```bash
npx --yes external-sandbox-v86 \
  --preserve-paths --mount-rw "project=$PWD"
```

需要 Node.js 22.19 以上。第二条在另一个终端启动 Pi 代理，加载 `external-sandbox-pi` 扩展，禁用内置工具，并指向沙箱：

```bash
npx --yes @earendil-works/pi-coding-agent \
  -e npm:external-sandbox-pi --no-builtin-tools \
  --sandbox-url http://127.0.0.1:8686
```

在 Pi 里执行 `!uname -a`，输出是 Alpine Linux 内核，而不是 macOS，说明命令确实进了沙箱。代理可以执行命令、读写项目文件夹，但碰不到机器上的其他内容。

这套方案带来的保障包括：代理留在 Mac 上；沙箱只看到挂载的文件夹，且可控制只读或读写；默认没有外网；开启 `--proxy` 后只能访问 allow-list 里的主机；代理层可以做凭证替换；沙箱自带 Web UI，提供浏览器终端、修改网络规则和查看请求日志；因为协议统一，任何代理都可以配任何沙箱。

不同代理的接入方式不同，这是文章的技术重点之一。

Claude Code 使用 `CLAUDE_CODE_SHELL_PREFIX` 环境变量。设置后，Claude 的 Bash 工具会在每条命令前加上这个前缀，实际变成调用一个脚本，脚本再把完整 shell 字符串送进沙箱。需要额外设置 `CLAUDE_CODE_SHELL`、`CLAUDE_CODE_TMPDIR`（必须位于可写挂载内）和 `EXTERNAL_SANDBOX_API_URL`。文章特别提醒：Claude Code 原生的 Read 和 Edit 工具仍然在宿主机上运行，不在沙箱里。挂载规则只能限制它的 Bash 命令，Claude 仍可以直接读写 Mac 上的文件。这是使用 Claude Code 时需要注意的边界。

Codex 使用 `codex exec-server` 机制，这是一个用于启动和控制子进程的小型 JSON-RPC 服务器。通过专用的 `CODEX_HOME` 和 `environments.toml`，把 Codex 指向沙箱的 `/codex` WebSocket 端点。启动时用 `--sandbox danger-full-access` 告诉 Codex 不要再套一层自己的沙箱，并关闭 `shell_snapshot` 和 `unified_exec_tty`。作者说明 exec-server 协议还是实验性的，他们用 Codex CLI 0.164.0 测试过，其他版本可能需要检查。

Pi 使用扩展机制。`external-sandbox-pi` 把 Pi 的 `bash`、`read`、`write`、`edit`、`grep`、`find`、`ls` 工具替换成对沙箱操作的版本，`grep` 和 `find` 依赖沙箱里的 ripgrep，三个默认镜像都带。它还把 Pi 的 `!command` 和 `!!command` 快捷键配置为在沙箱内执行。`--no-builtin-tools` 的作用是：即使扩展加载失败，Pi 也没有能在你电脑上运行的工具，工具会报错而不是回退到主机执行。可以安装扩展并设置 `EXTERNAL_SANDBOX_API_URL`，让 Pi 默认连沙箱。

网络控制是安全模型的核心。默认完全无外网，目的是防止 bug 或提示注入把私有数据泄露出去，也就是 Simon Willison 说的“致命三要素”：私有数据、不可信内容、外发通道同时存在时风险很大。开启代理后，沙箱内会设置 `HTTP_PROXY` 和 `HTTPS_PROXY`，并提供代理的 CA 证书，设置 `SSL_CERT_FILE`、`REQUESTS_CA_BUNDLE`、`NODE_EXTRA_CA_CERTS` 等变量，让代理能检查并过滤 TLS 流量；不遵守这些设置、试图直连的代码仍然会被阻断。

`--proxy-config` 指向一个 JSON 文件，指定允许的 origin 和 HTTP 方法。文章给出 GitHub API 的例子：允许 `https://api.github.com` 的 GET，并配置 `credential` 块，把 `authorization` 头里的占位符 `Bearer placeholder-github-token` 替换成宿主机环境变量 `GITHUB_TOKEN` 的真实值；`guestEnv` 则让沙箱内代码拿到占位符。这样代理可以调用需要认证的 API，但真实密钥不会进入沙箱，也不会被代理看到。作者提醒：被允许的主机仍可能在响应里回显凭证，所以只对信任的服务使用凭证规则，并尽量收窄方法和路径。Web UI 的 `/proxy` 页面可以在会话运行中修改策略、查看允许和拒绝的请求日志；只有启动时加了 `--proxy` 或 `--proxy-config` 才能访问这个页面。

最后是限制和提醒。这些沙箱仍是实验性原型，没有经过足以放心处理敏感工作负载的审计。读写挂载仍然允许代理破坏该文件夹里的任何东西，所以应放在版本控制下，能只读就只读。沙箱运行 Linux，macOS 上构建的依赖，比如项目里的 `node_modules` 或 `.venv`，可能需要在沙箱内重新安装。三个沙箱配三个代理的组合说明协议可以混搭模型、代理和沙箱平台；如果想基于其他技术做沙箱，可以从协议规范和一一致性测试工具开始。
