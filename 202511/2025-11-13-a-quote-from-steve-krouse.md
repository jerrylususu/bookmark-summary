# A quote from Steve Krouse
- URL: https://simonwillison.net/2025/Nov/12/steve-krouse/
- Added At: 2025-11-13 13:28:50
- Tags: #read #llm
- [Link To Text](2025-11-13-a-quote-from-steve-krouse_raw.md)

## TL;DR
MCP协议利用LLM动态推理机制，实现快速迭代且无需担心兼容性问题，相比传统API具有更高灵活性和开发效率。

## Summary
这篇文章引用了Steve Krouse关于MCP（Model Context Protocol）的观点，比较了MCP与传统API的区别。主要内容如下：

1. **MCP开发速度更快**：MCP与传统API不同，允许开发者快速迭代发布，这得益于运行时的动态推理机制。

2. **传统API的限制**：传统API是对开发者的承诺，一旦代码依赖这些API，任何变更都可能导致兼容性问题，甚至需要紧急修复代码。

3. **MCP的优势**：MCP服务器由LLM（大型语言模型）调用，每次都会动态读取规范，因此MCP服务器可以频繁变更，无需担心破坏承诺。LLM每次调用都能重新适应变化，无需预先固定接口。

引用来源：Steve Krouse的推文，发布于2025年11月12日。文章还包含博客的导航信息、相关标签和归档链接，但核心内容是围绕MCP的灵活性和效率展开。
