# How Core Git Developers Configure Git
- URL: https://blog.gitbutler.com/how-git-core-devs-configure-git/
- Added At: 2025-02-26 14:26:05

## TL;DR
文章探讨了Git的多种配置设置，建议修改某些默认值以提升用户体验，并列出了核心开发人员常用的配置。特别推荐了一些明显提升Git体验的设置，如更好的diff、推送和获取配置。

## Summary
1. **引言**：
   - 作者讨论了Git的`help.autocorrect`设置及其历史，并思考了其他不为人知的`git config`设置，认为这些设置应该有不同的默认值。
   - 作者从核心Git开发人员那里学到了许多配置技巧。

2. **TLDR**：
   - 提供了核心Git开发人员常用的Git配置设置列表，这些设置可以提升Git的使用体验。

3. **核心开发人员的Git配置**：
   - 作者探讨了Git核心开发人员是否认为某些默认值应该更改，并提到了Git邮件列表中的“Spring Cleaning”讨论。
   - 该讨论列出了9个配置设置和3个别名，参与者认为这些应该成为新的默认设置。

4. **配置分类**：
   - **Clearly Makes Git Better**：这些设置明显提升了Git的默认体验，几乎没有缺点。
     - **分支列表**：使用`branch.sort`和`column.ui`设置，使分支按最近提交日期排序，并在列中显示。
     - **默认分支**：设置`init.defaultBranch`为`main`，避免每次初始化仓库时的警告。
     - **更好的diff**：使用`histogram`算法代替默认的`myers`算法，提供更清晰的代码移动差异。
     - **更好的推送**：使用`push.default simple`、`push.autoSetupRemote`和`push.followTags`设置，简化推送流程。
     - **更好的获取**：使用`fetch.prune`、`fetch.pruneTags`和`fetch.all`设置，自动清理已删除的远程分支和标签。

   - **Why the Hell Not?**：这些设置通常无害，偶尔有帮助。
     - **自动纠错提示**：启用`help.autocorrect prompt`，Git会在命令输入错误时提示并猜测你的意图。
     - **提交时显示diff**：启用`commit.verbose`，在提交时显示完整的diff输出，帮助编写提交信息。
     - **重复使用记录的解决方案**：启用`rerere.enabled`和`rerere.autoupdate`，在冲突解决后自动应用相同的解决方案。
     - **全局忽略文件**：设置`core.excludesfile`为`~/.gitignore`，便于管理全局忽略文件。
     - **稍微更好的rebase**：启用`rebase.autoSquash`、`rebase.autoStash`和`rebase.updateRefs`，提升rebase体验。

   - **A Matter of Taste**：这些设置基于个人喜好，可能对某些人有益。
     - **更好的合并冲突**：使用`merge.conflictstyle zdiff3`，在合并冲突时显示更多上下文信息。
     - **更好的pulling**：设置`pull.rebase true`，使`git pull`默认使用rebase而不是merge。
     - **运行fsmonitor进程**：启用`core.fsmonitor`和`core.untrackedCache`，加快大仓库中的`git status`速度。

5. **总结**：
   - 作者希望这些Git配置建议对读者有用，并强调了一些应该成为默认设置的选项。
   - 除了这些配置，作者还提到了其他个性化Git的方法，如使用别名和外部工具。
