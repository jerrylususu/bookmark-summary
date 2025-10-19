Title: What have we learned about building agentic AI tools?

URL Source: https://www.seangoedecke.com/ideas-in-agentic-ai-tooling/

Markdown Content:
In the middle of 2025, agentic coding finally became a thing: first with the release of Claude Sonnet 4, the first “smart enough to be useful” agentic model, and then with OpenAI’s GPT-5-Codex, which is for my money the best-in-class agentic model. “Agent mode” is now the main way to interact with your preferred AI coding tool (whether that’s Claude Code, Codex, Copilot, or Cursor)[1](https://www.seangoedecke.com/ideas-in-agentic-ai-tooling/#fn-1).

Obviously, much of this improvement is the result of better models. Sonnet 4 and Codex simply get lost less often and make fewer mistakes than their predecessors. But we’ve also seen a ton of improvements to the agentic _harness_: the code that wraps the LLM in a loop with tools.

For an interesting time capsule, you can read my 2023 post [_Building LLM-driven agents_](https://www.seangoedecke.com/llm-driven-agents), where I wrote about my attempts to build an agentic coding system on top of GPT-3 (!). This was before tool calls existed - I had to prompt the model to include structured tool call content in its output and then parse that out. In hindsight, I was right about a few important things:

*   LLM agentic coding could actually work
*   If you build a good agentic coding tool, it’s only going to get more useful as better models come out
*   You should tune your tool to a specific model instead of expecting one tool to work well across all models
*   Most importantly, building an agentic coding tool is _normal software engineering_: you can make it more useful by investing more time into polishing and improving it

So what have we learned about building agentic coding tools since then?

**Agents should plan, then act.** Instead of just saying “here are your tools, go solve this problem”, you should set up your coding tool (via some combination of specific tools and prompting) to begin by making an explicit plan. In fact, your tool should check items off the plan as it goes. This goes a long way towards maintaining coherence and preventing the chain-of-thought from going off the rails. It’s often a good idea to have a more powerful model make the plan and then a cheaper-but-faster model handle the execution.

**Users should be able to plug their own tools in.** The canonical version of this is [MCP](https://www.seangoedecke.com/model-context-protocol), but any kind of tools marketplace or plugin system will do. The point is that there’s a lot of mileage in letting users connect, say, their Slack or Jira instance to your coding agent. However:

**Don’t give the agent too many tools.** Agents work best when they’ve got a short-but-sweet set of tools to work with. Too many tools can use too much of the context window and end up confusing the model. In fact, the current trend is to go extremely minimal, with something like an “execute shell command” tool and a “make a patch edit to a file” tool[2](https://www.seangoedecke.com/ideas-in-agentic-ai-tooling/#fn-2). Any strong LLM can already use a command line to list and read files, make HTTP requests, and so on - if it’s in the training data, you don’t need to take up valuable context space for it.

**Use nested per-chat rule files.** One advantage of agentic tooling is that it’s _extremely_ customizable via natural language instructions. All current AI coding tools take advantage of this, whether via a CLAUDE.md file or a more generic AGENTS.md file. In fact, tools now support nesting these files, so you can have a global AGENTS.md in your home directory with general rules, and one in your repo with repo-specific rules, and one in the `/auth` folder with rules that just pertain to your auth code, and so on. The tool will automatically handle loading the right combination of these files into the context as the agent navigates between folders.

**Make it easy for the user to steer an agent mid-flight.** If your agent is spinning away and you see it doing something wrong or surprising, the user should have a way to interrupt and point the agent in a new direction. Claude Code does this automatically when you send a message, while Codex makes you hit escape to pause the agent’s chain-of-thought first. I think either way works fine - the point is that agents need some way to recover from taking a wrong turn[3](https://www.seangoedecke.com/ideas-in-agentic-ai-tooling/#fn-3).

**Make it possible for the user to queue up new commands.** Codex does this when you send new messages. Claude Code doesn’t let you do this, and I think it’s a big mistake. Agents are now good enough to be trusted with small changes, so users should be able to say “when you’re finished, make this tweak” as many times as they want. Queued commands are also useful when you want to force the agent to run for a long time. For instance, when I was trying out Codex on my “five minute LLM” [challenge](https://www.seangoedecke.com/ai-research-with-codex), sometimes I would just queue up ten “Good, please continue” messages if I had to step away for an hour[4](https://www.seangoedecke.com/ideas-in-agentic-ai-tooling/#fn-4).

**Support slash commands.** Users are going to interact with your agentic coding tool _by typing_: at first a description of what they want done, and then various “no, do it like this” or “yes, go on” messages. Agentic tools should thus expose extra functionality as slash commands that the user can type (e.g. to switch model, or to submit a PR, or whatever).

**Use normal search tooling, not RAG.** In the early days of agents, it looked like RAG - chunking a codebase and generating an embedding for each chunk, then using some kind of numerical similarity to identify relevant chunks of the codebase - was going to be the best solution for navigating large codebases[5](https://www.seangoedecke.com/ideas-in-agentic-ai-tooling/#fn-5). But that turned out to be dead wrong. Current AI coding tools just let the LLM do string search, which is much more effective (and much easier for the user, since it doesn’t require an slow “embed the entire codebase” step before the agent can start working).

We are still really early to the world of agentic AI software. There are almost certainly other basic design elements yet to be discovered. Maybe we’ll end up with specialized codebase-searching models like Windsurf’s [SWE-grep](https://cognition.ai/blog/swe-grep). Right now there’s a fairly even split between in-editor tooling and CLI tooling, but eventually one of those might win. I think sub-agents are mostly fluff, but I could be wrong. Better models might still change the game (for instance, by making it more appealing to run an agentic flow without supervision). I personally am missing a “dump your current goal and context into a prompt that I can then paste into a different tool” workflow.

What other obvious-in-hindsight ideas are we missing?

* * *

1.   Or other tools that don’t start with “c”.

[↩](https://www.seangoedecke.com/ideas-in-agentic-ai-tooling/#fnref-1)
2.   I want to register a prediction that somebody will eventually build a for-LLMs CLI tool that makes sensible patch edits to files, and once that tool gets represented in the training data agents will just use bash commands only.

[↩](https://www.seangoedecke.com/ideas-in-agentic-ai-tooling/#fnref-2)
3.   In 2023, I thought that this would require deleting the wrong turn from the agent’s context. Today, I know I was wrong about that: smarter models actually perform better if you leave the mistake in.

[↩](https://www.seangoedecke.com/ideas-in-agentic-ai-tooling/#fnref-3)
4.   I wouldn’t do this on an actual codebase (even a hobby project) but it’s a good option for when you’re giving an agentic tool an easily-verifiable research task.

[↩](https://www.seangoedecke.com/ideas-in-agentic-ai-tooling/#fnref-4)
5.   In my 2023 experiments, embedding and chunking was way better than just letting the model search. I guess newer models are better at searching.

[↩](https://www.seangoedecke.com/ideas-in-agentic-ai-tooling/#fnref-5)

If you liked this post, consider [subscribing](https://buttondown.com/seangoedecke) to email updates about my new posts, or [sharing it on Hacker News](https://news.ycombinator.com/submitlink?u=https://www.seangoedecke.com/ideas-in-agentic-ai-tooling/&t=What%20have%20we%20learned%20about%20building%20agentic%20AI%20tools?).

October 19, 2025│ Tags: [ai](https://www.seangoedecke.com/tags/ai/)

* * *