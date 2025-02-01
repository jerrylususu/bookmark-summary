Title: Git: avoid reset --hard, use reset --keep instead - Adam Johnson

URL Source: https://adamj.eu/tech/2024/09/02/git-avoid-reset-hard-use-keep/

Markdown Content:
2024-09-02![Image 3: Protect the king, protect the uncommitted changes.](https://adamj.eu/tech/assets/2024-09-02-chess.jpeg)When I started learning Git, I found many references covering two ways to undo commits with `git reset`:

1.  `git reset --soft <commit>`
    
    This mode changes the current branch to point to a new commit but leaves files as they are.
    
2.  `git reset --hard <commit>`
    
    This mode changes the current branch to point at a new commit, resetting all files to the state of that commit.
    

But whilst researching for my book on Git, I discovered [`git reset --keep`](https://git-scm.com/docs/git-reset#Documentation/git-reset.txt---keep) in the documentation. The description there is brief and oblique, but after figuring it out, I realized that `--keep` is way more preferable to `--hard`!

`git reset --hard` is destructive—as destructive as a Git command can be. That’s because it **throws away uncommitted changes**, which Git provides no way to recover.

Git always has the possibility to recover **committed** changes. Normally, this means fetching old commits from the reflog (“reference log”) of a given branch, which has a default expiry of 30 days. In more complicated cases, you might need [`git fsck`](https://git-scm.com/docs/git-fsck). But as long as you commit something, you can recover it.

When `git reset --hard` moves a branch from one commit to another, it updates files to match the new commit. But whilst it does that, it also throws out any uncommitted changes **to any file**.

By contrast, `git reset --keep` keeps any uncommitted changes. It even fails if doing the reset would throw away your precious unsaved work.

An example[](https://adamj.eu/tech/2024/09/02/git-avoid-reset-hard-use-keep/#an-example "Permalink to this headline")
---------------------------------------------------------------------------------------------------------------------

Imagine you had a repository of puzzles with some commits affecting `cloud.svg`:

$ git log \--oneline
f60792a (HEAD -\> main) Solve 3 more pieces of cloud jigsaw
304d197 Solve 53 pieces of cloud jigsaw
...

…with uncommitted changes to `rainbow.svg`:

$ git status
On branch main
Changes not staged for commit:
        modified:   rainbow.svg

no changes added to commit

Then, you run `git reset --hard` to undo the last commit:

$ git reset \--hard 304d197
HEAD is now at 304d197 Solve 53 pieces of cloud jigsaw

Unfortunately, that command throws away your progress on `rainbow.svg` as well! 🌈😭

$ git status
On branch main
nothing to commit, working tree clean

By contrast, if we rerun the same scenario but use `--keep`:

$ git status
On branch main
Changes not staged for commit:
        modified:   rainbow.svg

no changes added to commit

$ git reset \--keep 304d197

$ git show \-s \--oneline
304d197 (HEAD -\> main) Solve 53 pieces of cloud jigsaw

…Git retains the uncommitted changes:

$ git status
On branch main
Changes not staged for commit:
        modified:   rainbow.svg

no changes added to commit

(`git show` step added for illustration since `reset` has no output if `--hard` isn’t used.)

Aliases[](https://adamj.eu/tech/2024/09/02/git-avoid-reset-hard-use-keep/#aliases "Permalink to this headline")
---------------------------------------------------------------------------------------------------------------

If you use Oh My Zsh, [its git plugin](https://github.com/ohmyzsh/ohmyzsh/tree/master/plugins/git) provides `grhk` as an alias for `git reset --keep`.

And if you don’t use it, you can copy it! For example, on Bash/Zsh, add this to your shell profile file:

alias grhk\='git reset --keep'

Fin[](https://adamj.eu/tech/2024/09/02/git-avoid-reset-hard-use-keep/#fin "Permalink to this headline")
-------------------------------------------------------------------------------------------------------

May your uncommitted changes never go missing,

—Adam

* * *

🎉 My book [Boost Your Git DX](https://adamchainz.gumroad.com/l/bygdx) was updated on January 28th!

* * *

One summary email a week, no spam, I pinky promise.

**Related posts:**

*   [Git: the basics of `git bisect`](https://adamj.eu/tech/2024/01/29/git-bisect-basics/)
*   [Git: Undo a rebase with `git reflog`](https://adamj.eu/tech/2023/11/24/git-undo-rebase/)
*   [Git: Show commits that come after](https://adamj.eu/tech/2023/11/02/git-log-commits-after/)

**Tags:** [git](https://adamj.eu/tech/tag/git/)
