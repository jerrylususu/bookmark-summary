# How I Automated My Podcast Transcript Production With Local AI
- URL: https://den.dev/blog/how-i-automated-podcast-transcription-with-local-ai/
- Added At: 2025-03-08 10:56:49
- [Link To Text](2025-03-08-how-i-automated-my-podcast-transcript-production-with-local-ai_raw.md)

## TL;DR
作者开发开源工具roboscribe，通过整合WhisperX语音处理和Llama-3.1等大模型，实现本地AI自动化播客转录与优化。该工具可自动完成转录、时间轴对齐、说话人分离及文本清理（去除冗余、修正语法），处理35分钟音频仅需15分钟，输出质量显著提升。当前需高配GPU运行，未来计划优化适配更多设备。工具已开源（GitHub可获取）。

## Summary
作者通过开发名为 `roboscribe` 的开源工具，实现了本地 AI 自动化播客转录流程，显著提升效率并减少人工干预。该工具整合 WhisperX 进行语音转文本和说话人分离，并利用本地大语言模型（如 Llama-3.1-8B-Instruct）对转录内容进行清理优化。

### 核心步骤与技术细节
1. **语音处理流程**：
   - **转录**：使用 WhisperX 将音频转换为文本，记录时间戳。
   - **对齐**：细化时间轴与文本片段的匹配。
   - **说话人分离**：识别并标注不同发言者，依赖 Hugging Face 的模型实现。
   
2. **文本清理规则**：
   - 拆分文本块不超过 500 字，避免模型输出异常。
   - 结构化输出为 JSON 格式以保证一致性。
   - 明确系统指令：强调保留原始内容的准确性，去除重复词、填充词（如“uh”），添加标点与语法修正，禁止添加新内容或干扰性文本。

3. **硬件与环境**：
   - 硬件配置：AMD Ryzen 9 5950X CPU、64GB RAM、双 NVIDIA RTX 3090 GPU。
   - 依赖项：CUDA 12.6、Python 3.12、cuDNN，推荐在 Linux 或 WSL2 运行。

### 输出与效果
- **时间效率**：35-40 分钟音频处理耗时约 15 分钟，较纯人工整理大幅缩短。
- **输出文件**：包含原始转录（`YOUR_OUTPUT_FILE.raw.txt`）、清理后版本（`.txt`）及中间调试文件（`.temp.txt`）。
- **质量对比**：使用 WinMerge 对比原始与清理工作用例显示，文本流畅度和可读性显著提升。

### 限制与展望
- 当前工具对硬件要求较高，需 GPU 支持，未来计划优化适配更广泛设备。
- 清洁模型（如 Instruct 类型）在多轮对话中表现有限，但单次清理任务效果良好。
- 作者计划改进动态资源配置与准确性，并探索进一步优化流程的潜力。

工具开源地址：[GitHub - roboscribe](https://github.com/dend/roboscribe)，支持通过命令行调用，需提供 Hugging Face 访问令牌及音频路径。
