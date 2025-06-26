Title: How I Vibe Coding?

URL Source: https://xuanwo.io/2025/03-how-i-vibe-coding/

Markdown Content:
Hello everyone, long time no see. I've been evaluating various AI copilots extensively lately and have developed a fairly stable workflow that suits my context and background. I'm now writing it down to hopefully inspire you and to receive some feedback as well.

Background
----------

I'm [Xuanwo](https://github.com/Xuanwo/), an open source Rust engineer.

_Open source_ means I primarily work in open source environments. I can freely allow LLMs to access my code as context, without needing to set up a local LLM to prevent code leaks or meet company regulations. It also means my work is publicly available, so LLMs can easily search for and retrieve my code and API documentation.

_Rust_ means I spend most of my time writing Rust. It's a nice language has _great documentation, a friendly compiler with useful error messages, and top-notch tooling_. Rust has a strong ecosystem for developer tools and is highly accessible. Most LLMs already know how to use `cargo check`, `cargo clippy`, and `cargo test`. Writing Rust also means that both I and AI only need to work with code in text form. We don't need complex workflows like those often seen in frontend development: coding, screen capturing, image diffing, and so on.

_Engineer_ means I'm an engineer by profession. I earn my living through my coding work. I'm not a content producer or advertiser. As an engineer, I choose the most practical tools for myself. I want these tools to be fast, stable, and useful. I don't need them to be flashy, and I don't care whether they can build a website in one shot or write a flappy bird with correct collision detection.

Toolset
-------

My current toolset consists of [`Zed`](https://github.com/zed-industries/zed) and [`Claude Code`](https://github.com/anthropics/claude-code). More specifically, I run `claude` in a Zed terminal tab, which allows me to access both the code and its changes alongside the LLM.

![Image 1](https://xuanwo.io/2025/03-how-i-vibe-coding/claude-code-in-zed.png)

To give `claude-code` its full capabilities, it's actually running in [a container I built myself](https://gist.github.com/Xuanwo/68e04e11949d130a6a579d8eeb6c6a03). Whenever I need to run `claude`, I use `docker run` instead. I also have an alias `claudex` for this purpose:

```
# claudex
alias claudex='docker run -it --rm \
  -v $(pwd):/workspace \
  -v ~/.claude:/home/user/.claude \
  -v ~/.claude.json:/home/user/.claude.json \
  -v ~/.config/gh:/home/user/.config/gh \
  -v ~/Notes:/home/user/Notes \
  xuanwo-dev'
```

Mindset
-------

Before introducing my workflow, I want to share my current mindset on LLMs. At the time of writing, I see LLMs as similar to recent graduates at a junior level.

As juniors, they have several strengths: They possess a solid understanding of widely used existing techniques. They can quickly learn new tools or patterns. They are friendly and eager to tackle any task you assign. They never complain about your requests. They excel at repetitive or highly structured tasks, as long as you pay them.

However, as juniors, they also have some shortcomings. They lack knowledge of your specific project or tasks. They don't have a clear goal or vision and require your guidance for direction. At times, they can be overly confident, inventing nonexistent APIs or using APIs incorrectly. Occasionally, they may get stuck and fail to find a way out.

As a mentor, leader, or boss, my job is to provide the right context, set a clear direction, and always be prepared to step in when needed. Currently, my approach is to have AI write code that I can personally review and take responsibility for.

For example, I find that LLMs are most effective when refactoring projects that have a clear API and nive test coverage. I will refactor the service for `aws` first, and then have the LLMs follow the same patterns to refactor the `azure` and `gcs` services. I rarely allow LLMs to initiate entirely new projects or create completely new components. Most of the time, I define the API myself and ask the LLMs to follow the same design and handle the implementation details.

Workflow
--------

My workflow is quiet simple: I arrange my day in 5 hours chunk which aligns with [claude usage limits](https://support.anthropic.com/en/articles/11014257-about-claude-s-max-plan-usage). I map those two chunks to every day's morning and afternoon.

In the morining, I will collect, read, think and plan. I will write my thinking down in my `Notes`, powered by [`Obsidian`](https://obsidian.md/). All my notes is in markdown formats, so LLMs like Claude Opus 4 can understand without any other tools. I will feed my notes to claude code directly, and request them to read my notes while needed.

In the afternoon, I will run `claudex` inside my projects, as I mentioned earlier. I will monitor their progress from time to time and prepare myself to step in when necessary. Sometimes, I use `git worktree` to spawn additional Claude instances so they can collaborate on the same projects.

Claude works very quickly, so I spend most of my time reviewing code. To reduce the burden of code review, I also design robust test frameworks for my projects to ensure correct behavior. `rust`'s excellent developer experience allows me to instruct the LLMs to run `cargo check`, `cargo clippy`, and `cargo test` on the code independently. They may need to repeat this process a few times to get everything right, but most of the time, they figure it out on their own.

While reviewing code, I pay close attention to the public API and any tricky parts within the codebase. LLMs are like junior developers. Sometimes, they might overemphasize certain aspects of a task and lose sight of the overall context. For example, they can focus too much on minor details of API design without realizing that the entire approach could be improved with a better overall design. This also reinforces my belief that you should only allow LLMs to write code you can control. Otherwise, you can't be sure the LLMs are doing things correctly. It's very dangerous if the LLMs are working in a direction you don't understand.

In my workflow, I only need `claude` and `zed`. `claude` excels at using tools and understanding context, while `zed` is fast and responsive. As a Rust developer, I don't have a strong need for various extensions, so the main drawback of `zed`, its limited extension support, isn't a major issue for me.

Tips
----

Here are some tips I've learned from my recent exploration of AI agents and LLMs.

### Claude 4 is the best vibe coding model (for now)

Claude 4 Sonnet and Opus are the best coding models available so far.

Many people have different opinions on this and might argue: hey, o3, gemini-2.5-pro, or deepseek-r1 are better than Claude 4, they can build a working website in one shot! Unfortunately, I disagree, at least for my needs right now. As a Rust developer, I don't care if a model can build a website or demonstrate strong reasoning. What matters to me is whether it can use tools intelligently and efficiently. LLMs used for vibe coding should have a strong sense of planning and be skilled at coding. A smart model that doesn't know how to edit files can't truly serve as your coding copilot.

I'm not a content creator; I'm an engineer. I need a reliable tool that can help me complete my work. I'm not building demos or marketing materials. This isn't a game or a show that can be restarted repeatedly. I'm working on a project with downstream users, and I have to take responsibility for whatever the LLMs do. I need to collaborate with LLMs to achieve both my goals and my company's goals.

Claude 4 is the right tool.

### MCP is a lie

MCP is uesless for vibe coding.

Claude 4 is good at using tools. As long as you let it know that a tool is installed locally, it can use the tool effectively. It can even use `--help` to learn how to use it correctly. I've never encountered a scenario where I needed to use an MCP server. I tried the GitHub MCP server before, but it performed much worse than simply letting LLMs use the `gh` CLI locally.

Use tools instead of configuring MCP servers.

### Integrate AI into workflow

Integrate AI into your existing workflow instead of adapting yourself to AI.

AI workflows are constantly evolving. Stay calm and add the best tools to your toolkit. Don't change yourself just to fit a particular AI workflow. It's the tool's problem that can't be integrated into your existing workflow.

I've had some unsuccessful attempts at using Cursor or Windsurf. My progress began when I started incorporating Claude Code into portions of my daily workflow, rather than completely switching to a new IDE.

Recommended Readings
--------------------

Thank you for reading my post. I also recommend the following posts if you want to try vibe coding:

*   [Agentic Coding Recommendations](https://lucumr.pocoo.org/2025/6/12/agentic-coding/) from [@mitsuhiko](https://x.com/mitsuhiko)
*   [Here’s how I use LLMs to help me write code](https://simonwillison.net/2025/Mar/11/using-llms-for-code/) from [@simonw](https://x.com/simonw)

Hope you're enjoying the coding vibes: create more, hype less.
