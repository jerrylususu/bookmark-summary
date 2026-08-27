# Copy-on-write git worktrees
- URL: https://commaok.xyz/post/git-cow-worktrees/
- Added At: 2026-08-27 14:37:12
- Tags: #read #tips

## TL;DR
利用文件系统写时复制（reflink）特性，让多个 Git worktree 共享工作文件，从而节省磁盘空间。作者通过先 `--no-checkout` 创建 worktree，再以 reflink 复制已有文件，最后检出完成，并封装为 `git-cow-worktree` 工具。

## Summary
这篇文章介绍了一种节省磁盘空间的技巧，用于管理大量 Git worktree（工作树）。作者以前只使用少数几个 worktree，但现在 worktree 数量像野草一样疯长，占用了大量磁盘空间。虽然 Git worktree 之间会共享 Git 对象（.git 目录里的数据），但每个 worktree 的工作目录（实际检出的文件）是独立的，这本来是 worktree 的核心特性——允许你在不同目录里独立编辑不同的分支或提交。但这也意味着每个 worktree 都会完整复制一份工作文件，文件多的时候磁盘占用会很大。

作者的解决思路是：如果文件系统支持 reflink（写时复制，copy-on-write），比如 macOS 的 APFS 或某些 Linux 文件系统，那么就可以让多个 worktree 的大部分工作文件也共享同一份底层数据，只有在修改文件时才真正复制。这样既能保留 worktree 的独立性，又能大幅减少磁盘占用。

Git 本身并没有直接提供这个功能，但可以手动近似实现。具体步骤是：

1. 使用 `git worktree add --no-checkout` 创建一个新的 worktree，但不立即检出文件。
2. 从另一个内容相似（比如同分支或相近提交）的已有 worktree 中，用支持 reflink 的复制方式（比如 `cp --reflink` 或 APFS 的 clonefile）把 Git 跟踪的文件复制过去。因为 reflink 不实际复制数据，所以速度快且几乎不占额外空间。
3. 然后在这个新 worktree 里运行 `git checkout` 或类似命令，让 Git 完成剩余的检出工作。Git 会检查哪些文件与目标提交一致（不需要动）、哪些不一致或缺失需要更新，并刷新索引。

作者把这个流程封装成了一个命令工具，放在 GitHub 上：`git-cow-worktree`（https://github.com/josharian/git-cow-worktree）。使用这个工具后，虽然当文件很多时，速度会比直接用 `git worktree` 慢一些，但整体上作者很满意，因为它解决了磁盘空间问题。

简单来说，这篇文章的核心就是：利用文件系统的写时复制特性，让多个 Git worktree 共享大部分工作文件，从而节省磁盘空间，同时保持各自独立的编辑能力。
