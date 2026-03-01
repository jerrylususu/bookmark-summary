# Rolling your own serverless OCR in 40 lines of code | Christopher Krapu
- URL: https://ckrapu.github.io/blog/2026/ocr-textbooks-modal-deepseek/
- Added At: 2026-03-01 09:04:36
- Tags: #read #guide

## TL;DR
本文介绍了如何利用 Modal 无服务器平台和 DeepSeek OCR 模型，在 40 行代码内构建一个高效的 OCR 系统。该方案能将 PDF 教科书转换为可搜索的 Markdown 文本，通过云端 GPU 并行处理，实现了低成本（约 2 美元处理 600 页）且高质量的数学公式识别。

## Summary
本文介绍如何使用 Modal 平台和 DeepSeek OCR 模型，在 40 行代码内构建一个无服务器的 OCR 系统，用于将 PDF 教科书转换为可搜索的 Markdown 文本。

**核心思路与工具选择**
*   **问题**：作者希望将贝叶斯数据分析教科书 PDF 转为可搜索文本，但现有 OCR 工具昂贵或有使用限制，且本地 GPU 无法运行最新的 DeepSeek OCR 模型。
*   **解决方案**：使用 **Modal** 无服务器计算平台。Modal 允许在云端 GPU 上运行 Python 代码，按实际运行秒数付费，无需管理服务器。
*   **关键技术**：Modal 的装饰器模式（如 `@modal.function` 和 `@modal.asgi_app()`）简化了在云端部署带 GPU 的容器和 FastAPI 服务的过程。

**实现步骤**
1.  **定义容器镜像**：配置包含 PyTorch、Transformers 及相关依赖的 Docker 镜像，确保兼容 CUDA 11.8。
2.  **部署 FastAPI 服务**：在 Modal 上部署一个 FastAPI 应用，加载 DeepSeek-OCR 模型。模型在容器启动时加载一次，后续请求复用以提高吞吐量。
3.  **处理批量推理**：OCR 任务是高度并行的。通过将多页图像打包成批次（Batch）进行单次前向传播，显著提升处理速度。代码中设置了 `temperature=0.0` 以确保输出确定性。
4.  **本地客户端**：使用 `@app.local_entrypoint()` 编写本地运行的客户端脚本。该脚本读取 PDF，将页面渲染为高分辨率图像（2倍缩放以提高识别精度），并通过 HTTP 请求将批次发送至云端服务。
5.  **输出清理**：DeepSeek 的 OCR 输出包含文本坐标等 grounding tags。使用正则表达式清理这些标签，仅保留纯文本内容，并保存为 `.mmd`（多模态 Markdown）文件。

**效果与成本**
*   **性能**：处理约 600 页的教科书（批次大小为 4），在 A100 GPU 上耗时约 45 分钟，成本约 2 美元。
*   **质量**：对数学公式的识别效果出色，生成的 Markdown 文本保留了 LaTeX 格式的公式，使 PDF 变得可搜索、可被 AI 分析。
*   **价值**：该方案提供了一种低成本、可复用的方法，将扫描版教材、论文等转换为结构化文本，便于后续的 grep 搜索、AI 辅助学习或构建索引。
