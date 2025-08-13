# Just a nice shell script
- URL: https://www.bitecode.dev/p/just-a-nice-shell-script
- Added At: 2025-08-13 14:29:06
- [Link To Text](2025-08-13-just-a-nice-shell-script_raw.md)

## TL;DR


uv安装脚本通过跨Shell兼容性适配、LoongArch等特殊架构检测及依赖检查等技术，确保多系统环境可靠性。虽手动处理参数冗余且代码冗长，但覆盖主流场景及非主流架构，支持多shell路径自动配置，并提醒用户审查脚本安全性以规避风险。

## Summary


- **`curl | bash`安装脚本的现状与挑战**  
  尽管存在安全风险，这种方式仍是安装开发工具的常见手段。`cargo-dist`生成的脚本能自动化下载并配置可执行文件至系统路径，例如ruff的安装脚本`curl -LsSf https://astral.sh/ruff/install.sh | sh`。用户强调需先审查脚本内容，而非盲目信任。

- **uv安装脚本的技术亮点**  
  - **跨Shell兼容性**：通过检测`local`命令是否存在，适配bash/dash/ksh/zsh。若`ksh`无`local`支持，则用`typeset`替代。  
  - **跨系统环境处理**：`get_home`函数通过`USER`、`id -un`及`getent passwd`多途径获取用户家目录，解决部分Linux发行版未设置`HOME`的问题。  
  - **函数模块化设计**：提供`say`/`warn`/`err`日志函数、命令存在性检测(`need_cmd`)等实用工具，增强脚本健壮性。  
  - **依赖检查机制**：初始化阶段强制检查`uname`、`tar`等关键命令是否存在，确保脚本运行环境基础功能完备。

- **架构检测与特例处理**  
  - **LoongArch架构适配**：针对中国Loongson公司自主研发的LoongArch CPU，因旧版ABI与新版UAPI不兼容，脚本嵌入base64编码的汇编二进制程序，通过系统调用检测当前运行环境。  
  - **snap包问题规避**：若检测到通过snap安装的`curl`（路径含`/snap/`），则放弃使用该`curl`，防止其潜在功能异常。

- **路径与安装细节优化**  
  - **多shell路径配置**：通过`shotgun_install_dir_to_path`等函数，将安装目录写入`.bashrc`、`.zshrc`等多类配置文件，确保不同shell环境自动识别新二进制文件。  
  - **参数解析繁琐性**：脚本手动处理参数如`--quiet`/`--verbose`，需手动维护帮助文档，对比Python的`argparse`显冗余，但适应无Python环境的设备。

- **幽默与人性化设计**  
  - 针对`snap`包的嘲讽注释：“Canonical应摒弃snap，转向.deb和flatpak”。  
  - 安装时检测命令路径冲突(`check_for_shadowed_bins`)，避免用户因环境变量优先级导致命令无法生效。

- **总结**  
  uv安装脚本通过大量兼容性适配和边缘情况处理（如老旧系统、特殊架构），展现了高可靠性。虽存在代码冗长、参数处理不便等局限，但其覆盖多数使用场景，甚至支持非主流架构如LoongArch，体现了脚本开发的深度与广度。作者戏称其为“陀螺式的生存策略”——通过持续旋转应对环境的不确定性。
