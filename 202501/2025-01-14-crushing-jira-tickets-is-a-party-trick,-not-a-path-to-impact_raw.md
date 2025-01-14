Title: Crushing JIRA tickets is a party trick, not a path to impact

URL Source: https://www.seangoedecke.com/party-tricks/

Markdown Content:
Don’t be a JIRA ticket zombie! I think a common experience among ambitious juniors - certainly I did this once - is to get frustrated at the slow pace of a team and decide “screw it, I’ll just burn through all these tickets”. On many teams, it’s not that hard to do 2x or 3x more tickets than the next most productive person. But this is a dead end. You’ll get a pat on the head, told “nice work, don’t burn yourself out”, and no progress towards a senior promotion.

Everything you could want from a company - promotions, bonuses, internal respect - comes from [shipping _projects_](https://www.seangoedecke.com/how-to-ship), not from closing out tickets. It can still be useful to go through a stage of churning out tickets: to learn how fast you can work, to get rapid familiarity with the codebase, and to build some credit with your colleagues. But at some point you need to transition from doing whatever work is in front of you to prioritizing the work you think is the most important.

### How do you work on important things?

What determines importance? Importance at a tech company is **whatever your directors/VPs/C-staff say it is**. I mean that quite literally. Your job as an engineer is to execute on the strategy of the company, and since that strategy is set by executives, your job is to make sure you’re aligned with what they consider important. In any remotely functional company, they will tell you (over and over) what that is. You should pay attention when they do[1](https://www.seangoedecke.com/party-tricks/#fn-1).

Try to be ruthless about dropping work that is no longer important. If you ship a project and your management chain begins talking about the next thing, _stop improving that project_. In my experience, continuing to work on an already-shipped project is a very common mistake. Declare victory and walk away!

The formula for prioritizing is literally this simple:

1.  Am I working on the most important thing right now?
2.  If not, drop what I’m doing and go do that

You should be asking yourself this at least twice a day. That’s the first mistake I see lots of engineers make: not even really trying to prioritize, just coming in every day and continuing work on whatever they were doing the day before, or picking up a new JIRA ticket.

The second mistake is not having a sense of what the most important thing is. Here’s how I figure that out in practice:

1.  Is there an ongoing high-visibility incident going on (e.g. directors/VPs are asking about it)? If so, can I help with that?
2.  Are there any open questions in Slack/JIRA/etc that I’m able to answer? Is there anyone waiting for a response from my team?
3.  For each project that I’m leading, in order of importance: could it ship right now? If not, is there anything I could do right now to speed that up (any code that needs to be deployed or PRs that need reviewing)?
4.  For each project that my team is working on, in order of importance: is there any work available to be picked up that would move it along?
5.  Are there any tickets on the JIRA board in “ready for work”?

Note that going to the JIRA board is the _last_ step, not the first step. Remember, companies care about projects, not tickets.

If you get this right - if you only spend your time on the most important thing - you can be hugely impactful with much less than 40 hours of work per week. Companies are so full of engineers who work without conscious direction that doing one or two useful things per day will immediately make you unusually productive.

### It’s not your manager’s fault

Here’s a story about the angriest I’ve ever been at work. Early in my career I was deeply invested in keeping a suite of staging integration tests green. It was really hard work: keeping them up-to-date as the app changed, making sure the stateful parts (e.g. the pool of accounts) were healthy, making the tests as resilient as possible to transient issues like slow connections, and so on. I sweated over it for _months_. We went from 90% red to near-100% green. And then in a meeting my manager made some passing comment suggesting I shouldn’t spend so much time on it, since it wasn’t that important.

I got up and left the meeting midway - the only time I’ve ever done that, before or since. I went to an empty meeting room, sat down, and updated my resume. I felt like the hard, important work I’d been doing had been completely dismissed. In hindsight, it’s a funny story. I was working so hard! But my manager was right to dismiss the work I was doing, because whatever I was doing it wasn’t my actual job.

I’ve seen this story play out many times. An engineer decides that some particular task is important (say, adding support for some obscure input format, or removing some piece of tech debt) and spends weeks or months working on this. They do all the correct Agile things: communicate early with their manager, create issues, break up their work into modular PRs. And then the first time this project conflicts with a _real_ company value, they’re told to drop it, which makes them furious (or sad) about all the wasted effort.

Is this a failure of management? Yes and no. In theory, their manager could have warned them early on that this was low-priority work and probably not worth their time. But managers often trust their senior engineers when those engineers tell them that technical work is important. Managers also tend to communicate gently about priorities: for instance, they’ll give lukewarm responses like “sure, if you think this is worth doing go ahead” instead of explicitly saying “I don’t see the value in this work”.

There’s another reason why managers aren’t reliable guides: the company’s stated values are often at odds with their real values. When I was obsessing over integration tests as a junior, my manager wasn’t about to tell me “actually, the company doesn’t care _that_ much if our integration tests are flaky”, because the company was doing a lot of internal messaging about the importance of integration tests. It was my responsibility to decide how seriously to take that, and to weigh that against the other tasks I had available to me.

### Be wary of convincing your company to do things

By far the easiest way to deliver value is to figure out what the most important thing your organization is doing and help with that. It can be difficult to figure out whether the company’s stated tenth highest priority is actually valuable, but the company’s stated top priority almost always is. You can usually just ask your manager (or your skip, if you have skip 1:1s) what their top priority is. Alternatively, pay attention to what your skip level and above are asking about in Slack or in meetings.

The hardest way to deliver value is to figure out an important thing that your organization _isn’t_ doing and try to convince them to do it. This is basically betting that your company’s executives have done a bad job of identifying what they want, and that you can do a better one.

Maybe you can! Particularly if your company works on developer tools (like GitHub), you might have a useful perspective. But it’s a big risk. Even if you succeed in convincing them it’s worth looking at, you’re unlikely to put it near the top of their priority list. The next time the wind changes, the project you worked so hard to push is probably going to stop being important. And then you’ll be in my position with the automated tests: deeply invested in a hard technical task that the company doesn’t value.

Don’t let me dissuade you from trying to sell the company on an idea. It’s some of the most satisfying work you can do. Just be cautious if you do go down that road - if it doesn’t work out, you might work away with zero return on the time you put in.

### Summary

*   Burning through JIRA tickets is a cool party trick, not a path to impact
*   To work on important tasks, pay deliberate attention to what your management chain thinks is important
*   Be ruthless about dropping unimportant work
*   Don’t rely on your direct manager to tell you what’s worth doing
*   Convincing your company that a task is important can work, but it’s risky
