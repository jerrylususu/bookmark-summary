Title: New zine: The Secret Rules of the Terminal

URL Source: https://jvns.ca/blog/2025/06/24/new-zine--the-secret-rules-of-the-terminal/

Markdown Content:
Hello! After many months of writing deep dive blog posts about the terminal, on Tuesday I released a new zine called “The Secret Rules of the Terminal”!

You can get it for $12 here: [https://wizardzines.com/zines/terminal](https://wizardzines.com/zines/terminal), or get an [15-pack of all my zines here](https://wizardzines.com/zines/all-the-zines/).

Here’s the cover:

[![Image 1](https://jvns.ca/images/terminal-cover-small.jpg)](https://wizardzines.com/zines/terminal)

### [the table of contents](https://jvns.ca/blog/2025/06/24/new-zine--the-secret-rules-of-the-terminal/#the-table-of-contents)

Here’s the table of contents:

[![Image 2](https://jvns.ca/images/terminal-toc-small.png)](https://wizardzines.com/zines/terminal/toc.png)
### [why the terminal?](https://jvns.ca/blog/2025/06/24/new-zine--the-secret-rules-of-the-terminal/#why-the-terminal)

I’ve been using the terminal every day for 20 years but even though I’m very confident in the terminal, I’ve always had a bit of an uneasy feeling about it. Usually things work fine, but sometimes something goes wrong and it just feels like investigating it is impossible, or at least like it would open up a huge can of worms.

So I started trying to write down a list of weird problems I’ve run into in terminal and I realized that the terminal has a lot of tiny inconsistencies like:

*   sometimes you can use the arrow keys to move around, but sometimes pressing the arrow keys just prints `^[[D`
*   sometimes you can use the mouse to select text, but sometimes you can’t
*   sometimes your commands get saved to a history when you run them, and sometimes they don’t
*   some shells let you use the up arrow to see the previous command, and some don’t

If you use the terminal daily for 10 or 20 years, even if you don’t understand exactly _why_ these things happen, you’ll probably build an intuition for them.

But having an intuition for them isn’t the same as understanding why they happen. When writing this zine I actually had to do a lot of work to figure out exactly what was _happening_ in the terminal to be able to talk about how to reason about it.

### [the rules aren’t written down anywhere](https://jvns.ca/blog/2025/06/24/new-zine--the-secret-rules-of-the-terminal/#the-rules-aren-t-written-down-anywhere)

It turns out that the “rules” for how the terminal works (how do you edit a command you type in? how do you quit a program? how do you fix your colours?) are extremely hard to fully understand, because “the terminal” is actually made of many different pieces of software (your terminal emulator, your operating system, your shell, the core utilities like `grep`, and every other random terminal program you’ve installed) which are written by different people with different ideas about how things should work.

So I wanted to write something that would explain:

*   how the 4 pieces of the terminal (your shell, terminal emulator, programs, and TTY driver) fit together to make everything work
*   some of the core conventions for how you can expect things in your terminal to work
*   lots of tips and tricks for how to use terminal programs

### [this zine explains the most useful parts of terminal internals](https://jvns.ca/blog/2025/06/24/new-zine--the-secret-rules-of-the-terminal/#this-zine-explains-the-most-useful-parts-of-terminal-internals)

Terminal internals are a mess. A lot of it is just the way it is because someone made a decision in the 80s and now it’s impossible to change, and honestly I don’t think learning everything about terminal internals is worth it.

But some parts are not that hard to understand and can really make your experience in the terminal better, like:

*   if you understand what **your shell** is responsible for, you can configure your shell (or use a different one!) to access your history more easily, get great tab completion, and so much more
*   if you understand **escape codes**, it’s much less scary when `cat`ing a binary to stdout messes up your terminal, you can just type `reset` and move on
*   if you understand how **colour** works, you can get rid of bad colour contrast in your terminal so you can actually read the text

### [I learned a surprising amount writing this zine](https://jvns.ca/blog/2025/06/24/new-zine--the-secret-rules-of-the-terminal/#i-learned-a-surprising-amount-writing-this-zine)

When I wrote [How Git Works](https://wizardzines.com/zines/git), I thought I knew how Git worked, and I was right. But the terminal is different. Even though I feel totally confident in the terminal and even though I’ve used it every day for 20 years, I had a lot of misunderstandings about how the terminal works and (unless you’re the author of `tmux` or something) I think there’s a good chance you do too.

A few things I learned that are actually useful to me:

*   I understand the structure of the terminal better and so I feel more confident debugging weird terminal stuff that happens to me (I was even able to suggest a [small improvement](https://github.com/fish-shell/fish-shell/issues/10834) to fish!). Identifying exactly which piece of software is causing a weird thing to happen in my terminal still isn’t _easy_ but I’m a lot better at it now.
*   you can write a shell script to [copy to your clipboard over SSH](https://jvns.ca/til/vim-osc52/)
*   how `reset` works under the hood (it does the equivalent of `stty sane; sleep 1; tput reset`) – basically I learned that I don’t ever need to worry about remembering `stty sane` or `tput reset` and I can just run `reset` instead
*   how to look at the invisible escape codes that a program is printing out (run `unbuffer program > out; less out`)
*   why the builtin REPLs on my Mac like `sqlite3` are so annoying to use (they use `libedit` instead of `readline`)

### [blog posts I wrote along the way](https://jvns.ca/blog/2025/06/24/new-zine--the-secret-rules-of-the-terminal/#blog-posts-i-wrote-along-the-way)

As usual these days I wrote a bunch of blog posts about various side quests:

*   [How to add a directory to your PATH](https://jvns.ca/blog/2025/02/13/how-to-add-a-directory-to-your-path/)
*   [“rules” that terminal problems follow](https://jvns.ca/blog/2024/11/26/terminal-rules/)
*   [why pipes sometimes get “stuck”: buffering](https://jvns.ca/blog/2024/11/29/why-pipes-get-stuck-buffering/)
*   [some terminal frustrations](https://jvns.ca/blog/2025/02/05/some-terminal-frustrations/)
*   [ASCII control characters in my terminal](https://jvns.ca/blog/2024/10/31/ascii-control-characters/) on “what’s the deal with Ctrl+A, Ctrl+B, Ctrl+C, etc?”
*   [entering text in the terminal is complicated](https://jvns.ca/blog/2024/07/08/readline/)
*   [what’s involved in getting a “modern” terminal setup?](https://jvns.ca/blog/2025/01/11/getting-a-modern-terminal-setup/)
*   [reasons to use your shell’s job control](https://jvns.ca/blog/2024/07/03/reasons-to-use-job-control/)
*   [standards for ANSI escape codes](https://jvns.ca/blog/2025/03/07/escape-code-standards/), which is really me trying to figure out if I think the `terminfo` database is serving us well today

### [people who helped with this zine](https://jvns.ca/blog/2025/06/24/new-zine--the-secret-rules-of-the-terminal/#people-who-helped-with-this-zine)

A long time ago I used to write zines mostly by myself but with every project I get more and more help. I met with [Marie Claire LeBlanc Flanagan](https://marieflanagan.com/) every weekday from September to June to work on this one.

The cover is by Vladimir Kašiković, Lesley Trites did copy editing, Simon Tatham (who wrote [PuTTY](https://www.chiark.greenend.org.uk/~sgtatham/putty/)) did technical review, our Operations Manager Lee did the transcription as well as a million other things, and [Jesse Luehrs](https://github.com/doy) (who is one of the very few people I know who actually understands the terminal’s cursed inner workings) had so many incredibly helpful conversations with me about what is going on in the terminal.

### [get the zine](https://jvns.ca/blog/2025/06/24/new-zine--the-secret-rules-of-the-terminal/#get-the-zine)

Here are some links to get the zine again:

*   get [The Secret Rules of the Terminal](https://wizardzines.com/zines/terminal)
*   get a [15-pack of all my zines here](https://wizardzines.com/zines/all-the-zines/).

As always, you can get either a PDF version to print at home or a print version shipped to your house. The only caveat is print orders will ship in **August** – I need to wait for orders to come in to get an idea of how many I should print before sending it to the printer.
