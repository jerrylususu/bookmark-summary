# Garbage collection and closures
- URL: https://jakearchibald.com/2024/garbage-collection-and-closures/
- Added At: 2024-09-07 10:58:37
- [Link To Text](2024-09-07-garbage-collection-and-closures_raw.md)

## TL;DR
文章讨论了JavaScript中函数内垃圾回收机制的问题，指出即使变量不再被引用，由于内部函数和作用域的存在，可能导致内存泄漏。跨浏览器存在此问题，需手动管理作用域以避免内存泄漏。

## Summary
1. **问题发现**：
   - 作者与Surma和Jason在开发过程中发现函数内的垃圾回收机制与预期不符。
   - 示例代码展示了`bigArrayBuffer`在函数执行后未被垃圾回收，导致内存泄漏。

2. **预期行为**：
   - 预期在函数执行后，`bigArrayBuffer`不再被引用，应被垃圾回收。
   - 返回的取消函数未引用`bigArrayBuffer`，不应影响其回收。

3. **实际行为**：
   - JavaScript引擎保留了`bigArrayBuffer`，因为它被内部函数引用，且关联到`demo()`调用时创建的作用域。
   - 即使内部函数不再可调用，作用域仍存在，导致`bigArrayBuffer`无法被回收。

4. **特殊情况**：
   - 某些情况下，引擎能够正确识别并回收不再需要的变量。
   - 例如，内部函数不引用`bigArrayBuffer`时，引擎不会保留它。

5. **问题案例**：
   - 当返回的取消函数仍可调用时，作用域和`bigArrayBuffer`无法被回收。
   - 需要手动设置`globalThis.cancelDemo = null`才能触发垃圾回收。

6. **跨浏览器问题**：
   - 此问题在多个浏览器中存在，且由于性能问题，不太可能被修复。
   - 相关问题已在Chromium、Firefox和WebKit中被记录。

7. **历史记录**：
   - 此问题并非首次被发现，已有多个相关文章和讨论。
   - 包括Slava Egorov在2012年的分析、David Glasser在2013年的发现，以及Kevin Schiener在2024年的React相关讨论。

8. **非`eval()`问题**：
   - 有人错误地认为此问题与`eval()`有关，但实际上并非如此。
   - `eval()`会导致静态分析困难，但直接使用`eval`关键字会触发优化，而间接使用则不会。

9. **总结**：
   - 了解JavaScript引擎的垃圾回收机制有助于避免内存泄漏。
   - 手动管理作用域和变量的生命周期是必要的，特别是在涉及闭包和定时器时。
