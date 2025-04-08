Title: Git turns 20: A Q&A with Linus Torvalds

URL Source: https://github.blog/open-source/git/git-turns-20-a-qa-with-linus-torvalds/

Published Time: 2025-04-07T22:58:14+00:00

Markdown Content:
To celebrate two decades of Git, we sat down with Linus Torvalds—the creator of Git and Linux—to discuss how it forever changed software development.

April 7, 2025

|

29 minutes

*   Share:
*   [](https://x.com/share?text=Git%20turns%2020%3A%20A%20Q%26amp%3BA%20with%20Linus%20Torvalds&url=https%3A%2F%2Fgithub.blog%2Fopen-source%2Fgit%2Fgit-turns-20-a-qa-with-linus-torvalds%2F)
*   [](https://www.facebook.com/sharer/sharer.php?t=Git%20turns%2020%3A%20A%20Q%26amp%3BA%20with%20Linus%20Torvalds&u=https%3A%2F%2Fgithub.blog%2Fopen-source%2Fgit%2Fgit-turns-20-a-qa-with-linus-torvalds%2F)
*   [](https://www.linkedin.com/shareArticle?title=Git%20turns%2020%3A%20A%20Q%26amp%3BA%20with%20Linus%20Torvalds&url=https%3A%2F%2Fgithub.blog%2Fopen-source%2Fgit%2Fgit-turns-20-a-qa-with-linus-torvalds%2F)

Exactly twenty years ago, on April 7, 2005, Linus Torvalds made [the very first commit](https://github.com/git/git/commit/e83c5163316f89bfbde7d9ab23ca2e25604af290) to a new version control system called Git. Torvalds famously wrote Git in just ten days after Linux kernel developers lost access to their proprietary tool, BitKeeper, due to licensing disagreements. In fact, in that first commit, he’d written enough of Git to use Git to make the commit!

Git’s unconventional and decentralized design—nowadays ubiquitous and seemingly obvious—was revolutionary at the time, and reshaped how software teams collaborate and develop. (To wit, GitHub!)

To celebrate two decades of Git, we sat down with Linus himself to revisit those early days, explore the key design decisions behind Git’s lasting success, and discuss how it forever changed software development.

Check out the transcript of our interview below, and **check back later this week for the full video of our interview.**

**Want to watch a sneak peek of our video interview with Linus? 👇**

[https://github.blog/wp-content/uploads/2025/04/LINUS-TORVALDS-INTERVIEW-SOCIAL-CLIP\_BLOG.mp4#t=0.001](https://github.blog/wp-content/uploads/2025/04/LINUS-TORVALDS-INTERVIEW-SOCIAL-CLIP_BLOG.mp4#t=0.001)

_The following transcript has been lightly edited for clarity._

* * *

**It’s been 20 years, almost to the hour, since Git was self-hosted enough to write its initial commit. Did you expect to be sitting here 20 years later, still using it and talking about it?**

Still using it, yes. Maybe not talking about it. I mean, that has been one of the big surprises—basically how much it took over the whole SCM world. I saw it as a solution to my problems, and I obviously thought it was superior. Even literally 20 years ago to the day, I thought that first version, which was pretty raw—to be honest, even that version was superior to CVS.

But at the same time, I’d seen CVS just hold on to the market—I mean, SVN came around, but it’s just CVS in another guise, right?—for many, many decades. So I was like, okay, this market is very sticky. I can’t use CVS because I hate it with a passion, so I’ll do my own thing. I couldn’t use BitKeeper, obviously, anymore. So I was like, okay, I’ll do something that works for me, and I won’t care about anybody else. And really that showed in the first few months and years—people were complaining that it was kind of hard to use, not intuitive enough. And then something happened, like there was a switch that was thrown.

“I’ll do something that works for me, and I won’t care about anybody else.”

**Well, you mentioned BitKeeper. Maybe we can talk about that.**

Sure.

**Pretty famously, you wrote the initial version of Git in around 10 or so days as a replacement for the kernel.**

Yes and no. It was actually fewer than—well, it was about 10 days until I could use it for the kernel, yes. But to be fair, the whole process started like December or November the year before, so 2004.

What happened was BitKeeper had always worked fairly well for me. It wasn’t perfect, but it was light years ahead of anything else I’ve tried. But BitKeeper in the kernel community was always very, like, not entirely welcomed by the community because it was commercial. It was free for open source use because Larry McVoy, who I knew, really liked open source. I mean, at the same time, he was making a business around it and he wanted to sell BitKeeper to big companies. \[It\] not being open source and being used for one of the biggest open source projects around was kind of a sticking point for a lot of people. And it was for me, too.

I mean, to some degree I really wanted to use open source, but at the same time I’m very pragmatic and there was nothing open source that was even remotely good enough. So I was kind of hoping that something would come up that would be better. But what did come up was that Tridge in Australia basically reversed engineered BitKeeper, which wasn’t that hard because BitKeeper internally was basically a good wrapper around SCCS, which goes back to the 60s. This is not, CCS is almost worse than CVS.

But that was explicitly against the license rules for BitKeeper. BitKeeper was like, you can use this for open source, but you can’t reverse engineer it. And you can’t try to kind of clone BitKeeper. And that made for huge issues. And this was all in private, so I was talking to Larry and I was emailing with Tridge and we were trying to come up with a solution, but Tridge and Larry were really on completely opposite ends of the spectrum and there was no solution coming up.

So by the time I started writing Git, I had actually been thinking about the issue for four months and thinking about what worked for me and thinking about how do I do something that does even better than BitKeeper does but doesn’t do it the way BitKeeper does it. I did not want to be in the situation where Larry would say, “Hey, you did the one thing you were not supposed to do.”

> “…how do I do **something that does even better than BitKeeper does**, but doesn’t do it the way BitKeeper does it.”

So yes, the writing part was maybe 10 days until I started using Git for the kernel, but there was a lot of mental going over what the ideas should be.

**I want to talk about maybe both of those things. We can start with that kind of 10-day period. So as I understand it, you had sort of taken that period as a time away from the kernel and had mostly focused on Git in isolation. What was that transition like for you to just be working on Git and not thinking about the kernel?**

Well, since it was only two weeks, it ended up being that way. It wasn’t actually a huge deal. I’d done things like that just for—I’ve been on, like in the last 35 years, I’ve been on vacation a couple of times, right, not very many times. But I have been away from the kernel for two weeks at a time before.

And it was kind of interesting because it was—one of my reactions was how much easier it is to do programming in the userspace. You need to be, there’s so much less you need to care about. You don’t need to worry about memory allocations. You don’t need to worry about a lot of things. And debugging is so much easier when you have all this infrastructure that you’re writing when you’re doing a kernel.

So it was actually somewhat—I mean, I wouldn’t say relaxing, but it was fun to do something user spacey where I had a fairly clear goal of what I wanted. I mean, a clear goal in the sense I knew the direction. I didn’t know the details.

**I want to talk about one of the things I find so interesting about Git, especially 20 years on, is it’s so… the development model that it encourages, to me, seems so simple that it’s almost obvious at this point. But I don’t say that as a reductive term. I think there must have been quite a lot of thought into distilling down from the sort of universe of source control ideas down into something that became Git. Tell me, what were the sort of non-obvious choices you made at the time that we have?**

The fact that you say it’s obvious now, I think it wasn’t obvious at the time. I think one of the reasons people found Git to be very hard to use was that most people who started without using Git, were coming from a background of something CVS like. And the Git mindset, I came at it from a file system person’s standpoint, where I had this disdain and almost hatred of most source control management projects.

So I was not at all interested in maintaining the status quo. And like the biggest issue for me—well, there were two huge issues. One was performance—back then I still applied a lot of patches, which I mean, Git has made almost go away because now I just merge other people’s code.

But for me, one of the goals was that I could apply a patch series in basically half a minute, even when it was like 50, 100 patches.

**You shouldn’t need a coffee to…**

Exactly. And that was important to me because it’s actually a quality-of-life thing. It’s one of those things where if things are just instant, some mistake happens, you see the result immediately and you just go on and you fix it. And some of the other projects I had been looking at took like half a minute per patch, which was not acceptable to me. And that was because the kernel is a very large project and a lot of these SCMs were not designed to be scalable.

> “And that was important to me because **it’s actually a quality-of-life thing.”**

So that was one of the issues. But one of the issues really was I knew I needed it to be distributed, but it needed to be really, really stable. And people kind of think that using the SHA-1 hashes was a huge mistake. But to me, SHA-1 hashes were never about the security. It was about finding corruption.

Because we’d actually had some of that during the BitKeeper things, where BitKeeper used CRCs and MD5s, right, but didn’t use it for everything. So one of the early designs for me was absolutely everything was protected by a really good hash.

And that kind of drove the whole project. having two or three really fundamental design ideas which is why at a low level it is actually fairly simple right and then the complexities are in the details and the user interfaces and in all the things it has to be able to do because everybody wants it to do crazy things. But having a low level design that has a few core concepts made it easier to write and much easier to think and also to some degree explain to people what the ideas are.

And I kind of compare it to Unix. Unix has like a core philosophy of everything is a process, everything is a file, you pipe things between things. And then the reality is it’s not actually simple. I mean, there’s the simple concepts that underlie the philosophy, but then all the details are very complicated.

And I think that’s what made me appreciate Unix in the first place. And I think Git has some of the same kind of, there’s a fundamental core simplicity to the design and then there’s the complexity of implementation.

**There’s a through line from Unix into the way that Git was designed.**

Yes.

**You mentioned SHA-1. One of the things that I think about in this sort of week or two where you were developing the first version of Git is you made a lot of decisions that have sort of stuck with us.**

Yeah.

**Were there any, including SHA-1 or not, that you regretted or wish you had done differently?**

Well, I mean, SHA-1 I regret in the sense that I think it caused a lot of pointless churn with the whole trying to support SHA-256 as well as SHA-1. And I understand why it happened, but I do think it was mostly pointless.

I don’t think there was a huge, real need for it, but people were worried, so it was short. So I think there’s a lot of wasted effort there. There’s a number of other small issues. I think I made a mistake in how the index file entries are sorted. I think there’s these stupid details that made things harder than they should be.

But at the same time, many of those things could be fixed, but they’re small enough. It doesn’t really matter. All the complexities are elsewhere in the end.

**So it sounds like you have few regrets. I think that’s good. Were there any moments where you weren’t sure that what you were trying to achieve was going to work or come together or be usable? Or did you already have a pretty clear idea?**

I had a clear idea of the initial stages but I wasn’t sure how it would work in the long run. So honestly, after the first week, I had something that was good for applying patches, but not so much for everything else. I had the basics for doing merges, and the data structures were in place for that, but it actually took, I think it took an additional week before I did my first merge.

There were a number of things where I had kind of the big picture and result in mind, but I wasn’t sure if I’d get there. Yeah, the first steps, I mean the first week or two, I mean, you can go and look at the code—and people have—and it is not complicated code.

**No.**

It’s—I think the first version was 10,000 lines or something.

**You can more or less read it in a single sitting.**

Yeah, and it’s fairly straightforward and doesn’t do a lot of error checking and stuff like that. It’s really a, “Let’s get this working because I have another project that I consider to be more important than I need to get back to.” It really was. I will hit, I mean, and it happened where I would hit issues that required me to do some changes.

“There were a number of things where I had kind of the big picture and result in mind, but I wasn’t sure if I’d get there.”

The first version—you can tell it’s not, I think we ended up doing a backwards incompatible object store transfer at one point. At least `fsck` complains about some of the old objects we had because I changed the data format.

**I didn’t know where that came from.**

Yeah, no. So there were things that were… the first version just was not doing everything it needed to do.

And I forget if I actually did a conversion or not. I may not have ever needed to convert. And we just have a few warnings for like a few objects in the kernel where `fsck` will say, “Hey, this is an old, no longer supported format.” Kind of thing. But on the other, on the whole, it really worked, I mean, surprisingly well.

The big issue was always people’s acceptance of it.

**Right.**

And that took a long time.

“But on the other, on the whole, it really worked, I mean, surprisingly well.”

**Well, we talked a little bit about how sort of merging was put in place, but not functional until, you know, maybe week two or week three. What were the other sort of features that you left out of the initial version that you later realized were actually quite essential to the project?**

Well, it wasn’t so much later realized. It was stuff that I didn’t care about, but I knew that if this is going to go anywhere, somebody else will. I mean, the first week when I was using it for the kernel, I was literally using the raw, what are now called plumbing commands by hand.

**Of course.**

Because there was no so-called porcelain. There was nothing above that to make it usable. So to make a commit, you’d do these very arcane things.

**Set your index, `commit-tree`.**

Yeah, `commit-tree`, write, and that just returns an SHA that you by hand just write into the head file and that was it.

**Did `hash-object` exist in the first version?**

I think that was one of the first binaries that I had where I could just check that I could hash everything by hand and it would return the hash to standard out, then you could do whatever you wanted to it. But it was like the early porcelain was me scripting shell scripts around these very hard to use things.

And honestly, it wasn’t easy to use even with my shell scripts.

But to be fair, the first initial target audience for this were pretty hardcore kernel people who had been using BitKeeper. They at least knew a lot of the concepts I was aiming for. People picked it up.

I think I had… it didn’t take that long before some other kernel developers started actually using it. I was actually surprised by how quickly some source control people started coming in. And I started getting patches from the outside within days of making the first Git version public.

**So we’ve talked a lot about the first couple of weeks with Git. I want to move forward a bit. You made the decision to hand off maintainership to Junio pretty early on in the project. I wonder if you could tell me a little bit about what it’s been like to sort of watch him run the project and really watch the community interact with it at a little bit of a distance after all these years?**

I mean, to be honest, I maintained Git for like three or four months. I think I handed it off in August or something like that.

And when I handed it off, I truly just handed it off. I was like, I’m still around. I was still reading the Git mailing list, which I don’t do anymore. Junio wanted to make sure that if he asked me anything, I’d be okay.

But at the same time, I was like, this is not what I want to do. I mean, this is… I still feel silly. My oldest daughter went off to college, and two months later, she sends this text to me and says that I’m more well known at the computer science lab for Git than for Linux because they actually use Git for everything there. And I was like, Git was never a big thing for me. Git was a—I need to get this done to do the kernel. And it’s kind of ridiculous that, yes, I used four months of my life maintaining it.

But now, at the 20 years later, yes, you should definitely talk to Junio, not to me because he’s been doing a great job and I’m very happy it worked out so well. But to be honest I’ll take credit for having worked with people on the internet for long enough that I was like—during the four months I was maintaining Git, I was pretty good at picking up who has got the good taste to be a good maintainer.

> My oldest daughter went off to college, and two months later, she sends this text to me and says that **I’m more well known at the computer science lab for Git than for Linux** because they actually use Git for everything there.

**That’s what it’s about—taste for you.**

For me, it’s hard to describe. You can see it in patches, you can see it in how they react to other people’s code, how they think, kind of things. Junio actually came—he was not the first person in the project, but he was one of the early ones that was around from pretty much week one after I had made it public.

So he was one of the early persons—but it wasn’t like you’re the first one, tag you’re it. It was more like okay, I have now seen this person work for three months and I don’t want to maintain this project. I will ask him if he wants to be the maintainer. I think he was a bit nervous at first, but it really has been working out.

**Yeah he’s certainly run the project very admirably in the…**

Yeah, I mean, so taste is to me very important, but practically speaking, the fact that you stick around with a project for 20 years, that’s the even more important part, right? And he has.

**I think he’s knowledgeable about almost every area of the tree to a surprising degree.**

**Okay, so we’ve talked a lot about early Git. I want to talk a little bit about sort of the middle period of Git maybe, or maybe even the period we’re in now.**

**One of the things that I find so interesting about the tool, given how ubiquitous it’s become, it’s clearly been effective at aiding the kernel’s development, but it’s also been really effective for university students writing little class projects on their laptops. What do you think was unique about Git that made it effective at sort of both extremes of the software engineering spectrum?**

So the distributed nature really ends up making so many things so easy and that was one big part that set Git apart from pretty much all SCMs before, was… I mean there had been distributed SCMs, but there had, as far as I know, never been something where it was like the number one design goal—I mean along with the other number one design goals—where it means that you can work with Git purely locally and then later if you want to make it available in any other place it’s so easy.

And that’s very different from say CVS where you have to set up this kind of repository and if you ever want to move it anywhere else it’s just very very painful and you can’t share it with somebody else without losing track of it.

Or there’s always going to be one special repository when you’re using a traditional SCM and the fact that Git didn’t do that, and very much by design didn’t do that, I mean that’s what made services like GitHub trivial. I mean I’m trivializing GitHub because I realized there’s a lot of work in making all the infrastructure around Git, but at the same time the basic Git hosting site is basically nothing because the whole design of Git is designed around making it easy to copy and every repository is the same and equal.

And I think that ended up being what made it so easy to then use as an individual developer. When you make a new Git repository, it’s not a big deal. It’s like you do in Git and you’re done. And you don’t need to set up any infrastructure and you don’t need to do any of the stuff that you traditionally needed to do with an SCM. And then if that project ever grows to be something where you decide, “oh, maybe I want other people to work with it,” that works too. And again, you don’t have to do anything about it. You just push it to GitHub and again, you’re done.

That was something I very much wanted. I didn’t realize how many other people wanted it, too. I thought people were happy with CVS and SVN. Well, I didn’t really think that, but I thought they were sufficient for most people—let’s put it that way.

**So we’ve talked a little bit about just now sort of how Git has applicability on both ends of the software engineering extremes. I’ve lived my whole life with version control as part of software development, and one of the things I’m curious about is how you see its role in shaping how software development gets done today.**

That’s too big of a question for me—I don’t know. It wasn’t why I wrote Git.

I wrote it for my own issues. I think GitHub and the other hosting services have made it clear how easy it is now to make all these random small projects in ways that it didn’t used to be. And that has resulted in a lot of dead projects too. You find these one-off things where somebody did something and left it behind and it’s still there.

But does that really change how software development is done in the big picture? I don’t know. I mean, it changes the details. It makes collaboration easier to some degree. It makes it easier to do these throwaway projects. And if they don’t work, they don’t work. And if they do work, now you can work together with other people. But I’m not sure it changed anything fundamentally in software development.

“It makes collaboration easier to some degree.”

**Moving ahead a little bit, you know, modern software development has never been changing faster than it is today.**

Are you going to say the AI word?

**I’m not going to say the AI word, unless you want me to.**

No, no, no.

**What are some of the areas of the tool that you think have evolved or maybe still need to evolve to continue to support the sort of new and demanding workflows that people are using it for?**

I’d love to see more bug tracking stuff. I mean, everybody is doing that. I mean, there are, whether you call it bug tracking or issues or whatever you want to call it, they’re all—I’d love to see that be more unified. Because right now it’s very fragmented where every single hosting site does their own version of it.

And I understand why they do it. A, there is no kind of standard good base. And B, it’s also a way to do the value add and keep people in that ecosystem even when Git itself means that it’s really easy to move the code.

But I do wish there was a more unified thing where bug tracking and issues in general would be something that would be more shared among the hosting sites.

**You mentioned earlier that you were, maybe not pretty quick, but it’s at least been a while since you sort of regularly follow the mailing list.**

Yeah.

**In fact, it’s been a little bit of time since you even committed to the project. I think by my count, it’s—August of 2022 was the last time…**

Yeah, I have a few experimental patches in my tree that I just keep around. So these days I do a pull of the Git sources and I have, I think, four or five patches that I use myself. And I think I’ve posted a couple of them to the Git mailing list, but they’re not very important. They’re like details that tend to be very specific to my workflow.

But honestly, I mean, this is true of the Linux kernel, too. I’ve been doing Linux for 35 years, and it did everything I needed in the first year—right? And the thing that keeps me going on the kernel side is, A, hardware keeps evolving, and a kernel needs to evolve with that, of course. But B, it’s all the needs of other people. Never in my life would I need all of the features that the kernel does. But I’m interested in kernels, and I’m still doing that 35 years later.

When it came to Git, it was like Git did what I needed within the first year. In fact, mostly within the first few months. And when it did what I needed, I lost interest. Because when it comes to kernels, I’m really interested in how they work, and this is what I do. But when it comes to SCMs, it’s like—yeah, I’m not at all interested.

> “When it came to Git, it was like **Git did what I needed within the first year**. In fact, mostly within the first few months.”

**Have there been any features that you’ve followed in the past, you know, handful of years from the project that you found interesting?**

I liked how the merge strategies got slightly smarter. I liked how some of the scripts were finally rewritten in C just to make them faster, because I saw that. Even though I don’t apply, like, 100 patch series anymore, I do end up doing things like rebasing for test trees and stuff like that and having some of the performance improvements.

But then, I mean, those are fairly small implementation details in the end. They’re not the kind of big changes that, I mean—I think the biggest change that I was still tracking a few years ago was all the multiple hashes thing, which really looks very painful to me.

**Have there been any tools in the sort of ecosystem that you’ve used alongside? I mean, I’m a huge `tig` user myself. I don’t know if you’ve ever used this.**

I never—no, even early on when we had, like when Git was really hard to use and they were like these add-on UIs, the only wrapper around Git I ever used was `gitk`. And that was obviously integrated into Git fairly quickly, right? But I still use the entire command language. I don’t use any of the editor integration stuff. I don’t do any of that because my editor is too stupid to integrate with anything, much less Git.

So when I say, I mean, I occasionally do statistics on my Git history usage just because I’m like, what commands do I use? And it turns out I use five Git commands. And `git merge` and `git blame` and `git log` are three of them pretty much. So, I’m a very casual user of Git in that sense.

**I have to ask about what the other two are.**

I mean obviously `git commit` and `git pull`. I did this top five thing at some point and it may have changed, but there’s not a lot of—I do have a few scripts and then do like use `git rev-list` and go reload like due statistics for the project but then they…

**In terms of your interaction with the project, what do you feel like have been some of the features in the project either from early on or in the time since that maybe haven’t gotten the appreciation they deserve?**

I mean Git has gotten so much more appreciation than it deserves. But that’s the reverse of what I would ask me. A big thing for me was when people actually started appreciating what Git could do instead of complaining about how different it was.

And that, I mean, that was several years after the initial Git. I think it was these strange web developers who started using Git in a big way. It’s like Ruby on Rails, I think. Which I had no idea, I still don’t know what Ruby even is. But the Ruby on Rails people started using Git sometime in 2008, something like this.

It was strange because it brought in a completely new kind of Git user—at least one that I hadn’t seen before. It must have existed in the background, it just made it very obvious that suddenly you had all these young people who had never used SCM in their life before and Git was the first thing they ever used and it was what the project they were using was using, so it was kind of the default thing.

And I think it changed the dynamics. When you didn’t have these old timers who had used a very different SCM their whole life, and suddenly you had young people who had never seen anything else and appreciated it, and instead of saying, “Git is so hard,” I started seeing these people who were complaining about “How do I do this when this old project is in CVS?” So, that was funny.

But yeah, no. The fact that people are appreciating Git, I mean, way more than I ever thought. Especially considering the first few years when I got a lot of hate for it.

**Really?**

Oh, the complaints kept coming.

**Tell me about it.**

Oh, I mean, it’s more like I can’t point to details. You’d have to Google it. But the number of people who sent me, “Why does it do this?” And the flame wars over my choice of names. For example, I didn’t have `git status`, which actually is one of the commands I use fairly regularly now.

**It’s in the top five?**

It’s probably not in the top five, but it’s still something fairly common. I don’t think I’d ever used it with CVS because it was so slow.

And people had all these expectations. So I just remember the first few years, the complaints about why the names of the subcommands are different for no good reason. And the main reason was I just didn’t like CVS very much, so I did things differently on purpose sometimes.

And the shift literally between 2007 and 2010—those years, when people went from complaining about how hard Git was to use to really appreciating some of the power of Git, was interesting to me.

**I want to spend maybe just a moment thinking about the future of the project. In your mind, what are the biggest challenges that Git either is facing or will face?**

I don’t even know. I mean, it has just been so much more successful than I ever… I mean, the statistics are insane. It went from use for the kernel and a couple of other projects to being fairly popular to now being like 98% of the SCMs used. I mean, that’s a number I saw in some report from last year.

So, I mean, it’s—I don’t know how true that is, but it’s like big. And in that sense, I wouldn’t worry about challenges because I think SCMs, there is a very strong network effect. And that’s probably why, once it took off, it took off in a big way. Just when every other project is using Git, by default, all the new projects will use Git, too. Because the pain of having two different SCMs for two different projects to work on is just not worth it.

So I would not see that as a challenge for Git as much as I would see it as a challenge for anybody else who thinks they have something better. And honestly, because Git does everything that I need, the challenges would likely come from new users.

I mean, we saw some of that. We saw some of that with people who used Git in ways that explicitly were things I consider to be the wrong approach. Like Microsoft, the monorepo for everything, which showed scalability issues. I’m not saying Microsoft was wrong to do that. I’m saying this is literally what Git was not designed to do.

I assume most of those problems have been solved because I’m not seeing any complaints, but at the same time I’m not following the Git mailing list as much as I used to.

**Well, it’s very kind. That’s most of what I work on, so I appreciate it.**

Okay. But I mean, also, people who—I don’t know, I don’t even know if the large file issue is considered to be solved. If you want to put a DVD image in Git, that was like, why would you ever want to do that?

But, I mean, that’s the challenge. When Git is everywhere, you find all these people who do strange things that you would never imagine—that I didn’t imagine and that I consider to be actively wrong.

But hey, I mean, that’s a personal opinion. Clearly other people