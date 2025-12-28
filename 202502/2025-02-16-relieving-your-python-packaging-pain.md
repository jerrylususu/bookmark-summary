# Relieving your Python packaging pain
- URL: https://www.bitecode.dev/p/relieving-your-python-packaging-pain
- Added At: 2025-02-16 06:52:36

## TL;DR
文章建议使用较旧的Python稳定版本，通过官方渠道安装，避免使用conda等工具，仅使用pip和venv管理包和虚拟环境，以减少Python打包问题。

## Summary
1. **Python版本选择**：
   - 不要安装最新的Python主要版本。
   - 建议使用较旧的稳定版本，如最新的主要版本是3.11，则最多使用3.10，最低可使用3.7。
   - 参考[Python状态页面](https://devguide.python.org/versions/)查看各版本的维护状态。

2. **安装来源**：
   - 在Windows和Mac上使用[python.org](https://python.org/)的官方安装程序。
   - 在Linux上使用官方仓库的工具（如“apt”、“yum”等）安装Python。
   - 对于Ubuntu用户，可以使用[deadsnake PPA](https://launchpad.net/%7Edeadsnakes/+archive/ubuntu/ppa)扩展可用的Python版本。
   - 对于Red Hat用户，可以使用[EPEL](https://docs.fedoraproject.org/en-US/epel/)。

3. **虚拟环境管理**：
   - 永远不要在虚拟环境之外安装或运行任何Python工具。
   - 仅使用“pip”和“venv”进行包管理。
   - 使用“venv”创建虚拟环境，并明确指定所使用的Python版本。
   - 在虚拟环境中运行所有命令，包括pip。

4. **命令运行方式**：
   - 使用“-m”标志运行Python模块，如`python -m pip install`。
   - 避免直接使用`pip install`或其他命令。

5. **工具限制**：
   - 不要使用conda、poetry、pipenv、pdm、easy_install或pipx。
   - 不要混用conda和其他工具，如pip或venv。

6. **虚拟环境创建命令**：
   - 在Windows上使用`py -3.8 -m venv .venv`。
   - 在Linux和Mac上使用`python3.8 -m venv .venv`。

7. **问题根源**：
   - 大多数Python打包问题并非来自打包本身，而是来自Python的引导（安装、配置和运行）。
   - 遵循上述步骤可以显著减少所谓的“打包问题”。

8. **特殊情况：Anaconda**：
   - 仅在必要时使用Anaconda，并确保所有操作都在Anaconda环境中进行。
   - 使用conda创建和管理虚拟环境，避免使用pip或venv。
