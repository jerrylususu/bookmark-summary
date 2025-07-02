Title: Continuous AI in software engineering

URL Source: https://www.seangoedecke.com/continuous-ai/

Markdown Content:
When I use AI in my software engineering job, I use it “on tap”: when I have a problem that I’d like to run past the LLM, [I go and do that](https://www.seangoedecke.com/how-i-use-llms), and then I return to my normal work.

Imagine if we used other software engineering tools like this - for instance when I have a problem that I’d like to solve with unit tests, I go and run the tests, before returning to my normal work. Or suppose when I want to type-check my codebase, I open a terminal and run `npm run tsc`. Would that be a sensible way of using tests and types?

Of course not. Tests and types, and many other programming tools, are used _continuously_: instead of a developer deciding to use them, they’re constantly run and checked via automation. Tests run in CI or as a pre-push commit hook. Types are checked on every compile, or even more often via IDE highlighting. A developer can choose to run these tools manually if they want, but they’ll also get value from them over time even if they never consciously trigger them. Having automatic tests and types raises the level of ambient intelligence in the software development lifecycle.

### What is continuous AI?

All of this is why GitHub is excited about what we call [“continuous AI”](https://githubnext.com/projects/continuous-ai), which refers to any way AI tooling can be automatically integrated into existing development flows. Here are some examples:

*   Automated AI-driven PR reviews (GitHub has a Copilot one that I use at work, but there’s tons of open-source options)
*   AI-driven issue or PR labeling
*   Daily or weekly summary rollups. I’ve written my fair share of these by hand
*   GitHub Copilot or Cursor-like autocomplete

Note that this doesn’t include tooling like Claude Code or Devin that purports to write and test an entire change for you. That tooling is very exciting as well! But it’s not _ambient_ intelligence. You have to go and get it when you want to use it.

### A series of small, boring wins

I wasn’t always a believer in continuous AI. But surprisingly, having Copilot PR reviews turned on by default is what changed my mind. Many of the reviews don’t add much value, but one in every five or ten catches something I missed[1](https://www.seangoedecke.com/continuous-ai/#fn-1) - and the Copilot reviews are so easy to skim that I don’t mind brushing past four of them to get to the one that’s useful. I would like more of this in my development workflow: a second AI opinion on most of my decisions that I can glance at to see if there’s something I missed or not.

I also think there’s a lot of coordination work in large organizations that could be safely delegated to the AI. Most teams I’ve worked on have required weekly rollups: some kind of summary on important issues that can be collected and sent up the management chain as a report. Sometimes this requires careful human attention - for instance, if the project is going badly - but much of the time it just serves as a steady heartbeat of “yes, we’re still working on this, don’t worry”.

This kind of AI work also appeals to the kind of software engineer I am. I like boring things that add a surprising amount of value. I’d rather spend my time picking up low-hanging fruit than building a big clever system to do a big clever thing. In terms of AI-assisted engineering, that means sprinkling a little bit of AI into the software development workflow, instead of being the ten thousandth person to work on the “fully automated software engineer” problem.

### GitHub Actions

One of the most satisfying small wins of my career happened earlier this year, when I added the GitHub Models [permission](https://docs.github.com/en/github-models/use-github-models/integrating-ai-models-into-your-development-workflow#using-ai-models-with-github-actions) to the native access token in GitHub Actions. GitHub Models is GitHub’s free [inference API](https://docs.github.com/en/rest/models?apiVersion=2022-11-28)[2](https://www.seangoedecke.com/continuous-ai/#fn-2). It doesn’t have the most generous rate limits or context windows in the world, but on the other hand it’s free to literally all GitHub users. In my view, Models + Actions is the perfect combo for continuous AI. The free inference means you can try something out without worrying about blowing out your costs or who’s going to pay for the subscription. And Actions is tightly integrated into basically everything you can do on GitHub: you can trigger it when a PR or issue is opened, when someone pushes to the default branch, on a cron job schedule, and so on.

There’s already a [healthy set](https://github.com/githubnext/awesome-continuous-ai) of AI-driven GitHub Actions out there. I think this is only going to grow over time as we find out which patterns work and which don’t. Of course, none of this is specific to GitHub - it could be running on GitLab CI and a paid OpenAI subscription, or whatever your chosen runtime and inference provider is.

In five or ten years, it might be the case that humans aren’t doing any coding, and a series of increasingly powerful agentic models are handling all of the work. But if that future doesn’t materialize[3](https://www.seangoedecke.com/continuous-ai/#fn-3), I think there will still be various layers of AI performing automated checks, organizational tasks, and helping with other parts of the software engineering process.

* * *

1.   For instance, a recent review caught a n+1 query that I hadn’t anticipated.

[↩](https://www.seangoedecke.com/continuous-ai/#fnref-1)
2.   As of last week, now with an optional paid tier for higher rate limits!

[↩](https://www.seangoedecke.com/continuous-ai/#fnref-2)
3.   Even if it does go that way, we might still end up with the AI software engineers assisted by an array of less-sophisticated continuous AI tooling, just like they’re still going to use regular CI and types.

[↩](https://www.seangoedecke.com/continuous-ai/#fnref-3)

If you liked this post, consider [subscribing](https://buttondown.com/seangoedecke) to email updates about my new posts.

July 2, 2025│ Tags: [ai](https://www.seangoedecke.com/tags/ai/)

* * *
