Title: Type Checking is a Symptom, Not a Solution

URL Source: https://programmingsimplicity.substack.com/p/type-checking-is-a-symptom-not-a

Published Time: 2025-09-05T03:22:08+00:00

Markdown Content:
What if the programming industry’s decades-long obsession with type checking is solving the wrong problem entirely? What if our increasingly sophisticated type systems—from Haskell’s category theory to Rust’s borrow checker—are elaborate workarounds for fundamental architectural mistakes we’ve been making since the beginning?

The software industry has convinced itself that type checking is not just useful, but essential. We’ve built entire programming languages around the premise that catching type errors at compile time is one of the highest priorities in software design. We’ve invested countless person-years into developing ever more powerful type systems, treating each advancement as unquestionable progress.

But step back and ask a simple question: Why do we need type checking at all?

The standard answer is scale. “Small programs don’t need types,” the reasoning goes, “but large programs become unmaintainable without them.” This sounds reasonable until you realize what we’re actually admitting: that we’ve designed our systems to be inherently incomprehensible to human reasoning. We’ve created architectures so tangled, so dependent on invisible connections and implicit behaviors, that we need automated tools just to verify that our programs won’t crash in obvious ways.

Type checking, in other words, is not a solution to complexity—it’s a confession that we’ve created unnecessary complexity in the first place.

Consider this: electronics engineers routinely design systems with millions of components, intricate timing relationships, and complex interactions between subsystems. Yet they don’t rely on anything analogous to our type checkers. They use different architectural principles—isolation, explicit interfaces, and time-aware design—that make their systems naturally more robust and understandable.

The problem isn’t that software is inherently more complex than hardware. The problem is that we’ve chosen abstractions and architectural patterns that create artificial complexity, then built elaborate tooling to manage the mess we’ve made.

**The Accepted Wisdom**

Walk into any software engineering discussion about large-scale systems, and you’ll hear the same refrains: “Types catch bugs before they reach production.” “Static typing makes refactoring safe.” “You can’t maintain a million-line codebase without a strong type system.”

These statements aren’t wrong, exactly. Within the context of how we currently build software—with sprawling inheritance hierarchies, deeply nested function calls, and invisible dependencies threading through dozens of modules—type checking does indeed catch bugs that would otherwise be painful to debug. The Rust compiler’s borrow checker does prevent memory safety issues that plague C programs. TypeScript does make JavaScript codebases more maintainable.

But notice what’s happening here. We’ve created systems so intricate and interconnected that human reasoning fails, then declared the tools that help us navigate this complexity to be essential. It’s like building a maze so convoluted that you need a GPS to walk through it, then concluding that GPSs are fundamental to architecture.

The software industry has elevated type checking from a useful technique to an unquestioned necessity. We debate whether dynamic or static typing is better, but rarely ask whether the conditions that make typing feel essential are actually inevitable. We’ve accepted that programs will grow beyond human comprehension, that dependencies will multiply beyond tracking, that the relationships between components will become too complex to reason about directly.

This acceptance runs so deep that questioning it feels almost heretical. Suggest that type checking might be unnecessary, and you’ll be met with the programming equivalent of “But how would we build airplanes without blueprints?” The analogy reveals the problem: we’ve confused our current methods with the only possible methods.

**The Hidden Assumption**

The entire edifice of modern type systems rests on a single, rarely examined assumption: that software systems will inevitably grow beyond the capacity of human reasoning. This assumption is so fundamental to our thinking that we’ve stopped seeing it as an assumption at all.

Consider the “Rule of 7”—the cognitive science finding that humans can effectively reason about roughly seven variables or dependencies at once. When a system exceeds this threshold, we start making mistakes, missing edge cases, and losing track of how changes ripple through the codebase. Type checking, the argument goes, becomes essential precisely when systems cross this cognitive boundary.

But here’s the hidden assumption: that crossing this boundary is inevitable. That large software systems must, by their very nature, become cognitively overwhelming. That the only solution is to build tools sophisticated enough to navigate the complexity we’ve created.

What if this assumption is wrong? What if the need for type checking is not a natural consequence of scale, but a symptom of poor architectural choices? What if we’ve built systems that are unnecessarily complex, then mistaken that complexity for an inherent property of software?

The evidence for this alternative view is hiding in plain sight. UNIX pipelines routinely compose dozens of programs into complex workflows, yet they require no type checking at the transport layer. The individual programs trust that data flowing between them consists of simple, agreed-upon formats—usually lines of text separated by newlines. This works because each component maintains strict isolation: what happens inside a component stays inside, and communication occurs only through explicit, simple interfaces.

Similarly, the internet itself operates without centralized type checking. HTTP servers and clients, email systems, DNS resolvers—they all interoperate based on simple protocols and the assumption that each component will handle its internal complexity responsibly. The web scales to billions of interactions daily not because of sophisticated type systems, but because of architectural principles that keep components loosely coupled and interfaces simple.

These examples suggest that complexity becomes unmanageable not because of scale per se, but because of how we structure our systems. When components are truly isolated and communicate through simple, explicit channels, even large systems can remain comprehensible to human reasoning.

**The Function Trap**

To understand why we’ve created unnecessarily complex systems, we need to examine the fundamental abstraction that underlies most modern programming: the function call. Functions seem so natural, so obviously correct, that questioning them feels like questioning mathematics itself. Yet functions carry hidden baggage that makes them unsuitable for the distributed, time-based systems we’re increasingly building.

Here’s the problem: every function call conflates two distinct concepts—data flow and control flow. When you call a function, you’re not just passing data to another component; you’re also surrendering control. The caller must suspend its execution and wait for the callee to complete and return a value. This blocking behavior creates a tight coupling between components that seems innocent in small programs but becomes toxic at scale.

Consider what happens when you build a distributed system using function-based thinking. You end up with remote procedure calls (RPCs), where network requests masquerade as function calls. The caller still blocks, but now it’s blocking on network latency, potential failures, and the unpredictable timing of remote systems. To make this work, you need elaborate mechanisms: timeouts, retries, circuit breakers, distributed transactions. You’ve taken a paradigm designed for single-threaded, in-memory computation and forced it to work across geographic distances and unreliable networks.

The type checking complexity flows directly from this architectural mismatch. When functions call other functions across module boundaries, you need sophisticated type systems to ensure that the data flowing through these call chains maintains consistency. When functions return values that are passed to other functions, you need generics and higher-order types to track how data transforms through the call graph. When functions might throw exceptions that propagate up the call stack, you need either exception specifications or Result types to manage error flow.

All of this complexity stems from trying to maintain the illusion that distributed, asynchronous systems can be programmed as if they were single-threaded, synchronous programs. We’ve built increasingly sophisticated type systems not because the problems we’re solving are inherently complex, but because we’re using the wrong abstraction for modern computing challenges.

Function-based languages like C and functional programming languages excel at developing the internals of isolated components. But they break down when you try to coordinate between components, especially when those components are distributed, long-running, or event-driven. We’re trying to use a paradigm designed for calculation to build systems that are fundamentally about coordination and communication.

**Lessons from Other Domains**

If function-based programming is the wrong paradigm for modern systems, what’s the right one? The answer has been hiding in plain sight in domains that routinely build systems far more complex than most software.

Electronics engineers design processors with billions of transistors, intricate timing relationships, and complex interactions between subsystems. They coordinate signals across different clock domains, manage power distribution networks, and ensure that electromagnetic interference doesn’t corrupt data. Yet they don’t rely on anything analogous to our elaborate type systems. Instead, they use architectural principles that make complexity manageable: strict isolation between components, explicit timing constraints, and simple, well-defined interfaces.

In electronics, time is a first-class concept. Signals have duration, components have setup and hold times, and the sequencing of events is explicitly designed rather than hoped for. This isn’t an accident—it’s recognition that distributed systems (and a circuit board is a distributed system) require different thinking than sequential computation.

David Harel recognized this when he developed Statecharts in the 1980s. Statecharts brought the electronics mindset to software, treating time as a fundamental control-flow concept rather than an afterthought. Harel’s key insight was that the state explosion problem—the exponential growth of possible system states that makes complex systems unmanageable—could be solved through strong isolation and hierarchical layering, not through more sophisticated analysis tools.

Statecharts prove that software can handle complex, concurrent, time-based behavior without the elaborate type machinery we’ve convinced ourselves is necessary. The secret is architectural: components are truly isolated (what happens inside a statechart stays inside), communication occurs only through explicit events, and the overall system behavior emerges from the composition of simple, understandable parts.

UNIX pipelines offer another glimpse of this alternative approach. When you compose commands like `grep | sort | uniq`, you’re not doing type checking at the transport layer. Instead, you’re relying on architectural principles: each command is completely isolated, communication occurs only through simple data streams (lines of text), and complex behavior emerges from the composition of simple components. The transport layer uses extremely simple data—bytes or characters—which allows universal pluggability. Individual components can layer more sophisticated agreements about data meaning on top of this simple substrate.

Both examples share a crucial insight: when the architecture is right, complexity remains manageable without elaborate analysis tools. The need for sophisticated type checking is not a sign of engineering maturity—it’s a symptom of architectural immaturity.

**The Real Problem**

The software industry’s obsession with type checking represents a profound misallocation of intellectual resources. While we’ve spent decades perfecting increasingly sophisticated type systems, the fundamental challenges of modern computing have gone largely unaddressed.

Consider where we’ve chosen to focus our collective brainpower. We debate whether Rust’s borrow checker is better than Haskell’s type classes. We argue about whether TypeScript’s structural typing is superior to Java’s nominal typing. We invest enormous effort into making sure that functions can be composed safely, that data structures maintain their invariants, and that null pointer exceptions are caught at compile time.

Meanwhile, the problems that actually matter in modern computing remain largely unsolved. How do we build truly distributed systems that gracefully handle network partitions? How do we create software that can scale across geographic distances without sacrificing consistency? How do we design systems that can evolve and adapt over time without requiring complete rewrites?

These are the challenges that define 21st-century computing, yet we’re approaching them with abstractions designed for 20th-century problems. We’re still thinking in terms of shared memory when components are separated by thousands of miles. We’re still designing for expensive, scarce CPUs when processing power is practically free. We’re still trying to optimize for perfect reliability when resilience in the face of failure is what actually matters.

The tragedy is that every hour spent perfecting type systems is an hour not spent understanding concurrency, emergence, or fault tolerance. Every brilliant mind focused on making function calls safer is a brilliant mind not focused on building systems that naturally avoid the problems function calls create.

We’ve created a peculiar situation where our most sophisticated tools address the symptoms of our architectural choices rather than questioning those choices themselves. It’s like perfecting the engineering of buggy whips while ignoring the invention of the automobile. We’ve gotten incredibly good at managing the complexity we’ve created instead of asking whether we should create that complexity in the first place.

This misallocation goes deeper than just wasted effort—it’s actively harmful. By treating type checking as essential, we’ve locked ourselves into architectural patterns that require type checking. We’ve made it harder to explore alternatives because those alternatives look “unsafe” or “unscalable” from within our current paradigm.

**Toward Better Architectures**

The path forward isn’t to abandon type checking entirely—within the context of function-based programming, types remain useful. Instead, we need to recognize that the felt necessity of sophisticated type systems is a signal that we’re using the wrong architectural foundations.

True isolation offers a compelling alternative. When components are designed as genuine black boxes—where what happens inside stays inside, and communication occurs only through explicit input and output ports—systems naturally become easier to reason about. You don’t need elaborate type machinery to understand what a component does if its interface is simple and its behavior is contained.

Consider how this changes the reasoning process. Instead of tracing through complex call graphs and type hierarchies to understand how data flows through a system, you can reason about each component in isolation. Instead of worrying about how changes in one module might ripple through dozens of dependencies, you can focus on the explicit contracts between components. Instead of relying on type checkers to catch interaction bugs, you can design systems where problematic interactions are structurally impossible.

This isn’t just theoretical. Modern developments are already pointing in this direction. Container technologies like Docker embody the principle of isolation—each container is a complete, self-contained environment that communicates with others through explicit interfaces. Microservices architectures, despite their current implementation challenges, represent an attempt to break large systems into small, independently deployable components. Event-driven architectures recognize that asynchronous communication is often more natural than synchronous function calls.

The missing piece is programming languages and development environments designed from the ground up for this isolated, message-passing world. Languages where time is a first-class concept, where components are naturally isolated, and where simple data formats enable universal composition. Tools that make it as easy to wire together distributed components as it is to pipe together UNIX commands.

When such systems emerge, the debate over type checking will seem quaint. Not because types are bad, but because the architectural patterns that make elaborate type systems feel necessary will no longer be dominant. We’ll look back on our current obsession with type safety the same way we now look back on goto elimination—as solving a real problem, but one that better abstractions made largely irrelevant.

The goal isn’t to make type checking unnecessary by abandoning safety, but to make it unnecessary by building systems that are naturally more comprehensible, more robust, and more aligned with the realities of distributed, concurrent, time-based computing. The future of programming lies not in better analysis of complex systems, but in better ways of building simple ones.

**See Also**

_Email_: [ptcomputingsimplicity@gmail.com](mailto:ptcomputingsimplicity@gmail.com)

_Substack_: [paultarvydas.substack.com](http://paultarvydas.substack.com/)

_Videos_: [https://www.youtube.com/@programmingsimplicity2980](https://www.youtube.com/@programmingsimplicity2980)

_Discord_: [https://discord.gg/65YZUh6Jpq](https://discord.gg/65YZUh6Jpq)

_Leanpub_: [WIP] [https://leanpub.com/u/paul-tarvydas](https://leanpub.com/u/paul-tarvydas)

_Twitter_: @paul_tarvydas

_Bluesky:_ @paultarvydas.bsky.social

_Mastodon:_@paultarvydas

_(earlier)_ _Blog:_[guitarvydas.github.io](http://guitarvydas.github.io/)

_References:_[https://guitarvydas.github.io/2024/01/06/References.html](https://guitarvydas.github.io/2024/01/06/References.html)

[Leave a comment](https://programmingsimplicity.substack.com/p/type-checking-is-a-symptom-not-a/comments)

[Share](https://programmingsimplicity.substack.com/p/type-checking-is-a-symptom-not-a?utm_source=substack&utm_medium=email&utm_content=share&action=share)