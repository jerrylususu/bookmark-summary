# The bottom emoji breaks rust-analyzer
- URL: https://fasterthanli.me/articles/the-bottom-emoji-breaks-rust-analyzer#the-way-forward
- Added At: 2025-04-09 15:01:03
- [Link To Text](2025-04-09-the-bottom-emoji-breaks-rust-analyzer_raw.md)

## TL;DR


该文介绍了在Emacs中配置rust-analyzer时遇到的崩溃问题，当输入UTF-8表情符号（如`🥺`）时，因LSP客户端（lsp-mode）发送非法字节偏移量导致服务端断言失败。解决方案包括：通过软链或配置正确指向rustup管理的最新版本分析器，升级工具链及插件，并确保文本操作符合Unicode字符边界规范。文章强调了编码兼容性和协议规范遵循的重要性。

## Summary


文章介绍了在Emacs环境中配置rust-analyzer时出现的崩溃问题，具体表现为输入特定表情符号（如`🥺`）后语言服务器崩溃。以下是关键点总结：

---

### **问题重现**
1. **初始配置失败**：
   - 用户通过`rustup`安装rust-analyzer，但发现版本较旧（1.67.1），删除后导致无法启动。
   - 默认路径下未找到`rust-analyzer`，需通过`rustup which rust-analyzer`定位到`~/.rustup/toolchains/`目录下的二进制文件。

2. **Emacs配置问题**：
   - `lsp-mode`优先检测到已弃用的`rls`（而非`rust-analyzer`），导致启动失败。
   - 需手动创建软链接或配置路径，使Emacs识别`rustup`管理的版本。

---

### **核心问题：表情符号引发崩溃**
- **触发条件**：在Rust代码中添加包含UTF-8多字节字符的表情符号（如`🥺`）时，rust-analyzer崩溃，堆栈显示断言`self.is_char_boundary(n)`失败。
- **原因分析**：
  - **Unicode编码差异**：
    - Rust采用UTF-8编码，`String`操作必须保证字节偏移量位于字符边界。
    - 表情符号`🥺`的UTF-8编码占4字节（`f0 9f a5 ba`），而客户端可能错误地传递非字符边界偏移量。
  - **LSP客户端问题**：
    - Emacs的`lsp-mode`在文本更新时发送的文本偏移量不合法（如直接使用字节偏移而非字符索引）。
    - `rust-analyzer`未处理这种非法输入，直接触发断言panic。

---

### **LSP协议与Unicode处理**
1. **LSP通信问题**：
   - 客户端（`lsp-mode`）与服务端（`rust-analyzer`）通过JSON RPC通信。当客户端发送`didChange`通知时，若偏移量计算错误，服务端处理文本更新时会因越界导致崩溃。
   - 调试方法：拦截LSP通信（如使用ZIG脚本拦截`rust-analyzer`输出）可捕获具体参数，验证偏移量是否合法。

2. **Rust字符串安全机制**：
   - Rust标准库强制`String`操作必须位于字符边界，例如`replace_range`会检测边界合法性，非法时直接panic。
   - 不安全操作（如直接修改字节）可能导致无效UTF-8，但需要开发者自行保证正确性。

---

### **解决方案**
1. **配置Emacs正确路径**：
   - 手动创建软链接：
     ```bash
     ln -s $(rustup which rust-analyzer) ~/.cargo/bin/rust-analyzer
     ```
   - 或在配置中指定路径：
     ```elisp
     (setq lsp-rust-analyzer-server-command (list (string-trim (shell-command-to-string "rustup which rust-analyzer"))))
     ```

2. **更新工具链与插件**：
   - 使用最新`rust-analyzer`版本，可能包含对LSP偏移量处理的优化。
   - 升级`lsp-mode`和`rustic`插件，确保兼容性。

3. **Unicode编码注意事项**：
   - 避免直接操作字节偏移，应通过Rust的字符迭代器或`graphemes`库进行多字节安全操作。
   - 客户端需确保发送的文本位置基于字符边界而非字节位置。

---

### **结论**
问题源于LSP客户端与服务端对文本编码的不同处理方式，以及旧版rust-analyzer对非法输入的脆弱性。通过路径配置、工具链更新及注意Unicode安全操作，可避免此类崩溃。文章强调跨平台开发中编码兼容性与协议规范遵循的重要性。
