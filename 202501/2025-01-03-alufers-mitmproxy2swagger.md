# alufers/mitmproxy2swagger
- URL: https://github.com/alufers/mitmproxy2swagger
- Added At: 2025-01-03 15:33:27
- [Link To Text](2025-01-03-alufers-mitmproxy2swagger_raw.md)

## TL;DR
mitmproxy2swagger是一个自动化工具，可将mitmproxy捕获的流量或浏览器导出的HAR文件转换为OpenAPI 3.0规范，逆向工程REST API。支持Python和Docker安装，提供详细的安装和使用指南，开发者可通过poetry和pytest进行依赖管理和测试。项目采用MIT许可证。

## Summary
1. **项目简介**：
   - **mitmproxy2swagger**：一个自动化工具，用于将mitmproxy捕获的流量转换为OpenAPI 3.0规范，从而逆向工程REST API。

2. **新功能**：
   - **HAR支持**：新增支持处理从浏览器DevTools导出的HAR文件。

3. **安装指南**：
   - **依赖**：需要Python3和pip3。
   - **安装命令**：
     - `pip install mitmproxy2swagger`
     - `pip3 install mitmproxy2swagger`
     - 通过Docker安装：
       - `git clone git@github.com:alufers/mitmproxy2swagger.git`
       - `cd mitmproxy2swagger`
       - `docker build -t mitmproxy2swagger .`

4. **使用说明**：
   - **mitmproxy**：
     - **捕获流量**：使用mitmproxy工具捕获HTTP流量，推荐使用mitmweb。
     - **保存流量**：将捕获的流量保存为flow文件。
     - **首次运行**：使用`mitmproxy2swagger`命令生成初始schema文件。
     - **编辑schema**：手动编辑生成的schema文件，移除`ignore:`前缀。
     - **二次运行**：再次运行`mitmproxy2swagger`以生成完整的API描述。
   - **HAR**：
     - **捕获和导出**：从浏览器DevTools捕获并导出HAR文件。
     - **处理HAR**：使用`mitmproxy2swagger`处理HAR文件，步骤与mitmproxy相同。

5. **示例输出**：
   - **生成文件**：包括生成的schema文件和通过redoc-cli生成的HTML文档。
   - **查看示例**：可以在项目仓库的`example_outputs`目录下查看示例输出。

6. **开发与贡献**：
   - **工具**：
     - **依赖管理**：使用poetry。
     - **代码格式化**：使用pre-commit。
     - **单元测试**：使用pytest。
   - **命令**：
     - **运行linters**：`pre-commit run --all-files`
     - **安装pre-commit hooks**：`pre-commit install`
     - **运行测试**：`poetry run pytest`
     - **运行测试并生成覆盖率报告**：`poetry run pytest --cov=mitmproxy2swagger`

7. **许可证**：
   - **MIT许可证**：项目采用MIT许可证。
