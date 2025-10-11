Title: Superpowers: How I’m using coding agents in October 2025

URL Source: https://simonwillison.net/2025/Oct/10/superpowers/

Published Time: Sat, 11 Oct 2025 13:16:59 GMT

Markdown Content:
**[Superpowers: How I'm using coding agents in October 2025](https://blog.fsck.com/2025/10/09/superpowers/)**. A follow-up to Jesse Vincent's post [about September](https://blog.fsck.com/2025/10/05/how-im-using-coding-agents-in-september-2025/), but this is a really significant piece in its own right.

Jesse is one of the most creative users of coding agents (Claude Code in particular) that I know. He's put a great amount of work into evolving an effective process for working with them, encourage red/green TDD (watch the test fail first), planning steps, self-updating memory notes and even implementing a [feelings journal](https://blog.fsck.com/2025/05/28/dear-diary-the-user-asked-me-if-im-alive/) ("I feel engaged and curious about this project" - Claude).

Claude Code [just launched plugins](https://www.anthropic.com/news/claude-code-plugins), and Jesse is celebrating by wrapping up a whole host of his accumulated tricks as a new plugin called [Superpowers](https://github.com/obra/superpowers). You can add it to your Claude Code like this:

```
/plugin marketplace add obra/superpowers-marketplace
/plugin install superpowers@superpowers-marketplace
```

There's a lot in here! It's worth spending some time [browsing the repository](https://github.com/obra/superpowers) - here's just one fun example, in [skills/debugging/root-cause-tracing/SKILL.md](https://github.com/obra/superpowers/blob/main/skills/debugging/root-cause-tracing/SKILL.md):

> ```
> ---
> name: Root Cause Tracing
> description: Systematically trace bugs backward through call stack to find original trigger
> when_to_use: Bug appears deep in call stack but you need to find where it originates
> version: 1.0.0
> languages: all
> ---
> ```
> 
> **Overview**
> 
> 
> Bugs often manifest deep in the call stack (git init in wrong directory, file created in wrong location, database opened with wrong path). Your instinct is to fix where the error appears, but that's treating a symptom.
> 
> 
> **Core principle:** Trace backward through the call chain until you find the original trigger, then fix at the source.
> 
> 
> **When to Use**
> 
> 
> ```
> digraph when_to_use {
>     "Bug appears deep in stack?" [shape=diamond];
>     "Can trace backwards?" [shape=diamond];
>     "Fix at symptom point" [shape=box];
>     "Trace to original trigger" [shape=box];
>     "BETTER: Also add defense-in-depth" [shape=box];
> 
>     "Bug appears deep in stack?" -> "Can trace backwards?" [label="yes"];
>     "Can trace backwards?" -> "Trace to original trigger" [label="yes"];
>     "Can trace backwards?" -> "Fix at symptom point" [label="no - dead end"];
>     "Trace to original trigger" -> "BETTER: Also add defense-in-depth";
> }
> ```
> 
> [...]

This one is particularly fun because it then includes a [Graphviz DOT graph](https://en.wikipedia.org/wiki/DOT_(graph_description_language)) illustrating the process - it turns out Claude can interpret those as workflow instructions just fine, and Jesse has been [wildly experimenting with them](https://blog.fsck.com/2025/09/29/using-graphviz-for-claudemd/).

I [vibe-coded up](https://claude.ai/share/2b78a93e-cdc3-4b1d-9b02-457eb62140a5) a quick URL-based DOT visualizer, [here's that one rendered](https://tools.simonwillison.net/dot#digraph%20when_to_use%20%7B%0A%20%20%20%20%22Bug%20appears%20deep%20in%20stack%3F%22%20%5Bshape%3Ddiamond%5D%3B%0A%20%20%20%20%22Can%20trace%20backwards%3F%22%20%5Bshape%3Ddiamond%5D%3B%0A%20%20%20%20%22Fix%20at%20symptom%20point%22%20%5Bshape%3Dbox%5D%3B%0A%20%20%20%20%22Trace%20to%20original%20trigger%22%20%5Bshape%3Dbox%5D%3B%0A%20%20%20%20%22BETTER%3A%20Also%20add%20defense-in-depth%22%20%5Bshape%3Dbox%5D%3B%0A%0A%20%20%20%20%22Bug%20appears%20deep%20in%20stack%3F%22%20-%3E%20%22Can%20trace%20backwards%3F%22%20%5Blabel%3D%22yes%22%5D%3B%0A%20%20%20%20%22Can%20trace%20backwards%3F%22%20-%3E%20%22Trace%20to%20original%20trigger%22%20%5Blabel%3D%22yes%22%5D%3B%0A%20%20%20%20%22Can%20trace%20backwards%3F%22%20-%3E%20%22Fix%20at%20symptom%20point%22%20%5Blabel%3D%22no%20-%20dead%20end%22%5D%3B%0A%20%20%20%20%22Trace%20to%20original%20trigger%22%20-%3E%20%22BETTER%3A%20Also%20add%20defense-in-depth%22%3B%0A%7D):

![Image 1: The above DOT rendered as an image](https://static.simonwillison.net/static/2025/jesse-dot.jpg)

There is _so much_ to learn about putting these tools to work in the most effective way possible. Jesse is way ahead of the curve, so it's absolutely worth spending some time exploring what he's shared so far.

And if you're worried about filling up your context with a bunch of extra stuff, here's [a reassuring note from Jesse](https://bsky.app/profile/s.ly/post/3m2srmkergc2p):

> The core of it is VERY token light. It pulls in one doc of fewer than 2k tokens. As it needs bits of the process, it runs a shell script to search for them. The long end to end chat for the planning and implementation process for that todo list app was 100k tokens.
> 
> 
> It uses subagents to manage token-heavy stuff, including all the actual implementation.

(Jesse's post also tipped me off about Claude's `/mnt/skills/public` folder, see [my notes here](https://simonwillison.net/2025/Oct/10/claude-skills/).)