# A Short Survey of Compiler Targets
- URL: https://abhinavsarkar.net/notes/2025-compiler-backend-survey/
- Added At: 2025-11-08 09:03:43
- Tags: #read #compiler
- [Link To Text](2025-11-08-a-short-survey-of-compiler-targets_raw.md)

## TL;DR
本文概述了编译器后端的多种目标选项，包括机器码、中间表示、高级语言转译、虚拟机字节码、WebAssembly等，并分析其优缺点。选择时需根据性能、可移植性和开发复杂度进行权衡。

## Summary
### 一、引言
本文简要调查了编译器后端的多种目标选项，对比了传统与现代方法的差异，旨在帮助编译器开发者根据需求选择合适的编译目标。

### 二、主要编译目标分类及特点

1. **机器码/汇编语言**
   - 直接生成针对特定指令集架构（ISA）的代码，如 Tiny C Compiler 和 Turbo Pascal。
   - 优点：高性能、低延迟。
   - 挑战：需处理寄存器分配等底层细节，可移植性差。

2. **中间表示（IR）**
   - 先将源代码转换为语言无关的 IR，再生成机器码。
   - **主流工具**：
     - LLVM：被 Rust、Swift 等语言使用，支持多架构。
     - GCC：通过 GIMPLE IR 和 libgccjit 实现，适用于 JIT 编译。
     - 轻量级替代品：如 QBE（强调简单性）和 libFIRM（基于图的 SSA 表示）。

3. **其他高级语言**
   - 通过转译（transpilation）利用现有语言的工具链。
   - **常见目标**：
     - C/C++：提高可移植性（如 Chicken Scheme、Vala）。
     - JavaScript：适用于浏览器和 JS 运行时（如 TypeScript、PureScript）。
     - Lua：轻量级脚本语言（如 MoonScript、Fennel）。
     - Lisp 方言：如 Chez Scheme（被 Idris 2、Racket 使用）。

4. **虚拟机/字节码**
   - 生成便携字节码，由虚拟机提供垃圾回收、JIT 编译等功能。
   - **主流虚拟机**：
     - JVM：支持 Java、Kotlin 等语言。
     - CLR：支持 C#、F# 等。
     - BEAM：专注于高并发和容错（如 Erlang、Elixir）。
     - MoarVM：为 Raku 语言设计。

5. **WebAssembly（Wasm）**
   - 新兴目标，注重安全性和效率，支持浏览器和非浏览器环境（通过 WASI）。
   - 被 Rust、Go、Zig 等语言采用。

6. **元追踪和元编译框架**
   - 用于构建自定义 JIT 编译器，而非直接作为编译目标。
   - **示例**：
     - RPython：用于实现 PyPy。
     - GraalVM/Truffle：支持多语言互操作。

7. **非常规目标**
   - 出于学术或实验目的，挑战编译极限。
   - **例子**：
     - Brainfuck：极简语言，作为编译挑战。
     - Lambda 演算：用于教育性编译器。
     - SKI 组合子：更简化的计算模型。
     - JSFuck：仅用 6 个字符编写 JS 代码。
     - 其他：Postscript、正则表达式、乐高、细胞自动机等。

### 三、结论
选择编译目标需权衡性能、可移植性、开发复杂度等因素。作者以幽默方式结尾，提及计划将 C++ 编译到 JSFuck，强调了编译目标的多样性。
