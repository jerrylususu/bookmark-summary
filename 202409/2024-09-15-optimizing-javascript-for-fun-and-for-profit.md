# Optimizing Javascript for fun and for profit
- URL: https://romgrk.com/posts/optimizing-javascript
- Added At: 2024-09-15 12:12:37
- [Link To Text](2024-09-15-optimizing-javascript-for-fun-and-for-profit_raw.md)

## TL;DR
本文详细介绍了JavaScript代码优化的多种策略，包括避免不必要的工作、字符串比较、对象形状、数组/对象方法、间接访问、缓存未命中、大对象、`eval`、字符串操作、专业化、数据结构选择等，并强调了基准测试的重要性。

## Summary
1. **优化概述**：
   - JavaScript代码通常运行速度较慢，主要是因为未进行适当的优化。
   - 性能优化通常以可读性为代价，何时追求性能或可读性由开发者决定。
   - 优化前必须进行基准测试，微优化可能对整体性能影响甚微。

2. **避免不必要的工作**：
   - 优化第一步是避免不必要的工作，包括记忆化、惰性和增量计算。
   - 在React中，可以使用`memo()`、`useMemo()`等方法。

3. **避免字符串比较**：
   - JavaScript中的字符串比较成本较高，通常为`O(n)`。
   - 使用TypeScript的枚举可以避免字符串作为枚举值。
   - 示例展示了字符串比较和整数比较的性能差异。

4. **避免不同形状的对象**：
   - JavaScript引擎通过假设对象具有特定形状来优化代码。
   - 不同形状的对象会导致引擎无法优化，性能下降。
   - 示例展示了单态、多态和超多态对象的性能差异。

5. **避免数组/对象方法**：
   - 函数式编程方法（如`map`、`filter`、`reduce`）通常比命令式编程慢。
   - 这些方法需要创建数组的完整副本，增加垃圾回收负担。
   - 示例展示了函数式和命令式方法的性能差异。

6. **避免间接访问**：
   - 代理对象、对象属性访问和函数调用都可能导致性能下降。
   - 示例展示了代理对象和直接访问对象的性能差异。

7. **避免缓存未命中**：
   - CPU通过预取和L1/L2/L3缓存优化内存访问。
   - 顺序访问内存比随机访问更快。
   - 示例展示了顺序访问和随机访问内存的性能差异。

8. **避免大对象**：
   - 大对象会导致引擎使用常规哈希表，增加缓存未命中。
   - 示例展示了通过数组访问对象和直接访问对象的性能差异。

9. **使用`eval`**：
   - `eval`可以避免某些难以优化的JavaScript模式。
   - 示例展示了使用`eval`和不使用`eval`的性能差异。

10. **谨慎使用字符串**：
    - 字符串操作在JavaScript中常见，引擎通过多种字符串表示来优化。
    - 字符串拼接和切片不会创建副本，但修改字符串会导致复制。
    - 示例展示了字符串拼接和修改的性能差异。

11. **使用专业化**：
    - 根据特定用例调整逻辑，优化常见条件。
    - 示例展示了未专业化和专业化的性能差异。

12. **数据结构选择**：
    - 选择错误的数据结构会对性能产生重大影响。
    - 示例展示了`Array.includes`和`Set.has`的性能差异。

13. **基准测试**：
    - 基准测试是优化的关键，优先优化占用大部分运行时间的代码。
    - 避免微基准测试，怀疑测试结果，选择合适的引擎进行基准测试。

14. **浏览器注意事项**：
    - 使用干净的浏览器配置文件进行基准测试，避免浏览器扩展影响结果。
    - 了解样本和结构化分析的区别，使用适当的工具进行分析。

15. **总结**：
    - 希望读者从本文中学到有用的优化技巧，欢迎反馈和问题。
