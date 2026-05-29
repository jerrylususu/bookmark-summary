# Dancing mad with sandboxing
- URL: https://xeiaso.net/blog/2026/dancing-mad-sandboxing/
- Added At: 2026-05-29 14:13:36
- Tags: #read #deepdive

## TL;DR
Kefka是一个Go原生沙箱，模拟操作系统环境，通过虚拟文件系统和WebAssembly技术安全运行不受信任的代码（如AI代理），支持Python等工具，确保隔离与兼容性。

## Summary
这篇文章介绍了作者开发的Go原生沙箱环境Kefka，它模拟了一个操作系统，提供核心工具、Python（通过WebAssembly）等功能，用于安全地运行不受信任的代码（如AI代理）。以下是结构化总结：

### 1. 背景与动机
- **问题起源**：受JavaScript沙箱项目`just-bash`启发，作者希望在Go生态中实现类似功能，以安全地执行命令（如防止`rm -rf /`破坏系统）。
- **核心目标**：创建一个用户空间沙箱，让程序在隔离环境中运行，避免依赖主机系统工具。

### 2. Kefka的设计与实现
- **操作系统类比**：将沙箱视为一个微型操作系统，提供系统调用接口（如文件操作、输入输出），通过`Execer`接口实现命令执行。
- **核心组件**：
  - **Shell引擎**：基于`mvdan.cc/sh/v3`包，提供真实的Shell解释器。
  - **虚拟文件系统**：使用`billy`接口模拟文件操作，支持本地和对象存储（如Tigris S3）。
  - **命令注册**：通过`Execer`接口实现核心工具（如`true`、`false`），确保POSIX兼容性。
- **WebAssembly集成**：通过`wazero`运行时，将Python、jq、ripgrep等工具编译为WASM模块，注入虚拟文件系统和标准I/O。

### 3. 关键技术挑战与解决方案
- **文件系统适配**：从`io/fs`切换到`billy`接口，以更好地支持写操作和对象存储；开发S3到Billy的适配器。
- **WASM限制**：WASI 0.1不支持网络套接字，未来可能集成`wasix`以扩展网络功能。
- **错误处理**：将WASM错误映射为POSIX errno值，确保兼容性。
- **SSH集成**：通过`gliderlabs/ssh`包实现SSH服务器，为每个用户提供隔离的沙箱环境（如`sophia.xeiaso.net`）。

### 4. 应用场景与扩展
- **AI代理安全**：为AI代理提供“小丑监狱”（clown jail），防止恶意命令破坏系统。
- **多工具支持**：已集成Python、jq、ripgrep，并易于扩展其他WASM程序。
- **未来方向**：添加网络栈（如tsnet）、CEL网络过滤，以及会话录制功能。

### 5. 总结
Kefka是一个创新的Go原生沙箱，通过模拟操作系统和WebAssembly技术，实现了安全、隔离的代码执行环境。它不仅适用于AI代理管理，还可扩展至开发工具和云存储集成，展示了用户空间沙箱的潜力。
