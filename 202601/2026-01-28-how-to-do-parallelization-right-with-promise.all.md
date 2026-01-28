# How to do Parallelization Right with Promise.all
- URL: https://dodov.dev/blog/how-to-do-parallelization-right-with-promise-all
- Added At: 2026-01-28 12:44:18
- Tags: #read #tips

## TL;DR
在JavaScript中，错误地在Promise.all中使用await会导致并行化失效，代码顺序执行。正确做法是直接传递Promise，或使用parallelize函数进行类型检查，以提升性能并避免错误。

## Summary
并行化是提升性能的简单有效方法，但在JavaScript中容易出错，甚至TypeScript也无法完全避免。文章通过示例说明了常见错误和正确做法。

**问题引入**：JavaScript中，错误使用`Promise.all`可能导致并行化失效。例如，在代码中，如果在每个Promise前添加`await`，会使Promise顺序执行，失去并行优势。

**错误示例**：
- 代码：在`Promise.all`数组中每个`delay`调用前使用`await`，导致执行顺序为100ms、150ms、200ms，总耗时455ms。
- 输出：Promise依次解析，没有并行化，`Promise.all`无效。

**正确示例**：
- 代码：移除`await`，直接传递Promise给`Promise.all`，实现并行执行。
- 输出：Promise几乎同时解析，总耗时约201ms，性能提升超过2倍。

**解决方案**：提供`parallelize`包装函数，强制检查传入值是否为Promise类型。如果误用`await`，TypeScript会报错，避免错误被忽视。这有助于在复杂代码中快速发现性能问题。

**结语**：在真实生产代码中，这种错误容易隐藏，使用`parallelize`函数可以简化检查，优化性能。
