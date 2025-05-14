# Vision Language Models (Better, faster, stronger)
- URL: https://huggingface.co/blog/vlms-2025
- Added At: 2025-05-14 13:42:26
- [Link To Text](2025-05-14-vision-language-models-(better,-faster,-stronger)_raw.md)

## TL;DR


本文总结了一年内视觉语言模型（VLM）的核心进展：新型Any-to-any架构的跨模态模型支持多任务交互，混合专家（MoE）结构优化计算效率，小型化模型（如SmolVLM、Gemma3）实现本地运行。专业能力扩展至视觉任务处理、多模态安全过滤及文档检索（如DSE）。代理工具（smolagents、UI-TARS）结合VLM实现自动化任务交互。视频模型引入动态帧率与时序技术。通过DPO优化对齐，新基准推动评估。未来方向包括轻量化设计、代理应用、视频处理优化及跨领域民主化，开源工具与标准化数据集加速落地。

## Summary


本文总结了过去一年视觉语言模型（VLM）的关键进展：  
**1. 新模型趋势**  
- **跨模态转换模型（Any-to-any）**：如Qwen2.5-Omni、MiniCPM-o 2.6、Janus-Pro-7B，支持多模态输入（图像、文本、语音）和输出，采用“Thinker-Talker”架构提升对话能力。  
- **推理与多任务模型**：Kimi-VL-A3B-Thinking等支持长链推理、视频、文档输入及机器人操作，通过混合专家（MoE）结构优化效率。  
- **小型高效模型**：如SmolVLM系列、Gemma3-4B-IT（支持128k上下文、140+语言）、Qwen2.5-VL-3B-Instruct（擅长图像定位和文档理解），可在本地设备运行。  
- **混合专家解码器（MoE）**：在LLaVA、DeepSeek-VL2、Llama4中应用，动态激活子模型，减少计算资源，加速推理。  
- **视觉语言动作模型（VLA）**：如pi0、GR00T-N1，用于机器人领域，结合视觉与动作指令，完成复杂任务并支持设备交互。  

**2. 专业能力扩展**  
- **视觉任务处理**：PaliGemma 2、Qwen2.5-VL可执行对象检测、分割、计数，输出边界框坐标或分割掩码代码。  
- **多模态安全模型**：ShieldGemma-2-4B和Llama Guard 4，通过图像与文本分析过滤有害内容，支持实时生成过滤。  
- **多模态RAG**：  
  - **文档检索**：DSE（文档截图嵌入）和ColBERT-like架构（如ColPali）直接处理PDF图像，无需文本转换。  
  - **实时检索**：ViDoRe数据集用于多语言文档训练，提升复杂任务的准确性和效率。  

**3. 多模态代理**  
- 代理工具smolagents结合VLM实现UI导航（如Web自动化），支持动态截图反馈和工具调用（例：代码生成、浏览器控制）。  
- 权威模型UI-TARS-1.5和MAGMA-8B，在浏览器、游戏交互中展现高效性能。  

**4. 视频语言模型**  
- **视频理解技术**：LongVU通过DINOv2去冗余帧，Qwen2.5-VL利用动态帧率与时序处理，Gemma3支持时间戳嵌入，增强视频分析能力。  

**5. 对齐与优化**  
- **偏好优化技术（DPO）**：利用TRL库训练VLM，通过标注偏好数据集（如RLAIF-V）提升响应一致性，减少偏差。  

**6. 新基准测试**  
- **MMT-Bench与MMMU-Pro**：评估模型在多模态理解、推理和生成等综合能力，推动模型性能量化。  

**趋势展望**：  
小型高效模型、动态MoE结构、多模态代理、视频处理与安全控制将成为未来发展重点。开源工具（mlx、llama.cpp）和标准化数据集（如ViDoRe）加速应用落地，促进跨领域创新（如机器人、文档智能）的民主化。
