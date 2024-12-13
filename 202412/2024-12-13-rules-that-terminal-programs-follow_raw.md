Title: "Rules" that terminal programs follow

URL Source: https://jvns.ca/blog/2024/11/26/terminal-rules/

Markdown Content:
Recently I’ve been thinking about how everything that happens in the terminal is some combination of:

1.  Your **operating system**’s job
2.  Your **shell**’s job
3.  Your **terminal emulator**’s job
4.  The job of **whatever program you happen to be running** (like `top` or `vim` or `cat`)

The first three (your operating system, shell, and terminal emulator) are all kind of known quantities – if you’re using bash in GNOME Terminal on Linux, you can more or less reason about how how all of those things interact, and some of their behaviour is standardized by POSIX.

But the fourth one (“whatever program you happen to be running”) feels like it could do ANYTHING. How are you supposed to know how a program is going to behave?

This post is kind of long so here’s a quick table of contents:

*   [programs behave surprisingly consistently](https://jvns.ca/blog/2024/11/26/terminal-rules/#programs-behave-surprisingly-consistently)
*   [these are meant to be descriptive, not prescriptive](https://jvns.ca/blog/2024/11/26/terminal-rules/#these-are-meant-to-be-descriptive-not-prescriptive)
*   [it’s not always obvious which “rules” are the program’s responsibility to implement](https://jvns.ca/blog/2024/11/26/terminal-rules/#it-s-not-always-obvious-which-rules-are-the-program-s-responsibility-to-implement)
*   [rule 1: noninteractive programs should quit when you press `Ctrl-C`](https://jvns.ca/blog/2024/11/26/terminal-rules/#rule-1-noninteractive-programs-should-quit-when-you-press-ctrl-c)
*   [rule 2: TUIs should quit when you press `q`](https://jvns.ca/blog/2024/11/26/terminal-rules/#rule-2-tuis-should-quit-when-you-press-q)
*   [rule 3: REPLs should quit when you press `Ctrl-D` on an empty line](https://jvns.ca/blog/2024/11/26/terminal-rules/#rule-3-repls-should-quit-when-you-press-ctrl-d-on-an-empty-line)
*   [rule 4: don’t use more than 16 colours](https://jvns.ca/blog/2024/11/26/terminal-rules/#rule-4-don-t-use-more-than-16-colours)
*   [rule 5: vaguely support readline keybindings](https://jvns.ca/blog/2024/11/26/terminal-rules/#rule-5-vaguely-support-readline-keybindings)
*   [rule 5.1: `Ctrl-W` should delete the last word](https://jvns.ca/blog/2024/11/26/terminal-rules/#rule-5-1-ctrl-w-should-delete-the-last-word)
*   [rule 6: disable colours when writing to a pipe](https://jvns.ca/blog/2024/11/26/terminal-rules/#rule-6-disable-colours-when-writing-to-a-pipe)
*   [rule 7: `-` means stdin/stdout](https://jvns.ca/blog/2024/11/26/terminal-rules/#rule-7-means-stdin-stdout)
*   [these “rules” take a long time to learn](https://jvns.ca/blog/2024/11/26/terminal-rules/#these-rules-take-a-long-time-to-learn)

### programs behave surprisingly consistently

As far as I know, there are no real standards for how programs in the terminal should behave – the closest things I know of are:

*   POSIX, which mostly dictates how your terminal emulator / OS / shell should work together. I think it does specify a few things about how core utilities like `cp` should work but AFAIK it doesn’t have anything to say about how for example `htop` should behave.
*   these [command line interface guidelines](https://clig.dev/)

But even though there are no standards, in my experience programs in the terminal behave in a pretty consistent way. So I wanted to write down a list of “rules” that in my experience programs mostly follow.

### these are meant to be descriptive, not prescriptive

My goal here isn’t to convince authors of terminal programs that they _should_ follow any of these rules. There are lots of exceptions to these and often there’s a good reason for those exceptions.

But it’s very useful for me to know what behaviour to expect from a random new terminal program that I’m using. Instead of “uh, programs could do literally anything”, it’s “ok, here are the basic rules I expect, and then I can keep a short mental list of exceptions”.

So I’m just writing down what I’ve observed about how programs behave in my 20 years of using the terminal, why I think they behave that way, and some examples of cases where that rule is “broken”.

### it’s not always obvious which “rules” are the program’s responsibility to implement

There are a bunch of common conventions that I think are pretty clearly the program’s responsibility to implement, like:

*   config files should go in `~/.BLAHrc` or `~/.config/BLAH/FILE` or `/etc/BLAH/` or something
*   `--help` should print help text
*   programs should print “regular” output to stdout and errors to stderr

But in this post I’m going to focus on things that it’s not 100% obvious are the program’s responsibility. For example it feels to me like a “law of nature” that pressing `Ctrl-D` should quit a REPL, but programs often need to explicitly implement support for it – even though `cat` doesn’t need to implement `Ctrl-D` support, `ipython` [does](https://github.com/prompt-toolkit/python-prompt-toolkit/blob/a2a12300c635ab3c051566e363ed27d853af4b21/src/prompt_toolkit/shortcuts/prompt.py#L824-L837). (more about that in “rule 3” below)

Understanding which things are the program’s responsibility makes it much less surprising when different programs’ implementations are slightly different.

### rule 1: noninteractive programs should quit when you press `Ctrl-C`

The main reason for this rule is that noninteractive programs will quit by default on `Ctrl-C` if they don’t set up a `SIGINT` signal handler, so this is kind of a “you should act like the default” rule.

Something that trips a lot of people up is that this doesn’t apply to **interactive** programs like `python3` or `bc` or `less`. This is because in an interactive program, `Ctrl-C` has a different job – if the program is running an operation (like for example a search in `less` or some Python code in `python3`), then `Ctrl-C` will interrupt that operation but not stop the program.

As an example of how this works in an interactive program: here’s the code [in prompt-toolkit](https://github.com/prompt-toolkit/python-prompt-toolkit/blob/a2a12300c635ab3c051566e363ed27d853af4b21/src/prompt_toolkit/key_binding/bindings/vi.py#L2225) (the library that iPython uses for handling input) that aborts a search when you press `Ctrl-C`.

### rule 2: TUIs should quit when you press `q`

TUI programs (like `less` or `htop`) will usually quit when you press `q`.

This rule doesn’t apply to any program where pressing `q` to quit wouldn’t make sense, like `tmux` or text editors.

### rule 3: REPLs should quit when you press `Ctrl-D` on an empty line

REPLs (like `python3` or `ed`) will usually quit when you press `Ctrl-D` on an empty line. This rule is similar to the `Ctrl-C` rule – the reason for this is that by default if you’re running a program (like `cat`) in “cooked mode”, then the operating system will return an `EOF` when you press `Ctrl-D` on an empty line.

Most of the REPLs I use (sqlite3, python3, fish, bash, etc) don’t actually use cooked mode, but they all implement this keyboard shortcut anyway to mimic the default behaviour.

For example, here’s [the code in prompt-toolkit](https://github.com/prompt-toolkit/python-prompt-toolkit/blob/a2a12300c635ab3c051566e363ed27d853af4b21/src/prompt_toolkit/shortcuts/prompt.py#L824-L837) that quits when you press Ctrl-D, and here’s [the same code in readline](https://github.com/bminor/bash/blob/6794b5478f660256a1023712b5fc169196ed0a22/lib/readline/readline.c#L658-L672).

I actually thought that this one was a “Law of Terminal Physics” until very recently because I’ve basically never seen it broken, but you can see that it’s just something that each individual input library has to implement in the links above.

Someone pointed out that the Erlang REPL does not quit when you press `Ctrl-D`, so I guess not every REPL follows this “rule”.

### rule 4: don’t use more than 16 colours

Terminal programs rarely use colours other than the base 16 ANSI colours. This is because if you specify colours with a hex code, it’s very likely to clash with some users’ background colour. For example if I print out some text as `#EEEEEE`, it would be almost invisible on a white background, though it would look fine on a dark background.

But if you stick to the default 16 base colours, you have a much better chance that the user has configured those colours in their terminal emulator so that they work reasonably well with their background color. Another reason to stick to the default base 16 colours is that it makes less assumptions about what colours the terminal emulator supports.

The only programs I usually see breaking this “rule” are text editors, for example Helix by default will use a custom colorscheme with this very nice purple background which is not a default ANSI colour. It seems fine for Helix to break this rule since Helix isn’t a “core” program and I assume any Helix user who doesn’t like that colorscheme will just change the theme.

### rule 5: vaguely support readline keybindings

Almost every program I use supports `readline` keybindings if it would make sense to do so. For example, here are a bunch of different programs and a link to where they define `Ctrl-E` to go to the end of the line:

*   ipython ([Ctrl-E defined here](https://github.com/prompt-toolkit/python-prompt-toolkit/blob/a2a12300c635ab3c051566e363ed27d853af4b21/src/prompt_toolkit/key_binding/bindings/emacs.py#L72))
*   atuin ([Ctrl-E defined here](https://github.com/atuinsh/atuin/blob/a67cfc82fe0dc907a01f07a0fd625701e062a33b/crates/atuin/src/command/client/search/interactive.rs#L407))
*   fzf ([Ctrl-E defined here](https://github.com/junegunn/fzf/blob/bb55045596d6d08445f3c6d320c3ec2b457462d1/src/terminal.go#L611))
*   zsh ([Ctrl-E defined here](https://github.com/zsh-users/zsh/blob/86d5f24a3d28541f242eb3807379301ea976de87/Src/Zle/zle_bindings.c#L94))
*   fish ([Ctrl-E defined here](https://github.com/fish-shell/fish-shell/blob/99fa8aaaa7956178973150a03ce4954ab17a197b/share/functions/fish_default_key_bindings.fish#L43))
*   tmux’s command prompt ([Ctrl-E defined here](https://github.com/tmux/tmux/blob/ae8f2208c98e3c2d6e3fe4cad2281dce8fd11f31/key-bindings.c#L490))

None of those programs actually uses `readline` directly, they just sort of mimic emacs/readline keybindings. They don’t always mimic them _exactly_: for example atuin seems to use `Ctrl-A` as a prefix, so `Ctrl-A` doesn’t go to the beginning of the line.

Also all of these programs seem to implement their own internal cut and paste buffers so you can delete a line with `Ctrl-U` and then paste it with `Ctrl-Y`.

The exceptions to this are:

*   some programs (like `git`, `cat`, and `nc`) don’t have any line editing support at all (except for backspace, `Ctrl-W`, and `Ctrl-U`)
*   as usual text editors are an exception, every text editor has its own approach to editing text

I wrote more about this “what keybindings does a program support?” question in [entering text in the terminal is complicated](https://jvns.ca/blog/2024/07/08/readline/).

### rule 5.1: Ctrl-W should delete the last word

I’ve never seen a program (other than a text editor) where `Ctrl-W` _doesn’t_ delete the last word. This is similar to the `Ctrl-C` rule – by default if a program is in “cooked mode”, the OS will delete the last word if you press `Ctrl-W`, and delete the whole line if you press `Ctrl-U`. So usually programs will imitate that behaviour.

I can’t think of any exceptions to this other than text editors but if there are I’d love to hear about them!

### rule 6: disable colours when writing to a pipe

Most programs will disable colours when writing to a pipe. For example:

*   `rg blah` will highlight all occurrences of `blah` in the output, but if the output is to a pipe or a file, it’ll turn off the highlighting.
*   `ls --color=auto` will use colour when writing to a terminal, but not when writing to a pipe

Both of those programs will also format their output differently when writing to the terminal: `ls` will organize files into columns, and ripgrep will group matches with headings.

If you want to force the program to use colour (for example because you want to look at the colour), you can use `unbuffer` to force the program’s output to be a tty like this:

```
unbuffer rg blah |  less -R
```

I’m sure that there are some programs that “break” this rule but I can’t think of any examples right now. Some programs have an `--color` flag that you can use to force colour to be on, in the example above you could also do `rg --color=always | less -R`.

### rule 7: `-` means stdin/stdout

Usually if you pass `-` to a program instead of a filename, it’ll read from stdin or write to stdout (whichever is appropriate). For example, if you want to format the Python code that’s on your clipboard with `black` and then copy it, you could run:

```
pbpaste | black - | pbcopy
```

(`pbpaste` is a Mac program, you can do something similar on Linux with `xclip`)

My impression is that most programs implement this if it would make sense and I can’t think of any exceptions right now, but I’m sure there are many exceptions.

### these “rules” take a long time to learn

These rules took me a long time for me to learn because I had to:

1.  learn that the rule applied anywhere at all ("`Ctrl-C` will exit programs")
2.  notice some exceptions (“okay, `Ctrl-C` will exit `find` but not `less`”)
3.  subconsciously figure out what the pattern is ("`Ctrl-C` will generally quit noninteractive programs, but in interactive programs it might interrupt the current operation instead of quitting the program")
4.  eventually maybe formulate it into an explicit rule that I know

A lot of my understanding of the terminal is honestly still in the “subconscious pattern recognition” stage. The only reason I’ve been taking the time to make things explicit at all is because I’ve been trying to explain how it works to others. Hopefully writing down these “rules” explicitly will make learning some of this stuff a little bit faster for others.
