# Makefiles for Web Work
- URL: https://rosszurowski.com/log/2022/makefiles
- Added At: 2024-11-08 14:02:51
- [Link To Text](2024-11-08-makefiles-for-web-work_raw.md)

## TL;DR
`make`是一个历史悠久的构建工具，适用于多种语言项目，具有速度快、语言无关和简单可扩展等优势。它通过Makefile提供一致的命令接口，简化开发流程，但需注意Windows兼容性和复杂构建的管理。

## Summary
1. **`make`工具简介**：
   - `make`是一个自1970年代以来就存在的构建工具，最初设计用于自动化C程序的构建过程，如安装依赖、运行测试和编译二进制文件。
   - 在现代Web项目中，`make`同样可以用于自动化类似步骤，如安装node_modules、运行代码检查和测试、启动开发服务器以及使用esbuild或Rollup编译文件。

2. **自动化工具选择**：
   - 默认选择通常是npm/yarn脚本，这些脚本将shell命令写入项目的`package.json`文件中。
   - 更复杂的项目可能会使用Gulp/Grunt或Docker构建。
   - 作者认为`make`通常能满足许多需求，且使用起来更为简便。

3. **`make`的优势**：
   - **广泛可用**：大多数系统在安装开发工具时会默认安装`make`，无需额外步骤。
   - **速度快**：相比npm/yarn脚本，`make`启动速度快约30倍，符合“快速软件是好软件”的理念。
   - **语言无关**：`make`基于shell脚本工作，不依赖于特定语言或工具链，适用于Go、PHP、Rust、Node等多种项目。
   - **简单且可扩展**：对于小型项目，Makefile的简单结构和依赖跟踪功能恰到好处。

4. **一致的接口**：
   - `make`作为项目脚本的统一接口，有助于在不同项目间创建一致的命令。
   - 作者在每个新项目中添加`make dev`命令，自动下载依赖、启动开发服务器并监视更改，无论项目使用何种语言。

5. **常见命令**：
   - `make dev`：启动带有实时重载的开发服务器。
   - `make build`：构建生产就绪的二进制文件或文件集。
   - `make deploy`：标记CI构建的发布，或通过rsync将文件同步到服务器。
   - `make format`：使用prettier或gofmt格式化所有代码。
   - `make lint`：运行代码质量检查，如eslint或golanglint-ci。
   - `make test`：运行完整的测试套件，有时会包含lint脚本。
   - `make clean`：移除所有构建工件和下载的依赖。
   - `make help`：列出Makefile中的所有命令。

6. **技巧与技术**：
   - **无依赖任务**：使用`.PHONY`标记，确保命令每次运行。
   - **引用node_modules二进制文件**：在Makefile中显式引用`node_modules/.bin`目录中的工具。
   - **自动安装node_modules**：通过定义依赖关系，确保在运行其他命令前安装node_modules。
   - **跳过慢任务的重新运行**：通过定义依赖文件和文件夹，避免不必要的重新构建。
   - **使用环境变量**：在Makefile顶部包含`.env`文件，并导出变量。
   - **配置任务的默认变量**：使用`?=`设置默认变量，允许外部覆盖。
   - **自文档化Makefile**：添加`make help`目标，自动生成命令帮助文档。
   - **并行开发服务器**：使用concurrently等工具处理并行任务。
   - **密封环境**：通过自动下载工具链的本地版本，确保所有团队成员使用相同版本。

7. **局限性**：
   - **Windows兼容性**：Makefile依赖UNIX工具和约定，可能不适用于Windows。
   - **复杂构建**：对于复杂的依赖链，Makefile可能变得难以管理。
   - **现有设置**：如果已有满意的工作流程，无需更换。

8. **参考Makefile**：
   - 提供了几个实际项目中的Makefile示例，展示了如何使用`make`简化开发流程。
