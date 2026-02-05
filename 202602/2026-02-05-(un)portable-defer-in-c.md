# (Un)portable defer in C
- URL: https://antonz.org/defer-in-c/
- Added At: 2026-02-05 14:21:19
- Tags: #read #c

## TL;DR
文章探讨C语言中`defer`功能的非标准实现，比较多种方案后推荐Simplified GCC/Clang版本，跨平台时可选Stack版本，认为现有实现已足够，无需等待C标准。

## Summary
文章讨论了C语言中`defer`功能的非标准实现方法，因为C标准尚未正式纳入`defer`，但该功能在资源管理中非常重要。文章比较了多种实现方案，并评估了它们的优缺点。

首先，文章介绍了背景：`defer`在现代系统编程语言中很常见，能简化资源释放，但C语言的标准提案（如N2895和N3734）尚未被接受，导致开发者依赖非标准实现。

接下来，文章详细分析了几种实现方法：
- **C23/GCC版本**：利用C23属性语法和GCC的嵌套函数、cleanup属性，实现简单，但仅限GCC编译器，不支持Clang。
- **C11/GCC版本**：适配C11标准，类似C23版本，但同样仅限GCC。
- **GCC/Clang版本**：结合GCC的cleanup属性和Clang的块扩展，需要编译标志（如`-fblocks`），支持两种编译器，但不支持MSVC，且语法需注意（如使用`__block`变量）。
- **MSVC版本**：使用Windows特有的结构化异常处理（__try和__finally），仅适用于Windows平台，不是真正的`defer`替代。
- **Long jump版本**：基于setjmp和longjmp，实现复杂且不推荐用于生产环境，因为代码冗长或hacky。
- **STC版本**：使用宏和循环，简单且兼容所有主流编译器，但不支持早期退出（如break或return），会导致延迟代码不执行。
- **Stack版本**：通过栈结构管理延迟调用，支持所有编译器，能正确处理早期退出，但语法受限（需使用defers和returnd宏），且只支持单函数调用。
- **Simplified GCC/Clang版本**：简化版，仅支持函数调用，利用cleanup属性，简洁有效，作者偏好此版本，但缺少MSVC支持。

最后，作者表达个人观点：推荐Simplified GCC/Clang版本，因为其实用且易于实现；如果需要跨平台支持（包括MSVC），则考虑Stack版本。总体而言，文章认为无需等待C标准，现有实现已足够。
