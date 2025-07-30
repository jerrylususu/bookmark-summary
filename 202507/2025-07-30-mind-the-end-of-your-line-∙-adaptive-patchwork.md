# Mind the End of Your Line ∙ Adaptive Patchwork
- URL: https://adaptivepatchwork.com/2012/03/01/mind-the-end-of-your-line/
- Added At: 2025-07-30 13:43:38
- [Link To Text](2025-07-30-mind-the-end-of-your-line-∙-adaptive-patchwork_raw.md)

## TL;DR


Git通过配置处理跨平台行分隔符问题，规定仓库统一使用LF，提交时转换CRLF为LF，检出时根据系统自动转回。核心配置包括`core.autocrlf`（旧系统）和`.gitattributes`（推荐新系统），后者可显式定义文件转换规则，如`*.cs text`强制转换，`binary`标记二进制文件避免误处理。需团队统一配置以避免合并冲突。

## Summary


本文讨论Git中处理行末符（Line Endings）的复杂性和配置方法，解决跨平台（Windows使用CRLF，Unix/Linux/macOS使用LF）协作时因行分隔符差异导致的混乱问题。

### 核心机制
1. **Git存储规范**  
   Git规定仓库对象数据库中所有文本文件应统一使用LF作为行分隔符，避免跨平台协作时的混乱。此规范需通过配置实现，非强制但被广泛采用。

2. **关键配置项**
   - **core.eol**：定义写入工作目录时的行分隔符格式，默认`native`（随操作系统自动选择），也可显式指定`crlf`或`lf`。
   - **对象数据库与工作目录交互**  
     - **写入对象库**：提交时Git会根据配置转换行分隔符。
     - **读取到工作目录**：检出代码时执行反向转换（如Windows下LF转CRLF）。

---

### 旧系统：`core.autocrlf`
- **模式**：
  - `false`：不处理行分隔符，可能导致文件混乱（默认值）。
  - `true`：Windows推荐，提交时LF转CRLF，检出时逆向转换。
  - `input`：Unix推荐，提交时仅处理CRLF→LF，不逆向转换。
- **风险控制**：  
  `core.safecrlf`检测转换可逆性（`true`阻止操作，`warn`仅警告），但依赖Git的二进制文件识别可能误判。

- **文件类型冲突**：  
  可通过`.gitattributes`文件定义特定文件的转换规则（如指定`*.txt crlf`或`-crlf`）。

---

### 新系统（Git 1.7.2+）：`.gitattributes`文件
1. **核心策略**  
   通过仓库内`.gitattributes`文件统一定义转换规则，消除对全局配置的依赖，提升协作性。

2. **关键设置**：  
   - `text`：强制文件转换（CRLF→LF入库，LF→CRLF出库）。  
   - `-text`：禁用转换。  
   - `text=auto`：仅对Git识别为文本的文件自动转换（依赖二进制检测）。  

3. **推荐实践**：  
   显式声明文本文件类型（如`.cs`、`.md`等）并设置转换规则，关键文件示例：
   ```
   *.cs text diff=csharp
   *.png binary
   * text=auto  # 配合后续规则
   ```
   
4. **兼容性**：  
   未明确指定时回退至`core.autocrlf`旧逻辑，但建议优先使用显式配置。

---

### 注意与建议
- 跨平台协作时必须统一处理行分隔符，否则会导致代码对比混乱、合并冲突。
- 新系统更推荐，因其配置与仓库绑定，便于团队标准化。
- 二进制文件需标记为`binary`（即`-text -diff`）避免误处理。
