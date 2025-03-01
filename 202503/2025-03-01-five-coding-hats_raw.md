Title: Five coding hats

URL Source: https://dubroy.com/blog/five-coding-hats/

Markdown Content:
February 3, 2025

Early in my career, I was convinced there was “good code” and “bad code”. That you could look at something and — without knowing anything about the context — pass judgement on it.

These days, my views are much more nuanced. I try to adapt my style to the situation. The code I write, and the process I use, depends a lot more on what the goals are. Am I trying to bang together a quick prototype to learn something? Or am I fixing a bug that might affect hundreds of thousands of users? My approach would be completely different in those two scenarios.

Years ago, I read Edward De Bono’s [Six Thinking Hats](https://en.wikipedia.org/wiki/Six_Thinking_Hats), which describes a framework for problem solving and creative thinking. The idea is that you can “put on a hat” to deliberately adopt a specific mode of thinking. It’s a bit corny but (imo) there’s a useful idea there.

Maybe this applies to different styles of programming, too? What “coding hats” do I use?

Captain’s hat 🧑‍✈️
-------------------

The captain’s hat is about doing things by the book: being careful, moving slowly and deliberately, following the proper procedures. This is attitude I’d adopt if a mistake could [crash 8.5 million systems](https://en.wikipedia.org/wiki/2024_CrowdStrike-related_IT_outages).

With the captain’s hat on, I’d focus on small, focused, independent commits — things that are easy to roll back if a problem occurs. I’d make sure my PRs include tests. I’d write descriptive commit messages and make sure the code is reviewed.

This is the closest thing to what I used to think “the right way” was. What I missed back and then — and it’s a big miss — is that this isn’t the right approach for all situations, not even close.

Scrappy hat 🐕
--------------

A few months ago, I was sharing a small prototype with a friend. Before I showed him the code, I felt the need to give some disclaimers: “This is deliberately written in a very minimal style”, “I was going for the simplest possible thing that could work”, stuff like that. Eventually I started thinking: _I wrote this with my scrappy hat on_.

The scrappy hat is about keeping things lean — taking the straightest possible path to your goal, and skipping the ceremony. No code reviews, minimal tests. Sometimes you just need something concrete to discuss; with the scrappy hat on, you can quickly throw something together and decide later if it’s worth keeping.

This is pretty close to the default mode that most small startups operate in. It’s the hat of the “minimum viable” and the 80-20.

MacGyver Hat 🛠️
----------------

The MacGyver hat is all about getting a result. Sometimes you don’t care what it takes, how messy the code is — you just need to figure out if something is possible, whether it’s worth spending more time on. It’s the quick-and-dirty, any-which-way, by-hook-or-by-crook mode.

I’ve used this hat before when I’m doing performance work. Maybe I have five different ideas to make something faster. They’d each take a day or two to implement cleanly, but if I don’t care what the code looks like, I can hack each one together in an hour. Once I know something has promise, I’ll put in the work to do it right.

Chef’s hat 🧑‍🍳
----------------

The chef’s hat is all about _presentation_. You want the code to look beautiful, in addition to serving its purpose. There are few real-world situations that truly call for the chef’s hat, but sometimes it’s just what you want to do.

Sometimes I’ll use this in a time-boxed way — once I’ve got the basic functionality working, I might “put on my chef’s hat” for thirty minutes and see if I can clean the code up a bit.

Like the captain’s hat, this one is sometimes mistaken for The Right Way, and is often overused. It’s easy to convince yourself that you’re doing something valuable, making the code more readable and maintainable. But often you’re just polishing for its own sake.

Teacher’s hat 🧑‍🏫
-------------------

With the teacher’s hat on, you’re concerned about _what your code communicates_, and not so much on what it actually does. You might want to use this if you’re writing example code for an open source project, or writing a blog post to explain a concept.

Maybe you skip error checking, because it obscures the main thing you’re trying to show. Or you use more descriptive variable and function names than you otherwise would. You don’t pick the most efficient solution, you use the most _understandable_ one.

Look, I’m not trying to convince you to adopt my framework. I won’t be doing corporate training workshops anytime soon. But I do think it’s worth being deliberate about what mode you’re operating in, and asking yourself if a different approach might be worth trying.

💬 _Want to leave feedback? [Send me an email](https://dubroy.com/blog/about/#contact) or respond on [Bluesky](https://bsky.app/profile/dubroy.com/post/3lhbm7722jd2g) or [Mastodon](https://hachyderm.io/@dubroy/113940096861433018)._

Related:

*   Thorsten: [Surely not all code’s worth it](https://registerspill.thorstenball.com/p/surely-not-all-codes-worth-it)
*   Jimmy: [Discovery coding](https://jimmyhmiller.github.io/discovery-coding)
