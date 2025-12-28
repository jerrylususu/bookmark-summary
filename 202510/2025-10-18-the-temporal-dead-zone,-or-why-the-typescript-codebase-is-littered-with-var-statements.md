# The Temporal Dead Zone, or why the TypeScript codebase is littered with var statements
- URL: https://vincentrolfs.dev/blog/ts-var
- Added At: 2025-10-18 15:30:26

## TL;DR
TypeScript代码库为优化约8%性能，选择使用存在缺陷的`var`语句替代`let`/`const`，以规避变量时空死区带来的运行时开销。尽管现代JavaScript推荐使用更安全的块级作用域声明，但出于性能权衡仍保留`var`。

## Summary
文章主要讨论了 TypeScript 代码库中大量使用 `var` 语句的原因，这与 JavaScript 的“时空死区”（Temporal Dead Zone, TDZ）相关。

- **背景**：现代 JavaScript 推荐使用 `const` 和 `let` 声明变量，它们具有块级作用域，能避免变量泄漏到外部；而 `var` 声明存在作用域泄漏和可变性问题，容易导致错误。
- **时空死区（TDZ）**：指变量声明后但未初始化的区域。在 TDZ 内访问变量会抛出 `ReferenceError`，这是 `const` 和 `let` 的安全特性。例如，在变量初始化前调用依赖该变量的函数会触发错误。
- **TypeScript 使用 `var` 的原因**：尽管 `var` 有缺陷，但 TypeScript 代码库中仍大量使用它，主要是为了性能优化。TDZ 检查需要运行时判断，引入性能开销；迁移部分代码到 `var` 后，TypeScript 在基准测试中获得了约 8% 的性能提升。
- **结论**：作者个人倾向于避免使用 `var`，但理解 TypeScript 的权衡；同时提到 TypeScript 可能迁移到 Go 以进一步优化性能。

文章还提供了相关代码示例和讨论链接，帮助读者理解 TDZ 的影响和性能问题。
