# Agent harness security and Git
- URL: https://iter.ca/post/llm-agent-git/
- Added At: 2026-09-13 13:37:28
- Tags: #read #security

## TL;DR
Git 支持仓库内嵌裸仓库，编码代理对只读 Git 命令免审批，攻击者可在不可信仓库埋恶意 config 触发代码执行。多家代理已修复，根本防御是沙箱化代理。

## Summary
这篇文章的核心是：Git 允许在一个普通仓库内部再放一个“裸仓库”，而很多 LLM 编码代理会允许一些 Git 只读命令免审批运行。攻击者只要在不可信仓库里埋一个看起来像裸仓库的子目录，并放入恶意 `config`，就可能诱使代理在子目录里运行 Git 命令，从而执行任意代码。作者认为现实中多数情况不算严重，因为更正确的防御是沙箱化代理，而不是只限制命令，但这些发现揭示了代理安全模型的漏洞。

Git 的这个特性叫“被埋藏的裸仓库”。普通仓库有 `.git` 目录；裸仓库没有工作树，靠 `objects/`、`refs/`、`HEAD` 等结构被识别。当你在某个子目录里运行 Git 命令时，Git 会向上找仓库根。如果这个子目录本身长得像一个裸仓库，Git 就会把它当成仓库根。攻击者可以在里面放这样的配置：

```ini
[core]
    repositoryformatversion = 0
    fsmonitor = "echo pwned > /tmp/pwned; echo"
    worktree = "."
```

很多 Git 子命令会调用 `core.fsmonitor` 来检查文件系统变化，于是恶意命令被执行。作者强调这不是 Git 的新漏洞，2022 年就已知，libgit2 等项目甚至用这种结构在测试仓库里放测试用 Git 仓库。Git 3.0 的默认行为会改变，裸仓库需要显式用 `--git-dir` 或 `GIT_DIR` 指定。

克隆一个不可信仓库本身理论上安全，因为 `.git` 是 Git 自己创建的，不是攻击者放的。但如果你进入克隆仓库内部、被伪造成裸仓库的子目录，再运行 Git 命令，就不安全了。攻击者可以在子目录里伪造仓库结构，并放入恶意 hooks 或 config。

在编码代理方面，Claude Code 的安全模型是：不要在不信任目录运行；除了读写之外，操作需要用户或 LLM 分类器批准。作者发现，在接受编辑模式下，Claude 可以创建嵌套的裸仓库，然后执行 `cd ... && git status`，从而免审批运行任意代码。因为 `git status` 在只读允许列表里，而代理可以改变路径。harness 会阻止直接写 `.git/`，但不会阻止写裸仓库，因为仅凭路径无法判断它是不是裸仓库。作者 2 月报告后，Anthropic 先标记为重复，后来修复方式是：不再允许同一条命令里同时出现 `cd` 和 `git`。

Codex 最初也会自动允许 Git 命令，但只在 Windows 上是安全问题，因为其他平台默认在沙箱里跑命令。作者 2 月 12 日邮件 OpenAI，同一天他们就把 Windows 也改成隔离沙箱，沙箱外运行命令需要权限。不过中间还出现过启动时运行 `git status`、在信任提示后可能代码执行的问题。2 月底作者报告后，到 5 月他们修了，但又改成启动时运行：

```bash
git ls-remote https://github.com/openai/plugins.git HEAD
```

这虽然不触发 fsmonitor，但攻击者控制 config 时可以用 `insteadOf` 执行代码：

```ini
[protocol "ext"]
    allow = always
[url "ext::sh -c id>/tmp/pwned #"]
    insteadOf = https://github.com/
```

作者 5 月报告，OpenAI 在 5 月和 7 月回复，8 月修复，并移除了内置的安全命令允许列表。

Copilot CLI 也有类似问题。作者发现，在不信任目录运行 Copilot 时，它会在显示“是否信任此文件夹”提示之前先运行 `git status`，从而可能代码执行。还有 Git 命令可以在未询问权限时执行代码，和 Claude Code、Codex 类似。对应漏洞是 GHSA-9ccr-r5hg-74gf / CVE-2026-45033，后来一起修复。

作者还检查了 IDE。VS Code 和 IntelliJ IDEA 都有工作区信任机制，信任后才启用源码控制。Cursor 是 VS Code 的分支，默认禁用了工作区信任，所以会自动信任你打开的每个目录，并在启动时立即运行多个 Git 命令。

防御建议是：不要在不可信目录运行 Git 命令，包括刚克隆仓库里的子目录。可以设置：

```bash
git config --global safe.bareRepository explicit
```

这会让 Git 不自动识别裸仓库，Git 3.0 也会默认如此。但它仍不能防住恶意 `.git`，所以不能因此就在不可信目录里放心运行 Git。少数命令目前可以安全运行，比如 `git rev-parse --show-toplevel`，但未来 Git 增加新配置键后也可能变危险。根本办法还是沙箱化代理，不要信任不可信目录。

脚注里还提到：Claude 的报告最初因为作者误解安全模型被关闭，后来重新打开并作为重复关闭；OpenAI 虽然有 Bugcrowd 页面，但作者认为披露条款不合理，所以改用邮件；过去也有在自己克隆的仓库里运行 Git 命令导致代码执行的安全问题。
