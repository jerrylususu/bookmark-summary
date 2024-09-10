Title: Why GitHub Actually Won

URL Source: https://blog.gitbutler.com/why-github-actually-won/

Published Time: 2024-09-09T15:40:08.000Z

Markdown Content:
A few days ago, a video produced by [@t3dotgg](https://www.youtube.com/@t3dotgg?ref=blog.gitbutler.com) was posted to his very popular YouTube channel where he reviews an article written by the Graphite team titled “[How](https://graphite.dev/blog/github-monopoly-on-code-hosting?ref=blog.gitbutler.com) [GitHub replaced SourceForge as the dominant code hosting platform](https://graphite.dev/blog/github-monopoly-on-code-hosting?ref=blog.gitbutler.com)”.

Theo’s title was a little more succinct, “[Why](https://youtu.be/4FNNlMtPS-0?ref=blog.gitbutler.com) [GitHub Won](https://youtu.be/4FNNlMtPS-0?ref=blog.gitbutler.com)”.

Being a cofounder of [GitHub](https://github.com/?ref=blog.gitbutler.com), I found Greg’s article and Theo’s subsequent commentary fun, but figured that it might be interesting to write up my own take on the reasoning behind the rise and dominance of GitHub and perhaps correct a few things that were not quite right from their outside analysis.

Being at the very center of phenomena like this can certainly leave you with blind spots, but unlike these youngsters, I was actually there. Hell, I [wrote the book](https://git-scm.com/book/en/v2?ref=blog.gitbutler.com).

![Image 1](https://paper-attachments.dropboxusercontent.com/s_0A1F620D7ECC4C89A98039CC93A097D615018963BB0593AA9CBBB3ED31CAB20D_1725520720130_CleanShot+2024-09-05+at+09.18.162x.png)

Unboxing of the first batch of the first edition of my Pro Git book, 2009

So here’s an _insider’s_ take on why GitHub won.

TLDR
----

If you want a very short read, here is the quick version of why _I_ believe GitHub won and why you’re probably using the site to this day.

I can boil it down to **exactly two reasons** that happened to resonate with each other at the perfect frequency.

1.  GitHub started at the right time
2.  GitHub had good taste

All four GitHub cofounders had flops both before and after GitHub. Chris and PJ couldn’t quite make [FamSpam](https://web.archive.org/web/20081202124457/http://famspam.com/) work before GitHub, Tom and I couldn’t quite make [Chatterbug](https://chatterbug.com/en/?ref=blog.gitbutler.com) explode after GitHub. I think both of these ventures had good taste and great product, but it wasn’t the right place or time or market or whatever for them to become GitHub level.

At the time GitHub was starting, [distributed](https://en.wikipedia.org/wiki/GNU_arch?ref=blog.gitbutler.com) [open](https://web.archive.org/web/20230506175749/http://bazaar.canonical.com/en/) [source](https://en.wikipedia.org/wiki/Monotone_/(software/)?ref=blog.gitbutler.com) [version](https://en.wikipedia.org/wiki/Mercurial?ref=blog.gitbutler.com) [control](https://en.wikipedia.org/wiki/Darcs?ref=blog.gitbutler.com) [tools](https://git-scm.com/?ref=blog.gitbutler.com) were starting to get useful, solid and adopted and there was nobody around to seriously (much less commercially) host them. Big hosts didn’t care and smaller players weren’t serious.

Furthermore, the players (Sourceforge, Google Code, etc) who eventually did care, after seeing Git and GitHub rising in popularity, simply had no taste. They could never have competed with a developer tools company whose cofounders were all product-focused open source software developers.

We cared about the developer experience and had the creativity to throw away assumptions about what it was supposed to be and build how we wanted to work. Everyone else tried to build what they thought they could sell to advertisers or CTOs.

**That’s why GitHub won.**

Now that that’s out of the way, if you’re interested in some storytelling, let me lead you down the path of how some of this actually unfolded from the inside.

The Environment
---------------

Let’s go back to the beginning of the story.

I’ll dig a little more into the “GitHub started at the right time” theme from the point of view of a software developer circa 2005. This is when Git had it’s [first commit](https://github.com/git/git/commit/e83c5163316f89bfbde7d9ab23ca2e25604af290?ref=blog.gitbutler.com) by Linus and Mercurial had it’s [first commit](https://repo.mercurial-scm.org/hg/rev/9117c6561b0b?ref=blog.gitbutler.com) by Olivia.

![Image 2](https://paper-attachments.dropboxusercontent.com/s_0A1F620D7ECC4C89A98039CC93A097D615018963BB0593AA9CBBB3ED31CAB20D_1725516213021_CleanShot+2024-08-28+at+09.40.062x.png)

My Windows Vista, Ubuntu and Mac Tiger desktops, circa a stupid long time ago.

What was it like to develop software almost 20 years ago and how was this an environment where Git could win over people and a GitHub could be born?

![Image 3](https://paper-attachments.dropboxusercontent.com/s_0A1F620D7ECC4C89A98039CC93A097D615018963BB0593AA9CBBB3ED31CAB20D_1724835623733_TigerDesk.png)

Mac OS Tiger, released in 2005. If you were using a Mac, it looked something like this.

If you were a software developer in 2005, you were probably (hopefully) using a centralized version control system like Subversion. I professionally used [RCS](https://en.wikipedia.org/wiki/Revision_Control_System?ref=blog.gitbutler.com), [CVS](https://en.wikipedia.org/wiki/Concurrent_Versions_System?ref=blog.gitbutler.com), [Subversion](https://subversion.apache.org/?ref=blog.gitbutler.com) and [Perforce](https://www.perforce.com/perforce/doc.051/manuals/p4guide/03_quickstart.html?ref=blog.gitbutler.com#1043460) before Git came along. Hell, I was actually in a company that FTP'd it's PHP files directly to the production server.

Now, if you were working on proprietary commercial software, centralized version control systems like SVN honestly wasn’t the most horrible thing. It was pretty simple to checkout, make changes, check back in. Branching and merging completely sucked but in a lot of situations it could basically be avoided (I’m not sure I ever really used branching in Subversion or Perforce).

People probably complain more about Git today than they did about SVN back then, to be honest - the user interface and mental model is arguably simpler than in Git.

![Image 4](https://paper-attachments.dropboxusercontent.com/s_0A1F620D7ECC4C89A98039CC93A097D615018963BB0593AA9CBBB3ED31CAB20D_1724837536935_CleanShot+2024-08-28+at+11.27.542x.png)

Perforce 2005.1 visual client. I spent a loooot of time hating this software.

The big problem that I think started coming to a head around this time was not in the world of professional development within closed, trusted teams. The big problem was within the growing world of open source.

You see, open source was [barely a thing before this time](https://blog.gitbutler.com/the-future-of-open-source/#a-quick-history-of-open-source), especially compared to today. Most of you kids probably don’t remember a time where there weren’t millions of open source projects around, but the phrase was only _coined_ in 1998.

To get a sense of scale, Dirk Riehle [published a paper in 2008](https://dirkriehle.com/publications/2008-selected/the-total-growth-of-open-source/comment-page-1/?ref=blog.gitbutler.com) analyzing global open source project trends and they estimated that there were a _total_ of 18,000 active open source projects in the world at that time - in 2005, certainly far fewer.

![Image 5](https://paper-attachments.dropboxusercontent.com/s_0A1F620D7ECC4C89A98039CC93A097D615018963BB0593AA9CBBB3ED31CAB20D_1724838149032_total-growth-figure-5.jpg)

Total open source projects. From “The Total Growth of Open Source”, 2008, published by Amit Deshpande and Dirk Riehle

To put this in perspective, there are over **280 _million_** public repositories on GitHub alone today.

So, why did open source help usher in the era of Git and GitHub?

Because open source was growing fast and centralized version control systems were particularly bad at open contribution strategies. That is, you couldn’t easily share a project publicly and then take contributions back into it in a simple manner.

Contributing to Open Source in 2005
-----------------------------------

Really, how bad could it have been?

If you would like to see me talk about what open source contributing was like via my AWS Tokyo keynote 10 years ago, check it out and then you can skip the next few paragraphs:

Me talking about how we used to contribute to open source before GitHub. I recommend watching it at 1.5x, I had to speak slowly for the translators.

Basically, you could make your Subversion server read only for unauthenticated users, this is generally how you hosted an open source project (or you put a tarball somewhere occasionally).

If you wanted to contribute, essentially you had to:

*   checkout the latest version
*   make your changes
*   generate a patch file with GNU diff
*   upload that patch file to a ticketing system or email list used by the project

Then the maintainer needed to:

*   pull down that patch file
*   apply it to their project to see if it
    *   applied cleanly
    *   worked properly
*   either submit feedback, make changes, or commit the change

There are still artifacts of this around the internet. I used the [Trac](https://trac.edgewall.org/?ref=blog.gitbutler.com) project at some point for this type of project, you can still see their [Submitting Patches guide](https://trac.edgewall.org/wiki/TracDev/SubmittingPatches?ref=blog.gitbutler.com) and an example of how a [change would be suggested](https://trac.edgewall.org/ticket/2553?ref=blog.gitbutler.com#no1).

**It was a goddamn nightmare.**

The [Rails project](https://rails.lighthouseapp.com/projects/8994/tickets/300-unsigned-integers-for-mysql?ref=blog.gitbutler.com), as well as my friends (and future GitHub cofounders) at [Err](http://errtheblog.com/?ref=blog.gitbutler.com) used a similar ticketing system called [Lighthouse](https://err.lighthouseapp.com/projects/466/home?ref=blog.gitbutler.com) (which is mind-blowingly still up) and one of my earliest open source projects was a command line tool called [git-lighthouse](https://github.com/schacon/git-lighthouse?ref=blog.gitbutler.com) that could simplify the process of pulling down and applying attached patches from tickets you wanted to test out.

![Image 6](https://paper-attachments.dropboxusercontent.com/s_0A1F620D7ECC4C89A98039CC93A097D615018963BB0593AA9CBBB3ED31CAB20D_1724842653665_CleanShot+2024-08-28+at+12.56.282x.png)

[Here](https://rails.lighthouseapp.com/projects/8994/tickets/6098-activerecord-fixture-class?ref=blog.gitbutler.com) is an example of 3 different versions of a patch that were submitted to the Rails project in the early days.

This process sucked enough that when something came around that simplified it, it was quickly embraced. And that something was GitHub. But first, we needed a Git.

The Rise of Git
---------------

Git actually started from the fact that Linus Torvalds really liked an (at the time) commercial version control system called [BitKeeper](https://www.bitkeeper.org/?ref=blog.gitbutler.com). It was actually built specifically to help simplify the existing kernel development process.

If it had been open source or had better licensing terms, there probably would have been no Git or GitHub.

However, what happened instead was that one of the Linux developers reverse engineered the protocol, breaking the licensing terms, and BitKeeper and Linus determined that the spat that followed was untenable and they mutually decided to part ways.

So Linus took some of the concepts that BitKeeper opened his eyes to, threw together the simplest thing he thought would solve his problems with those principles in mind, and called the new project Git, the “[information](https://github.com/git/git/commit/e83c5163316f89bfbde7d9ab23ca2e25604af290?ref=blog.gitbutler.com) [manager from hell](https://github.com/git/git/commit/e83c5163316f89bfbde7d9ab23ca2e25604af290?ref=blog.gitbutler.com)”.

It was fairly quickly embraced by several people in the Linux community and slowly grew into an actual, sort of, version control system.

There are several reasons why Git felt awesome at the time. They were:

*   branching and merging were dreams rather than nightmares
*   it was stupendously fast
*   permissions were vastly simpler

In the early days of Git, I would do talks where I would just go on stage, create a few branches, commit changes into them, switch between them and then merge them together, all in 60 seconds. I would _literally_ see peoples jaw’s drop. Some of them would think I was faking the demo.

I just cannot tell you how magical it felt in 2006 to be able to switch and merge contexts that fast and easily. In Subversion this was a total nightmare.

![Image 7](https://paper-attachments.dropboxusercontent.com/s_0A1F620D7ECC4C89A98039CC93A097D615018963BB0593AA9CBBB3ED31CAB20D_1724843142271_CleanShot+2024-08-28+at+13.05.322x.png)

Baby Scott talking about Git at RailsConf 2008

Not having to go over a network to negotiate a commit with a central server was also incredible. It felt like a rocket ship. Everything was _so fast_.

And probably most importantly, you could fork the repository incredibly easily, which meant that you could host your own copy of a repository and have your own write access and push changes there that other people could pull down into _their_ fork. The Linux project started doing this early on - for larger changes, they could send a request to pull changes from a hosted fork and Linus could very easily do so.

In fact, if you’re wondering where the terminology “Pull Request” came from, this is it. Git has a [`git request-pull`](https://git-scm.com/docs/git-request-pull?ref=blog.gitbutler.com) command that would format an email for sending to a mailing list to help make this process simpler. When GitHub added the ability to basically generate this same type of message, we decided that a request to pull should be called a Pull Request. _(A little more backstory on that_ [_here_](https://x.com/chacon/status/1823416898379505749?ref=blog.gitbutler.com) _if you’re curious)_

Some people think that developers liked Git because it was distributed and you got the whole history when you cloned, which meant you could share locally, etc. I disagree. I don’t think almost anybody really cared about any of that. Distributed was cool because you could do operations _fast_ and you could host your own full, writeable fork which made permissions much simpler.

It was cool because contributing went from a problem of who had permission to push into the simplicity of who had something interesting to pull.

And of course, this last point led directly to GitHub.

The Rise of GitHub
------------------

Late last year, I interviewed my GitHub cofounder Tom, and among the things we discussed, he told the story of how he got the initial idea of working on GitHub.

Essentially, when he was working at [Powerset](https://en.wikipedia.org/wiki/Powerset_/(company/)?ref=blog.gitbutler.com), Tom’s team started using Git internally. However, it was a pain in the ass to add other team members to the internal server, because Git’s main protocol was over SSH, which means you need a user with ssh privileges on the machine. For everyone. It was difficult and, for most of the team, not worth it. This spawned the concept for him of making this process as easy as possible.

Git is awesome, Git hosting is a pain in the ass. This is why Tom started working on GitHub.

![Image 8](https://paper-attachments.dropboxusercontent.com/s_0A1F620D7ECC4C89A98039CC93A097D615018963BB0593AA9CBBB3ED31CAB20D_1724843527071_CleanShot+2024-08-28+at+13.11.502x.png)

Why GitHub was started. To ease ass pain.

I went through my old emails to see if I could find the first time I heard about Tom’s “GitHub” project, and it was this email from Chris responding to a [Git screencast](https://youtu.be/7x98k_IQlcY?ref=blog.gitbutler.com) I made in late 2007.

![Image 9](https://paper-attachments.dropboxusercontent.com/s_0A1F620D7ECC4C89A98039CC93A097D615018963BB0593AA9CBBB3ED31CAB20D_1724843800367_CleanShot+2024-08-28+at+13.16.272x.png)

It was still a secret side project between the two of them at that point (_also Chris… lower-case ‘h’?_) and it’s when I started chatting with Chris and Tom about the [Git/Ruby libraries](https://github.com/mojombo/grit?ref=blog.gitbutler.com) that ran the site, and [eventually how](https://github.blog/news-insights/the-library/supercharged-ruby-git/?ref=blog.gitbutler.com) I wiggled my way into the project and company.

There are a few interesting things about this pitch.

The first is that they compared it to the only other real public Git hosting site, [repo.or.cz](https://repo.or.cz/?ref=blog.gitbutler.com) (which also miraculously is still running, if you want to see what the state of Git hosting was pre-GitHub), but made a _crucial_ innovation over that site and every other hosting service like it, which is to make it user-centric rather than project-centric. Before this, if you wanted to host something on Sourceforge or whatever, you needed to grab the name. With GitHub, you can make any project you want named anything you want because it’s namespaced to _your user._

The second was that they focused on a pull model rather than a push model (basically the permissions thing I talked about before).

The third is that “not ugly” was a core feature. _GitHub had taste._

Git Wins
--------

This is why Git was cool and why GitHub was started to make using it easier, but the question is, why did _Git_ win? Lots of distributed systems sprang up during this time. Mercurial was similar in a lot of ways and better in many. Why did Git come out on top in the great DVCS war?

I think the answer there was “PR”.

And there are two big PR gorillas fighting it out for the “_why did **Git** win”_ answer. The first was Linux and by extension, Linus. The other was GitHub, and specifically the Rails community.

Maybe it was Linus/Linux
------------------------

The Linux project using Git and Linus having started the project gave **instant credibility** to it.

Everyone knew Linux, everyone knew Linus. If he made an amazing operating system that everyone uses _(at least for their servers, next year is the year of Linux on the desktop)_, he can certainly make a next-level version control system. And even if it’s difficult to use, that just means he’s smarter than us and we should try harder, right?

This video is one of the first talks about Git online, circa 2007. It's Linus talking about Git and distributed version control systems, then a brand new concept, at the Google campus.

It came out in between when I started using Git (late 2005) and when I started at GitHub (mid 2008). I watched it several times, as did millions of people. Who doesn’t like listening to the Linux guy say “CVS is the dumbest shit that has ever been thought of, and everyone who disagrees is ugly and stupid”? At _Google_!

It’s just _great_ PR.

Beyond that, if you conflate Linux and Linus, which most people do, there is an argument that Linux itself pushed Git adoption indirectly through Android.

This is where I really don’t know how much impact my own efforts or GitHub’s efforts had compared to this big, quiet, behind-the-scenes side effect of Android becoming a thing at exactly the same time. Or even, my personal impact in either or both of these fronts, doing Git talks and corporate training for years.

In early September 2008, right as Android 1.0 was being released (like 2 weeks after this email, but before I did the training), [Shawn Pearce](https://git.github.io/rev_news/2017/08/16/edition-30/?ref=blog.gitbutler.com#developer-spotlight-shawn-pearce), an early super hero of the Git ecosystem, wrote me this email asking me to help train the Google Android team on Git.

![Image 10](https://paper-attachments.dropboxusercontent.com/s_0A1F620D7ECC4C89A98039CC93A097D615018963BB0593AA9CBBB3ED31CAB20D_1724868390458_CleanShot+2024-08-28+at+20.05.372x.png)

It’s difficult to determine what impact Android had in corporate Git adoption, but it certainly wasn’t zero. While the Google/Android team was the first that I did corporate training for under the GitHub banner, I also eventually did Git training for engineering teams at Motorola, Qualcomm, Ericsson and Broadcom, just to name the _telecoms_. And that was before we hired a team to do this for us full time.

Linus pushed Git with his broad ranging brand of superstar nerd PR that Mercurial never got, but Android furthermore pushed Git uniquely, via it’s dependance from the Linux kernel, into massive companies out of pure practicality that also otherwise never would have happened for at least another decade.

Maybe it was GitHub
-------------------

There is also, and I must say this with a grain of hopeful humility, a possibility that _GitHub_ was the determining factor in the eventual dominance of Git over Mercurial.

GitHub had the incredible luck to have an amazingly supportive and hip community that embraced us right out of the gate, namely the Ruby community. Within months, _everyone_ in the Ruby community put their stuff on GitHub. Rails was the hot shit at that time, it was cooler than PHP, JS frameworks weren’t really around, there was no Node, etc. So everyone was paying attention to what the hip cats in the Ruby community were doing, they were the bleeding edge of cool development in the software world. And they were using GitHub.

And it’s not just me, Linus _himself_ also recently said that from his perspective, the Ruby community unexpectedly made Git explode overnight. He doesn’t credit GitHub for that by name, but I think it’s impossible for anyone to argue that the Ruby community didn’t adopt Git in a very large part due to us.

By the transitive property and some speculation, I’ll make the claim that **Linus in fact thinks that GitHub is the reason Git won**. 😀

“…the Ruby people, strange people, started using Git and suddenly it just exploded…”

Of course, the Ruby community adopting GitHub wasn’t random.

I remember all of us - Chris, Tom, PJ and myself - sitting at tables at Ruby conferences with all the guys in the early Ruby community, showing them GitHub, selling them on Git, doing talks, etc. We were all speaking at the same conferences, we all drank beers together after Ruby meetups in SF. These were the guys who started Rails, Heroku, Twitter, jQuery, you name it.

It’s not that we were _selling_ it, it’s that we were all sharing what we were passionate about. There was a high level of trust in this community, the GitHub founders were a deep and authentic part of it, and we all tried each others stuff and supported each other.

![Image 11](https://paper-attachments.dropboxusercontent.com/s_0A1F620D7ECC4C89A98039CC93A097D615018963BB0593AA9CBBB3ED31CAB20D_1725465770267_CleanShot+2024-08-28+at+08.52.092x.png)

Me and PJ at Scotland on Rails in March 2009 with a table full of amazing early Ruby peeps

The Ruby community using GitHub meant that every conference talk everywhere had a GitHub plug in it. Free advertising everywhere. This meant that as more and more projects moved to or were started on GitHub, even people who liked Mercurial had no real choice but to use Git. After a while, it probably just wasn’t worth it. GitHub’s dominance in the hosting sphere just crushed Mercurial in just the span of a few years.

In Mercurial land, there was BitBucket, which was started for Mercurial hosting and written in the Django framework, but I think we just had too much of a head start and there wasn’t enough differentiation. The Python community just didn't adopt it as aggressively as our Ruby community did.

As early as December 2008, GitHub was hosting about 27,000 public repositories where BitBucket had a little over 1,000. It became difficult to catch up.

How do I remember those numbers you might ask? Well, I had a website I put up called whygitisbetterthanx.com and this guy named Jesper emailed me to say that one of my points was incorrect, where I argued that Git has GitHub and Mercurial and Bazaar didn't have a GitHub. I rather arrogantly argued that they're not in the same league.

![Image 12](https://blog.gitbutler.com/content/images/2024/09/CleanShot-2024-09-09-at-17.30.22@2x.png)

Young Scott being a little bitchy. Sorry, Jesper.

To his credit, he never called me out on my response, which now seems real snippy of me in hindsight. But it turns out that Jesper in fact was the founder of BitBucket. Whoopsie.

A year or so later, we met up with him in Amsterdam, drank some nice whiskey together and have remained friendly ever since.

![Image 13](https://paper-attachments.dropboxusercontent.com/s_0A1F620D7ECC4C89A98039CC93A097D615018963BB0593AA9CBBB3ED31CAB20D_1724920284163_CleanShot+2024-08-28+at+08.51.162x.png)

GitHub cofounder PJ Hyett and myself with BitBucket founder Jesper Noehr (black shirt) getting a friendly competitor whiskey in Amsterdam, circa 2009 or so. Always be friends with those you compete against.

The Competitive Field Collapses
-------------------------------

In the end, whether it was GitHub that helped Git win, or Git that helped GitHub win, it was quickly over.

In 2006-2007, people were first learning about distributed version control systems and Git and Mercurial were starting to fight it out.

In 2008, GitHub launched.

In 2011, both Google Code and BitBucket added Git support, which I’ll mark as the year that the nail was in the Mercurial coffin. Git had won and GitHub was now essentially unbeatable.

Just 4 years later, in 2015, Google Code just completely gave up and shut it’s service down. In the email they sent out, they basically said “just move to GitHub”. If I remember correctly, they even reached out to us for help with the migration.

![Image 14](https://paper-attachments.dropboxusercontent.com/s_0A1F620D7ECC4C89A98039CC93A097D615018963BB0593AA9CBBB3ED31CAB20D_1724921748582_CleanShot+2024-08-29+at+10.55.182x.png)

So, Why Not Google Code?
------------------------

Of course, while BitBucket started after us and so we had a head start, there were other hosting sites that existed before us. So why didn’t _they_ win?

In early 2009, Google Code [added Mercurial support](https://arstechnica.com/information-technology/2009/04/google-code-adds-mercurial-version-control-system/?ref=blog.gitbutler.com#:~:text=Google%20has%20announced%20that%20it,more%20are%20preparing%20to%20migrate.) and Sourceforge added both Git and Mercurial support. So if these industry monsters had a _massive_ user head start _and_ had DVCS support only months after we launched, why didn’t they wipe the floor with us little guys?

Not only _little_, but also nearly _completely_ un-funded. Chris was able to put a little bit of money in to bootstrap iirc, but the rest of us were totally broke and we didn't raise any outside funding.

When Google Code launched Mercurial support, we were still 4 developers working out of cafes in South Beach with zero VC investment. We [struck deals with our buddies](https://github.blog/news-insights/the-library/rolling-with-engine-yard/?ref=blog.gitbutler.com) (May 2008) at Engine Yard for help with hosting costs because we didn’t really have the cash.

How is it possible that this tiny, unfunded team made Google Code fold in just a few years?

**Side Note: GitHub Funding**

As a side note, speaking of funding, the article I’m reacting to states _“VC investment wasn't an option for the cofounders.”_ This is _purely_ untrue.

From the very first days, we were talking to VCs. When PJ emailed me in July of 2008 to say they wanted me to join them and we should all make the leap, quit our respective jobs, and make this a full time thing instead of a side project, he explicitly said “_we've been talking to one VC in particular we like a lot and we want to raise a handful of money to do a few of things._” These were things like get an office, hire some people, etc.

It was always on the table, we could have done it at _literally_ any time. We considered and thoughtfully rejected the idea constantly over the years. We didn't really need an office. We didn't really need more people yet.

Not only that, we actually nearly rejected the idea when we were considering our [$100 million A round](https://a16z.com/announcement/github/?ref=blog.gitbutler.com) from Andreessen Horowitz, 4 years later. I remember vividly the night we all sat down for dinner at some restaurant on Folsum St in April of 2012 and argued very heatedly if we should take a capital round _at all_.

We basically had offers from [a16z](https://a16z.com/?ref=blog.gitbutler.com), [Benchmark](https://www.benchmark.com/?ref=blog.gitbutler.com), [Sequoia](https://www.sequoiacap.com/?ref=blog.gitbutler.com) and [Bessemer](https://www.bvp.com/?ref=blog.gitbutler.com) (pretty much the best VC firms on the planet) on the table and meanwhile us four assholes sat around and heatedly yelled at each other about whether or not we should tell all of them “thanks, but no thanks”. Offers that other tech entrepreneurs would probably literally have killed for.

But the point is that it wasn’t that we couldn’t have raised money, but that we _didn’t even need to_ in order to take down the entire field.

GitHub Had Taste
----------------

The original article is correct, the other hosts focused on distribution and revenue streams. We cared about developers. But it wasn’t about when they added Git, it never really mattered. [They never had any taste](https://www.youtube.com/watch?v=3KdlJlHAAbQ&ref=blog.gitbutler.com). They never cared about the developer workflow. They could have added Git at any time and I think they all still would have lost.

You can try to explain it by the features or “value adds”, but the core takeaway that is still relevant to starting a startup today is more fundamental than if we had an activity feed or profile page or whatever. The much simpler, much more fundamentally interesting thing that I think showed in everything that we did was that we **built for ourselves**. We had taste. We cared about the experience.

We were developers and we built what we wanted in order to enable how we wanted to ideally work. We were the only tool in the space built by developers for developers without PMs or accountants or CEOs trying to optimize for revenue rather than for developer experience.

In the end we won because the open source community started to converge on distributed version control and we were the only ones in the hosting space that truly cared about how developers worked at all. The only ones who questioned it, approached it from first principles, tried to make it better holistically rather than just throwing more features onto something existing in order to sell it.

So, to sum up, we won because we started at the right time and we had taste.

We were there when a new paradigm was being born and we approached the problem of helping people embrace that new paradigm with a developer experience centric approach that nobody else had the capacity for or interest in.

I guess the question is, what is the next sea change in developer workflow, and who will have good enough taste to make it explode in the same way?
