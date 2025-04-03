Title: Revenge of the junior developer | Sourcegraph Blog

URL Source: https://sourcegraph.com/blog/revenge-of-the-junior-developer

Markdown Content:
Hello, hello, hello! Good to see everyone again.

I've really gotta start being careful what I say these days. I've got so many people watching.

So anyway, I ripped a fart the other day that sounded like _viiiibecooode,_ and I was immediately approached by 3 investors. I had to tell them no sorry that was just a fart, just to get them off me.

There's so much going on that once again I tried several times to write this post, but each attempt grew huge and rabid, and I had to put 'em all down like Old Yeller. This time I'll just ship it while it's still a pup. _(Edit: Damn. At least it’s action-packed to the end.)_

_Brief note about the meaning of "vibe coding":_ In this post, I assume that **vibe coding will grow up** and people will use it for real engineering, with the "turn your brain off" version of it sticking around just for prototyping and fun projects. For me, vibe coding just means letting the AI do the work. How closely you choose to _pay attention_ to the AI's work depends solely on the problem at hand. For production, you pay attention; for prototypes, you chill. Either way, it’s vibe coding if you didn’t write it by hand.

_One more note:_ The revenge part happens at the very end, just like in the movies.

OK! With those administrative items out of the way, let's goooooo!

‍

### Part 1: The six waves

Vibe coding is a whimsical name for chat-based coding, where you ask the LLM to write code, and then you feed it the results and ask it for more, in a continuous loop. It’s very different from traditional coding, or even coding with code completions.

Chat coding has been around a while in coding assistants, but without a rallying cry. It finally got one, when in [early February](https://x.com/karpathy/status/1886192184808149383) the illustrious Dr. Andrej Karpathy, famed among other things for co-founding OpenAI, put a pretty name to the face of chat. He called it “vibe coding” and it became an instant blue/gold dress situation pretty much overnight.

Today as of, wait lemme look at my watch, _right_ _now_ as you’re reading this, vibe coding has entered a strange, unprecedented, quantum-like triplet-state:

*   **Vibe coding is still completely invisible to 80%** **of the industry** outside Silicon Valley, who will have little clue as to what we’re talking about here. Many haven’t even heard the phrase “vibe coding” yet, let alone “coding agent”. I guess they never open the news? Unfortunately they all risk getting blindsided, nay, T-boned by AI.
*   **Vibe coding is currently going batshit viral,** growing like crazy on a dramatic exponential curve, hitting major media outlets like the NYT, flooding social media, celebrated by some, decried by others. A bunch of companies were busy banishing it just as [Google was unofficially adopting it](https://www.searchenginejournal.com/why-google-may-adopt-vibe-coding-for-search-algorithms/541641/). Everyone’s still arguing about what “vibe coding” even means. But a ton of people, more every day, think it’s the future right now.
*   **_Chat_ coding in general is already utterly passé** to an exponentially-_faster_ growing group of developers who now wouldn’t walk across the street to piss on chat-based coding if it was on fire. They are still vibe coding and indeed getting better vibes than anyone. And yet they could not possibly care any less about _your_ vibe coding – those long back-and-forth chat conversations – ever again, good day to you Sir, I said Good. Day!

Here at Exaggeration Central, we are finding it hard to make anything up that’s crazier than this. It’s real, but unfolding so fast that it feels genuinely surreal.

Vibe coding is in steep ascent, and chat-based coding – what _you_ think of as vibe coding, and what I used to call [CHOP](https://sourcegraph.com/blog/the-death-of-the-junior-developer) – is indeed also still on the rise… for now. But agentic coding – the subject of this post – will soon rocket by chat coding as if it’s standing still.

By Q3, today's chat coding will for many have become a dire fallback of last resort, reserved for when you can’t afford to do it the superfast way with agents. And through it all, as chat coding is eclipsed, vibe coding will live on.

I've done my best to represent how I personally think about this stuff in Figure 1.

‍

![Image 1](https://cdn.prod.website-files.com/6750d0c3f154999a486dade7/67ddc78096f9b99f2e1e12c7_AD_4nXcOzNxtnxw6PVzSz1Kq4EcknDapFEhVWZFNvy8_Dgud2owjYaIJRkEJxdbWq_5KB_lVlp8dCswV0__AD8yaE5OBjUitjO5AmlBMerE7WGvbC20HRUSv17YDGfD-QMfQcUHQ1Nc.avif)

_Figure 1: Overlapping waves of AI coding modalities_

The chart in Figure 1 depicts six overlapping waves of programming: traditional (2022), completions-based (2023), chat-based (2024), coding agents (2025 H1), agent clusters (2025 H2), and agent fleets (2026).

In the figure, traditional and completions-based coding – the two manual modalities – are on the decline, and the others are rising exponentially. Beginning with chat, each new wave rises much faster than previous waves. Finally the figure depicts vibe coding as also increasing exponentially, but on a dotted line alongside the others, because as we’ll see in a bit, vibe coding is not a modality.

As a sneak preview for our discussion, "agent clusters" is the placeholder term I'm using for devs being able to run and fruitfully manage many coding agents in parallel, potentially even more than can fit on a dev’s local machine. And "agent fleets" are what happens when we get AI supervisors for the leaf nodes, as shown in Figure 2, "FY26 Org Chart".

‍

![Image 2](https://cdn.prod.website-files.com/6750d0c3f154999a486dade7/67ddc78055ba7640defaebad_AD_4nXeZ7QEmrK2Y-_bEapXRCtKEbT6uuTZpgu7pOfDwFAMKy85ZiriV3w6ptq9IbGV7iMHz5x5fFqZ5vY3Jo9fFq6w_u2z-mDNF-eLxbNCslKCVd3hH0EC2fQVFosgqn9Ze_T6WiNA.avif)

_Figure 2: FY26 Org Chart_

This figure shows all individual contributor (leaf-node) devs in the org acting like second-level line managers, running AI “manager agents,” which themselves are supervising groups of coding agents. For instance, under the guidance of a single IC developer, one managed agent group might be doing bug backlog grooming, another working on new business features, and a third group working on a long-running architectural migration. A veritable agent farm!

This is of course just a crude approximation of how it will unfold, but I think it's close enough. We all predicted the “wave four” coding agents were coming, and they arrived faster than most of us expected. And it's already possible to jump on wave five manually, albeit with effort. I’ve been running two agents in parallel. When you do this, it becomes evident that a lot of the work can be facilitated with agentic help.

How do agents help with agents? Today, you have to notice when an agent worker is stuck, done, or gone astray, and nudge it appropriately. Supervisor agents can and will start doing most of that for us very soon. The result: wave six. Developers will be empowered to keep work queues full in large fleets of coding agents, grinding their way through vast mountain ranges of enterprise legacy code. It will be glorious.

And these magical agent fleets will be here by early 2026 at the _latest_. Because building them isn't actually that hard – we're already very good at parallelizing work.

That’s our lightning intro. Lots more to come. If all this is a big fat surprise to you, then you're in for some troubled waters in the months ahead.

‍

### Part 2: Where are you?

If you still think of AI-based code-autocompletion suggestions as the primary way programmers use AI, and/or you are still measuring Completion Acceptance Rate (CAR), then you are sitting on the vaguely dinosaur-shaped curve representing Traditional Programming in Figure 1. This curve super-slides into obsolescence around 2027.

I have bad news: Code completions were very popular a year ago, a time that now feels like a distant prequel. But they are now the AI equivalent of “dead man walking.”

If you’re a bit more avant-garde, then you might think that chat-based programming is how things are going to unfold this year – meaning, in-IDE coding assistant chat interfaces like Copilot, Cursor, Sourcegraph, and Windsurf. If you’re in this group, then you're not doing too badly at all. Middle-of-the-pack, pat on the back. You've at least adopted a modality that's useful _– extremely_ so compared to code completions – and chat is still rising in popularity.

But suddenly we have this latest wave, the new coding agents like Aider.chat and Claude Code – and soon, similar and prettier agents in all your favorite IDEs, _wink nudge cough cough_.

Once you have tried coding agents, and figured out how to be effective with them, you will never want to go back. They are going to stomp chat coding. And the great thing is, with agents you are still vibe coding. That’s why it’s not a modality: You can vibe code with any non-manual AI modality: chat, agents, clusters. As long as AI is doing the work, you’re vibing! The only difference with agents is that you don’t rendezvous with them as often.

Now that agents have emerged, we can start to see patterns. Each successive modality wave, beginning with chat, is conservatively about 5x as productive as the previous wave. Chat can be 5x as productive as manual coding, agents can be 5x as productive as chat, and so on. Note that each wave would probably grow to be 10x as productive as its predecessor, if left unchallenged and given time to mature. But they keep getting flattened by new, even faster modalities.

That’s the situation as I see it today. We find ourselves in a big race in the AI ocean, beslapped by increasingly violent waves. The ones who make it will ride those waves. Every company falls somewhere on one or more of the adoption curves in Figure 1. Where are you?

And that, dear folks, is my charming, Disneyfied mental model of what lies ahead. I’ve asserted that the upcoming waves of clusters and fleets are not only inevitable, but practically right around the corner. Vibe coding remains a durable and lasting feature of that landscape – but not in the way most people think. Vibe coding simply means never writing code again.

If you're with me so far, then let’s take a look at the financial impacts. First I’ll quickly get you up to speed on how coding agents work – it’s not complicated, you just start burning money and the smoke makes them smarter. And if you’re not with me so far, I encourage you to go play with these new coding agents. Seriously. Or watch someone who knows how.

Whether you're convinced or skeptical, let’s at least look at how these new coding agents actually work. Because there’s no magic.

‍

### Part 3: New camel owner’s manual

Let's see why this mere weeks-old development could quickly put your company in a real bind. A right pickle, you might say. A fine kettle of fish.

We’ve heard claims of software coding agents before. But this is different. These “true” coding agents are still _very_ _very_ new, weeks old at best, and they only run in text-based 1970s Unix-style terminals. Getting one of these is a lot like you've been walking all your life and someone gives you a free camel. In fact, they say, take all the damn camels you want. And it’s amazing having one. _One_. They're great compared to walking everywhere, but they'll spit on you and bite you and they require large amounts of leafy green food, primarily fifties and hundreds.

A lot of you, I know this for a fact, have been super skeptical about chat coding. I’ve even heard that some developers have expressed to their managers, clearly and unambiguously, that they want to keep writing code. That’s what they’re here for, they say. Writing. Code. They say it slowly, like they think you’re deaf and it would help. They claim they’re never going to delegate their coding work to an AI. Hey there! I see you.

All of you skeptics should drop whatever you’re doing or holding, just throw it on the ground, and run like mad towards the nearest camel and hop on. Download and try out a coding agent, ideally one launched after March 1st 2025. Because they turn whatever you know or thought you knew about coding with AI, _right_ on its head. I myself could scarcely believe what I was seeing, just three weeks ago.

Coding agents are simple enough in principle. They work just like a typical vibe-coding chat session, with the LLM doing most of the analysis and heavy lifting, and you mostly wearing headphones. But with agents, you don’t have to do all the ugly toil of bidirectional copy/paste and associated prompting, which is the slow human-y part. Instead, the agent takes over and handles that for you, only returning to chat with you when it finishes or gets stuck or you run out of cash.

And they often get pretty darn far, entirely unassisted. They just grind away at their task until they get it right, throwing tokens at the problem to explore the space as needed. The human is removed as the bottleneck for 90-99% of the work, but otherwise it’s pretty much just like a faster version of chat vibe coding.

The only practical difference from chat, aside from cost, is that agents can perform much larger subtasks at a time, potentially encompassing many individual steps. During this time, the supervising developer is freed up for important work like finishing off that bag of Cheetos and browsing HN.

Just to make it concrete, you might tell a coding agent something like, "Here is JIRA ticket #_<number\>_; please go fix it." That is all you would need to say. The agent would first try hard to get access to the JIRA ticket: it might look for the JIRA command-line tool, maybe even asking you if it can download it. It could even write a throwaway program for itself to fetch the ticket fields programmatically. We see them write throwaway programs pretty often.

Once the agent can read the ticket, it uses tools on your machine, examining your code just like you would, to track your bug down. It asks you for permissions for each tool – one of the biggest slowdowns in the process today. Once the agent finds the bug, it will propose a fix, write tests to verify the fix, run those tests, and make any other changes necessary to get the tests passing – all in a loop without needing you, for the most part.

These new coding agents can solve huge issues, create even bigger messes, and generally behave like a supernaturally fast human developer who’s always flying a little blind and a little behind schedule.

It sounds like science fiction but you can use them right now.

It's important to understand that these new agents are still only capable of handling modestly small-ish to medium-esque tasks at a time. Task graph decomposition, a skill we've all learned during the chat days of yore (December), is just as important today as you switch to vibe coding with agents. Even more so, because it’s so easy to overshoot and be over-ambitious with agents. They are so incredibly effective that it’s easy to get greedy and smother the goose.

Be nice to your goose. Don’t overstuff it. You need to break things down and shepherd coding agents carefully. If you give one a task that’s too big, like "Please fix all my JIRA tickets", it will hurl itself at the problem and get almost nowhere. They require careful supervision and thoughtful problem selection today. In short, they are ornery critters.

But that will change. Before you can so much as lash a bat, speaking of critters, agents will creep into your IDE, not as camels but as saddled horses: a mostly ergonomic improvement, sure, but a welcome one. It will be nice to have a tool that can’t spit foul-smelling fluids with high accuracy at objects up to thirty-six meters away.

Every iteration of the tools from here on out will help make coding agents easier, more parallelizable, and more powerful. And we’ll start seeing truly dramatic steps forward even more often this year.

Chariots are next. Just you wait.

‍

### Part 4: I was told there would be no math

This section is for CIOs and finance folks. Hi. Thanks for reading this far.

In your FY26 planning that you _just_ wrapped up a few weeks ago, how much opex budget did you put aside for developer LLM spend? Maybe a little? A lot? One company told me they were considering a generous budget of $25 per developer _per day_. That seems bold, like a lot of money. An almost reckless amount.

Well, it turns out they were on the right track. Coding agents are très cher, muy caro, we're talking very, very expensive. They burn lots of LLM tokens, to the tune of $10-$12/hour at current rates. How much are your per-seat licenses for your coding assistant right now? Thirty a month? Ballpark? Maybe less?

For calculation purposes, as a rule of thumb, you can think of each coding agent instance as being approximately as valuable, amortized over this fiscal year, as having one additional junior level software developer on staff – provided that someone (human or AI) is keeping it mostly busy for 8-10 hours a day.

That’s a heck of a rule of thumb. I think you’ll agree that ten bucks an hour is a steal for a professional software engineer who just needs a good babysitter.

So it's going to be worth your while to budget more like $80-$100 of LLM spend per developer, per day. $30 a day is only going to be enough for three hours of camel rides, and then your devs go back to walking after lunch. But if you pay the full Ben Franklin, each of your devs will easily _double_ their output, since they can play nanny for two agents and get other work done on the side. It’s a no-brainer.

However.

The upcoming wave, which I'm calling "agent clusters" – the chariot I hinted at in the last section – should make landfall by Q3. This wave will enable _each_ of your developers to run many agents at once in parallel, every agent working on a different task: bug fixing, issue refinement, new features, backlog grooming, deployments, documentation, literally anything a developer might do.

Each of your devs will suddenly become like many devs. At least, the ones who are good at it will. (_Foreshadowing: I smell revenge.)_

Agent clusters will have the side effect of finally moving software development into the cloud. People have been predicting cloud-based IDEs for decades! Right? Half of you have probably tried to build one at some point. They seem like such an obvious idea.

But it has always been more convenient to run IDEs locally, so cloud-based development never took off. The agent-clusters wave of H2 2025 will change that. Your dev desktop does not have enough power to run dozens of agents at once, let alone hundreds. The bulk of developer work will shift up to the cloud practically overnight.

So you probably need some more cloud budget.

Running N agents at once multiplies your devs' innocuous daily spend of $10/hr by whatever N is, and that’s not counting cloud costs, just token burn. If your developers are each on average running, say, five agents at once – a very conservative number, since agents will work mostly independently, leaving the dev free to do other stuff – then those devs are each now spending $50/hr, or roughly $100k/year.

It’s not really a steal anymore, so much as a heist. We’re talking about each developer gradually boosting their productivity by a multiplier of ~5x by Q4 2025 (allowing for ramp-up time), for an additional amortized cost of only maybe $50k/year the first year. Who wouldn’t go for that deal?

Unfortunately, you almost certainly didn't include $50k/year _per developer_ of LLM spend in your 2026 operating budget. This situation will rapidly separate companies into the have-budgets and have-budget-nots, and the haves will, well, have it. The have-nots’ll hardly have half. Follow me?

To put it more bluntly: Software development is now a pay-to-play bullet train. If you can’t afford a ticket, you risk getting red-shifted away from the pack.

‍

### Part 5: The agent fleet is coming

Here's where it starts to get a little bit uncomfortable. If you’re already sweating, or feeling any kind of palpitations, maybe take a little break, grab a soda, dust off that resume, whatever. Take your time. Whenever you’re ready. We’ll wait.

OK, from _here on_, you all promise you are chill, scout’s honor. Let’s do this.

The wave after clusters, or agent "fleets", for lack of a better word, will allow your developers to run 100+ agents at a time… with the help of yet more agents. Supervisory agents will be able to run groups or pods of coding agents, mediating on their behalf and only bringing in the human when agents get really stuck.

The new job of a software developer going forward will soon be managing dashboards of coding agents and their AI supervisors, as sketched in Figure 2: FY26 Org Chart. Some might derisively call this job _babysitting_, and accuse AIs of being little whiny baby robots that need a grownup to cut their food into little pieces, and change their diapers, and clean up their messes, and keep them from wandering out of their playpens. But we prefer to call it _software development_. This is our destiny.

For you CIO-types, fleets will enable your developers to spend thousands of dollars a day. Even if inference costs plummet, the [Jevons Paradox](https://www.npr.org/sections/planet-money/2025/02/04/g-s1-46018/ai-deepseek-economics-jevons-paradox) will result in higher usage offsetting those costs. If you don’t believe that, go ask to see your bug backlog; it’s basically infinite.

Thousands a day!? But it's money incredibly well spent! Your engineering org will start to be able to go as fast as _you_ want them to go, for once. Can you believe it? It'll be like being a startup again. You’ll be able to “surprise and delight your customers”, as Jeff Bezos is fond of saying, at an elite level you never dreamed possible.

But you're going to have to find a whole lot of new budget somewhere. Maybe you're lucky and your company has deep pockets. For instance I just heard, going to press here, that a big familiar brand you all know has a very large slush fund allocated for LLM experimentation this year. I wonder how many companies did that, and in doing so, perhaps unwittingly dodged this year’s budget-planning black swan event?

If after searching the couch for coins, you’re not able to scrape together an extra $50k per developer by EOY, maybe you can raise the money somehow. This probably plays better into the hands of startups than big companies right now. I think this agent thing has leveled a lot of playing fields.

The scary part of this story is that if you can’t find or raise money, and you want to stay competitive, then you're going to have to make painful cuts in order to free up the opex budget. And if you run the numbers again, there's only one department where it makes sense to cut.

The rest, I'm afraid, is an exercise for the reader. I have no idea what will happen. I’m just some dude. Maybe this is all overblown, and you’ll need to add six months to my projections before they come true. I argued with Claude about it for a while, and Claude capitulated and said it was plausible if I stretched all my estimates by six months. So the bad news mayn’t be all bad!

And now for the good news! You did ask for the bad news first, didn’t you? Well regardless, it’s out of the way. It’s easy peasy from here, and we’re almost done. All that’s left is sweet, sweet revenge.

‍

### Part 6: Revenge of the junior developer

It turns out, it’s not all doom and gloom ahead. Far from it! There will be a _bunch_ of jobs in the software industry. Just not the kind that involve writing code by hand like some sort of barbarian.

One consistent pattern I’ve observed in the past year, since I published "[The Death of the Junior Developer"](https://sourcegraph.com/blog/the-death-of-the-junior-developer), is that junior developers have actually been _far_ more eager to adopt AI than senior devs. It’s not always true; a few folks have told us that their juniors are scared to use it because they think, somewhat irrationally, that it will take their jobs. (See: Behavioral regret theory. Thanks for the pointer Dr. Daniel Rock!)

But for the most part, junior developers – including (a) newly-minted devs, (b) devs still in school, and (c) devs who are still thinkin’ about school – are all picking this stuff up really fast. They grab the [O’Reilly AI Engineering](https://www.oreilly.com/library/view/ai-engineering/9781098166298/) book, which all devs need to know cover to cover now, and they treat it as job training. They’re all using chat coding, they all use coding assistants, and I _know_ a bunch of you junior developers out there are using coding agents already.

Junior devs are vibing. They get it. The world is changing, and you have to adapt. So they adapt!

Whereas senior developers are, well… struggling, to put it gently. I have no shortage of good friends, old-timers like me, who have basically never touched an LLM or even seen one naked. Plenty of others have only barely dabbled with coding assistants. I even hear about senior developer cohorts, from many industry leaders, who take a flat-out stand against it.

Example: a tech director at a well-known brand just told me that one of their devs sent them a PDF explaining, with color slides and charts, why they all needed to abandon AI and go back to regular coding. Now do you see what I meant when I said we have the widest distribution of understanding in tech history? There are people who still think this is like, crypto or something. Yikes!

Look, some senior devs are struggling, no doubt, because they’re just busy. I get it. But I think for most of them, there’s something deeper going on. When I used to blog about programming languages, I found that simply saying that I _liked_ some programming language, any language at all, would get me in surprisingly serious hot water. People would yell in threads, digital spittle flying everywhere. I didn’t get what was going on. All this, just because I said I liked a language?

After several years I figured out that it’s because they felt if people listened to me, then everyone would switch to that language, and then the senior devs would have to learn it too. They equated having to learn something new – and I mean really new, sort of like starting over – with losing their job and their health insurance and going bankrupt and dying outside a hospital on the steps. It’s just human nature at work, in the face of big uncertain change.

I believe the AI-refusers regrettably have a lot invested in the status quo, which they think, with grievous mistakenness, equates to job security. They all tell themselves that the AI has yet to prove that it’s better than they are at performing X, Y, or Z, and therefore, it’s not ready yet.

But from where I’m sitting, they’re the ones who aren’t ready. I lay this all out in detail, my friends, so you can help yourselves.

Regardless of _why_ the luddites aren’t adopting it, they have lost. Junior devs have the high ground, and the battle is now over. Not only are junior devs on average adopting AI faster, but junior devs are also – surprise! – cheaper. If companies are going to make cuts to pay for their devs to win with tokens, which devs do you think they’re gonna keep?

The AI holdouts don’t see _any_ of this this coming yet, so the junior devs are going to have to lower their light sabers and shout this message down from the hilltop above:

> It’s not AI’s job to prove it’s better than you. It’s _your_ job to get better using AI. 

Otherwise, you get… the else clause. You know. The else clause. The lava. You fall in. Why do I have to spell this out?

So! Here we are, at the end of the movie. You made it. High five, junior devs! ✋I didn’t see this coming last year, but I’m very impressed that you’ve managed to be the ones voting the losers off the island. And high five to those of you senior devs who _have_ figured this out and are truckin’ along already. There aren’t as many of you as you’d think, at least outside the Bay Area Bubble.

For the rest of you… _lean into it._ Be like a Junior. Seriously. It doesn’t matter who you are, really, nor even if you’re a person or a company. Lean in. It’s time. AI is here.

Here at Sourcegraph, we study the hell out of this problem space every day. We are working towards a world where all this stuff, despite being incredibly expensive, is astonishingly, and soon undeniably, _valuable_. To everyone who chooses to use it, anyway. Coding-agent armies are marching across the Rubicon, and getting them wired up to enterprise IP assets and code bases is the next big game in town. That’s where we’re focused.

More broadly, we all think there will be jobs. Lots of jobs. We think the flat hiring right now is just companies signalling that they don’t know what to do yet. But this very fiscal year, companies of all shapes and sizes can be more ambitious than ever before, and I say that without a hint of hyperbole. If history is any indicator, from steam to electricity to computing, we’re going to see vastly more people creating software soon. The resulting productivity wave may boost national GDPs by astonishing amounts, 100% or more.

But to participate, you're going to have to learn the next wave. As a developer, heck, even if you’re a PM or literally any tech-adjacent role – you need to catch up on coding agents, and stay caught up. No more dallying and dabbling. Figure out how to use an automatic coding agent right now, and don't give up until you know how to wield it. Push on it until it works for you.

And don’t get cocky and try to push it too hard. A coding agent is like a big-ass tunnel borer machine when you've been using power shovels. It is strong, sure, hella strong. But it is expensive, it can still get stuck badly, and you need to guide it carefully at all times. And it's not _that_ fast – it's not going to bore through the English Channel in a day. So don't set unrealistic expectations going in. Just focus on how different this stuff is from 2 years ago when ChatGPT came out, and then marvel at how different it is from 2 _months_ ago when the best we had was chat.

Have fun with it. It’s called vibe coding for a reason. It turns out not writing code is pretty easy.

Don’t fall prey to the tempting work-deferral trap. Saying “It’ll be way faster in 6 months, so I’ll just push this work out 6 months” is like saying, “I’m going to wait until traffic dies down.” Your drive will be shorter, sure. But you will arrive last.

Agents are coming. Vast fleets of them. Not just coding agents. Agents are arising _everywhere_, across entire businesses and production tech processes. I talked to a big customer this morning who has already built dozens to hundreds of "AI task machines" – custom-built agents that perform specific parts of their giant workflows. The future is now. Agents are here.

If you’re looking for a call to action, then I give the same advice to both humans and companies: Switch to chat. Ditch completions. Stop writing code by hand. Learn how validation and verification work in the new world. Familiarize yourself with the space, and follow the state of the art. Stop whinging and turn this into an engineering exercise. Stay on top of it. You can do it.

Above all, pay close attention to the new coding agents. They may be nigh-unusable for most devs today, but not for long. Not long at all. They are incredibly expensive productivity machines – and at bargain-basement prices compared to humans. Tough choices ahead for all.

The new job of “software engineer,” by the end of this year, will involve little direct coding, and a _lot_ of agent babysitting. The sooner you get on board with that, the easier your life will be.

If you’re really not sure what to do after reading this far, go ask a junior developer for help.

That's pretty much it. We are coming up to the 2-year anniversary of "[Cheating is all you need"](https://sourcegraph.com/blog/cheating-is-all-you-need). It’s absolutely insane how much has changed since then. If I could send this blog post back in time, my 2-years-ago self wouldn’t believe it.

Thanks to my boss Quinn Slack for blowing our minds with most of these ideas a week ago. Hope you found this useful in some way. I'm off to fart on some investors. Ciao!

‍
