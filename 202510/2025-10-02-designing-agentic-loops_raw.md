Title: Designing agentic loops

URL Source: https://simonwillison.net/2025/Sep/30/designing-agentic-loops/

Published Time: Thu, 02 Oct 2025 12:52:42 GMT

Markdown Content:
30th September 2025

Coding agents like Anthropic’s [Claude Code](https://claude.com/product/claude-code) and OpenAI’s [Codex CLI](https://github.com/openai/codex) represent a genuine step change in how useful LLMs can be for producing working code. These agents can now directly exercise the code they are writing, correct errors, dig through existing implementation details, and even run experiments to find effective code solutions to problems.

As is so often the case with modern AI, there is a great deal of depth involved in unlocking the full potential of these new tools.

A critical new skill to develop is **designing agentic loops**.

One way to think about coding agents is that they are brute force tools for finding solutions to coding problems. If you can reduce your problem to a clear goal and a set of tools that can iterate towards that goal a coding agent can often brute force its way to an effective solution.

My preferred definition of an LLM agent is something that [runs tools in a loop to achieve a goal](https://simonwillison.net/2025/Sep/18/agents/). The art of using them well is to carefully design the tools and loop for them to use.

*   [The joy of YOLO mode](https://simonwillison.net/2025/Sep/30/designing-agentic-loops/#the-joy-of-yolo-mode)
*   [Picking the right tools for the loop](https://simonwillison.net/2025/Sep/30/designing-agentic-loops/#picking-the-right-tools-for-the-loop)
*   [Issuing tightly scoped credentials](https://simonwillison.net/2025/Sep/30/designing-agentic-loops/#issuing-tightly-scoped-credentials)
*   [When to design an agentic loop](https://simonwillison.net/2025/Sep/30/designing-agentic-loops/#when-to-design-an-agentic-loop)
*   [This is still a very fresh area](https://simonwillison.net/2025/Sep/30/designing-agentic-loops/#this-is-still-a-very-fresh-area)

#### The joy of YOLO mode[#](https://simonwillison.net/2025/Sep/30/designing-agentic-loops/#the-joy-of-yolo-mode)

Agents are inherently dangerous—they can make poor decisions or fall victim to malicious [prompt injection attacks](https://simonwillison.net/tags/prompt-injection/), either of which can result in harmful results from tool calls. Since the most powerful coding agent tool is “run this command in the shell” a rogue agent can do anything that you could do by running a command yourself.

To [quote Solomon Hykes](https://simonwillison.net/2025/Jun/5/wrecking-its-environment-in-a-loop/):

> **An AI agent is an LLM wrecking its environment in a loop.**

Coding agents like Claude Code counter this by defaulting to asking you for approval of almost every command that they run.

This is kind of tedious, but more importantly, it dramatically reduces their effectiveness at solving problems through brute force.

Each of these tools provides its own version of what I like to call YOLO mode, where everything gets approved by default.

This is _so dangerous_, but it’s also key to getting the most productive results!

Here are three key risks to consider from unattended YOLO mode.

1.   Bad shell commands deleting or mangling things you care about.
2.   Exfiltration attacks where something steals files or data visible to the agent—source code or secrets held in environment variables are particularly vulnerable here.
3.   Attacks that use your machine as a proxy to attack another target—for DDoS or to disguise the source of other hacking attacks.

If you want to run YOLO mode anyway, you have a few options:

1.   Run your agent in a secure sandbox that restricts the files and secrets it can access and the network connections it can make.
2.   Use someone else’s computer. That way if your agent goes rogue, there’s only so much damage they can do, including wasting someone else’s CPU cycles.
3.   Take a risk! Try to avoid exposing it to potential sources of malicious instructions and hope you catch any mistakes before they cause any damage.

Most people choose option 3.

Despite the existence of [container escapes](https://attack.mitre.org/techniques/T1611/) I think option 1 using Docker or the new Apple [container tool](https://github.com/apple/container) is a reasonable risk to accept for most people.

Option 2 is my favorite. I like to use [GitHub Codespaces](https://github.com/features/codespaces) for this—it provides a full container environment on-demand that’s accessible through your browser and has a generous free tier too. If anything goes wrong it’s a Microsoft Azure machine somewhere that’s burning CPU and the worst that can happen is code you checked out into the environment might be exfiltrated by an attacker, or bad code might be pushed to the attached GitHub repository.

There are plenty of other agent-like tools that run code on other people’s computers. [Code Interpreter](https://simonwillison.net/tags/code-interpreter/) mode in both ChatGPT and [Claude](https://simonwillison.net/2025/Sep/9/claude-code-interpreter/) can go a surprisingly long way here. I’ve also had a lot of success (ab)using OpenAI’s [Codex Cloud](https://chatgpt.com/features/codex).

Coding agents themselves implement various levels of sandboxing, but so far I’ve not seen convincing enough documentation of these to trust them.

**Update**: It turns out Anthropic have their own documentation on [Safe YOLO mode](https://www.anthropic.com/engineering/claude-code-best-practices#d-safe-yolo-mode) for Claude Code which says:

> Letting Claude run arbitrary commands is risky and can result in data loss, system corruption, or even data exfiltration (e.g., via prompt injection attacks). To minimize these risks, use `--dangerously-skip-permissions` in a container without internet access. You can follow this [reference implementation](https://github.com/anthropics/claude-code/tree/main/.devcontainer) using Docker Dev Containers.

Locking internet access down to a [list of trusted hosts](https://github.com/anthropics/claude-code/blob/5062ed93fc67f9322f807ecbf391ae4376cf8e83/.devcontainer/init-firewall.sh#L66-L75) is a great way to prevent exfiltration attacks from stealing your private source code.

#### Picking the right tools for the loop[#](https://simonwillison.net/2025/Sep/30/designing-agentic-loops/#picking-the-right-tools-for-the-loop)

Now that we’ve found a safe (enough) way to run in YOLO mode, the next step is to decide which tools we need to make available to the coding agent.

You can bring [MCP](https://modelcontextprotocol.io/) into the mix at this point, but I find it’s usually more productive to think in terms of shell commands instead. Coding agents are _really good_ at running shell commands!

If your environment allows them the necessary network access, they can also pull down additional packages from NPM and PyPI and similar. Ensuring your agent runs in an environment where random package installs don’t break things on your main computer is an important consideration as well!

Rather than leaning on MCP, I like to create an [AGENTS.md](https://agents.md/) (or equivalent) file with details of packages I think they may need to use.

For a project that involved taking screenshots of various websites I installed my own [shot-scraper](https://shot-scraper.datasette.io/) CLI tool and dropped the following in `AGENTS.md`:

```
To take a screenshot, run:

shot-scraper http://www.example.com/ -w 800 -o example.jpg
```

Just that one example is enough for the agent to guess how to swap out the URL and filename for other screenshots.

Good LLMs already know how to use a bewildering array of existing tools. If you say "use [playwright python](https://playwright.dev/python/)" or "use ffmpeg" most models will use those effectively—and since they’re running in a loop they can usually recover from mistakes they make at first and figure out the right incantations without extra guidance.

#### Issuing tightly scoped credentials[#](https://simonwillison.net/2025/Sep/30/designing-agentic-loops/#issuing-tightly-scoped-credentials)

In addition to exposing the right commands, we also need to consider what credentials we should expose to those commands.

Ideally we wouldn’t need any credentials at all—plenty of work can be done without signing into anything or providing an API key—but certain problems will require authenticated access.

This is a deep topic in itself, but I have two key recommendations here:

1.   Try to provide credentials to test or staging environments where any damage can be well contained.
2.   If a credential can spend money, set a tight budget limit.

I’ll use an example to illustrate. A while ago I was investigating slow cold start times for a scale-to-zero application I was running on [Fly.io](https://fly.io/).

I realized I could work a lot faster if I gave Claude Code the ability to directly edit Dockerfiles, deploy them to a Fly account and measure how long they took to launch.

Fly allows you to create organizations, and you can set a budget limit for those organizations and issue a Fly API key that can only create or modify apps within that organization...

So I created a dedicated organization for just this one investigation, set a $5 budget, issued an API key and set Claude Code loose on it!

In that particular case the results weren’t useful enough to describe in more detail, but this was the project where I first realized that “designing an agentic loop” was an important skill to develop.

#### When to design an agentic loop[#](https://simonwillison.net/2025/Sep/30/designing-agentic-loops/#when-to-design-an-agentic-loop)

Not every problem responds well to this pattern of working. The thing to look out for here are problems with **clear success criteria** where finding a good solution is likely to involve (potentially slightly tedious) **trial and error**.

Any time you find yourself thinking “ugh, I’m going to have to try a lot of variations here” is a strong signal that an agentic loop might be worth trying!

A few examples:

*   **Debugging**: a test is failing and you need to investigate the root cause. Coding agents that can already run your tests can likely do this without any extra setup.
*   **Performance optimization**: this SQL query is too slow, would adding an index help? Have your agent benchmark the query and then add and drop indexes (in an isolated development environment!) to measure their impact.
*   **Upgrading dependencies**: you’ve fallen behind on a bunch of dependency upgrades? If your test suite is solid an agentic loop can upgrade them all for you and make any minor updates needed to reflect breaking changes. Make sure a copy of the relevant release notes is available, or that the agent knows where to find them itself.
*   **Optimizing container sizes**: Docker container feeling uncomfortably large? Have your agent try different base images and iterate on the Dockerfile to try to shrink it, while keeping the tests passing.

A common theme in all of these is **automated tests**. The value you can get from coding agents and other LLM coding tools is massively amplified by a good, cleanly passing test suite. Thankfully LLMs are great for accelerating the process of putting one of those together, if you don’t have one yet.

#### This is still a very fresh area[#](https://simonwillison.net/2025/Sep/30/designing-agentic-loops/#this-is-still-a-very-fresh-area)

**Designing agentic loops** is a very new skill—Claude Code was [first released](https://www.anthropic.com/news/claude-3-7-sonnet) in just February 2025!

I’m hoping that giving it a clear name can help us have productive conversations about it. There’s _so much more_ to figure out about how to use these tools as effectively as possible.