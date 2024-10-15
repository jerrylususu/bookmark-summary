# Making algorithms faster
- URL: https://learnmoderncpp.com/2024/10/12/making-algorithms-faster/
- Added At: 2024-10-13 11:10:50
- [Link To Text](2024-10-13-making-algorithms-faster_raw.md)

## TL;DR
文章探讨了通过优化和并行化算法来提升计算勾股数的效率。初始实现使用三重嵌套循环，优化后减少了内层循环范围，速度提升2.81倍。进一步并行化使用`std::for_each()`和执行策略，最终并行无序执行速度提升18.47倍。结论是并行化效果显著，优化也值得进行。

## Summary
1. **问题背景**：
   - 任何编程语言都可能编写低质量代码，通常源于使用次优算法。
   - 现代软件的大部分执行时间花在循环中，优化循环效率是值得的。
   - 利用现代机器的所有CPU以最大化吞吐量。

2. **案例研究**：
   - **目标**：改进并并行化一个简单的算法，并通过基准测试展示实际收益。
   - **算法描述**：计算所有小于给定最大斜边的勾股数（Pythagorean Triples）。

3. **初始实现**：
   - **数据结构**：使用模板结构体`PythagoreanTriple`存储三元组。
   - **算法**：三重嵌套循环，确保`a < b < c`，并使用欧几里得最大公约数算法排除重复三元组。
   - **基准测试**：最大斜边为5000时，耗时14171350微秒，找到792个三元组。

4. **优化尝试**：
   - **改进点**：
     - 找到三元组后立即跳出内层循环。
     - 利用`a < √(c² - b²)`减少内层循环范围。
   - **结果**：优化后耗时5043447微秒，速度提升2.81倍。

5. **并行化**：
   - **策略**：使用`std::for_each()`替换外层循环，并引入执行策略参数。
   - **实现细节**：
     - 使用`std::vector`存储`c`的值。
     - 使用`std::mutex`确保对`triples`向量的写访问安全。
   - **基准测试**：
     - 顺序执行（`std::seq`）：5059061微秒，速度提升2.80倍。
     - 无序执行（`std::unseq`）：5088973微秒，速度提升2.78倍。
     - 并行执行（`std::par`）：769096微秒，速度提升18.43倍。
     - 并行无序执行（`std::par_unseq`）：767454微秒，速度提升18.47倍。

6. **总结**：
   - **优化步骤**：
     1. 在单线程环境中尽可能优化算法。
     2. 使用标准库算法替换至少一个循环，并测试顺序执行策略。
     3. 进行必要的修改以适应并行算法，如排序结果以确保顺序。
   - **结论**：并行化对算法速度提升的影响大于优化，但优化是值得的，相当于使用三倍数量的CPU。

7. **代码资源**：
   - 文章的源代码可以在GitHub上找到。