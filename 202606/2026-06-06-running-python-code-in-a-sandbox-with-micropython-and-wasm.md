# Running Python code in a sandbox with MicroPython and WASM
- URL: https://simonwillison.net/2026/Jun/6/micropython-in-a-sandbox/
- Added At: 2026-06-06 06:50:51
- Tags: #read #agent #security

## TL;DR
作者开发了 micropython-wasm 包，基于 MicroPython 和 WebAssembly 实现 Python 代码的安全沙箱执行，支持资源限制与会话持久化，目前已在 PyPI 发布 alpha 版本并用于 Datasette 项目。

## Summary
作者开发了一个名为 micropython-wasm 的 Python 包，用于在 WebAssembly 沙箱中安全执行 Python 代码，以满足其开源项目（如 Datasette）对插件系统安全性的需求。该方案基于 MicroPython 编译为 WebAssembly，利用 wasmtime 运行时实现内存和 CPU 限制、文件与网络访问控制，并支持暴露主机函数。通过多线程和队列机制，实现了会话状态的持久化，允许变量和函数在多次代码执行间保持驻留。目前该包以 alpha 版本发布在 PyPI，作者已将其用于 Datasette Agent 的插件中，并进行了初步安全测试，但建议用户谨慎使用。
