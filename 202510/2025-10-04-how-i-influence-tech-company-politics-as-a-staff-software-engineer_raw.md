Title: How I influence tech company politics as a staff software engineer

URL Source: https://www.seangoedecke.com/how-to-influence-politics/

Markdown Content:
Many software engineers are fatalistic about company politics. They believe that it’s pointless to get involved, because[1](https://www.seangoedecke.com/how-to-influence-politics/#fn-1):

*   Technical decisions are often made for [completely selfish reasons](https://news.ycombinator.com/item?id=45441068) that cannot be influenced by a well-meaning engineer
*   Powerful stakeholders are typically [so stupid and dysfunctional](https://news.ycombinator.com/item?id=45442587) that it’s effectively impossible for you to identify their needs and deliver solutions to them
*   The political game being played depends on private information that software engineers do not have, so any attempt to get involved will result in just blundering around
*   Managers and executives spend most of their time playing politics, while engineers spend most of their time doing engineering, so engineers are at a serious political disadvantage before they even start

The general idea here is that **software engineers are simply not equipped to play the game at the same level as real political operators**. This is true! It would be a terrible mistake for a software engineer to think that you ought to start scheming and plotting like you’re in _Game of Thrones_. Your schemes will be immediately uncovered and repurposed to your disadvantage and other people’s gain. Scheming takes practice and power, and neither of those things are available to software engineers.

It is simply a fact that software engineers are tools in the political game being played at large companies, not players in their own right. However, there are many ways to get involved in politics without scheming.

The easiest way is to **actively work to make a high-profile project successful**. This is more or less what you ought to be doing anyway, just as part of your ordinary job. If your company is heavily investing in some new project - these days, likely an AI project - using your engineering skill to make it successful[2](https://www.seangoedecke.com/how-to-influence-politics/#fn-2) is a politically advantageous move for whatever VP or executive is spearheading that project. In return, you’ll get the rewards that executives can give at tech companies: bonuses, help with promotions, and positions on future high-profile projects. I wrote about this almost a year ago in [_Ratchet effects determine engineer reputation at large companies_](https://www.seangoedecke.com/ratchet-effects).

A slightly harder way (but one that gives you more control) is to **make your pet idea available for an existing political campaign**. Suppose you’ve wanted for a while to pull out some existing functionality into its own service. There are two ways to make that happen.

The hard way is to expend your own political capital: drum up support, let your manager know how important it is to you, and slowly wear doubters down until you can get the project formally approved. The easy way is to **allow some executive to spend their (much greater) political capital on your project**. You wait until there’s a company-wide mandate for some goal that aligns with your project (say, a push for reliability, which often happens in the wake of a high-profile incident). Then you suggest to your manager that your project might be a good fit for this. If you’ve gauged it correctly, your org will get behind your project. Not only that, but it’ll increase your political capital instead of you having to spend it.

Organizational interest comes in waves. When it’s reliability time, VPs are desperate to be _doing something_. They want to come up with plausible-sounding reliability projects that they can fund, because they need to go to their bosses and point at what they’re doing for reliability, but they don’t have the skillset to do it on their own. They’re typically happy to fund anything that the engineering team suggests. On the other hand, when the organization’s attention is focused somewhere else - say, on a big new product ship - the last thing they want is for engineers to spend their time on an internal reliability-focused refactor that’s invisible to customers.

So if you want to get something technical done in a tech company, **you ought to wait for the appropriate wave**. It’s a good idea to prepare multiple technical programs of work, all along different lines. Strong engineers will do some of this kind of thing as an automatic process, simply by noticing things in the normal line of work. For instance, you might have rough plans:

*   to migrate the billing code to stored-data-updated-by-webhooks instead of cached API calls
*   to rip out the ancient hand-rolled build pipeline and replace it with Vite
*   to rewrite a crufty high-volume Python service in Golang
*   to replace the slow CMS frontend that backs your public documentation with a fast static site

When executives are concerned about billing, you can offer the billing refactor as a reliability improvement. When they’re concerned about developer experience, you can suggest replacing the build pipeline. When customers are complaining about performance, you can point to the Golang rewrite as a good option. When the CEO checks the state of the public documentation and is embarrassed, you can make the case for rebuilding it as a static site. **The important thing is to have a detailed, effective program of work ready to go for whatever the flavor of the month is.**

Some program of work will be funded whether you do this or not. However, if you don’t do this, you have no control over what that program is. In my experience, **this is where companies make their worst technical decisions**: when the political need to do _something_ collides with a lack of any good ideas. When there are no good ideas, a bad idea will do, in a pinch. But nobody prefers this outcome. It’s bad for the executives, who then have to sell a disappointing technical outcome as if it were a success[4](https://www.seangoedecke.com/how-to-influence-politics/#fn-4), and it’s bad for the engineers, who have to spend their time and effort building the wrong idea.

If you’re a very senior engineer, the VPs (or whoever) will quietly blame you for this. They’ll be right to! **Having the right idea handy at the right time is your responsibility.**

You can view all this in two different ways. Cynically, you can read this as a suggestion to make yourself a convenient tool for the sociopaths who run your company to use in their endless internecine power struggles. Optimistically, you can read this as a suggestion to let executives set the overall priorities for the company - that’s their job, after all - and to tailor your own technical plans to fit[3](https://www.seangoedecke.com/how-to-influence-politics/#fn-3). Either way, you’ll achieve more of your technical goals if you push the right plan at the right time.

* * *

1.   I was prompted to write this after reading Terrible Software’s article [_Don’t avoid workplace politics_](https://terriblesoftware.org/2025/10/01/stop-avoiding-politics/) and its [comments](https://news.ycombinator.com/item?id=45440571) on Hacker News. Disclaimer: I am talking here about broadly functional tech companies (i.e. ones that are making money). If you’re working somewhere that’s completely dysfunctional, I have no idea whether this advice would apply at all.

[↩](https://www.seangoedecke.com/how-to-influence-politics/#fnref-1)
2.   What it takes to make a project successful is itself a complex political question that every senior+ engineer is eventually forced to grapple with (or to deliberately avoid, with consequences for their career). For more on that, see [_How I ship projects at large tech companies_](https://www.seangoedecke.com/how-to-ship).

[↩](https://www.seangoedecke.com/how-to-influence-politics/#fnref-2)
3.   For more along these lines, see [_Is it cynical to do what your manager wants?_](https://www.seangoedecke.com/cynicism)

[↩](https://www.seangoedecke.com/how-to-influence-politics/#fnref-3)
4.   Just because they _can_ do this doesn’t mean they _want_ to.

[↩](https://www.seangoedecke.com/how-to-influence-politics/#fnref-4)

If you liked this post, consider [subscribing](https://buttondown.com/seangoedecke) to email updates about my new posts, or [sharing it on Hacker News](https://news.ycombinator.com/submitlink?u=https://www.seangoedecke.com/how-to-influence-politics/&t=How%20I%20influence%20tech%20company%20politics%20as%20a%20staff%20software%20engineer).

October 4, 2025│ Tags: [good engineers](https://www.seangoedecke.com/tags/good%20engineers/), [tech companies](https://www.seangoedecke.com/tags/tech%20companies/)

* * *