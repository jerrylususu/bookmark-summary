# Importing a frontend Javascript library without a build system
- URL: https://jvns.ca/blog/2024/11/18/how-to-import-a-javascript-library/
- Added At: 2024-11-19 16:27:52

## TL;DR
本文介绍了在没有构建系统的情况下如何导入前端JavaScript库，详细说明了不同文件类型（如UMD、ES模块、CommonJS）的使用方法，并推荐了多种工具（如importmaps、esm.sh、download-esm）来帮助开发者实现这一目标。

## Summary
1. **背景**：作者喜欢在没有构建系统的情况下编写JavaScript，但经常遇到需要导入JavaScript库的问题，尤其是在库的设置说明假设用户使用构建系统时。

2. **目标**：本文旨在提供一个在没有构建系统的情况下导入前端JavaScript库的指南。

3. **文件类型**：
   - **经典文件**：定义全局变量，可通过`<script src>`直接使用。
   - **ES模块**：可能依赖其他文件，使用`import`和`export`语法。
   - **CommonJS模块**：主要用于Node.js，浏览器中无法直接使用。

4. **查找文件**：
   - **NPM构建**：所有库都会上传到NPM，即使通过CDN链接使用，文件也源自NPM。
   - **示例1：Chart.js**：
     - **选项1**：`chart.cjs`，CommonJS文件，浏览器中无法直接使用。
     - **选项2**：`chart.js`，ES模块。
     - **选项3**：`chart.umd.js`，UMD文件，可在浏览器中直接使用。
   - **示例2：@atcute/oauth-browser-client**：
     - **index.js**：ES模块，可通过importmaps或直接导入使用。
   - **示例3：@atproto/oauth-client-browser**：
     - **index.js**：CommonJS模块，需通过esm.sh转换为ES模块。

5. **使用方法**：
   - **UMD文件**：直接通过`<script src>`使用。
   - **ES模块**：
     - **无依赖**：直接导入。
     - **有依赖**：使用importmaps或download-esm工具。
   - **CommonJS模块**：通过esm.sh转换为ES模块。

6. **工具与支持**：
   - **Importmaps**：2023年成为主流浏览器支持的标准。
   - **ES模块标准化**：使开发者更放心使用，因为浏览器承诺长期兼容。
   - **工具列表**：
     - **download-esm**：下载并转换ES模块。
     - **esm.sh**和**skypack.dev**：将CommonJS转换为ES模块。
     - **esbuild**：构建工具。
     - **JSPM**：生成importmaps。

7. **总结**：本文旨在帮助开发者在没有构建系统的情况下理解和使用不同类型的JavaScript文件，并介绍了多种工具和方法来实现这一目标。
