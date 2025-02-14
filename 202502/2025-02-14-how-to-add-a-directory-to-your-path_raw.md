Title: How to add a directory to your PATH

URL Source: https://jvns.ca/blog/2025/02/13/how-to-add-a-directory-to-your-path/

Markdown Content:
I was talking to a friend about how to add a directory to your PATH today. It’s something that feels “obvious” to me since I’ve been using the terminal for a long time, but when I searched for instructions for how to do it, I actually couldn’t find something that explained all of the steps – a lot of them just said “add this to `~/.bashrc`”, but what if you’re not using bash? What if your bash config is actually in a different file? And how are you supposed to figure out which directory to add anyway?

So I wanted to try to write down some more complete directions and mention some of the gotchas I’ve run into over the years.

Here’s a table of contents:

*   [step 1: what shell are you using?](https://jvns.ca/blog/2025/02/13/how-to-add-a-directory-to-your-path/#step-1-what-shell-are-you-using)
*   [step 2: find your shell’s config file](https://jvns.ca/blog/2025/02/13/how-to-add-a-directory-to-your-path/#step-2-find-your-shell-s-config-file)
    *   [a note on bash’s config file](https://jvns.ca/blog/2025/02/13/how-to-add-a-directory-to-your-path/#a-note-on-bash-s-config-file)
*   [step 3: figure out which directory to add](https://jvns.ca/blog/2025/02/13/how-to-add-a-directory-to-your-path/#step-3-figure-out-which-directory-to-add)
    *   [step 3.1: double check it’s the right directory](https://jvns.ca/blog/2025/02/13/how-to-add-a-directory-to-your-path/#step-3-1-double-check-it-s-the-right-directory)
*   [step 4: edit your shell config](https://jvns.ca/blog/2025/02/13/how-to-add-a-directory-to-your-path/#step-4-edit-your-shell-config)
*   [step 5: restart your shell](https://jvns.ca/blog/2025/02/13/how-to-add-a-directory-to-your-path/#step-5-restart-your-shell)
*   problems:
    *   [problem 1: it ran the wrong program](https://jvns.ca/blog/2025/02/13/how-to-add-a-directory-to-your-path/#problem-1-it-ran-the-wrong-program)
    *   [problem 2: the program isn’t being run from your shell](https://jvns.ca/blog/2025/02/13/how-to-add-a-directory-to-your-path/#problem-2-the-program-isn-t-being-run-from-your-shell)
*   notes:
    *   [a note on source](https://jvns.ca/blog/2025/02/13/how-to-add-a-directory-to-your-path/#a-note-on-source)
    *   [a note on fish\_add\_path](https://jvns.ca/blog/2025/02/13/how-to-add-a-directory-to-your-path/#a-note-on-fish-add-path)

### [step 1: what shell are you using?](https://jvns.ca/blog/2025/02/13/how-to-add-a-directory-to-your-path/#step-1-what-shell-are-you-using)

If you’re not sure what shell you’re using, here’s a way to find out. Run this:

```
ps -p $$ -o pid,comm=
```

*   if you’re using **bash**, it’ll print out `97295 bash`
*   if you’re using **zsh**, it’ll print out `97295 zsh`
*   if you’re using **fish**, it’ll print out an error like “In fish, please use $fish\_pid” (`$$` isn’t valid syntax in fish, but in any case the error message tells you that you’re using fish, which you probably already knew)

Also bash is the default on Linux and zsh is the default on Mac OS (as of 2024). I’ll only cover bash, zsh, and fish in these directions.

### [step 2: find your shell’s config file](https://jvns.ca/blog/2025/02/13/how-to-add-a-directory-to-your-path/#step-2-find-your-shell-s-config-file)

*   in zsh, it’s probably `~/.zshrc`
*   in bash, it might be `~/.bashrc`, but it’s complicated, see the note in the next section
*   in fish, it’s probably `~/.config/fish/config.fish` (you can run `echo $__fish_config_dir` if you want to be 100% sure)

### [a note on bash’s config file](https://jvns.ca/blog/2025/02/13/how-to-add-a-directory-to-your-path/#a-note-on-bash-s-config-file)

Bash has three possible config files: `~/.bashrc`, `~/.bash_profile`, and `~/.profile`.

If you’re not sure which one your system is set up to use, I’d recommend testing this way:

1.  add `echo hi there` to your `~/.bashrc`
2.  Restart your terminal
3.  If you see “hi there”, that means `~/.bashrc` is being used! Hooray!
4.  Otherwise remove it and try the same thing with `~/.bash_profile`
5.  You can also try `~/.profile` if the first two options don’t work.

(there are a lot of elaborate flow charts out there that explain how bash decides which config file to use but IMO it’s not worth it and just testing is the fastest way to be sure)

### [step 3: figure out which directory to add](https://jvns.ca/blog/2025/02/13/how-to-add-a-directory-to-your-path/#step-3-figure-out-which-directory-to-add)

Let’s say that you’re trying to install and run a program called `http-server` and it doesn’t work, like this:

```
$ npm install -g http-server
$ http-server
bash: http-server: command not found
```

How do you find what directory `http-server` is in? Honestly in general this is not that easy – often the answer is something like “it depends on how npm is configured”. A few ideas:

*   Often when setting up a new installer (like `cargo`, `npm`, `homebrew`, etc), when you first set it up it’ll print out some directions about how to update your PATH. So if you’re paying attention you can get the directions then.
*   Sometimes installers will automatically update your shell’s config file to update your `PATH` for you
*   Sometimes just Googling “where does npm install things?” will turn up the answer
*   Some tools have a subcommand that tells you where they’re configured to install things, like:
    *   Node/npm: `npm config get prefix` (then append `/bin/`)
    *   Go: `go env GOPATH` (then append `/bin/`)
    *   asdf: `asdf info | grep ASDF_DIR` (then append `/bin/` and `/shims/`)

### [step 3.1: double check it’s the right directory](https://jvns.ca/blog/2025/02/13/how-to-add-a-directory-to-your-path/#step-3-1-double-check-it-s-the-right-directory)

Once you’ve found a directory you think might be the right one, make sure it’s actually correct! For example, I found out that on my machine, `http-server` is in `~/.npm-global/bin`. I can make sure that it’s the right directory by trying to run the program `http-server` in that directory like this:

```
$ ~/.npm-global/bin/http-server
Starting up http-server, serving ./public
```

It worked! Now that you know what directory you need to add to your `PATH`, let’s move to the next step!

### [step 4: edit your shell config](https://jvns.ca/blog/2025/02/13/how-to-add-a-directory-to-your-path/#step-4-edit-your-shell-config)

Now we have the 2 critical pieces of information we need:

1.  Which directory you’re trying to add to your PATH (like `~/.npm-global/bin/`)
2.  Where your shell’s config is (like `~/.bashrc`, `~/.zshrc`, or `~/.config/fish/config.fish`)

Now what you need to add depends on your shell:

**bash instructions:**

Open your shell’s config file, and add a line like this:

```
export PATH=$PATH:~/.npm-global/bin/
```

(obviously replace `~/.npm-global/bin` with the actual directory you’re trying to add)

**zsh instructions:**

You can do the same thing as in bash, but zsh also has some slightly fancier syntax you can use if you prefer:

```
path=(
  $path
  ~/.npm-global/bin
)
```

**fish instructions:**

In fish, the syntax is different:

```
set PATH $PATH ~/.npm-global/bin
```

(in fish you can also use `fish_add_path`, some notes on that [further down](https://jvns.ca/blog/2025/02/13/how-to-add-a-directory-to-your-path/#a-note-on-fish-add-path))

### [step 5: restart your shell](https://jvns.ca/blog/2025/02/13/how-to-add-a-directory-to-your-path/#step-5-restart-your-shell)

Now, an extremely important step: updating your shell’s config won’t take effect if you don’t restart it!

Two ways to do this:

1.  open a new terminal (or terminal tab), and maybe close the old one so you don’t get confused
2.  Run `bash` to start a new shell (or `zsh` if you’re using zsh, or `fish` if you’re using fish)

I’ve found that both of these usually work fine.

And you should be done! Try running the program you were trying to run and hopefully it works now.

If not, here are a couple of problems that you might run into:

### [problem 1: it ran the wrong program](https://jvns.ca/blog/2025/02/13/how-to-add-a-directory-to-your-path/#problem-1-it-ran-the-wrong-program)

If the wrong **version** of a is program running, you might need to add the directory to the _beginning_ of your PATH instead of the end.

For example, on my system I have two versions of `python3` installed, which I can see by running `which -a`:

```
$ which -a python3
/usr/bin/python3
/opt/homebrew/bin/python3
```

The one your shell will use is the **first one listed**.

If you want to use the Homebrew version, you need to add that directory (`/opt/homebrew/bin`) to the **beginning** of your PATH instead, by putting this in your shell’s config file (it’s `/opt/homebrew/bin/:$PATH` instead of the usual `$PATH:/opt/homebrew/bin/`)

```
export PATH=/opt/homebrew/bin/:$PATH
```

or in fish:

```
set PATH ~/.cargo/bin $PATH
```

### [problem 2: the program isn’t being run from your shell](https://jvns.ca/blog/2025/02/13/how-to-add-a-directory-to-your-path/#problem-2-the-program-isn-t-being-run-from-your-shell)

All of these directions only work if you’re running the program **from your shell**. If you’re running the program from an IDE, from a GUI, in a cron job, or some other way, you’ll need to add the directory to your PATH in a different way, and the exact details might depend on the situation.

**in a cron job**

Some options:

*   use the full path to the program you’re running, like `/home/bork/bin/my-program`
*   put the full PATH you want as the first line of your crontab (something like PATH=/bin:/usr/bin:/usr/local/bin:….). You can get the full PATH you’re using in your shell by running `echo "PATH=$PATH"`.

I’m honestly not sure how to handle it in an IDE/GUI because I haven’t run into that in a long time, will add directions here if someone points me in the right direction.

### [a note on `source`](https://jvns.ca/blog/2025/02/13/how-to-add-a-directory-to-your-path/#a-note-on-source)

When you install `cargo` (Rust’s installer) for the first time, it gives you these instructions for how to set up your PATH, which don’t mention a specific directory at all.

```
This is usually done by running one of the following (note the leading DOT):

. "$HOME/.cargo/env"        	# For sh/bash/zsh/ash/dash/pdksh
source "$HOME/.cargo/env.fish"  # For fish
```

The idea is that you add that line to your shell’s config, and their script automatically sets up your `PATH` (and potentially other things) for you.

This is pretty common (for example [Homebrew](https://github.com/Homebrew/install/blob/deacfa6a6e62e5f4002baf9e1fac7a96e9aa5d41/install.sh#L1072-L1087) suggests you eval `brew shellenv`), and there are two ways to approach this:

1.  Just do what the tool suggests (like adding `. "$HOME/.cargo/env"` to your shell’s config)
2.  Figure out which directories the script they’re telling you to run would add to your PATH, and then add those manually. Here’s how I’d do that:
    *   Run `. "$HOME/.cargo/env"` in my shell (or the fish version if using fish)
    *   Run `echo "$PATH" | tr ':' '\n' | grep cargo` to figure out which directories it added
    *   See that it says `/Users/bork/.cargo/bin` and shorten that to `~/.cargo/bin`
    *   Add the directory `~/.cargo/bin` to PATH (with the directions in this post)

I don’t think there’s anything wrong with doing what the tool suggests (it might be the “best way”!), but personally I usually use the second approach because I prefer knowing exactly what configuration I’m changing.

### [a note on `fish_add_path`](https://jvns.ca/blog/2025/02/13/how-to-add-a-directory-to-your-path/#a-note-on-fish-add-path)

fish has a handy function called `fish_add_path` that you can run to add a directory to your `PATH` like this:

```
fish_add_path /some/directory
```

This is cool (it’s such a simple command!) but I’ve stopped using it for a couple of reasons:

1.  Sometimes `fish_add_path` will update the `PATH` for every session in the future (with a “universal variable”) and sometimes it will update the `PATH` just for the current session and it’s hard for me to tell which one it will do. In theory the docs explain this but I could not understand them.
2.  If you ever need to _remove_ the directory from your `PATH` a few weeks or months later because maybe you made a mistake, it’s kind of hard to do (there are [instructions in this comments of this github issue though](https://github.com/fish-shell/fish-shell/issues/8604)).

### [that’s all](https://jvns.ca/blog/2025/02/13/how-to-add-a-directory-to-your-path/#that-s-all)

Hopefully this will help some people. Let me know (on Mastodon or Bluesky) if you there are other major gotchas that have tripped you up when adding a directory to your PATH, or if you have questions about this post!
