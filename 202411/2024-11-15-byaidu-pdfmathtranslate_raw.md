Title: GitHub - Byaidu/PDFMathTranslate: PDF scientific paper translation and bilingual comparison - 完整保留排版的 PDF 文档全文双语翻译，支持 Google/DeepL/Ollama/OpenAI 翻译

URL Source: https://github.com/Byaidu/PDFMathTranslate

Markdown Content:
English | [简体中文](https://github.com/Byaidu/PDFMathTranslate/blob/main/README_zh-CN.md)

PDFMathTranslate
----------------

[](https://github.com/Byaidu/PDFMathTranslate#pdfmathtranslate)

[![Image 1](https://camo.githubusercontent.com/1979980005d1807ecd4ec85a5adea164a0de4c50a13507a102473a2e5d6376e7/68747470733a2f2f696d672e736869656c64732e696f2f707970692f762f706466327a68)](https://pypi.org/project/pdf2zh/) [![Image 2](https://camo.githubusercontent.com/9f40687efb34ebfcd5c15dff60336204d77f07021ab22ecfedde1ec53156f992/68747470733a2f2f7374617469632e706570792e746563682f62616467652f706466327a68)](https://pepy.tech/projects/pdf2zh) [![Image 3](https://camo.githubusercontent.com/8f57d6cdf002babece25e78a86d501103ca389ede211c3d2a360138d892d5fad/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f6c6963656e73652f4279616964752f5044464d6174685472616e736c617465)](https://github.com/Byaidu/PDFMathTranslate/blob/main/LICENSE) [![Image 4](https://camo.githubusercontent.com/319447b7de63636e4cfd81c002fe3b02c25ae1cefc09686f824deaccd3c5ca68/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f54656c656772616d2d3243413545303f7374796c653d666c61742d73717565617265266c6f676f3d74656c656772616d266c6f676f436f6c6f723d7768697465)](https://t.me/+Z9_SgnxmsmA5NzBl)

PDF scientific paper translation and bilingual comparison.

*   📊 Retain formulas and charts.
    
*   📄 Preserve table of contents.
    
*   🌐 Support multiple translation services.
    

Feel free to provide feedback in [issues](https://github.com/Byaidu/PDFMathTranslate/issues) or [user group](https://t.me/+Z9_SgnxmsmA5NzBl).

Installation
------------

[](https://github.com/Byaidu/PDFMathTranslate#installation)

Require Python version \>\=3.8, <\=3.12

Usage
-----

[](https://github.com/Byaidu/PDFMathTranslate#usage)

Execute the translation command in the command line to generate the translated document `example-zh.pdf` and the bilingual document `example-dual.pdf` in the current directory. Use Google as the default translation service.

Please refer to [ChatGPT](https://chatgpt.com/share/6734a83d-9d48-800e-8a46-f57ca6e8bcb4) for how to set environment variables.

### Translate the entire document

[](https://github.com/Byaidu/PDFMathTranslate#translate-the-entire-document)

### Translate part of the document

[](https://github.com/Byaidu/PDFMathTranslate#translate-part-of-the-document)

pdf2zh example.pdf -p 1-3,5

### Translate with the specified language

[](https://github.com/Byaidu/PDFMathTranslate#translate-with-the-specified-language)

See [Google Languages Codes](https://developers.google.com/admin-sdk/directory/v1/languages), [DeepL Languages Codes](https://developers.deepl.com/docs/resources/supported-languages)

pdf2zh example.pdf -li en -lo ja

### Translate with DeepL/DeepLX

[](https://github.com/Byaidu/PDFMathTranslate#translate-with-deepldeeplx)

See [DeepLX](https://github.com/OwO-Network/DeepLX)

Set ENVs to construct an endpoint like: `{DEEPL_SERVER_URL}/translate`

*   `DEEPL_SERVER_URL` (Optional), e.g., `export DEEPL_SERVER_URL=https://api.deepl.com`
*   `DEEPL_AUTH_KEY`, e.g., `export DEEPL_AUTH_KEY=xxx`

pdf2zh example.pdf -s deepl

### Translate with Ollama

[](https://github.com/Byaidu/PDFMathTranslate#translate-with-ollama)

See [Ollama](https://github.com/ollama/ollama)

Set ENVs to construct an endpoint like: `{OLLAMA_HOST}/api/chat`

*   `OLLAMA_HOST` (Optional), e.g., `export OLLAMA_HOST=https://localhost:11434`

pdf2zh example.pdf -s ollama:gemma2

### Translate with OpenAI/SiliconCloud/Zhipu

[](https://github.com/Byaidu/PDFMathTranslate#translate-with-openaisiliconcloudzhipu)

See [SiliconCloud](https://docs.siliconflow.cn/quickstart), [Zhipu](https://open.bigmodel.cn/dev/api/thirdparty-frame/openai-sdk)

Set ENVs to construct an endpoint like: `{OPENAI_BASE_URL}/chat/completions`

*   `OPENAI_BASE_URL` (Optional), e.g., `export OPENAI_BASE_URL=https://api.openai.com/v1`
*   `OPENAI_API_KEY`, e.g., `export OPENAI_API_KEY=xxx`

pdf2zh example.pdf -s openai:gpt-4o

### Use regex to specify formula fonts and characters that need to be preserved

[](https://github.com/Byaidu/PDFMathTranslate#use-regex-to-specify-formula-fonts-and-characters-that-need-to-be-preserved)

pdf2zh example.pdf -f "(CM\[^RT\].\*|MS.\*|.\*Ital)" -c "(\\(|\\||\\)|\\+|=|\\d|\[\\u0080-\\ufaff\])"

Preview
-------

[](https://github.com/Byaidu/PDFMathTranslate#preview)

[![Image 5: image](https://private-user-images.githubusercontent.com/21212051/365099053-57e1cde6-c647-4af8-8f8f-587a40050dde.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MzE2ODUzMjIsIm5iZiI6MTczMTY4NTAyMiwicGF0aCI6Ii8yMTIxMjA1MS8zNjUwOTkwNTMtNTdlMWNkZTYtYzY0Ny00YWY4LThmOGYtNTg3YTQwMDUwZGRlLnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNDExMTUlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjQxMTE1VDE1MzcwMlomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTVmZGE3ZDM3YmU2YjhmYmUyZTFmOTM3NGFhYzQzOWJiYThjYjZlMzJhYmFlNmUyYWU1YmMxMTQ3YzdjMzQ0MjYmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0In0.jnM0wA6I0rra5AJj85s5RrnOOuXNY3XHIvNntnp8DKk)](https://private-user-images.githubusercontent.com/21212051/365099053-57e1cde6-c647-4af8-8f8f-587a40050dde.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MzE2ODUzMjIsIm5iZiI6MTczMTY4NTAyMiwicGF0aCI6Ii8yMTIxMjA1MS8zNjUwOTkwNTMtNTdlMWNkZTYtYzY0Ny00YWY4LThmOGYtNTg3YTQwMDUwZGRlLnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNDExMTUlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjQxMTE1VDE1MzcwMlomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTVmZGE3ZDM3YmU2YjhmYmUyZTFmOTM3NGFhYzQzOWJiYThjYjZlMzJhYmFlNmUyYWU1YmMxMTQ3YzdjMzQ0MjYmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0In0.jnM0wA6I0rra5AJj85s5RrnOOuXNY3XHIvNntnp8DKk)

[![Image 6: image](https://private-user-images.githubusercontent.com/21212051/375674097-0e6d7e44-18cd-443a-8a84-db99edf2c268.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MzE2ODUzMjIsIm5iZiI6MTczMTY4NTAyMiwicGF0aCI6Ii8yMTIxMjA1MS8zNzU2NzQwOTctMGU2ZDdlNDQtMThjZC00NDNhLThhODQtZGI5OWVkZjJjMjY4LnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNDExMTUlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjQxMTE1VDE1MzcwMlomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTVhNjZkNGUzYjAwZGVjYjI1M2FkNTRjNGM5MWQxNWFhYmY2ZTBkODFiMWRhYmU3YWM3ODc3NWVhNDliYmRlZTMmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0In0.84XV9HoqziBc8XJjd_fHmVpSqjdDSFxyYvCdl43_qlY)](https://private-user-images.githubusercontent.com/21212051/375674097-0e6d7e44-18cd-443a-8a84-db99edf2c268.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MzE2ODUzMjIsIm5iZiI6MTczMTY4NTAyMiwicGF0aCI6Ii8yMTIxMjA1MS8zNzU2NzQwOTctMGU2ZDdlNDQtMThjZC00NDNhLThhODQtZGI5OWVkZjJjMjY4LnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNDExMTUlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjQxMTE1VDE1MzcwMlomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTVhNjZkNGUzYjAwZGVjYjI1M2FkNTRjNGM5MWQxNWFhYmY2ZTBkODFiMWRhYmU3YWM3ODc3NWVhNDliYmRlZTMmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0In0.84XV9HoqziBc8XJjd_fHmVpSqjdDSFxyYvCdl43_qlY)

[![Image 7: image](https://private-user-images.githubusercontent.com/21212051/383060278-5fe6af83-2f5b-47b1-9dd1-4aee6bc409de.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MzE2ODUzMjIsIm5iZiI6MTczMTY4NTAyMiwicGF0aCI6Ii8yMTIxMjA1MS8zODMwNjAyNzgtNWZlNmFmODMtMmY1Yi00N2IxLTlkZDEtNGFlZTZiYzQwOWRlLnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNDExMTUlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjQxMTE1VDE1MzcwMlomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPThiZDBiMmQ3ZTdiYTBmMzRhNWQ4MjJmZWE2OGJlMGQzZmE0ZTljZjliYzUxZDQ3ZWFjZWY2MmM3MDRmNjI5ODkmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0In0.VXsDfiFRdzj-LgvcYd79-6VdgT_Y_D9Qq76O3_5vPcY)](https://private-user-images.githubusercontent.com/21212051/383060278-5fe6af83-2f5b-47b1-9dd1-4aee6bc409de.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MzE2ODUzMjIsIm5iZiI6MTczMTY4NTAyMiwicGF0aCI6Ii8yMTIxMjA1MS8zODMwNjAyNzgtNWZlNmFmODMtMmY1Yi00N2IxLTlkZDEtNGFlZTZiYzQwOWRlLnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNDExMTUlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjQxMTE1VDE1MzcwMlomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPThiZDBiMmQ3ZTdiYTBmMzRhNWQ4MjJmZWE2OGJlMGQzZmE0ZTljZjliYzUxZDQ3ZWFjZWY2MmM3MDRmNjI5ODkmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0In0.VXsDfiFRdzj-LgvcYd79-6VdgT_Y_D9Qq76O3_5vPcY)

Acknowledgement
---------------

[](https://github.com/Byaidu/PDFMathTranslate#acknowledgement)

Document merging: [PyMuPDF](https://github.com/pymupdf/PyMuPDF)

Document parsing: [Pdfminer.six](https://github.com/pdfminer/pdfminer.six)

Document extraction: [MinerU](https://github.com/opendatalab/MinerU)

Multi-threaded translation: [MathTranslate](https://github.com/SUSYUSTC/MathTranslate)

Layout parsing: [DocLayout-YOLO](https://github.com/opendatalab/DocLayout-YOLO)

Document standard: [PDF Explained](https://zxyle.github.io/PDF-Explained/), [PDF Cheat Sheets](https://pdfa.org/resource/pdf-cheat-sheets/)

Contributors
------------

[](https://github.com/Byaidu/PDFMathTranslate#contributors)

[![Image 8](https://camo.githubusercontent.com/59bae6b66d359f7af499230f5e8fa465dff61fc1dacb5bb329c2f84558e6eb77/68747470733a2f2f636f6e747269622e726f636b732f696d6167653f7265706f3d4279616964752f5044464d6174685472616e736c617465)](https://github.com/Byaidu/PDFMathTranslate/graphs/contributors)

Star History
------------

[](https://github.com/Byaidu/PDFMathTranslate#star-history)

  [![Image 9: Star History Chart](https://camo.githubusercontent.com/e36b882836a58c1774ee53f32b25804e087fbcffd76df986b7aa72e2291f735f/68747470733a2f2f6170692e737461722d686973746f72792e636f6d2f7376673f7265706f733d4279616964752f5044464d6174685472616e736c61746526747970653d44617465)](https://star-history.com/#Byaidu/PDFMathTranslate&Date)
