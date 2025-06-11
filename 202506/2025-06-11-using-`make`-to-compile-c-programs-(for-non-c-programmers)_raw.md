Title: Using `make` to compile C programs (for non-C-programmers)

URL Source: https://jvns.ca/blog/2025/06/10/how-to-compile-a-c-program/

Markdown Content:
I have never been a C programmer but every so often I need to compile a C/C++ program from source. This has been kind of a struggle for me: for a long time, my approach was basically “install the dependencies, run `make`, if it doesn’t work, either try to find a binary someone has compiled or give up”.

“Hope someone else has compiled it” worked pretty well when I was running Linux but since I’ve been using a Mac for the last couple of years I’ve been running into more situations where I have to actually compile programs myself.

So let’s talk about what you might have to do to compile a C program! I’ll use a couple of examples of specific C programs I’ve compiled and talk about a few things that can go wrong. Here are three programs we’ll be talking about compiling:

*   [paperjam](https://mj.ucw.cz/sw/paperjam/)
*   [sqlite](https://www.sqlite.org/download.html)
*   [qf](https://git.causal.agency/src/tree/bin/qf.c) (a pager you can run to quickly open files from a search with `rg -n THING | qf`)

### [step 1: install a C compiler](https://jvns.ca/blog/2025/06/10/how-to-compile-a-c-program/#step-1-install-a-c-compiler)

This is pretty simple: on an Ubuntu system if I don’t already have a C compiler I’ll install one with:

```
sudo apt-get install build-essential
```

This installs `gcc`, `g++`, and `make`. The situation on a Mac is more confusing but it’s something like “install xcode command line tools”.

### [step 2: install the program’s dependencies](https://jvns.ca/blog/2025/06/10/how-to-compile-a-c-program/#step-2-install-the-program-s-dependencies)

Unlike some newer programming languages, C doesn’t have a dependency manager. So if a program has any dependencies, you need to hunt them down yourself. Thankfully because of this, C programmers usually keep their dependencies very minimal and often the dependencies will be available in whatever package manager you’re using.

There’s almost always a section explaining how to get the dependencies in the README, for example in [paperjam](https://mj.ucw.cz/sw/paperjam/)’s README, it says:

> To compile PaperJam, you need the headers for the libqpdf and libpaper libraries (usually available as libqpdf-dev and libpaper-dev packages).

> You may need `a2x` (found in [AsciiDoc](http://www.methods.co.nz/asciidoc/a2x.1.html)) for building manual pages.

So on a Debian-based system you can install the dependencies like this.

```
sudo apt install -y libqpdf-dev libpaper-dev
```

If a README gives a name for a package (like `libqpdf-dev`), I’d basically always assume that they mean “in a Debian-based Linux distro”: if you’re on a Mac `brew install libqpdf-dev` will not work. I still have not 100% gotten the hang of developing on a Mac yet so I don’t have many tips there yet. I guess in this case it would be `brew install qpdf` if you’re using Homebrew.

### [step 3: run `./configure` (if needed)](https://jvns.ca/blog/2025/06/10/how-to-compile-a-c-program/#step-3-run-configure-if-needed)

Some C programs come with a `Makefile` and some instead come with a script called `./configure`. For example, if you download [sqlite’s source code](https://www.sqlite.org/download.html), it has a `./configure` script in it instead of a Makefile.

My understanding of this `./configure` script is:

1.   You run it, it prints out a lot of somewhat inscrutable output, and then it either generates a `Makefile` or fails because you’re missing some dependency
2.   The `./configure` script is part of a system called [autotools](https://www.gnu.org/software/automake/manual/html_node/Autotools-Introduction.html) that I have never needed to learn anything about beyond “run it to generate a `Makefile`”.

I think there might be some options you can pass to get the `./configure` script to produce a different `Makefile` but I have never done that.

### [step 4: run `make`](https://jvns.ca/blog/2025/06/10/how-to-compile-a-c-program/#step-4-run-make)

The next step is to run `make` to try to build a program. Some notes about `make`:

*   Sometimes you can run `make -j8` to parallelize the build and make it go faster
*   It usually prints out a million compiler warnings when compiling the program. I always just ignore them. I didn’t write the software! The compiler warnings are not my problem.

### [compiler errors are often dependency problems](https://jvns.ca/blog/2025/06/10/how-to-compile-a-c-program/#compiler-errors-are-often-dependency-problems)

Here’s an error I got while compiling `paperjam` on my Mac:

```
/opt/homebrew/Cellar/qpdf/12.0.0/include/qpdf/InputSource.hh:85:19: error: function definition does not declare parameters
   85 |     qpdf_offset_t last_offset{0};
      |                   ^
```

Over the years I’ve learned it’s usually best not to overthink problems like this: if it’s talking about `qpdf`, there’s a good change it just means that I’ve done something wrong with how I’m including the `qpdf` dependency.

Now let’s talk about some ways to get the `qpdf` dependency included in the right way.

### [the world’s shortest introduction to the compiler and linker](https://jvns.ca/blog/2025/06/10/how-to-compile-a-c-program/#the-world-s-shortest-introduction-to-the-compiler-and-linker)

Before we talk about how to fix dependency problems: building C programs is split into 2 steps:

1.   **Compiling** the code into **object files** (with `gcc` or `clang`)
2.   **Linking** those object files into a final binary (with `ld`)

It’s important to know this when building a C program because sometimes you need to pass the right flags to the compiler and linker to tell them where to find the dependencies for the program you’re compiling.

### [`make` uses environment variables to configure the compiler and linker](https://jvns.ca/blog/2025/06/10/how-to-compile-a-c-program/#make-uses-environment-variables-to-configure-the-compiler-and-linker)

If I run `make` on my Mac to install `paperjam`, I get this error:

```
c++ -o paperjam paperjam.o pdf-tools.o parse.o cmds.o pdf.o -lqpdf -lpaper
ld: library 'qpdf' not found
```

This is not because `qpdf` is not installed on my system (it actually is!). But the compiler and linker don’t know how to _find_ the `qpdf` library. To fix this, we need to:

*   pass `"-I/opt/homebrew/include"` to the compiler (to tell it where to find the header files)
*   pass `"-L/opt/homebrew/lib -liconv"` to the linker (to tell it where to find library files and to link in `iconv`)

And we can get `make` to pass those extra parameters to the compiler and linker using environment variables! To see how this works: inside `paperjam`’s Makefile you can see a bunch of environment variables, like `LDLIBS` here:

```
paperjam: $(OBJS)
	$(LD) -o $@ $^ $(LDLIBS)
```

Everything you put into the `LDLIBS` environment variable gets passed to the linker (`ld`) as a command line argument.

### [secret environment variable: `CPPFLAGS`](https://jvns.ca/blog/2025/06/10/how-to-compile-a-c-program/#secret-environment-variable-cppflags)

`Makefiles` sometimes define their own environment variables that they pass to the compiler/linker, but `make` also has a bunch of “implicit” environment variables which it will automatically pass to the C compiler and linker. There’s a [full list of implicit environment variables here](https://www.gnu.org/software/make/manual/html_node/Implicit-Variables.html#index-CFLAGS0), but one of them is `CPPFLAGS`, which gets automatically passed to the C compiler.

(technically it would be more normal to use `CXXFLAGS` for this, but this particular `Makefile` hardcodes `CXXFLAGS` so setting `CPPFLAGS` was the only way I could find to set the compiler flags without editing the `Makefile`)

 As an aside: it took me a long time to realize how closely tied to C/C++ `make` is -- I used to think that `make` was just a general build system (and of course you can use it for anything!) but it has a lot of affordances for building C/C++ programs that it doesn't have for building any other kind of program. 
### [two ways to pass environment variables to `make`](https://jvns.ca/blog/2025/06/10/how-to-compile-a-c-program/#two-ways-to-pass-environment-variables-to-make)

I learned thanks to [@zwol](https://www.owlfolio.org/) that there are actually two ways to pass environment variables to `make`:

1.   `CXXFLAGS=xyz make` (the usual way)
2.   `make CXXFLAGS=xyz`

The difference between them is that `make CXXFLAGS=xyz` will override the value of `CXXFLAGS` set in the `Makefile` but `CXXFLAGS=xyz make` won’t.

I’m not sure which way is the norm but I’m going to use the first way in this post.

### [how to use `CPPFLAGS` and `LDLIBS` to fix this compiler error](https://jvns.ca/blog/2025/06/10/how-to-compile-a-c-program/#how-to-use-cppflags-and-ldlibs-to-fix-this-compiler-error)

Now that we’ve talked about how `CPPFLAGS` and `LDLIBS` get passed to the compiler and linker, here’s the final incantation that I used to get the program to build successfully!

```
CPPFLAGS="-I/opt/homebrew/include" LDLIBS="-L/opt/homebrew/lib -liconv" make paperjam
```

This passes `-I/opt/homebrew/include` to the compiler and `-L/opt/homebrew/lib -liconv` to the linker.

Also I don’t want to pretend that I “magically” knew that those were the right arguments to pass, figuring them out involved a bunch of confused Googling that I skipped over in this post. I will say that:

*   the `-I` compiler flag tells the compiler which directory to find header files in, like `/opt/homebrew/include/qpdf/QPDF.hh`
*   the `-L` linker flag tells the linker which directory to find libraries in, like `/opt/homebrew/lib/libqpdf.a`
*   the `-l` linker flag tells the linker which libraries to link in, like `-liconv` means “link in the `iconv` library”, or `-lm` means “link `math`”

### [tip: how to just build 1 specific file: `make $FILENAME`](https://jvns.ca/blog/2025/06/10/how-to-compile-a-c-program/#tip-how-to-just-build-1-specific-file-make-filename)

Yesterday I discovered this cool tool called [qf](https://git.causal.agency/src/tree/bin/qf.c) which you can use to quickly open files from the output of `ripgrep`.

`qf` is in a big directory of various tools, but I only wanted to compile `qf`. So I just compiled `qf`, like this:

```
make qf
```

Basically if you know (or can guess) the output filename of the file you’re trying to build, you can tell `make` to just build that file by running `make $FILENAME`

### [tip: look at how other packaging systems built the same C program](https://jvns.ca/blog/2025/06/10/how-to-compile-a-c-program/#tip-look-at-how-other-packaging-systems-built-the-same-c-program)

If you’re having trouble building a C program, maybe other people had problems building it too! Every Linux distribution has build files for every package that they build, so even if you can’t install packages from that distribution directly, maybe you can get tips from that Linux distro for how to build the package. Realizing this (thanks to my friend Dave) was a huge ah-ha moment for me.

For example, [this line from the nix package for `paperjam`](https://github.com/NixOS/nixpkgs/blob/405624e81a9b65378328accb0a11c3e5369e651c/pkgs/by-name/pa/paperjam/package.nix#L35) says:

```
env.NIX_LDFLAGS = lib.optionalString stdenv.hostPlatform.isDarwin "-liconv";
```

This is basically saying “pass the linker flag `-liconv` to build this on a Mac”, so that’s a clue we could use to build it.

That same file also says `env.NIX_CFLAGS_COMPILE = "-DPOINTERHOLDER_TRANSITION=1";`. I’m not sure what this means, but when I try to build the `paperjam` package I do get an error about something called a `PointerHolder`, so I guess that’s somehow related to the “PointerHolder transition”.

### [step 5: installing the binary](https://jvns.ca/blog/2025/06/10/how-to-compile-a-c-program/#step-5-installing-the-binary)

Once you’ve managed to compile the program, probably you want to install it somewhere! Some `Makefile`s have an `install` target that let you install the tool on your system with `make install`. I’m always a bit scared of this (where is it going to put the files? what if I want to uninstall them later?), so if I’m compiling a pretty simple program I’ll often just manually copy the binary to install it instead, like this:

```
cp qf ~/bin
```

### [step 6: maybe make your own package!](https://jvns.ca/blog/2025/06/10/how-to-compile-a-c-program/#step-6-maybe-make-your-own-package)

Once I figured out how to do all of this, I realized that I could use my new `make` knowledge to contribute a `paperjam` package to Homebrew! Then I could just `brew install paperjam` on future systems.

The good thing is that even if the details of how all of the different packaging systems, they fundamentally all use C compilers and linkers.

### [it can be useful to understand a little about C even if you’re not a C programmer](https://jvns.ca/blog/2025/06/10/how-to-compile-a-c-program/#it-can-be-useful-to-understand-a-little-about-c-even-if-you-re-not-a-c-programmer)

I think all of this is an interesting example of how it can useful to understand some basics of how C programs work (like “they have header files”) even if you’re never planning to write a nontrivial C program if your life.

It feels good to have some ability to compile C/C++ programs myself, even though I’m still not totally confident about all of the compiler and linker flags and I still plan to never learn anything about how autotools works other than “you run `./configure` to generate the `Makefile`”.

Also one important thing I left out is `LD_LIBRARY_PATH / DYLD_LIBRARY_PATH` (which you use to tell the dynamic linker at runtime where to find dynamically linked files) because I can’t remember the last time I ran into an `LD_LIBRARY_PATH` issue and couldn’t find an example.
