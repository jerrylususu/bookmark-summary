# Everything I've learned so far about running local LLMs
- URL: https://nullprogram.com/blog/2024/11/10/
- Added At: 2024-11-11 14:15:02
- [Link To Text](2024-11-11-everything-i've-learned-so-far-about-running-local-llms_raw.md)

## TL;DR
作者探索了LLM的快速发展，强调了技术进步的迅速和避免供应商锁定的必要性。他推荐使用llama.cpp和Hugging Face上的模型，并介绍了多种LLM的实际应用和局限性。

## Summary
1. **LLM探索背景**：
   - 作者在过去一个月探索了大型语言模型（LLM）的快速发展领域。
   - 现在可以在Raspberry Pi上运行比原始ChatGPT更智能的LLM。
   - 技术进步迅速，信息可能在几个月内就过时。

2. **LLM简介**：
   - LLM是2022年突破性的神经网络，用于训练对话式“聊天”。
   - 用户可以与一个难以区分于人类的创造性人工智能进行对话。

3. **技术进步**：
   - 每周都有新发展，作者建议忽略超过一年的信息。
   - 最好的跟进方式是通过[r/LocalLLaMa](https://old.reddit.com/r/LocalLLaMA)。

4. **避免供应商锁定**：
   - 作者担心供应商锁定，曾因服务关闭或更改而受到影响。
   - 现在可以在自己的硬件上运行接近最先进水平的模型，避免了供应商锁定问题。

5. **运行LLM的要素**：
   - 需要**软件**和**模型**。

6. **软件选择**：
   - 作者主要使用[llama.cpp](https://github.com/ggerganov/llama.cpp)。
   - 其他选项存在，但llama.cpp适用于基本的CPU推理，无需Python环境。
   - 在Windows上，llama-server.exe大小为5MB，无运行时依赖。

7. **GPU推理限制**：
   - GPU推理的瓶颈是视频RAM（VRAM）。
   - 模型越大，需要的RAM越多，上下文窗口越长。
   - 低于8GB VRAM时不建议使用GPU推理。

8. **llama-server的使用**：
   - llama-server是一个HTTP服务器，默认端口8080，带有聊天UI和API。
   - 上下文大小是LLM一次可以处理的最大token数量，通常为8K到128K。
   - `--flash-attn`选项可以减少内存需求，建议使用。

9. **模型选择**：
   - [Hugging Face](https://huggingface.co/)是“LLM的GitHub”，免费托管各种模型。
   - 对于llama.cpp，建议使用GGUF格式的模型。
   - 推荐使用`Q4_K_M`量化，4-bit量化。

10. **作者喜欢的模型**：
    - **Mistral-Nemo-2407 (12B)**：适用于写作和代码审查。
    - **Qwen2.5-14B和Qwen2.5-72B**：阿里巴巴云的模型，性能出色。
    - **Gemma-2-2B**：适用于快速翻译。
    - **Phi3.5-Mini (4B)**：适用于文档评估。
    - **SmolLM2-360M**：适用于旧硬件。
    - **Mixtral-8x7B (48B)**：适用于CPU推理。
    - **Llama-3.1-70B和Llama-3.1-Nemotron-70B**：需要远程访问。

11. **用户界面**：
    - 作者使用llama.cpp的内置UI，并构建了自己的命令行工具**Illume**。
    - Illume可以将标准输入转换为API查询，并将响应流式传输到标准输出。

12. **FIM（Fill-in-the-Middle）**：
    - FIM是LLM的一种训练方式，用于在现有程序中生成代码。
    - 使用特殊token来分隔前缀、后缀和中段。
    - 一些模型在FIM方面表现出色，如DeepSeek-Coder-V2-Lite和Qwen2.5-Coder-7B。

13. **LLM的实际应用**：
    - **校对**：适用于文档校对，但建议手动审查。
    - **写作短篇小说**：适用于生成创意内容。
    - **生成性娱乐**：与历史人物对话或生成新场景。
    - **语言翻译**：适用于快速翻译。

14. **LLM的局限性**：
    - **正确性验证**：LLM输出不可靠，需要手动验证。
    - **工作记忆**：LLM的上下文长度有限，通常为几千行代码。
    - **编程能力**：LLM生成的代码质量不高，难以维护。
    - **经济性**：如果AI能大幅提高生产力，公司不会出售AI，而是自己使用。
