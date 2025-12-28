# 从Prompt Engineering到Context Engineering - 铁蕾的个人博客
- URL: http://zhangtielei.com/posts/blog-context-engineering.html
- Added At: 2025-06-27 15:27:51

## TL;DR


Context Engineering是AI领域新兴的系统化工程理念，旨在通过动态整合信息检索、记忆管理和工具调用等模块，优化LLM接收的上下文质量，解决因模型不确定性和工具交互导致的系统稳定性问题。与静态的提示词工程不同，它强调全局动态设计，以智能筛选替代单纯扩大上下文窗口，最终实现精准、可控且聚焦的上下文管理，提升复杂场景中的AI系统表现。

## Summary


Context Engineering（上下文工程）是AI领域新兴的系统化工程理念，旨在解决LLM（大语言模型）驱动的Agent系统在复杂场景中稳定性不足的问题。其产生背景主要有两点：一是AI技术亟需在生产环境落地，但现有技术如tool calling loop易因多轮迭代导致混乱，高频故障难以接受；二是LLM的天然不确定性（基于概率预测机制）与外部工具（如网络搜索）引入大量不可控信息，使得整体Context难以精准控制。  

Context Engineering定义为动态系统工程，核心目标是通过智能架构确保LLM接收到的Context（上下文）准确、完整且格式优化，包含信息检索（如RAG）、记忆管理（长期/短期）、工具调用决策、错误处理等多模块协作。与Prompt Engineering（提示词工程）相比，它更强调全局与动态：Prompt Engineering是局部的静态技巧，依赖人工设计特定提示词；而Context Engineering需在复杂系统中动态整合多元信息源（如文档片段、工具调用历史、用户反馈等），且上下文质量对结果影响超过模型本身。  

两者的区别体现在三个方面：  
1. **范围差异**：Context Engineering是包含Prompt Engineering在内的更广泛系统工程，覆盖信息检索、工具调用、记忆管理等；  
2. **动态特性**：Context Engineering需实时动态组装Context，而Prompt Engineering多属静态预先设计；  
3. **信息复杂度**：Context Engineering整合多来源且不确定的信息（如外部工具返回结果），而传统Prompt Engineering主要依赖可控静态内容。  

文章指出，追求更长的上下文窗口并非解决之道，关键在于构建智能漏斗机制，精准筛选相关信息并优化呈现。RAG等技术在此框架下得到强化，成为Context Engineering的核心组成部分。最终目标是实现“小而聚焦”的Context设计，在可控性和完整性间取得平衡，而非单纯依赖模型能力。
