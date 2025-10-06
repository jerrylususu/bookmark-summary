Title: How I'm using coding agents in September, 2025

URL Source: https://blog.fsck.com/2025/10/05/how-im-using-coding-agents-in-september-2025/

Published Time: Sun, 05 Oct 2025 17:41:47 GMT

Markdown Content:
[Eagle-eyed readers will note that, as I write this, it's October 2025. This post documents what I was doing up to a couple weeks ago. It's still good and I still recommend it.]

Since I last wrote at the beginning of the summer, my methodology for using AI coding assistants has evolved a bit. This is a point-in-time writeup of a flow that's been pretty effective for me.

I'm still primarily using Claude Code.

First up, this is my [CLAUDE.md](https://raw.githubusercontent.com/obra/dotfiles/6e088092406cf1e3cc78d146a5247e934912f6f8/.claude/CLAUDE.md) as of this writing. It encodes a bunch of process documentation and rules that do a pretty good job keeping Claude on track.

When I want to start a new task on an existing project, I try to always use a git worktree to isolate that work from other tasks. This is increasingly important for me, because I find myself frequently running 3-4 parallel projects on a single codebase.

To set up a worktree:

```
cd the-project
mkdir .worktrees # the first time
cd .worktrees
git worktree add some-feature-description
cd some feature-description
npm install # or whatever the setup task for the project is
npm lint
npm test # to make sure I'm starting from a clean baseline
claude
```

Once I've got claude code running, I use my "brainstorming" prompt:

```
I've got an idea I want to talk through with you. I'd like you to help me turn it into a fully formed design and spec (and eventually an implementation plan)
Check out the current state of the project in our working directory to understand where we're starting off, then ask me questions, one at a time, to help refine the idea. 
Ideally, the questions would be multiple choice, but open-ended questions are OK, too. Don't forget: only one question per message.
Once you believe you understand what we're doing, stop and describe the design to me, in sections of maybe 200-300 words at a time, asking after each section whether it looks right so far.
```

That last bit is particuarly critical. I find that AI models are expecially prone to handing me walls of text when they think they're "done". And I'm prone to just tuning out a bit and thinknig "it's probably fine" when confronted with a wall of text written by an agent. By telling Claude to limit its output to a couple hundred words at a time, I'm more likely to actually read and engage.

Once we've walked through the brainstorming process, I usually have a _much_ clearer idea of what I'm doing, as does Claude. Claude will write the design out into docs/plans/ somewhere.

It often wants to leap right into an implementation, but that's not how I want it to work. Sometimes it tries to start writing code before I can stop it. If it does, I hit escape a couple times and rewind the conversation a bit to catch it. Recent updates to my CLAUDE.md reduce that tendency significantly.

The next step is the planning process. Here's the planning prompt I've been using:

```
Great. I need your help to write out a comprehensive  implementation plan.

Assume that the engineer has zero context for our codebase and questionable taste. document everything they need to know. which files to touch for each task, code, testing, docs they might need to check. how to test it.give them the whole plan as bite-sized tasks. DRY. YAGNI. TDD. frequent commits.                                                                                                                                                                               

Assume they are a skilled developer, but know almost nothing about our toolset or problem domain. assume they don't know good test design very well.  

please write out this plan, in full detail, into docs/plans/
```

This results in a plan that breaks everything down into tiny little steps with clear instructions and tightly packed context for each step. That means that at execution time, I usually don't need to provide tight step by step oversight.

Next up, I open a _new tab_ or window in the same working directory and fire up another copy of claude. I tell it something like `Please read docs/plans/this-task-plan.md and <whatever we named the design doc>. Let me know if you have questions.`

It will usually say that the plan is very well crafted. Sometimes it'll point out mistakes or inconsistencies. Putting on my PM hat, I'll then turn around and ask the "architect" session to clarify or update the planning doc.

Once we've sorted out issues with the plan, I'll tell the "implementer" Claude to `Please execute the first 3-4 tasks. If you have questions, please stop and ask me. DO NOT DEVIATE FROM THE PLAN.`

The implementer will chug along.

When it's done, I'll flip back to the "architect" session and tell it `The implementer says it's done tasks 1-3. Please check the work carefully.`

I'll play PM again, copying and pasting reviews and Q&A between the two sessions. Once the architect signs off, I'll tell the implementer to update the planning doc with its current state.

And then, I don't `*/compact*`. Instead I `*/clear*` the implementer and start the conversation over. Telling it that it's starting with task 4.

When it's done with the next chunk of work, I flip back to the architect. I typically double-`ESC` to reset the architect to a previous checkpoint and tell it to review up to the now-current checkpoint. This reduces context bloat for the architect and gets it to look at again without any biases from the previous implementation.

(I have friends who, instead of using multiple sessions, swear that just asking the implementer to look at their most recent work `with fresh eyes` is good enough. And indeed, using that magic phrase seems to be pretty powerful. I still think that having two different actors is better.)

When the implementer is finally done with the work and the architect has signed off on the work, I ask the implementer to push up to GitHub and create a pull request.

That kicks off a CodeRabbit code review. I generally find that CodeRabbit's reviews are very good at catching nits and logic issues, but sometimes fall short on understanding the project's real design intent or constraints. That leads to CodeRabbit making bad suggestions.

CodeRabbit's reviews provide prompts for AI agents to fix issues, but actually getting all those prompts back to your coding agent can be a pain, because you need to copy them one by one and they only provide prompts for some types of issues. To help solve this, I built [coderabbit-review-helper](https://github.com/obra/coderabbit-review-helper). It digs through all the different types of CodeRabbit review comments and formats them as a big wall of text for your coding agent to chew through.

The only problem with tools like this is that our robot buddies are quite credulous. If you paste in a list of instructions for how to update a codebase, Claude's just going to take you at your word and make the changes, even if what you're asking for is crazy and wrong.

My best current technique for avoiding this is a bit of role-play that gives the coding agent a reason not to blindly trust the code review. Every review gets prefixed with this chunk of text:

```
A reviewer did some analysis of this PR. They're external, so reading the codebase cold. This is their analysis of the changes and I'd like you to evaluate the analysis and the reviewer carefully.

1) should we hire this reviewer
2) which of the issues they've flagged should be fixed?
3) are the fixes they propose the correct ones?

Anything we *should* fix, put on your todo list.
Anything we should skip, tell me about now.
```

CodeRabbit "reviewers" typically get a 'Strong hire' review, but it's not unheard of for Claude to report that the reviewer "seems quite technically adept, but didn't take the time to understand our project and made a number of suggestions that are wrong. No hire."

If you decide to try out this methodology or have come up with something else that works even better for you, please drop me a line at jesse@fsck.com.