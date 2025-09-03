Title: Seeing like a software company

URL Source: https://www.seangoedecke.com/seeing-like-a-software-company/

Markdown Content:
The big idea of James C. Scott’s [_Seeing Like A State_](https://files.libcom.org/files/Seeing%20Like%20a%20State%20-%20James%20C.%20Scott.pdf) can be expressed in three points:

1.   Modern organizations exert control by maximising “legibility”: by altering the system so that all parts of it can be measured, reported on, and so on.
2.   However, these organizations are dependent on a huge amount of “illegible” work: work that cannot be tracked or planned for, but is nonetheless essential.
3.   Increasing legibility thus often actually _lowers_ efficiency - but the other benefits are high enough that organizations are typically willing to do so regardless.

By “legible”, I mean work that is predictable, well-estimated, has a paper trail, and doesn’t depend on any contingent factors (like the availability of specific people). Quarterly planning, OKRs, and Jira all exist to make work legible. Illegible work is everything else: asking for and giving favors, using tacit knowledge that isn’t or can’t be written down, fitting in unscheduled changes, and drawing on interpersonal relationships. As I’ll argue, tech companies need to support both of these kinds of work.

Thinking in terms of legibility and illegibility explains so many of the things that are confusing about large software companies. It explains why companies do many things that seem obviously counter-productive, why the [rules in practice](https://www.seangoedecke.com/breaking-rules) are so often out of sync with the rules as written, and why companies are surprisingly willing to tolerate rule-breaking in some contexts.

### Seeing like a state

James C. Scott was writing about the “high modernist” movement in governance that produced (among other things) the [tidy German forests](https://en.wikipedia.org/wiki/German_Forest) of the 19th century[1](https://www.seangoedecke.com/seeing-like-a-software-company/#fn-1). In order to produce wood at scale, the German state demanded _legibility_: forests that an inspector could visit to tally up the amount of healthy trees. That means that you must be able to walk through the forest - i.e. the underbrush must be controlled - and the trees ought to be ideally laid out in neat rows of a single type.

Proponents of legibility often describe their processes as “efficiency measures” or ways to “avoid waste”. But overall, the new “efficient” forests were in fact far less efficient than the old, illegible forests. They produced less wood per year and required more effort to fight disease, because the underbrush proved surprisingly load-bearing to the health of the soil, and the variety of species turned out to have been an asset. The new homogeneous forests could be wiped out by a single parasite or disease in a way that the older, more varied forests could not.

However, the advantages of legibility are enormous. Once you know exactly how many trees you have, you can plan ahead, make large trade deals, avoid graft, and so on. To me, this is the most interesting point Scott makes. Large organizations did genuinely think that more legibility would necessarily increase efficiency[2](https://www.seangoedecke.com/seeing-like-a-software-company/#fn-2). But even when it became clear that that was false, _those organizations continued pushing for legibility anyway_, because the other advantages were too powerful.

### Seeing like a software company

It’s the same way in software companies. It’s almost a truism among software engineers that a single engineer can be more efficient alone than they can by working as part of a team. That’s why there are so many anecdotes about engineers taking leave to finally get some work done, or about productive work being done on nights and weekends.

Likewise, it should be obvious to any practicing engineer that engineer-driven work goes far more swiftly than work that is mandated from above. Engineer-driven work doesn’t need to be translated into something that makes sense, doesn’t need to be actively communicated in all directions, and can in general just be done in the most straightforward and efficient way.

This is why tiny software companies are often much better than large software companies at delivering software: it doesn’t matter that the large company is throwing ten times the number of engineers at the problem if the small company is twenty times more efficient[3](https://www.seangoedecke.com/seeing-like-a-software-company/#fn-3).

Why don’t large companies react to this by doing away with all of their processes? [Are they stupid?](https://knowyourmeme.com/memes/is-he-stupid-is-she-smart-are-they-stupid) No. The processes that slow engineers down are the same processes that make their work _legible_ to the rest of the company. And that legibility (in dollar terms) is more valuable than being able to produce software more efficiently.

### Why legibility is valuable to tech companies

What does legibility mean to a tech company, in practice? It means:

*   The head of a department knows, to the engineer, all the projects the department is currently working on
*   That head also knows (or can request) a comprehensive list of all the projects the department has shipped in the last quarter
*   That head has the ability to _plan_ work at least one quarter ahead (ideally longer)
*   That head can, in an emergency, direct the entire resources of the department at _immediate_ work

Note that “shipping high quality software” or “making customers happy” or even “making money” is not on this list. Those are all things tech companies want to do, but they’re not _legibility_.

Our small-but-efficient software company meets only one of these criteria: the ability to pivot to some immediate problem that needs solving. The other information is all locked up in various engineers’ heads, who may or may not remember what they did two months ago (and who certainly won’t be willing to commit to work two months from now). That’s not necessarily a problem, so long as everyone’s on the same page about what needs doing and the product is continuing to improve.

A typical large software company meets almost all of these criteria - I say almost, because in some companies or departments the ability to direct _immediate_ work has atrophied (more on that later). But aside from that, large companies are usually very good at cataloguing what is being worked on, remembering what’s been shipped in the past, and planning work in the medium-to-long-term.

Why are these capabilities so valuable to a large software company, when small software companies can do without them? This is leaving my area of expertise somewhat, but I’m pretty sure the main answer is **large enterprise deals**. Making deals with large enterprise customers is fantastically profitable. Any sufficiently large SaaS will thus pivot from small customers to enterprise customers, if it can[4](https://www.seangoedecke.com/seeing-like-a-software-company/#fn-4). But enterprise deals (a) can take many, many months to set up, and (b) require making long-term feature commitments. An illegible company is not configured to be able to stick with a boring enterprise deal for many months, constantly answering questions and delivering features. Large enterprise customers simply won’t trust a small software company to deliver the things they need over the next year or two.

Customers like this typically value legibility very highly, and so demand that their vendors also be legible. In fact, highly legible organizations struggle to communicate at all with organizations that are less legible (and vice versa). They don’t have access to the right bona fides, they don’t talk the same language, and so on. This puts real pressure on growing tech companies to become more legible, even if it hurts their ability to deliver software.

### Legible assumptions

In the pursuit of legibility, large tech companies make simplifying assumptions about the nature of tech work. For instance, they assume:

*   Any engineers with the same job title perform roughly the same.
*   Engineers can be shuffled and reorganized without substantial loss of productivity.
*   A team will maintain the same level of productivity over time, if it has the same number of engineers.
*   Projects can be estimated ahead of time, albeit with some margin for error. The more time spent estimating a project, the more accurate the estimate will become.

Of course, all of these are false. **Within the same job title, there is _significant_ variance in engineering ability.** Engineers have different skillsets and interests, and will work much more productively on projects that are a good fit for them. Because of this, the productivity of a team has a weak relationship to the number of engineers on the team.

Project estimates are largely fantasy. More accurately, they’re _performative_: **the initial estimate determines the kind of engineering work that gets done to deliver by that estimate, not the other way around**. For this reason, breaking down a project into parts and estimating each part often delivers a less accurate estimate, because it makes it harder for engineers to align with the overall ship date.

However, these assumptions are true enough for their purpose, which is to provide legibility to the executives in charge of the company. Whether the project estimate is accurate or not, it can be used to plan and to communicate with other large organizations (who are themselves typically aware that these estimates ought not to be taken completely seriously).

### Temporary sanctioned zones of illegibility

I mentioned above that large companies sometimes lose the ability to prioritize immediate work. This is because the processes that make work legible also impose a serious delay. Consider the steps that a hypothetical large company might take before beginning to write code on a problem:

1.   Somebody has a product idea.
2.   They take that idea to the Product org, where it goes into the “planning” stage. Meetings are had about the idea.
3.   Once the Product org formally decide they want to do it, the idea then passes to the Engineering org: into the hands of some council of engineering architects, who are tasked with the initial technical review. They figure out how it fits into the general engineering priorities and give it a very rough time estimate.
4.   The VPs and senior managers in the engineering org then negotiate which team will own the work. Often this is a semi-technical, semi-organizational decision (because which service the work should fall into is at least partly a technical question).
5.   Finally the work lands on the team. It enters the team planning backlog, where the team technical lead breaks it out into smaller pieces of work.
6.   Those smaller pieces of work enter the team ticket backlog, and are estimated in the team’s weekly planning meeting.
7.   Finally some of those pieces of work make it into the next sprint, and are picked up by an engineer who can actually do it.

I’m leaving out many crucial parts of this process: the updates on each ticket, which then roll up to higher levels of management, legal and design review, which can themselves take weeks, and then the final steps involved in shipping the change to customers. All of this makes the work very legible, but **none of this is compatible with work that has to be done _right now_**. What do you do when there’s a sudden, urgent technical problem - maybe you’re about to overflow your `int` ID column on the users table, or some very large customer is experiencing a show-stopping bug?[5](https://www.seangoedecke.com/seeing-like-a-software-company/#fn-5)

To solve this kind of problem, tech companies often reserve the right to create _temporary_ zones where illegible work is allowed. Sometimes these are called “virtual teams”, or “strike teams” (or even the colourful name “tiger teams”). They are composed of hand-picked engineers who are trusted by the organization. Often there is no manager assigned at all, but instead some very senior engineer who’s tasked with running the project. These teams are given a loose mandate - like “stop the database from falling over every few days” - and allowed to do basically whatever it takes to get it done.

This is a smart compromise between complete illegibility, which as I discussed above would make the company unable to make deals with its richest customers, and complete legibility, which would force even urgent company-killing issues to go through the entire laborious process of scoping, planning and estimating.

Even when siloed to a temporary team, sanctioned illegibility still coexists awkwardly with the rest of the organization. Engineers outside the team don’t like seeing other engineers given the freedom to work without the burden of process: either because they’re jealous, or because they’re believers in process and think that such work is unacceptably dangerous. Managers also don’t like extending that level of trust. That’s why sanctioned efforts like this are almost always temporary. The majority of the illegible work that occurs in large organizations is still _unsanctioned_.

### Permanent zones of unsanctioned illegibility

If you’re an engineer on team A, and you need team B to do some kind of work for you, the formal way to do this is to create an issue in their “planning” backlog and wait for it to go through the entire twelve-step process before it finally makes its way into one of their sprints, where hopefully somebody will pick it up and do it. This can take weeks to months. When what you want is a one-line change, it’s incredibly frustrating to watch your requested work item go through all these steps - each one of which takes many times longer than it would take to simply do the work.

The official way around this problem is that team A should anticipate in their planning process that team B will need to do this work, so that piece for team B can enter their backlog at the same time as it enters team A’s backlog. That way (in theory) they should be complete at around the same time[6](https://www.seangoedecke.com/seeing-like-a-software-company/#fn-6). Any practicing software engineer knows how ridiculous this idea is. You can never anticipate every change that has to be made months before you start writing code.

The _actual_ way around this problem is **illegible backchannels**. An engineer on team A reaches out to an engineer on team B asking “hey, can you make this one-line change for me”. That engineer on team B then does it immediately, maybe creating a ticket, maybe not. Then it’s done! This works great, but it’s illegible because the company can’t expect it or plan for it - it relies on the interpersonal relationships between engineers on different teams, which are very difficult to quantify. If you’re a well-liked engineer, your ability to pull on these backchannels is significantly greater than if you’re brand-new or have a bad reputation. But how well-liked you are is not something companies can officially use when they’re planning projects.

Backchannels are a constant presence at all levels of the company. As well as engineer-engineer cross-team backchannels, there are backchannels inside teams, between managers, product managers, and so on. Often when a question is asked formally in a public space, it’s already been rehearsed and workshopped privately with the person who’s answering the question. None of this is or can be documented as part of the formal processes of the company, but it’s load-bearing nonetheless. Many formal processes simply cannot function without the consensus mechanisms or safety valves offered by backchannels.

Sometimes backchannels can go badly. Earlier this year I wrote [_Protecting your time from predators in large tech companies_](https://www.seangoedecke.com/predators) about how some people use backchannels to benefit themselves at the expense of the naive engineers they’re requesting work from. And it never feels good when you get the sense that everyone in a meeting has privately discussed the topic ahead of time except for you. For these reasons, some people think that backchannels themselves are a bad thing, and that all communication should go via formal, legible channels.

### Sociopaths, clueless, and losers

There’s another text which has been as influential to many as _Seeing Like A State_. This one isn’t a book, but a blog post: [_The Gervais Principle_](https://www.ribbonfarm.com/2009/10/07/the-gervais-principle-or-the-office-according-to-the-office/) by Venkatesh Rao. Rao divides organizations into three groups. At the top are the “sociopaths”, who cynically use organizational rules for their own benefit. In middle management are the “clueless”, who are bought into the formal rules of the organization and don’t realise that there’s a deeper game being played above their heads. Below them are the “losers”, who realise there’s a game being played but don’t want to play it. The name “losers” is not a value judgement - I think it’s meant to affectionately pick out people like the leads in _Clerks_, who are too authentic to get involved in the corporate game.

I don’t agree with everything in _The Gervais Principle_, though I think it’s worth a read (if you’re interested in this stuff, you should also read the excellent [_Moral Mazes_](https://www.amazon.com.au/Moral-Mazes-World-Corporate-Managers/dp/0199729883)). But the categories here can be very naturally read in terms of _legibility_. Both sociopaths and losers are engaged with the illegible world of the organization. Sociopaths use this world to climb the ladder, while losers use it to carve out a cosy low-effort niche for themselves.

The “clueless” are only engaged with legible processes. They’re the people who, when they want to get promoted, go and look up the formal job ladder and make a plan for how they can exemplify each of the values at the next level. They’re concerned with doing everything by the book. When they’re forced into an encounter with the illegible world, their reaction is to shake their heads and start drafting updates to the legible process that can accommodate some pale approximation of the more-efficient illegible process.

I think it’s far too cynical to call these people clueless. Legible process is still very important - after all, it’s the large part of what the organization does. Improving formal processes is still very high-leverage work, even if formal processes can’t ever describe the entirety of how an organization operates. People who are invested in legibility have real value to any tech company.

However, thinking about people in Rao’s categories - people who exploit illegibility, people who find it distasteful, and people who use it casually - can be illuminating. Many frequent areas of conflict in software companies stem from the friction between these groups of people.

### Final thoughts

I write a lot about recognizing and using illegibility in tech companies:

*   Breaking the (formal, legible) rules is [sometimes the right thing to do](https://www.seangoedecke.com/breaking-rules)
*   Beware of savvy product managers (and others) exploiting illegible channels to [chisel work out of naive engineers](https://www.seangoedecke.com/predators)
*   Competent engineers should work on [“side bets”](https://www.seangoedecke.com/side-bets) that are outside the normal planning process
*   Getting promoted to Staff and above has [very little to do](https://www.seangoedecke.com/staff-engineer-promotions) with the formal job ladder

In general, advice about illegible processes is what I call [“dangerous advice”](https://www.seangoedecke.com/dangerous-advice). It’s dangerous because if you make it legible - for instance, if you announce publicly that you’re getting a piece of work done through backchannels instead of the formal process - you will be punished by the organization _even if your management chain wanted you to do it_. You can’t speak too loudly about it. It has to stay illegible.

I get a lot of negative feedback on these posts from people who say that you should never sidestep the formal process. According to them, if it needs changing, you should change the process instead of going around it. In other words, everything that goes on in a tech company should be _legible_, and _illegible_ processes should be stamped out and converted to legible ones.

I think this view is naive. All organizations - tech companies, social clubs, governments - have both a legible and an illegible side. The legible side is important, past a certain size. It lets the organization do things that would otherwise be impossible: long-term planning, coordination with other very large organizations, and so on. But the illegible side is just as important. It allows for high-efficiency work, offers a release valve for processes that don’t fit the current circumstances, and fills the natural human desire for gossip and soft consensus.

* * *

1.   This is the first example Scott gives, but I promise I did read the whole book. Other examples: the construction of [Brasília](https://en.wikipedia.org/wiki/Bras%C3%ADlia), [Operation Vijiji](https://en.wikipedia.org/wiki/Operation_Vijiji) in Tanzania, and the Soviet [attempt](https://en.wikipedia.org/wiki/Collectivization_in_the_Soviet_Union) to replace individual peasant farms with state-run collectives.

[↩](https://www.seangoedecke.com/seeing-like-a-software-company/#fnref-1)
2.   This is a very common false belief today among software engineers.

[↩](https://www.seangoedecke.com/seeing-like-a-software-company/#fnref-2)
3.   I don’t think small companies just work harder; plenty of people at large companies work very hard. I also don’t think that small companies just have better engineers - what advantage they have in enthusiasm is often outweighed by the fact that they can’t afford to pay as well.

[↩](https://www.seangoedecke.com/seeing-like-a-software-company/#fnref-3)
4.   I was at Zendesk during the height of its pivot.

[↩](https://www.seangoedecke.com/seeing-like-a-software-company/#fnref-4)
5.   Ironically, the most urgent types of problem typically can be solved via a normal “incident” process - but this itself is usually a zone where the rules are relaxed a bit in order to resolve the incident as quickly as possible. Anyway, here I’m not talking about incidents but about projects that will take a couple of weeks to resolve.

[↩](https://www.seangoedecke.com/seeing-like-a-software-company/#fnref-5)
6.   The other, healthier official way is to allow teams to make small changes to other teams’ services themselves. But this only goes so far - the other team will always be the gatekeepers for changes like this, and are always in a position to slow down the change by days or weeks.

[↩](https://www.seangoedecke.com/seeing-like-a-software-company/#fnref-6)

If you liked this post, consider [subscribing](https://buttondown.com/seangoedecke) to email updates about my new posts, or [sharing it on Hacker News](https://news.ycombinator.com/submitlink?u=https://www.seangoedecke.com/seeing-like-a-software-company/&t=Seeing%20like%20a%20software%20company).

September 3, 2025│ Tags: [tech companies](https://www.seangoedecke.com/tags/tech%20companies/)

* * *