Title: Slashing my ".bashrc" in half

URL Source: https://www.bitecode.dev/p/slashing-my-bashrc-in-half

Published Time: 2025-02-20T21:20:44+00:00

Markdown Content:
_By installing [Atuin](https://atuin.sh/) (a history handler), [Starship](https://starship.rs/) (a prompt manager), [ripgrep](https://github.com/BurntSushi/ripgrep) (an alternative to grep), [fd](https://github.com/sharkdp/fd) (an alternative to find, to search files and directories), and [fzf](https://github.com/junegunn/fzf) (a universal fuzzy searcher), I shrank down my ".bashrc" in half and removed tons of plugins from my setup._

_It is now faster, leaner, easier to maintain, with modern features that I know will still work in 10 years, and very little effort on my part._

There are two configs I could never get quite right: vim's and my shell's.

For years I spent hours fiddling with options, half of them not sure what they really did. I installed - oh-my! - all sorts of plugin systems that were supposed to make everything better.

But rarely things did work to satisfaction, and when they did, they ended up breaking down the road.

I dropped the idea of Vim as a main editor, tired of spending more time catering to it than producing code with it. I still use it for occasional editing but with its default OS settings.

As for my terminal experience, after having done several times the usual zsh/fish/blabla migration dance, I stopped, and went back to bash, with a subset of manual ".bashrc" tweaks that I knew worked.

This was my (non-client-provided) laptop experience for a decade.

I gave up. I accepted my fate. I settled.

I know it doesn't seem to have anything to do with this, but it surprisingly does.

The Rust community has been attracting highly competent people who appreciate quality software, and as the language grew in popularity, it started to foster [a new age of basic command-line tools](https://zaiste.net/posts/shell-commands-rust/).

First, it was about upping the game for simple classics.

We got a wave of alternatives for `grep`, `ls`, `cat`, `cut`, `find`, etc., that were faster, with saner defaults and better ergonomics. And sure it was not a new phenomenon (`ack` and `ag` were a thing, for example), but it was not just a technical trend, it was cultural. Rust cli tools became synonymous with "fast", "stable" and "well-built". You started by installing one of them because HN had a post about it, and suddenly, you searched for more.

This prompted a second wave of tools, still for the terminal, but with the explicit goal of integrating with the shell and improving it. This meant you could still have a sucky shell, and yet have nice features. Nice features that would be fast and robust because it would be coded in native code, not shell code. And with the same mindset of zero or little work upfront.

We are now in the 3rd wave, with scripting language stacks being also rewritten in Rust with the same idea in mind. For Python, we of course think of `uv`, but [Javascript is following suit](https://voidzero.dev/).

And little by little, little by little, my ".bashrc" shrank.

I used to have a lot of aliases for finding things, filtering things, and moving to places.

They don't exist anymore, they have been replaced by 4 tools:

*   [ripgrep](https://github.com/BurntSushi/ripgrep): an alternative to grep, to filter outputs.
    
*   [fd](https://github.com/sharkdp/fd): an alternative to find, to search files and directories.
    
*   [zoxide](https://github.com/ajeetdsouza/zoxide): an alternative to autojump, to move across the file system quickly.
    
*   [fzf](https://github.com/junegunn/fzf): a universal fuzzy searcher you can apply to everything, especially the 3 tools above.
    

`ripgrep` and `fd` are pretty self-explanatory. They have super nice defaults (they are fast, have clear flags, coloration, ignore VCS files, etc) and basically require no work from you to benefit from them. Install, use, enjoy. Done.

`fzf` is a bit different because it's only 5 years old and more exotic. But basically, it turns any list of things into a pager you can filter with as-you-type fuzzy search. You can pipe the stdout of any command to it, and then narrow the result down. It doesn't seem super useful at first, but the more you use it, the more it feels you can actually apply it to everything.

`zoxide` record your `cd` calls, and then you can jump anywhere in your file system to the place you previously went. `z <whatever>` will move you to the place in the `cd` history that has the closest match to "whatever". Sometimes a few letters are enough. And if you are not feeling like recalling even a few letters, `zi` will pop the entire history into `fzf` if it's installed, basically giving you a filterable favorite place list at your fingertips.

They are all easy to install. In fact, right now, all of them are in Ubuntu repositories.

So all the aliases, functions, or plugins that were basically providing a subset of those features went away.

During the second wave, I adopted two new tools, that tweaked my shell:

*   [Atuin](https://atuin.sh/): a history handler.
    
*   [Starship](https://starship.rs/): a prompt manager.
    

Again, unlike the alternatives, they were not only easy to install, but worked out of the box with a good-enough behavior I used them as-is for some time before even feeling the need to change any config.

Atuin meant all my tabs history was synced, unlimited, and easy to search. No more hacky plugin, no more playing with `HISTCONTROL`, `HISTSIZE`, or `HISTFILESIZE`. No need to move to `zsh` (although it is compatible with it).

Startship obliterated the need for so many prompt hacks and tools to make them work it probably halved my ".bashrc" loading time. I'm exaggerating, but it is very performant, and very feature-complete. You set it up, you install a nice font, et that's it, you will get your git status, activated virtualenv, cur dir, perm status, software versions, etc. proudly displayed when you need it the most. And it's compatible with Windows shells, meaning I can often install it on my clients’ workstations and get a decent terminal experience even there for very little effort on my part.

I restored an old ".bashrc", it used to be 359 lines long. My current one is 153. And it's faster, easier to understand, and requires less work on my part.

I never regretted "the good old days" for anything, and I certainly double down on that statement for shells.

Some things, I don't need to be replaced. I don't need a replacement for `cat` or `ps`. If I want coloration for a file, I'll use `vim` or `subl`, and if I want a better process manager, I'll use `btop`.

Even if I don't have the best tools, I don't change something for a marginal gain. I already have to change things all day long, that's literally part of my job.

Also, why not an alternative to `sed` or `cut`, given they are painful to use with all their legacy quirks? Because I don't make big shell scripts, and I don't care about portability, so I can just ask ChatGPT whatever one-liner I need. I don't need to scratch my brain until some forgotten hieroglyph from `perl` or `awk` fall out of it anymore, I can just ask the AI, and it's very good at it. The wisdom used to be you should know just enough about those to be dangerous, but it's simply not true anymore, even if I get pushbacks every time I mention this in nerdy circles.

And for anything else, well, there is [uv init --script](https://www.bitecode.dev/p/uv-tricks).

Apart from loading all this stuff, I still got a bunch of aliases:

```
...
alias vpn_up='sudo wg-quick up default'
alias whatismyip='curl http://checkip.amazonaws.com'
alias pyhton="uvx python"
alias python="uvx python"
alias py="uvx python"
alias ur="uv run"
alias download_mp3="uvx --with yt-dlp[default,curl-cffi] yt-dlp@latest --extract-audio --audio-format mp3"
...
```

Loads of things replaced with `uv` in there.

Some config:

```
...
export EDITOR="subl -w" # you know why now
export PYTHONSTARTUP="/home/user/Scripts/pythonstartup.py"
export PIP_REQUIRE_VIRTUALENV=1 # say no to drugs
export LANGUAGE=en_US.UTF-8
export LC_MESSAGES=en_US.UTF-8 # force english error messages
...
```

[Some plugins](https://github.com/scmbreeze/scm_breeze) I love and can't go without:

```
...
[ -s "/home/user/.scm_breeze/scm_breeze.sh" ] && source "/home/user/.scm_breeze/scm_breeze.sh"
...
```

And a bunch of utility functions like:

```
...
# I can never remember the syntax to ssh tunnel
tunnel_ssh() {
    LOCAL_PORT=$1
    REMOTE_HOST=$2
    REMOTE_PORT=$3
    HOST_NAME=$(ssh -v $REMOTE_HOST ' ' 2>&1 | grep '^debug1: Connecting to' | cut -d [ -f 2 | sed "s/\]//")
    echo "Connected to ${HOST_NAME}"
    echo "Now, forwarding all traffic from our local $LOCAL_PORT port to its internal $REMOTE_PORT port"
    ssh -L "$LOCAL_PORT":127.0.0.1:"$REMOTE_PORT" "$REMOTE_HOST" -N
}
...
```

The most important thing is when I now read my `.bashrc`, it feels clean. I'm not looking at hacks all over the place. I understand what each line does. I can edit it, maintain it, but above all, not do anything for months.

Completely forgetting about it.

And it will keep working.
