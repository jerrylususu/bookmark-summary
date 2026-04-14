# OpenHealth – Chat with Apple Health Data, Anywhere
- URL: https://jonno.nz/posts/openhealth-chat-with-apple-health-data/
- Added At: 2026-04-14 13:17:02
- Tags: #read

## TL;DR
OpenHealth 是一个开源工具，将 Apple Health 数据转换为七个 Markdown 文件，支持本地解析与 LLM 对话，确保数据隐私与控制，适用于多设备健康分析。

## Summary
OpenHealth 是一个开源工具，旨在将 Apple Health 导出数据转换为七个易于 LLM 读取的 Markdown 文件，帮助用户与健康数据进行对话。其核心解决的问题是：Apple Health 数据庞大且难以直接分析，而现有 AI 工具（如 Claude、ChatGPT）的健康数据连接器仅限美国用户，且用户无法控制数据处理流程。

### 主要功能与特点
1. **三种使用方式**：
   - **静态网页应用**：在浏览器中直接解析导出的 ZIP 文件，无需上传数据，完全本地处理。
   - **命令行工具（CLI）**：使用 Bun 编译，支持一键导出 Markdown 文件，可打包或复制到剪贴板。
   - **手机到桌面传输**：通过 WebRTC 实现 iPhone 直接传输 ZIP 文件到桌面浏览器，仅通过 Cloudflare Worker 中转握手信号，不传输健康数据。

2. **高效数据处理**：
   - 使用流式 SAX 解析器（saxes）处理大型 XML 文件（可达 4GB），避免内存溢出。
   - 通过 Web Worker 在浏览器中运行解析，保持低内存占用。
   - 支持多设备数据源（如 Apple Watch、Withings 体重秤、MyFitnessPal），自动选择高可信度数据并去重。

3. **七个 Markdown 文件**：
   - `health_profile.md`：基线数据、来源和长期平均值。
   - `weekly_summary.md`：当前周及四周滚动对比。
   - `workouts.md`：最近四周的详细训练日志。
   - `body_composition.md`：体重趋势和营养平均值。
   - `sleep_recovery.md`：睡眠阶段、HRV、静息心率等趋势。
   - `cardio_fitness.md`：跑步日志、心率区间分布。
   - `prompt.md`：系统提示，用于指导 LLM 分析其他文件。

4. **隐私与控制**：
   - 所有解析均在本地完成，数据不上传。
   - 用户可选择将 Markdown 文件输入任意 LLM（如本地模型 Ollama），确保数据完全离线。
   - 项目采用 MIT 许可，代码开源，可自行验证。

### 适用场景
- 分析训练恢复、睡眠与运动关联、长期健康趋势等。
- 适合非美国用户或希望完全控制数据处理流程的用户。
- 适用于多设备数据整合，提供一致的健康视图。

### 注意事项
- 工具仅用于个人健康思考，不替代医疗诊断。
- 若使用云端 LLM（如 ChatGPT），数据将被该服务访问，用户需自行权衡隐私与便利。

项目地址：[GitHub](https://github.com/jonnonz1/openhealth) | [网页应用](https://openhealth-axd.pages.dev/)
