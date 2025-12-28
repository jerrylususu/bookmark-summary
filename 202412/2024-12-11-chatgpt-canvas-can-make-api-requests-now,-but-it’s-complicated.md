# ChatGPT Canvas can make API requests now, but it’s complicated
- URL: https://simonwillison.net/2024/Dec/10/chatgpt-canvas/
- Added At: 2024-12-11 14:30:01

## TL;DR
ChatGPT Canvas通过Pyodide在浏览器中运行Python代码，支持网络请求，扩展了应用场景，但也带来了CORS问题和安全风险。与Code Interpreter相比，Canvas更灵活但功能受限，用户需适应新的使用规则。

## Summary
1. **ChatGPT Canvas简介**：
   - ChatGPT Canvas是OpenAI推出的新功能，允许用户与ChatGPT在侧边面板中共享编辑器中协作编辑文档或编写代码。
   - 该功能扩展了ChatGPT的应用场景，超越了纯聊天模式。

2. **Canvas的Python运行机制**：
   - Canvas中的Python代码可以通过Pyodide在浏览器中直接运行，而不是通过Code Interpreter在服务器端运行。
   - Pyodide是Python编译为WebAssembly的实现，允许在浏览器中执行Python代码。

3. **网络请求能力**：
   - Canvas中的Python代码可以进行网络请求，而Code Interpreter则完全禁止网络访问。
   - 这使得Canvas在处理API请求时更加灵活，但也带来了潜在的安全风险。

4. **CORS问题**：
   - 由于Canvas中的Python代码直接在浏览器中运行，因此它只能访问那些实现了开放CORS策略的API端点。
   - CORS（跨域资源共享）是与LLM（大型语言模型）交互时的一个常见问题，即使在专业开发者中也较为晦涩。

5. **功能对比**：
   - **Code Interpreter**：
     - 可以访问上传的文件和内置库，但不能进行API请求。
     - 无法通过`pip install`安装额外包，但可以通过上传wheel文件来扩展功能。
   - **Canvas Python**：
     - 可以使用Pyodide进行API请求，但不能访问上传的文件。
     - 可以通过micropip安装额外的Python包，但仅限于与Pyodide兼容的纯Python包。

6. **用户界面限制**：
   - 无论是Canvas还是Code Interpreter，都无法提供完全自定义的用户界面。
   - 但它们都可以使用Pandas生态系统中的可视化工具来展示图表或表格。

7. **复杂性问题**：
   - 随着功能的增加，ChatGPT的使用变得越来越复杂，用户需要理解多种不同的运行机制和限制。
   - 即使是经验丰富的开发者也可能难以完全掌握这些工具的所有功能。

8. **潜在的安全风险**：
   - Canvas的API请求能力可能成为数据泄露的新途径。
   - 攻击者可能通过提示注入攻击诱使用户运行恶意Python代码，从而将敏感数据通过API泄露给攻击者。

9. **总结**：
   - ChatGPT Canvas的引入增加了工具的灵活性，但也带来了复杂性和安全风险。
   - 随着LLM工具的功能不断扩展，用户需要不断学习和适应新的使用规则和限制。
