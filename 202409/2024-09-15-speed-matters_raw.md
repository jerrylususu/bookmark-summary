Title: Speed matters

URL Source: https://www.scattered-thoughts.net/writing/speed-matters/

Markdown Content:
_This post is part of a series, starting at [Reflections on a decade of coding](https://www.scattered-thoughts.net/writing/reflections-on-a-decade-of-coding)._

I think that one of the most important things to focus on improving is how fast you can work.

* * *

I wrote [strucjure](https://github.com/jamii/strucjure) in 2012 and [rematch](https://github.com/RelationalAI-oss/Rematch.jl/) in 2018. Both libraries provide a pattern matching macro with very similar functionality. Strucjure was never used by anyone. I think rematch is still used in production in the relational.ai compiler.

I don't know exactly how long each took because both of their commit histories start with a code dump from a different repo. But strucjure has commits from me on 61 different days across more than a year. Rematch has commits from me on 9 different days across two months. Also most of the rematch commits are little tweaks requested by people using it - I think the original rewrite of [match.jl](https://github.com/kmsquire/Match.jl/issues) only took a day or two and then it went into use almost immediately.

So the error bars here are pretty big, but this is at minimum a 5x speedup and probably more like 20-30x if my recollection is correct. Most of the speedup is down to setting much more concrete goals and being much faster at making mundane design decisions (eg what features to support, how to structure code, what to name things), but I also got a lot of benefit from better work processes and from low-level mechanical speedups like writing fewer silly bugs.

Call this an existence proof. It's possible to get something like 10x faster at producing this kind of code over the course of 6 years. This was also without much in the way of active effort, deliberate practice or reflection, so it's very much a lower bound.

There are ~33k characters in the rematch repo, most of which are tests. I type ~500 characters per minute. So if I could sit down and type the correct code first time, without making mistakes or getting distracted, it would take 66 minutes. I don't see any fundamental reason why I shouldn't be able to at least approach that bound for such simple code - maybe get within 3 hours, say. So there is potentially room for another 10x speedup.

* * *

So let's suppose a 10x speedup is within reach.

The first order effects are obvious. If you could work 10x as fast then you could do 10x as much. Or do 5x as much and go home after lunch every day.

New me would be able to do as much work as 10 old mes. Probably more - the 10 old mes would lose a lot of their time to coordination and communication costs.

* * *

Being 10x faster also changes the kinds of projects that are worth doing.

Last year I spent something like 100 hours writing a text editor. That would be 2-4 weeks if had been working on it full-time. I learned the basics of graphics programming, I got to try out some unusual architecture ideas, I get the satisfaction of working every day with a tool that I made myself and I now have a small familiar codebase that I can use for [other experiments](https://www.scattered-thoughts.net/writing/imp-live-repl/). That's a pretty good deal for a few weeks work.

If I was 10x slower it would have been 20-50 weeks. Suddenly that doesn't seem like such a good deal any more - what a waste of a year!

If I was 10x faster yet it would have been 10 hours. That's a long plane ride. Even with a full-time job I would still be able to squeeze in a couple of text editor sized projects every month. I would be able to learn so many new things.

* * *

When I think about speed I think about the whole process - researching, planning, designing, arguing, coding, testing, debugging, documenting etc.

Often when I try to convince someone to get faster at one of those steps, they'll argue that the others are more important so it's not worthwhile trying to be faster. Eg choosing the right idea is more important than coding the wrong idea really quickly.

But that's totally conditional on the speed of everything else! If you could code 10x as fast then you could try out 10 different ideas in the time it would previously have taken to try out 1 idea. Or you could just try out 1 idea, but have 90% of your previous coding time available as extra idea time.

The best part is that you can improve your coding speed a lot by improving simple mechanical skills which are easy to measure, practice and improve. It's a lot easier to get faster at coding then it is to get better at choosing the right idea!

* * *

It's also really hard to get better at having good ideas because you get such little feedback. It might take a year to build out a complex idea before finding out if it's good or not, which means you get maybe 40 attempts in your career.

But if you can try out 10 ideas a year then you get 400 attempts. Having 10x as much feedback is a huge advantage in learning any complex skill.

In addition, if you can code 10x as fast, you also get to do 10x as much coding practice, which will probably lead to yet more improvements.

* * *

Being really fast in one area can also indirectly make you faster in other areas by opening up new tactics.

I mentioned in a previous post [Tonsky writing gui tools during the icfp contest](https://tonsky.me/blog/icfpc-2021/). If I tried to do this I would spend a lot of time looking things up and making the wrong decisions and probably not even have a working gui before the competition was over. So not only is he much faster than me at writing gui tools, but because he's faster he's able to build tools that speed up the rest of his process.

I see similar tooling effects in testing, debugging, profiling, benchmarking etc. The faster you are, the more it becomes worthwhile to build tools on the fly to make you go even faster.

* * *

Another way that speed helps is by removing mental load.

If you compare two coders, one who can touch type and one who has to hunt and peck, the difference between them is not just down to typing speed. The hunter-and-pecker has to think about typing! This consumes attention and short-term memory that is sorely needed for thinking about the program itself.

That example is an extreme, but I think that typing speed and accuracy are on a continuum. Every time your typing falls behind your thinking, ideas start to pile up in short-term memory. Every typo requires a break in the flow that might cause you to forget a task you had queued up.

Similarly, when I first learnt to code I found it really difficult to write simple loops. I would have to get a sheet of paper and write out the state changes on each iteration. Now that process is completely automatic. If I still had to think that hard about loops today I would be completely incapable of doing my job.

Any process that you can make automatic, any decision or context switch that you can avoid, frees up mental resources that can be redeployed elsewhere. So even if the complex high-level work seems like the most crucial, you can still make gains by speeding up the low-level mechanical stuff.

* * *

Another common objection is that any given tweak to the work process might only be a tiny improvement in speed. But little tweaks are cheap and they add up over time.

I often think about [this sqlite release announcement](https://web.archive.org/web/20141007141334/http://permalink.gmane.org/gmane.comp.db.sqlite.general/90549):

> The latest SQLite 3.8.7 alpha version is 50% faster than the 3.7.17 release from 16 months ago. \[...\] This is 50% faster at the low-level grunt work of moving bits on and off disk and search b-trees. We have achieved this by incorporating hundreds of micro-optimizations. Each micro-optimization might improve the performance by as little as 0.05%. If we get one that improves performance by 0.25%, that is considered a huge win. Each of these optimizations is unmeasurable on a real-world system (we have to use cachegrind to get repeatable run-times) but if you do enough of them, they add up.

If you can find a 0.1% improvement each day, that adds up to getting 2x faster every two years (`1.001^(365*2) == 2.07`).

* * *

For me the strongest argument is that being faster is more fun.

I like being able to make more things. I like being able to take on more ambitious projects. I like being good at what I do, and I like trying to get better.

I'm definitely not operating anywhere near the theoretical limits yet, which means I might have another 10x in me. That's pretty exciting.
