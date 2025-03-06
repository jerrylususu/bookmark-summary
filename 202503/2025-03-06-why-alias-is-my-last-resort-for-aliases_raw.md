Title: Why "alias" is my last resort for aliases

URL Source: https://evanhahn.com/why-alias-is-my-last-resort-for-aliases/

Published Time: 2025-03-05T00:00:00+00:00

Markdown Content:
Aliases were one of the first things I added when customizing my dotfiles. For example, here’s a very early alias I defined:

Now, I can run `g` instead of `git`, which saves me a little time for a command I run dozens of times a day!

```
# These two commands are now equivalent:
git status
g status
```

I used to define these aliases with `alias`. After all…I’m defining an alias!

But over time, I think I discovered a better way: **a script in my `$PATH`**.

How it works
------------

In my home directory, I have a folder of scripts called `bin`. For example, here’s a simplified version of `~/bin/g`:

```
#!/usr/bin/env bash
exec git "$@"
```

Running this script basically just runs `git`.

I add this folder to my `$PATH`. (See [Julia Evans’s guide on how to do this](https://jvns.ca/blog/2025/02/13/how-to-add-a-directory-to-your-path/).) In my `.zshrc`, I have a line like this:

```
export PATH="$HOME/bin:$PATH"
```

Now, when I type `g`, it runs that script.

This behaves just like an alias. As before, `g status` and `git status` are equivalent.

```
# These two commands are still the same:
git status
g status
```

This is a lot more verbose than `alias`. So _why do it this way?_

Benefits of scripts over aliases
--------------------------------

Scripts have several advantages over using `alias`:

*   **No reloading; changes are picked up immediately.** When I create, update, or delete an `alias`, I have to reload my `.zshrc`. I do this by opening a new terminal tab or running `source ~/.zshrc`. But with scripts, I don’t have to! I can just edit files in `~/bin` and they’re immediately ready. This makes it easier to iterate.
    
*   **Choice of programming language.** I use Bash for a lot of my scripts, but not all. For example, I have a note-taking script called [`~/bin/note`](https://gitlab.com/EvanHahn/dotfiles/-/blob/42af33e66387598b174694e3c088ba39d823f8ad/home/bin/bin/note) which I didn’t want to write in Bash, so I wrote it in Python instead. With an alias, I’d _have_ to write it in Zsh.
    
*   **More space to work.** Aliases are typically for simple things, like running `git` when you type `g`. But I have some scripts in `~/bin` that are a little more complex. For example, [`~/bin/sleepybear`](https://gitlab.com/EvanHahn/dotfiles/-/blob/42af33e66387598b174694e3c088ba39d823f8ad/home/bin/bin/sleepybear) puts my computer to sleep, which has different logic on Linux versus macOS. It’s easier to encode that logic in a script than an alias. (I could also do this with a shell function.)
    
*   **More portable.** I usually use Zsh, but I _occasionally_ use Bash and am interested in giving [Fish](https://fishshell.com/) another try. If I used aliases, I’d have to manually port things over to my new shell. With a `~/bin` directory, it’s much less work: just add it to my `$PATH` environment variable and I’m done.
    

These benefits are enough to convince to use scripts as my default, even for simple aliases like `g=git`.

Benefits of aliases over scripts
--------------------------------

Scripts are my preference but they aren’t perfect. Everything in programming has tradeoffs!

There are a few things that are better about `alias`:

*   **Special powers.** `alias` and shell functions have special powers that scripts don’t. For example, I [alias `cd..` to `cd ..`](https://gitlab.com/EvanHahn/dotfiles/-/blob/42af33e66387598b174694e3c088ba39d823f8ad/home/zsh/.config/zsh/aliases.zsh#L33) because I make that typo a lot. I also have a shell function, [`boop`](https://gitlab.com/EvanHahn/dotfiles/-/blob/42af33e66387598b174694e3c088ba39d823f8ad/home/zsh/.config/zsh/aliases.zsh#L56-64), which makes a sound based on the exit status of the previous command. As far as I know, a shell script can’t do these things. It can’t change the working directory of the outer process and it doesn’t know other processes’ exit statuses. If it’s difficult/impossible to do with a script, I fall back to an alias or a shell function.
    
*   **Conditional definition.** It’s harder to conditionally define a file in `~/bin` than it is to conditionally define an alias. For example, I love the `open` command that comes with macOS. On Linux, where it doesn’t exist, [I define an alias with `alias`](https://gitlab.com/EvanHahn/dotfiles/-/blob/42af33e66387598b174694e3c088ba39d823f8ad/home/zsh/.config/zsh/linux.zsh#L13). This alias doesn’t exist on macOS at all because I define it conditionally.
    
*   **Easier to bypass.** I alias `vim` to `nvim`, but _occasionally_ I want to run the real Vim. Bash and Zsh offer [a few ways to bypass aliases](https://unix.stackexchange.com/a/39296/101918); for example, I could run `\vim`. With a shell script in my `$PATH`, I can’t do this. The only way to bypass these is to use the full path, such as `/usr/bin/vim`, to temporarily remove `~/bin` from my `$PATH`, or temporarily move the whole script.
    
*   **Brevity.** When I create a new script, I have to create a new file in `~/bin`, put `#!/usr/bin/env bash` at the top, and make the file executable. This isn’t so bad, but it’s a bit faster to type `alias g=git`. (To make this easier, I wrote [a script called `mksh`](https://gitlab.com/EvanHahn/dotfiles/-/blob/2c9df0139a6960a53a4c490ef3017171d0eedfda/home/bin/bin/mksh) which does this.)
    
*   **Performance.** In an informal test I ran, `alias`es are more than 100× faster. That makes sense; the computer has to find a file in your `$PATH` on disk, parse it, and execute it—slower than just running a command it probably stores in memory. In practice, I have never noticed this performance difference, but maybe I would if I were running `g` hundreds of times a second.
    

Choose your favorite
--------------------

Ultimately, this decision doesn’t make much difference. Both methods—aliases and scripts—are pretty similar. But for me, I default to using scripts because I like what they can do.
