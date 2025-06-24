Title: Learnings from two years of using AI tools for software engineering

URL Source: https://newsletter.pragmaticengineer.com/p/two-years-of-using-ai

Published Time: 2025-06-24T12:30:32+00:00

Markdown Content:
It feels like GenAI is changing software engineering fast: first, it was smarter autocomplete, and now there’s ever more agentic tools that many engineers utilize. But what are some practical approaches for using these tools?

To find out more, I turned to [Birgitta Böckeler](https://birgitta.info/), Distinguished Engineer at Thoughtworks, who has been tackling this question full time for the past two years. She still writes production code at Thoughtworks, but her main focus is developing expertise in AI-assisted software delivery.

To stay on top of the latest developments, Birgitta talks to Thoughtworks colleagues, clients, and fellow industry practitioners, and uses the tools. She tries out tools, and figures out how they fit into her workflow. Today, Birgitta walks us through what she’s learned the last two years of working with AI tools:

1.   **Evolution from “autocomplete on steroids” to AI agents**. From the early days of autocompete, through AI chats and IDE integration, to the agentic step change.

2.   **Working with AI**:a practical mental model of your “AI teammate,” beware of cognitive biases where GenAI can “manipulate” you, and emerging workflows with AI

3.   **Impact on team effectiveness.**AI coding assistants increase the speed of software delivery – though it’s complicated to measure by _exactly_ how much. Without close supervision, the impact on quality could be negative. Team dynamics will most likely be impacted when rolling out these tools quickly.

4.   **The future.**LLMs are _not_ the next compilers: they are something different, the future of AI coding is unevenly distributed, and we will take on tech debt while figuring out how to use these AI tools the right way.

To learn more, check out additional thoughts by Birgitta in the [Exploring Generative AI](https://martinfowler.com/articles/exploring-gen-ai.html) collection on her colleague Martin Fowler's website.

_Programming note: this week, I’m in Mongolia for the launch of The Software Engineer’s Guidebook translated into Mongolian, so there will be no podcast episode or The Pulse this week: see you for the next issue, next Tuesday!_

_The bottom of this article could be missing in some email clients. [Read the full article online](https://newsletter.pragmaticengineer.com/p/two-years-of-using-ai)_

[Read the full article online](https://newsletter.pragmaticengineer.com/p/two-years-of-using-ai)

_With that, it’s over to Birgitta. Note, the terms AI, Generative AI, and LLM are used interchangeably throughout this article._

Almost precisely 2 years ago in July 2023, Thoughtworks decided to introduce a full-time, subject-matter expert role for "AI-assisted software delivery". It was when the immense impact that Generative AI can have on software delivery was becoming ever more apparent, and I was fortunate enough to be in the right place at the right time, with the right qualifications to take on the position. And I’ve been drinking from the firehose ever since.

**I see myself as a domain expert for effective software delivery who applies Generative AI to that domain.** As part of the role, I talk to Thoughtworks colleagues, clients, and fellow industry practitioners. I use the tools myself and try to stay on top of the latest developments, and regularly [write](https://martinfowler.com/articles/exploring-gen-ai.html) and [talk](https://birgitta.info/) about my findings and experiences.

This article is a round-up of my findings, experiences, and content, from the past 2 years.

AI coding tools have been developing at breakneck speed, making it very hard to stay on top of the latest developments. Therefore, developers not only face the challenge of adapting to generative AI's nature, they also face an additional hurdle: once they've formed opinions about tools or established workflows, they must adjust constantly to accommodate new developments. Some thrive in this environment, while others find it frustrating.

So, let’s start with a recap of that race so far, of how AI coding assistants have evolved in two years. It all started with enhanced autocomplete, and has led to a swarm of coding agents to choose from today.

[![Image 1](https://substackcdn.com/image/fetch/$s_!Mmxx!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F94587a2c-3dc9-45e6-92ef-5705eaa64638_1600x1326.png)](https://substackcdn.com/image/fetch/$s_!Mmxx!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F94587a2c-3dc9-45e6-92ef-5705eaa64638_1600x1326.png)

_How AI assistants evolved, 2021-2025_

The first step of AI coding assistance felt like an enhanced version of the autocomplete we already knew, but on a new level. As far as I know, Tabnine was the first prominent product to offer this, in around 2019. GitHub Copilot was first released in preview in 2021. It was a move from predictions based on abstract syntax trees and known refactoring and implementation patterns, to a suggestion engine that is much more adaptive to our current context and logic, but also less deterministic, and more hit and miss. Developer reactions ranged from awe, to a dismissive “I’ll stick with my reliable IDE functions and shortcuts, thank you very much.”

Back then, I already found it a useful productivity booster, and soon didn’t want to work without it, especially for languages I was less familiar with. However, like many others, I soon discovered the reality of “review fatigue” which leads some developers to switch off the assistant and focus fully on code creation, instead of code review.

It seems unimaginable today, but there was a time when assistants did not have chat functionality. I recall announcing in the company chat in July 2023 that our GitHub Copilot licenses finally had the chat feature: 24 minutes later somebody posted that they’d asked Copilot to explain a shell script in Star Wars metaphors. From a developer experience point of view, it was a big deal to be able to ask questions directly in the IDE, without having to go to the browser and sift through lots of content to find the relevant nugget for my situation.

And it was not just about asking straightforward questions, like whether there are static functions in Python; we also started using them for code explanation and simple debugging. I remember fighting with a piece of logic for a while before the assistant explained that two of my variables were named the wrong way around, which is why I had been misunderstanding the code the whole time.

At that point, hallucinations started to become an even bigger topic of discourse, along with comparisons to StackOverflow, which was starting to observe its first decline in traffic.

Over time, AI tooling also got more advanced integration into existing IDE functionality: AI started showing up in “quick fix” menus, and integration with the IDE terminal got better. In late 2023, I finally stopped prompting through code comments; instead, I started popping up the little inline editor chat to give quick prompting instructions right where my code was.

[![Image 2](https://substackcdn.com/image/fetch/$s_!Y3Rm!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F209f1cfc-1939-41b0-a952-538ece90f1c0_1600x365.png)](https://substackcdn.com/image/fetch/$s_!Y3Rm!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F209f1cfc-1939-41b0-a952-538ece90f1c0_1600x365.png)

Inline editor chat in VS Code

IDE integration is one reason I prefer using IDE coding assistants over terminal-based ones. IDEs are built to understand, navigate, and change code, and pairing them with token-based LLMs is really powerful. I believe there is much more potential integration still untapped, and look forward to having my agent access the debugger or refactoring functionalities.

The key to AI assistants is the context of what’s being worked on, so their integration with the codebase as a whole was the next big step, which started happening in around autumn 2023. Being able to ask questions about the codebase is especially useful when working with an unfamiliar one, and I found it very useful to be able to ask questions like “where is validation of X implemented”, or “how are we filtering?”. Even in the early days of these features, I found they more often than not pointed me in the right direction, and offered added value over text search. Since then, codebase awareness has significantly improved.

How effectively this codebase search is implemented is still a differentiating factor between coding assistants. The approaches range from vector-based indices like Cursor and Windsurf, to abstract syntax and file tree based text search such as Cline, and sophisticated code search engines like Sourcegraph Cody.

**Context Providers**

The codebase is not all the context there is, though; there are lots of other data sources that can provide helpful context for an AI assistant. More context providers were integrated into the assistants to give developers greater control over what information the AI assistant sees. Developers could point at the local change set, terminal output, website URLs, reference documentation, and even the first instances of JIRA ticket integration.

There were also the first indications of the need for an ecosystem when GitHub announced [GitHub Copilot Extensions](https://github.blog/news-insights/product-news/introducing-github-copilot-extensions/) in May 2024; a way for providers to integrate context providers. Fast forward to today, [MCP](https://newsletter.pragmaticengineer.com/p/mcp) (Model Context Protocol) has sent the context provider ecosystem into overdrive and taken over the space.

**Model evolution**

In parallel to all these tool features, the models have evolved, too. This space is particularly tricky to keep up with, as it's hard to get objective measures of how well a model performs for coding. A “TL/DR” summary of where model evolution is at this point, is that while there are multiple good candidates out there, Anthropic's Claude Sonnet series has clearly emerged as a consistent favorite for coding tasks. It’s my "sensible default" recommendation, as of today. The model used is definitely important, but I think it’s still widely underestimated what a big role the features and integrated tools play, especially when models are paired up with tools that understand code, and can therefore complement the large language model’s (LLM) purely tokenised understanding of things.

The current frontier – and arguably the biggest step change so far – is the emergence of agentic coding. I currently divide the coding agents into two buckets:

**Supervised coding agents:** Interactive chat agents driven and steered by a developer. Create code locally, in the IDE.

_**Tools:**_ The very first tool in this style I saw was Aider, and its git history starts as early as May 2023. Cline has been around since July 2024, the agentic modes in Cursor and Windsurf started around November 2024, and GitHub Copilot Coding Agent was a late arrival [in May 2025](https://github.com/newsroom/press-releases/coding-agent-for-github-copilot). Claude Code and various Cline forks have also gained a lot of traction in the first half of 2025.

**Autonomous background coding agents:** Headless agents which are sent off to work autonomously through a whole task. Code gets created in a remote environment spun up exclusively for that agent, and usually results in a pull request. Some are also runnable locally.

_**Tools:**_ The very first one of these that got a lot of attention was Devin, with big announcements in March 2024, soon followed by online controversy. They released a generally available version in December 2024. While there were a few similar attempts here and there, including an open source project called “OpenDevin” that quickly had to rename itself to “OpenHands”, background agents have recently seen new momentum with the releases of OpenAI Codex, Google Jules, and Cursor background agents.

Coding agents expand the size of the task that can be collaborated on with AI into a larger problem-solving loop. This is mainly fuelled by increased automation and integration with tools like terminal command execution or web search. Just imagine any tool used by developers in their coding workflow, and how it could enhance a coding agent's capabilities if it were integrated. MCP is the catalyst of that ecosystem of integrations, at the moment.

Here’s an example of a problem-solving loop:

*   "I'm getting this error message, help me debug: …"

*   Agent does web research, finds something in the library's documentation, and some issue discussions on GitHub

*   Adds patch library dependency to the project

*   Runs npm install to install the new dependency

*   Adds necessary code to the project

*   Restarts application

*   Sees error message

*   Tries to fix the code based on the error message

*   Restarts application again

*   ...

With a **supervised agent**, a human is looking over the agent's shoulder and intervenes when necessary. This over-the-shoulder look can range from skimming the agent's reasoning to see if it's going in a good direction, code review, interrupting and rolling back, answering questions from the agent, or approving the execution of terminal commands.

Many people were introduced to the supervised agentic modes via the “vibe coding” meme in early February 2025. Even though vibe coding by definition is a mode where a person does not review the code, I still see it in this supervised category, as a human constantly looks at the resulting application and gives the agent feedback.

**Autonomous background agents** are assigned to work on a task autonomously, and a person only looks at the result once the agent is done. The result can be a local commit or a pull request. I haven’t yet seen them work for more than small, simple tasks, but they’ll probably have their place in our toolchain as they mature.

**We cover supervised agents in this article**. Autonomous background agents are [still in their early days](https://martinfowler.com/articles/exploring-gen-ai/autonomous-agents-codex-example.html), and have a lot of kinks to work out. Below, I use "coding agents" synonymously with "supervised agents."

Generative AI is a fast-moving target, so practices constantly adapt to new developments. However, there are some “timeless” principles and ways of working that I apply today.

First of all, there’s a distinct shift in mindset required to work effectively with GenAI. [Ethan Mollick](https://www.linkedin.com/in/emollick), professor at Wharton, researcher on AI, made the observation early on that [“AI is terrible software”](https://www.oneusefulthing.org/p/ai-is-not-good-software-it-is-pretty). This really clicked for me: generative AI tooling is not like any other software. To use it effectively, it’s necessary to adapt to its nature and embrace it. This is a shift that’s especially hard for software engineers who are attached to building deterministic automation. It feels uncomfortable and hacky that these tools sometimes work and other times don’t.

Therefore, the first thing to navigate is the mindset change of becoming an effective human in the loop.

A helpful step for me was to give my coding assistant a persona, to anthropomorphize it just enough to calibrate my expectations (inspired by Ethan Mollick and his book, [Co-Intelligence](https://www.goodreads.com/book/show/198678736-co-intelligence)). There are mental models for each human teammate, which are used implicitly when deciding to trust their work and input. Someone who’s very experienced in backend and infrastructure work is likely to have their input and advice trusted, but it still might be wise to double check when they’re building their first React Hook.

Here’s [the persona](https://martinfowler.com/articles/exploring-gen-ai/08-how-to-tackle-unreliability.html) I settled on for AI assistants:

*   Eager to help

*   Stubborn, and sometimes with a short-term memory

*   Very well-read, but inexperienced

*   Overconfident

[![Image 3](https://substackcdn.com/image/fetch/$s_!_N29!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ffe3f9b49-97ae-45f8-9a67-c73f5db75694_1600x751.png)](https://substackcdn.com/image/fetch/$s_!_N29!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ffe3f9b49-97ae-45f8-9a67-c73f5db75694_1600x751.png)

_My mental model for an AI teammate_

This mental model helped me develop an intuition of when to reach for GenAI, when to trust its results more, and when to trust it less. I expect enthusiasm and assistance, and even access to current information via web search. But I must still exercise judgment, context, and final authority.

Working with Generative AI is fertile ground for several cognitive biases that can undermine judgment. I find this a fascinating part of GenAI: how manipulative this technology is.

Here are just a few examples of potential cognitive biases:

**[Automation bias](https://en.wikipedia.org/wiki/Automation_bias)** represents our tendency to favor suggestions from automated systems while ignoring contradictory information, even when that information is correct. Once you've experienced success with AI-generated code, it's natural to start over-trusting the system. The confident tone and polished output can make us less likely to question its recommendations, even when experience suggests a different approach.

**The [framing effect](https://en.wikipedia.org/wiki/Framing_effect_(psychology))** reinforces the impact of the positive, confident phrasing of LLM responses. For instance, if an AI suggests that a particular approach is "best practice," we are more likely to take that at face value and adopt it, without considering context-specific factors.

**The [anchoring effect](https://en.wikipedia.org/wiki/Anchoring_effect)** can kick in when AI presents a solution before we thought about it. After viewing AI's suggestions, we can find it harder to think creatively about alternative solutions. The AI's approach becomes our mental starting point, potentially limiting our exploration of better alternatives. On the flip side, AI can also help us mitigate anchoring bias, for example when assisting with modernising a pre-existing solution we're already anchored to.

And finally, there is also a version of **[sunk cost fallacy](https://en.wikipedia.org/wiki/Sunk_cost#Fallacy_effect)** at work when coding with AI. Investing less human labour into writing code, should make it easier to discard code that’s not working. However, I've caught myself becoming over-attached to large pieces of AI-generated code which I’d rather try to fix instead of revert. Perceived time savings create a psychological investment that can make one reluctant to abandon AI-generated solutions, even when they're sub-optimal.

Once you’re mentally prepared and have steeled yourself against the biases, the following are some general principles I’ve found practical for utilizing AI assistants efficiently.

**Reflect on feedback loops**. How do you know the AI did as instructed, and can this be learned quickly, and review fatigue reduced? If it's a small change, do you write a unit test, or let AI generate one and use that as the main point of review? If it's a larger change, which available tests are trustworthy: an integration test, an end-to-end test, or an easy manual test? Beyond functionality, what is in place to quickly assess code quality: a static code analysis plugin in the IDE, a pre-commit hook, a human pairing partner? It’s sensible to be aware of all options and to reflect on the feedback loop when working on a task with AI.

**Know when to quit**. When I feel like I'm losing control of a solution and don't really understand what's happening, I revert; either the whole set of local changes, or to a previous checkpoint – which is a feature supported by most coding assistants. I then reflect on how to take a better approach, like ways to improve my prompts, or breaking down a task into smaller steps, or resorting to "artisanal coding" like writing the code from scratch, myself.

**Know your context providers and integrated tools**. Does a tool have web access, or does it solely rely on its training data, how much access does it have to your codebase, does it search it automatically, or do you have to provide explicit references, what other context providers and MCP servers are available and useful? Having knowledge of the capabilities and access of the tool is important for picking the right one for the job, and for adjusting expectations and trust level. You should also know which data an agent has access to and where it's sent, in order to understand [risks to the software supply chain](https://martinfowler.com/articles/exploring-gen-ai/software-supply-chain-attack-surface.html), and wield this powerful tool responsibly.

Before coding agents, the coding workflow with AI assistants was relatively close to how engineers usually work, 1-50 lines of code at a time. AI was along for the ride and boosting us step by step. This has changed with coding agents, which not only increase the size of tasks to work on, but also the size of the code review and the context information needed.

Below are the main recommendations I currently give for working with agentic assistants. I should say, all of these are ways to increase the likelihood of success, but as always with Generative AI, there are no guarantees, and its effectiveness depends on the task and the context.

**Use custom instructions**. Custom instructions – or “custom rules” as some tools call them – are a great way to maintain common instructions for the AI. They are like a natural language configuration of the coding assistant, and can contain instructions about coding style and conventions, tech stack, domain, or just mitigations for common pitfalls the AI falls into.

**Plan (with AI) first**. As appealing as it sounds to just throw one sentence at the agent and then have it magically translate that into multiple code changes across a larger codebase, that's usually not how it works well. Breaking down the work first into smaller tasks not only makes it easier for the agent to execute the right changes in small steps, but also gives a person the chance to review the direction the AI is going in and to correct it early, if needed.

**Keep tasks small**. The planning stage should break the work down into small tasks. Even though models technically have larger and larger context windows, that doesn't necessarily mean they can handle all the context in a long coding conversation well, or that they can maintain focus on the most important things in that long context. It’s much more effective to start new conversations frequently, and not let the context grow too large because the performance usually degrades.

**Be concrete**. "Make it so I can toggle the visibility of the edit button", is an example of a more high level task description that an agent could translate into multiple different interpretations and solutions. A concrete description which will lead to more success is something like, "add a new boolean field 'editable' to the DB, expose it through /api/xxx and toggle visibility based on that".

**Use some form of memory**. Working in small tasks is all well and good, but when working on a larger task in multiple smaller sessions, it’s not ideal to repeat the task, the context, and what has already been done, every time a new subtask is started. A common solution to this is to have the AI create and maintain a set of files in the workspace that represent the current task and its context, and then point at them whenever a new session starts. The trick then becomes to have a good idea of how to best structure those files, and what information to include. [Cline's memory bank](https://docs.cline.bot/prompting/cline-memory-bank) is one example of a definition of such a memory structure.

The introduction of AI tooling to software delivery teams has led to a resurgence of the perennial question of how to measure software team productivity. _Note from Gergely: we dig into this topic with Kent Beck in [Measuring developer productivity? A response to McKinsey](https://newsletter.pragmaticengineer.com/p/measuring-developer-productivity)._

My short answer to how to measure developer productivity is that the problem does not change just because there’s something new in the toolbox. We still have the same challenge, which is that software delivery is not an assembly line that produces a stream of comparable pieces to count and measure. Productivity is a multi-dimensional concept that can’t be summed up in a single number.

Having said that, of course it’s possible to look at the many indicators that make up the holistic picture of productivity, and see how AI impacts them. I focus on speed and quality first, and then touch on team flow and process.
