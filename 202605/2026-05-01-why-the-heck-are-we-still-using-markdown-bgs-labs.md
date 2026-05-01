# Why the heck are we still using Markdown?? | BGs Labs
- URL: https://bgslabs.org/blog/why-are-we-using-markdown/
- Added At: 2026-05-01 09:53:27
- Tags: #read #language

## TL;DR
Markdown 因语法歧义、内联 HTML 安全风险及缺乏规范而问题重重，作者建议转向更严谨的替代品或开发新工具。

## Summary
Markdown 作为一种轻量级标记语言，因其简洁易学而被广泛使用，但其设计存在诸多问题。作者指出，Markdown 的语法存在歧义，例如多种方式可表示同一格式（如粗体可用 `**`、`__` 或 `<b>`），导致解析复杂且易出错。此外，Markdown 支持内联 HTML，这引入了安全风险（如 XSS 漏洞）和解析负担，使其偏离了“简单标记语言”的初衷。

Markdown 的语法源自早期电子邮件和网络论坛的惯例，但遗留了多种冗余写法（如两种标题语法、列表和脚注的上下文依赖），使其变得像 C++ 一样复杂。作者认为，Markdown 在解析和渲染时面临挑战：简单文本转换需编译器级处理，而现代需求（如数学公式、自定义样式）进一步增加了复杂性。

作者提出，Markdown 的根本问题在于缺乏明确的规范和构建系统，导致功能膨胀和安全漏洞。解决方案包括放弃 Markdown，转向更严谨的替代品（如纯文本、ReStructuredText 或 MDX），或开发一个具备清晰语法、编译时钩子和安全约束的新工具。最终，作者强调，Markdown 试图充当编程语言却缺乏形式化基础，因此在标记和编程两方面均告失败。
