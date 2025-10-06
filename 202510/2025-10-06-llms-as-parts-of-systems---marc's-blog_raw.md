Title: LLMs as Parts of Systems

URL Source: https://brooker.co.za/blog/2025/08/12/llms-as-components.html

Markdown Content:
Towers of Hanoi is a boring game, anyway.

Over on the [Kiro](https://kiro.dev/) blog, I wrote a post about [Kiro and the future of AI spec-driven software development](https://kiro.dev/blog/kiro-and-the-future-of-software-development/), looking at where I think the space of AI-agent-powered development tools is going. In that post, I made a bit of cheeky oblique reference to a topic I think is super important. I asked Kiro to build a Towers of Hanoi game.

It’s an oblique reference to Apple’s [The Illusion of Thinking](https://machinelearning.apple.com/research/illusion-of-thinking) paper, and the discourse that followed it. The question of whether LLMs can scalably play Towers of Hanoi is an interesting theoretically and scientifically, but not the most important question. The more important one is _can systems built with LLMs play these games?_. By picking me Towers of Hanoi in that other post, I was pointing out that the answer is clearly _yes_. And has been for several LLM generations.

As a system builder, I’m much more interested in what systems of LLMs and tools can do together. LLMs and code interpreters. LLMs and databases. LLMs and browsers. LLMs and SMT solvers. These systems can do things, today, that LLMs alone simply can’t, and will never be able to do. More importantly, they can do things today orders of magnitude more cheaply and quickly than LLMs can, even in the case where they can do the same things.

You know, this kind of thing:

```
> Generate a python snippet that counts the number of rs in a string.

def count_rs(input_string):
    return input_string.lower().count('r')
```

Trivial? Yes. But I’ve now created a system that that can solve problems that this LLM can’t. A better LLM can, but at about six orders of magnitude higher cost per example. Systems, fundamentally, are more than the sum of their components. A good system can do things that no component can do alone.

The trivial example is trivial, but you can imagine how that power could extend to being able to use decades of progress in algorithms. And not only `count`, but much more powerful things like SMT solvers, or ILP approximation, or MCMC. But, given the efficiency, even trivial things like `count`, `sum`, and `grep` are interesting.

A more advanced example is Amazon Bedrock’s [Automated Reasoning Checks](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-automated-reasoning-checks.html). Automated Reasoning checks use LLMs to extract the underlying _rules_ from a set of documents, and _facts_ from an LLM or agent response, and then uses an [SMT solver](https://en.wikipedia.org/wiki/Satisfiability_modulo_theories) to verify that the facts are logically consistent with the rules. [Danilo’s blog post](https://aws.amazon.com/blogs/aws/minimize-ai-hallucinations-and-deliver-up-to-99-verification-accuracy-with-automated-reasoning-checks-now-available/) goes through a detailed example of what this looks like, if you’d like to understand more.

Automated Reasoning checks, like my trivial example above, combine LLMs with other methods of reasoning to create a system that’s greater than the sum of its parts. LLMs are used for what they’re good at - extracting facts and rules from the messy natural language that humans use. SMT solvers are used for what they’re great at - reasoning precisely through a set of logical steps, and providing formal justification for that reasoning. The current generation of LLMs can’t do this type of reasoning alone, but systems composed of LLMs and other tools (SMT solvers in this case) can do it.

The hype and buzz around LLMs makes it easy to forget this point, but it’s a critical one. LLMs are more powerful, more dependable, more efficient, and more flexible when deployed as a component of a carefully designed system.

It’s a very exciting time to be a systems person, because we’ve been handed a new and extremely powerful component that can be used to build better systems with new capabilities. Some old ideas will go away, but the fundamental ideas won’t. They’ll be more relevant than ever.

_What About The Bitter Lesson?_

Is this view of LLMs as parts of systems consistent with Rich Sutton’s [The Bitter Lesson](https://www.cs.utexas.edu/~eunsol/courses/data/bitter_lesson.pdf)? Sutton says:

> The biggest lesson that can be read from 70 years of AI research is that general methods that leverage computation are ultimately the most effective, and by a large margin.

and

> We have to learn the bitter lesson that building in how we think we think does not work in the long run.

I’m not proposing that these systems, systems composed of LLMs and other computational and storage tools, should build in _how we think we think_[1](https://brooker.co.za/blog/2025/08/12/llms-as-components.html#foot1). The way I read Sutton’s point is not at all incompatible with the idea that there are better (more efficient, more reliable, etc) and worse (less efficient, less reliable, etc) ways to do computing. For example, Sutton doesn’t seem to be implying that generating and executing (or memoizing, retrieving, and executing) code to do a task is less good than doing it with a lot of linear algebra.

> We want AI agents that can discover like we can, not which contain what we have discovered. Building in our discoveries only makes it harder to see how the discovering process can be done.

Indeed. Computing, from Python to SMT, has been a powerful tool of discovery for over eighty years. Making these tools available to the systems we build, and specifically to the AI agents we build, gives them more power and leverage. Not by encoding the way we think, but by encoding the things computer science has learned about the way the universe works.

**Footnotes**

1.   [](https://brooker.co.za/blog/2025/08/12/llms-as-components.html) One could look at the heuristics that SAT solvers use to guide their searches as an encoding of _how we think we think_, at least to some extent. I’m not a deep expert, but I do think it’s reasonable to believe that a more computation approach will allow us to discover new and more effective search heuristics for some classes of problems. The fundamental algorithms (like [DPLL](https://en.wikipedia.org/wiki/DPLL_algorithm) and [CDCL](https://en.wikipedia.org/wiki/Conflict-driven_clause_learning)) look pretty compute-maximalist to me.