Title: A Short Survey of Compiler Targets

URL Source: https://abhinavsarkar.net/notes/2025-compiler-backend-survey/

Published Time: 2025-11-05T00:00:00Z

Markdown Content:
As an amateur compiler developer, one of the decisions I struggle with is choosing the right compiler target. Unlike the 80’s when people had to target various machine architectures directly, now there are many mature options available. This is a short and very incomplete survey of some of the popular and interesting options.

### Contents

1.   [Machine Code / Assembly](https://abhinavsarkar.net/notes/2025-compiler-backend-survey/#machine-code-assembly)
2.   [Intermediate Representations](https://abhinavsarkar.net/notes/2025-compiler-backend-survey/#intermediate-representations)
3.   [Other High-level Languages](https://abhinavsarkar.net/notes/2025-compiler-backend-survey/#other-high-level-languages)
4.   [Virtual Machines / Bytecode](https://abhinavsarkar.net/notes/2025-compiler-backend-survey/#virtual-machines-bytecode)
5.   [WebAssembly](https://abhinavsarkar.net/notes/2025-compiler-backend-survey/#webassembly)
6.   [Meta-tracing and Metacompilation Frameworks](https://abhinavsarkar.net/notes/2025-compiler-backend-survey/#meta-tracing-and-metacompilation-frameworks)
7.   [Unconventional Targets](https://abhinavsarkar.net/notes/2025-compiler-backend-survey/#unconventional-targets)
8.   [Conclusion](https://abhinavsarkar.net/notes/2025-compiler-backend-survey/#conclusion)

Machine Code / Assembly
-----------------------

A compiler can always directly output machine code or assembly targeted for one or more architectures. A well-known example is the [Tiny C Compiler](https://www.bellard.org/tcc/). It’s known for its speed and small size, and it can compile and run C code on the fly. Another such example is [Turbo Pascal](https://en.wikipedia.org/wiki/Turbo_Pascal). You could do this with your compiler too, but you’ll have to figure out the intricacies of the _[Instruction set](https://en.wikipedia.org/wiki/Instruction\_set)_ of each architecture (ISA) you want to target, as well as, concepts like _[Register allocation](https://en.wikipedia.org/wiki/Register\_allocation)_.

Most modern compilers actually don’t emit machine code or assembly directly. They lower the source code down to a language-agnostic _[Intermediate representation](https://en.wikipedia.org/wiki/Intermediate\_representation)_ (IR) first, and then generate machine code for major architectures (x86-64, ARM64, etc.) from it.

The most prominent tool in this space is [LLVM](https://llvm.org/). It’s a large, open-source compiler-as-a-library. Compilers for many languages such as [Rust](https://www.rust-lang.org/), [Swift](https://www.swift.org/), C/C++ (via [Clang](https://clang.llvm.org/)), and [Julia](https://julialang.org/) use LLVM as an IR to emit machine code.

An alternative is the [GNU Compiler Collection](https://gcc.gnu.org/) (GCC), via its [GIMPLE](https://gcc.gnu.org/onlinedocs/gccint/GIMPLE.html) IR, though no compilers seem to use it directly. GCC can be used as a library to compile code, much like LLVM, via [libgccjit](https://gcc.gnu.org/onlinedocs/jit/). It is used in [Emacs](https://www.gnu.org/software/emacs/) to [_Just-in-time_](https://en.wikipedia.org/wiki/Just-in-time_compilation) (JIT) compile [Elisp](https://www.gnu.org/software/emacs/manual/html_node/elisp/). [Cranelift](https://cranelift.dev/) is another new option in this space, though it supports only few ISAs.

For those who find LLVM or GCC too large or slow to compile, minimalist alternatives exist. [QBE](https://c9x.me/compile/) is a small backend focused on simplicity, targeting “70% of the performance in 10% of the code”. It’s used by the language [Hare](https://harelang.org/) that prioritizes fast compile times. Another option is [libFIRM](http://libfirm.org/), which uses a graph-based [SSA](https://en.wikipedia.org/wiki/Static_single-assignment_form) representation instead of a linear IR.

Other High-level Languages
--------------------------

Sometimes you are okay with letting other compilers/runtimes take care of the heavy lifting. You can [transpile](https://en.wikipedia.org/wiki/transpile) your code to a another established high-level language and leverage that language’s existing compiler/runtime and toolchain.

A common target in such cases is C. Since C compilers exist for nearly all platforms, generating C code makes your language highly portable. This is the strategy used by [Chicken Scheme](https://www.call-cc.org/) and [Vala](https://vala.dev/). Or you could compile to C++ instead, like [Jank](https://jank-lang.org/), if that’s your thing. There is also [C–](https://en.wikipedia.org/wiki/C--), a subset of C targeted by [GHC](https://www.haskell.org/ghc/) and [OCaml](https://ocaml.org/).

Another ubiquitous target is [JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript) (JS), which is one of the two options (other being [WebAssembly](https://abhinavsarkar.net/notes/2025-compiler-backend-survey/#webassembly)) for running code natively in a web browser or one of the JS runtimes ([Node](https://nodejs.org/), [Deno](https://deno.com/), [Bun](https://bun.com/)). Multiple languages such as [TypeScript](https://www.typescriptlang.org/), [PureScript](https://www.purescript.org/), [Reason](https://reasonml.github.io/), [ClojureScript](https://clojurescript.org/), [Dart](https://dart.dev/) and [Elm](https://elm-lang.org/) transpile to JS. [Nim](https://nim-lang.org/) interestingly, can transpile to C, C++ or JS.

Another target similar to JS is [Lua](https://www.lua.org/), a lightweight and embeddable scripting language, which languages such as [MoonScript](https://moonscript.org/) and [Fennel](https://fennel-lang.org/) transpile to.

A more niche approach is to target a Lisp dialect. Compiling to [Chez Scheme](https://cisco.github.io/ChezScheme/), for example, allows you to leverage its macro system, runtime, and compiler. The [Idris 2](https://www.idris-lang.org/) and [Racket](https://racket-lang.org/) use Chez Scheme as their primary backend targets.

Virtual Machines / Bytecode
---------------------------

This is a common choice for application languages. You compile to a portable bytecode for a _[Virtual machine](https://en.wikipedia.org/wiki/Virtual\_machine#Process\_virtual\_machines)_ (VM). VMs generally come with features like _[Garbage collection](https://en.wikipedia.org/wiki/Garbage\_collection\_(computer\_science))_, _[JIT compilation](https://en.wikipedia.org/wiki/Just-in-time\_compilation)_, and security sandboxing.

The [Java Virtual Machine](https://en.wikipedia.org/wiki/Java_Virtual_Machine) (JVM) is probably the most popular one. It’s the target for many languages including [Java](https://en.wikipedia.org/wiki/Java), [Kotlin](https://kotlinlang.org/), [Scala](https://www.scala-lang.org/), [Groovy](https://groovy-lang.org/), and [Clojure](https://clojure.org/). Its main competitor is the [Common Language Runtime](https://en.wikipedia.org/wiki/Common_Language_Runtime), originally developed by [Microsoft](https://en.wikipedia.org/wiki/Microsoft), which is targeted by languages such as [C#](https://en.wikipedia.org/wiki/C_Sharp_(programming_language)), [F#](https://fsharp.org/), and [Visual Basic.NET](https://en.wikipedia.org/wiki/Visual_Basic.NET).

Another notable VM is the [BEAM](https://en.wikipedia.org/wiki/BEAM_(Erlang_virtual_machine)), originally built for [Erlang](https://www.erlang.org/). The BEAM VM isn’t built for raw computation speed but for high concurrency, fault tolerance, and reliability. Recently, new languages such as [Elixir](https://elixir-lang.org/) and [Gleam](https://gleam.run/) have been created to target it.

Finally, this category also includes [MoarVM](https://www.moarvm.org/)—the spiritual successor to the [Parrot VM](https://en.wikipedia.org/wiki/Parrot_virtual_machine)—built for the [Raku](https://web.archive.org/web/20251105/https://raku.org/) (formerly Perl 6) language.

WebAssembly
-----------

[WebAssembly](https://webassembly.org/) (Wasm) is a relatively new target. It’s a portable binary instruction format focused on security and efficiency. Wasm is supported by all major browsers, but not limited to them. The [WebAssembly System Interface](https://wasi.dev/) (WASI) standard provides APIs for running Wasm in non-browser and non-JS environments. Wasm is now targeted by many languages such as [Rust](https://www.rust-lang.org/), [C/C++](https://emscripten.org/), [Go](https://golang.org/), [Kotlin](https://kotlinlang.org/), [Scala](https://www.scala-lang.org/), [Zig](https://ziglang.org/), and [Haskell](https://ghc.gitlab.haskell.org/ghc/doc/users_guide/wasm.html).

_[Meta-tracing](https://en.wikipedia.org/wiki/Meta-tracing)_ and _[Metacompilation](https://en.wikipedia.org/wiki/Metacompilation)_ frameworks are a more complex category. These are not the targets for your compiler backend, instead, you use them to build a custom JIT compiler for your language by specifying an interpreter for it.

The most well-known example is [PyPy](https://www.pypy.org/), an implementation of [Python](https://python.org/), created using the [RPython](https://rpython.readthedocs.io/) framework. Another such framework is [GraalVM/Truffle](https://www.graalvm.org/), a polyglot VM and meta-tracing framework from [Oracle](https://www.oracle.com/). Its main feature is zero-cost interoperability: code from [GraalJS](https://www.graalvm.org/javascript/), [TruffleRuby](https://www.graalvm.org/ruby/), and [GraalPy](https://www.graalvm.org/python/) can all run on the same VM, and can call each other directly.

Unconventional Targets
----------------------

Move past the mainstream, and you’ll discover a world of unconventional and esoteric compiler targets. Developers pick them for academic curiosity, artistic expression, or to test the boundaries of viable compilation targets.

*   Brainfuck: An esoteric language with only eight commands, [Brainfuck](https://en.wikipedia.org/wiki/Brainfuck) is _[Turing-complete](https://en.wikipedia.org/wiki/Turing-complete)_ and has been a target for compilers as a challenge. People have written compilers for [C](https://github.com/arthaud/c2bf), [Haskell](https://github.com/xy-kasumi/hs2bf) and [Lambda calculus](https://github.com/tlively/BrainCoqulus).

*   Lambda calculus: [Lambda calculus](https://en.wikipedia.org/wiki/Lambda_calculus) is a minimal programming languages that expresses computation solely as functions and their applications. It is often used as the target of educational compilers because of its simplicity, and its link to the fundamental nature of computation. [Hell](https://chrisdone.github.io/hell/), a subset of Haskell, compiles to [Simply typed lambda calculus](https://en.wikipedia.org/wiki/Simply_typed_lambda_calculus).

*   SKI combinators: The [SKI combinator calculus](https://en.wikipedia.org/wiki/SKI_combinator_calculus) is even more minimal than lambda calculus. All programs in SKI calculus can be composed of only three combinators: S, K and I. [MicroHs](https://github.com/augustss/MicroHs) compiles a subset of Haskell to SKI calculus.

*   JSFuck: Did you know that you can write all possible JavaScript programs using only six characters `[]()!+`? Well, [now you know](https://jsfuck.com/).

*   Postscript: [Postscript](https://en.wikipedia.org/wiki/Postscript) is also a Turing-complete programming language. Your next compiler could target it!

*   [Regular Expressions](https://blog.poisson.chat/posts/2024-06-18-turing-regex.html)? [Lego](https://www.yankodesign.com/2024/10/02/functional-lego-turing-machine-brings-algorithm-processing-to-life-with-2900-bricks/)? [Cellular automata](https://web.archive.org/web/20251105/https://conwaylife.com/wiki/Turing_complete)?

Conclusion
----------

I’m going to write a compiler from C++ to JSFuck.

If you have any questions or comments, please leave a comment below. If you liked this post, please share it. Thanks for reading!

### Like, repost, or comment

*   [Fediverse](https://fantastic.earth/@abnv/115496808679524403)
*   [Lobsters](https://lobste.rs/s/ctbibn)
*   [Reddit](https://www.reddit.com/r/compilers/comments/1op0h7e/)
*   [Hacker News](https://news.ycombinator.com/item?id=45821785)
*   [Comments below](https://abhinavsarkar.net/notes/2025-compiler-backend-survey/#comment-container)

### Send a Webmention for this post

 Posted by [Abhinav Sarkar](https://abhinavsarkar.net/about/) at [https://abhinavsarkar.net/notes/2025-compiler-backend-survey/](https://abhinavsarkar.net/notes/2025-compiler-backend-survey/)