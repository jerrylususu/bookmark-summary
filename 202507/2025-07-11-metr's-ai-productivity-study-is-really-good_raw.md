Title: METR's AI productivity study is really good

URL Source: https://www.seangoedecke.com/impact-of-ai-study/

Markdown Content:
I complain a lot on this blog about [AI](https://www.seangoedecke.com/illusion-of-thinking)[studies](https://www.seangoedecke.com/your-brain-on-chatgpt). Given that, I ought to give credit when an AI study comes out that I think is really good. Yesterday METR released a study called [Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity](https://metr.org/Early_2025_AI_Experienced_OS_Devs_Study.pdf)[1](https://www.seangoedecke.com/impact-of-ai-study/#fn-1). It contained a result that was surprising to me: that AI assistance actually slowed engineers down, while making them think they were going faster. Let’s talk about it.

### Why this study is good

What makes this study better than other ones I’ve seen? First, it uses actual state-of-the-art AI models and tools (Cursor Pro and 3.5/3.7 Sonnet). A depressing number of studies and articles about AI are based on GPT-4o, or even 3.5. Agentic coding tools only really started to work [this year](https://www.seangoedecke.com/ai-agents-are-commoditized). Second, it tests actual real-world coding tasks, not weak proxies like writing college essays or toy puzzles. Third, it tests a homogeneous group of professionals: developers with multiple years of experience on their codebases. Fourth - and most exciting to me - it tests actual large codebases. Working on a 500 line codebase is just [qualitatively different](https://www.seangoedecke.com/large-established-codebases) from working on a 1M+ line codebase. That’s even more true when you’re using AI, since the difference between “the whole problem fits in my context window” and “I have to go and search for the relevant code snippets that need changing” is huge.

### What they found

The main result of the study is fascinating. When asked to estimate how much using AI would speed them up, the developers guessed around 24%. After actually using AI, they thought they’d been working about 20% faster. But in fact they were 19% _slower_ overall - even though it was entirely up to them how much or how they used AI.

When you read a result like this, it’s very tempting to start hypothesizing (particularly if you yourself have been using AI tooling and think it’s made you faster). For instance, maybe there’s a steep learning curve to the tooling that the study participants didn’t have enough time to climb? The authors of the study anticipated this, and wrote a whole section about twenty possible hypotheses and why they might be plausible (page 18 of the [pdf](https://metr.org/Early_2025_AI_Experienced_OS_Devs_Study.pdf)). The “maybe there’s a steep learning curve” is addressed in C.2.7, where they make these points:

*   Developers didn’t get faster with AI over the course of the experiment
*   Breaking down the data by which developers have previous AI tooling experience doesn’t show a difference
*   Breaking down the data by _hours of experience with Cursor_ doesn’t show a difference[2](https://www.seangoedecke.com/impact-of-ai-study/#fn-2)

How do the authors explain the 19% slowdown? They picked five hypotheses, which I’ll summarize in three points:

First, the developers in the study might have been over-optimistic about how useful AI would be, and so used it too much: i.e. on tasks that they could have done quicker on their own. Many developers in the study reported spending much of their time cleaning up AI-generated code.

Second, the study focused on developers doing work in open-source repositories that they’ve got an average of five years and 1,500 commits of experience with. These people are going to be _very fast_ at doing normal issues on their own - it’s possible that there’s just not much room for AI to help here, and that the real niche of AI is when developers have to do tasks that are a little out of their comfort zone.

Third, the repositories in question are large, with a lot of implicit rules. AI isn’t at its best in this environment. It might have done better in smaller projects.

### Why I think AI wasn’t faster

Of the authors’ theories, I think the second hypothesis is most convincing. I use AI a lot in my own work, but the vast majority of my AI use (not counting quick second-opinion checks) is when I’m a little out of my comfort zone. I am much faster than Claude Sonnet 3.7/4 at fixing bugs in code I know well. Some of the time I can almost dictate exactly what the bugfix will look like upon reading the bug report. It’s hard for AI to compete with that.

I have my own hypothesis as well. Looking at the repositories in question - at least the subset that were able to be made public - I notice that almost all of them are libraries or compilers. In other words, they’re what I would call [“pure” software](https://www.seangoedecke.com/pure-and-impure-engineering). Pure software is always going to be less amenable to AI-generated changes, because the quality bar is necessarily higher. It’s much more likely that GPT-4.1 can write acceptable code for the prototype dashboard at my startup than it can for the Haskell compiler (one of the actual repositories in the study).

### The illusion of speed

However, this is only half of the study’s result. The other half is even more interesting: developers came away from the study thinking they were 20% faster, but were in fact 19% slower. How can experienced developers not know how fast they’re going?

I don’t think the study offers a compelling answer to this question. But it does give some hints. First, it notes that many developers (though not all) felt that working with AI was easier. 69% of developers continued using the AI tooling after the end of the study, which is at least strong circumstantial evidence of that. Second, it notes that the screen-recording data showed that AI-assisted coding had more idle time: not just “waiting for the model” time, but straight-up no activity at all.

In my view, the likeliest explanation is that coding with AI requires less cognitive effort, and makes it easier to multi-task or just to zone out. Even if it’s not faster, it feels faster because (a) you’re getting more ancillary tasks done while you wait for the LLM, or (b) you’re more mentally relaxed, so time feels like it’s passing quicker.

Incidentally, this is an underrated benefit of AI-assisted coding. When I am rested and focused I am a fast and effective programmer. But I don’t spend all my time rested and focused. When I’m tired, or mentally frayed after a long day of work, or just distracted, I can’t really sit down and fix a bug (at least not without a serious mental effort). However, I _can_ fire off an agentic coding session. Checking the LLM output - particularly for a bugfix, which is typically a small diff - is much less cognitively taxing than having to do it myself. So it’s not so much “AI makes me more effective at my normal work”, as it is “AI means I can work at times that I otherwise would be able to get nothing done at all”. It doesn’t really matter if it’s 19% or 50% or 200% slower than my normal working pace, since any amount of progress is better than zero.

### Final thoughts

I don’t want to downplay the main result of the study. Even if I can rationalize it, it’s still genuinely surprising that AI use slowed people down while making them believe they were faster. If nothing else, it’s evidence that my internal feeling of “wow, this new technology is really speeding me up” may not be reliable.

It’s also a bit unfair to say that all studies should be like this one. This study was pretty expensive! It paid participants $150/hr for a lot of engineering work, on top of the raw inference costs (though I suspect some of that was donated). I don’t blame other studies for focusing on the standard student participants - particularly since “do LLMs help students learn” is itself a valuable question.

Still, I really do think this is the best study on AI-in-engineering that I’ve seen. I would very much like to see a version of this where the engineers were working on unfamiliar codebases, or where the engineers were a bit sleep-deprived or drunk[3](https://www.seangoedecke.com/impact-of-ai-study/#fn-3). If there’s still a slowdown under those circumstances, I might have to seriously reconsider how I think about AI-assisted coding.

* * *

1.   In terms of naming, a marked improvement over “Your Brain on ChatGPT” and “The Illusion of Thinking”.

[↩](https://www.seangoedecke.com/impact-of-ai-study/#fnref-1)
2.   Interestingly, the developer in their study with the most Cursor experience actually sped up when they used AI (though an author [comment](https://news.ycombinator.com/item?id=44523638) on HN made the good point that it’s hard to distinguish “slower without AI” from “faster with AI”).

[↩](https://www.seangoedecke.com/impact-of-ai-study/#fnref-2)
3.   Possibly this isn’t an experiment you could run - though it seems to me that with the amount of money at stake, large enterprises _could_ be incentivized to run something like this internally. Microsoft, I volunteer!

[↩](https://www.seangoedecke.com/impact-of-ai-study/#fnref-3)

If you liked this post, consider [subscribing](https://buttondown.com/seangoedecke) to email updates about my new posts.
