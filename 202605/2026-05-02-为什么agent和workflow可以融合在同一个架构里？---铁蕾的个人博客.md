# 为什么agent和workflow可以融合在同一个架构里？ - 铁蕾的个人博客
- URL: https://zhangtielei.com/posts/blog-amphiflow_implementation.html
- Added At: 2026-05-02 05:14:24
- Tags: #read #agent

## TL;DR
AmphiLoop 架构融合 workflow 与 agent，通过“观察-思考-行动”循环实现模式切换：默认稳定运行 workflow，遇障自动切换至 agent 灵活应对，兼具稳定性与适应性，适用于复杂 AI 场景。

## Summary
AmphiLoop 架构通过“决策与执行解耦”和统一的“观察-思考-行动”循环，将 workflow 和 agent 融合为 amphiflow 模式。  
- **工作方式**：默认以 workflow 模式运行，稳定且节省资源；遇到意外障碍时自动切换到 agent 模式，通过小降级（修复当前步骤）或大降级（重新规划路径）应对异常。  
- **实现原理**：  
  1. **统一循环**：两种模式共享观察与行动步骤，但思考过程独立——workflow 通过生成器产生决策，agent 由 LLM 生成决策。  
  2. **决策解耦**：workflow 的决策通过 Python `yield` 语法延迟执行，形成动态程序；agent 的决策则依赖 LLM。  
  3. **模式切换**：基于错误检测机制，在 workflow 失败时触发 agent 模式，修复后可返回 workflow 继续执行。  
- **优势**：结合 workflow 的稳定性与 agent 的灵活性，解决 AI 应用不可控、高 token 消耗等问题，适用于复杂场景。
