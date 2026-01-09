# Why Object of Arrays (SoA pattern) beat interleaved arrays: a JavaScript performance rabbit hole | Royal Bhati's Blog
- URL: https://royalbhati.com/posts/js-array-vs-typedarray
- Added At: 2026-01-09 14:27:19
- Tags: #read #perf

## TL;DR
通过对比数组结构（AoS）和结构数组（SoA）在JavaScript中的性能，发现SoA模式速度提升4倍，优势源于减少对象分配、优化循环和属性访问。SoA核心通过连续内存布局降低开销，更适合大数据场景。

## Summary
本文探讨了在JavaScript中使用数组结构（AoS）和结构数组（SoA）模式时的性能差异。通过实验对比，发现SoA模式显著快于AoS，核心因素如下：

### 实验设置
- **AoS模式**：使用数组存储对象，每个对象包含x、y、z属性。对100万个点求和耗时约42ms。
- **SoA模式**：使用三个TypedArray分别存储x、y、z属性。耗时约10ms，性能提升4倍。

### 关键发现
1. **性能差异的主因不是TypedArray与普通数组的对比**：当普通数组只包含数字时，V8引擎（如使用PACKED_DOUBLE_ELEMENTS）会优化为连续内存布局，性能与TypedArray相近。但TypedArray能保证性能稳定性。
2. **SoA优势的核心因素**：
   - **减少对象开销**：AoS模式需要为每个点创建独立对象，导致内存碎片、缓存局部性差和GC压力；SoA模式仅需少量分配，内存连续。
   - **循环开销优化**：SoA模式在每次循环中处理多个属性，减少了迭代次数和循环开销（如计数器递增和分支预测），从而提升效率。
   - **属性访问优化**：SoA模式下，属性查找（如`points.x`）可被JIT编译器提升到循环外，而AoS模式需在循环内频繁查找对象属性。
3. **其他测试验证**：
   - **预分配与push()的影响**：对读取性能无显著差异。
   - **交错存储模式（Interleaved）**：理论上有更好的缓存局部性，但实测比SoA慢，因循环内索引计算（如`i * 3`）增加开销，且JIT优化受限。
   - **缓存局部性**：现代CPU预取器能处理多数组流，因此SoA访问三个数组不会成为瓶颈。

### 结论
- SoA模式在JavaScript中性能更优，主要得益于减少对象分配、优化循环和属性访问。
- 实际开发中，应优先考虑数据布局而非单纯依赖TypedArray，尤其在处理大量数据时。作者计划进一步验证CPU多内存流处理能力。
