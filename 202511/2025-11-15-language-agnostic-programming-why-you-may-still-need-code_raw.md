Title: Language Agnostic Programming: Why you may still need code

URL Source: https://joaquimrocha.com/2025/08/31/language-agnostic-programming-why-you-may-still-need-code/

Published Time: 2025-08-31T17:10:00.000Z

Markdown Content:
Throughout my career, I have had the pleasure (and sometimes the pain) of working with various programming languages and paradigms. And recently, like everyone else, I have been leveraging large language models (LLMs), and user interfaces for them like GitHub Copilot, Cursor, Claude Code, …, for increasing my output. Yet, I get skeptical when I read claims like “English will be the only programming language you’ll ever need”. What this really means, especially the “ever” part, is: if AI can translate our English descriptions into working code, do we still need programming languages at all?

Sure, AI does an impressive job at translating natural language into code. And sure, if you can express your intent clearly in English (or any other natural language), you can get a lot done, I know I do!

Even with all that, I think that one aspect of programming will remain essential: _debugging_. No matter how good AI gets at generating code and even at debugging it, we’ll still need to understand what that code actually does when it doesn’t work as expected. And for that, we need programming languages. Not necessarily for writing the initial code, but for reading, tracing, and reasoning about it when things go wrong.

When Natural Language Falls Short
---------------------------------

There’s a classic joke that my brother loves: a software engineer’s partner asks him to go to the store and get milk, and if there are eggs, bring twelve! The engineer comes back with twelve bottles of milk. When asked why, he says “they had eggs”.

This kind of ambiguity is usually resolved through context and common sense for (most) humans, but computers require unambiguous instructions. In programming, such ambiguity can lead to catastrophic failures rather than just humorous misunderstandings.

Programming languages eliminate this ambiguity by design. When we write:

```
for (int i = 0; i < 10; ++i) {
    printf("%d\n", i);
}
```

there’s no question about what this means. The syntax is precise and unambiguous (and let’s put aside fun things like undefined behavior in C). In contrast, natural language descriptions of the same logic could be expressed in dozens of different ways, each potentially open to interpretation.

The Language Choice Dilemma
---------------------------

So let’s assume for a minute that we accept that LLMs do write all the code and that programming languages are still necessary for understanding and debugging it. This raises an interesting question that has plagued software engineers since forever: which programming language should you learn? You see, the enthusiasm of “English as the only programming language” idea is not just about simplifying or democratizing access to programming, but also about the perceived drop of complexity when you do not have to learn JavaScript for the Web, or C for systems programming.

Programming language choice is a perennial dilemma that is not just about taste or preference; it can significantly affect the development process. Developers working primarily in high-level languages like Python or JavaScript do not need to grasp concepts like manual memory management in C, or the ownership model in Rust. Likewise, having to work on code bases written in a language you’re not familiar with can be a significant barrier to productivity.

A New Possibility: Language-Agnostic Programming
------------------------------------------------

Here’s an intriguing possibility that LLMs may enable: if LLMs can translate programming languages seamlessly and accurately, then could debugging (and perhaps even broader code comprehension) a project not be tied to a specific programming language at all? Imagine a future where programs are written (by LLMs) in a single, highly precise language like Rust (with its explicit ownership and type systems), but programmers can choose to view and edit that code in whatever language they prefer.

Think about it this way: a project is “written” in Rust’s precise type system and ownership model, capturing all the necessary details about memory management, thread safety, and error handling, and is thus optimized for speed and safety. But when I want to read the project’s code (or parts of it), or debug it, I could view it as Go if that’s the language I’m most comfortable with. Or I might prefer to see it as Python, while another team member could work with it in Typescript.

The underlying program remains the same (precise and unambiguous), but each developer interacts with it through their preferred linguistic interface. Sure, there are technical issues to this. How can you express Rust’s ownership model in Python? C++‘s template metaprogramming or Python’s dynamic typing may not map cleanly to other languages. How do you handle language-specific idioms and libraries? There are obviously limitations, but I believe that many of these challenges could be addressed with careful design and tooling. E.g. parts of the program that do not translate well to a higher-level language could still be viewed in Rust or annotated with comments to clarify their design. The job of the LLM would be to ensure that the semantics when translating back to Rust remain consistent.

Right now, it’s possible to ask GitHub Copilot to “show me this module in Python” or “convert this function to JavaScript”. But for the idea above to work in a productive way, we would need LLMs to work much faster (ideally faster than opening your code in Emacs), and would need to be accurate in interpreting and translating the code. This is a tall order, but not outside the realm of possibility given the rapid advancements in AI.

The Future Model
----------------

In this model:

*   AI systems generate code directly from natural language descriptions into a precise, safe, and fast programming language
*   Programmers who need to read or debug the code can choose their preferred programming language interface
*   The AI handles the translation between the precise underlying code and the various language interfaces, ensuring that the semantics remain consistent across all views

This approach could democratize programming further, as well as facilitating onboarding and collaboration across teams, by allowing programmers to work in the languages they are most comfortable with, regardless of the underlying implementation.

Of course, this is just a theory, and I’m not certain it will play out this way. I am not even sure I would like it to play out that way! But, as the relationship between AI and programming is still evolving rapidly and we might see entirely different paradigms emerge, it may.