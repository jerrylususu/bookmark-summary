Title: The bottom emoji breaks rust-analyzer

URL Source: https://fasterthanli.me/articles/the-bottom-emoji-breaks-rust-analyzer

Published Time: 2023-02-13T14:20:00Z

Markdown Content:
![Image 1](https://cdn.fasterthanli.me/content/articles/the-bottom-emoji-breaks-rust-analyzer/_thumb~a475a12cf5f15197.jxl)

👋 This page was last updated ~2 years ago. Just so you know.

Some bugs are merely fun. Others are simply delicious!

Today’s pick is the latter.

[Reproducing the issue, part 1 -----------------------------](https://fasterthanli.me/articles/the-bottom-emoji-breaks-rust-analyzer#reproducing-the-issue-part-1)(It may be tempting to skip that section, but reproducing an issue is an important part of figuring it out, so.)

I’ve never used Emacs before, so let’s install it. I do most of my computing on an era-appropriate Ubuntu, today it’s Ubuntu 22.10, so I just need to:

```
$ sudo apt install emacs-nox
```

And then create a new Rust crate, `cd` into it, and launch emacs:

```
$ cargo new bottom
     Created binary (application) `bottom` package
$ cd bottom/
$ emacs
```

I am greeted with a terminal interface that says: “Welcome to GNU Emacs, one component of the GNU/Linux operating system”. I feel [religious](https://www.gnu.org/fun/jokes/gospel.html) already.

To open `src/main.rs`, I can press `C-x C-f`, where `C-` means `Ctrl+` (and `M-` means `Alt+`, at least for me), which opens a “Find file” prompt at the bottom, pre-filled with the current working directory: for me that’s `~/bearcove/bottom`.

There’s tab-completion in there, so `s<TAB>m<TAB>` completes it to `.../src/main.rs`, and pressing Enter (which I understand Emacs folks spell `RET`, for Return) opens the file.

Without additional configuration, not much happens: there’s no syntax highlighting, no code intelligence of any kind, we have to ask for that.

So let’s ask for that.

With guidance from a friend (on IRC, of all places! what year is this?), I ended up putting the following in my `~/.emacs` file:

(The bit at the bottom was there originally, I’m guessing Ubuntu ships it? It didn’t have `lsp-ui` / `rustic` / `lsp-mode` before I restarted emacs).

Restarting emacs installs everything, just like Vim plug-in managers would do, so far, so good.

Opening `src/main.rs` again prompts me to import a workspace root, I pick the first option, which seems reasonable, and tada, we have Rust highlighting and inline documentation and stuff!

![Image 2: Windows Terminal screenshot showing emacs open on a Rust hello world source file](https://cdn.fasterthanli.me/content/articles/the-bottom-emoji-breaks-rust-analyzer/assets/emacs~abb86632f43d5091.jxl)

Or rather, I do, because I have a `rust-analyzer` binary in path from a while ago (I contribute occasionally):

```
$ which rust-analyzer
/home/amos/.cargo/bin/rust-analyzer

$ rust-analyzer --version
rust-analyzer 0.0.0 (caf23f291 2022-07-11)
```

This is old. [rust-analyzer](https://rust-analyzer.github.io/) is released every week. Let’s remove it and see if things still work.

```
$ rm $(which rust-analyzer)

$ emacs src/main.rs

(cut)
Server rls:83343/starting exited (check corresponding stderr buffer
for details). Do you want to restart it? (y or n)
```

Ah. It doesn’t. That’s unfortunate!

[How rust-analyzer is distributed --------------------------------](https://fasterthanli.me/articles/the-bottom-emoji-breaks-rust-analyzer#how-rust-analyzer-is-distributed)Rust components are normally distributed with `rustup`. `rustc` is a Rust component, so, it is:

```
$ which rustc
/home/amos/.cargo/bin/rustc

$ rustc -V
rustc 1.67.1 (d5a82bbd2 2023-02-07)

$ rustup show active-toolchain
stable-x86_64-unknown-linux-gnu (default)

$ rustup which rustc
/home/amos/.rustup/toolchains/stable-x86_64-unknown-linux-gnu/bin/rustc

$ ~/.rustup/toolchains/stable-x86_64-unknown-linux-gnu/bin/rustc -V
rustc 1.67.1 (d5a82bbd2 2023-02-07)
```

You can also get it from elsewhere, and I’m sure you have your reasons, but they’re not relevant to the topic at hand.

After rust-analyzer was promoted from “very useful peripheral project” to [official rust-lang project](https://blog.rust-lang.org/2022/02/21/rust-analyzer-joins-rust-org.html), it started being distributed as a rustup component.

Back then, it was done by it being a git submodule in the [rust-lang/rust](http://github.com/rust-lang/rust) repository. Since then, it’s been [migrated to a git subtree](https://github.com/rust-lang/rust/pull/99603), which helped resolve the [rust-analyzer support for proc macros in Rust nightly](https://fasterthanli.me/articles/proc-macro-support-in-rust-analyzer-for-nightly-rustc-versions) issue.

Why do we care? Because that means there’s technically two trees for rust-analyzer at any given moment in time: a git subtree can (and should) be merged in _either direction_: ra-\>rust because ra moves fast and is developed mostly in its own repository, and rust-\>ra because the proc-macro bridge might change.

So! We can install `rust-analyzer` with rustup:

```
$ rustup component add rust-analyzer
info: downloading component 'rust-analyzer'
info: installing component 'rust-analyzer'
```

But that doesn’t set up a “proxy binary” under `~/.cargo/bin`:

```
$ which rust-analyzer

(it prints nothing)
```

It is, however, somewhere on disk:

```
$ rustup which rust-analyzer
/home/amos/.rustup/toolchains/stable-x86_64-unknown-linux-gnu/bin/rust-analyzer
```

We can even try it out ourselves by launching it, and typing `{}` then Enter/Return:

```
$ ~/.rustup/toolchains/stable-x86_64-unknown-linux-gnu/bin/rust-analyzer
{}
[ERROR rust_analyzer] Unexpected error: expected initialize request, got error: receiving on an empty and disconnected channel
expected initialize request, got error: receiving on an empty and disconnected channel

```

That’s right! It’s our old friend JSON-over-stdin.

Since this is a reasonable way in which users might want to install rust-analyzer, let’s see if our emacs setup picks it up:

```
$ emacs src/main.rs
(cut)
Server rls:86574/starting exited (check corresponding stderr buffer for details).
Do you want to restart it? (y or n)
```

No. This is unfortunate, again.

And even if it _did_ work, it would still not be ideal, because… that version is old too:

```
$ $(rustup which rust-analyzer) --version
rust-analyzer 1.67.1 (d5a82bb 2023-02-07)
```

Okay.. that one’s only a few days old, but only because Rust 1.67.0 did an [oopsie-woopsie when it comes to thin archives](https://blog.rust-lang.org/2023/02/09/Rust-1.67.1.html#whats-in-1671-stable) and they had to release 1.67.1 shortly after.

But yeah, if we check the version shipped with Rust 1.67.0:

```
$ $(rustup +1.67.0 which rust-analyzer) --version
rust-analyzer 1.67.0 (fc594f1 2023-01-24)
```

It’s from around that time. And that hash refers to a a commit in [rust-lang/rust](https://github.com/rust-lang/rust/commits/fc594f1), not `rust-lang/rust-analyzer`, so depending when the the last sync has been made, it might be even further behind.

rust-analyzer wants to ship every monday, and so, it does! At the time of this writing, the latest release is from 2023-02-13, and it’s [on GitHub](https://github.com/rust-lang/rust-analyzer/releases/tag/2023-02-13), which is where the VSCode extension _used_ to download it from.

These days, it ships the rust-analyzer binary directly in the extension:

```
$ unzip -l rust-lang.rust-analyzer-0.4.1398@linux-x64.vsix
Archive:  rust-lang.rust-analyzer-0.4.1398@linux-x64.vsix
  Length      Date    Time    Name
---------  ---------- -----   ----
     2637  2023-02-10 00:29   extension.vsixmanifest
      462  2023-02-10 00:29   [Content_Types].xml
    15341  2023-02-09 18:46   extension/icon.png
     1036  2023-02-09 18:46   extension/language-configuration.json
    12006  2023-02-09 18:46   extension/LICENSE.txt
   415788  2023-02-10 00:29   extension/out/main.js
   298705  2023-02-09 18:46   extension/package-lock.json
    86857  2023-02-10 00:29   extension/package.json
      756  2023-02-09 18:46   extension/ra_syntax_tree.tmGrammar.json
     2422  2023-02-10 00:29   extension/README.md
 41073816  2023-02-10 00:29   extension/server/rust-analyzer
   648798  2023-02-10 00:29   extension/node_modules/d3-graphviz/build/d3-graphviz.min.js
   279449  2023-02-10 00:29   extension/node_modules/d3/dist/d3.min.js
---------                     -------
 42838073                     13 files
```

But other editor plug-ins, like [coc-rust-analyzer](https://github.com/fannheyward/coc-rust-analyzer), download it [right from GitHub releases](https://github.com/fannheyward/coc-rust-analyzer/blob/4a7ea2d7c3ba866d257b958175f4149823bc3a8f/src/downloader.ts).

It seemed odd that the Emacs ecosystem would lack such functionality, so I looked it up: `rustic` says about automatic server installation that [lsp-mode provides this feature, but eglot doesn’t](https://github.com/brotzeit/rustic#automatic-server-installation), and then it says “Install rust-analyzer manually”.

In lsp-mode, I found code that [seems like it should download rust-analyzer](https://github.com/emacs-lsp/lsp-mode/blob/781889628b9e0504fde279371548149deae4849d/clients/lsp-rust.el#L894-L905), but I’m not sure how to use it.

The docs talk about an `lsp-enable-suggest-server-download` option, which [defaults to true](https://emacs-lsp.github.io/lsp-mode/page/settings/mode/#lsp-enable-suggest-server-download), but I’ve never seen it download the server (I know because I checked `~/.emacs.d/.cache/lsp`).

Although… now that I look at it closer, this error message:

```
Server rls:83343/starting exited (check corresponding stderr buffer
for details). Do you want to restart it? (y or n)
```

Mentions `rls`, which is the predecessor to `rust-analyzer`, and that definitely sounds wrong. But `lsp-rust-server` defaults to `rust-analyzer`, so.. is it just falling back? Setting the option explicitly doesn’t seem to change much.

After more Emacs learning, I discovered how to switch to the `*lsp-log*` buffer [the docs point to](https://emacs-lsp.github.io/lsp-mode/page/troubleshooting/) and discovered the following:

```
Command "rls" is present on the path.
Command "rust-analyzer" is not present on the path.
Command "rls" is present on the path.
Command "rust-analyzer" is not present on the path.
Found the following clients for /home/amos/bearcove/bottom/src/main.rs: (server-id rls, priority -1)
The following clients were selected based on priority: (server-id rls, priority -1)
```

This is a _horrible_ fallback. RLS [is deprecated](https://github.com/rust-lang/rls#%EF%B8%8F-rls-is-no-longer-supported). The only reason it’s falling back to it is because there _is_ a proxy binary for it, that exists, but errors out since the component is not installed:

```
$ which rls
/home/amos/.cargo/bin/rls

$ rls
error: 'rls' is not installed for the toolchain 'stable-x86_64-unknown-linux-gnu'
To install, run `rustup component add rls`

$ echo $?
1
```

Let’s summarize the situation:

*   rustup is the “blessed” way to get a rust toolchain (you can do nice things like [pinning](https://rust-lang.github.io/rustup/overrides.html#the-toolchain-file) with it)
*   it sets up an `rls` proxy binary under `~/.cargo/bin` like it should, because even though rls is deprecated, some folks still use it for now I guess
*   `lsp-mode` looks for `rust-analyzer` first, `rls` second, and if it finds the second (even if it’s just a stub/proxy that says “sorry not installed”), it falls back to it and the “auto download rust-analyzer” logic never triggers

I must admit this is an even bigger deal than what I was originally planning to write about! If this is the experience Emacs folks have been having with Rust, this explains a lot of things.

My sample size is N=3, but everyone in that sample ended up building rust-analyzer from source, and that means they get an extremely up-to-date RA once, and then most probably forget to update it forever, which is even worse than grabbing it from rustup.

Please remind me to submit a PR to `lsp-mode` that yanks ALL the rls stuff after I’m done writing this article. Someone must.

ANYWAY.

For today, let’s just tell `lsp-mode` to use the one from rustup:

```
_;; under (use-package lsp-mode
__;; in the :custom block
_  (lsp-rust-analyzer-server-command (list (string-trim (shell-command-to-string _"rustup which rust-analyzer"_))))
```

Just kidding! That doesn’t work. And yes, that evaluates to the right path. And yes, that “custom” option expects a list. And yes, I did learn what `custom-set-variables` does while troubleshooting this, and no, setting it through there doesn’t work either.

The `*Messages*` buffer still shows that it couldn’t find `rust-analyzer` in PATH.

My best guess is that `rustic`, which can use either `lsp-mode` or `eglot`, overrides this very late in the game, and I can’t do a damn thing about it. I’m not sure why they even have an “Automatic server installation” section in their docs then.

So. Fine. We’ll use violence and create a shell script in `~/.cargo/bin/rust-analyzer`, containing this:

```
#!/bin/bash

$(rustup which rust-analyzer) "$@"
```

```
$ chmod +x ~/.cargo/bin/rust-analyzer
$ hash -r
$ rust-analyzer --version
rust-analyzer 1.67.1 (d5a82bb 2023-02-07)

```

Tada, we did a crime!

[Reproducing the issue, part 2 -----------------------------](https://fasterthanli.me/articles/the-bottom-emoji-breaks-rust-analyzer#reproducing-the-issue-part-2)So, now that we have emacs configured with lsp-mode and rustic, using a recent-ish rust-analyzer, we’re back to square one.

Note that I forgot to add [company-mode](https://company-mode.github.io/), the thing that actually provides completions: we can add it next to `(use-package rustic)` in `~/.emacs`:

```
_;; in `~/.emacs`
_
_;; cut: everything before that line
_
(require _'_use-package-ensure)
(setq use-package-always-ensure t)

(use-package rustic)
_;; 👇 new!
_(use-package company-mode)
```

Restarting emacs installs it, and we now get completions “after typing a few characters and waiting a bit”. You can bind a key combination to “company-complete” to have it pop up on-demand, which I did, and then Emacs told me “no, you shouldn’t write it `C-SPC`, you should write it `[?\C- ]`”, which is exceedingly rude, but let’s move on.

(The keybinding didn’t work in the terminal but it did work in emacs-gtk, which I installed out of frustration).

Anyway!

Now onto the actual bug: let’s add to our code.. an emoji! Any emoji.

```
_fn_ _main__(__)_ _{_
  _// 🥺_
  _println__!__(__"Hello, world!"__)__;_
_}_
```

Upon typing this emoji in the editor, a message will pop up in the bottom bar (appropriate) saying the LSP server crashed, would you like to restart it, no I wouldn’t, I’d like to see the messages, a little `C-x b *rust-anal<TAB>::std<TAB>` later I’m in buffer `*rust-analyzer::stderr*` seeing this:

```
Panic context:
>
version: 1.67.1 (d5a82bb 2023-02-07)
notification: textDocument/didChange

thread 'LspServer' panicked at 'assertion failed: self.is_char_boundary(n)', /rustc/d5a82bbd26e1ad8b7401f6a718a9c57c96905483/library/alloc/src/string.rs:1819:29
stack backtrace:
   0: rust_begin_unwind
             at /rustc/d5a82bbd26e1ad8b7401f6a718a9c57c96905483/library/std/src/panicking.rs:575:5
   1: core::panicking::panic_fmt
             at /rustc/d5a82bbd26e1ad8b7401f6a718a9c57c96905483/library/core/src/panicking.rs:64:14
   2: core::panicking::panic
             at /rustc/d5a82bbd26e1ad8b7401f6a718a9c57c96905483/library/core/src/panicking.rs:111:5
   3: <alloc::string::String>::replace_range::<core::ops::range::Range<usize>>
   4: rust_analyzer::lsp_utils::apply_document_changes::<<rust_analyzer::global_state::GlobalState>::on_notification::{closure#3}::{closure#0}>
   5: <<rust_analyzer::global_state::GlobalState>::on_notification::{closure#3} as core::ops::function::FnOnce<(&mut rust_analyzer::global_state::GlobalState, lsp_types::DidChangeTextD\
ocumentParams)>>::call_once
   6: <rust_analyzer::dispatch::NotificationDispatcher>::on::<lsp_types::notification::DidChangeTextDocument>
   7: <rust_analyzer::global_state::GlobalState>::handle_event
   8: <rust_analyzer::global_state::GlobalState>::run
   9: rust_analyzer::main_loop::main_loop
  10: rust_analyzer::run_server
note: Some details are omitted, run with `RUST_BACKTRACE=full` for a verbose backtrace.

Process rust-analyzer stderr finished
```

_That_ is the bug we’re interested in.

And if you have some instinct as to the source of this bug, let me tell you: it’s so much worse than you think.

[Exploring UTF-8 and UTF-16 with Rust ------------------------------------](https://fasterthanli.me/articles/the-bottom-emoji-breaks-rust-analyzer#exploring-utf-8-and-utf-16-with-rust)Rust strings are UTF-8, period.

And by “Rust strings” I mean the owned type [String](https://doc.rust-lang.org/stable/std/string/struct.String.html) and string slices, aka [&str](https://doc.rust-lang.org/stable/std/primitive.str.html).

There’s a ton of other types that dereference to `str`, like `Box<str>`, `Arc<str>` etc., but they’re not relevant to this discussion.

We can tell by printing the underlying byte representation:

```
_fn_ _main__(__)_ _{_
    _println__!__(__"{:02x?}"__,_ _"abc"__.__as_bytes__(__)__)__;_
_}_
```

```
$ cargo run --quiet
[61, 62, 63]
```

Which is not to say that you cannot use UTF-16 string representation in Rust, you just.. make your own type for it. Or, more likely, you use a crate, like [widestring](https://lib.rs/crates/widestring):

```
$ cargo add widestring
    Updating crates.io index
      Adding widestring v1.0.2 to dependencies.
             Features:
             + alloc
             + std
```

```
_fn_ _main__(__)_ _{_
    _// this is a macro, it does the right thing_
    _let_ s = widestring_::_u16str!_(__"abc"__)__;_
    _println__!__(__"{:04x?}"__,_ s_.__as_slice__(__)__)__;_
_}_
```

This gives us a `&[u16]`, so it’s not quite what we’re looking for:

```
$ cargo run --quiet
[0061, 0062, 0063]
```

Getting at the bytes is harder, but not impossible:

```
_fn_ _main__(__)_ _{_
    _// this is a macro, it does the right thing_
    _let_ s = widestring_::_u16str!_(__"abc"__)__;_
    _{_
        _let_ u16s = s_.__as_slice__(__)__;_
        _let_ _(___,_ u8s_,_ __)_ = _unsafe_ _{_ u16s_.__align_to__::__<__u8__>__(__)_ _}__;_
        _println__!__(__"{:02x?}"__,_ u8s_)__;_
    _}_
_}_
```

Heck, it shouldn’t even _really_ require unsafe, since anything that’s u16-aligned is also definitely u8-aligned, here, let me make a safe wrapper for it:

```
_fn_ _u16_slice_to_u8_slice__(__s__:_ _&__[__u16__]__)_ -> _&__[__u8__]_ _{_
    _unsafe_ _{_
        _// Safety: u8 slices don't require any alignment, it really doesn't_
        _// get any smaller without bit-twiddling_
        s_.__align_to__::__<__u8__>__(__)__.__1_
    _}_
_}_
```

There:

```
_fn_ _main__(__)_ _{_
    _// this is a macro, it does the right thing_
    _let_ s = widestring_::_u16str!_(__"abc"__)__;_
    _{_
        _let_ u16s = s_.__as_slice__(__)__;_
        _let_ u8s = _u16_slice_to_u8_slice__(_u16s_)__;_
        _println__!__(__"{:02x?}"__,_ u8s_)__;_
    _}_
_}_
```

```
$ cargo run --quiet
[61, 00, 62, 00, 63, 00]
```

Okay, cool! So utf-16 is just utf-8 with extra zeroes.

![Image 3: Cool bear](https://cdn.fasterthanli.me/content/img/reimena/cool-bear-neutral~206d206a2216de47.jxl)

No, that’s… no.

No, of course not. It’s easy with ASCII characters, but it gets more complicated the fancier you want to get.

How about “é” for example. That sounds fancy! How does it look?

```
_const_ S_:_ _&__str_ = _"é"__;_

_fn_ _main__(__)_ _{_
    _println__!__(__"{S:?}"__)__;_
    _println__!__(__"UTF-8   {:02x?}"__,_ S_.__as_bytes__(__)__)__;_
    _println__!__(_
        _"UTF-16  {:02x?}"__,_
        _u16_slice_to_u8_slice__(__(_widestring_::_u16str!_(_S_)__)__.__as_slice__(__)__)_
    _)__;_
_}_

_fn_ _u16_slice_to_u8_slice__(__s__:_ _&__[__u16__]__)_ -> _&__[__u8__]_ _{_
    _unsafe_ _{_
        _// Safety: u8 slices don't require any alignment, it really doesn't_
        _// get any smaller without bit-twiddling_
        s_.__align_to__::__<__u8__>__(__)__.__1_
    _}_
_}_
```

```
$ cargo run -q
"é"
UTF-8   [c3, a9]
UTF-16  [e9, 00]
```

Ah, not fancy enough! It takes up 2 bytes in UTF-8, and one “code unit” in UTF-16, which we’re showing as two bytes, because we can.

Let’s try something fancier!

```
$ cargo run -q
"œ"
UTF-8   [c5, 93]
UTF-16  [53, 01]
```

“Latin Small Ligature Oe” is in the [Latin Extended-A](https://unicode-table.com/en/0153/) range: that goes `0100-017F`. We no longer have a “useless byte” in the UTF-16 encoding, since the code unit is actually “0153” (in hexadecimal).

Meanwhile, in UTF-8 land, we still need two bytes to encode it. All is well.

Let’s get fancier still! How about some Hiragana? (`3040-309F`)

```
$ cargo run -q
"ぁ"
UTF-8   [e3, 81, 81]
UTF-16  [41, 30]
```

“Hiragana Letter Small A” takes 3 bytes in UTF-8, but only 2 bytes (one 16-bit code unit) in UTF-16. Huh! That must be why people loved UTF-16 so much, they made it the default string representation [for Java](https://devdocs.io/openjdk~8/java/lang/string) _and_ [JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String#utf-16_characters_unicode_codepoints_and_grapheme_clusters) (no relation).

Because at some point in the history of the human race, we thought 65536 characters were _more than enough_. It would be _absurd_ to need more characters than that. And so we made UCS-2, which used two bytes for every character, enabling the encoding of the BMP, the [Basic Multilingual Plane](https://en.wikipedia.org/wiki/Universal_Coded_Character_Set#Encoding_forms).

But that’s a lie. We knew 65536 characters weren’t enough, because China.

(Among other reasons).

So there were already 1.1 million characters defined by Unicode, and some of those wouldn’t fit, and so we made UCS-4, which used four bytes for every character, but that sounds _terribly wasteful_ compared to plain old ASCII-with-a-codepage-good-luck-exporting-documents I guess.

So ISO/IEC 2022 specifies escape sequences to _switch between character sets_. I wish I was making it up, but [I’m not](https://en.wikipedia.org/wiki/ISO/IEC_2022#Character_set_designations)! Apparently xterm supports some of it! I know!!! I can’t believe it either!

So anyway, UTF-16 is an evolution of UCS-2 that says hey maybe switching character encodings in-band isn’t the greatest thing (also I’m not sure how widely adopted those escape sequences were in the first place), let’s just have a thing where _most_ characters fit in 2 bytes, and those that don’t fit in.. more.

So let’s look at our Hiragana again but simply print UTF-16 code units now, instead of the underlying two bytes:

```
_const_ S_:_ _&__str_ = _"ぁ"__;_

_fn_ _main__(__)_ _{_
    _println__!__(__"{S:?}"__)__;_
    _println__!__(__"UTF-8   {:02x?}"__,_ S_.__as_bytes__(__)__)__;_
    _println__!__(__"UTF-16  {:02x?}"__,_ _(_widestring_::_u16str!_(_S_)__)__.__as_slice__(__)__)__;_
_}_
```

```
$ cargo run -q
"ぁ"
UTF-8   [e3, 81, 81]
UTF-16  [3041]
```

Okay, cool, so: for U+3041, we need 3 bytes in UTF-8, and one UTF-16 code unit (2 bytes).

Let us now embark on a cross-plane journey:

```
$ cargo run -q
"𠀀"
UTF-8   [f0, a0, 80, 80]
UTF-16  [d840, dc00]
```

But first, a minute of silence for anyone reading this from a Linux desktop machine.

…

There. In case you can’t see it, the character in question is [Ideograph the sound made by breathing in; oh! (cf. U+311B BOPOMOFO LETTER O, which is derived from this character) CJK](https://unicode-table.com/en/20000/), or “hē”, for friends.

It is U+20000, which is outside the BMP.

![Image 4: Cool bear](https://cdn.fasterthanli.me/content/img/reimena/cool-bear-neutral~206d206a2216de47.jxl)

The?

BMP, [Basic Multilingual Plane](https://en.wikipedia.org/wiki/Plane_(Unicode)#Basic_Multilingual_Plane), we’ve gone over this: it’s `0000-FFFF`, except… except part of it is reserved for UTF-16 surrogates! High surrogates are `D800-DB7F`, and surprise surprise, that’s what our first code unit is: `d840`. Low surrogates are `DC00-DFFF`, and that’s what our second code unit is.

How does this work? Well, we take our codepoint, in our case `U+20000`, and subtract 0x10000 from it. We get `0x10000`, or, in binary:

```
 0b00010000000000000000
   <--------><-------->
       hi        lo
```

Then we take the high ten bits, add them to `0xD800`, in our case, `0b1000000` gives `0x40`, so we get `0xD840`. As for the low ten bits, we add them to `0xDC00`, for us that’s 0x0 (should’ve picked a different example), so we get `0xDC00`.

Easy peasy.

And so, “𠀀” (which should render as ![Image 5: he](https://cdn.fasterthanli.me/content/articles/the-bottom-emoji-breaks-rust-analyzer/assets/he~a4395e65b08b813b.jxl)) is:

*   1 [grapheme cluster](https://en.wikipedia.org/wiki/Universal_Character_Set_characters#Characters%2C_grapheme_clusters_and_glyphs)
*   1 unicode character (with the unicode code point U+20000)
*   4 UTF-8 bytes
*   2 UTF-16 code units

All clear? Good.

How about our emoji? Our innocent little emoji? Look at it. It didn’t mean to cause any trouble. Let’s find out:

```
$ cargo run -q
"🥺"
UTF-8   [f0, 9f, a5, ba]
UTF-16  [d83e, dd7a]
```

Okay, same! Ooh I bet we can find what codepoint it is by doing the inverse transformation on the UTF-16 surrogate pair here:

```
$ gdb --quiet
(cut)
(gdb) p/x 0xd83e - 0xd800
$1 = 0x3e
(gdb) p/x 0xdd7a - 0xdc00
$2 = 0x17a
```

![Image 6: Cool bear](https://cdn.fasterthanli.me/content/img/reimena/cool-bear-neutral~206d206a2216de47.jxl)

_That’s_ your hex calculator of choice?

![Image 7: Amos](https://cdn.fasterthanli.me/content/img/reimena/amos-neutral~7ef5a72ffb0f390c.jxl)

Shh I’m trying to focus here.

```
(continued)

(gdb) p/t 0x3e
$3 = 111110
(gdb) p/t 0x17a
$4 = 101111010
```

![Image 8: Cool bear](https://cdn.fasterthanli.me/content/img/reimena/cool-bear-neutral~206d206a2216de47.jxl)

Wait wait why are you going through binary, you can just do a left shift here, right?

![Image 9: Amos](https://cdn.fasterthanli.me/content/img/reimena/amos-neutral~7ef5a72ffb0f390c.jxl)

Yes, yes, alright

```
(continued)

(gdb) p/x (0x3e << 10) + 0x17a + 0x10000
$5 = 0x1f97a
```

Hurray, here it is! [U+1F97A Bottom Face Emoji](https://unicode-table.com/en/1F97A/).

So. Rust really likes UTF-8, and so do I. Hence, I really like Rust.

Whereas some languages just do not let you mutate strings at all (it’s safer that way), Rust does! You can totally do this, for example:

```
_fn_ _main__(__)_ _{_
    _let_ _mut_ s = _String__::__from__(__"amos"__)__;_
    s_.__replace_range__(__0_.._1__,_ _"c"__)__;_
    _dbg__!__(_s_)__;_
_}_
```

```
$ cargo run -q
[src/main.rs:4] s = "cmos"
```

Note that this is safe rust!

Also note that Amos is my first name, and [CMOS](https://en.wikipedia.org/wiki/CMOS) is a type of metal-oxide-semiconductor field-effect transistor fabrication process that uses complementary and symmetrical pairs of p-type and n-type MOSFETs for logic functions.

Coincidence? Probably.

We can also do this, using unsafe Rust:

```
_fn_ _main__(__)_ _{_
    _let_ _mut_ s = _String__::__from__(__"amos"__)__;_
    _// why b'c'? because 'c' is a char, whereas b'c' is a u8 (a byte)._
    _unsafe_ _{_ s_.__as_bytes_mut__(__)__[__0__]_ = _b'c'_ _}__;_
    _dbg__!__(_s_)__;_
_}_
```

And we get the same output.

Which begs the question, why is the former safe and the latter unsafe, if they do the same darn thing!

It’s because they don’t.

The unsafe version lets us do this:

```
_fn_ _main__(__)_ _{_
    _let_ _mut_ s = _String__::__from__(__"🥺"__)__;_
    _unsafe_ _{_
        s_.__as_bytes_mut__(__)__[__3__]_ = _b'#'__;_
    _}__;_
    _dbg__!__(_s_)__;_
_}_
```

```
$ cargo run --quiet
[src/main.rs:6] s = "�#"
```

Which is, say it with me: undefined behaviorrrr ooooh spooky ghost emoji! We broke an invariant (strings must always be valid UTF-8) and now anything goes, we could even have memory corruption come out of this! Probably!

Them’s the rules of unsafe Rust: if we use it, we are suddenly responsible for maintaining all the invariants ourselves. Just like we are, all the time, in unsafe languages like C/C++ (also C, and C++).

`replace_range` does not let us do that:

```
_fn_ _main__(__)_ _{_
    _let_ _mut_ s = _String__::__from__(__"🥺"__)__;_
    s_.__replace_range__(__3_.._4__,_ _"#"__)__;_
    _dbg__!__(_s_)__;_
_}_
```

```
$ cargo run --quiet
thread 'main' panicked at 'assertion failed: self.is_char_boundary(n)', /rustc/d5a82bbd26e1ad8b7401f6a718a9c57c96905483/library/alloc/src/string.rs:1811:29
note: run with `RUST_BACKTRACE=1` environment variable to display a backtrace
```

Well well well, doesn’t that look familiar.

Again with a backtrace:

```
$ RUST_BACKTRACE=1 cargo run --quiet
thread 'main' panicked at 'assertion failed: self.is_char_boundary(n)', /rustc/d5a82bbd26e1ad8b7401f6a718a9c57c96905483/library/alloc/src/string.rs:1811:29
stack backtrace:
   0: rust_begin_unwind
             at /rustc/d5a82bbd26e1ad8b7401f6a718a9c57c96905483/library/std/src/panicking.rs:575:5
   1: core::panicking::panic_fmt
             at /rustc/d5a82bbd26e1ad8b7401f6a718a9c57c96905483/library/core/src/panicking.rs:64:14
   2: core::panicking::panic
             at /rustc/d5a82bbd26e1ad8b7401f6a718a9c57c96905483/library/core/src/panicking.rs:111:5
   3: alloc::string::String::replace_range
             at /rustc/d5a82bbd26e1ad8b7401f6a718a9c57c96905483/library/alloc/src/string.rs:1811:29
   4: bottom::main
             at ./src/main.rs:3:5
   5: core::ops::function::FnOnce::call_once
             at /rustc/d5a82bbd26e1ad8b7401f6a718a9c57c96905483/library/core/src/ops/function.rs:507:5
note: Some details are omitted, run with `RUST_BACKTRACE=full` for a verbose backtrace.
```

Yep okay this is _definitely_ familiar.

![Image 10: Cool bear](https://cdn.fasterthanli.me/content/img/reimena/cool-bear-neutral~206d206a2216de47.jxl)

So this is what’s happening with lsp-mode + rust-analyzer, right?

lsp-mode is sending bad offsets, rust-analyzer panics. Mystery solved?

Well, yes. But why does that happen? And what should rust-analyzer actually do in this case?

[The Language Server Protocol ----------------------------](https://fasterthanli.me/articles/the-bottom-emoji-breaks-rust-analyzer#the-language-server-protocol)To answer these questions, we must look at the LSP: the [Language Server Protocol](https://microsoft.github.io/language-server-protocol/).

And instead of reading the spec directly, let’s look at what’s _actually_ being sent between an LSP client (like lsp-mode for Emacs) and an LSP server (like rust-analyzer).

There’s something built into lsp-mode to do this, the `lsp-log-io` setting, but I think it’s a lot more fun to capture it ourselves, by providing a wrapper for rust-analyzer.

```
// in `src/main.zig`

_const_ _std_ = @import_(_"std"_)__;_
_const_ _ChildProcess_ = _std__.__ChildProcess__;_
_const_ _StdIo_ = _ChildProcess__.__StdIo__;_
_const_ _File_ = _std__._fs_.__File__;_
_const_ _Thread_ = _std__.__Thread__;_

_const_ _DEBUG_ = false_;_
_const_ _DEBUG_LEAKS_ = false_;_
_const_ _CLEANUP_STREAMS_WORKAROUND_NAME_ = ".cleanupStreamsWorkaround"_;_

_fn_ _debug__(__comptime_ fmt_:_ _[__]__const_ _u8__,_ args_:_ _anytype__)_ _void_ _{_
    if _(__DEBUG__)_ _{_
        _std__._debug_.__print__(__fmt__,_ _args__)__;_
    _}_
_}_

_pub_ _fn_ _main__(__)_ !_void_ _{_
    _var_ _alloc__:_ _std__._mem_.__Allocator_ = _undefined__;_ // like the behavior

    _var_ _gpa__:_ _?__std__._heap_.__GeneralPurposeAllocator__(__.__{__}__)_ = _undefined__;_
    // this `defer` cannot live inside the `if DEBUG_LEAKS` block, because then
    // the allocator would be deinitialized before our program even runs.
    _defer_ if _(__gpa__)_ _|_*__g_|_ _{_
        _std__._debug_.__print__(_"Checking for memory leaks..._\n_"_,_ _.__{__}__)__;_
        _std__._debug_.__assert__(__!__g__.__deinit__(__)__)__;_
    _}__;_

    if _(__DEBUG_LEAKS__)_ _{_
        // can't figure out how to elide the type name here
        // assigning apparently promotes from `GPA` to `?GPA`
        _gpa_ _=_ _std__._heap_.__GeneralPurposeAllocator__(__.__{__}__)__{__}__;_
        // ...but we still need to 'unwrap' it here (could get away
        // with a temporary variable)
        _alloc_ _=_ _gpa__.?__.__allocator__(__)__;_
    _}_ else _{_
        _alloc_ _=_ _std__._heap_._page_allocator_;_
    _}_

    // note: on Linux, this ends up using `fork+execve`. this is a bad idea,
    // as others have found out before: https://github.com/golang/go/issues/5838
    //
    // I was curious why passing `rustup` here worked: for me it had to either
    /