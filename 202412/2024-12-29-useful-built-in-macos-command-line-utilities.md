# Useful built-in macOS command-line utilities
- URL: https://weiyen.net/articles/useful-macos-cmd-line-utilities/
- Added At: 2024-12-29 12:55:28

## TL;DR
本文介绍了多个实用的macOS命令行工具，涵盖Keychain访问、文件操作、复制粘贴、时间管理、网络测试、防止睡眠、UUID生成等功能。还推荐了图像处理、音频管理、磁盘工具等高级命令，帮助用户更高效地管理和自动化任务。

## Summary
1. **Keychain访问**：
   - 使用`security`命令可以编程方式访问存储在Keychain中的秘密信息。
   - 示例命令：`security find-internet-password -s "https://example.com"`
   - 适用于编写使用本地存储凭证的自动化脚本。
   - 链接：[https://ss64.com/mac/security.html](https://ss64.com/mac/security.html)
   - 额外提示：1Password用户可以使用[1Password CLI](https://developer.1password.com/docs/cli/get-started/)从命令行访问1Password项目。

2. **文件打开**：
   - 使用`open`命令可以从终端打开文件。
   - 示例命令：`open file.txt`
   - 文件将在默认应用程序中打开，类似于在Finder中双击文件。
   - 链接：[https://ss64.com/mac/open.html](https://ss64.com/mac/open.html)

3. **复制和粘贴**：
   - `pbcopy`和`pbpaste`是用于复制和粘贴文本到粘贴板的命令行工具。
   - `pbcopy`将标准输入的内容复制到粘贴板。
     - 示例命令：`echo "Hello, world!" | pbcopy;`
   - `pbpaste`将粘贴板的内容输出到标准输出。
     - 示例命令：`pbpaste`
   - 适用于将数据从文件传输到浏览器或其他GUI应用程序。
   - 链接：
     - [https://ss64.com/mac/pbcopy.html](https://ss64.com/mac/pbcopy.html)
     - [https://ss64.com/mac/pbpaste.html](https://ss64.com/mac/pbpaste.html)

4. **UTC时间**：
   - 使用`date -u`或`TZ=UTC date`可以获取当前的UTC时间。
   - 适用于查看服务器日志等场景。
   - 链接：[https://ss64.com/mac/date.html](https://ss64.com/mac/date.html)

5. **网络速度测试**：
   - 使用`networkQuality`命令可以直接在终端运行网络速度测试。
   - 注意：命令中的“Q”是大写。
   - 链接：[https://ss64.com/mac/networkquality.html](https://ss64.com/mac/networkquality.html)

6. **防止Mac睡眠**：
   - 使用`caffeinate`命令可以防止Mac进入睡眠状态。
   - 示例命令：`caffeinate`
   - 适用于运行服务器等需要保持Mac唤醒的场景。
   - 链接：[https://ss64.com/mac/caffeinate.html](https://ss64.com/mac/caffeinate.html)

7. **生成UUID**：
   - 使用`uuidgen`命令可以生成UUID。
   - 默认输出为大写，可以结合`tr`和`pbcopy`将小写UUID复制到剪贴板。
     - 示例命令：`uuidgen | tr '[:upper:]' '[:lower:]' | pbcopy`
   - 适用于编写需要ID的单元测试。
   - 链接：[https://ss64.com/mac/uuidgen.html](https://ss64.com/mac/uuidgen.html)

8. **其他实用命令**：
   - `mdfind`：在终端中进行Spotlight搜索。
   - `say`：让Mac朗读指定文本。
   - `screencapture`：截屏并保存到文件。
   - `networksetup`：编程方式配置网络设置。
   - 链接：
     - [https://ss64.com/mac/mdfind.html](https://ss64.com/mac/mdfind.html)
     - [https://ss64.com/mac/say.html](https://ss64.com/mac/say.html)
     - [https://ss64.com/mac/screencapture.html](https://ss64.com/mac/screencapture.html)
     - [https://ss64.com/mac/networksetup.html](https://ss64.com/mac/networksetup.html)

9. **更新后的推荐命令**：
   - `sips`：脚本化图像处理系统，用于图像格式转换。
   - `afinfo`：探测音频文件的元数据。
   - `mdls`：探测各种文件的元数据。
   - `afconvert`：音频格式转换。
   - `diskutil`：管理磁盘卷，替代内置的“磁盘工具”应用。
   - `powermetrics`：监控系统功耗。
   - `pmset`：电源管理任务，如自动开关机。
   - `dot_clean`：删除dot_underscore文件，适用于与非Mac机器共享文件。
   - 链接：
     - [https://ss64.com/mac/sips.html](https://ss64.com/mac/sips.html)
     - [https://ss64.com/mac/afinfo.html](https://ss64.com/mac/afinfo.html)
     - [https://ss64.com/mac/mdls.html](https://ss64.com/mac/mdls.html)
     - [https://ss64.com/mac/afconvert.html](https://ss64.com/mac/afconvert.html)
     - [https://ss64.com/mac/diskutil.html](https://ss64.com/mac/diskutil.html)
     - [https://ss64.com/mac/powermetrics.html](https://ss64.com/mac/powermetrics.html)
     - [https://ss64.com/mac/pmset.html](https://ss64.com/mac/pmset.html)
     - [https://ss64.com/mac/dot_clean.html](https://ss64.com/mac/dot_clean.html)

10. **其他资源**：
    - [https://saurabhs.org/advanced-macos-commands](https://saurabhs.org/advanced-macos-commands)
    - [https://notes.billmill.org/computer_usage/mac_os/mac_os_command_line_programs.html](https://notes.billmill.org/computer_usage/mac_os/mac_os_command_line_programs.html)
