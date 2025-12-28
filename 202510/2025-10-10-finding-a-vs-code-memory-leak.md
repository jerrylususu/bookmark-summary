# Finding a VS Code Memory Leak
- URL: https://randomascii.wordpress.com/2025/10/09/finding-a-vs-code-memory-leak/
- Added At: 2025-10-10 14:05:11

## TL;DR
作者Bruce Dawson通过观察同事电脑的高进程ID，发现VS Code因未关闭进程句柄导致内存泄漏。问题源于代码中忘记调用`CloseHandle`。经ETW分析后迅速修复，凸显资源管理和RAII重要性。

## Summary
本文讲述了作者Bruce Dawson发现Visual Studio Code（VS Code）中一个严重内存泄漏的过程和细节。尽管作者从未使用过VS Code，且泄漏在任务管理器中不可见，但通过观察同事电脑上的异常高进程ID（PID），他推断出存在进程句柄泄漏。

**关键发现过程：**
- 作者在2021年疫情期间通过远程协助注意到同事系统上的PID达到七位数（约400万），远高于正常水平（通常为四位数），暗示可能有数百万个进程句柄未被释放。
- 经分析，泄漏原因是Windows系统中，如果进程句柄未被关闭，即使进程结束，其PID也不会被重用，导致PID数值不断累积。
- 使用任务管理器确认VS Code进程泄漏句柄，并通过ETW（Event Tracing for Windows）追踪到具体代码：一个名为`GetProcessMemoryUsage`的函数中调用了`OpenProcess`但未调用`CloseHandle`，每次泄漏约64 KB内存。
- 泄漏代码示例显示，缺失的`CloseHandle(hProcess)`是根本原因，修复后只需添加一行代码即可解决问题。

**影响与修复：**
- 泄漏可导致内存消耗无上限，首次发现时已达64 GB，可能耗尽高端机器内存。
- 作者通过Twitter报告后，他人提交GitHub issue，问题在几天内被修复。
- 作者建议开发人员关注任务管理器中的句柄数，并提倡使用RAII（资源获取即初始化）等编程实践避免类似错误。
- 文末还讨论了设置资源限制（如句柄或内存上限）以自动检测泄漏的想法，但认为现实中难以实现。

**评论互动：**
- 读者分享了类似经历，强调RAII和静态分析的重要性，ChatGPT也能识别此类错误。
- 作者提供了工具链接（如FindZombieHandles）帮助诊断句柄泄漏，并讨论了PID异常的调查方法。

整体上，案例展示了通过细致观察和系统工具快速定位隐蔽错误的过程，突显了编程中资源管理的关键性。
