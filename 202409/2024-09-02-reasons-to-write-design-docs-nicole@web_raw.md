Title: Reasons to write design docs

URL Source: https://ntietz.com/blog/reasons-to-write-design-docs

Markdown Content:
Sometimes I joke that as a principal engineer, my main programming language is English. It's half true, though, since my job is as much about people and communciation as it is about technology. Probably more, actually.

Writing is useful at all levels of software engineering. It's not just something for tech leads, architects, and principal engineers. We write all the time, whether it's comments in code, descriptions in Jira, messages in Slack, or design documents in a wiki. We don't do this because it's fun; most engineers I've met don't _love_ writing[1](https://ntietz.com/blog/reasons-to-write-design-docs#love-writing). We do it because it's useful.

I've generally run into four main ways that writing design docs ends up being useful for me and the teams I'm on. There may be more, and there are also ways they're _not_ useful. Here they are with pithy summaries of how they're useful or not, with links to the full sections.

*   [Writing a design doc helps you think, leading to better designs.](https://www.ntietz.com/blog/reasons-to-write-design-docs/#think-better)
*   [Collaborating on a design doc with teammates improves the design.](https://www.ntietz.com/blog/reasons-to-write-design-docs/#collab-better)
*   [Sharing the design doc with teammates broadens the organization's understanding of the design.](https://www.ntietz.com/blog/reasons-to-write-design-docs/#share-better)
*   [Referring back to the design doc tells you why a decision was made.](https://www.ntietz.com/blog/reasons-to-write-design-docs/#remember-better)
*   [Reading a design doc _will not_ tell you how the system works!](https://www.ntietz.com/blog/reasons-to-write-design-docs/#understand-unhelpful)

Let's see how these shake out! If you have any others, I'd love to hear them!

Writing design docs helps you think
-----------------------------------

A popular conception of a really good engineer is that if you tell them a problem, they'll quickly tell you a solution. With software teams, we sort of expect to tell them a problem and have them go heads down on the keyboard cranking out code. Hands on keyboards, folks!

That's not how solving problems really works, though. For many things, I can probably give you _a_ solution quickly. But it might be fatally flawed, and it certainly won't be optimal. There wasn't time to think through all the details!

This is where writing a design doc really helps with design. There's a lot written about other techniques for thought, like going for walks and writing by hand. I highly recommend these and they're where I get most of my best ideas for how to solve problems. But writing a design doc isn't usually about generating the _ideas_. It's about expanding them and checking them and being thorough, and finding where your gaps are so you can solve the problems you didn't see yet.

Putting a design into words and diagrams means that you have to make the design more concrete. Instead of handwaving about it, it goes down onto the page. You can start to see the complexity of the system, so you can start thinking about how to chop out parts of that complexity. Most of all, it lets you see things that just plain don't make sense. Countless times, I've run into things that made sense in my head but as I type it out, I just _know_ it can't possibly work. It's much better to find that out before you try to implement it!

Collaborating on a design doc improves the design
-------------------------------------------------

Writing a design doc by yourself is useful, and I use them for a lot of solo projects. But they're _much_ better with other people to collaborate with.

By yourself, you have blind spots. Have you ever written a sentence where you you had a word repeated twice in a row[2](https://ntietz.com/blog/reasons-to-write-design-docs#repetition), then read past it multiple times while editing? It's amazing what our brains fail to see. There are some techniques to notice those repeated words in writing, like reading it aloud, but little beats having someone else proofread it.

When someone else reads your design doc, you get similar benefits. They come into it with fresh eyes. They'll find those double words, and they'll also spot areas where you've missed the mark on your design. Any time a reader has a question about the doc, it's a signal that the document is unclear, and you should edit or rewrite part of it.

It's pretty easy to collaborate on these documents in a work setting. It is harder to get reviews for design documents for personal projects, but it is possible! For this, I like to have friends read over the design and give me feedback, and I return the favor for them.

It's clear to me that _writing_ a design doc is useful in itself, and I would keep doing it even if I just burned the document immediately after writing it. The process of writing helps us! But the benefits go so much further than that in an organization.

Imagine a software engineering org where every team makes its design decisions by talking out loud and scribbling on the whiteboard, then jumps to code without a design doc. You might work at one right now! How do you find out what other teams are working on?

In orgs like this one, a lot of knowledge and news is just passed by word of mouth. You get coffee with your friend from another team, and she tells you that they're using a new database. Coffee with another friend, and he tells you that they've created a new kind of user account. These would have been nice to know for your team! And then you start wondering about why we use the _current_ database, so you ask your tech lead when you return from coffee, and they tell you what their previous tech lead told _them_.

Poems and songs used to be passed down by oral tradition. Many still are, but many have also been lost to time because they were never written down, and others have evolved in unknowable ways over the eons. When we don't have design docs, then our understanding of the design is itself an oral tradition. We learn it by passing around news and lore. As people come and go from the company, this understanding may be corrupted or may vanish entirely.

When we share design docs after writing them, we reduce these issues. Now it's easier to see what changes other teams are working on: just read their design docs. Since these docs are shared, everyone can get a common understanding of what changes are happening, and you get better organizational knowledge.

They also help you understand _why_ a previous decision was made.

Referring to old design docs tells you why a decision was made
--------------------------------------------------------------

There is a famous story about a fence, told by one [Chesterton](https://en.wikipedia.org/wiki/Wikipedia:Chesterton%27s_fence). Someone wanted to remove a fence, and they weren't allowed to until they could figure out the reason it was put there in the first place. You don't typically build a fence for no reason, so don't remove it if you don't know why it's there. This comes up a lot in software engineering, because we've all seen seemingly unnecessary bits that end up being load bearing fixes for critical bugs or edge cases.

Without design docs, you have to try to piece together an understanding of why something is the way it is. In the best case scenario, you can ask a coworker. As an early employee at multiple companies, I've served in this role, which is also why I like design docs—I shouldn't be a single point of failure and my knowledge shouldn't all leave with me! If you don't have anyone to ask, you can scrounge through the code for clues and look at the commit history. However, commit history often gives you an incomplete picture of the "why" behind a change.

It's much better to refer back to the original design doc associated with a change, if there is one. Then you can see in the author's own words what changes they were intending to make and _why_ they wanted to do that. In some cases, even the initial implementation and design doc drift apart, and they certainly will after much time has passed. Regardless, the _intention and reasoning_ let you see what problem was being solved. With that knowledge in hand, you can be more confident with your own changes.

To make those changes, though, you still have to understand the system in its current state.

Reading a design doc will not tell you how the system works now
---------------------------------------------------------------

Unfortunately, design docs cannot tell you how a system works right now. At best, they're an approximation of how it worked at one point in time. Even if they're written right now, their correctness relies on one person or a small group of people understanding how the system works. This understanding often has so many holes that it looks like swiss cheese!

Design docs sit as snapshots of changes or of an overall architecture. The doc tells you what the intention and problem were, but not even if it got implemented. Some teams strive to update these docs, but that relies on human discipline to do so. I mean... have you _met_ humans? We're pretty bad at that followup thing, so relying on updates is fraught.

They're even worse for overall system architecture. They can give you a view of how someone _thinks_ the system works, but they won't tell you how the system _actually_ works. For a sufficiently large software system (almost all of it), it's too big for any one person to fit in their head. We can't fit the whole design with full correctness and all details into our heads.

It's not all worthless, though, because even that approximation gives you a _starting point_. It tells you what other people understood about this system and lets you get started. You can go from there to look at the code and see what was actually implemented or how things work now. You start with something to anchor from instead of a complete blank slate.

You should probably write more
------------------------------

Design docs are one form of writing that is pretty essential for software engineering teams. Without them, you're just not going to make good decisions, and you'll end up slower in the long run. Bad decisions compound and slow you down.

They're just one form of writing that helps us, though. There are many others. Writing can feel unproductive, because it's not _code_, but it's essential.

The beauty of writing is that it is communication that lasts. We invented writing for a reason, instead of persisting with only oral traditions. When you write something down, more people can read it and benefit from it for longer.

Most teams I've seen don't have enough writing in place. I totally get it, because I have the same instincts and fall into the same traps, and _my_ starting point is that I _love_ to write. Even with that, I will routinely start on things for my own projects (and even at work, ssshhhh) without a solid design doc. This is a mistake, and we should write more of these!

But not just design docs, we should write more in general. Communication is key to, well, everything in life? Writing is a fantastic way to communicate. If you write some fiction, an essay, or a poem, each of these will ultimately improve your communication. And then hey, maybe you've used your love of productivity to hack your brain into letting you do something fun for yourself.

* * *

Thank you to [Erika Rowland](https://erikarow.land/) and [Eugenia Tietz-Sokolskaya](https://sokolskayatranslations.com/) for feedback on a draft of this post.

* * *

If this post was enjoyable or useful for you, **please share it!** If you have comments, questions, or feedback, you can email [my personal email](mailto:me@ntietz.com). To get new posts and support my work, subscribe to the [newsletter](https://www.ntietz.com/newsletter/). There is also an [RSS feed](https://www.ntietz.com/atom.xml).
