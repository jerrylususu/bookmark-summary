# Byaidu/PDFMathTranslate
- URL: https://github.com/Byaidu/PDFMathTranslate
- Added At: 2024-11-15 15:35:35
- [Link To Text](2024-11-15-byaidu-pdfmathtranslate_raw.md)

## TL;DR
PDFMathTranslate 是一个用于 PDF 科学论文翻译和双语对比的工具，支持保留公式、图表和目录，兼容多种翻译服务如 Google、DeepL、Ollama 和 OpenAI。安装需 Python 3.8-3.12，可通过命令行执行翻译，支持部分翻译和指定语言。感谢多个开源项目的支持。

## Summary
1. **项目简介**：PDFMathTranslate 是一个用于 PDF 科学论文翻译和双语对比的工具，能够完整保留排版，支持多种翻译服务。

2. **主要功能**：
   - **保留公式和图表**：翻译过程中保留文档中的数学公式和图表。
   - **保留目录**：保留文档的目录结构。
   - **多翻译服务支持**：支持 Google、DeepL、Ollama、OpenAI 等多种翻译服务。

3. **安装要求**：需要 Python 版本 >=3.8 且 <=3.12。

4. **使用方法**：
   - **命令行执行**：通过命令行执行翻译命令，生成翻译后的文档 `example-zh.pdf` 和双语文档 `example-dual.pdf`。
   - **部分翻译**：支持指定部分文档进行翻译，例如 `pdf2zh example.pdf -p 1-3,5`。
   - **指定语言**：支持指定翻译的源语言和目标语言，例如 `pdf2zh example.pdf -li en -lo ja`。
   - **使用特定翻译服务**：
     - **DeepL/DeepLX**：设置环境变量 `DEEPL_SERVER_URL` 和 `DEEPL_AUTH_KEY`，例如 `pdf2zh example.pdf -s deepl`。
     - **Ollama**：设置环境变量 `OLLAMA_HOST`，例如 `pdf2zh example.pdf -s ollama:gemma2`。
     - **OpenAI/SiliconCloud/Zhipu**：设置环境变量 `OPENAI_BASE_URL` 和 `OPENAI_API_KEY`，例如 `pdf2zh example.pdf -s openai:gpt-4o`。
   - **正则表达式**：使用正则表达式指定需要保留的公式字体和字符，例如 `pdf2zh example.pdf -f "(CM[^RT].*|MS.*|.*Ital)" -c "(\\(|\\||\\)|\\+|=|\\d|[\\u0080-\\ufaff])"`。

5. **预览**：提供了多个翻译结果的预览图片，展示了翻译后的文档效果。

6. **致谢**：
   - **文档合并**：使用 [PyMuPDF](https://github.com/pymupdf/PyMuPDF)。
   - **文档解析**：使用 [Pdfminer.six](https://github.com/pdfminer/pdfminer.six)。
   - **文档提取**：使用 [MinerU](https://github.com/opendatalab/MinerU)。
   - **多线程翻译**：使用 [MathTranslate](https://github.com/SUSYUSTC/MathTranslate)。
   - **布局解析**：使用 [DocLayout-YOLO](https://github.com/opendatalab/DocLayout-YOLO)。
   - **文档标准**：参考 [PDF Explained](https://zxyle.github.io/PDF-Explained/) 和 [PDF Cheat Sheets](https://pdfa.org/resource/pdf-cheat-sheets/)。

7. **贡献者**：列出了项目的贡献者列表。

8. **Star 历史**：展示了项目的 Star 历史图表。
