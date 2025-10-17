Title: Claude Skills are awesome, maybe a bigger deal than MCP

URL Source: https://simonwillison.net/2025/Oct/16/claude-skills/

Markdown Content:
16th October 2025

Anthropic this morning [introduced Claude Skills](https://www.anthropic.com/news/skills), a new pattern for making new abilities available to their models:

> Claude can now use _Skills_ to improve how it performs specific tasks. Skills are folders that include instructions, scripts, and resources that Claude can load when needed.
> 
> 
> Claude will only access a skill when it’s relevant to the task at hand. When used, skills make Claude better at specialized tasks like working with Excel or following your organization’s brand guidelines.

Their engineering blog has a [more detailed explanation](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills). There’s also a new [anthropic/skills](https://github.com/anthropics/skills) GitHub repo.

(I inadvertently preempted their announcement of this feature when I reverse engineered and [wrote about it last Friday](https://simonwillison.net/2025/Oct/10/claude-skills/)!)

Skills are conceptually extremely simple: a skill is a Markdown file telling the model how to do something, optionally accompanied by extra documents and pre-written scripts that the model can run to help it accomplish the tasks described by the skill.

Claude’s new [document creation abilities](https://www.anthropic.com/news/create-files), which accompanied [their new code interpreter feature](https://simonwillison.net/2025/Sep/9/claude-code-interpreter/) in September, turned out to be entirely implemented using skills. Those are [now available Anthropic’s repo](https://github.com/anthropics/skills/tree/main/document-skills) covering `.pdf`, `.docx`, `.xlsx`, and `.pptx` files.

There’s one extra detail that makes this a feature, not just a bunch of files on disk. At the start of a session Claude’s various harnesses can scan all available skill files and read a short explanation for each one from the frontmatter YAML in the Markdown file. This is _very_ token efficient: each skill only takes up a few dozen extra tokens, with the full details only loaded in should the user request a task that the skill can help solve.

*   [Trying out the slack-gif-creator skill](https://simonwillison.net/2025/Oct/16/claude-skills/#trying-out-the-slack-gif-creator-skill)
*   [Skills depend on a coding environment](https://simonwillison.net/2025/Oct/16/claude-skills/#skills-depend-on-a-coding-environment)
*   [Claude Code as a General Agent](https://simonwillison.net/2025/Oct/16/claude-skills/#claude-as-a-general-agent)
*   [Skills compared to MCP](https://simonwillison.net/2025/Oct/16/claude-skills/#skills-compared-to-mcp)
*   [Here come the Skills](https://simonwillison.net/2025/Oct/16/claude-skills/#here-come-the-skills)
*   [The simplicity is the point](https://simonwillison.net/2025/Oct/16/claude-skills/#the-simplicity-is-the-point)

#### Trying out the slack-gif-creator skill[#](https://simonwillison.net/2025/Oct/16/claude-skills/#trying-out-the-slack-gif-creator-skill)

Here’s that metadata for an example [slack-gif-creator skill](https://github.com/anthropics/skills/blob/main/slack-gif-creator/SKILL.md) that Anthropic published this morning:

> Toolkit for creating animated GIFs optimized for Slack, with validators for size constraints and composable animation primitives. This skill applies when users request animated GIFs or emoji animations for Slack from descriptions like “make me a GIF for Slack of X doing Y”.

I just tried this skill out in the Claude mobile web app, against Sonnet 4.5. First I enabled the slack-gif-creator skill [in the settings](https://claude.ai/settings/capabilities), then I prompted:

> `Make me a gif for slack about how Skills are way cooler than MCPs`

And Claude [made me this GIF](https://claude.ai/share/eff7ae7b-b386-417b-9fa0-213fa76ace6e). Click to play (it’s almost epilepsy inducing, hence the click-to-play mechanism):

![Image 1](https://static.simonwillison.net/static/2025/skills_vs_mcps_still.gif)

OK, this particular GIF is terrible, but the great thing about skills is that they’re very easy to iterate on to make them better.

Here are some noteworthy snippets from [the Python script it wrote](https://gist.github.com/simonw/ef35bb9e6c514d1d596dac9227da482b), comments mine:

# Start by adding the skill's directory to the Python path
import sys
sys.path.insert(0, '/mnt/skills/examples/slack-gif-creator')

from PIL import Image, ImageDraw, ImageFont
# This class lives in the core/ directory for the skill
from core.gif_builder import GIFBuilder

# ... code that builds the GIF ...

# Save it to disk:
info = builder.save('/mnt/user-data/outputs/skills_vs_mcps.gif', 
                    num_colors=128, 
                    optimize_for_emoji=False)

print(f"GIF created successfully!")
print(f"Size: {info['size_kb']:.1f} KB ({info['size_mb']:.2f} MB)")
print(f"Frames: {info['frame_count']}")
print(f"Duration: {info['duration_seconds']:.1f}s")

# Use the check_slack_size() function to confirm it's small enough for Slack:
passes, check_info = check_slack_size('/mnt/user-data/outputs/skills_vs_mcps.gif', is_emoji=False)
if passes:
    print("✓ Ready for Slack!")
else:
    print(f"⚠ File size: {check_info['size_kb']:.1f} KB (limit: {check_info['limit_kb']} KB)")
This is pretty neat. Slack GIFs need to be a maximum of 2MB, so the skill includes a validation function which the model can use to check the file size. If it’s too large the model can have another go at making it smaller.

#### Skills depend on a coding environment[#](https://simonwillison.net/2025/Oct/16/claude-skills/#skills-depend-on-a-coding-environment)

The skills mechanism is _entirely dependent_ on the model having access to a filesystem, tools to navigate it and the ability to execute commands in that environment.

This is a common pattern for LLM tooling these days—ChatGPT Code Interpreter was the first big example of this [back in early 2023](https://simonwillison.net/2023/Apr/12/code-interpreter/), and the pattern later extended to local machines via coding agent tools such as Cursor, Claude Code, Codex CLI and Gemini CLI.

This requirement is the biggest difference between skills and other previous attempts at expanding the abilities of LLMs, such as MCP and [ChatGPT Plugins](https://simonwillison.net/tags/chatgpt-plugins/). It’s a significant dependency, but it’s somewhat bewildering how much new capability it unlocks.

The fact that skills are so powerful and simple to create is yet another argument in favor of making safe coding environments available to LLMs. The word **safe** there is doing a _lot_ of work though! We really need to figure out how best to sandbox these environments such that attacks such as prompt injections are limited to an acceptable amount of damage.

#### Claude Code as a General Agent[#](https://simonwillison.net/2025/Oct/16/claude-skills/#claude-as-a-general-agent)

Back in January I [made some foolhardy predictions about AI/LLMs](https://simonwillison.net/2025/Jan/10/ai-predictions/), including that “agents” would once again fail to happen:

> I think we are going to see a _lot_ more froth about agents in 2025, but I expect the results will be a great disappointment to most of the people who are excited about this term. I expect a lot of money will be lost chasing after several different poorly defined dreams that share that name.

I was entirely wrong about that. 2025 really has been the year of “agents”, no matter which of the many [conflicting definitions](https://simonwillison.net/tags/agent-definitions/) you decide to use (I eventually settled on "[tools in a loop](https://simonwillison.net/2025/Sep/18/agents/)").

[Claude Code](https://www.claude.com/product/claude-code) is, with hindsight, poorly named. It’s not purely a coding tool: it’s a tool for general computer automation. _Anything_ you can achieve by typing commands into a computer is something that can now be automated by Claude Code. It’s best described as a **general agent**. Skills make this a whole lot more obvious and explicit.

I find the potential applications of this trick somewhat dizzying. Just thinking about this with my data journalism hat on: imagine a folder full of skills that covers tasks like the following:

*   Where to get US census data from and how to understand its structure
*   How to load data from different formats into SQLite or DuckDB using appropriate Python libraries
*   How to publish data online, as Parquet files in S3 or pushed as tables to Datasette Cloud
*   A skill defined by an experienced data reporter talking about how best to find the interesting stories in a new set of data
*   A skill that describes how to build clean, readable data visualizations using D3

Congratulations, you just built a “data journalism agent” that can discover and help publish stories against fresh drops of US census data. And you did it with a folder full of Markdown files and maybe a couple of example Python scripts.

#### Skills compared to MCP[#](https://simonwillison.net/2025/Oct/16/claude-skills/#skills-compared-to-mcp)

[Model Context Protocol](https://modelcontextprotocol.io/) has attracted an enormous amount of buzz since its initial release back [in November last year](https://simonwillison.net/2024/Nov/25/model-context-protocol/). I like to joke that one of the reasons it took off is that every company knew they needed an “AI strategy”, and building (or announcing) an MCP implementation was an easy way to tick that box.

Over time the limitations of MCP have started to emerge. The most significant is in terms of token usage: GitHub’s official MCP on its own famously consumes tens of thousands of tokens of context, and once you’ve added a few more to that there’s precious little space left for the LLM to actually do useful work.

My own interest in MCPs has waned ever since I started taking coding agents seriously. Almost everything I might achieve with an MCP can be handled by a CLI tool instead. LLMs know how to call `cli-tool --help`, which means you don’t have to spend many tokens describing how to use them—the model can figure it out later when it needs to.

Skills have exactly the same advantage, only now I don’t even need to implement a new CLI tool. I can drop a Markdown file in describing how to do a task instead, adding extra scripts only if they’ll help make things more reliable or efficient.

#### Here come the Skills[#](https://simonwillison.net/2025/Oct/16/claude-skills/#here-come-the-skills)

One of the most exciting things about Skills is how easy they are to share. I expect many skills will be implemented as a single file—more sophisticated ones will be a folder with a few more.

Anthropic have [Agent Skills documentation](https://docs.claude.com/en/docs/agents-and-tools/agent-skills/overview) and a [Claude Skills Cookbook](https://github.com/anthropics/claude-cookbooks/tree/main/skills). I’m already thinking through ideas of skills I might build myself, like one on [how to build Datasette plugins](https://simonwillison.net/2025/Oct/8/claude-datasette-plugins/).

Something else I love about the design of skills is there is nothing at all preventing them from being used with other models.

You can grab a skills folder right now, point Codex CLI or Gemini CLI at it and say “read pdf/SKILL.md and then create me a PDF describing this project” and it will work, despite those tools and models having no baked in knowledge of the skills system.

I expect we’ll see a Cambrian explosion in Skills which will make this year’s MCP rush look pedestrian by comparison.

#### The simplicity is the point[#](https://simonwillison.net/2025/Oct/16/claude-skills/#the-simplicity-is-the-point)

I’ve seen a some push back against skills as being so simple they’re hardly a feature at all. Plenty of people have experimented with the trick of dropping extra instructions into a Markdown file and telling the coding agent to read that file before continuing with a task. [AGENTS.md](https://agents.md/) is a well established pattern, and that file can already include instructions to “Read PDF.md before attempting to create a PDF”.

The core simplicity of the skills design is why I’m so excited about it.

MCP is a whole [protocol specification](https://modelcontextprotocol.io/specification/2025-06-18), covering hosts, clients, servers, resources, prompts, tools, sampling, roots, elicitation and three different transports (stdio, streamable HTTP and originally SSE).

Skills are Markdown with a tiny bit of YAML metadata and some optional scripts in whatever you can make executable in the environment. They feel a lot closer to the spirit of LLMs—throw in some text and let the model figure it out.

They outsource the hard parts to the LLM harness and the associated computer environment. Given everything we have learned about LLMs’ ability to run tools over the last couple of years I think that’s a very sensible strategy.