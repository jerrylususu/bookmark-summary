Title: AI-assisted coding for teams that can't get away with vibes

URL Source: http://blog.nilenso.com/blog/2025/05/29/ai-assisted-coding/

Markdown Content:
_Status: Living document based on production experience_

_Last updated: 5-Jun-2025_

AI should be adopted by serious engineering teams that want to build thoughtful, well-crafted products. This requires skillful usage of these tools. Our obsession with building high-quality software for over a decade has driven us to figure out how this new way of building can result in better products.

**Building with AI is fast**. The gains in velocity are important, because when harnessed correctly, it allows teams to tighten feedback loops with users faster and make better products.

Yet, AI tools are tricky to use. Hold it wrong, and you can generate underwhelming results, worse still, slow down your velocity by drowning your project in slop and technical debt.

This living playbook is based on our experience working with AI tools in the messy trenches of production software, where no one can afford to get away with vibes. I hope other teams can learn and benefit from our findings.

AI is a multiplier
------------------

To make AI good, get good yourself. AI is a multiplier. If you are a small coefficient, you won’t see much gain. If you are a negative coefficient, expect negative gains.

What I have noticed is that the best and most experienced engineers are able to extract a lot more out of AI tools. There are several reasons for this:

*   They are extremely good at communicating technical ideas.
*   They have a keen calibration and feel for what leads to a good system and can steer LLMs accordingly, i.e., they have what I like to call “the mechanic’s touch”.
*   They have strong fundamentals, so they immediately get up to speed with new tools and systems where knowledge, not skill is the bottleneck.
*   AI is still sensitive to language and style and will often mirror the tastes and sensibilities of the prompter. Highly skilled engineers have really sharpened taste and instinct for what works and what doesn’t.

Therefore, embody the care of a craftperson. At the end of the day, you should produce artifacts you are proud of, even if the AI assisted in making it. This has translated well into the output I am seeing from these systems.

Here’s an example. This prompt is not unreasonable but not particularly thoughtful:

```
Write a Python rate limiter that limits users to 10 requests per minute.
```

I would expect this prompt to give okay results, but also miss some edge cases, good practices and quality standards. This is how you might see someone at nilenso prompt an AI for the same task:

```
Implement a token bucket rate limiter in Python with the following requirements:

- 10 requests per minute per user (identified by `user_id` string)
- Thread-safe for concurrent access
- Automatic cleanup of expired entries
- Return tuple of (allowed: bool, retry_after_seconds: int)

Consider:
- Should tokens refill gradually or all at once?
- What happens when the system clock changes?
- How to prevent memory leaks from inactive users?

Prefer simple, readable implementation over premature optimization. Use stdlib only (no Redis/external deps).
```

Guess which prompt is going to better achieve the program designer’s intent?

A technique that has worked well for us is _metaprompting_. I prompt the model with a simple task and ask it to help surface tradeoffs and edge cases. Then I turn it into a tech spec and hand it off to another LLM agent to execute. Even the “better prompt” I shared above is a result of asking the AI to come up with a good prompt. From my experience, models have become good at prompting themselves.

The mechanics of what works for these tools are in flux, but one robust principle is to really work on yourself to be a good engineer. Your habits will quickly pass on to the AI systems you work with. The reason this works is because what helps the human helps the AI.

What helps the human helps the AI
---------------------------------

I shall clarify what software engineering is, something I found worth revisiting in the light of disruption from AI advancements.

Software engineering is not about writing code. Or at least, that’s not the defining characteristic, much like how writing is not wrist exercises with ink on paper.

To me software engineering is the art and science of maintaining a large body of well-defined mental models that achieve a business or economic need. Much of the work is around crafting and curating these large, complex sociotechnical systems, and code is just one representation of these systems.

Until AI is good enough to engulf this whole sociotechnical system and expel out all the humans cultivating it, it has to participate and benefit from this very system. In simpler words: AI thrives far, far better in an environment in which a human would also thrive. Which means your team’s software fundamentals should be strong.

A system in which AI thrives is one with markers of a high quality team and codebase. These are:

*   Good test coverage, with _useful_ assertions
*   Automated linting, formatting and test checks before code merges
*   Continuous integration and deployment
*   Well documented changes, tech specs, ADRs with good commit messages
*   Consistent styles and patterns, enforced through a formatter
*   Simple, concise, well-organised code
*   Clearly defined features, broken down into multiple small story cards

Today’s AI can and will make use of all these things to make things “just work”. When I give a coding agent a task, it keeps correcting itself in the agentic loop by running the test cases and static analysis tools. This greatly reduces the hand-holding and intervention needed to get work done.

A rich environment and context helps the AI work better.

Here’s an anecdote: when I was working at a project that had two services, one of them had all of the things I described above—good tests, well-documented changes, consistent patterns in the code, lots of checks and guardrails. The other service was messier and had none of the above. Our AI coding assistant struggled to complete a task of equal difficulty on the latter codebase when compared to the former! This is likely because the messier codebase was as confusing for the AI as it would be for a human. There were mixed signals about the right way to do things.

Tools and techniques in the editor
----------------------------------

Now that I have outlined the general strategy, here are some tactics that have helped me.

### Use the best frontier AI models, don’t cheap out.

*   Use the best coding model available. Do not try to save credits and cost by using a worse model. The goodness of a good model compounds. All the tactics that I present ahead will work far better when you have a strong coding model to begin with.

### Be excellent at providing context.

*   The effectiveness of AI-assisted coding is strongly dependent on how skillfully you can provide the right context to the LLM.
*   Use an “agentic” coding tool. These are tools that are able to read and analyse files, run shell commands, fetch docs, create plans and execute on those plans, needing no human intervention (except maybe approvals). Our current recommendation for tools that do this are Claude Code, Windsurf, Cursor, Cline.
*   LLMs can get distracted and fall into rabbitholes if given irrelevant or a cluttered context. Focus its attention by only @-mentioning files that are relevant and linking only to documentation that helps the task.
*   Encode coding standards and practices in a [RULES.md](http://rules.md/) file. Symlink this file to agent specific rules files such as `.cursorrules`, `.windsurfrules`, [`claude.md`](http://claude.md/), [`agents.md`](http://agents.md/) etc 
    *   This file should have information about the tech stack, how to use the dev tooling and run the linter, coding standard and patterns, and cover for common mistakes that the LLMs have made when working with the code. [Here’s an example](https://github.com/modelcontextprotocol/python-sdk/blob/main/CLAUDE.md).

### Implementing a new feature or refactor

*   Break down the problem. AI works better the more specific you are. Remember, you can also use the AI to reduce the tedium of making your prompts better written and more specific. Reasoning models are great at this!
*   If you are working on a big feature, break it down into small tasks, and feed the tasks one by one, making a commit at the end of each task. If you do these with your stories, the story card description with the task list is often a very helpful description for the AI.
*   Supply tech specs and relevant documentation about the product and feature. Don’t just ask it to write code without broader context of the product. Also feed it documentation on how to use the libraries you are using. Pasting links to documentation often works with most tools. Some libraries provide a [llms.txt](https://llmstxt.org/) for coding agents to use.
*   Another pattern that has worked well for us is to break down the feature into “planning” and “execution” stages. Some coding agents already do this kind of a breakdown for you.
*   Do not take AI suggestions for granted. Ask it to justify its choices, present alternatives and think about advantages and drawbacks.

### Debugging

*   Use AI to debug errors in its generation. Always paste the error context most relevant for the LLM to help it understand the issue (I prefer to delineate the error logs or output in a separate XML tag).
*   Explain what you have tried, and additional observations to help the model generate correct hypotheses and eliminate bad ones. Provide lots of context.

Tools and techniques outside the editor
---------------------------------------

### Use AI to grow your own skills and knowledge

*   LLMs are an infinitely patient teacher with massive world knowledge (and more recently, ability to research effectively). Aggressively use them to learn things and demystify any new code or stack. Relentlessly dig. Figure out the best practices. Ensure you are learning correctly by getting the LLM to cite high quality sources.

### Create extensive documentation

*   Create lots of detailed documentation easily by feeding codebases to the LLM. Egs: 
    *   Explain functionality, create a knowledge base
    *   Summarise all the current metrics being collected
    *   Identify missing test cases more intelligently

There’s a good reason to do this—documentation is now cheap to generate and feeds back into making your LLMs (and humans) on the project a lot more effective.

### Microfriction lubricants

LLMs greatly reduce the cost of creating lubricants for all the minor friction points that teams run into on a daily basis.

*   Use them to create mockservers to coordinate and unblock work between frontend and backend teams. All that is needed is agreeing on a contract.
*   Create runbooks and guides for infra deployments, common types of troubleshooting and more by supplying shell history sessions to the LLM.
*   Feed existing runbooks and guides to an LLM to make them into scripts automating common tasks.

### Code review

*   Have a template for Pull Requests, feed the code diff (`git log -p <range>`) of each feature to the AI to explain the changes and how to deploy them. Some tools can already do this for you.
*   To reduce time to first PR review, use a code reviewing bot for the first part. But do not replace human review!
*   Use LLMs to explain a change that you don’t fully understand as a reviewer. Ask it for clarification, and then ask the implementer after gathering the necessary context.

### Debugging and monitoring live applications

*   Use researching capabilities of LLMs to help find solutions to uncommon errors. Follow the advice of debugging in the editor to debug outside it. Provide as much context as you can.
*   LLMs are quite decent at writing queries and alerting rules for observability tools. They also are good at crunching data and performing analyses by writing custom python code.

### Performance optimisations

*   Use LLMs to help you optimise databases and tune configuration. When doing so provide context on the infrastructure and hardware. Share query plans.
*   [This](https://blog.nilenso.com/blog/2025/05/08/psa-ai-can-optimise-your-database/) is an example of such an interaction I had recently.

Implications on how AI changes craft
------------------------------------

This is a huge shift in how we write software, and I believe it warrants some changes to ideas that were previously considered common wisdom.

Firstly, It’s less valuable to spend too much time looking for and building sophisticated abstractions. DRY is useful for ensuring patterns in the code don’t go out of sync, but there are costs to implementing and maintaining an abstraction to handle changing requirements. LLMs make some repetition palatable and allow you to wait a bit more and avoid premature abstraction.

Redoing work is now extremely cheap. Code in the small is less important than structural patterns and organisation of the code in the large. You can also build lots of prototypes to test an idea out. For this, vibe-coding is great, as long as the prototype is thrown away and rewritten properly later.

Working with LLMs also lets you take advantage of the generator-verifier gap. Often it’s easier to verify and fix things than it is to produce them from scratch. This reduces activation energy to try new things.

Tests are non-negotiable, and AI removes all excuses to not write them because of how fast they can belt them out. But always review the assertions!

Future additions to this playbook as we learn more about these tools
--------------------------------------------------------------------

*   Deploying autonomous agents like Devin/Jules/Claude Code and using them well
*   AI tooling for writing queries, performing data analysis
*   Concerns with leaking proprietary code, hosted LLM options, etc
*   Building a culture of sharing prompts, patterns and templates
*   Effective ways of driving AI adoption in teams

References
----------

[Programming with LLMs - David Crawshaw](https://crawshaw.io/blog/programming-with-llms)

[Here’s how I use LLMs to help me write code - Simon Willison](https://simonwillison.net/2025/Mar/11/using-llms-for-code/)

[How I use “AI” - Nicholas Carlini](https://nicholas.carlini.com/writing/2024/how-i-use-ai.html)
