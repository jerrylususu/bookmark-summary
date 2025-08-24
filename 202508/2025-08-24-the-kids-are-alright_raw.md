Title: The kids are alright

URL Source: https://www.bitecode.dev/p/the-kids-are-alright

Published Time: 2025-08-23T09:36:15+00:00

Markdown Content:
_Vibes coding is fine. And yes, the kids suck, but so did we. Let's appreciate we got new players entering the game, and focus on what's really important: improving safety nets._

Welp, Armin Ronacher wrote "[Welcoming The Next Generation of Programmers](https://lucumr.pocoo.org/2025/7/20/the-next-generation/)" before I had the chance, so I deleted my draft and figured out what else I could say on the matter.

Then I wrote this instead.

It has become fashionable to call out AI as being the harbinger of the end of time for code quality, especially for the new people joining in.

I see currently established devs mocking all mistakes made by the young ones:

*   Ha, that one is discovering the need for version control!

*   Look at those security holes!

*   This code is atrocious, and you don't know what it does!

People, let's be real for a minute. I've done all similar stupid things on my very own, and way worse, before it was cool to blame it on LLM.

Have old geeks forgotten how much they sucked when they started?

Maybe you were surrounded by geniuses when you began learning to program, but I certainly was not.

We were bad.

Scratch that.

We were terrible.

The logic was faulty, the style was awful, the technical choices were all over the place, the tooling was lacking, and the general understanding of what we were doing akin to a chicken with a Rubik's Cube.

My bugs had bugs, I struggled to get the concept of logging (on which I wrote my university memoir!), I invested a colossal time trying to configure SciTE just right, and installing PhPMyAdmin was my idea of being a great hacker.

Why would it be any different today?

Is that because kids are overconfident since they can get a demo up in 5 minutes using Cursor? Suddenly, that justifies the need to smash their head back down to the ground... for being kids?

Arrogant know-it-all nerds were not in short supply in my time either. I should know, I was one. Still am in my spare time.

AI has nothing to do with this.

It has nothing to do with the fact they suck.

It has nothing to do with the fact they are annoyingly and naively optimistic.

It has everything to do with the fact they are kids.

And they are kids in the open. Let's celebrate that! It's the new generation showing they want to play!

Sure, it's frustrating to see a twenty-something claiming they discovered a revolutionary concept when in fact it's been the industry standard for decades.

They lose their work, then will tweet they now zip it with timestamps so that they can go back if their agent messes up everything. And someone sarcastically says Soon they will invent SVN.

They introduce problems, and they will make a TikTok stating they will now write some code that will automatically verify that their software works in the future. Surely, there is mumbling about unit tests in the room.

Then again, with variable names, refactoring, side effects, the cost of the cloud, complexity being bad, and so on, and so on.

Ah, those dumb kids with their AI! Don't they know we've had this figured out forever?

No, they don't. That's the point of learning.

None of us knew, and we all learned either with IRL `try`/`except` or mentoring. But let's be real, even with mentoring, you need the trial and error.

I called a recursive `unlink()` on a script run as root on a prod server. I wrote a state machine out of ORM classes, using table inheritance to encode the states. I forced pushed an empty commit on master. I wrote an entire object system to represent if/else conditions. I reinstalled from scratch my machine with a new distro on the first day of a 48h Hackathon.

I once wrote a bot to send love messages to my GF while I would be in a no-electronic retreat. It had a flaw that made it send the same message 140 000 times over 10 days, and she hated me for a month.

Again, what's with all the hate lately?

The community is usually so supportive of experimentation, trying things out, and building while helping each other.

But as soon as AI is involved, it's like a black stain on whatever you do. You build? You are a great kid. You build with the help of AI? Everything you do suck, and you are a terrible human being.

None of the mistakes the kids are making today are remotely linked to AI.

Of course, the AI may now suggest many of those mistakes to them, and at a faster rate. But they would have come out with their own anyway.

In fact, they will make fewer mistakes with a good agent on their side; it is something I have been consistently witnessing for the last 2 years with beginners. They are _better_ than I used to be at their age.

Plus, even if you don't believe that, AI will make the feedback cycle shorter, which means they will hit the mistakes quickly and reach the learning moment sooner.

Scared of them diving too deep because AI will give them too much rope to hang themselves, and they will be crawling in generated code-mud by the time they realize there is a problem?

Who cares?

It's also a learning experience. They HAVE to feel the pain to learn. There is no alternative to that.

After all, how did we learned that needless code complexity, piles of tech debt, and over-engineering were a problem? The same way, except instead of an AI building it in a month over a non-critical project, we inherited the production system from 10 years of monkey coding from our colleagues. Or worse, from a sweat chop on the other side of the world.

I think their situation is better, actually.

[History rhymes](https://www.bitecode.dev/p/hype-cycles), right? Because I heard this one before.

I heard it when Stackoverflow became a thing, and we blamed those young devs copy/pasting from it. They didn't use their brain, didn't understand the code, and were going to bring doom to our whole industry.

I heard it when package managers became a thing, and we claimed those damn youngsters didn't know their dependencies, relied on black box, reached for Rube Goldberg framework and will end IT as we know it.

I heard it when Google became a thing, and we screamed those lazy apocryphal 56K-deniers didn't read the doc anymore, just fetched snippets on random unreliable blogs and couldn't be bothered to look at the damn source code. This surely will be the end of computing.

I heard it when simple dynamic languages became a thing, and we lamented those weak-minded mouse clickers didn't know how CPU worked, wasted full megabytes of memory, and wrote sluggish programs that couldn't even make a single manual system call. That's it. It's over.

But you know what all of those instances also had in common? If you point out to the critics they have been repeating the same stuff that the previous gen said about them, they will reply:

> Yeah, but this times it's different, because...

We have all been vibe coding forever. Let's stop pretending this is some kind of awful practice only the sinful zoomers indulge in.

We called it having fun, making an MVP, exploratory programming, hacking, trying things out, learning, seeing what's up, quick and dirty, whipping up something, fooling around, building a PoC (that will actually end up in prod for 10 years)... So basically 99% of all coding being done in the world.

I believe some of my clients call that being agile.

If one thinks putting a large language model in there makes it fundamentally different, this is just a huge blind spot. Those tools are simply the logical conclusions of automation in a field where automation is the main thing. It's more of the same.

"But it's not reliable!"

Yes, so?

Humans are not. Google searches are not. Hell, computers are not. There is no such thing as a pure function.

It's more of the same. Just bigger. Faster. Fuzzier.

And if the author of Flask and Redis can make it work for them, I think we all can.

All this commotion prevents us from focusing our efforts on what's important: making this inevitable transition much more comfortable for us.

If you think this is a fad, that this will go away, that AI will prove not to be that useful after all, there is nothing I can do for you. You can stop reading here. In fact, you can ban this blog at the DNS level because we both understand life in a fundamentally incompatible way.

However, if you have come to the realization that this is our reality now, and that it's just the beginning, we have work to do, you and I.

Because AI magnifies all the human traits, creativity and laziness, curiosity and tunnel vision, enthusiasm and apathy.

The benefits will flow by themselves; there is nothing to do but welcome them. And open our arms to the new generation of coders that will both create the software of tomorrow, invent new ways of working, and teach us how to do so.

The problems, however we have to actively deal with them.

I jested about dynamic languages, Google, package managers, and StackOverflow affecting code quality, but we did, actually, paid a price for those.

We did have many vulnerable Worldpress instances, we did have the [LeftPad story](https://en.wikipedia.org/wiki/Npm_left-pad_incident), and I'm sure many of us can recall crap being uploaded on some FTP on a Friday night.

AI will undoubtedly increase the volume on which it's possible to [fake job test proficiency](https://www.bitecode.dev/p/the-hiring-test-that-defeated-ai), [create wasteful bug reports](https://www.theregister.com/2025/05/07/curl_ai_bug_reports/), and [push bad contributions](https://www.phoronix.com/news/Linux-Kernel-AI-Docs-Rules).

It's now more important than ever to assign persons to responsibilities, with real cost and consequences for them, and give them the tools and resources to manage it. Skin in the game and put your money where your mouth is, so to speak.

Vibe coding is fine. Pushing code of dubious quality to a production system, however, must be harshly discouraged, even more than we used to. I'm more strict about code review, tests, and punishing irresponsible moves than I was before with my client's team.

Because it’s so tempting, it’s so easy to do. [Programming is hard](https://www.bitecode.dev/p/how-much-effort-is-it-to-create-software), and humans are like water, taking the path of least resistance.

That's the irony about the productivity we gain from AI. It must be reinvested in improving our safety net. **As the cost to produce code goes down, the cost to vet code must go up.**

Because it's the dirty little secret of our job, isn't it?

It's not really about the code.