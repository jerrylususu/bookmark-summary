# Building a software factory for AI SDK
- URL: https://vercel.com/blog/building-a-software-factory-for-ai-sdk
- Added At: 2026-08-24 14:46:44
- Tags: #read #agent

## TL;DR
Vercel团队为AI SDK构建“软件工厂”，用多个专职agent自动处理issue和PR，运行于隔离沙箱，人类保留最终审批。四周后，工厂贡献25-35%合并PR，关闭超75% issues，积压大幅下降，验证了以人为核心的自动化维护模式。

## Summary
Vercel 团队为 AI SDK 这个高人气开源项目构建了一个“软件工厂”，用来应对 issues 和 PR 的积压问题。AI SDK 每周 npm 下载量超过 2000 万，仓库有 26000 多星，但维护者要同时跟进模型提供商、UI 框架、沙箱执行环境和 agent 适配器四条线。到 6 月底，积压了 1000 多个 open issues 和近 800 个 PR，纯靠人力已经无法消化。

他们选择构建软件工厂，而不是单纯增加 agent。原因是现有的 agent 方案虽然能辅助，但每个改动最终还是需要人类注意力来把关，而人类责任是 agentic 工程信任的核心。工厂的目标是自动化围绕人类的生命周期，而不是移除人类。

在设计自动化程度时，他们强调 AI SDK 是基础性 AI 基础设施，质量与安全不可妥协，因此工厂必须让人类保留对发布内容的控制权，并根据风险调整评审深度：文档修复快速扫一眼，定义清晰的 provider 变更做针对性验证，新的公共 API 则深度审查。

他们构建的 `ai-sdk-factory` 是一个自主处理 incoming issues 和 pull requests 的系统。工厂内有多个专职 agent，分别负责：bug 复现、bug 修复、PR 评审、backport、文档更新、特性分析、特性实现。每个 agent 只做一件事，便于测试、调试和维护。安全方面，所有 agent 都运行在隔离的 Vercel Sandbox 中，只拥有任务所需的最小权限，并屏蔽恶意网络路径，最后一层防线是人类审批。开发过程先在本地 CLI 迭代，成熟后迁移到云端，使用 Vercel Functions、Queues、Blob、Sandbox 和 Neon Postgres。

以 issue #17898（请求 OpenAI web search 支持 blocked domains）为例，工厂流程如下：分类 agent 识别为 Feature 并给出理由；分析 agent 生成探针程序确认功能缺失，并写出规格说明；实现 agent 根据规格实现代码、跑端到端测试验证，并提交 PR；自动评审 agent 评估风险并批准；人类维护者 Lars 阅读证据链、审查代码后合并；随后工厂自动为 v5 和 v6 版本创建 backport PR，其中 v5 遇到冲突时 agent 标注并修复后再次提交，最终由人类合并。

运行四周后的成果：每周合并的 PR 中 25-35% 由工厂 agent 编写；backport PR 占 v6 和 v5 每周合并的一半以上；7 月关闭的 issues 中超过 75% 由工厂关闭；open issues 从 1022 降至 844，open bugs 减少约 25%。

工厂的持续改进方式是把每次运行结果分为四类：成功、有缺陷、受阻塞、手动。只有成功会发布，其他都作为反馈改进 prompts、上下文、eval 用例或补足环境。随着每次修复，自动化边界不断扩大。最后作者认为，在 agent 定义软件开发生命周期的世界里，改进工厂本身将成为标准的工程工作。
