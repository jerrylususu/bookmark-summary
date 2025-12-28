# Using `make` to compile C programs (for non-C-programmers)
- URL: https://jvns.ca/blog/2025/06/10/how-to-compile-a-c-program/
- Added At: 2025-06-11 14:32:58

## TL;DR


本文总结了跨平台编译C/C++程序的步骤：安装编译器（Linux用apt，Mac需Xcode或Homebrew）、管理依赖项（注意跨平台包名差异）、运行配置脚本生成Makefile、使用`make -j`加速编译、通过`CPPFLAGS`和`LDLIBS`环境变量解决依赖路径问题（如Mac需指定/opt/homebrew路径），以及手动安装二进制文件。建议开发者通过基础编译参数处理问题，而非深入复杂工具细节。

## Summary


1. 安装C编译器：  
   - Linux（如Ubuntu）：通过`sudo apt-get install build-essential`安装GCC、G++和Make。  
   - Mac：需安装Xcode命令行工具或通过Homebrew安装相关依赖。

2. 安装程序依赖项：  
   - C/C++依赖需自行管理，通常依赖项由包管理器提供。  
   - README通常说明依赖名称（如`libqpdf-dev`），但需注意跨平台差异，例如Linux下的包名可能无法直接在Mac的Homebrew中使用。

3. 运行`./configure`（若存在）：  
   - 部分程序（如SQLite）使用Autotools生成`Makefile`，运行该脚本时可能因依赖缺失导致失败。  
   - 作者未深入Autotools细节，通常只需直接执行，或调整参数生成不同配置的`Makefile`。

4. 执行`make`编译：  
   - 可通过`make -j8`并行编译加速过程。  
   - 通常会输出大量编译警告，但作者建议忽略（非开发者无需处理）。

5. 解决编译错误：  
   - 大多因依赖未正确链接导致，需通过环境变量配置编译器和链接器路径。  
   - `CPPFLAGS`：用于传递头文件路径（如`-I`参数）给编译器。  
   - `LDLIBS`：用于传递库文件路径（`-L`）及库名称（如`-lqpdf`）给链接器。  
   - 示例：`CPPFLAGS="-I/opt/homebrew/include" LDLIBS="-L/opt/homebrew/lib -liconv" make paperjam`解决了Mac上库路径未识别的问题。

6. 安装二进制文件：  
   - 若`Makefile`提供`install`目标，可运行`make install`，但需注意文件存放位置。  
   - 作者倾向手动复制二进制文件（如`cp qf ~/bin`）而非使用`make install`。

额外技巧：  
   - 编译单个文件：通过`make $FILENAME`快速构建（如编译`qf`仅需`make qf`）。  
   - 参考其他包管理系统的构建配置：例如，Nix包中的`env.NIX_LDFLAGS`提示Mac需添加`-liconv`链接参数。  
   - 依赖差异：Mac的库文件可能位于`/opt/homebrew/lib`等非默认路径，需手动指定。  

注意事项：  
   - C编译与链接紧密相关，依赖问题需区分头文件（编译阶段）和库文件（链接阶段）。  
   - 非C程序员可通过理解基础概念（如头文件、编译器/链接器标志）进行编译，无需深入Autotools等工具。  
   - 动态链接路径配置（如`DYLD_LIBRARY_PATH`）未提及，因作者较少遇到相关问题。
