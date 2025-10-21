Title: Claude Code for web—a new asynchronous coding agent from Anthropic

URL Source: https://simonwillison.net/2025/Oct/20/claude-code-for-web/

Markdown Content:
20th October 2025

Anthropic launched Claude Code for web this morning. It’s an [asynchronous coding agent](https://simonwillison.net/tags/async-coding-agents/)—their answer to OpenAI’s [Codex Cloud](https://simonwillison.net/2025/May/16/openai-codex/) and [Google’s Jules](https://simonwillison.net/2025/May/19/jules/), and has a very similar shape. I had preview access over the weekend and I’ve already seen some very promising results from it.

It’s available online at [claude.ai/code](https://claude.ai/) and shows up as a tab in the Claude iPhone app as well:

![Image 1: Screenshot of Claude AI interface showing a conversation about updating a README file. The left sidebar shows "Claude" at the top, followed by navigation items: "Chats", "Projects", "Artifacts", and "Code" (highlighted). Below that is "Starred" section listing several items with trash icons: "LLM", "Python app", "Check my post", "Artifacts", "Summarize", and "Alt text writer". The center panel shows a conversation list with items like "In progress", "Run System C", "Idle", "Update Rese", "Run Matplotl", "Run Marketin", "WebAssembl", "Benchmark M", "Build URL Qu", and "Add Read-Or". The right panel displays the active conversation titled "Update Research Project README" showing a task to update a GitHub README file at https://github.com/simonw/research/blob/main/deepseek-ocr-nvidia-spark/README.md, followed by Claude's response and command outputs showing file listings with timestamps from Oct 20 17:53.](https://static.simonwillison.net/static/2025/claude-code-for-web.jpg)

As far as I can tell it’s their latest [Claude Code CLI](https://www.claude.com/product/claude-code) app wrapped in a container (Anthropic are getting _really_[good at containers](https://simonwillison.net/2025/Sep/9/claude-code-interpreter/) these days) and configured to `--dangerously-skip-permissions`. It appears to behave exactly the same as the CLI tool, and includes a neat “teleport” feature which can copy both the chat transcript and the edited files down to your local Claude Code CLI tool if you want to take over locally.

It’s very straight-forward to use. You point Claude Code for web at a GitHub repository, select an environment (fully locked down, restricted to an allow-list of domains or configured to access domains of your choosing, including “*” for everything) and kick it off with a prompt.

While it’s running you can send it additional prompts which are queued up and executed after it completes its current step.

Once it’s done it opens a branch on your repo with its work and can optionally open a pull request.

#### Putting Claude Code for web to work[#](https://simonwillison.net/2025/Oct/20/claude-code-for-web/#putting-claude-code-for-web-to-work)

Claude Code for web’s PRs are indistinguishable from Claude Code CLI’s, so Anthropic told me it was OK to submit those against public repos even during the private preview. Here are some examples from this weekend:

*   [Add query-string-stripper.html tool](https://github.com/simonw/tools/pull/73) against my simonw/tools repo—a _very_ simple task that creates (and deployed via GitHub Pages) this [query-string-stripper](https://tools.simonwillison.net/query-string-stripper) tool.
*   [minijinja vs jinja2 Performance Benchmark](https://github.com/simonw/research/tree/main/minijinja-vs-jinja2)—I ran this against a private repo and then copied the results here, so no PR. Here’s [the prompt](https://github.com/simonw/research/blob/main/minijinja-vs-jinja2/README.md#the-prompt) I used.
*   [Update deepseek-ocr README to reflect successful project completion](https://github.com/simonw/research/pull/1)—I noticed that the README produced by Claude Code CLI for [this project](https://simonwillison.net/2025/Oct/20/deepseek-ocr-claude-code/) was misleadingly out of date, so I had Claude Code for web fix the problem.

That second example is the most interesting. I saw [a tweet from Armin](https://x.com/mitsuhiko/status/1980034078297514319) about his [MiniJinja](https://github.com/mitsuhiko/minijinja) Rust template language [adding support](https://github.com/mitsuhiko/minijinja/pull/841) for Python 3.14 free threading. I hadn’t realized that project _had_ Python bindings, so I decided it would be interesting to see a quick performance comparison between MiniJinja and Jinja2.

I ran Claude Code for web against a private repository with a completely open environment (`*` in the allow-list) and prompted:

> I’m interested in benchmarking the Python bindings for [https://github.com/mitsuhiko/minijinja](https://github.com/mitsuhiko/minijinja) against the equivalente template using Python jinja2
> 
> 
> Design and implement a benchmark for this. It should use the latest main checkout of minijinja and the latest stable release of jinja2. The benchmark should use the uv version of Python 3.14 and should test both the regular 3.14 and the 3.14t free threaded version—so four scenarios total
> 
> 
> The benchmark should run against a reasonably complicated example of a template, using template inheritance and loops and such like In the PR include a shell script to run the entire benchmark, plus benchmark implantation, plus markdown file describing the benchmark and the results in detail, plus some illustrative charts created using matplotlib

I entered this into the Claude iPhone app on my mobile keyboard, hence the typos.

It churned away for a few minutes and gave me exactly what I asked for. Here’s one of the [four charts](https://simonwillison.net/2025/Oct/20/claude-code-for-web/) it created:

![Image 2: Line chart titled "Rendering Time Across Iterations" showing rendering time in milliseconds (y-axis, ranging from approximately 1.0 to 2.5 ms) versus iteration number (x-axis, ranging from 0 to 200+). Four different lines represent different versions: minijinja (3.14t) shown as a solid blue line, jinja2 (3.14) as a solid orange line, minijinja (3.14) as a solid green line, and jinja2 (3.14t) as a dashed red line. The green line (minijinja 3.14) shows consistently higher rendering times with several prominent spikes reaching 2.5ms around iterations 25, 75, and 150. The other three lines show more stable, lower rendering times between 1.0-1.5ms with occasional fluctuations.](https://static.simonwillison.net/static/2025/minijinja-timeline.jpg)

(I was surprised to see MiniJinja out-performed by Jinja2, but I guess Jinja2 has had a decade of clever performance optimizations and doesn’t need to deal with any extra overhead of calling out to Rust.)

Note that I would likely have got the _exact same_ result running this prompt against Claude CLI on my laptop. The benefit of Claude Code for web is entirely in its convenience as a way of running these tasks in a hosted container managed by Anthropic, with a pleasant web and mobile UI layered over the top.

#### Anthropic are framing this as part of their sandboxing strategy[#](https://simonwillison.net/2025/Oct/20/claude-code-for-web/#anthropic-are-framing-this-as-part-of-their-sandboxing-strategy)

It’s interesting how Anthropic chose to announce this new feature: the product launch is buried half way down their new engineering blog post [Beyond permission prompts: making Claude Code more secure and autonomous](https://www.anthropic.com/engineering/claude-code-sandboxing), which starts like this:

> Claude Code’s new sandboxing features, a bash tool and Claude Code on the web, reduce permission prompts and increase user safety by enabling two boundaries: filesystem and network isolation.

I’m _very_ excited to hear that Claude Code CLI is taking sandboxing more seriously. I’ve not yet dug into the details of that—it looks like it’s using seatbelt on macOS and [Bubblewrap](https://github.com/containers/bubblewrap) on Linux.

Anthropic released a new open source (Apache 2) library, [anthropic-experimental/sandbox-runtime](https://github.com/anthropic-experimental/sandbox-runtime), with their implementation of this so far.

Filesystem sandboxing is relatively easy. The harder problem is network isolation, which they describe like this:

> **Network isolation**, by only allowing internet access through a unix domain socket connected to a proxy server running outside the sandbox. This proxy server enforces restrictions on the domains that a process can connect to, and handles user confirmation for newly requested domains. And if you’d like further-increased security, we also support customizing this proxy to enforce arbitrary rules on outgoing traffic.

This is _crucial_ to protecting against both prompt injection and [lethal trifecta](https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/) attacks. The best way to prevent lethal trifecta attacks is to cut off one of the three legs, and network isolation is how you remove the data exfiltration leg that allows successful attackers to steal your data.

If you run Claude Code for web in “No network access” mode you have nothing to worry about.

I’m a little bit nervous about their “Trusted network access” environment. It’s intended to only allow access to domains relating to dependency installation, but the [default domain list](https://docs.claude.com/en/docs/claude-code/claude-code-on-the-web#default-allowed-domains) has dozens of entries which makes me nervous about unintended exfiltration vectors sneaking through.

You can also configure a custom environment with your own allow-list. I have one called “Everything” which allow-lists “*”, because for projects like my MiniJinja/Jinja2 comparison above there are no secrets or source code involved that need protecting.

I see Anthropic’s focus on sandboxes as an acknowledgment that coding agents run in YOLO mode (`--dangerously-skip-permissions` and the like) are _enormously_ more valuable and productive than agents where you have to approve their every step.

The challenge is making it convenient and easy to run them safely. This kind of sandboxing kind is the only approach to safety that feels credible to me.

**Update**: A note on cost: I’m currently using a Claude “Max” plan that Anthropic gave me in order to test some of their features, so I don’t have a good feeling for how Claude Code would cost for these kinds of projects.

From running `npx ccusage@latest` (an [unofficial cost estimate tool](https://github.com/ryoppippi/ccusage)) it looks like I’m using between $1 and $5 worth of daily Claude CLI invocations at the moment.