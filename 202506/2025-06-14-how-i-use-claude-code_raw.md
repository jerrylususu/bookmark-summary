Title: How I Use Claude Code

URL Source: https://spiess.dev/blog/how-i-use-claude-code

Markdown Content:
One month ago, I subscribed to Claude Max. I've been using AI agents including Claude Code for some time prior, but with the flat pricing, my usage skyrocketed and it's become a daily driver for many tasks. I find myself going to VS Code much less often now.

Since AI agents are new for everyone right now, I thought it might be fun to share some patterns I've been noticing recently. Here's how I use Claude code.

[#](https://spiess.dev/blog/how-i-use-claude-code#start-new-threads)Start New Threads
-------------------------------------------------------------------------------------

If there's one thing I want you to take away from this, it's that you should absolutely call `/clear` more often.

AI agents tend to become more unpredictable the longer a conversation goes. This is especially true when you're asking different questions. I found that it's often much more effective to create a new prompt even if that means repeating some instructions.

Once I started doing this more aggressively, my results improved dramatically. And [I'm definitely not the only one](https://ampcode.com/how-i-use-amp) with this advice.

[#](https://spiess.dev/blog/how-i-use-claude-code#create-precise-prompts)Create Precise Prompts
-----------------------------------------------------------------------------------------------

I feel like this goes without saying, but when you're working with _a new grad with amnesia_ (that's how I like to think of Claude), it's important that you write out all the context that you have in your head. This is hard, and frankly I don't think I'm very good at it myself yet, but the more context you can give Claude, the more effective it'll be. If you're thinking of some edge-cases, absolutely mention it to Claude. If you remember "there's a similar pattern that we've used for this type of problem in this codebase in the past", write it down! The more precise the prompt, the better Claude will do. Mind-reading technology isn't there _just yet_.

Try to think of any implicit context too. For example, if you ask Claude to create a _modern design_, it probably has no idea what you refer to as modern. It might be better to give examples instead (e.g., create a Linear-like app UI design).

[#](https://spiess.dev/blog/how-i-use-claude-code#let-claude-code-use-claude-code)Let Claude Code Use Claude Code
-----------------------------------------------------------------------------------------------------------------

Did you know that you can use Claude Code's tools as an MCP server (`claude mcp serve`)? When I found out, I looked into what tools it exposes and noticed one called `Task`. The premise of this tool is to spin off a sub-agent that will have the same access to tools as your main agent (except that it cannot spawn another sub-task) and reports back the results.

Knowing this is available is super handy when you have a more complex problem that you need a supervisor for. Here's a recent example of how I used this feature to do a deep-dive of the same problem with four different personas:

```
> Read files in the current directory to deduct a pattern for building Tailwind Plus components. You should spawn 4 sub-tasks with slightly different priorities (e.g. design color export, accessibility export, mobile/responsive expert, overall style expert) and compare their results.

✻ Thinking…

  Now I'll spawn 4 specialized sub-tasks with different priorities to analyze various aspects of the components.

⏺ Task(Design Color Expert Analysis)
  ⎿  Done (24 tool uses · 41.5k tokens · 3m 4.4s)

⏺ Task(Accessibility Expert Analysis)
  ⎿  Done (15 tool uses · 38.0k tokens · 2m 0.0s)

⏺ Task(Mobile/Responsive Expert Analysis)
  ⎿  Done (14 tool uses · 45.5k tokens · 2m 1.2s)

⏺ Task(Overall Style Expert Analysis)
  ⎿  Done (23 tool uses · 58.7k tokens · 2m 22.0s)
```

It's magnificent _and_ can be done in parallel. This is such a good way to keep the context window of your main task in order and keep Claude focused.

[#](https://spiess.dev/blog/how-i-use-claude-code#tell-claude-to-think)Tell Claude to Think
-------------------------------------------------------------------------------------------

Just like us old humans of flesh, Claude is lazy by default. E.g., when you tell Claude to do something, it'll choose the path of least resistance. If you tell it to do _at least_ three things, I bet you it will not do a single thing more.

The same holds true about using [extended thinking capabilities](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/extended-thinking-tips). To get better results, especially during planning processes, I recommend telling Claude to _ultrathink_.

[#](https://spiess.dev/blog/how-i-use-claude-code#edit-previous-messages)Edit Previous Messages
-----------------------------------------------------------------------------------------------

Whenever you're too eager to hit send or just feel like a previous message could be more precise to get better results, you can press Escape twice to jump to a previous message and fork the conversation. I use this all the time to refine prompts or simply have Claude _try again_.

Oh, and if you somehow want to get back to the previous state, you can start Claude with the `--resume` flag to list all prior threads.

[#](https://spiess.dev/blog/how-i-use-claude-code#yolo-mode)Yolo Mode
---------------------------------------------------------------------

This is probably extremely irresponsible of me, but I mostly run Claude with `--dangerously-skip-permissions` now (thanks [Peter](https://steipete.me/posts/2025/claude-code-is-my-computer) for being a bad influence). It's not necessary for everything, but if I have Claude working on some longer-running tasks, I _really_ don't want to have to focus-switch back to it every minute because it uses a new terminal command.

I have this set up in my zsh profile:

`alias yolo="claude --dangerously-skip-permissions"`
Funny enough, now that Claude can do whatever it wants, I have been running against the rate limit quota warning much more often too.

[#](https://spiess.dev/blog/how-i-use-claude-code#mcp-servers)MCP Servers
-------------------------------------------------------------------------

I'm personally not super excited about MCP servers since none have really brought me any value. In most cases, I find they just use up valuable tokens with stuff that I don't need most of the time. The built-in tools in Claude Code are enough for me (especially when used to the ways I outline here).

In the past, I used [Playwright MCP](https://github.com/microsoft/playwright-mcp). While it's incredibly fascinating to see Claude start a browser, click buttons, and make screenshots, I found that it mostly just fills the context window very quickly without really making for a better result.

[#](https://spiess.dev/blog/how-i-use-claude-code#claude-sdk)Claude SDK
-----------------------------------------------------------------------

Claude has an [SDK](https://docs.anthropic.com/en/docs/claude-code/sdk). It's quite powerful, especially if you're happy to deal with the `stream-json` output format. But even for small things, being able to pass a prompt directly to `claude` and have it print back the reply is making for great shortcuts.

As an example, I have a `gcauto` executable in my path that does the following:

```
#!/bin/bash
git commit -m "$(claude -p "Look at the staged git changes and create a summarizing git commit title. Only respond with the title and no affirmation.")"
```

So whenever I commit stuff now, I just stage them and run `gcauto`.

[#](https://spiess.dev/blog/how-i-use-claude-code#planning-mode)Planning Mode
-----------------------------------------------------------------------------

Claude Code has a built-in planning mode, that is triggered when you press Shift+Tab twice. In this mode, Claude won't write to your file system.

I personally like to do planning with another model though, just to spice it up a bit. In the past weeks, I've been using Gemini 2.5 Pro in [Google AI Studio](https://aistudio.google.com/) directly. I don't really know how that's possible but I don't think I have to pay for it even?

[#](https://spiess.dev/blog/how-i-use-claude-code#let-claude-rtfm)Let Claude RTFM
---------------------------------------------------------------------------------

A rookie mistake I've made in the beginning is to tell Claude to set up a new project with _framework x_. It works, sure, but I noticed Claude often using outdated setups and project structures, especially for fast-moving frontend frameworks!

What I do now is ask Claude to read the manual first. This can be done in different ways:

*   Paste a link to the docs and ask Claude to read it first
*   Ask Claude to find out the state-of-the-art
*   Use the `Task` tool and have Claude conduct deep-research on a particular topic

An example for a deep research task can look like this:

```
> create a deep research task to figure out how to migrate a website from tailwind 3 to 4 and then present me with a
  short summary of the results

⏺ I'll create a research task to investigate migrating from Tailwind CSS v3 to v4, focusing on the specific context of
  your Tailwind UI codebase.

⏺ Task(Tailwind v3 to v4 migration research)
  ⎿  Done (4 tool uses · 29.9k tokens · 5m 47.6s)

⏺ Summary

  Migrating from Tailwind CSS v3 to v4 involves significant changes but comes with major performance improvements (3.5x
   faster builds) and a better developer experience.

  Key points:
  - Use the automated upgrade tool: npx @tailwindcss/upgrade@next
  - Configuration moves from JavaScript to CSS-first using @theme directive
  - Breaking changes include dropped browser support, new import syntax, and removed deprecated utilities
  - Performance gains: builds are now measured in microseconds
  - Container queries are now built-in (no plugin needed)

  The migration is straightforward with the upgrade tool, but plan for testing time to ensure all components render correctly.
```

[#](https://spiess.dev/blog/how-i-use-claude-code#voice-input)Voice Input
-------------------------------------------------------------------------

Apps like [Superwhisper](https://superwhisper.com/) make it very easy to dictate a prompt. I found this super effective when I want to write a longer prompt since it'll get the ideas out of my head much faster.

This works incredibly well with any LLM input field, really, because LLMs can usually figure out what you mean even if the transcript is poor and full of mistakes.

[#](https://spiess.dev/blog/how-i-use-claude-code#stage-early-stage-often)Stage Early, Stage Often
--------------------------------------------------------------------------------------------------

One feature I'm missing in Claude Code is the ability to make automatic file system snapshots. It happens quite often for me that Claude gets a bit too _trigger happy_ and starts to make large changes when I don't want it to. If this happens after I've been getting some good changes, this can screw up the working directory quite a bit.

To circumvent this, I started to stage (i.e. `git add`) changes early and often. If I'm happy after a turn, I'm usually going to stage everything just so I know I can easily revert to it later.

[#](https://spiess.dev/blog/how-i-use-claude-code#git-worktrees)Git Worktrees
-----------------------------------------------------------------------------

I am so obsessed by Claude Code that I now have at least two working trees of every major project I work on on my machine. This allows me to have Claude running on two different problems _in the same repository_.

It's very easy to set up, too! It's like creating a branch but the code will be in a different directory. Inside your git repository, run:

`git worktree add ../tailwindcss.com-2 chore/upgrade-next`
And, voila, you now have another working directory for Claude Code to go absolutely feral in.

[#](https://spiess.dev/blog/how-i-use-claude-code#experiment-with-one-off-work)Experiment with One-Off Work
-----------------------------------------------------------------------------------------------------------

With AI, code is becoming _really cheap_. This means that you can now build stuff that you only ever use once without feeling bad about it. Everything that you wish would make your current task easier can just be created out of thin air. Here are some examples of things I built recently that would never have been worth my time before coding agents:

*   A dashboard that visualizes my current progress during a large migration at work
*   A chrome extension that shows me which version of Tailwind CSS a website is using (or, god-forbid, wether it isn't using Tailwind CSS at all)
*   A [CLI and backend](https://github.com/philipp-spiess/claude-code-viewer) to upload Claude Code transcripts to be shared publicly
*   A [CLI to sum up my Claude Code API costs](https://github.com/philipp-spiess/claude-code-costs) to see how much value I get out of the Max plan (oh so much...)
*   An [Electron app that experiments with Claude Code inside a git GUI](https://github.com/philipp-spiess/claude-code-app)

[#](https://spiess.dev/blog/how-i-use-claude-code#if-possible-dont-attempt-to-one-shot)If Possible, Don't Attempt to One-Shot
-----------------------------------------------------------------------------------------------------------------------------

I'm currently focused on a large-scale change that requires me to touch many Tailwind Plus components in the process. My naive first idea was to create an amazing, thought-out prompt with a lot of detail that can surely make the AI do all of this in one go... That surely must be possible, right?

Well, spoiler alert but I failed miserably with this approach. Not only did it not do what I wanted it to do in the first place, it also made it impossible for me to review the changes or make any meaningful changes. I had to start fresh.

This time I asked Claude Code questions about the problems first. We discussed possible changes before writing any code. Only when I felt certain it knew what I wanted, I let it change one component. After some testing and feedback, I let it do two more. Then another five until I finally let it fan out and do the remainder of the work.

While this obviously wasn't as spectacular as creating the perfect prompt, it got me to the end result much faster and with tighter feedback loops and supervision. I still was able to save so much time compared to doing this change by hand across hundreds of different components.

This might very well be an issue of me _holding it wrong_. I've been seeing a lot of other people claiming to be successful with large one-shot tasks (some of which say that Claude is working for _hours_ straight). However, in my own experience, errors compound quickly and LLMs often loose the thread with a growing context window (and that was with extensive sub-agent calls and even trying Gemini 2.5 Pro). I would love it if someone could share their secrets with me!

[#](https://spiess.dev/blog/how-i-use-claude-code#autonomous-feedback-or-human-in-the-loop)Autonomous Feedback or Human in the Loop?
------------------------------------------------------------------------------------------------------------------------------------

Related to the issue above, this is also an area I still struggle with. Whenever I see people praising AI agents, they mention the importance of some autonomous feedback cycles so that the LLM can improve the result on their own.

However, I have not been able to do this effectively yet. When I try to set up unit tests or linter feedback, Claude _will read it and then suggest everything is working just fine when there still many are issues/warnings left_. When I set it up so it can navigate to the page and make screenshots, the context window is quickly full with tokens. Safe to say that the experience hasn't been great for me.

What I like to do instead is just have the dev server running myself. Whenever Claude gets back to me, I take a look at it myself and either copy paste any eventual stack traces as-is, or give some hints as to what I want done differently. I personally find this approach is far more likely to get me to what I want.

[#](https://spiess.dev/blog/how-i-use-claude-code#interrupt-early-interrupt-often)Interrupt Early, Interrupt Often
------------------------------------------------------------------------------------------------------------------

Whenever I see something going wrong, I usually press Escape to interrupt Claude right away and ask it to revert the latest changes and then guide it more to the direction I want. Of course this only works when you're keeping an eye which I frankly often don't do.

[#](https://spiess.dev/blog/how-i-use-claude-code#configure-your-terminal)Configure Your Terminal
-------------------------------------------------------------------------------------------------

Claude Code has a hidden `/terminal-setup` command that will look at your current terminal setup and make some changes like making it possible to use Shift+Enter to add newlines or register the right bell type. While I wasn't able to figure out the newline thing with Warp, my terminal now beeps whenever Claude needs some human input again.

[#](https://spiess.dev/blog/how-i-use-claude-code#connect-your-ide)Connect Your IDE
-----------------------------------------------------------------------------------

Another relatively new feature is that you can connect Claude to see what files you have open in your IDE and read linter warnings, etc. This is set up either when you run `claude` from within your IDE's terminal, or by running the `/ide` command. This is handy if you want to tell Claude to "fix my linter issues."

[#](https://spiess.dev/blog/how-i-use-claude-code#custom-commands)Custom Commands
---------------------------------------------------------------------------------

You can create [custom slash commands](https://docs.anthropic.com/en/docs/claude-code/tutorials#create-custom-slash-commands) in Claude Code. If you find yourself writing a similar prompt more than once, this might be your chance to save even more time.

I have something set up to clean up temporary scripts or helper files that Claude is very eager to create, for better or worse.

[#](https://spiess.dev/blog/how-i-use-claude-code#paste-images-into-claude)Paste Images into Claude
---------------------------------------------------------------------------------------------------

You can paste in images into Claude Code. Just copy the image directly or drag a file into your Terminal, and it'll be added as an attachment to your next message. I use this sometimes when i want to make small visual changes.

[#](https://spiess.dev/blog/how-i-use-claude-code#conclusion)Conclusion
-----------------------------------------------------------------------

Claude Code has fundamentally changed how I approach many programming tasks. While it's not perfect and requires adapting your workflow, the productivity gains are real. The key is finding the right balance between automation and human oversight, and being willing to experiment with different approaches.

As AI coding assistants continue to evolve, I expect many of these patterns will change. But for now, these techniques have made my daily coding life significantly more productive and, dare I say, more fun.
