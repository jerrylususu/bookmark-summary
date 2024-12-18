Title: Problem Driven Development

URL Source: https://staysaasy.com/engineering/2024/12/17/problem-driven-development.html

Published Time: 2024-12-17T12:59:22+00:00

Markdown Content:
Figuring out what to do is a big part of senior tech roles. Senior Engineers and Engineering Managers often struggle to define technical roadmaps. Reasons include:

*   There’s little industry training on how to do it
*   It can be daunting to prioritize against professional PMs who are specifically selected and trained to be persuasive
*   Some organizations expect PMs to be responsible for all prioritization in teams, making Engineering roadmap ownership ambiguous

Oftentimes, good technical vision can feel like it has to be some gift from the heavens or a skill you’re born with. In reality, good technical vision is often a very simple and boring review of small amounts of data.

An easy playbook for technical roadmap development is Problem Driven Development. In short, it means you develop your technical roadmap based on fixing things that are going wrong. It sounds simple, but it can be very empowering.

Development Without Problems
----------------------------

The classic first-attempt by EMs/Senior Engineers at roadmap development is to ask people what they think the team should do. This usually ends in sadness, because:

*   Without time to think, people give bad answers.
*   People over-index on opinions of people in positions of authority. “The Chief Architect said this was a good idea!” They did, but they said that after a 2 minute chat, not after a deep understanding of the project and your roadmap.
*   People offer solutions, not problems to solve.

You get a list like:

*   Upgrade our library version to the next minor version
*   Refactor the Foo class to be composable
*   Try out the new hot SaaS thing for X

The implicit “we should do this because it solves X problem” gets lost. Three sprints later people start debating the solution in abstract without ever remembering why they were doing it in the first place.

The main fault with this approach is that it does not capture and solve the biggest problems.

When you prioritize solutions, your job is done once everyone agrees to do your idea. You can prioritize solutions for years and execute effectively without fixing your problems.

When you prioritize problems, you prioritize fixing the issues you actually have. You cannot prioritize problems for years and execute effectively and not solve your problems.

The a-ha moment is this: everything you’re doing should be solving a problem. Align your team on the biggest problems you have. Derive your technical roadmap based on solving those problems. Periodically revisit your problems list to make sure it is still accurate.

Problem Driven Development
--------------------------

OK, if you’re going to solve problems, you must figure out where they live. Most software teams have problems that live in the following places:

*   Pages
*   SLO violations
*   Wasted time in projects/tasks
*   Wasted time in development (e.g. slow CD)
*   Application alerts
*   Cost
*   Change failures

These failure repositories are auditable and you can directly build prioritized list of problems based off of them. When building a technical roadmap, you might end up with something like:

*   We get too many pages. 80% of them are the WizBang service. We need to drive that to 0.
*   We spend 12% of our time on manual tasks and we think we can reduce that by 50% with a month of work.
*   SLOs have been great, no work needed.

From here, you can figure out solutions you think solve these problems. It sounds very simple, but it’s a powerful way of figuring out what to do.

Problem Driven Development: Tech Debt
-------------------------------------

Tech debt prioritization is notoriously fraught and challenging in industry. One major contributor to this is that engineers are pretty bad at saying why tech debt is important. Another contributor is that PMs often require PM-level prioritization research to prioritize against product work, which is unfair. Teams then get in fights and land on %-based tech debt allotments to not have to deal with each other.

In any case, engineers ought to be better at doing reasonable due diligence on tech debt reasoning, e.g.:

*   The class sucks, ok what problems does that cause?
*   The problem is that it’s hard to code in.
*   OK how big of a problem is that?
*   What do you mean?
*   Besides it being gross, how much time are we wasting with it.
*   Well we only change it like once every two years.
*   OK so is that worth spending a month refactoring?
*   No, but this other file has the same issue and we modify it every week and its change fail rate is super high.
*   OK let’s fix that one.

Pretty quickly you can get to tech debt principles about wasted time, fail rates, and change frequency of issues if you frame things as solving problems and believe it can be done.

Regular-sized tech debt should just be addressed as people code other work in that area of the codebase. But if you’re asking a team to take the time to scope and prioritize work, you should have at least a miniscule amount of data to back up your claim. I’ve often found myself high conviction on a piece of tech debt until I actually researched the value in this way.

Problem Driven Development: Summary
-----------------------------------

Problem Driven Development is a theory so simple it sounds obvious. But I’ve seen many Engineers and Engineering Managers struggle to figure out what to do. And I’ve seen even more not have a framework to say no to a Senior Engineer who loves a solution that doesn’t solve a problem.

Some next steps:

*   If you find yourself in a position of needing to make a technical roadmap - find the problems, figure out the biggest ones, and make a plan to solve them.
*   If you’re a junior engineer wanting to work on your advocacy and vision, look at where your team’s problems live. Don’t stare at one class of code and lament the lack of design patterns. That’s where a single problem lives. Instead, look at the repositories that host the patterns of behavior that justify prioritization.
*   If you’re an EM that wants your team to have more vision, expose and educate them on the problems you’re having. I remember working at a major tech company and I was never remotely close to a holistic view of the problems my team was facing. If you only ever show people tickets, don’t cry when you have a team full of ticket-takers.
*   Whoever you are, always ground your team in the why of what you’re doing. Once you lose sight of the problem, you’ve definitely lost sight of the solution.

Problem Driven Development: Appendix
------------------------------------

Problem Driven Development is basically just ersatz product management. One irony, however, is that PMs can do Problem Driven Development to a fault. Customer’s problems are often much harder to get information about and take a very long time to gather. At the same time, your competitors might all have one feature that is clearly valuable that you don’t have. In that case, you shouldn’t be spending a bunch of time researching the problem just to get to the solution your competitors all have. More on this in a future post. Stay SaaSy everyone!
