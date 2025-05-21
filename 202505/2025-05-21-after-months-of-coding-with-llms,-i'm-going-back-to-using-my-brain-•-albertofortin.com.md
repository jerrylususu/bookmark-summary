# After months of coding with LLMs, I'm going back to using my brain • albertofortin.com
- URL: https://albertofortin.com/writing/coding-with-ai
- Added At: 2025-05-21 14:37:53
- [Link To Text](2025-05-21-after-months-of-coding-with-llms,-i'm-going-back-to-using-my-brain-•-albertofortin.com_raw.md)

## TL;DR


作者尝试全程依赖AI开发SaaS项目，虽初期高效但代码质量差，暴露出AI协作局限。后转手动重写核心代码并限制AI在简单任务的作用，恢复项目控制。指出AI存在逻辑混乱、不稳定等缺陷，不宜盲目依赖，尤其复杂逻辑或硬件结合场景易失效，强调技术探索需审慎。

## Summary


作者在为自己的SaaS项目开发新基础设施时，尝试完全依赖LLM（如Claude）与工具（如Cursor Notepads）完成从架构设计到编码的全流程。初期通过AI生成Go+Clickhouse方案，以“产品经理”角色高效推进，但代码质量逐渐暴露问题：重复冗余的文件、命名不一致、逻辑混乱，如同10名未协作的开发者独立编写。尽管提供充足上下文和使用大模型，AI仍无法保证代码结构与一致性。

反思阶段，作者意识到过度依赖AI导致自身编码能力退化，丧失对项目的完整掌控。改用“程序员主导+AI辅助”模式：手动重写关键代码、学习Go/Clickhouse最佳实践、限制AI用于简单任务（如变量重命名），恢复清晰的调试与架构规划能力。作者担忧AI使技术人员依赖工具而弱化核心技能，尤其对非程序员而言，“无脑调用AI编码”易引发灾难性后果。他强调当前AI工具存在明显局限，如处理复杂查询或与硬件限制结合时的失效，认为对新兴技术需保持审慎态度，避免被不切实际的宣传误导。同时指出AI工具体验的不稳定性（同模型/提示下结果常矛盾），质疑背后是否存在资源限制或算法缺陷。
