Title: What's involved in getting a "modern" terminal setup?

URL Source: https://jvns.ca/blog/2025/01/11/getting-a-modern-terminal-setup/

Markdown Content:
Hello! Recently I ran a terminal survey and I asked people what frustrated them. One person commented:

> There are so many pieces to having a modern terminal experience. I wish it all came out of the box.

My immediate reaction was “oh, getting a modern terminal experience isn’t that hard, you just need to….”, but the more I thought about it, the longer the “you just need to…” list got, and I kept thinking about more and more caveats.

So I thought I would write down some notes about what it means to me personally to have a “modern” terminal experience and what I think can make it hard for people to get there.

### [what is a “modern terminal experience”?](https://jvns.ca/blog/2025/01/11/getting-a-modern-terminal-setup/#what-is-a-modern-terminal-experience)

Here are a few things that are important to me, with which part of the system is responsible for them:

*   **multiline support for copy and paste**: if you paste 3 commands in your shell, it should not immediatly run them all! That’s scary! (**shell**, **terminal emulator**)
*   **infinite shell history**: if I run a command in my shell, it should be saved forever, not deleted after 500 history entries or whatever. Also I want commands to be saved to the history immediately when I run them, not only when I exit the shell session (**shell**)
*   **a useful prompt**: I can’t live without having my **current directory** and **current git branch** in my prompt (**shell**)
*   **24-bit colour**: this is important to me because I find it MUCH easier to theme neovim with 24-bit colour support than in a terminal with only 256 colours (**terminal emulator**)
*   **clipboard integration** between vim and my operating system so that when I copy in Firefox, I can just press `p` in vim to paste (**text editor**, maybe the OS/terminal emulator too)
*   **good autocomplete**: for example commands like git should have command-specific autocomplete (**shell**)
*   **having colours in `ls`** (**shell config**)
*   **a terminal theme I like**: I spend a lot of time in my terminal, I want it to look nice and I want its theme to match my terminal editor’s theme. (**terminal emulator**, **text editor**)
*   **automatic terminal fixing**: If a programs prints out some weird escape codes that mess up my terminal, I want that to automatically get reset so that my terminal doesn’t get messed up (**shell**)
*   **keybindings**: I want `Ctrl+left arrow` to work (**shell** or **application**)
*   **being able to use the scroll wheel in programs like `less`**: (**terminal emulator** and **applications**)

There are a million other terminal conveniences out there and different people value different things, but those are the ones that I would be really unhappy without.

### [how I achieve a “modern experience”](https://jvns.ca/blog/2025/01/11/getting-a-modern-terminal-setup/#how-i-achieve-a-modern-experience)

My basic approach is:

1.  use the `fish` shell. Mostly don’t configure it, except to:
    *   set the `EDITOR` environment variable to my favourite terminal editor
    *   alias `ls` to `ls --color=auto`
2.  use any terminal emulator with 24-bit colour support. In the past I’ve used GNOME Terminal, Terminator, and iTerm, but I’m not picky about this. I don’t really configure it other than to choose a font.
3.  use `neovim`, with a configuration that I’ve been very slowly building over the last 9 years or so (the last time I deleted my vim config and started from scratch was 9 years ago)
4.  use the [base16 framework](https://github.com/chriskempson/base16) to theme everything

### [some “out of the box” options for a “modern” experience](https://jvns.ca/blog/2025/01/11/getting-a-modern-terminal-setup/#some-out-of-the-box-options-for-a-modern-experience)

What if you want a nice experience, but don’t want to spend a lot of time on configuration? Figuring out how to configure vim in a way that I was satisfied with really did take me like ten years, which is a long time!

My best ideas for how to get a reasonable terminal experience with minimal config are:

*   shell: either `fish` or `zsh` with [oh-my-zsh](https://ohmyz.sh/)
*   terminal emulator: almost anything with 24-bit colour support, for example all of these are popular:
    *   linux: GNOME Terminal, Konsole, Terminator, xfce4-terminal
    *   mac: iTerm (Terminal.app doesn’t have 256-colour support)
    *   cross-platform: kitty, alacritty, wezterm, or ghostty
*   shell config:
    *   set the `EDITOR` environment variable to your favourite terminal text editor
    *   maybe alias `ls` to `ls --color=auto`
*   text editor: this is a tough one, maybe [micro](https://micro-editor.github.io/) or [helix](https://helix-editor.com/)? I haven’t used either of them seriously but they both seem like very cool projects and I think it’s amazing that you can just use all the usual GUI editor commands (`Ctrl-C` to copy, `Ctrl-V` to paste, `Ctrl-A` to select all) in micro and they do what you’d expect. I would probably try switching to helix except that retraining my vim muscle memory seems way too hard. Also helix doesn’t have a GUI or plugin system yet.

Personally I **wouldn’t** use xterm, rxvt, or Terminal.app as a terminal emulator, because I’ve found in the past that they’re missing core features (like 24-bit colour in Terminal.app’s case) that make the terminal harder to use for me.

I don’t want to pretend that getting a “modern” terminal experience is easier than it is though – I think there are two issues that make it hard. Let’s talk about them!

### [issue 1 with getting to a “modern” experience: the shell](https://jvns.ca/blog/2025/01/11/getting-a-modern-terminal-setup/#issue-1-with-getting-to-a-modern-experience-the-shell)

bash and zsh are by far the two most popular shells, and neither of them provide a default experience that I would be happy using out of the box, for example:

*   you need to customize your prompt
*   they don’t come with git completions by default, you have to set them up
*   by default, bash only stores 500 (!) lines of history and (at least on Mac OS) zsh is only configured to store 2000 lines, which is still not a lot
*   I find bash’s tab completion very frustrating, if there’s more than one match then you can’t tab through them

And even though [I love fish](https://jvns.ca/blog/2024/09/12/reasons-i--still--love-fish/), the fact that it isn’t POSIX does make it hard for a lot of folks to make the switch.

Of course it’s totally possible to learn how to customize your prompt in bash or whatever, and it doesn’t even need to be that complicated (in bash I’d probably start with something like `export PS1='[\u@\h \W$(__git_ps1 " (%s)")]\$ '`, or maybe use [starship](https://starship.rs/)). But each of these “not complicated” things really does add up and it’s especially tough if you need to keep your config in sync across several systems.

An extremely popular solution to getting a “modern” shell experience is [oh-my-zsh](https://ohmyz.sh/). It seems like a great project and I know a lot of people use it very happily, but I’ve struggled with configuration systems like that in the past – it looks like right now the base oh-my-zsh adds about 3000 lines of config, and often I find that having an extra configuration system makes it harder to debug what’s happening when things go wrong. I personally have a tendency to use the system to add a lot of extra plugins, make my system slow, get frustrated that it’s slow, and then delete it completely and write a new config from scratch.

### [issue 2 with getting to a “modern” experience: the text editor](https://jvns.ca/blog/2025/01/11/getting-a-modern-terminal-setup/#issue-2-with-getting-to-a-modern-experience-the-text-editor)

In the terminal survey I ran recently, the most popular terminal text editors by far were `vim`, `emacs`, and `nano`.

I think the main options for terminal text editors are:

*   use vim or emacs and configure it to your liking, you can probably have any feature you want if you put in the work
*   use nano and accept that you’re going to have a pretty limited experience (for example I don’t think you can select text with the mouse and then “cut” it in nano)
*   use `micro` or `helix` which seem to offer a pretty good out-of-the-box experience, potentially occasionally run into issues with using a less mainstream text editor
*   just avoid using a terminal text editor as much as possible, maybe use VSCode, use VSCode’s terminal for all your terminal needs, and mostly never edit files in the terminal

### [issue 3: individual applications](https://jvns.ca/blog/2025/01/11/getting-a-modern-terminal-setup/#issue-3-individual-applications)

The last issue is that sometimes individual programs that I use are kind of annoying. For example on my Mac OS machine, `/usr/bin/sqlite3` doesn’t support the `Ctrl+Left Arrow` keyboard shortcut. Fixing this to get a reasonable terminal experience in SQLite was a little complicated, I had to:

*   realize why this is happening (Mac OS won’t ship GNU tools, and “Ctrl-Left arrow” support comes from GNU readline)
*   find a workaround (install sqlite from homebrew, which does have readline support)
*   adjust my environment (put Homebrew’s sqlite3 in my PATH)

I find that debugging application-specific issues like this is really not easy and often it doesn’t feel “worth it” – often I’ll end up just dealing with various minor inconveniences because I don’t want to spend hours investigating them. The only reason I was even able to figure this one out at all is that I’ve been spending a huge amount of time thinking about the terminal recently.

A big part of having a “modern” experience using terminal programs is just using newer terminal programs, for example I can’t be bothered to learn a keyboard shortcut to sort the columns in `top`, but in `htop` I can just click on a column heading with my mouse to sort it. So I use htop instead! But discovering new more “modern” command line tools isn’t easy (though I made [a list here](https://jvns.ca/blog/2022/04/12/a-list-of-new-ish--command-line-tools/)), finding ones that I actually like using in practice takes time, and if you’re SSHed into another machine, they won’t always be there.

### [everything affects everything else](https://jvns.ca/blog/2025/01/11/getting-a-modern-terminal-setup/#everything-affects-everything-else)

Something I find tricky about configuring my terminal to make everything “nice” is that changing one seemingly small thing about my workflow can really affect everything else. For example right now I don’t use tmux. But if I needed to use tmux again (for example because I was doing a lot of work SSHed into another machine), I’d need to think about a few things, like:

*   if I wanted tmux’s copy to synchronize with my system clipboard over SSH, I’d need to make sure that my terminal emulator has [OSC 52 support](https://old.reddit.com/r/vim/comments/k1ydpn/a_guide_on_how_to_copy_text_from_anywhere/)
*   if I wanted to use iTerm’s tmux integration (which makes tmux tabs into iTerm tabs), I’d need to change how I configure colours – right now I set them with a [shell script](https://github.com/chriskempson/base16-shell/blob/588691ba71b47e75793ed9edfcfaa058326a6f41/scripts/base16-solarized-light.sh) that I run when my shell starts, but that means the colours get lost when restoring a tmux session.

and probably more things I haven’t thought of. “Using tmux means that I have to change how I manage my colours” sounds unlikely, but that really did happen to me and I decided “well, I don’t want to change how I manage colours right now, so I guess I’m not using that feature!”.

It’s also hard to remember which features I’m relying on – for example maybe my current terminal _does_ have OSC 52 support and because copying from tmux over SSH has always Just Worked I don’t even realize that that’s something I need, and then it mysteriously stops working when I switch terminals.

### [change things slowly](https://jvns.ca/blog/2025/01/11/getting-a-modern-terminal-setup/#change-things-slowly)

Personally even though I think my setup is not _that_ complicated, it’s taken me 20 years to get to this point! Because terminal config changes are so likely to have unexpected and hard-to-understand consequences, I’ve found that if I change a lot of terminal configuration all at once it makes it much harder to understand what went wrong if there’s a problem, which can be really disorienting.

So I usually prefer to make pretty small changes, and accept that changes can might take me a REALLY long time to get used to. For example I switched from using `ls` to [eza](https://github.com/eza-community/eza) a year or two ago and while I like it (because `eza -l` prints human-readable file sizes by default) I’m still not quite sure about it. But also sometimes it’s worth it to make a big change, like I made the switch to fish (from bash) 10 years ago and I’m very happy I did.

### [getting a “modern” terminal is not that easy](https://jvns.ca/blog/2025/01/11/getting-a-modern-terminal-setup/#getting-a-modern-terminal-is-not-that-easy)

Trying to explain how “easy” it is to configure your terminal really just made me think that it’s kind of hard and that I still sometimes get confused.

I’ve found that there’s never one perfect way to configure things in the terminal that will be compatible with every single other thing. I just need to try stuff, figure out some kind of locally stable state that works for me, and accept that if I start using a new tool it might disrupt the system and I might need to rethink things.
