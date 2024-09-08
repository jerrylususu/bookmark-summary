# MiniJinja: Learnings from Building a Template Engine in Rust
- URL: https://lucumr.pocoo.org/2024/8/27/minijinja/
- Added At: 2024-08-28 14:50:51
- [Link To Text](2024-08-28-minijinja:-learnings-from-building-a-template-engine-in-rust_raw.md)

## TL;DR
MiniJinja是Rust实现的Jinja2兼容模板引擎，经过两年开发几乎实现Jinja2所有功能。它构建了基于文本生成优化的动态编程语言，通过Value类型和Object trait管理运行时值，并设计了基于栈的VM和AST字节码编译器。API设计巧妙，文档详尽，适合需要Jinja2兼容或对Rust运行时构建感兴趣的开发者。

## Summary
1. **MiniJinja简介**：
   - MiniJinja是作者为Rust实现的Jinja2模板引擎，旨在提供与Jinja2兼容的模板功能。
   - 提供了多个资源链接，包括[MiniJinja playground](https://mitsuhiko.github.io/minijinja-playground/)、[API Documentation](https://docs.rs/minijinja/)、[GitHub Project](https://github.com/mitsuhiko/minijinja/)、[crates.io上的minijinja](https://crates.io/crates/minijinja)和[minijinja-cli](https://crates.io/crates/minijinja-cli)。

2. **开发动机**：
   - 作者出于实验性基础设施自动化的需要，开发了MiniJinja。
   - 由于模板需要动态加载，无法使用Askama这类生成Rust代码的类型安全模板系统。
   - 大多数动态的Rust模板引擎并不完全兼容Jinja，因此作者决定再次尝试开发模板引擎。

3. **功能实现**：
   - 经过两年的开发，MiniJinja几乎实现了与Jinja2相同的功能，且使用体验良好。

4. **运行时值**：
   - MiniJinja构建了一个基于文本生成优化的动态编程语言，面临内存管理和将原生Rust对象暴露给嵌入语言的挑战。
   - 核心对象模型是一个Value类型，通过enum实现，支持多种基本类型和对象。
   - 对象通过Object trait实现，提供多种方法如get_value、enumerate、call等。

5. **枚举器和对象行为**：
   - 枚举器允许对象描述其内部内容，结合repr()方法，引擎改变迭代方式。
   - 枚举器包括NonEnumerable、Empty、Iter、Seq、Values等类型，通过try_iter方法转换为迭代器。
   - 枚举器的长度查询通过size_hint实现，影响对象的交互方式。

6. **构建虚拟机**：
   - MiniJinja采用基于栈的VM和AST字节码编译器，避免使用代码生成。
   - AST设计采用包含Spanned<T>值的大型enum，Spanned<T>包装内部节点并存储代码位置Span。
   - 指令集是一个大型enum，保持变体参数数量较低，以节省内存。
   - VM通过State对象维护运行时状态，通过循环遍历指令列表执行模板。

7. **宏的处理**：
   - 宏作为Value持有Macro Object，通过ID动态查找指令，确保模板状态一致性。
   - 宏可能引起循环引用，引擎通过手动清除闭包来打破循环。

8. **API设计**：
   - 通过巧妙的trait hackery实现不同签名的函数注册为过滤器。
   - FunctionArgs、ArgType、Filter、FunctionResult等trait帮助实现类型转换和函数调用。

9. **总结**：
   - MiniJinja的开发展示了Rust中创造性API设计的可能性。
   - 引擎的公共API设计良好，内部和外部都有详尽的文档，适合需要Jinja2兼容模板引擎或对Rust运行时和对象系统构建感兴趣的开发者。
