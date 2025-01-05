# Mistakes engineers make in large established codebases
- URL: https://www.seangoedecke.com/large-established-codebases/
- Added At: 2025-01-04 11:09:14
- [Link To Text](2025-01-04-mistakes-engineers-make-in-large-established-codebases_raw.md)

## TL;DR
大型代码库的维护面临诸多挑战，如学习难度高、一致性要求严格等。一致性是避免问题、便于未来改进的关键。工程师需理解服务使用情况、依赖管理和测试限制，并谨慎处理代码移除。大型代码库通常产生公司主要价值，值得投入精力维护。在开发新功能时，必须研究现有实践并遵循模式，同时依赖监控和防御性编程来捕捉错误。

## Summary
1. **大型代码库的挑战**：
   - **定义**：大型代码库通常包含数百万行代码，由数百名工程师共同维护，且代码库的初始版本至少有十年历史。
   - **学习难度**：无法通过开源项目或个人项目提前练习，因为这些项目通常规模较小且从头开始。

2. **核心错误：不一致性**：
   - **常见错误**：工程师倾向于在自己的功能实现中忽略代码库的其余部分，以保持代码的整洁。
   - **重要性**：一致性可以避免意外问题，减缓代码库的混乱进程，并允许利用未来的改进。
   - **实例**：在实现API端点时，应遵循现有代码库中的认证模式，即使这些模式看起来不理想。

3. **一致性的好处**：
   - **避免地雷**：现有功能代表了一条安全的路径，遵循这些路径可以避免未知的代码库特性。
   - **长期维护**：一致性使得未来的改进变得可能，而不一致的代码库则使得通用改进变得困难。

4. **其他重要考虑**：
   - **理解服务使用情况**：了解哪些端点最常被访问，哪些是关键端点，以及服务的延迟要求。
   - **测试限制**：在大型项目中，无法测试所有状态组合，必须依赖关键路径测试、防御性编程和监控。
   - **依赖管理**：非常不情愿地引入新依赖，因为它们会带来长期的安全漏洞和包更新成本。
   - **代码移除**：有机会时移除代码，但要非常小心，确保在生产中调用者为零。
   - **小规模PR**：在大型项目中，小规模的PR和提前影响其他团队代码的更改至关重要。

5. **为何要处理大型代码库**：
   - **价值产生**：大型代码库通常产生公司90%的价值，是支付工程师工资的主要来源。
   - **理解必要性**：在拆分大型代码库之前，必须首先理解它，因为无法从第一原则重新设计一个非平凡的项目。

6. **总结**：
   - **重要性**：大型代码库值得投入，因为它们通常支付你的工资。
   - **一致性**：一致性是最重要的。
   - **研究先行**：在开始新功能之前，必须研究代码库中的现有实践。
   - **遵循模式**：如果不遵循现有模式，必须有充分的理由。
   - **生产足迹**：理解代码库的生产足迹。
   - **测试策略**：不要期望能测试所有情况，依赖监控。
   - **代码移除**：有机会时移除代码，但要非常小心。
   - **错误捕捉**：使领域专家尽可能容易地捕捉到你的错误。