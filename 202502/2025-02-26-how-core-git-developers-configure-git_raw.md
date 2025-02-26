Title: How Core Git Developers Configure Git

URL Source: https://blog.gitbutler.com/how-git-core-devs-configure-git/

Published Time: 2025-02-22T08:23:09.000Z

Markdown Content:
A few weeks ago I [wrote about](https://blog.gitbutler.com/why-is-git-autocorrect-too-fast-for-formula-one-drivers/) Git’s `help.autocorrect` setting and the strange tale of the origin of it’s deciseconds value.

It got me to thinking about other `git config` settings that most people likely don’t know about and which should probably be defaulted differently.

In this post, I’ll go through some of the perhaps obscure Git config settings that I have personally globally enabled and go into them to explain what they do and why they should _probably_ be the default settings.

Also, it turns out that I learned most of these from the people who actually work on the core Git codebase every day.

TLDR
----

First, though, some of you may not particularly care about the wonderful and sordid history of the `rerere` values or whatever. You may just be thinking “just give me the settings so I can blindly throw them into my `~/.gitconfig` file."

Well, fair enough. Here is the fun stuff:

```
# clearly makes git better

[column]
        ui = auto
[branch]
        sort = -committerdate
[tag]
        sort = version:refname
[init]
        defaultBranch = main
[diff]
        algorithm = histogram
        colorMoved = plain
        mnemonicPrefix = true
        renames = true
[push]
        default = simple
        autoSetupRemote = true
        followTags = true
[fetch]
        prune = true
        pruneTags = true
        all = true

# why the hell not?

[help]
        autocorrect = prompt
[commit]
        verbose = true
[rerere]
        enabled = true
        autoupdate = true
[core]
        excludesfile = ~/.gitignore
[rebase]
        autoSquash = true
        autoStash = true
        updateRefs = true

# a matter of taste (uncomment if you dare)

[core]
        # fsmonitor = true
        # untrackedCache = true
[merge]
        # (just 'diff3' if git version < 2.3)
        # conflictstyle = zdiff3 
[pull]
        # rebase = true
```

Copypasta, my friends.

How do Git core devs configure their Gits?
------------------------------------------

Before I dig into these one by one, there is an interesting question about if even the core Git developers think that some of these default values should be changed.

This came up not too long ago on the Git mailing list, and honestly, a few of these settings I personally learned from [this thread](https://lore.kernel.org/git/60b5d281552d6_e359f20828@natae.notmuch/?ref=blog.gitbutler.com) called "Spring Cleaning" where Felipe Contreras challenged the Git core team to remove all their built up config options and aliases and see what it’s like to use Git stock, out of the box.

He challenged the list to pay attention to what settings they really wanted to change and share the top settings changes that seemed the most important with the list.

The [results](https://lore.kernel.org/git/60df97ed24687_34a92088a@natae.notmuch/?ref=blog.gitbutler.com) were very interesting, a rather concise list of 9 config settings and 3 aliases that the experiment participants more or less agreed should arguably be new defaults. Let's just take a look at the proposed config setting changes.

```
merge.conflictstyle = zdiff3
rebase.autosquash = true
rebase.autostash = true 
commit.verbose = true
diff.colorMoved = true
diff.algorithm = histogram
grep.patternType = perl
feature.experimental = true
branch.sort = committerdate
```

Now, _none_ of these have become the new defaults in the 3 or 4 years since this experiment, but it’s interesting that a lot of the Git developers themselves have a hard time using Git without several of these turned on.

Even more interesting is that _most of you_ probably don’t know what _any_ of these do.

So, let’s dig into them. What do these do and why should you almost certainly blindly trust me and go ahead and enable them?

I'm going to group these settings into three categories:

*   [Clearly Makes Git Better](https://blog.gitbutler.com/how-git-core-devs-configure-git/#clearly-makes-git-better)
*   [Why the Hell Not?](https://blog.gitbutler.com/how-git-core-devs-configure-git/#why-the-hell-not)
*   [A Matter of Taste](https://blog.gitbutler.com/how-git-core-devs-configure-git/#a-matter-of-taste)

Let's get started.

Clearly Makes Git Better
------------------------

This first group of settings _clearly_ makes Git better by default. There are generally zero downsides to enabling any of them.

Listing branches
----------------

I noted this in a previous blog post here about Git Tips under “[Branch Stuff](https://blog.gitbutler.com/git-tips-2-new-stuff-in-git/#some-git-branch-stuff)” but as this was also in the Spring Cleaning list, I think everyone agrees that listing out Git branches should probably not be alpha-ordered by default.

The two settings which help improve this are `branch.sort` and `column.ui`. The first of which sorts the list by the most recent commit date (so probably more interesting at the top) rather than by alpha order. The second will put the branch names in a column format so you can see more per screen.

```
git config --global column.ui auto
git config --global branch.sort -committerdate
```

The `column.ui` setting also affects the output of other listing commands (clean, status, tag), but generally I think it’s better than the default.

![Image 1](https://blog.gitbutler.com/content/images/2025/02/CleanShot-2025-02-21-at-08.04.03@2x.png)

You can also sort by other things than committer date, but I think it’s pretty clearly the most useful one.

Speaking of listing things, it’s also pretty ridiculous that this isn’t the default for listing tags, since it’s what nearly everyone actually wants.

Normally, if you list tags by alpha order, you’ll get something like this:

```
$ git tag
nightly/0.5.100
nightly/0.5.1000
nightly/0.5.1001
nightly/0.5.101
nightly/0.5.1010
```

Nobody wants `0.5.101` to come after `0.5.1000`, but that’s alpha order. You can fix this by setting this:

```
git config --global tag.sort version:refname
```

Which will generally do what you expect, treating dotted version numbers as a series of integer values for sorting purposes. Trust me, just enable this.

Default branch
--------------

This one may be a little more controversial, since it can be argued to be somewhat political, but there should be a default branch name in Git where it doesn’t complain every time you `init` a new repo.

```
git config --global init.defaultBranch main
```

Personally, I don’t have a problem with `master` and most of my repositories use that since that used to be the default, but I’m also fine with `main`, so whatever it is you want to use, just go ahead and set it.

Mostly what I find stupid is that now Git is annoying about this rather than just updating the default value. I wish Git had some taste here, but they don't, so you should just set it to something you find reasonable. But whatever.

Better diff
-----------

There is actually a whole blog post that could be written about `git diff` algorithms, but the short story is that by default Git will use an old, fast, pretty reliable diff algorithm called "myers diff".

To give you a sense of what ‘old’ means, it was first published in a paper in 1986, so it’s almost 40 years old now. If you’re as old as I am, perhaps I can give you some childhood perspective as to what that means. The movies ‘The Three Amigos’, ‘An American Tail’ and the first ‘Highlander’ came out in theaters that year.

In any case, some advances have been made since then (with some tradeoffs too) and it may surprise you to know that Git actually ships with 4 built in diff algorithms it can use: `myers`, `minimal`, [`patience`](https://blog.jcoglan.com/2017/09/19/the-patience-diff-algorithm/?utm_source=chatgpt.com) and `histogram`.

Almost certainly what you want to be using is the `histogram` algorithm (an incremental improvement on ‘patience’), rather than the default of 'myers'. You can globally change it like this:

```
git config --global diff.algorithm histogram
```

Here is an example of simple code movement diffed in `myers` vs `histogram`, to give a short taste of how it can be a bit smarter:

Let's say we move a css class below a similar one, change it a little, and then run `git diff` with the default `myers` algorithm. We may get something like this:

![Image 2](https://blog.gitbutler.com/content/images/2025/02/CleanShot-2025-02-20-at-16.07.58@2x.png)

Ok, a little confusing. Here is what `histogram` would give us in the same scenario:

![Image 3](https://blog.gitbutler.com/content/images/2025/02/CleanShot-2025-02-20-at-16.08.28@2x.png)

It's a bit more clear here what's actually happened.

As recently as last year, Elijah (of our [Git Merge fame](https://www.youtube.com/watch?v=KXPmiKfNlZE&ref=blog.gitbutler.com)) suggested that  
[histogram or patience](https://lore.kernel.org/git/CABPp-BEmgOAj17DozyXNaf-9CawDic4uTpMbckef3+zHf7URqQ@mail.gmail.com/?ref=blog.gitbutler.com) might make better defaults, in addition to Felipe's Spring Cleaning suggestion of the same thing, but in reality it’s unlikely to get through the gauntlet anytime soon.

That’s a big one, but there are also a few more smaller tweaks you can make to `git diff`:

```
git config --global diff.colorMoved plain
git config --global diff.mnemonicPrefix true
git config --global diff.renames true
```

The `colorMoved` was also in the Spring Cleaning suggestion list, so it also should probably be a default change.

Here is an example of the previous code movement with the `colorMoved` turned on:

![Image 4](https://blog.gitbutler.com/content/images/2025/02/CleanShot-2025-02-20-at-16.14.15@2x.png)

You can see actually the difference between the moved code and the added line. With `colorMoved` it will show code movement in different colors then added and removed lines.

The `diff.renames` option will detect if a file has been renamed, which is generally good (if slightly more expensive) and `diff.mnemonicPrefix` will replace the `a/` and `b/` in your diff header output with where the diff is coming from, so `i/` (index), `w/` (working directory) or `c/` commit.

So if I diff a change in my index to my working directory I get this as my diff header instead:

```
❯ git diff
diff --git i/apps/web/page.js w/apps/web/page.js
index 7568be2ef..b9e9a00d7 100644
--- i/apps/web/page.js
+++ w/apps/web/page.js
```

A little difficult to see in this example perhaps, but you can tell which side is from the index and which is from the working directory by the leading path names. It’s really subtle, but I like it.

Better pushing
--------------

One of the things that has continued to confuse and frustrate me since the very early days of Git is setting up tracking branches properly. When I push, where does it push, or does it push at all?

There are three updated push settings that I think make for a much nicer default experience. The first (`push.default simple`) has been the new default since Git 2.0, but the others still need to be set explicitly.

```
git config --global push.default simple # (default since 2.0)
git config --global push.autoSetupRemote true
git config --global push.followTags true
```

This has always been a bit of a pain in Git. The new `simple` default is built more or less for centralized workflows and by default pushes the current branch to the same name on the remote. I think this is a pretty sensible default.

However, if that branch does not exist and there is no tracking branch setup, you’ll still get this error:

```
$ git push
fatal: The current branch my-branch-name has no upstream branch.
To push the current branch and set the remote as upstream, use

    git push --set-upstream origin my-branch-name
```

I have to imagine that you have all seen this roughly _one million_ times.

If you set `push.autoSetupRemote` to true, then you won’t get this error anymore. If the upstream is not set, it will automatically set it. I cannot tell you how much I love this setting.

Finally, the `push.followTags` setting will push all tags that you have locally that aren’t on the server, every time you push anything. I’ve been bitten by this a few times - if you ever create tags locally, set this up so you don’t have to worry about other people not seeing them.

Better fetching
---------------

It can be argued that it’s nice to keep some historical local copies of branches and tags that used to be on the server but are not any longer, but I don’t really buy that.

Personally, I think the default behavior of Git should be to make your remote references as close to what is on the remote as possible. Prune stuff that’s gone, etc.

So, I think these fetch settings should be the default:

```
git config --global fetch.prune true
git config --global fetch.pruneTags true
git config --global fetch.all true
```

Really all that this does is make sure we delete `origin/blah` if `blah` is deleted on the server, and also do it automatically for all the remotes that we have configured. Seems pretty reasonable to me.

Why the Hell Not?
-----------------

This next batch of settings are generally harmless and occasionally helpful.

I’m not sure I would necessarily change the defaults, but I also don’t think it would hurt anyone and in many cases would be more helpful, so I’m including them in my list.

Autocorrect prompting
---------------------

As I explained in great length in my [previous post](https://blog.gitbutler.com/why-is-git-autocorrect-too-fast-for-formula-one-drivers/), there is a rather nice feature in Git where if your fingers trip up while typing a command, it will guess what you meant and try to run it.

The default is to not do this at all. What I rather prefer is to guess and prompt you.

```
git config --global help.autocorrect prompt
```

If you want to read about this setting, it’s reasoning and it’s history ad nauseam, I have [just the post for you](https://blog.gitbutler.com/why-is-git-autocorrect-too-fast-for-formula-one-drivers/).

Commit with diffs
-----------------

This was also one of the suggestions in the Spring Cleaning list, I think mostly because it just adds more information to the context you can reference when you write your commit message in your editor.

By default, a `git commit` will give you a message that looks something like this:

![Image 5](https://blog.gitbutler.com/content/images/2025/02/CleanShot-2025-02-20-at-17.03.26@2x.png)

Where there is just a list of files that were changed. If you set `commit.verbose` to be true, it will put the whole `diff` output in there for you to reference as you write your message.

```
git config --global commit.verbose true
```

Here’s what it looks like now when you go to commit:

![Image 6](https://blog.gitbutler.com/content/images/2025/02/CleanShot-2025-02-20-at-17.01.54@2x.png)

All of this will be removed from the commit message (everything under the hilarious `-- >8 --` "scissors" line), but it can give you much more context in writing your message.

Reuse recorded resolutions
--------------------------

This setting is only useful if you’re doing rebases with conflicts over and over again. It’s not the most common situation, but there is not really an issue if it’s turned on and never used.

```
git config --global rerere.enabled true
git config --global rerere.autoupdate true
```

The `enabled` option will make sure it records the before and after states of rebase conflicts and the `autoupdate` will automatically re-apply the resolutions if it sees them again. I wrote about this at some length [over here](https://blog.gitbutler.com/git-tips-1-theres-a-git-config-for-that/#reuse-recorded-resolution), so I won’t bore you with the recap any further.

Global ignore file
------------------

This is pretty dumb, but as there is a `~/.gitconfig` file with global values, it would be cool if there were a `~/.gitignore` file with global values. This setting accomplishes that:

```
git config --global core.excludesfile ~/.gitignore
```

In reality, this is sort of unnecessary, since Git will already look for global ignore values in the following two places: `~/git/ignore` and `~/.config/git/ignore` but since those are a little obscure, I feel like it’s nice to have this more guessable path.

Slightly nicer rebase
---------------------

This section mostly has to do with the use case where you're fixing up and squashing your commits. If you don't know what that is, please check out our previous blog post on [autosquashing](https://blog.gitbutler.com/git-autosquash/).

However, if you are squashing and rebasing a lot (or even occasionally), these settings could help and certainly won't hurt things.

```
git config --global rebase.autoSquash true
git config --global rebase.autoStash true
git config --global rebase.updateRefs true
```

The `updateRefs` setting should almost certainly be a default, honestly. It just takes stacked refs in a branch and makes sure they're also moved when a branch is rebased.

If you want to learn a tiny bit more about how to use fixup, autosquash and updateRefs, it's probably easiest to watch a few minutes of a talk where I go over it here:

A Matter of Taste
-----------------

The next group is based on your personal taste, but most people don’t know they exist and a lot of people may find them useful. They are commented out in my TLDR settings.

Better merge conflicts
----------------------

So, while this is brought up in the Spring Cleaning thread as something that might want to be the new default, I'm not sure that all of you would agree.

When you have a merge conflict in Git, instead of inserting the conflict markers from left and right, you can ask it to insert what the base of it looked like too. Sometimes this can be really useful, but some people can find it pretty annoying.

```
git config --global merge.conflictstyle zdiff3
```

There have been discussions on the Git mailing list to make this the default and actually GitButler uses the `diff3` strategy when dealing with merge conflict markers and to be totally honest, not all of us love it.

Here is an example of a simple merge conflict marker you might get in a file when doing a merge or rebase:

![Image 7](https://blog.gitbutler.com/content/images/2025/02/CleanShot-2025-02-21-at-11.47.34@2x.png)

With the `merge.conflictStyle zdiff3` setting, it would look like this:

![Image 8](https://blog.gitbutler.com/content/images/2025/02/CleanShot-2025-02-21-at-11.48.36@2x.png)

Essentially, in addition to the `<<<<<<` and `>>>>>>` sections that show you how you changed the block and how the other person changed it, it adds a `|||||||` block that shows you what the block looked like before either of you changed it.

That extra context (what that section looked like before either side modified it) can sometimes be super useful, but often it's just more data and somewhat confusing.

Really, it's up to you if you prefer more data there.

⚠️

Git has nearly always had `diff3` as a strategy. I'm recommending `zdiff3` here, which stands for "__zealous diff3__" and is slightly better, but only available since Git 2.35 (Jan 2022). If you have an older Git version, just remove the "z".

Better pulling
--------------

The merge versus rebase debate is of course one that may never be agreed upon, but most of us have a preference. However, you may not know that you can set the `git pull` default so that it will only do one or the other. No need for `git pull --rebase`, you can make it the default:

```
git config --global pull.rebase true
```

This is a personal decision, but as I’ve migrated to the rebase only camp recently, it is in fact in my config.

Run the fsmonitor processes
---------------------------

Again, this is really only a thing for larger repositories, and maybe you don’t want filesystem monitors running all over the place, but it can make things like `git status` much faster if you have big working directories.

Maybe it shouldn’t be a default, but it’s not very bad and can make a big difference. Maybe `git clone` should ask you if you want to set it or not. Whatever, it’s an option for you.

```
git config --global core.fsmonitor true
git config --global core.untrackedCache true
```

This will run a filesystem monitor (per repository) that notices file changes and updates a cache so that `git status` doesn’t have to crawl every file and see if anything changed via a thousand `mtime` stat calls, it can just look at a simple log of file changes.

⚠️

Be aware that this will run a single process __per repository__ that you are active in, which can be a lot. They mostly don't do much as they're event based, so it shouldn't affect memory or CPU noticeably, even with hundreds of them, but it's something to keep in mind. You can also leave out the `--global` and just enable it for your larger repos.

Final thoughts
--------------

Hopefully this has been a useful reference and maybe you learned some new Git config things, some of which should almost certainly already be the defaults, which isn’t even a controversial option in the Git mailing list community.

There are lots of other ways to pimp your Git ride (aliases, cool external [pager](https://github.com/dandavison/delta?ref=blog.gitbutler.com) and [diff](https://github.com/so-fancy/diff-so-fancy?ref=blog.gitbutler.com) tools, things like that) but I thought it would be best to just stick to globally useful and relatively simple vanilla Git settings.

Hope you enjoyed this and see you next time!
