Title: What Even Is Vibe Coding?

URL Source: https://ashley.dev/posts/what-even-is-vibe-coding

Published Time: 2025-05-07T00:00:00.000Z

Markdown Content:
When I first heard the phrase _vibe coding_, I rolled my eyes a little. It sounded like another fleeting buzzword, one of those things that shows up in a thread, gets memed into the ground, and disappears before it ever really lands. As someone who respects the craft of building software, the idea of _just vibing_ through development felt like it was missing the point entirely.

And honestly, if you had asked me, even just four weeks ago, whether I’d be writing a blog post about vibe coding, I probably would’ve LOL’ed.

But then I saw where it came from.

The term popped up in early 2025 from [Andrej Karpathy](https://x.com/karpathy/status/1886192184808149383), who described it like this:

> Fully giving in to the vibes. See things, say things, run things, copy paste things. No reading the diffs. Just vibes.

At first glance, it reads like satire. But underneath the humor is something real: a different way of working. Vibe coding, at its core, is about using natural language to tell an AI coding assistant what you want, and then watching it try to build it for you. You’re not manually managing logic or carefully threading state through components, you’re describing intent and letting the model do the busywork.

The first time I saw it in action, I thought, “There’s no way this scales.” But the more I tried it myself and the more I watched others experiment, the harder it became to write it off.

The Room’s a Bit Divided
------------------------

When I brought up vibe coding on [Threads](https://www.threads.com/@ashley_n_willis/post/DJFpef7zuGc?xmt=AQF0ZG9HS6xnQd33HkJD0NcHZEN51NRZ3dyWRbb1BC5UkQ), people had feelings. Some immediately dismissed it as sloppy or unserious. Others were curious but skeptical. It felt like one of those moments where the tech community splits into “this is the future” and “this is a joke,” and neither side is really wrong.

Over on [Bluesky](https://bsky.app/profile/ashley.dev/post/3lo2tqeuar222), the tone was a little more exploratory. Devs were sharing their wins and fails, people building quick prototypes with nothing more than a vision, or talking about how easy it was to fall into the trap of blindly shipping untested code. The consensus seemed to be: it’s fast, it’s fun, but you still have to think. Vibe coding might be a useful tool in the early stages of a project, but it’s not quite ready to carry the full weight of production.

And that’s fair. The whole conversation hints at something deeper: how do we evolve our workflows without letting quality slip through the cracks?

So What _Is_ Vibe Coding Now?
-----------------------------

Originally, vibe coding meant letting go entirely, describe what you want, hit run, and see what happens. You don’t read the code. You don’t edit it. You trust the output, or at least pretend to. That was the bit that made a lot of us nervous.

[Simon Willison](https://simonwillison.net/2025/May/1/not-vibe-coding/) pushed back on the way the term started evolving. He said:

> Vibe coding does not mean ‘using AI tools to help write code.’ It means ‘generating code with AI without caring about the code that is produced.

And he’s not wrong. But language shifts. And lately, “vibe coding” has been getting used as shorthand for _any_ AI-assisted development, even when the dev is still reviewing the output, writing tests, and guiding the structure. In other words: we started using “vibe coding” to describe something much more responsible than the name implies.

That kind of semantic drift isn’t new. We’ve seen it happen with words like “cloud” and “serverless.” And while it can be frustrating, it also reflects the reality that people are experimenting. They’re using the tools in ways that make sense to them, even if the vocabulary gets a little messy along the way.

A Little Skepticism Never Hurt
------------------------------

I’m not new to side-eyeing shiny new tech. I remember wondering if we _really_ needed iPads when they first came out. Why would I want a giant iPhone that doesn’t make calls? And yet, here we are, many of us using them daily (myself included) for things we didn’t even know we’d care about.

Same story with the cloud. Not the infrastructure itself, but the early marketing around it. It felt like buzzwords stacked on buzzwords. Elastic, scalable, serverless magic. But now? Try building anything serious without it. It’s the backbone of how we work.

I’ve been around long enough to know that new tools often sound silly before they sound useful. And honestly, that’s a good thing. A little skepticism keeps us grounded. It forces us to ask the uncomfortable questions early: What does this break? What does it replace? What does it make possible and for whom?

But I’ve also learned that some things need time to show their value. Especially when the first pitch is… let’s say, aspirational. AI coding assistants are kind of in that stage now. Some days, they feel like a party trick. Other days, they feel like the start of something real. I’m not convinced the dust has settled yet, but I’m paying attention. I think we all should be.

Vibe Coding Without Realizing It
--------------------------------

Lately, I’ve been spending more time with [GitHub Copilot’s](https://github.com/features/copilot/whats-new?utm_source=agent-awakens-announcement&utm_medium=blogtop&utm_campaign=agentic-ai) Agent mode and it turns out, I’ve been vibe coding without even realizing it.

As someone who builds creative side projects, quick experiments, and weird little tools that don’t need enterprise-grade rigor, I sometimes just open an empty repo, sketch out a vision in a README, and hand it off to GitHub Copilot in agent mode to see what happens. I describe the structure, the feel (yes, the vibe), and what I want the user to be able to do. Then I let the Agent take the first pass.

It scaffolds layouts, creates routes, fills in placeholder content, basically roughs out the shape of the thing I described. I still review it, refactor it, test it, and shape it into something I’d actually ship. But that first pass? It saves me hours. And more importantly, it frees up mental space so I can focus on the interesting parts.

A few weeks ago, I was doing exactly that, just messing around with a fun idea, seeing how far GitHub Copilot could take it, and afterward, it hit me: I had basically vibe coded the whole thing. I wasn’t ignoring the code. I still owned the final product. But I was definitely working from instinct, exploring an idea through natural language and iteration instead of planning every detail from the start.

Sometimes vibe coding doesn’t look like a radical new workflow. Sometimes it just looks like creative play and that’s not a bad thing.

A Word About Ethics (and Who This Helps… and Who It Doesn’t)
------------------------------------------------------------

AI generated code isn’t magic. It can be fast and impressive, but it still needs review. It can introduce bugs, security vulnerabilities, or quietly license code in ways that create downstream problems. Just like any other tool, it’s only as safe or responsible as the person using it.

Still, I’ve been thinking a lot about who this helps. Vibe coding lowers barriers. Whether you’re someone who struggles with focus, or just dipping in on a weekend to try something fun, it lets more people actually start. It helps people get unstuck when they can’t remember the syntax or the exact method name. That freedom to just start, that’s not nothing. For some folks, it’s what makes creating possible.

But I’ve also had my own quiet concerns about what this means for early-career developers. So much of how I learned came from chasing bugs in broken tutorials and seeing how all the pieces connected, or didn’t. There was value in that. And maybe I’ve been a little protective of it.

A mentor challenged that. He pointed out that debugging AI generated code is a lot like onboarding into a legacy codebase, making sense of decisions you didn’t make, finding where things break, and learning to trust (or rewrite) what’s already there. That’s the kind of work a lot of developers end up doing anyway.

So maybe this shift isn’t as dramatic as it feels. But it does mean we need to be intentional. As AI takes on more of the tedious setup and glue work, we need to rethink what we hand to junior devs. The path in might be different, but it still needs to exist. And it needs to be supported.

Of course, lowering barriers doesn’t just help the good actors. It also opens the door for people to build fast, messy, and potentially harmful systems without having the experience or ethics to understand what they’re unleashing. That kind of scale, in the wrong hands, is more than a nuisance. It’s a real risk.

And then there’s the labor side of this. As companies start using AI to justify shrinking engineering teams, flattening pay, or skipping mentorship entirely, that’s not the future of work. That’s just cutting corners. We’ve seen this story before, and the only thing new is the tool.

So yes, vibe coding has a lot of promise. But we also need to stay vigilant. To protect the parts of the craft that matter.

Where the Industry’s Headed
---------------------------

Whether you’re ready or not, AI assisted development is already here and the industry isn’t slowing down. Tools like GitHub Copilot are getting better at generating code in context. Product teams are building faster, shipping more, and rethinking what “developer productivity” even means.

There’s momentum, no doubt. But with that momentum comes pressure. Pressure to automate more. Pressure to reduce costs. Pressure to deliver without stopping to ask, _is this still good?_ Or _are we just moving fast because we can?_

And while it’s tempting to treat these AI coding assistants as an automatic upgrade to the dev stack, we haven’t really finished asking what’s downstream of that shift. Are we solving problems, or just doing more work faster? Are we giving teams more space to think or less?

I think vibe coding sits right in the middle of that tension. It’s more than just a cheeky phrase. It’s a reflection of the moment we’re in, a stand-in for the bigger questions we’re grappling with. How do we build responsibly when the scaffolding is done for us? What does creativity look like when the keyboard isn’t always in our hands? Who gets to build, and who benefits when they do?

Some days it feels like we’re evolving the craft. Other days it feels like we’re just accelerating it. But either way, it’s worth paying attention to the values we carry with us while we move forward.

Final Thoughts
--------------

So… what is vibe coding?

It’s still being figured out. Right now, it’s part meme, part mindset, and part reflection of how AI is changing the way we work. Some people use the term lightly. Others use it to describe a very real shift in how they interact with code.

I’m not here to tell you whether to love it or hate it. But I do think it’s worth exploring.

Try it. Prompt your way through something you’d normally scaffold by hand. See what the model comes up with. And then apply your judgment, your experience, to shape it into something real.

Because this isn’t about replacing the craft. It’s about redefining what the craft can include.

And if all you take from this is that you’re allowed to start with vibes and follow up with rigor, that’s a pretty good place to start.
