# Filesystem Backed by an LLM
- URL: https://healeycodes.com/filesystem-backed-by-an-llm
- Added At: 2025-07-08 14:19:46

## TL;DR


该文章介绍了基于大型语言模型构建FUSE文件系统"llmfs"的设计方法。通过调用OpenAI API实时生成文件内容，对系统文件或恶意脚本等场景返回错误码（如EACCES）；利用内存日志存储操作历史，支持偏移量追加写入以保证内容一致性；采用自定义JSON格式响应数据或错误，并通过LLM自动处理JSON转义。未来计划通过序列化FUSE对象优化架构。项目已开源，验证了LLM与文件系统的交互可行性。

## Summary


该文章介绍了基于大型语言模型（LLM）构建FUSE文件系统“llmfs”的实现方法和核心设计。作者通过调用OpenAI API实现实时生成文件内容，部分内容示例（如系统文件或恶意脚本）由LLM返回拒绝操作的UNIX错误码（如EACCES）。文件操作历史记录以内存日志形式存储，LLM根据上下文生成文件内容并保证一致性，例如支持按偏移量追加写入。系统使用自定义JSON格式响应，包含“data”或“error”字段，确保内容的正确生成和错误处理。技术挑战方面，LLM自动处理JSON转义问题，但作者认为未来可通过序列化FUSE对象简化架构，以扩展对更多文件系统操作的支持。项目代码已开源，演示了LLM与文件系统的交互逻辑。
