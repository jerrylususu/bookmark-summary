Title: The reality of long-term software maintenance from the maintainer's perspective

URL Source: https://www.construct.net/en/blogs/ashleys-blog-2/reality-long-term-software-1892

Published Time: 2025-02-19T10:34:45.9130000Z

Markdown Content:
The reality of long-term software maintenance - Ashley's blog
===============
The reality of long-term software maintenance from the maintainer's perspective
Upvote
15
Downvote
Blogs Next Ashley's blog Next Viewing Post 
Official iconOfficial Construct Team Post
Ashley's avatar
Ashley
19 Feb, 2025
 3,149 words
 ~13-21 mins
 37,462 visits
Not favorited
2
favourites
I was reading about a dispute involving the Linux kernel recently (which for the record I don't think either side handled well), and I realised something: very few people seem to understand the reality of maintaining large software projects in the long term. Of course non-technical people won't understand it, and likely inexperienced developers don't really understand it - but what I've noticed is even experienced software developers who are capable of writing a large and complex codebase don't always seem to understand it. That seems to have been a factor in that Linux kernel dispute (although there were several other factors).

I think this lack of understanding contributes to some common remarks you come across in software development, such as:

"I could write that in a weekend!" (often regarding some major product like Dropbox)
"Just integrate <some library> - it does that feature for you"
"Here, I've made a prototype - take it and integrate it in to your product!"
"I've made a cool plugin - why not make it built-in to the base product?"
"Why won't this open source project accept my 10,000 lines of code patch? I've done all the hard work!"
The reality is, if you maintain a large and complex software project over a period of many years, you come to realise a key point: writing the initial code for a feature is only a fraction of the work, once you take in to account everything else you also have to do in the long term. I think unless in your career you've had the responsibility for maintaining a large (100,000+ lines of code) and continually evolving codebase for 5+ years, it's probably difficult to appreciate the substantial challenges that are unique to this.

Our experience
In our case, our browser-based game and animation tool Construct currently stands at around 750,000 lines of code, and its first lines of code were laid down about a decade ago. (It's also our third-generation product, with Construct 2 and Construct Classic before that - we started in around 2007.) I would estimate that writing the initial code for a feature is about 25% of the total work involved for that feature. The rest is maintenance - testing, diagnosing and fixing bugs, optimising performance, upgrading it to work with other changes, refactoring, customer support, writing documentation and similarly revising the documentation over time, and possibly ultimately rewriting the code (and then further maintenance still continues beyond that).

In the grand scheme of things, Construct isn't even that big: browsers, operating systems like Linux, and many other projects run in to the many millions of lines of code. In those cases I wouldn't be surprised if the ratio is more like 10%, or even less.

Once you've been burned a few times by having to do an extraordinary amount of work for a small change, or having an exciting new upgrade planned but then you realise some particular feature is a major problem that blocks the upgrade, or having to completely rewrite a major feature involving someone else's code and finding all sorts of complications in it - all of which has happened to us - then you start to really appreciate this. I think many people, including experienced developers, view software development as hammering out the necessary lines of code, and then job done. Perhaps that's true in some jobs! But for projects like ours, that's far from the case.

The maintainer's perspective
Once you truly understand this, then you start to see things very differently. To many on the outside, seeing someone submitting 10,000 lines of code for a new feature in an open-source project is a generous, helpful person who deserves respect and co-operation from the developers. However experienced developers responsible for the codebase will be well aware that person may suddenly disappear off the face of the earth - and then once you consider the long term, they've essentially dumped responsibility for perhaps 4-10x as much work as they've done themselves on to the project's other developers. If they quite reasonably decide they'd rather not deal with that, then this becomes a very thorny diplomatic problem: how do you politely turn down someone who appears to have been so generous? In the case of that Linux kernel dispute, this seems to have been part of the point the kernel developers were trying to make. (However they used what I'd call extremely undiplomatic language which looks to have added to the acrimony.)

A construction analogy
Software is a very abstract thing, and I think that makes it harder to have an intuition about. So to help explain how it works from the maintainer's point of view, I've come up with an analogy involving building a house. No analogy is perfect, and I don't have any construction experience, but it's easier to have intuition about real-world physical things that we've all experienced, so hopefully it conveys the point well enough.

A volunteer builder
Suppose you're an experienced builder and you decide to build yourself a new house from the ground up. You take care to use the best materials and techniques for a robust house that will last for decades to come.

Then suppose a younger relative just starting out in construction makes you an offer: they suggest they'll build an extension of the building for free! You can rent out the space and make money too! And they get real-world experience and something to put on their CV. Everyone says what a wonderful offer it is and how generous they are to do that for you. So you accept and they get to work on their extension.

Gradually you realise that they are working quickly, using cheap materials and basic techniques. You know to go above and beyond to make a building that lasts, but they do the minimum necessary. There is some complicated work to combine the plumbing, heating and electrics between your section and theirs. But hey, they're providing their bit for free, so you may as well take it, right?

The work finishes and everything looks OK: both sections have all relevant utilities, are waterproof, are habitable, and comply with regulations, so it seems good enough. You high-five your relative, who mentions perhaps you owe them one, and then they disappear off on to the rest of their career.

Maintenance problems arise
Fast-forward ten years. Your part of the construction is robust and still going strong. However the extension your relative build is having serious problems. The roof is leaking; the insulation is poor and wasting money on heating bills; the electrics keep tripping, affecting both properties. You are making money from renting it to tenants, but now they are complaining about these problems. You do the necessary work to maintain it and keep it going, but eventually it becomes clear: this structure is not going to last much longer. The problems are getting worse, and it is starting to need drastic maintenance: the roof needs replacing; it needs rewiring; those walls should probably have been built to the same standards as yours in the first place; and so on. However you have tenants living there, who have rights, and you can't just kick them out straight away. They've been complaining regularly about all the maintenance problems and it's been a big source of stress.

The maintainer's nightmare
Now you're in the maintainer's nightmare. The easiest thing to do would be to demolish the extension and not replace it. In the software world, that is often too difficult to do for backwards-compatibility reasons. So in this analogy, let's say you are obligated to provide the tenants with a place to live. So now you have a range of bad options:

You could just keep patching things over time. But you know it's only going to get worse and consume more time and money and cause more stress. So that's not an option.
You could try asking your relative back to do a load more free work. Chances are though they'll say sorry, they've done enough free work already, and perhaps in fact it's you who owes them a favour. Perhaps they moved away and there's no chance of getting them back anyway.
You could demolish and rebuild the extension, but you will need to temporarily house the current tenants somewhere else while you do the rebuilding, which makes it much more expensive. (In software, this might be using complicated workarounds, or writing dedicated code to handle the transition).
You could build a whole new extension somewhere else, move the tenants over, and then demolish the old extension. This is a good solution, but you have to have the space to do it, and you have to make sure the new extension has everything the old one did, while being better quality. Meanwhile, during construction - which may take a very long time - you still have to deal with all the maintenance problems of the old extension. So things will get worse before they get better. (In software, this might be writing an entirely separate new feature, and then migrating everyone over, which can be very tricky to pull off.)
You could rebuild the extension, but in stages, while the tenants are still living there. This will be awful for the tenants as they'll be living in a building site for months, but they don't have to move. It is also by far the most complicated solution, as a lot of building work has to be done while at every stage providing a habitable building. This likely makes it the slowest and most expensive option - but sometimes you have to do it if other constraints make the other options impossible. (In software, this would be upgrading the existing code in pieces over time, while ensuring it keeps working with backwards compatibility.)
The realisation
There are no good options. Suppose you pick an option and after a time-consuming and expensive rebuilding project, you have a terrible realisation: the time and cost you've invested have completely negated all the rental income you've ever received, or will receive for the next several years. With regret you come to a final realisation: it would be better to have never had the extension at all. You'd have saved money, and had far less stress.

That's when you become wise to the risks of outside contributions. You realise: they built the first structure, but they left me with the long-term responsibility of managing it - a responsibility ultimately involving more work than the initial construction, and that ultimately caused so much trouble and expense that I'd rather they never did it in the first place, or alternatively I wish I just built it myself.

This is regrettable, but unfortunately this is sometimes the reality. Perhaps in some cases everything works out great. But nobody can really be sure - who knows how things will play out in 5-10 years, what upgrades will become necessary, or what maintenance problems will come up? So experienced maintainers become extremely wary of contributions from anyone who isn't very likely to still be there and helping many years down the line.

Diplomacy
This then creates a thorny diplomatic problem when people propose things like substantial prototypes, patches, or libraries - the software world's equivalent to our analogy of building an extension. If you ask "will you maintain this?", they may well answer "Sure!", do it for a while, then ultimately stop and move on to something else. Maintainers don't tend to ask the question directly, as they know there is no guarantee of help from the outside and over many years most people move on. Instead the maintainer will usually respond with scepticism, resistance, and extremely stringent requirements. For example in the analogy this might be insisting the extension was built to the same high standard as the rest of the building. But overseeing this still requires time and effort from the maintainer, who may have their own priorities they'd rather be spending time on. It can also cause friction with the contributor, who may take the stance "this is already sufficient, why force me to keep going?" because they don't yet have the deep experience necessary to fully appreciate the difference between what's good enough now and what will still be good enough in 10 year's time.

From the outside this can look like needlessly bureaucratic and un-cooperative behaviour by the maintainer, and end up with accusations of intransigence and dictatorial behaviour, which can then degrade in to rudeness and acrimony. The fundamental problem though is the maintainers are thinking "this may well end up with us doing 75-90% of the work on this feature, so we want to be absolutely sure we are willing to do that".

Software examples
Back in the world of software, even with just our Construct products, we've been through this kind of thing several times, despite the fact it's not open source. Here are some real-world examples:

Construct 2 used a storage plugin contributed by a community member. After a few years we replaced it with an in-house one, but customer projects could keep using the old one for backwards compatibility. Despite that happening around 10 years ago, and releasing a whole new product Construct 3 since then, customers still run in to backwards-compatibility problems with the old community-contributed plugin.
Once it was suggested we add new features faster by contracting outside developers to do them. We tried this with our official Sprite Font plugin. The original developer became unreachable, and found it extremely difficult dealing with bug fixes and feature requests relating to the other developer's code, who used a substantially different coding style. In the end we had to rewrite all our plugins for Construct 3, and so we ended up rewriting all the code anyway, which was particularly challenging given we hadn't written it ourselves in the first place and didn't have a deep understanding of how it worked. It's far easier now it's all our own code.
Sometimes we add a third-party library to implement some feature. The library developer continues to support it for say 5 years, and then moves on. Then 10 years later we're still stuck with the library and struggling with bug fixes and improvements, and having to face either rewriting it ourselves or migrating to some other library (which might then stop being supported later too). With Construct I think we're now on our fourth library for minifying JavaScript code, having repeatedly switched due to maintenance difficulties, and switches often being really painful and time-consuming projects.
Sometimes people write a prototype or a proof-of-concept for a feature in a day or two, and then pressure us to implement it in Construct because they believe they've demonstrated how easy it is. However we know they've only done a fraction of the work.
Sometimes people use developer tools or encapsulation-breaking features to directly hack some feature in to the codebase, and then ask why we don't officially support it. However we know how much of a challenge long-term maintenance is; sometimes we also know there are possible future upgrades that we'd like to do that would conflict with that feature and cause a serious backwards-compatibility problem. The person demonstrating their change usually doesn't seem to care about this at all and just wants their thing to work now, but we know we're the ones dealing with the long-term fallout.
For open-source projects it's probably much harder as in theory anyone can directly contribute a large amount of code, and many projects actively encourage this. I would guess if you just accept any code from anyone then it won't be long before the whole thing implodes, so the developers running the project will need some kind of requirements for submissions. However I can't really speak to this having not had much experience of open source projects, so really on this aspect I'm just on the side-lines pointing out what I think is part of the problem in cases like the Linux kernel dispute.

Conclusion
Software is abstract and hard to have an intuition about. I suspect working on the same large complex evolving codebase for 5+ years is relatively rare in the industry - like I say some developers seem perfectly capable of writing a large amount of complex code, but appear to have little appreciation for maintenance considerations. Long-term software maintenance is surprisingly like maintaining physical thing like a building. Obviously over time a building needs maintenance, repairs, and the occasional part replaced; in the very long run major works may be needed such as replacing the roof. Software needs that too, despite the fact those 1s and 0s don't physically degrade. The term software rot aptly describes how unmaintained software still degrades over time, almost like some organic substance that starts to rot, even if the actual program data is perfectly preserved. As a software developer you usually have to stick around for a very long time before you start to find the software rot in your own code, start learning lessons the hard way, and gain that deep experience in long-term software maintenance.

I'm reminded of the quote by Robert C. Martin about programming: "the ratio of time spent reading versus writing is well over 10 to 1." That's in part because writing the initial code for a feature in a large long-term software project is only a fraction of the work. In the long run maintenance is a majority of the work for any given feature, and responsibility for maintenance defaults to the project maintainers. All too often a proposal to use some code is in fact putting the burden of responsibility for the majority of the work on someone else, even when it is done in good faith. If you suggest some software project uses some code - even a small amount - will you be there in literally 10 year's time sorting out all the issues that arise from it? Usually the answer is no. Often the maintainers know they will be though. It looks like one approach the Linux kernel developers have to this question is to favour code submitted by people who have been contributing for many years already, while being extremely sceptical of code from newcomers. This has the downside of looking like a formidable and unwelcoming community, but it illustrates the level of commitment that is needed to be able to maintain a codebase over a span of decades. It's a level of commitment that in reality not everyone will live up to, even when they genuinely and in good faith fully intend to.

Hopefully by illustrating this point we can talk about software improvements in a more realistic way, being able to negotiate the often tricky human dynamics of proposing and contributing improvements to large software projects, whether it's Construct or the Linux kernel.

Subscribe
Get emailed when there are new posts!

