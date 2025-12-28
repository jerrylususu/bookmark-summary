# Git: avoid reset --hard, use reset --keep instead - Adam Johnson
- URL: https://adamj.eu/tech/2024/09/02/git-avoid-reset-hard-use-keep/
- Added At: 2025-02-01 00:18:08

## TL;DR
文章介绍了Git中的`reset`命令，重点对比了`--hard`和`--keep`选项。`--hard`会丢弃未提交的更改，存在数据丢失风险，而`--keep`则保留未提交的更改，更安全。建议使用`--keep`并设置别名以提高效率。

## Summary
1. **Git Reset命令概述**：
   - `git reset --soft <commit>`：将当前分支指向新的提交，但不改变工作目录中的文件。
   - `git reset --hard <commit>`：将当前分支指向新的提交，并将工作目录中的文件重置为该提交的状态。

2. **`git reset --keep`的发现**：
   - 在Git文档中发现`git reset --keep`命令，尽管描述简短，但发现其比`--hard`更优。
   - `--keep`命令在重置时保留未提交的更改，避免数据丢失。

3. **`git reset --hard`的风险**：
   - `git reset --hard`是破坏性的，会丢弃所有未提交的更改，且无法恢复。
   - 已提交的更改可以通过reflog或`git fsck`恢复，但未提交的更改一旦丢失则无法找回。

4. **`git reset --keep`的优势**：
   - 保留未提交的更改，避免数据丢失。
   - 如果重置操作会导致未提交的更改丢失，`--keep`会失败，从而保护用户的工作。

5. **示例场景**：
   - 使用`git reset --hard`重置提交时，未提交的更改（如`rainbow.svg`的修改）会被丢弃。
   - 使用`git reset --keep`重置提交时，未提交的更改会被保留，确保工作进度不丢失。

6. **别名设置**：
   - 使用Oh My Zsh的用户可以通过`grhk`别名快速调用`git reset --keep`。
   - 其他用户可以通过在shell配置文件中添加`alias grhk='git reset --keep'`来创建别名。

7. **总结与建议**：
   - 建议使用`git reset --keep`代替`git reset --hard`，以避免未提交更改的丢失。
   - 通过设置别名简化命令输入，提高工作效率。

8. **相关资源**：
   - 作者的书《Boost Your Git DX》提供了更多Git使用技巧。
   - 相关文章链接提供了更多Git命令的使用指南，如`git bisect`、`git reflog`等。
