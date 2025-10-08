Title: Vibe engineering

URL Source: https://simonwillison.net/2025/Oct/7/vibe-engineering/

Published Time: Wed, 08 Oct 2025 00:39:04 GMT

Markdown Content:
7th October 2025

I feel like **vibe coding** is [pretty well established now](https://simonwillison.net/2025/Mar/19/vibe-coding/) as covering the fast, loose and irresponsible way of building software with AI—entirely prompt-driven, and with no attention paid to how the code actually works. This leaves us with a terminology gap: what should we call the other end of the spectrum, where seasoned professionals accelerate their work with LLMs while staying proudly and confidently accountable for the software they produce?

I propose we call this **vibe engineering**, with my tongue only partially in my cheek.

One of the lesser spoken truths of working productively with LLMs as a software engineer on non-toy-projects is that it’s _difficult_. There’s a lot of depth to understanding how to use the tools, there are plenty of traps to avoid, and the pace at which they can churn out working code raises the bar for what the human participant can and should be contributing.

The rise of **coding agents**—tools like [Claude Code](https://www.claude.com/product/claude-code) (released February 2025), OpenAI’s [Codex CLI](https://github.com/openai/codex) (April) and [Gemini CLI](https://github.com/google-gemini/gemini-cli) (June) that can iterate on code, actively testing and modifying it until it achieves a specified goal, has dramatically increased the usefulness of LLMs for real-world coding problems.

I’m increasingly hearing from experienced, credible software engineers who are running multiple copies of agents at once, tackling several problems in parallel and expanding the scope of what they can take on. I was skeptical of this at first but [I’ve started running multiple agents myself now](https://simonwillison.net/2025/Oct/5/parallel-coding-agents/) and it’s surprisingly effective, if mentally exhausting!

This feels very different from classic vibe coding, where I outsource a simple, low-stakes task to an LLM and accept the result if it appears to work. Most of my [tools.simonwillison.net](https://simonwillison.net/) collection ([previously](https://simonwillison.net/2025/Sep/4/highlighted-tools/)) were built like that. Iterating with coding agents to produce production-quality code that I’m confident I can maintain in the future feels like a different process entirely.

It’s also become clear to me that LLMs actively reward existing top tier software engineering practices:

*   **Automated testing**. If your project has a robust, comprehensive and stable test suite agentic coding tools can _fly_ with it. Without tests? Your agent might claim something works without having actually tested it at all, plus any new change could break an unrelated feature without you realizing it. Test-first development is particularly effective with agents that can iterate in a loop.
*   **Planning in advance**. Sitting down to hack something together goes much better if you start with a high level plan. Working with an agent makes this even more important—you can iterate on the plan first, then hand it off to the agent to write the code.
*   **Comprehensive documentation**. Just like human programmers, an LLM can only keep a subset of the codebase in its context at once. Being able to feed in relevant documentation lets it use APIs from other areas without reading the code first. Write good documentation first and the model may be able to build the matching implementation from that input alone.
*   **Good version control habits**. Being able to undo mistakes and understand when and how something was changed is even more important when a coding agent might have made the changes. LLMs are also fiercely competent at Git—they can navigate the history themselves to track down the origin of bugs, and they’re better than most developers at using [git bisect](https://til.simonwillison.net/git/git-bisect). Use that to your advantage.
*   Having **effective automation** in place. Continuous integration, automated formatting and linting, continuous deployment to a preview environment—all things that agentic coding tools can benefit from too. LLMs make writing quick automation scripts easier as well, which can help them then repeat tasks accurately and consistently next time.
*   A **culture of code review**. This one explains itself. If you’re fast and productive at code review you’re going to have a much better time working with LLMs than if you’d rather write code yourself than review the same thing written by someone (or something) else.
*   A **very weird form of management**. Getting good results out of a coding agent feels uncomfortably close to getting good results out of a human collaborator. You need to provide clear instructions, ensure they have the necessary context and provide actionable feedback on what they produce. It’s a _lot_ easier than working with actual people because you don’t have to worry about offending or discouraging them—but any existing management experience you have will prove surprisingly useful.
*   Really good **manual QA (quality assurance)**. Beyond automated tests, you need to be really good at manually testing software, including predicting and digging into edge-cases.
*   Strong **research skills**. There are dozens of ways to solve any given coding problem. Figuring out the best options and proving an approach has always been important, and remains a blocker on unleashing an agent to write the actual code.
*   The ability to **ship to a preview environment**. If an agent builds a feature, having a way to safely preview that feature (without deploying it straight to production) makes reviews much more productive and greatly reduces the risk of shipping something broken.
*   An instinct for **what can be outsourced** to AI and what you need to manually handle yourself. This is constantly evolving as the models and tools become more effective. A big part of working effectively with LLMs is maintaining a strong intuition for when they can best be applied.
*   An updated **sense of estimation**. Estimating how long a project will take has always been one of the hardest but most important parts of being a senior engineer, especially in organizations where budget and strategy decisions are made based on those estimates. AI-assisted coding makes this _even harder_—things that used to take a long time are much faster, but estimations now depend on new factors which we’re all still trying to figure out.

If you’re going to really exploit the capabilities of these new tools, you need to be operating _at the top of your game_. You’re not just responsible for writing the code—you’re researching approaches, deciding on high-level architecture, writing specifications, defining success criteria, [designing agentic loops](https://simonwillison.net/2025/Sep/30/designing-agentic-loops/), planning QA, managing a growing army of weird digital interns who will absolutely cheat if you give them a chance, and spending _so much time on code review_.

Almost all of these are characteristics of senior software engineers already!

AI tools **amplify existing expertise**. The more skills and experience you have as a software engineer the faster and better the results you can get from working with LLMs and coding agents.

#### “Vibe engineering”, really?[#](https://simonwillison.net/2025/Oct/7/vibe-engineering/#-vibe-engineering-really-)

Is this a stupid name? Yeah, probably. “Vibes” as a concept in AI feels a little tired at this point. “Vibe coding” itself is used by a lot of developers in a dismissive way. I’m ready to reclaim vibes for something more constructive.

I’ve never really liked the artificial distinction between “coders” and “engineers”—that’s always smelled to me a bit like gatekeeping. But in this case a bit of gatekeeping is exactly what we need!

**Vibe engineering** establishes a clear distinction from vibe coding. It signals that this is a different, harder and more sophisticated way of working with AI tools to build production software.

I like that this is cheeky and likely to be controversial. This whole space is still absurd in all sorts of different ways. We shouldn’t take ourselves too seriously while we figure out the most productive ways to apply these new tools.

I’ve tried in the past to get terms like **[AI-assisted programming](https://simonwillison.net/tags/ai-assisted-programming/)** to stick, with approximately zero success. May as well try rubbing some vibes on it and see what happens.

I also really like the clear mismatch between “vibes” and “engineering”. It makes the combined term self-contradictory in a way that I find mischievous and (hopefully) sticky.