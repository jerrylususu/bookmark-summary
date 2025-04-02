# A steam locomotive from 1993 broke my yarn test
- URL: https://blog.cloudflare.com/yarn-test-suffers-strange-derailment/
- Added At: 2025-04-02 14:52:04
- [Link To Text](2025-04-02-a-steam-locomotive-from-1993-broke-my-yarn-test_raw.md)

## TL;DR


作者在运行Jest测试时遭遇27秒定时崩溃问题，排查发现是jest-changed-files插件误将系统命令`sl`（蒸汽火车动画）识别为Git检测工具，导致进程被劫持。通过重命名`sl`命令或升级Jest补丁解决，事件凸显开源生态中的罕见命名冲突风险，以及系统级调试工具的重要性。

## Summary


该文章讲述了作者在使用 `yarn test` 运行 Jest 测试时遇到的神秘问题及排查过程：

### 问题现象
1. **首次失败**：作者首次运行 `yarn test` 时，测试卡顿并报错 `[Error]`，无明确提示。
2. **排查无果**：尝试 `--verbose`、`--debug`、`--no-cache` 等参数无效，Jest 文档和社区搜索均无有效解决方案。
3. **规律发现**：测试在固定 27 秒后崩溃，无论选择多少测试用例，均触发相同错误。

### 关键排查步骤
1. **系统调用跟踪**：使用 `strace` 发现 Jest 频繁调用 `sl` 命令（该命令于1993年开发，用于模拟蒸汽火车动画）。
2. **命名冲突**：Jest 的 `jest-changed-files` 插件误将 `sl` 解析为 `sl`（Steam Locomotive）而非预期的 `sl`（Sapling CLI），导致测试进程被蒸汽火车模拟程序劫持。
3. **时间谜团**：蒸汽火车动画在终端执行时间与终端宽度相关，总执行时间约为 4 波次（每波约 6-7 秒），总和接近 27 秒。

### 解决方案
- **临时修复**：重命名或删除 `sl` 命令（路径通常为 `/usr/games/sl`），使 Jest 调用路径正常。
- **长期补丁**：Jest 官方发布补丁（PR #15053）以避免命名冲突，社区以幽默方式传播事件相关新闻。

### 背后原因
- **根因定位**：Jest 的 `jest-changed-files` 插件试图通过 `sl root` 检测 Git 仓库状态，但误触发了蒸汽火车模拟程序。
- **环境差异**：作者使用 Linux，该系统默认安装 `sl`；同事的 macOS 未安装此命令，因此未复现问题。

### 彩蛋细节
- **蒸汽火车执行逻辑**：Jest 调用 `sl` 的次数与项目配置的 `rootDirs` 数量相关，在 16 个仓库目录中分批执行。
- **社区反应**：开发人员在 issue 中调侃蒸汽火车事故，相关 meme（如火车撞毁 Jest 视觉图）广泛传播。

### 结语
该事件最终归因于罕见的命令命名冲突，揭示了开源生态中的偶然性问题，同时展示了系统级调试工具（如 `strace`）的重要性。
