# Getting DeepSeek-OCR working on an NVIDIA Spark via brute force using Claude Code
- URL: https://simonwillison.net/2025/Oct/20/deepseek-ocr-claude-code/
- Added At: 2025-10-21 13:31:33

## TL;DR
作者在NVIDIA Spark设备上使用Claude Code成功部署DeepSeek-OCR模型。通过Docker容器自动化配置环境，关键解决了PyTorch版本与GPU兼容性问题。经测试"Free OCR"提示词效果最佳，整个流程仅需少量人工干预，验证了自动化工具的可行性。

## Summary
本文记录了作者如何使用Claude Code在NVIDIA Spark设备上通过“暴力”方式成功运行DeepSeek-OCR模型的过程。

### 项目背景
- DeepSeek发布了一个6.6GB的OCR专用模型DeepSeek-OCR，需要PyTorch和CUDA环境。
- 作者在NVIDIA Spark（ARM架构）上尝试运行该模型，并决定将整个配置过程交给Claude Code自动化完成。
- 项目耗时约40分钟，其中作者仅主动参与5-10分钟，其余时间由Claude Code自动执行。

### 实施步骤
1. **环境准备**：  
   - 通过SSH连接到NVIDIA Spark，启动一个带GPU支持的Docker容器（基于CUDA 13.0的Ubuntu镜像）。
   - 在容器内安装npm和Claude Code，并以沙盒模式运行（跳过权限检查）。

2. **初始提示与执行**：  
   - 作者向Claude Code提供目标：克隆DeepSeek-OCR的GitHub和Hugging Face仓库，检查环境兼容性，并对指定图片进行OCR测试。
   - Claude Code在过程中自动记录详细笔记到`notes.md`文件。

3. **遇到问题与解决**：  
   - **关键障碍**：PyTorch 2.5.1不支持Spark的GB10 GPU（计算能力sm_121），导致CUDA错误。
   - **解决方案**：作者提示Claude Code检查其他PyTorch版本。Claude发现PyTorch 2.9.0的ARM64 CUDA 13.0兼容版本，安装后成功绕过兼容性问题。

4. **OCR测试与优化**：  
   - 模型成功运行，但初始输出（使用`<|grounding|>`提示）仅生成带坐标的文本，未正确保存内容。
   - 作者提示优化后，Claude尝试不同提示词（如“Free OCR”和“Convert to markdown”），并生成对比表格：
     - **“Free OCR”**：速度最快，文本质量最佳，适合通用OCR。
     - **“Markdown”**：保留文档结构，速度中等。
     - **“Grounding”**：提供完整坐标，速度慢。
   - 最终成功提取OCR文本并保存结果。

5. **结果整理**：  
   - Claude自动生成脚本、笔记、总结文件（如`README.md`、`PROMPTS_GUIDE.md`）和输出文件，打包为zip供作者下载。

### 关键成功因素
1. **明确的任务设计**：提供具体目标、环境访问权限和资源链接，符合“代理循环”设计原则。
2. **沙盒环境**：Docker容器允许Claude Code无干预运行，避免操作繁琐。
3. **人工干预关键点**：作者在遇到兼容性问题时提供方向性提示，引导Claude找到解决方案。

### 附加技巧：远程监控容器文件
- 作者使用VS Code的“Remote SSH”和“Dev Containers”扩展，实时监控Docker容器内的文件变化，并直接下载结果。

### 结论
- DeepSeek-OCR模型效果良好，但需通过提示词调整优化输出。
- 该方法证明了自动化工具有效性，未来可复用于类似复杂环境配置任务。
