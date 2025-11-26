Title: Becoming unblockable

URL Source: https://www.seangoedecke.com/unblockable/

Markdown Content:
With enough careful effort, it’s possible to become unblockable. In other words, you can put yourself in a position where you’re always able to make forward progress on your goals.

I wrote about this six months ago in [_Why strong engineers are rarely blocked_](https://www.seangoedecke.com/becoming-unblockable), but I wanted to take another crack at it and give some more concrete advice.

### Work on more than one thing

The easiest way to avoid being blocked is to have more than one task on the go. Like a CPU thread, if you’re responsible for multiple streams of work, you can deal with one stream getting blocked by rolling onto another one. While one project might be blocked, _you_ are not: you can continue getting stuff done.

Because of this, I almost always have more than one task on my plate. However, there’s a lot of nuance involved in doing this correctly. The worst thing you can do is to be responsible for two urgent tasks at the same time - no matter how hard you work, one of them will always be making no progress, which is very bad[1](https://www.seangoedecke.com/unblockable/#fn-1). If you’ve got too many ongoing tasks at the same time, you also risk overloading yourself if one or two of them suddenly blow out. It’s famously hard to scope engineering work. In a single day, you can go from having two or three trivial tasks to having three big jobs at the same time.

**I do not recommend just mindlessly picking up an extra ticket from your project board.** Instead, try to have some non-project work floating around: refactors, performance work, writing performance reviews, mandatory training, and so on. It can be okay to pick up an extra ticket if you’re tactical about which ticket you pick up. Try to avoid having two important tasks on the go at the same time.

### Sequence your work correctly

**Plan out projects from the start to minimize blockers.** This section is more relevant for projects that you yourself are running, but the principle holds even for smaller pieces of work.

If you think something is likely to get blocked (for instance, maybe database migrations at your company are run by a dedicated team with a large backlog), **do it as early as possible**. That way you can proceed with the rest of the project while you wait. Getting this wrong can add weeks to a project. Likewise, if there’s a part of your project that’s likely to be controversial, do it early so you can keep working on the rest of the project while the debate rages on.

### Be ruthless about your tooling

Do _whatever it takes_ to have a stable and reliable developer environment. I don’t think it’s possible to overstate the importance of this. The stability of your developer environment directly determines how much of a workday you can spend actually doing work.

For instance, **use as normal a developer stack as possible**. At GitHub, most development is done in [Codespaces](https://github.com/features/codespaces), a platform for server-hosted dev containers. You can connect to a codespace with almost any IDE, but the majority of people use VSCode, _so I use VSCode_, with as few plugins as possible[2](https://www.seangoedecke.com/unblockable/#fn-2). I think a lot of developers are too focused on their personal “top speed” with their developer environment when everything is working great, and under-emphasize how much time they spend tweaking config, patching dotfiles, and troubleshooting in general.

**Fix developer environment problems as quickly as production incidents.** If you can’t run tests or run a local server, don’t half-ass the troubleshooting process - focus on it until it’s fixed. On the flip side, don’t treat it as a leisurely learning experience (say, about how MacOS handles Dockerized networking). In many circumstances you’re probably better off tearing down and re-creating everything than digging in and trying to patch the specific issue.

If your developer environment really is irreparably broken - maybe you’re waiting on new hardware, or you’re making a one-off change to a service that you don’t have the right dev environment permissions for - **be scrappy about finding alternatives**. If you can’t run tests, your GitHub CI probably can. If you can’t run a server locally, can you deploy to a staging environment and test there? Be careful about doing this in your main developer environment. You’re usually better off spending the time to actually fix the problem. But when you can’t, you should be creative about how you can keep working instead of just giving up.

### Debug outside of your area of responsibility

I see a lot of engineers run into a weird thing - commonly a 403 or 400 status code from some other service - and say “oh, I’m blocked, I need this other service’s owners to investigate”. **You can and should investigate yourself.** This is particularly true if you’ve got access to the codebase. If you’re getting an error, go and search their codebase to see what could be causing the error. Find the logs for your request to see if there’s anything relevant there. Of course, you won’t be able to dig as deep as engineers with real domain expertise, but often **it doesn’t take domain expertise** to solve your particular problem.

There’s even less excuse not to do this now that AI agents are ubiquitous. Point Codex (or Copilot agent mode, or Claude Code, or whatever you have access to) at the codebase in question and ask “why might I be seeing this error with this specific request?” In my experience, you get the correct answer about a third of the time, which is _amazing_. Instead of waiting for hours or days to get help, you can spend ten minutes waiting for the agent and half an hour checking its work.

Even if you can’t solve the problem yourself, **a bit of research can often make your request for help much more compelling**. As a service owner, there’s nothing more dispiriting than getting a “help, I get weird 400 errors” message - you know you’re going to spend a lot of time trawling through the logs before you can even figure out what the problem is, let alone how to reproduce it. But if the message already contains a link to the logs, or the text of a specific error, that immediately tells you where to start looking.

### Build relationships

There are typically two ways to do anything in a large tech company: the formal, [legible](https://www.seangoedecke.com/seeing-like-a-software-company) way, and the informal way. As an example, it’s common to have a “ask for code review” Slack channel, which is full of engineers posting their changes. But many engineers don’t use these channels at all. Instead, they ping each other for immediate reviews, which is a much faster process.

Of course, you can’t just DM random engineers asking for them to review your PR. It might work in the short term, but people will get really annoyed with you. You have to **build relationships** with engineers on every codebase you’d like to work on. If you’re extremely charismatic, maybe you can accomplish this with sheer force of will. But the rest of us have to build relationships by being useful: giving prompt and clear responses to questions from other teams, investigating bugs for them, reviewing their code, and so on.

**The most effective engineers at are tech company typically have really strong relationships with engineers on many other different teams.** That isn’t to say that they operate entirely through backchannels, just that they have personal connections they can draw on when needed. If you’re blocked on work that another team is doing, it makes a huge difference having “someone on the inside”.

### Acquire powerful allies

Almost all blockers at large tech companies can be destroyed with sufficient “air support”. Typically this means a director or VP who’s aware of your project and is willing to throw their weight around to unblock you. For instance, they might message the database team’s manager saying “hey, can you prioritize this migration”, or task their very-senior-engineer direct report with resolving some technical debate that’s delaying your work.

You can’t get air support for everything you’d like to do - it just doesn’t work like that, unless the company is very dysfunctional or you have a _very_ good relationship with a senior manager. But you can choose to do things that align with what senior managers in the organizaton want, which can put you in a position to request support and get it. I wrote about this a lot more in [_How I influence tech company politics as a staff software engineer_](https://www.seangoedecke.com/how-to-influence-politics), but in one sentence: the trick is to have a bunch of possible project ideas in your back pocket, and then choose the ones that align with whatever your company cares about this month.

Many engineers just don’t make use of the powerful allies they have. If you’re working on a high-priority project, the executive in charge of that project is unlikely to have the bandwidth to follow your work closely. They will be depending on you to go and tell them if you’re blocked and need their help.

Unlike the relationships you may have with engineers on different teams, requesting air cover does not spend any credit. In fact, it often _builds_ it, by showing that you’re switched-on enough to want to be unblocked, and savvy enough to know you can ask for their help. Senior managers are usually quite happy to go and unblock you, if you’re clear enough about what exactly you need them to do.

### Summary

To minimize the amount of time you spend blocked, I recommend:

*   Working on at least two things at a time, so when one gets blocked you can switch to the other
*   Sequencing your work so potential blockers are discovered and started early
*   Making a reliable developer environment a high priority, including avoiding unusual developer tooling
*   Being willing to debug into other services that you don’t own
*   Building relationships with engineers on other teams
*   Making use of very senior managers to unblock you, when necessary

* * *

1.   At some point somebody important will ask “why isn’t this task making any progress”, and you do not want the answer to be “I was working on something else”.

[↩](https://www.seangoedecke.com/unblockable/#fnref-1)
2.   Before I joined GitHub, I worked entirely inside a terminal and neovim. I switched to VSCode entirely because of Codespaces. If I joined another company where most developers used JetBrains, I would immediately switch to JetBrains.

[↩](https://www.seangoedecke.com/unblockable/#fnref-2)

If you liked this post, consider[subscribing](https://buttondown.com/seangoedecke)to email updates about my new posts, or[sharing it on Hacker News](https://news.ycombinator.com/submitlink?u=https://www.seangoedecke.com/unblockable/&t=Becoming%20unblockable). Here's a preview of a related post that shares tags with this one.

> Mistakes I see engineers making in their code reviews
> 
> 
> 
> In the last two years, code review has gotten much more important. Code is now easy to generate using LLMs, but it’s still just as hard to review. Many software engineers now spend as much (or more) time reviewing the output of their own AI tools than their colleagues’ code.
> 
> 
> I think a lot of engineers don’t do code review correctly. Of course, there are lots of different ways to do code review, so this is largely a statement of my [engineering taste](https://www.seangoedecke.com/taste).
> 
> [Continue reading...](https://www.seangoedecke.com/good-code-reviews/)

* * *