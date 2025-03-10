# The 70% problem: Hard truths about AI-assisted coding
- URL: https://addyo.substack.com/p/the-70-problem-hard-truths-about
- Added At: 2025-01-04 05:07:47
- [Link To Text](2025-01-04-the-70%-problem-hard-truths-about-ai-assisted-coding_raw.md)

## TL;DR
AI辅助开发显著提升了生产力，但软件质量未显著改善。高级工程师通过AI加速已知任务和原型设计，而初级工程师则面临代码质量低和学习障碍的问题。AI工具的最佳用途是作为经验丰富开发者的原型加速器和学习辅助工具。未来，AI将具备更高的自主性和多模态能力，但创建高质量软件仍需人类的同理心和工程纪律。AI的真正价值在于加速迭代和实验，而非替代良好的软件实践。

## Summary
1. **AI辅助开发的现状**：
   - 工程师报告称使用AI后生产力显著提高，但日常使用的软件质量并未显著提升。
   - 作者认为这揭示了软件开发中的一些基本事实。

2. **AI辅助开发的两种模式**：
   - **Bootstrappers**：
     - 使用AI工具（如Bolt、v0、screenshot-to-code AI）快速启动新项目。
     - 从设计或粗略概念开始，生成完整的初始代码库。
     - 在几小时或几天内获得可工作的原型，而不是几周。
     - 专注于快速验证和迭代。
   - **Iterators**：
     - 使用AI工具（如Cursor、Cline、Copilot、WindSurf）进行日常开发。
     - 用于代码补全、复杂重构任务、生成测试和文档。
     - 将AI作为“结对编程”工具进行问题解决。

3. **AI辅助开发的隐藏成本**：
   - 高级工程师使用AI工具时，会不断重构生成的代码，添加边缘情况处理，强化类型定义和接口，质疑架构决策，并添加全面的错误处理。
   - 初级工程师更容易接受AI的输出，导致代码质量不高，形成“纸牌屋代码”。

4. **知识悖论**：
   - 高级工程师使用AI加速已知任务，而初级工程师试图用AI学习如何完成任务，结果差异显著。
   - 高级工程师使用AI快速原型化已知想法，生成基本实现并加以完善，探索已知问题的替代方法，自动化常规编码任务。
   - 初级工程师往往接受错误或过时的解决方案，忽视关键的安全和性能考虑，难以调试AI生成的代码，构建脆弱的系统。

5. **70%问题**：
   - 非工程师使用AI进行编码时，可以快速完成70%的工作，但最后的30%变得非常困难。
   - 修复一个小错误可能导致更多问题，形成恶性循环。
   - 缺乏编程背景的人难以理解代码的底层原理，导致依赖AI修复问题，而不是自己解决问题。

6. **AI辅助开发的学习障碍**：
   - AI工具的可访问性可能阻碍学习，因为代码“凭空出现”而不需要理解底层原理。
   - 用户无法发展调试技能，错过学习基本模式，难以推理架构决策，难以维护和演进代码。

7. **成功使用AI工具的非工程师**：
   - 使用AI进行快速原型设计。
   - 花时间理解生成的代码。
   - 在AI使用过程中学习基本编程概念。
   - 逐步建立知识基础。
   - 将AI作为学习工具，而不仅仅是代码生成器。

8. **AI工具的最佳用途**：
   - 作为经验丰富的开发人员的原型加速器。
   - 作为致力于理解开发的学习辅助工具。
   - 作为快速验证想法的MVP生成器。

9. **AI辅助开发的实用建议**：
   - 让AI生成基本实现，手动审查和重构模块化。
   - 添加全面的错误处理，编写彻底的测试，记录关键决策。
   - 为每个任务启动新的AI对话，保持上下文集中和最小化，频繁审查和提交更改，保持紧密的反馈循环。
   - 使用AI进行初始代码生成，手动审查所有关键路径，自动化测试边缘情况，定期进行安全审计。

10. **AI在软件开发中的角色**：
    - **加速已知任务**：AI擅长帮助实现已知模式。
    - **探索可能性**：AI适合快速原型设计和探索不同方法。
    - **自动化常规任务**：AI显著减少样板和常规编码任务的时间。

11. **AI辅助开发的未来**：
    - **代理式软件工程**：未来的AI工具将能够计划、执行和迭代解决方案，具有更高的自主性。
    - **多模态能力**：未来的工具将整合视觉理解、语言对话和环境交互，能够像人类一样全面理解和工作。

12. **AI与开发者的协作**：
    - 最有效的团队将学会为AI代理设定明确的边界和指导方针，建立强大的架构模式，创建有效的反馈循环，保持人类监督的同时利用AI的自主性。

13. **软件开发的艺术**：
    - AI工具可能使快速构建软件变得容易，但创建真正精致、消费者质量的体验仍然需要人类的同理心、经验和对工艺的深刻关注。
    - 未来的软件产品将是由那些注重细节、关注用户体验、为边缘情况构建、创造真正自助体验的开发人员构建的。

14. **总结**：
    - AI并没有显著提高软件质量，因为软件质量的主要限制因素从来不是编码速度。
    - AI的真正价值在于让我们更快地迭代和实验，通过更快速的探索可能带来更好的解决方案。
    - 关键在于保持工程纪律，将AI作为工具，而不是替代良好的软件实践。
