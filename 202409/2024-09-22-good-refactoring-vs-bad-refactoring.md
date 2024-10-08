# Good Refactoring vs Bad Refactoring
- URL: https://www.builder.io/blog/good-vs-bad-refactoring
- Added At: 2024-09-22 09:58:47
- [Link To Text](2024-09-22-good-refactoring-vs-bad-refactoring_raw.md)

## TL;DR
文章讨论了重构代码的常见错误，如大幅度改变编码风格、不必要的抽象、增加不一致性等，强调了理解代码和业务背景的重要性，以避免引入不必要的复杂性和不一致性。

## Summary
1. **引言**：
   - 作者多年雇佣了许多开发者，其中不少人认为代码需要大量重构。
   - 几乎每次重构后的代码都被其他开发者认为更难理解和维护，且通常更慢、更多bug。
   - 重构本身不是坏事，但糟糕的重构确实有害，且很容易在试图改进时反而使情况恶化。

2. **好重构与坏重构的区别**：
   - **抽象的正确应用**：
     - 抽象可以是好的，也可以是坏的，关键在于何时以及如何应用它们。
     - 常见的陷阱包括过度抽象和在不理解代码的情况下进行重构。

3. **常见错误**：
   - **1. 大幅度改变编码风格**：
     - 常见错误是开发者在重构时完全改变编码风格。
     - 例子：从命令式风格改为函数式风格，引入新库（如Ramda），导致团队不熟悉，维护困难。
     - 好的重构：使用更惯用的JavaScript方法（如`filter`和`map`），保持代码简洁易读。

   - **2. 不必要的抽象**：
     - 例子：引入不必要的类和方法，增加复杂性。
     - 好的重构：将逻辑分解为小而可重用的函数，避免不必要的复杂性。

   - **3. 增加不一致性**：
     - 例子：在React应用中，一个组件使用Redux Toolkit，而其他组件使用React Query，导致不一致。
     - 好的重构：保持一致性，使用React Query进行数据获取。

   - **4. 不理解代码就重构**：
     - 例子：移除重要的缓存机制，导致性能下降。
     - 好的重构：保持缓存行为，使用更高级的缓存管理器。

   - **5. 不了解业务背景**：
     - 例子：为依赖SEO的电商网站构建单页应用，导致SEO问题。
     - 好的重构：使用Next.js进行服务器端渲染，提升SEO效果。

   - **6. 过度整合代码**：
     - 例子：将所有Firebase函数的设置统一，无法为不同函数设置不同配置。
     - 好的重构：允许每个API传递不同的Firebase选项。

4. **总结**：
   - 重构时需谨慎，避免引入不必要的复杂性和不一致性。
   - 理解代码和业务背景是成功重构的关键。
