Title: Nobody Codes Here Anymore

URL Source: https://ghiculescu.substack.com/p/nobody-codes-here-anymore

Published Time: 2025-04-29T06:48:17+00:00

Markdown Content:
There is plenty of commentary online about how AI will replace coding as we know it in the future. There’s huge amounts of prediction about what the future holds.[1](https://ghiculescu.substack.com/p/nobody-codes-here-anymore#footnote-1-162309066) But I haven’t come across many case studies of rolling out the tools that exist today. So here’s some observations.

For context: SaaS product. Ruby on Rails. Mature (12 years) codebase, in good condition. About 40 developers.

We’ve given every developer the option to buy [Cursor](https://www.cursor.com/en) or [Claude Code](https://www.anthropic.com/solutions/coding). (I’ll refer to these as Agents for the rest of this article.) If someone wanted to buy another agentic tool that isn’t one of those we’d probably say yes if the price was similar. In a recent informal survey I did, 8 people answered yes to “I use Cursor/Claude Code for most (or all) of my coding”, and 11 to “I alternate between using them and not using them based on the task, it averages out to about 50% of the time”.

I use Claude Code and don’t really like Cursor. The main reason for that is I’m obsessed with Sublime Text as my editor. So having to change to another editor is basically a deal breaker for me. Most other people are more sane, and thus Cursor adoption has been slightly higher than Claude.

They also different things. Claude (particularly with the newest models) likes to write entire features for you, and can sometimes get a bit carried away. [Anthropic’s best practices guide](https://www.anthropic.com/engineering/claude-code-best-practices) is a goldmine, and one great suggestion it made that I’ve successfully adopted is asking Claude to make a plan before writing any code, and then telling it to write the code.

By contrast, Cursor (from what I’ve seen) seems to be content making smaller and more self contained changes. It seems less likely to try and write the entire thing and commit it without your consent. Conversely, it seems less capable of doing ambitious one shot prompts.

In the future, a “senior engineer” might be someone who knows the right agent to use for the given task.

It’s the question everyone is asking. And to be honest it’s hard to give a totally objective answer. How did you mention developer productivity before agents?

That said if forced to pick a number I would say I’m about 20% more productive thanks to agents. But there’s a massive grain of salt there. Agents are really helpful for some things, and barely helpful at all for others, so right now it is all about incorporating them into your workflow where it makes sense.

Some people online who are against agentic coding argue that with a junior developer you can teach them stuff and so they gradually improve over time. But the same can’t be said for agents, they are always going to be as smart as they are today, so if they are as good as a junior dev now they’ll always be only that good. Presumably this applies to domain specific stuff, since LLMs already know all the generic stuff in the world. Regardless, it’s nonsense, and is easily disproven by two observations:

1.   Using agents well changes how you structure your codebase in a way that makes them more able to work with it over time, ie. they get smarter.

2.   The quality of LLMs is improving often. The other week ChatGPT added a feature where it remembers everything you’ve ever said to it and incorporates that into context, which sounds a lot to me like a junior picking up domain knowledge and building on it.

So far the biggest limiting factor is remembering to use it. Even people I consider power users (based on their Claude token usage) agree with the sentiment that sometimes you just forget to ask Claude to do a task for you, and end up doing it manually. Sometimes you only notice that Claude could have done it, once you are finished. This happens to me an embarrassing amount.

I suspect this is less of an issue for Cursor users because it’s always there in your editor, while Claude Code lives in your terminal.

We have found agents work really well for increasing the ambition of code that gets written. This can mean a few different things:

*   Our head of product is a reformed lawyer who taught himself to code while working here. He’s shipped 150 PRs in the last 12 months.

*   The product manager he sits next to has shipped 130 PRs in the last 12 months. When we look for easy wins and small tasks for new starters, it’s harder now, because he’s always got an agent chewing through those in the background.

*   We built a new product for a new region with a single developer working solo (with the help of Claude). Previously we did this slower, with teams of people. Those teams are adopting Claude now too, but using it from the start and getting good at using it really helps.

*   I’m sure everyone comes across feature ideas that sound cool but it’s not obvious right now where to start. Like a coding writers block. Turns out typing a prompt is a lot easier than typing the code and it is a great way to unblock and get started on ideas you wouldn’t otherwise try.

Agents are extremely good at helping you understand parts of the codebase you haven’t seen before - just ask them - and I suspect that’s helping a lot here.

A few times now we’ve tried to connect agents to Linear or Sentry to try and get automatic draft PRs for bug fixing. So far the results have been mixed.

All you are really doing here is hoping that the Linear ticket (or context in Sentry issue) is enough that the agent can work out the bug and fix it. In other words you’re hoping the ticket works as well as a one shot prompt that a developer would write. Sometimes this happens, and if it does it’s very impressive.

More often it doesn’t. The issue I’ve found is that in many cases the proposed fix is incorrect, but in a subtle way, where if you don’t know the codebase you’re looking at (or don’t think about it critically enough) you’ll be led astray. It’s easy to see a draft PR with all tests passing, including new tests full of comments, and not realise that the tests are garbage and the fix is wrong. This is less likely to happen if you have taken time to think about the feature & scope beforehand, but much more likely if you see a bug report and a green draft PR ready to go alongside it.

For this reason we have avoided pushing automatic draft PRs.

Claude Code is incredibly good at refactors. Particularly if the refactors involve frontend code.

A recent example was to convert a set of screens built into React into our new design system, that’s built on Hotwire and is all rendered serverside. Using [this prompt](https://gist.github.com/ghiculescu/fa28b988c64e4ca9bc442dbd1d976858) Claude Code came up with an almost right plan. I made a few tweaks and then asked it to write the code, which it did correctly.

It missed a few client side validations that we only found while testing, which is to say that it’s important to still test. I think if I had explicitly asked it to ensure it included all these sorts of validations in my prompt it would have.

Doing the refactor by hand would have taken me a few hours, so realistically using the agent probably saved me an hour. But it would have been boooooring. Knowing how boring it would be, I’d been putting off doing it forever, even though it was something I really wanted to see done. Agents are underrated for quickly getting through chores.

Agents work great at doing straightforward tasks using straightforward parts of well documented frameworks.

You have to be careful with more complex tasks that are below the surface level, where you could get a wide variety of architectures come back and you need to be critical about getting the best one.

For example, I asked an agent to help me ensure that a specific operation could only happen once at any time. I suggested it used locking. It came back with a custom built Redis locking mechanism. After a nudge, it suggested using the Rails cache. After another nudge, a manually executed Postgres advisory lock. After another nudge, it finally settled on Rails’ `with_lock` method. Had I not been thinking critically it would have had me introduce new dependencies to solve a problem where tools to fix it were built into the framework.

Cursor has a [fixed price](https://www.cursor.com/pricing). I suspect they are thinking about pricing the way gyms do: if everyone used Cursor as much as they allow you to, they’d go out of business. But in practice most people use a lot less tokens than they are paying for.

You can see this in practice when you use Claude Code, which is pay-per-token. Our heaviest users are using $50/month of tokens. That’s a lot of tokens.

I asked our CFO and he said he’d be happy to spend $100/dev/month on agents. To get 20% more productive that’s a bargain.

This critique may only make sense to sufficiently [DHH-pilled](https://rubyonrails.org/doctrine) people, but so be it. I haven’t yet come across an agent that can write _beautiful_ code.

That doesn’t mean it can’t write correct code, or (particularly if you prompt it right) succinct code. And it isn’t to say that all code needs to be beautiful. But in some cases the elegance of the code does matter because it says a lot about the elegance - and the quality - of the architecture. Agents still aren’t there in those cases.

The most common thing that makes agentic code ugly is the overuse of comments. I have tried _everything_ I can think of and apart from prefacing every prompt with “Don’t write comments” I cannot find a way to get agents to not comment every line they write.[2](https://ghiculescu.substack.com/p/nobody-codes-here-anymore#footnote-2-162309066)

In the worst case this means rewriting all the code the agent wrote. I still think this is worthwhile. Often writing the prompt and going back and forth will the agent will help you understand the issue better which will lead to you writing your architecture better. And they write code so quickly, it’s not like you’re wasting days before throwing it away and writing it yourself.

A related issue is that if everyone uses agents, individual coding styles are lost. When you’ve worked with someone for a while you can tell if they wrote some code just by reading it. That is lost when everything goes through an agent. I’m sure in 10 years time this will seem quaint, like mourning over the assembly that powers the C code that sits under Ruby. But for now it makes me a little bit sad sometimes.

We’ve done a few things to make the codebase easier for agents to reason with.

*   Setting up [Cursor rules](https://docs.cursor.com/context/rules) and [Claude.md](https://docs.anthropic.com/en/docs/agents-and-tools/claude-code/overview#initialize-your-project). These end up also holding great context for new teammates.

*   Making it easy to run tests with a single command. We used to do development & run tests via docker over ssh. It was a good idea at the time. But fixing a few things so that we could run tests locally meant we could ask the agent to run (and fix!) tests after writing code.

Many companies have issued mandates for using AI, some of which have [leaked](https://x.com/tobi/status/1909251946235437514)[publicly](https://www.capitalbrief.com/article/employment-hero-tracks-employees-in-push-for-ai-first-within-six-weeks-ec8e88ef-9415-4664-8b99-dd1280edf992/preview/).[3](https://ghiculescu.substack.com/p/nobody-codes-here-anymore#footnote-3-162309066)

We haven’t. That doesn’t mean I don’t expect people to try this stuff out, but I think forcing them to do it is silly. If the productivity gains are as significant as I suspect they are, than anyone who has their self interest (or the company’s interests, if they are so inclined) at heart will quickly pick up agentic coding.

It is a very exciting time to be in software development. I’ve written this a few times, but it’s really true, and every time I write it I then get more impressed with the quality of agentic coding.

Similar to being good at writing code, being good at using agents is not a binary thing. There’s a sliding scale of quality. In the future there will be 10x prompters just like today there’s 10x developers.

I think it’s worth trying to get really good at using agents to code, no matter where in your career you are. Even with agents, the hardest thing in programming remains working out what the software should do, and articulating it well. Bashing out the syntax continues to get easier.

[2](https://ghiculescu.substack.com/p/nobody-codes-here-anymore#footnote-anchor-2-162309066)

A close second in Rails is adding `rescue` statements to every controller action.

[3](https://ghiculescu.substack.com/p/nobody-codes-here-anymore#footnote-anchor-3-162309066)

The irony of Ben Thompson posting Milei videos on X and then monitoring everyone’s Gemini usage is not lost on me.
