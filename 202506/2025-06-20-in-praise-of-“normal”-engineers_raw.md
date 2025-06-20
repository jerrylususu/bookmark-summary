Title: In Praise of “Normal” Engineers

URL Source: https://charity.wtf/2025/06/19/in-praise-of-normal-engineers/

Published Time: 2025-06-19T17:11:50+00:00

Markdown Content:
_This article was originally [commissioned by Luca Rossi](https://refactoring.fm/p/in-praise-of-normal-engineers) (paywalled) for refactoring.fm, on February 11th, 2025. Luca edited a version of it that emphasized the importance of building “10x engineering teams” . It was later picked up by IEEE Spectrum (!!!), who scrapped most of the teams content and published a [different, shorter piece](https://spectrum.ieee.org/10x-engineer) on March 13th._

_This is my personal edit. It is not exactly identical to either of the versions that have been publicly released to date. It contains a lot of the source material for the talk I gave last week at #LDX3 in London, “[In Praise of ‘Normal’ Engineers](https://speakerdeck.com/charity/in-praise-of-normal-engineers-ldx3)” (slides), and a couple weeks ago at CraftConf._

Most of us have encountered a few engineers who seem practically magician-like, a class apart from the rest of us in their ability to reason about complex mental models, leap to non-obvious yet elegant solutions, or emit waves of high quality code at unreal velocity.![Image 1: In Praise of "Normal" Engineers](https://i0.wp.com/charity.wtf/wp-content/uploads/2025/06/normal-praise-black-squish.png?resize=174%2C174&ssl=1)

I have run into any number of these incredible beings over the course of my career. I think this is what explains the curious durability of the “10x engineer” meme. It may be based on flimsy, shoddy research, and the claims people have made to defend it have often been risible (e.g. “10x engineers have dark backgrounds, are rarely seen doing UI work, are poor mentors and interviewers”), or blatantly double down on stereotypes (“we look for young dudes in hoodies that remind us of Mark Zuckerberg”). But damn if it doesn’t resonate with experience. It just feels true.

The problem is not the idea that there are engineers who are 10x as productive as other engineers. I don’t have a problem with this statement; in fact, that much seems self-evidently true. The problems I do have are twofold.

Measuring productivity is fraught and imperfect
-----------------------------------------------

First: how are you measuring productivity? I have a problem with the implication that there is One True Metric of productivity that you can standardize and sort people by. Consider, for a moment, the sheer combinatorial magnitude of skills and experiences at play:

*   Are you working on microprocessors, IoT, database internals, web services, user experience, mobile apps, consulting, embedded systems, cryptography, animation, training models for gen AI… what?
*   Are you using golang, python, COBOL, lisp, perl, React, or brainfuck? What version, which libraries, which frameworks, what data models? What other software and build dependencies must you have mastered?![Image 2](https://i0.wp.com/charity.wtf/wp-content/uploads/2025/06/normal-rainbow-black.png?resize=173%2C173&ssl=1)
*   What adjacent skills, market segments, or product subject matter expertise are you drawing upon…design, security, compliance, data visualization, marketing, finance, etc?
*   What stage of development? What scale of usage? What matters most — giving good advice in a consultative capacity, prototyping rapidly to find product-market fit, or writing code that is maintainable and performant over many years of amortized maintenance? Or are you writing for the Mars Rover, or shrinkwrapped software you can never change?

Also: people and their skills and abilities are not static. At one point, I was a pretty good DBRE (I even co-wrote the book on it). Maybe I was even a 10x DB engineer then, but certainly not now. I haven’t debugged a query plan in years.

“10x engineer” makes it sound like 10x productivity is an immutable characteristic of a person. But someone who is a 10x engineer in a particular skill set is still going to have infinitely more areas where they are normal or average (or less). I know a lot of world class engineers, but I’ve never met anyone who is 10x better than everyone else across the board, in every situation.

Engineers don’t own software, teams own software
------------------------------------------------

Second, and even more importantly: So what? It doesn’t matter. Individual engineers don’t own software, teams own software. **The smallest unit of software ownership and delivery is the engineering team**. It doesn’t matter how fast an individual engineer can write software, what matters is how fast the team can collectively write, test, review, ship, maintain, refactor, extend, architect, and revise the software that they own.

Everyone uses the same software delivery pipeline. If it takes the slowest engineer at your company five hours to ship a single line of code, it’s going to take the fastest engineer at your company five hours to ship a single line of code. The time spent writing code is typically dwarfed by the time spent on every other part of the software development lifecycle.

If you have services or software components that are owned by a single engineer, that person is a single point of failure.![Image 3](https://i0.wp.com/charity.wtf/wp-content/uploads/2025/06/normal-spof.png?resize=226%2C226&ssl=1)

I’m not saying this should never happen. It’s quite normal at startups to have individuals owning software, because the biggest existential risk that you face is not moving fast enough, not finding product market fit, and going out of business. But as you start to grow up as a company, as users start to demand more from you, and you start planning for the survival of the company to extend years into the future…ownership needs to get handed over to a team. Individual engineers get sick, go on vacation, and leave the company, and the business has got to be resilient to that.

If teams own software, then the key job of any engineering leader is to craft high-performing engineering teams. If you must 10x something, 10x this. **Build 10x engineering teams.**

The best engineering orgs are the ones where normal engineers can do great work
-------------------------------------------------------------------------------

When people talk about world-class engineering orgs, they often have in mind teams that are top-heavy with staff and principal engineers, or recruiting heavily from the ranks of ex-FAANG employees or top universities.

But I would argue that a truly great engineering org is one where you don’t HAVE to be one of the “best” or most pedigreed engineers in the world to get shit done and have a lot of impact on the business.

I think it’s actually the other way around. A truly great engineering organization is one where perfectly normal, workaday software engineers, with decent software engineering skills and an ordinary amount of expertise, can consistently move fast, ship code, respond to users, understand the systems they’ve built, and move the business forward a little bit more, day by day, week by week.

Any asshole can build an org where the most experienced, brilliant engineers in the world can build product and make progress. That is not hard. And putting all the spotlight on individual ability has a way of letting your leaders off the hook for doing their jobs. It is a HUGE competitive advantage if you can build sociotechnical systems where less experienced engineers can convert their effort and energy into product and business momentum.

A truly great engineering org also happens to be one that mints world-class software engineers. But we’re getting ahead of ourselves, here.

Let’s talk about “normal” for a moment
--------------------------------------

A lot of technical people got really attached to our identities as smart kids. The software industry tends to reflect and reinforce this preoccupation at every turn, from Netflix’s “we look for the top 10% of global talent” to Amazon’s talk about “bar-raising” or Coinbase’s recent claim to “hire the top .1%”. (Seriously, guys? Ok, well, Honeycomb is going to hire only the top _.00001%_!)

In this essay, I would like to challenge us to set that baggage to the side and think about ourselves as _normal people_.

It can be humbling to think of ourselves as normal people, but most of us are in fact pretty normal people (albeit with many years of highly specialized practice and experience), and![Image 4](https://i0.wp.com/charity.wtf/wp-content/uploads/2025/06/normal-made-not-born.png?resize=264%2C264&ssl=1) there is _nothing wrong with that_. Even those of us who are certified geniuses on certain criteria are likely quite normal in other ways — kinesthetic, emotional, spatial, musical, linguistic, etc.

Software engineering both selects for and develops certain types of intelligence, particularly around abstract reasoning, but _nobody_ is born a great software engineer. **Great engineers are made, not born**. I just don’t think there’s a lot more we can get out of thinking of ourselves as a special class of people, compared to the value we can derive from thinking of ourselves collectively as relatively normal people who have practiced a fairly niche craft for a very long time.

Build sociotechnical systems with “normal people” in mind
---------------------------------------------------------

When it comes to hiring talent and building teams, yes, absolutely, we should focus on identifying the ways people are exceptional and talented and strong. But when it comes to building sociotechnical systems for software delivery, we should focus on all the ways people are _normal_.

#### ![Image 5](https://i0.wp.com/charity.wtf/wp-content/uploads/2025/06/normal-transp-rainbow.png?resize=122%2C122&ssl=1)

Normal people have cognitive biases — confirmation bias, recency bias, hindsight bias. We work hard, we care, and we do our best; but we also forget things, get impatient, and zone out. Our eyes are inexorably drawn to the color red (unless we are colorblind). We develop habits and ways of doing things, and resist changing them. When we see the same text block repeatedly, we stop reading it.

We are embodied beings who can get overwhelmed and fatigued. If an alert wakes us up at 3 am, we are much more likely to make mistakes while responding to that alert than if we tried to do the same thing at 3pm. Our emotional state can affect the quality of our work. Our relationships impact our ability to get shit done.

When your systems are designed to be used by normal engineers, all that excess brilliance they have can get poured into the product itself, instead of wasting it on navigating the system itself.

How do you turn normal engineers into 10x engineering teams?
------------------------------------------------------------

None of this should be terribly surprising; it’s all well known wisdom. In order to build the kind of sociotechnical systems for software delivery that enable normal engineers to move fast, learn continuously, and deliver great results as a team, you should:

#### Shrink the interval between when you write the code and when the code goes live.

Make it as short as possible; the shorter the better. I’ve written and given talks about this many, many times. The shorter the interval, the lower the cognitive carrying costs. The faster you can iterate, the better. The more of your brain can go into the product instead of the process of building it.

One of the most powerful things you can do is have a short, fast enough deploy cycle that you can ship one commit per deploy. I’ve referred to this as the “software engineering death spiral” … when the deploy cycle takes so long that you end up batching together a bunch of engineers’ diffs in every build. The slower it gets, the more you batch up, and the harder it becomes to figure out what happened or roll back. The longer it takes, the more people you need, the higher the coordination costs, and the more slowly everyone moves.

Deploy time is the feedback loop at the heart of the development process. It is almost impossible to overstate the centrality of keeping this short and tight.

#### Make it easy and fast to roll back or recover from mistakes.

Developers should be able to deploy their own code, figure out if it’s working as intended or not, and if not, roll forward or back swiftly and easily. No muss, no fuss, no thinking involved.

#### Make it easy to do the right thing and hard to do the wrong thing. ![Image 6](https://i0.wp.com/charity.wtf/wp-content/uploads/2025/06/normal-sparkles.png?resize=137%2C137&ssl=1)

Wrap designers and design thinking into all the touch points your engineers have with production systems. Use your platform engineering team to think about how to empower people to swiftly make changes and self-serve, but also remember that a lot of times people will be engaging with production late at night or when they’re very stressed, tired, and possibly freaking out. Build guard rails. The fastest way to ship a single line of code should also be the easiest way to ship a single line of code.

#### Invest in instrumentation and observability.

You’ll never know — not really — what the code you wrote does just by reading it. The only way to be sure is by instrumenting your code and watching real users run it in production. Good, friendly sociotechnical systems invest _heavily_ in tools for sense-making.

Being able to visualize your work is what makes engineering abstractions accessible to actual engineers. You shouldn’t have to be a world-class engineer just to debug your own damn code.

#### Devote engineering cycles to internal tooling and enablement.

If fast, safe deploys, with guard rails, instrumentation, and highly parallelized test suites are “everybody’s job”, they will end up nobody’s job. Engineering productivity isn’t something you can outsource. Managing the interfaces between your software vendors and your own teams is both a science and an art. Making it look easy and intuitive is really hard. It needs an owner.

#### Build an inclusive culture.

Growth is the norm, growth is the baseline. People do their best work when they feel a sense of belonging. An inclusive culture is one where everyone feels safe to ask questions, explore, and make mistakes; where everyone is held to the same high standard, and given the support and encouragement they need to achieve their goals.

#### Diverse teams are resilient teams.![Image 7](https://i0.wp.com/charity.wtf/wp-content/uploads/2025/06/normal-transp-rainbow.png?resize=196%2C196&ssl=1)

Yeah, a team of super-senior engineers who all share a similar background can move incredibly fast, but a monoculture is fragile. Someone gets sick, someone gets pregnant, you start to grow and you need to integrate people from other backgrounds and the whole team can get derailed — fast.

When your teams are used to operating with a mix of genders, racial backgrounds, identities, age ranges, family statuses, geographical locations, skill sets, etc — when this is just table stakes, standard operating procedure — you’re better equipped to roll with it when life happens.

#### Assemble engineering teams from a range of levels.

The best engineering teams aren’t top-heavy with staff engineers and principal engineers. The best engineering teams are ones where nobody is running on autopilot, banging out a login page for the 300th time; everyone is working on something that challenges them and pushes their boundaries. Everyone is learning, everyone is teaching, everyone is pushing their own boundaries and growing. All the time.

By the way — all of that work you put into making your systems resilient, well-designed, and humane is the same work you would need to do to help onboard new engineers, develop junior talent, or let engineers move between teams.

It gets used and reused. Over and over and over again.

The only meaningful measure of productivity is impact to the business
---------------------------------------------------------------------

The only thing that actually matters when it comes to engineering productivity is whether or not you are moving the business materially forward.

Which means…we can’t do this in a vacuum. The most important question is whether or not we are working on the right thing, which is a problem engineering can’t answer without help from product, design, and the rest of the business.

Software engineering isn’t about writing lots of lines of code, it’s about solving business problems using technology.

Senior and intermediate engineers are actually the workhorses of the industry. They move the business forward, step by step, day by day. They get to put their heads down and crank instead of constantly looking around the org and solving coordination problems. If you have to be a staff+ engineer to move the product forward, something is seriously wrong.

Great engineering orgs mint world-class engineers
-------------------------------------------------

A great engineering org is one where you don’t HAVE to be one of the best engineers in the world to have a lot of impact. But — rather ironically — great engineering orgs mint world class engineers like nobody’s business.

The best engineering orgs are not the ones with the smartest, most experienced people in the world, they’re the ones where normal software engineers can consistently make progress, deliver value to users, and move the business forward, day after day.![Image 8](https://i0.wp.com/charity.wtf/wp-content/uploads/2025/06/normal-system-does.png?resize=253%2C253&ssl=1)

Places where engineers can get shit done and have a lot of impact are a magnet for top performers. Nothing makes engineers happier than building things, solving problems, making progress.

If you’re lucky enough to have world-class engineers in your org, good for you! Your role as a leader is to leverage their brilliance for the good of your customers and your other engineers, without coming to depend on their brilliance. After all, these people don’t belong to you. They may walk out the door at any moment, and that has to be okay.

These people can be phenomenal assets, assuming they can be team players and keep their egos in check. Which is probably why so many tech companies seem to obsess over identifying and hiring them, especially in Silicon Valley.

But companies categorically overindex on finding these people after they’ve already been minted, which ends up reinforcing and replicating all the prejudices and inequities of the world at large. Talent may be evenly distributed across populations, but opportunity is not.

Don’t hire the “best” people. Hire the right people.
----------------------------------------------------

We (by which I mean the entire human race) place too much emphasis on individual agency and characteristics, and not enough on the systems that shape us and inform our behaviors.

I feel like a whole slew of issues (candidates self-selecting out of the interview process, diversity of applicants, etc) would be improved simply by shifting the focus on engineering hiring and interviewing away from this inordinate emphasis on hiring the BEST PEOPLE and realigning around the more reasonable and accurate RIGHT PEOPLE. ![Image 9](https://i0.wp.com/charity.wtf/wp-content/uploads/2025/06/normal-hire.png?resize=182%2C182&ssl=1)

It’s a competitive advantage to build an environment where people can be hired for their unique strengths, not their lack of weaknesses; where the emphasis is on composing teams rather than hiring the BEST people; where inclusivity is a given both for ethical reasons and because it raises the bar for performance for everyone. Inclusive culture is what actual meritocracy depends on.

This is the kind of place that engineering talent (and good humans) are drawn to like a moth to a flame. **It feels good to ship**. It feels _good_ to move the business forward. It feels _good_ to sharpen your skills and improve your craft. It’s the kind of place that people go when they want to become world class engineers. And it’s the kind of place where world class engineers want to stick around, to train up the next generation.

<3, charity
