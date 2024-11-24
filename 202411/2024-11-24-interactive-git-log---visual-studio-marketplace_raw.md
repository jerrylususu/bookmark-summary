Title: Interactive Git Log - Visual Studio Marketplace

URL Source: https://marketplace.visualstudio.com/items?itemName=interactive-smartlog.interactive-smartlog

Markdown Content:
> ⚡⚡ **Revolutionize your Git Workflow** ⚡⚡  
> Interactive Git Log (IGL) is the most powerful Git GUI for VSCode, streamlining and enhancing your interaction with Git repositories.

![Image 21: commit](https://www.interactive-git-log.com/img/commit.gif)

**Changes to files in your working copy appear automatically in IGL, just like if you had run `git status`.** Underneath your uncommitted changes, there's a **Commit** button and an **Amend** button. Clicking these buttons opens up the commit form sidebar on the right side, where you can write a detailed commit message.

When you're satisfied with your message, the _Commit_ and _Amend_ buttons at the bottom right will let you create or amend your commit using your message.

🌳 Branches
-----------

**IGL displays a tree view of your commits and branches, starting from where they diverge from the primary remote branch** (usually `origin/main` or `origin/master`).

You can directly click on branch tags to go to them. You can also add, remove, and fetch branches directly from IGL.

![Image 22: branching](https://www.interactive-git-log.com/img/branching.gif)

✨ Uncommitted Changes
---------------------

The color and icon next to files shows you if a file was modified, added, or removed. The opacity of the filename indicates whether or not the file has been staged (via `git add`) for commit. You can click on files to open them.

When you hover over files listed under uncommitted changes, IGL dynamically presents you with a set of actionable buttons. These **buttons run Git commands**, making it effortless to stage or unstage files for commit, revert modifications, or even remove newly added files from the file system without resorting to the command line.

![Image 23: unstaged-changes](https://www.interactive-git-log.com/img/unstaged-changes.gif)

⚔️ Rebasing & Conflict Resolution
---------------------------------

You can hover over a branch to reveal a rebase button. Pressing the button rebases your current branch onto the target branch. When merge conflicts are detected, IGL will add to the list of uncommitted changes a list of unresolved conflicts.

![Image 24: rebase](https://www.interactive-git-log.com/img/rebase.gif)

**After opening each file and resolving the conflict markers, you can click the plus icon next to each file in IGL to mark it as resolved.** When all files have been resolved, you are free to continue the command that led to conflicts.

It is possible to hit merge conflicts multiple times, for example, when rebasing an entire stack of commits, as each commit is checked for conflicts one-by-one.

**While a command is running, you will see progress information at the bottom of the screen.** This is also where you can see error messages if something goes wrong when running a command. IGL shows the arguments used to run commands, so you could replicate the behavior on the CLI if you want to.

🔧 Reorder, Squash, and Drop Commits
------------------------------------

An **Edit stack** button will appear when you are on a branch with multiple commits. Upon clicking _Edit stack_, a dialog will open in which you can reorder, squash, and drop commits. Pressing _Save changes_ triggers IGL runs a git interactive rebase to edit the stack.

![Image 25: rebase](https://www.interactive-git-log.com/img/interactive-rebase.gif)
