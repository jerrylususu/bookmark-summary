Title: Preferring throwaway code over design docs

URL Source: https://softwaredoug.com/blog/2024/12/14/throwaway-prs-not-design-docs

Markdown Content:
We imagine software efforts that go through a clean, neat flow:

We write a design doc. Then make small incremental changes in a PR to rollout the functionality. Our git histories look clean and orderly. Like a steady march of progress.

> “Were it so Easy” The Arbiter, The Halo Series

It’s a bit of a delusion that we can take a design doc and go straight to clean gradual rollout of every step. I can guarantee you that once you start coding you’ll eat your design docs words.

> “No plan survives contact with the enemy” Eisenhower

We need to hack to find the design. We need to make a giant mess of code to make an actual plan. Making a giant mess then figuring out how to pick up the pieces might be the most efficient form of design out there.

I prefer a bit of a different design methodology-coding binges. Basically go through the following steps.

1.  Use a draft PR you don’t intend to merge. Implement your prototype or proof of concert
2.  Get eyes on the PR early - “what do you think of this approach to giant refactor/feature” etc to get alignment on an approach
3.  Document your approach in the draft PR - as a historical artifact of a design idea
4.  Be prepared to completely discard the draft PR - as early as possible
5.  Stage PRs out of the draft PR incrementally - take a week to stage clean productionizable PRs. Link your draft PR as a documentation artifact
6.  Fill in your testing, robustness gaps gradually as you stage each PR.

Important in this methodology is a great deal of maturity. Can you throw away your idea you’ve coded or will you be invested in your first solution? A major signal for seniority is whether you feel comfortable coding something 2-3 different ways. That your value delivery isn’t about lines of code shipped to prod, but organizational knowledge gained.

That’s also why you get alignment early on the most important parts. So you’re ongoing prototyping work isn’t a waste. Fail early, gather that organizational knowledge, get to the next idea…

Of course, you need to feel comfortable enough in the codebase to wire together the essenital parts fast. For senior employees, I feel you need to get to this comfort level. Or this can be a team effort.

Another important point is on using PRs for documentation. They are one of the best forms of documentation for devs. They’re discoverable - one of the first places you look when trying to understand why code is implemented a certain way. PRs don’t profess to reflect the current state of the world, but a state at a point in time. A historical artifact. On the other hand, most design docs lie to you. They’re [undead documentation](https://softwaredoug.com/blog/2023/10/13/fight-undead-documentation). Unless you’re fastidious of keeping them up to date (most of us aren’t) they reflect an outdated view of reality.

This approach dovetails with show don’t tell. A prototype can be worth 1000 design docs. If you want to drive change, you don’t usually do it in docs, but in code. Yet with an undisciplined organization you run the risk of your prototype being seen as the answer, not the question. The org may assume it says “we should do this!” When it really should be “should we do this? Or some other thing?”

Finally what about design docs?

I don’t want to discourage them completely. They can be useful in the following cases:

*   To organize and archive feedback from many different stakeholders, managers, and outside teams. Github won’t serve for collaborating. You can still go on the ‘coding binge’ to show your idea, but need a venue to discuss beyond Github.
*   Your ideas are so notional and long term, you can’t easily code them. In this case, some level of “North Star” document can be useful, with the next problem being how to actually get hands on keyboard with code
*   If you express in writing an idea more efficiently than coding a first draft. You’re not onboarded enough yet, and want to get something down for feedback.
*   Your company doesn’t have the discipline to throw away first solutions. And instead pushes to ship it to prod _right now_!!! So you hesitate to show don’t tell for fear of it becoming ‘the solution’.
*   Your junior employees don’t feel comfortable pushing back when senior developers build something as an idea, so you want to create a ‘softer’ artifact they can more safely question

Design docs can be used for bad reasons:

*   To ‘slow down’ the process for team members with less disciplined or skilled developers
*   As documentation - they’re usually outdated pretty fast
*   To answer all the design questions - you won’t discover the real problems until you write code

Still, I think IF your team can be discipilned, you’ll be far more efficient hacking than ‘designing’. I encourage you to create this discipline in your org. After all code speaks louder than words.
