Title: Git experts should try Jujutsu · pksunkara

URL Source: https://pksunkara.com/thoughts/git-experts-should-try-jujutsu/

Markdown Content:
Jul 3, 2025 · 4 min  · [git](https://pksunkara.com/tags/git/)[jujutsu](https://pksunkara.com/tags/jujutsu/)

I've been a **Git** command-line power user for a long time. For me, Git isn't just a tool for pulling and pushing code. It's a finely-tuned instrument for crafting history. I'm the person who will meticulously clean up my commit history before submitting a pull request. My toolkit is full of commands like `git rebase -i`, `git add -i`, `git commit --fixup`, and `git reset --hard`. I can reorder, squash, and reword commits in my sleep. If something goes wrong, I know how to use the `reflog` to get myself out of any mess. I don't just use Git, I speak it fluently. I even have _many many_ custom [git aliases](https://gist.github.com/pksunkara/988716) to make my workflow faster.

So when I first heard about **Jujutsu**, I was skeptical. The main selling point I saw was that it was much simpler than Git. It felt like a tool designed to shield beginners from Git's sharp edges, not something for a seasoned expert like me.

I gave the [tutorial](https://steveklabnik.github.io/jujutsu-tutorial) a quick look, but it didn't showcase any real benefits for my workflow. It confirmed my bias: this was for people who were afraid of Git's power, not for those who had already mastered it.

But the idea lingered. On a whim, I decided to install it on my work machine and used it on a complex project. That's when everything changed. I discovered that Jujutsu wasn't about _avoiding_ history manipulation. It was about making it faster, easier, and more intuitive than I ever thought possible. It took the concepts I had mastered in Git and gave them a superior interface.

[](https://pksunkara.com/thoughts/git-experts-should-try-jujutsu/#comparison) Comparison
----------------------------------------------------------------------------------------

Here are a few examples of how Jujutsu streamlined tasks that were already second nature to me in Git.

### [](https://pksunkara.com/thoughts/git-experts-should-try-jujutsu/#editing-an-old-commit) Editing an old commit

This is a classic scenario. You've spotted a typo or a small bug in a commit from five changes ago.

**In Git:** You start an interactive rebase, find the commit, mark it for editing, make your changes, amend the commit, and finally, continue the rebase.

```
# Find the commit in the log
git log --oneline
# Start the interactive rebase
git rebase -i HEAD~5 # And mark the commit you want to edit
# Make your code changes
vim lib/edit.ts
# Amend the commit
git add .
git commit --amend
# Finish the rebase
git rebase --continue
```

**In Jujutsu:** You simply tell it which change you want to edit. It checks it out, you make your changes, and you're done. Jujutsu handles the rebase automatically in the background.

```
# Find the change id
jj log
# Edit the change directly
jj edit <change-id>
# Make your code changes...
vim lib/edit.ts
```

There's no interactive editor, no `--continue` step. It's direct and to the point.

### [](https://pksunkara.com/thoughts/git-experts-should-try-jujutsu/#splitting-a-commit) Splitting a commit

You've just realized you bundled two unrelated changes into a single commit.

**In Git:** This requires another interactive rebase, mark it for editing, reset it to unstage the changes, and then carefully using `git add -p` to rebuild the commits piece by piece.

```
# Start the interactive rebase
git rebase -i <commit>^ # And mark the commit you want to edit
# Reset the commit but keep the changes in the working directory
git reset HEAD^
# Interactively add the first set of changes
git add -p
git commit -m "First part"
# Add the remaining changes
git add .
git commit -m "Second part"
# Finish the rebase
git rebase --continue
```

**In Jujutsu:** A single command initiates an interactive diff editor, allowing you to decide what to keep in the original commit and what to move to a new one.

```
jj split <change-id>
# This creates two new commits. You can then use `jj describe` to edit the commit messages.
```

This is far more intuitive and significantly faster.

### [](https://pksunkara.com/thoughts/git-experts-should-try-jujutsu/#creating-a-quick-pr) Creating a quick PR

**In Git:** The standard procedure is to create a branch, commit your changes, push that branch, and then open a pull request on your hosting platform.

```
# Create a new branch
git checkout -b my-feature-branch
# Make your changes
vim lib/edit.ts
# Stage and commit your changes
git add .
git commit -m "My feature"
# Push the branch to the remote
git push origin my-feature-branch
# Create a pull request
gh pr create
```

**In Jujutsu:** You can push your current change directly to the remote, which Jujutsu will place on a new branch for you. No need to manage local branches.

```
# Start a new change
jj new -m "My feature"
# Make your changes
vim lib/edit.ts
# Push the change to the remote
jj git push --change @
# Create a pull request
gh pr create --head <created-bookmark-name>
```

[](https://pksunkara.com/thoughts/git-experts-should-try-jujutsu/#conclusion) Conclusion
----------------------------------------------------------------------------------------

After years of honing my Git skills, I thought I had reached peak efficiency. Jujutsu proved me wrong. It's not a replacement for understanding how version control works. It's a force multiplier for those who already do. Jujutsu automates the tedious mechanics of history editing, letting you focus on the _what_ instead of the _how_.

If you're a Git expert who prides yourself on your ability to manipulate history, I urge you to give Jujutsu a serious try on a real project. You might just find that your favorite power tools have been upgraded.

And yes, I've already started a new list of [jj aliases](https://gist.github.com/pksunkara/622bc04242d402c4e43c7328234fd01c) to make my workflow even faster.
