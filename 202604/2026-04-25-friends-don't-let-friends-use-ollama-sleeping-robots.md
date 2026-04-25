# Friends Don't Let Friends Use Ollama | Sleeping Robots
- URL: https://sleepingrobots.com/dreams/stop-using-ollama/
- Added At: 2026-04-25 07:42:54
- Tags: #read #llm #tools

## TL;DR
文章批评Ollama依赖llama.cpp却未充分致谢，存在合规问题、性能下降及商业化倾向，建议使用llama.cpp等更开放的开源替代工具。

## Summary
文章批评了Ollama项目，指出其作为本地LLM工具的流行地位并非源于自身技术，而是建立在开源项目llama.cpp之上，却长期缺乏对上游的适当致谢和合规。作者列举了Ollama的多个问题：包括最初未在文档中提及llama.cpp、违反MIT许可证要求、后来虽添加致谢但态度消极；在2025年转向自定义后端后性能下降、引入旧bug；模型命名误导用户（如将DeepSeek-R1-distill简称为DeepSeek-R1）；推出闭源桌面应用；其Modelfile格式冗余且与GGUF标准冲突；模型注册表存在瓶颈，限制量化选项并延迟新模型支持；以及2025年底转向云服务，引发隐私担忧。文章还提到Ollama作为VC支持的初创公司，遵循了典型的“开源包装-融资-商业化”路径，导致供应商锁定。

作为替代，作者推荐直接使用llama.cpp（性能更好、更开放）、Mozilla的llamafile（单文件可执行）、llama-swap（多模型管理）等开源工具，或LM Studio、Jan等GUI应用，强调这些工具更尊重上游贡献且设置简单。结论是本地LLM生态无需Ollama，而应依赖llama.cpp及其更优的包装方案。
