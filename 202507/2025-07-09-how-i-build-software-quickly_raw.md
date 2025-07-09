Title: How I build software quickly

URL Source: https://evanhahn.com/how-i-build-software-quickly/

Published Time: 2025-07-08T00:00:00+00:00

Markdown Content:
Software is built under time and quality constraints. We want to write good code and have it done quickly.

If you go too fast, your work is buggy and hard to maintain. If you go too slowly, nothing gets shipped. I have not mastered this tension, but I’ll share a few lessons I’ve learned.

This post focuses on being a developer on a small team, maintaining software over multiple years. It doesn’t focus on creating quick prototypes. And this is only based on my own experience!

“How good should this be?”
--------------------------

Early in my career, I wanted all my code to be perfect: every function well-tested, every identifier elegantly named, every abstraction easily understood. And absolutely no bugs!

But I learned a lesson that now seems obvious in hindsight: there isn’t one “right way” to build software.

For example, if you’re making a game for a 24-hour game jam, you probably don’t want to prioritize clean code. That would be a waste of time! Who really cares if your code is elegant and bug-free?

On the other hand, if you’re building a pacemaker device, a mistake could really hurt someone. Your work should be much better! I wouldn’t want to risk my life with someone’s spaghetti code!

Most of my work has been somewhere in the middle. Some employers have aggressive deadlines where some bugs are acceptable, while other projects demand a higher quality bar with more relaxed schedules. Sussing this out has helped me determine where to invest my time. **What is my team’s idea of “good enough”?** What bugs are acceptable, if any? Where can I do a less-than-perfect job if it means getting things done sooner?

**In general, my personal rule of thumb is to aim for an 8 out of 10 score, delivered on time.** The code is good and does its job. It has minor issues but nothing major. And it’s done on time! (To be clear, I _aim_ for this. I don’t always hit it!) But again, it depends on the project—sometimes I want a perfect score even if it’s delayed, and other times I write buggy code that’s finished hastily.

Rough drafts
------------

Software, like writing, can benefit from a rough draft. This is sometimes called a “spike” or a “walking skeleton”.

**I like implementing a rough draft as quickly as I can. Later, I shape it into the final solution.**

My rough draft code is embarrassing. Here are some qualities of my typical spikes:

*   Lots of bugs and failed test cases.
*   Dozens of `TODO` comments.
*   Error cases are not handled. (I recently had a branch where an error message was logged 20 times per second.)
*   `print()` statements everywhere.
*   No regard for performance.
*   Commit messages are just three letters: “WIP”, short for “work in progress”.
*   3 packages were added and none of them are used anymore.
*   Lots of code is unnecessarily repeated.
*   Data is hard-coded.
*   The linter is angry.

This sounds pretty bad, but it has one important quality: _it vaguely resembles a good solution_.

As you might imagine, I fix these mistakes before the final patch!

This “rough draft” approach has a few advantages:

*   **It can reveal “unknown unknowns”.** Often, prototypes uncover things I couldn’t have anticipated. It’s generally good to discover those ASAP, not after I’ve perfected some code that ultimately gets discarded.

*   **Lots of these problems disappear over the course of the rough draft and I never have to fix them.** For example, I write a function that’s too slow but works well enough for a prototype. Later, I realize I didn’t need that function at all. Good thing I didn’t waste time speeding it up! (I can’t tell you how many functions I’ve fully unit tested and then deleted. What a waste of time!)

*   It helps me **focus**. I’m not fixing a problem in another part of the codebase or worrying about the perfect function name. I’m speedrunning this rough draft to understand the problem better.

*   It helps me **avoid premature abstractions**. If I’m rushing to get something ugly working, I’m less likely to try to build some byzantine abstraction. I build what I need for the specific problem, not what I think I _might_ need for future problems that may never come.

*   It becomes easier to **communicate progress to others** in two ways: first, I can usually give a more accurate estimate of when I’ll be done because I know approximately what’s left. Second, I can demo _something_, which helps stakeholders understand what I’m building and provide better feedback. This feedback might change the direction of the work, which is better to know sooner.

Here are some concrete things I do when building rough drafts:

*   **Focus on binding decisions.** Some choices, like the selection of programming language or database schema design, can be hard to change later. A rough draft is a good time for me to explore these, and make sure I’m not boxing myself into a choice that I’ll regret in a year.

*   **Keep track of hacks.** Every time I cut a corner, I add a `TODO` comment or equivalent. Later, when it’s time for polish, I run `git grep TODO` to see everything that needs attention.

*   **Build “top to bottom”.** For example, in an application, I prefer to scaffold the UI before the business logic, even if lots of stuff is hard-coded. I’ve sometimes written business logic _first_, which I later discarded once the UI came into play, because I miscalculated how it would be used. Build the top layer first—the “dream code” I want to write or the API I wish existed—rather than trying to build the “bottom” layer first. It’s easier to make the right API decisions when I start with how it will be used. It can also be easier to gather feedback on.

*   **Extract smaller changes while working.** Sometimes, during a rough draft, I realize that some improvement needs to be made elsewhere in the code. Maybe there’s a dependency that needs updating. Before finishing the final draft, make a separate patch to just update that dependency. This is useful on its own _and_ will benefit the upcoming change. I can push it for code review separately, and hopefully, it’ll be merged by the time I finish my final draft.

_See also: [“Throw away your first draft of your code”](https://ntietz.com/blog/throw-away-your-first-draft/) and [“Best Simple System for Now”](https://dannorth.net/best-simple-system-for-now/). [“YAGNI”](https://martinfowler.com/bliki/Yagni.html) is also somewhat related to this topic._

Try to change the requirements
------------------------------

Generally, doing less is faster and easier! **Depending on the task, you may be able to soften the requirements.**

Some example questions to ask:

*   Could I combine multiple screens into one?
*   Is it okay if we don’t handle a particularly tricky edge case?
*   Instead of an API supporting 1000 inputs, what if it just supported 10?
*   Is it okay to build a prototype instead of a full version?
*   _What if we didn’t do this at all?_

More generally, I sometimes try to nudge the culture of the organization towards a slower pace. This is a big topic, and I’m no expert on organizational change! But I’ve found that making big demands rarely works; I’ve had better luck with small, gradual suggestions that slowly shift discussions. I don’t know much about [unionizing](https://drewdevault.com/2025/06/09/2025-06-09-Unionize-or-die.html), but I wonder if it could help here too.

Avoid wandering through the code
--------------------------------

The modern world is full of distractions: notifications from your phone, messages from colleagues, and dreaded meetings. I don’t have smart answers for handling these.

But there’s another kind of distraction: I start wandering through the code. I begin working on one thing, and two hours later, I’m changing something completely unrelated. Maybe I’m theoretically being productive and improving the codebase, but that bug I was assigned isn’t getting fixed! I’m “lost in the sauce”!

I’ve found two concrete ways to manage this:

*   **Set a timer.** When I start working on a discrete task, I often set a timer. Maybe I think this function is going to take me 15 minutes to write. Maybe I think it’ll take me 1 hour to understand the source of this bug. My estimates are frequently wrong, but when the timer goes off, I’m often jolted out of some silly distraction. And there’s nothing as satisfying as running `git commit` right as my timer goes off—a perfect estimation. (This also helps me practice the impossible art of time estimation, though I’m still not great at it.)

*   **Pair programming** helps keep me focused. Another soul is less likely to let me waste their time with some rabbit hole.

Some programmers naturally avoid this kind of distraction, but not me! Discipline and deliberate action help me focus.

Make small changes
------------------

The worst boss I ever had encouraged us to make large patches. These changes were wide in scope, usually touching multiple parts of the code at once. From my experience, this was terrible advice.

**Small, focused diffs have almost always served me better.** They have several advantages:

*   They are usually easier to write, because there’s less to keep in your head.
*   They are usually easier to review. This lightens teammates’ cognitive load, makes my mistakes easier to spot, and usually means my code is merged sooner.
*   They are usually easier to revert if something goes wrong.
*   They reduce the risk of introducing new bugs since you’re changing less at once.

I also like to **make smaller changes that build up to a larger one**. For example, if I’m adding a screen that requires fixing a bug and upgrading a dependency, that could be three separate patches: one to fix the bug, one to upgrade the dependency, and one to add the screen.

Small changes usually help me build software more quickly and with higher quality.

Skills that have been useful
----------------------------

Most of the above is fairly high-level. Several more specific skills have come in handy, especially when trying to build software quickly:

*   **Reading code** is, by far, the most important skill I’ve acquired as a programmer. I’ve had to work on this a lot! It helps in so many ways: debugging is easier because I can see how some function works, bugs and poor documentation in third-party dependencies are less scary, it’s a huge source of learning, and so much more.

*   **Data modeling** is usually important to get right, even if it takes a little longer. [Making invalid states unrepresentable](https://kevinmahoney.co.uk/articles/my-principles-for-building-software/#make-invalid-states-unrepresentable) can prevent whole classes of bugs. Getting a database schema wrong can cause all sorts of headaches later. I think it’s worth spending time to design your data models carefully, especially when they’re persisted or exchanged.

*   **Scripting.** Being able to comfortably write quick Bash or Python scripts has sped me up. I write a few scripts a week for various tasks, such as [sorting Markdown lists](https://evanhahn.com/simple-script-to-sort-markdown-lists/), cleaning up some data, or finding duplicate files. I highly recommend [Shellcheck](https://www.shellcheck.net/) for Bash as it catches many common mistakes. LLMs tend to be good at these scripts, especially if they don’t need to be robust.

*   **Debuggers** have saved me _lots_ of time. There’s no substitute for a proper debugger. It makes it much easier to understand what’s going on (whether there’s a bug or not!), and quickly becomes faster than `print()`-based debugging.

*   **Knowing when to take a break.** If I’m stuck on a problem without making progress, I should probably take a break. This has happened to me many times: I struggle with a problem for _hours_, step away for a few minutes, come back, and solve it in 5 minutes.

*   **Prefer pure functions and immutable data.** The functional programming style eliminates many bugs and reduces mental overhead. It’s often easier than designing complex class hierarchies. Not always practical, but it’s my default choice.

*   **LLMs**, despite their issues, can accelerate some parts of the development process. It’s taken me awhile to understand their strengths and weaknesses, but I use them in my day-to-day programming. Lots of ink has been spilled on the topic of LLM-assisted software development and I don’t have much to add. I like the [“vibecoding” tag on Lobsters](https://lobste.rs/t/vibecoding), but there are lots of other places to read.

All of these are skills I’ve practiced a bunch, and I feel the investment has made me a faster developer.

Summary
-------

Here’s a summary of things I’ve learned about building software quickly:

*   Know how good your code needs to be for the task at hand.
*   Start with a rough draft/spike.
*   Try to soften requirements if you can.
*   Don’t get distracted.
*   Make small changes.
*   Practice specific skills.

Everything in this list seems obvious in hindsight, but these are lessons that took me a long time to learn.

I’m curious to what _you’ve_ discovered on this topic. Are there more tricks to know, or practices of mine you disagree with? [Contact me any time.](https://evanhahn.com/contact/) I’d love to learn from you!

_Thanks to the anonymous reviewers who provided feedback on drafts of this post._
