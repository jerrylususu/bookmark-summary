# Roaming RAG – Make the Model Find the Answers - Arcturus Labs
- URL: http://arcturus-labs.com/blog/2024/11/21/roaming-rag--make-_the-model_-find-the-answers/
- Added At: 2024-12-06 14:27:37
- [Link To Text](2024-12-06-roaming-rag-–-make-the-model-find-the-answers---arcturus-labs_raw.md)

## TL;DR
文章介绍了Roaming RAG，一种利用LLM助手浏览结构化文档以寻找答案的方法，无需复杂的检索基础设施，适用于法律代码、技术书籍等结构良好的文档。通过简化文档结构和使用唯一标识符，助手能有效导航并回答问题，提供更丰富的上下文信息。

## Summary
1. **引言**：
   - RAG（Retrieval-Augmented Generation）设置复杂，调试困难。
   - 传统RAG需要建立检索基础设施，包括向量数据库和文档处理管道。
   - 在LLM应用中，需要从文档中提取相关片段并整合到提示中。
   - 问题可能源于提示、分块或嵌入模型。

2. **替代方案**：
   - 提出“Roaming RAG”概念，让LLM助手自行浏览文档寻找答案。
   - 适用于结构良好的文档，如法律代码、技术书籍、产品手册等。

3. **核心思想**：
   - 利用LLM助手阅读文档的层次结构，并根据问题展开相关部分。
   - 无需设置检索基础设施，减少出错机会。

4. **演示**：
   - 使用llms.txt文件作为示例，展示Roaming RAG的工作原理。
   - llms.txt是一种机器可读文档，帮助LLM快速理解网站或项目的关键信息。
   - 演示中，用户提问“Cursor的Tab自动完成功能与GitHub Copilot有何不同？”，助手通过浏览文档找到答案。

5. **操作方法**：
   - 提供文档的简化版本，让模型能够导航并找到所需信息。
   - 文档需结构良好，标题清晰，内容逻辑性强。
   - 使用简化文档，保留顶级标题和部分开头文本，提供二级标题但不包含子内容。
   - 每个部分分配唯一标识符，便于扩展。

6. **后端实现**：
   - 使用`expand_section`工具扩展文档部分。
   - 系统消息解释助手的任务，即从关联的llms.txt中回答问题。

7. **实际应用**：
   - 助手通过浏览文档大纲，展开相关部分以寻找答案。
   - 助手可以同时打开多个部分，或深入阅读子部分。
   - 若无法找到信息，助手会建议其他查找方法。

8. **结论**：
   - Roaming RAG不适用于所有文档，仅适用于结构良好的文档。
   - 优势包括更丰富的上下文和无需额外基础设施。
   - 感谢Juan Pablo Mesa Lopez和Dan Becker的反馈。

9. **推广**：
   - 作者撰写了一本关于LLM应用提示工程的书，并提供问题咨询和博客订阅服务。
