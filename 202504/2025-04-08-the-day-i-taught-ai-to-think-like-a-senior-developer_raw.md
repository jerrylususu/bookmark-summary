Title: The day I taught AI to think like a Senior Developer

URL Source: https://nmn.gl/blog/ai-understand-senior-developer

Published Time: 2025-04-07T00:00:00+00:00

Markdown Content:
_Is it just me, or are the code generation AIs we’re all using fundamentally broken?_

For months, I’ve watched developers praise AI coding tools while silently cleaning up their messes, afraid to admit how much babysitting they actually need.

I realized that AI IDEs don’t actually _understand_ codebases — they’re just sophisticated autocomplete tools with good marketing. The emperor has no clothes, and I’m tired of pretending otherwise.

After two years of frustration watching my AI assistants constantly “forget” where files were located, create duplicates, and use completely incorrect patterns, I finally built what the big AI companies couldn’t (or wouldn’t.)

I decided to find out: What if I could make AI _actually_ understand how my codebase works?

Illusion of Comprehension
-------------------------

Last December, I hit my breaking point. My supposedly “intelligent” AI assistant kept generating components that didn’t follow our established patterns. When I pointed this out, it apologized — and then proceeded to make the exact same mistake ten minutes later.

This wasn’t a one-off. This was the norm.

The problem became clear: these AI tools don’t have any actual understanding of codebases as interconnected systems. They’re operating on small context windows and failing spectacularly at maintaining a mental model of the project.

What makes this particularly frustrating is how the marketing from major AI companies implies their tools “understand” your code. They don’t. They’re making educated guesses — and the difference becomes painfully obvious on any moderately complex project.

Universal Truths About Code
---------------------------

While thinking about this problem, I tried to understand the fundamental principles that govern how we organize code. Some “universal truths” I realized:

*   Related files are grouped together in folders, which is a semantic indication of purpose.
*   Sibling folders reflect conceptual similarity.
*   Subfolder structure indicates hierarchical relationships and dependency.
*   Not every line of code is equally “relevant.” Codebases contain significant amounts of boilerplate and library code that, while necessary, don’t define the project’s unique characteristics.

These insights are obvious to experienced developers, but they represent critical semantic knowledge that AI assistants completely miss.

Breakthrough
------------

The solution came to me during a 2 AM coding session, while I was dealing with yet another incorrectly generated file: what if we treated the codebase as a **hierarchical knowledge graph** instead of flat files?

![Image 1](https://nmn.gl/blog/assets/code_graph.png)

Human developers [don’t memorize entire codebases](https://nmn.gl/blog/ai-senior-developer). We build mental models of how components relate to each other. We understand that some code is boilerplate, while other sections are critical business logic. We naturally view code through different “lenses” depending on what we’re trying to accomplish.

I developed what I call “Ranked Recursive Summarization” (RRS), an algorithm that starts from the leaves of a project’s directory tree and recursively builds understanding upward using LLMs:

```
# pseudocode:
def ranked_recursive_summarization(folder):
    if is_file(folder):
        chunks = split_into_chunks(read_file(folder))
        ranked_chunks = rank_by_importance(chunks)
        return summarize(ranked_chunks)
    
    summaries = []
    for child in folder.children:
        summary = RRS(child)
        summaries.append(summary)
    
    return summarize(summaries)
```

This worked **shockingly** well, but I soon realized it wasn’t enough. Depending on what I was trying to work on, RRS missed certain details. If it had information about architecture and data models, it missed out on frontend components. If it was too focused on UI, it missed out on describing data flow.

I had to think deeper: what makes a certain part of the code _important_?

Lensed Understanding
--------------------

My second insight led to the truly transformative technique: “Prismatic Ranked Recursive Summarization” (PRRS).

Instead of having one global definition of “importance,” PRRS analyzes code through multiple conceptual lenses:

```
# pseudocode:
def prismatic_rrs(folder, lenses=['architecture', 'data_flow', 'security']):
    summaries = {}
    for lens in lenses:
        context = f"Analyze importance from {lens} perspective"
        summaries[lens] = RRS(folder, context=context)
    return summaries
```

The results were undeniable. AI suddenly understood:

*   Where files should logically be placed
*   Which patterns to follow
*   How to extend existing abstractions instead of creating new ones
*   When to reuse code vs. create new implementations

Honestly, the approach isn’t particularly complex or compute-intensive. The big AI companies could have implemented something like this from the beginning. But they haven’t, because it doesn’t align with their incentives of getting results for the lowest token costs.

Why This Matters
----------------

The implications go far beyond fixing basic errors. When AI truly understands your codebase:

1.  Technical debt becomes visible through the “architecture” lens
2.  Security vulnerabilities emerge naturally through the “security” lens
3.  Junior developers can navigate complex projects with senior-level insight
4.  Onboarding time for new team members decreases dramatically

There’s a darker side as well. As AI gets better at understanding codebases, the value of certain types of programming knowledge decreases: the [mid-level programmer](https://nmn.gl/blog/ai-illiterate-programmers) who primarily translates requirements into code without architectural insight may find themselves increasingly squeezed.

I’ve packaged this approach into my tool, [Giga](https://gigamind.dev/). It’s been used by hundreds of developers all over the world and they’re feeling less frustrated and are seeing productivity gains.

Implementation
--------------

Even without my specific tool, you can improve your AI assistant’s code understanding:

*   Create manual summaries of your most important directories and files
*   Ask an AI to further improve your manual documentation
*   Create and ensure multiple documentation files, each from a different “lens”, based on your project
*   Include relevant files into AI’s context as needed

These approaches won’t be as seamless as a purpose-built solution, but they’ll dramatically improve your results compared to the default experience.

Context is the Future
---------------------

I believe we’re at the beginning of a fundamental shift in how AI understands complex systems like codebases. The next generation of tools won’t just create embeddings of your code — they’ll build rich mental models from multiple perspectives, just like experienced developers do.

The companies that embrace this approach will leapfrog those still focused on token prediction alone. And developers who learn to leverage these sophisticated tools will have sustainable advantages that mere “prompt engineering” can’t match.

The future belongs to those who see AI not as a replacement for human developers, but as a force multiplier for human ingenuity.

And that future starts **now**.

_What frustrations have you experienced with AI coding assistants? I’d love to hear your stories at [hi@nmn.gl](mailto:hi@nmn.gl)_

P.S. My AI improves code generation in production & helps you ship faster. Loved by developers & teams all over the world. [Check out Giga AI](https://gigamind.dev/).
