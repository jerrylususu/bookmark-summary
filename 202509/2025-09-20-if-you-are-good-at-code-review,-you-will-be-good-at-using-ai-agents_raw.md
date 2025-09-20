Title: If you are good at code review, you will be good at using AI agents

URL Source: https://www.seangoedecke.com/ai-agents-and-code-review/

Markdown Content:
Using AI agents correctly is a process of _reviewing code_. If you’re good at reviewing code, you’ll be good at using tools like Claude Code, Codex, or the Copilot coding agent.

Why is that? Large language models are good at producing a lot of code, but they don’t yet have the depth of judgement of a competent software engineer. Left unsupervised, they will spend a lot of time committing to bad design decisions.

### AI agents and bad design

Last week I built [VicFlora Offline](https://github.com/sgoedecke/vicflora-offline): an offline-friendly PWA that hosts some of the VicFlora data for keying out plants, so you can still use the keys if you’re in the field somewhere with bad internet reception. Codex spent a _lot_ of effort trying to reverse-engineer the VicFlora frontend code for the [dichotomous key](https://simple.wikipedia.org/wiki/Dichotomous_key). It was honestly pretty impressive to watch! But I figured there had to be some easier way to access the raw data, and [I was right](https://keybase.rbg.vic.gov.au/projects/show/10). This happens over and over again when I use AI coding agents: about once an hour I notice that the agent is doing something that looks suspicious, and when I dig deeper I’m able to set it on the right track and save hours of wasted effort.

I’m also working on an app that helps me learn things with AI - think of it as an infinite, automatically-adjusting spaced-repetition feed. When I want to do things in parallel (e.g. generating a learning plan in the background), both Codex and Claude Code really want to build a full background job infrastructure: with job entities, result polling, and so on. I like background jobs, but for ordinary short-lived parallel work they are very obviously overkill. Just make a non-blocking request from the frontend! If I weren’t consistently pushing for simplicity, my codebase would be much more complex to reason about.

Incidentally, this is why I think pure “vibe coding” hasn’t produced an explosion of useful apps. If you don’t have the technical ability to spot when the LLM is going down the wrong track, you’ll rapidly end up stuck. Trying to make a badly-designed solution work costs time, tokens, and codebase complexity. All of these things cut into the agent’s ability to actually solve the problem. Once two or three of them pile up, the app is no longer tractable for the agent and the whole thing grinds to a halt.

### Code review

These examples should be familiar to anyone who’s spent enough time working on an engineering team with enthusiastic juniors. Diving right in to an early idea and making it work with sheer effort is a very common mistake. It’s the job of the rest of the team to rein that in. Working with AI agents is like working with enthusiastic juniors who never develop the judgement over time that a real human would[1](https://www.seangoedecke.com/ai-agents-and-code-review/#fn-1).

This is a good opportunity to talk about what I think is the biggest mistake engineers make in code review: **only thinking about the code that was written, not the code that _could have been_ written**. I’ve seen even experienced engineers give code reviews that go through the diff with a fine-toothed comb, while spending approximately zero seconds asking if this is even the right place for the code at all.

In my view, the best code review is _structural_. It brings in context from parts of the codebase that the diff didn’t mention. Ideally, that context makes the diff shorter and more elegant: for instance, instead of building out a new system for operation X, we can reuse a system that already exists. Instead of building a fragile scraping pipeline that pulls dichotomous key IDs from the frontend SPA code, let’s just download the dichotomous keys from this other place where they’re explicitly made available. Instead of building out an entire background job system, let’s just do our parallel work on the client, using all the existing machinery that websites have for doing two things at the same time.

If you’re a nitpicky code reviewer, I think you will struggle to use AI tooling effectively. You’ll be forever tweaking individual lines of code, asking for a `.reduce` instead of a `.map.filter`, bikeshedding function names, and so on. At the same time, you’ll miss the opportunity to guide the AI away from architectural dead ends.

Likewise, if you’re a rubber-stamp code reviewer, you’re probably going to put too much trust in the AI tooling. That approach works with competent colleagues, but it doesn’t work well when you’re onboarding junior engineers, and it doesn’t work well when you’re working with AI coding agents.

### Final thoughts

What does it mean to be “good at AI”? Being good at a normal tool like git is straightforward: if you have a grasp of the basic tree-structure of a git repository, and you’re familiar with the majority of git operations, you’re good at git. But the basic structure of AI is an impenetrable mass of model weights, and the “operations” it can perform are “basically anything you can do with a computer”. There are no software engineering tools like it.

The most optimistic AI proponents think that “being good at AI” is about maximally adopting AI tooling in every aspect of your life. The argument here is that AI plays something like the role of Jeff Bezos’ staff. Using a hyper-resourced, hyper-competent staff doesn’t require a lot of _skill_: you simply ask for what you want, and an enormous amount of other people’s effort will be devoted to providing it. But Bezos certainly uses his staff more effectively than I would, if I were to be teleported into his position today. I wouldn’t even consider asking for half the things I wanted - it just wouldn’t occur to me that I could get a hot [Lune croissant](https://lunecroissanterie.com/) waiting for me when I step off my private jet, for instance, even if I really would enjoy it. AI believers think AI tooling is kind of like this. According to them, when you genuinely internalize that you can ask your personal AI assistant to vibe code any program you want, or sort through any amount of data, or draft all of your emails, you will begin using AI much more frequently, to your benefit.

I don’t think we’re there yet. I use agentic coding tools a lot: GitHub Copilot at and for work, and both Codex and Claude Code for my personal projects[2](https://www.seangoedecke.com/ai-agents-and-code-review/#fn-2). While they can do a surprising number of tasks on their own, they do require fairly close supervision. The dominant programming model is something like [“centaur chess”](https://en.wikipedia.org/wiki/Advanced_chess), where a skilled human is paired with a computer assistant. The better you are at code review - at assessing whether a particular software approach is a sensible one - the better you’ll be at using agentic AI tooling.

* * *

1.   Every time I see this point made, I wonder - if you started using AI coding tooling with early Copilot in 2022, and you’re still using cutting-edge AI tooling in 2025, doesn’t it kind of feel like the tooling has grown at the same rate a human would? If you described early Copilot as a brand-new grad and current Claude Code (or whatever) as an engineer with three years of experience, would that be too far off? In another three years, will working with AI tooling be like working with a engineer with six years under their belt?

[↩](https://www.seangoedecke.com/ai-agents-and-code-review/#fnref-1)
2.   Using Codex and Claude Code doesn’t indicate that I think they’re better than Copilot. In my view, it’s part of my job to use a variety of AI tooling.

[↩](https://www.seangoedecke.com/ai-agents-and-code-review/#fnref-2)

If you liked this post, consider [subscribing](https://buttondown.com/seangoedecke) to email updates about my new posts, or [sharing it on Hacker News](https://news.ycombinator.com/submitlink?u=https://www.seangoedecke.com/ai-agents-and-code-review/&t=If%20you%20are%20good%20at%20code%20review,%20you%20will%20be%20good%20at%20using%20AI%20agents).

September 20, 2025│ Tags: [ai](https://www.seangoedecke.com/tags/ai/)

* * *