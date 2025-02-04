Title: LLMs: harmful to technical innovation?

URL Source: https://evanhahn.com/llms-and-technical-innovation/

Published Time: 2025-02-02T00:00:00+00:00

Markdown Content:
_In short: newer ideas have less available training data so the LLM experience will probably be worse. This could help existing technologies maintain their status._

I’ve been playing with a few less-popular programming languages like [Crystal](https://crystal-lang.org/), [Zig](https://ziglang.org/), and [Gleam](https://gleam.run/). They’re super cool!

I want more people to use them…but I understand why someone wouldn’t. Even if you pretend they’re _100% better_ on a “purely technical” level, you might choose a more popular language like Python because it has a bigger community. It’s easier to find Python programmers than Gleam programmers; there are more JavaScript libraries than Zig libraries; there are more tools made for Ruby than for Crystal.

In other words, popularity can be self-perpetuating.

I saw these ideas mentioned in [“Why Gumroad Didn’t Choose htmx”](https://htmx.org/essays/why-gumroad-didnt-choose-htmx/), a story of how Gumroad evaluated [htmx](https://htmx.org/) but ultimately decided to use React and Next.js, which are more established. Everything in the post felt level-headed and reasonable to me, even though I was rooting for htmx.

But one paragraph really stuck out:

> It’s worth noting that AI tools are intimately familiar with Next.js and not so much with htmx, due to the lack of open-source training data. \[…\] While not a dealbreaker, it did impact our development speed and the ease of finding solutions to problems. When we encountered issues, the wealth of resources available for React/Next.js made troubleshooting much faster.

In addition to all the other challenges—libraries, programmers, tools, books, blog posts, Q&A answers—there’s now an additional hurdle for nascent technologies: _a worse LLM experience due to less training data_.

Machine learning bias can have [far uglier consequences](https://www.popularmechanics.com/science/math/a32957375/mathematicians-boycott-predictive-policing/) than a JavaScript framework not getting adopted. And LLMs can _help_ technical innovation in other ways! But, at least on this one axis, LLMs might make it harder for new ideas to flourish.
