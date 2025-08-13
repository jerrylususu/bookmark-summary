Title: Just a nice shell script

URL Source: https://www.bitecode.dev/p/just-a-nice-shell-script

Published Time: 2025-08-12T22:32:57+00:00

Markdown Content:
_Despite all its flaws,_`curl -LsSf | sh`_is still a popular method to install dev tools, and those installer scripts pack a punch!_

_Today we are going to read a few excerpts from_`uv`_'s, an improved version of what cargo-dist provides out of the box._

_It got a little bit of everything for everybody: style, drama, humor, heart, twists, and executing a base64 inlined binary for China._

_Let's gooooooooo!_

I'm toying with the idea of making a quick and dirty UV-based installer for Python CLI programs, and in doing so, I'm having a look at the `curl | bash` script installers around here.

In the rust world, [cargo-dist](https://github.com/axodotdev/cargo-dist?tab=readme-ov-file) is the de facto tool to produce build artifacts. For convenience, one output it provides is a shell script to fetch the desired executable from Github and put it on your `PATH`.

An example of this at work is how you can install [ruff](https://docs.astral.sh/ruff/) on both Mac and Linux by running:

`curl -LsSf https://astral.sh/ruff/install.sh | sh`
(Assuming `curl` is installed. On debian-based distros, you have to get it first or use `wget`).

Of course, you should never, ever run code from the internet without looking at it first; and I certainly didn’t run countless such commands without checking if the script was sane, only trusting the provider's reputation and integrity for half of my career because that’s Pareto.

Unrelated to that, this week, I poured some homemade ice tea, and decided to lazily cruise through the lines of uv’s curl installer, hoping to catch some wisdom.

And damn, that's some nice script!

For this article, we'll focus on [this particular installer](https://github.com/astral-sh/uv/releases/latest/download/uv-installer.sh) version.

The rule of thumb when reading a shell script is to sample of few lines at the top to get a feeling of where you are at, then jump to the end to understand where you are going. Good news, this is also, by convention, where you'll find most often all utility functions in the bash world.

It starts with the usual boilerplate of shebang, the mandatory `set -u`, the litany of constant declarations and the [shellcheck](https://www.shellcheck.net/) policy (if you don't use shellcheck, do).

But it quickly steps up by noting:

```
# This runs on Unix shells like bash/dash/ksh/zsh. It uses the common `local`

# extension. Note: Most shells limit `local` to 1 var per line, contra bash.
```

So this tells us they support `bash`, `dash`, `ksh` and `zsh` and we are in for a lecture on shell compat and defensive programming.

The first hack is pretty sweet:

```
has_local() {
    local _has_local
}

has_local 2>/dev/null || alias local=typeset
```

They are going to use `local` var declarations, but that doesn't work with some `ksh` versions, so they make a fake one aliasing `typeset`. Clever.

I started giggling right about the [Some Linux distributions don't set HOME](https://github.com/astral-sh/uv/issues/6965#issuecomment-2915796022) comment. Somehow, I can feel the horror and the pain that went into discovering this issue and writing those lines:

```
get_home() {
    if [ -n "${HOME:-}" ]; then
        echo "$HOME"
    elif [ -n "${USER:-}" ]; then
        getent passwd "$USER" | cut -d: -f6
    else
        getent passwd "$(id -un)" | cut -d: -f6
    fi
}
```

Also, would it be easier to just always use `getent passwd "$(id -un)" | cut -d: -f6` ? Is it not available on all distros? Is it slow?

AI can't help you with this, it hallucinates very easily on those matters.

But that's also how the [UV_UNMANAGED_INSTALL](https://docs.astral.sh/uv/reference/installer/#unmanaged-installations) variable was introduced, letting you choose where it's going to be installed manually. So silver linings.

Having read the room, we can now rush to the `EOF`. We get to the entry point, which is basically making up a `main()` and calling it by proxying all args to it:

`download_binary_and_run_installer "$@" || exit 1`
What is it with script languages not having a feature to do this by default? Even in Python we have to `if __name__ == "__main__"` and at the very least `import sys`. This is silly, we should have a `@main` decorator that gives us:

```
@main() # builtin autocalling the function if in __main__
def _(sys): # instance of the sys module to get sys.args and sys.stderr
    return "Whatever" # passed to sys.exit
```

And all shell languages should have similar facilities.

I digress, the sweet part is that it's chock full of utility functions:

```
say() {
    # print stuff unless -q
}

say_verbose() {
    # don't print unless -v
}

warn() {
    # print stuff preffixed with WARN and in red
}

err() {
     # print stuff preffixed with ERR and in red
}

need_cmd() {
    # run this command, if you can't, the script can't 
    # continue so exit cleanly
}

check_cmd() {
    # so we have that stuff ?
}

assert_nz() {
    # this stuff should really not be empty
}

ensure() {
    # The script can't continue if this command fail,
    # so if it does, exit cleanly
}

ignore() {
    # thisisfine.jpg
}
```

So we got poor a man's log (a staple of all scripts), Unix cope, and catastrophic error recovery. Simple, clean, efficient. You can do a lot with those.

And the scripts really need that. Boy, does it need it. Like the main function, `download_binary_and_run_installer` starts with this jewel of a paranoid insurance policy:

```
need_cmd uname
    need_cmd mktemp
    need_cmd chmod
    need_cmd mkdir
    need_cmd rm
    need_cmd tar
    need_cmd grep
    need_cmd cat
```

Because, you know deep down, somehow, somewhere, some hellish spawn of a distro doesn't have `rm` just to raise a proud finger at the face of the universe.

In the same vein, `verify_checksum()` will not surprise you, but `downloader()` might break your little heart like it did mine.

Because I expected it to check if `curl` is available, and if not, fallback on `wget`. That's sad, but the reality is that Red Hat and Debian decided it was perfectly reasonable not to standardize on what downloader to have by default.

However, I didn't see the [Check if we have a broken snap curl](https://github.com/boukendesho/curl-snap/issues/1) snippet coming:

```
_snap_curl=0
if command -v curl > /dev/null 2>&1; then
  _curl_path=$(command -v curl)
  if echo "$_curl_path" | grep "/snap/" > /dev/null 2>&1; then
	_snap_curl=1
  fi
fi

if check_cmd curl && [ "$_snap_curl" = "0" ]
then _dld=curl
```

Basically, if you have `curl` but it's coming from a snap package (the name is going to be in the path), act like we don't have `curl`.

I hate snap. I hate it with a passion. It's always been broken, bloated, and slow. Nobody wants this tech. Canonical should own their mistake, trash this crap and move to providing both `.deb` and `flatpak` for everything.

Sorry, let's move on.

`get_architecture` is a bit gnarly, but that's to be expected given its job is hard. Apple doesn't make it easy as we can read that "Darwin `uname -m` can lie due to Rosetta shenanigans." or "Handling i386 compatibility mode in older macOS versions" but, I mean, they also try to accommodate CYGWIN, Solaris, and illumos (the latter has multi-arch userlands!). At some point, no pain, no gain, and they seem to be looking for serious gains.

I was expecting the "Detect 64-bit linux with 32-bit userland" to be worse, to be honest.

On the other hand, `check_loongarch_uapi` is kinda epic!

Let’s look at it.

[Loongson Technology](https://en.wikipedia.org/wiki/Loongson) is an interesting name to pop into. It's a Chinese company designing chips, mostly known in the Asian market. They have a strategic role to play for China, as they are the main actor that can create architectures unencumbered by Western IP. This makes it important to the country's tech sovereignty.

One of their CPU architecture, LoongArch, was shipped in some early commercial Linux distributions with a non-standard, vendor-specific implementation. This is what is referred as "old-world". An official ABI was eventually accepted upstream into the mainline Linux kernel, but it was incompatible with the previous one, here mentioned as "new-world".

This software only supports the standardized ABI, but to check on which one it runs, it has to do a system call you can't do from a shell.

The solution?

To embed an **inlined** full-blown [assembly written executable](https://gist.github.com/xen0n/5ee04aaa6cecc5c7794b9a0c3b65fc7f) in base 64, and run that:

```
# Minimal Linux/LoongArch UAPI detection, exiting with 0 in case of
    # upstream ("new world") UAPI, and 234 (-EINVAL truncated) in case 
    # of old-world (as deployed on several early commercial Linux 
    # distributions for LoongArch) [...]
    ignore base64 -d > "$_tmp" <<EOF
f0VMRgIBAQAAAAAAAAAAAAIAAgEBAAAAeAAgAAAAAABAAAAAAAAAAAAAAAAAAAAAQQAAAEAAOAAB
AAAAAAAAAAEAAAAFAAAAAAAAAAAAAAAAACAAAAAAAAAAIAAAAAAAJAAAAAAAAAAkAAAAAAAAAAAA
AQAAAAAABCiAAwUAFQAGABUAByCAAwsYggMAACsAC3iBAwAAKwAxen0n
EOF
```

Next time I'll get the stink eye because I inline a PNG into a `src` tag, I'll send them this.

Sometimes, the script is super delicate. For example, the `check_for_shadowed_bins` is something I rarely see in shell scripts and is quite considerate (it warns you if commands get priority over others in your `PATH` after the installation is done). The `install()` function itself assembles a lot of carefully crafted paths (both directory targets and binary import ones). They really care.

And then, sometimes it just brute force stuff by spraying `add_install_dir_to_path` liberally so that all supported shells get at least a mention.

Because geeks can't help themselves, there is an additional attempt at humor in doing so with the aptly named `shotgun_install_dir_to_path` that does it even with more abandon, for bash. With this one, all config files get the insert, not just the first one.

The idea is to add the binary installation directory to the `PATH` in as many files as possible, including, but not limited to: `.profile`, `.bashrc`, `.bash_profile`, `.bash_login`, `.zshrc`, `.zshenv` and all `.env.fish` files under the sun, in all folders those might exist if we have the permissions to do so.

You can disable that with `NO_MODIFY_PATH` and it's idempotent, but it's still pretty funny to read how much hammering is sometimes necessary to ensure something as simple as a command being callable.

There is also something quite intoxicating about reading the `case` statement in `select_archive_for_arch`, `aliases_for_binary` and `json_binary_aliases` as they make up for 500 lines of the 2000 of this beauty. Combinatorics are cruel.

I don't enjoy writing shell scripts, not one bit. It's not just the idiosyncrasies of the language and platform, but it's also the fact that you need to do so much stuff manually, every time.

Like they have only 4 arguments to this script, and yet, to get decent argument parsing, they need to do:

```
for arg in "$@"; do
        case "$arg" in
            --help)
                usage
                exit 0
                ;;
            --quiet)
                PRINT_QUIET=1
                ;;
            --verbose)
                PRINT_VERBOSE=1
                ;;
            --no-modify-path)
                say "--no-modify-path has been deprecated; please set UV_NO_MODIFY_PATH=1 in the environment"
                NO_MODIFY_PATH=1
                ;;
            *)
                OPTIND=1
                if [ "${arg%%--*}" = "" ]; then
                    err "unknown option $arg"
                fi
                while getopts :hvq sub_arg "$arg"; do
                    case "$sub_arg" in
                        h)
                            usage
                            exit 0
                            ;;
                        v)
                            PRINT_VERBOSE=1
                            ;;
                        q)
                            PRINT_QUIET=1
                            ;;
                        *)
                            err "unknown option -$OPTARG"
                            ;;
                        esac
                done
                ;;
        esac
    done
```

And then proceed to write the whole help text manually in a separate `usage()` function, that you have to remember to maintain.

This is so much better:

```
import sys
import argparse

parser = argparse.ArgumentParser(doc=__doc__)
parser.add_argument('-q', '--quiet', action='store_true' )
parser.add_argument('-v', '--verbose', action='store_true' )
parser.add_argument('--no-modify-path', action='store_true')

args = parser.parse_args()

if args.no_modify_path:
  print("--no-modify-path has been deprecated; please set UV_NO_MODIFY_PATH=1 in the environment", file=sys.stderr)
```

In fact, the whole script is about 40% shorter in fully typed Python, while being way easier to navigate.

Don't ask how I know that.

But the original script will work no matter how many lemons you throw at it, inside a toaster running a hacky port of busybox riding a Chinese proprietary RISC CPU.

And the beauty of it is, it will let you install `uv` and therefore, Python, next.