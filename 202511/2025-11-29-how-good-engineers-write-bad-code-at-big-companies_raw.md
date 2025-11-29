Title: How good engineers write bad code at big companies

URL Source: https://www.seangoedecke.com/bad-code-at-big-companies/

Markdown Content:
Every couple of years [somebody](https://ziglang.org/news/migrating-from-github-to-codeberg/)[notices](https://github.com/microsoft/terminal/issues/10362) that large tech companies sometimes produce surprisingly sloppy code. If you haven’t worked at a big company, it might be hard to understand how this happens. Big tech companies pay well enough to attract many competent engineers. They move slowly enough that it looks like they’re able to take their time and do solid work. How does bad code happen?

### Most code changes are made by relative beginners

I think the main reason is that **big companies are full of engineers working outside their area of expertise**. The average big tech employee stays for only [a year or two](https://stackoverflow.blog/2022/04/19/whats-the-average-tenure-of-an-engineer-at-a-big-tech-company-ep-434/)[1](https://www.seangoedecke.com/bad-code-at-big-companies/#fn-1). In fact, big tech compensation packages are typically designed to put a four-year cap on engineer tenure: after four years, the initial share grant is fully vested, causing engineers to take what can be a 50% pay cut. Companies do extend temporary yearly refreshes, but it obviously incentivizes engineers to go find another job where they don’t have to wonder if they’re going to get the other half of their compensation each year.

If you count internal mobility, it’s even worse. The longest I have ever stayed on a single team or codebase was three years, near the start of my career. I expect to be [re-orged](https://www.youtube.com/watch?v=yDcaRklX7q4) at least every year, and often much more frequently.

However, the average tenure of a codebase in a big tech company is a lot longer than that. Many of the services I work on are a decade old or more, and have had many, many different owners over the years. That means many big tech engineers are constantly “figuring it out”. **A pretty high percentage of code changes are made by “beginners”:** people who have onboarded to the company, the codebase, or even the programming language in the past six months.

### Old hands

To some extent, this problem is mitigated by “old hands”: engineers who happen to have been in the orbit of a particular system for long enough to develop real expertise. These engineers can give deep code reviews and reliably catch obvious problems. But relying on “old hands” has two problems.

First, **this process is entirely informal**. Big tech companies make surprisingly little effort to develop long-term expertise in individual systems, and once they’ve got it they seem to barely care at all about retaining it. Often the engineers in question are moved to different services, and have to either keep up their “old hand” duties on an effectively volunteer basis, or abandon them and become a relative beginner on a brand new system.

Second, **experienced engineers are always overloaded**. It is a _busy_ job being one of the few engineers who has deep expertise on a particular service. You don’t have enough time to personally review every software change, or to be actively involved in every decision-making process. Remember that _you also have your own work to do_: if you spend all your time reviewing changes and being involved in discussions, you’ll likely be punished by the company for not having enough individual output.

### The median productive engineer

Putting all this together, what does the median productive[2](https://www.seangoedecke.com/bad-code-at-big-companies/#fn-2) engineer at a big tech company look like? They are usually:

*   competent enough to pass the hiring bar and be able to do the work, but either
*   working on a codebase or language that is largely new to them, or
*   trying to stay on top of a flood of code changes while also juggling their own work.

They are almost certainly working to a deadline, or to a series of overlapping deadlines for different projects. In other words, **they are trying to do their best in an environment that is not set up to produce quality code.**

That’s how “obviously” bad code happens. For instance, a junior engineer picks up a ticket for an annoying bug in a codebase they’re barely familiar with. They spend a few days figuring it out and come up with a hacky solution. One of the more senior “old hands” (if they’re lucky) glances over it in a spare half-hour, vetoes it, and suggests something slightly better that would at least work. The junior engineer implements that as best they can, tests that it works, it gets briefly reviewed and shipped, and everyone involved immediately moves on to higher-priority work. Five years later somebody notices this[3](https://www.seangoedecke.com/bad-code-at-big-companies/#fn-3) and thinks “wow, that’s hacky - how did such bad code get written at such a big software company”?

### Big tech companies are fine with this

I have written a lot about the internal tech company dynamics that contribute to this. Most directly, in [_Seeing like a software company_](https://www.seangoedecke.com/seeing-like-a-software-company) I argue that big tech companies consistently prioritize internal _legibility_ - the ability to see at a glance who’s working on what and to change it at will - over productivity. Big companies know that treating engineers as fungible and moving them around destroys their ability to develop long-term expertise in a single codebase. **That’s a deliberate tradeoff.** They’re giving up some amount of expertise and software quality in order to gain the ability to rapidly deploy skilled engineers onto whatever the problem-of-the-month is.

I don’t know if this is a good idea or a bad idea. It certainly seems to be working for the big tech companies, particularly now that “how fast can you pivot to something AI-related” is so important. But if you’re doing this, then _of course_ you’re going to produce some genuinely bad code. That’s what happens when you ask engineers to rush out work on systems they’re unfamiliar with.

**Individual engineers are entirely powerless to alter this dynamic**. This is particularly true in 2025, when [the balance of power has tilted](https://www.seangoedecke.com/good-times-are-over) away from engineers and towards tech company leadership. The most you can do as an individual engineer is to try and become an “old hand”: to develop expertise in at least one area, and to use it to block the worst changes and steer people towards at least minimally-sensible technical decisions. But even that is often swimming against the current of the organization, and if inexpertly done can cause you to get [PIP-ed](https://www.reddit.com/r/csMajors/comments/1et7miz/what_you_need_to_know_about_performance/) or worse.

### Pure and impure engineering

I think a lot of this comes down to the distinction between [pure and impure software engineering](https://www.seangoedecke.com/pure-and-impure-engineering). To pure engineers - engineers working on self-contained technical projects, like [a programming language](https://ziglang.org/) - the only explanation for bad code is incompetence. But impure engineers operate more like plumbers or electricians. They’re working to deadlines on projects that are relatively new to them, and even if their technical fundamentals are impeccable, there’s always _something_ about the particular setup of this situation that’s awkward or surprising. To impure engineers, bad code is inevitable. As long as the overall system works well enough, the project is a success.

At big tech companies, engineers don’t get to decide if they’re working on pure or impure engineering work. It’s [not their codebase](https://www.seangoedecke.com/not-your-codebase)! If the company wants to move you from working on database infrastructure to building the new payments system, they’re fully entitled to do that. The fact that you might make some mistakes in an unfamiliar system - or that your old colleagues on the database infra team might suffer without your expertise - is a deliberate tradeoff being made by **the company, not the engineer**.

It’s fine to point out examples of bad code at big companies. If nothing else, it can be an effective way to get those specific examples fixed, since execs usually jump at the chance to turn bad PR into good PR. But I think it’s a mistake[4](https://www.seangoedecke.com/bad-code-at-big-companies/#fn-4) to attribute primary responsibility to the engineers at those companies. If you could wave a magic wand and make every engineer twice as strong, _you would still have bad code_, because almost nobody can come into a brand new codebase and quickly make changes with zero mistakes. The root cause is that **most big company engineers are forced to do most of their work in unfamiliar codebases**.

* * *

1.   I struggled to find a good original source on this. There’s a 2013 PayScale [report](https://www.payscale.com/data-packages/employee-loyalty/least-loyal-employees) citing a 1.1 year median turnover at Google, which seems low.

[↩](https://www.seangoedecke.com/bad-code-at-big-companies/#fnref-1)
2.   Many engineers at big tech companies are not productive, but that’s a post all to itself. I don’t want to get into it here for two reasons. First, I think competent engineers produce enough bad code that it’s fine to be a bit generous and just scope the discussion to them. Second, even if an incompetent engineer wrote the code, there’s almost always competent engineers who could have reviewed it, and the question of why that didn’t happen is still interesting.

[↩](https://www.seangoedecke.com/bad-code-at-big-companies/#fnref-2)
3.   The example I’m thinking of here is not the [recent GitHub Actions one](https://ziglang.org/news/migrating-from-github-to-codeberg/), which I have no first-hand experience of. I can think of at least ten separate instances of this happening to me.

[↩](https://www.seangoedecke.com/bad-code-at-big-companies/#fnref-3)
4.   In my view, mainly a failure of _imagination_: thinking that your own work environment must be pretty similar to everyone else’s.

[↩](https://www.seangoedecke.com/bad-code-at-big-companies/#fnref-4)

If you liked this post, consider[subscribing](https://buttondown.com/seangoedecke)to email updates about my new posts, or[sharing it on Hacker News](https://news.ycombinator.com/submitlink?u=https://www.seangoedecke.com/bad-code-at-big-companies/&t=How%20good%20engineers%20write%20bad%20code%20at%20big%20companies). Here's a preview of a related post that shares tags with this one.

> How I influence tech company politics as a staff software engineer
> 
> 
> 
> Many software engineers are fatalistic about company politics. They believe that it’s pointless to get involved, because:
> 
> 
> The general idea here is that **software engineers are simply not equipped to play the game at the same level as real political operators**. This is true! It would be a terrible mistake for a software engineer to think that you ought to start scheming and plotting like you’re in _Game of Thrones_. Your schemes will be immediately uncovered and repurposed to your disadvantage and other people’s gain. Scheming takes practice and power, and neither of those things are available to software engineers.
> 
> [Continue reading...](https://www.seangoedecke.com/how-to-influence-politics/)

* * *