# Simple macOS script to extract text from images (OCR)
- URL: https://evanhahn.com/mac-ocr-script/
- Added At: 2025-07-15 14:11:50
- [Link To Text](2025-07-15-simple-macos-script-to-extract-text-from-images-(ocr)_raw.md)

## TL;DR


该文章介绍了适用于macOS的命令行OCR脚本，用户输入`ocr image_path`即可从图片提取文本。基于苹果Vision框架开发，支持多语言检测与自动纠错，但存在长破折号识别错误和准确率受图片质量影响的局限。代码由Swift编写并开源，作者邀请改进。Linux用户可尝试Frog（含Tesseract）实现类似功能。

## Summary


该文章介绍了一个在macOS系统上通过命令行提取图片文本（OCR）的简易脚本。用户只需输入`ocr image_path`即可执行，适用于截图、照片等场景。脚本基于苹果的Vision框架与文本识别API开发，因此仅限macOS使用。作者另提到Linux用户可尝试Frog（内置Tesseract）实现类似功能。

文章通过示例展示脚本运行流程：输入图片路径后，输出识别文本，但存在部分文字错误（如长破折号识别失准）。脚本源代码采用Swift编写，核心逻辑包含参数校验、OCR请求配置（多语言检测、纠错模式）及结果循环输出。代码中使用`RecognizeTextRequest`执行图像分析，并提取置信度最高的文本候选结果。

脚本局限性包括：识别失败时会将错误日志输出至标准输出，作者尚未解决此问题；识别准确率受图片质量影响。代码及完整脚本地址已给出，作者邀请读者提交改进方案并留下联系方式。
