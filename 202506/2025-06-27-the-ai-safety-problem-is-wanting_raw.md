Title: The AI safety problem is wanting

URL Source: https://dynomight.net/wanting/

Published Time: 2025-06-26T00:00:00+00:00

Markdown Content:
I haven’t followed AI safety too closely. I tell myself that’s because tons of smart people are working on it and I wouldn’t move the needle. But I sometimes wonder, is that logic really unrelated to the fact that every time I hear about a new AI breakthrough, my chest tightens with a strange sense of dread?

AI is one of the most important things happening in the world, and possibly _the_ most important. If I’m hunkering in a bunker years from now listening to hypersonic kill-bots laser-cutting through the wall, will I really think, _boy am I glad I stuck to my comparative advantage_?

So I thought I’d take a look.

I stress that I am not an expert. But I thought I’d take some notes as I try to understand all this. Ostensibly, that’s because my outsider status frees me from the [curse of knowledge](https://en.wikipedia.org/wiki/Curse_of_knowledge) and might be helpful for other outsiders. But mostly, I like writing blog posts.

So let’s start at the beginning. AI safety is the long-term problem of making AI be nice to us. The obvious first question is, what’s the hard part? Do we know? Can we say anything?

To my surprise, I think we can: The hard part is making AI _want_ to be nice to us. You can’t solve the problem without doing that. But if you _can_ do that, then the rest is easier.

This is not a new idea. Among experts, I think it’s somewhere between “the majority view” and “near-consensus”. But I haven’t found many explicit arguments or debates, meaning I’m not 100% sure _why_ people believe it, or if it’s even correct. But instead of cursing the darkness, I thought I’d construct a legible argument. This may or may not reflect what other people think. But what is a blog, if not an exploit on [Cunningham’s Law](https://en.wikipedia.org/wiki/Ward_Cunningham#%22Cunningham's_Law%22)?

My argument, at a high level
----------------------------

Here’s my argument that the hard part of AI safety is making AI want to do what we want:

1.   To make an AI be nice to you, you can either impose _restrictions_, so the AI is unable to do bad things, or you can _align_ the AI, so it doesn’t _choose_ to do bad things.

2.   Restrictions will never work.

3.   You can break down alignment into making the AI _know_ what we want, making it _want_ to do what we want, and making it _succeed_ at what it tries to do.

4.   Making an AI _want_ to do what we want seems hard. But you can’t skip it, because then AI would have no reason to be nice.

5.   Human values are a mess of heuristics, but a capable AI won’t have much trouble understanding them.

6.   True, a super-intelligent AI would likely face weird “out of distribution” situations, where it’s hard to be confident it would correctly predict our values or the effects of its actions.

7.   But that’s OK. If an AI wants to do what we want, it will try to draw a conservative boundary around its actions and never do anything outside the boundary.

8.   Drawing that boundary is not that hard.

9.   Thus, if an AI system _wants_ to do what we want, the rest of alignment is not that hard.

10.   Thus, making AI systems _want_ to do what we want is necessary and sufficient-ish for AI safety.

I am not confident in this argument. I give it a ~35% chance of being correct, with step 8 the most likely failure point. And I’d give another ~25% chance that my argument is wrong but the final conclusion is right.

(Y’all agree that a low-confidence prediction for a surprising conclusion still contains lots of information, right? If we learned there was a 10% chance Earth would be swallowed by an alien squid tomorrow, that would be important, etc.? OK, sorry.)

My argument, in more detail
---------------------------

I’ll go quickly through the parts that seem less controversial.

### 1. There are two conceivable paths to AI safety.

Roughly speaking, to make AI safe you could either impose _restrictions_ on AI so it’s not able to do bad things, or _align_ AI so it doesn’t choose to do bad things. You can think of these as not giving AI access to nuclear weapons (restrictions) or making the AI choose not to launch nuclear weapons (alignment).

### 2. Restrictions will never work.

I advise against giving AI access to nuclear weapons. Still, if an AI is vastly smarter than us and _wants_ to hurt us, we have to assume it will be able to jailbreak any restrictions we place on it. Given any way to interact with the world, it will eventually find some way to bootstrap towards larger and larger amounts of power. Restrictions are hopeless. So that leaves alignment.

### 3. You can break down alignment into three parts.

Here’s a simple-minded decomposition:

1.   **The Knowing problem**: Making AI know what we want.
2.   **The Wanting problem**: Making AI want to do what we want.
3.   **The Success problem**: Making AI succeed at what it tries to do.

I sometimes wonder if that’s a _useful_ decomposition. But let’s go with it.

### 4. Wanting is necessary.

The Wanting problem seems hard, but there’s no way around it. Say an AI _knows_ what we want and _succeeds_ at everything it tries to do, but doesn’t care about what we want. Then, obviously, it has no reason to be nice. So we can’t skip Wanting.

Also, notice that even if you solve the Knowing and Success problems _really_ well, that doesn’t seem to make the Wanting problem any easier. (See also: [Orthogonality](https://arbital.greaterwrong.com/p/orthogonality/))

### 5. Human values are a shallow mess.

My take on human values is that they’re a big ball of heuristics. When we say that some action is right (wrong) that sort of means that genetic and/or cultural evolution thinks that the reproductive fitness of our genes and/or cultural memes is advanced by rewarding (punishing) that behavior.

Of course, evolution is far from perfect. Clearly our values aren’t remotely close to reproductively optimal right now, what with fertility rates crashing around the world. But still, values are the result of evolution _trying_ to maximize reproductive fitness.

Why do we get confused by [trolley problems](https://en.wikipedia.org/wiki/Trolley_problem) and [population ethics](https://en.wikipedia.org/wiki/Population_ethics)? I think because… our values are a messy ball of heuristics. We never faced evolutionary pressure to resolve trolley problems, so we never really formed coherent moral intuitions about them.

So while our values have lots of quirks and puzzles, I don’t think there’s anything _deep_ at the center of them, anything that would make learning them harder than learning to solve Math Olympiad problems or translating text between any pair of human languages. Current AI [already](https://dynomight.net/puzzles-results/) seems to understand our values fairly well.

Arguably, it would be hard to _prevent_ AI from understanding human values. If you train an AI to do any sufficiently difficult task, it needs a good world model. That’s why “predicting the next token” is so powerful—to do it well, you have to model the world. Human values are an important and not that complex part of that world.

### 6. Distribution shift may make it harder for AI to Know or Succeed.

The idea of “distribution shift” is that after super-intelligent AI arrives, the world may change quite a lot. Even if we train AI to be nice to us _now_, in that new world it will face novel situations where we haven’t provided any training data.

![Image 1: learned values might diverge from training data](https://dynomight.net/img/wanting/cartoon.svg)

This could conceivably create problems both for AI _knowing_ what we want, or for AI _succeeding_ at what it tries to do.

For example, maybe we teach an AI that it’s bad to kill people using lasers, and that it’s bad to kill people using viruses, and that it’s bad to kill people using radiation. But we forget to teach it that it’s bad to write culture-shifting novels that inspire people to live their best lives but also gradually increase political polarization and lead after a few decades to civilizational collapse and human extinction. So the AI _intentionally_ writes that book and causes human extinction because it thinks that’s what we want, oops.

Alternatively, maybe a super-powerful AI _knows_ that we don’t like dying and it _wants_ to help us not die, so it creates a retrovirus that spreads across the globe and inserts a new anti-cancer gene in our DNA. But it didn’t notice that this gene also makes us blind and deaf, and we all starve and die. In this case, the AI _accidentally_ does something terrible, because it has so much power that it can’t correctly predict all the effects of its actions.

### 7. But all AI needs to do is draw a conservative boundary.

What are your values? Personally, very high on my list would be:

> If an AI is considering doing anything and it’s not _very_ sure that it aligns with human values, then it should not do it without checking _very_ carefully with lots of humans and getting informed consent from world governments. Never _ever_ do anything like that.

And also:

> AIs should never release retroviruses without being _very_ sure it’s safe and checking _very_ carefully with lots of humans and getting informed consent from world governments. Never ever, thanks.

That is, AI safety doesn’t require AIs to figure out how to generalize human values to all weird and crazy situations. And it doesn’t need to correctly predict the effects of all possible weird and crazy actions. All that’s required is that AIs can _recognize_ that something is weird/crazy and then be conservative.

Clearly, just detecting that something is weird/crazy is easier than making correct predictions in all possible weird/crazy situations. But how _much_ easier?

### 8. Drawing that boundary isn’t that hard.

(I think this is the weakest part of this argument. But here goes.)

Would I trust an AI to correctly decide if human flourishing is more compatible with a universe where up quarks make up 3.1% of mass-energy and down quarks 1.9% versus one where up quarks make up 3.2% and down quarks 1.8%? Probably not. But I wouldn’t trust any particular human to decide that either. What I _would_ trust a human to do is say, “Uhhh?” And I think we can also trust AI to know that’s what a human would say.

Arguably, “human values” are a thing that only exist for some limited range of situations. As you get further from our evolutionary environment, our values sort of stop being meaningful. Do we prefer an Earth with 100 billion moderately happy people, or one with 30 billion very happy people? I think the correct answer is, “No”.

When we _have_ coherent answers, AI will know what they are. And otherwise, it will know that we don’t _have_ coherent answers. So perhaps this is a better picture:

![Image 2: values only exist in a limited range](https://dynomight.net/img/wanting/limited.svg)

And this seems… fine? AI doesn’t need to Solve Ethics, it just needs to understand the limited range of human values, such as they are.

That argument (if correct) resolves the issue of distribution shift for _values_. But we still need to think about how distribution shift might make it harder for AI to succeed at what it tries to do.

If AI attains godlike power, maybe it will be able to change planetary orbits or remake our cellular machinery. With this gigantic action space, it’s plausible that there would be many actions with bad but hard-to-predict effects. Even if AI only chooses actions that are 99.999% safe, if it makes 100 such actions per day, calamity is inevitable.

Sure, but surely we want AI to take false discovery rates (“calamitous discovery rates”?) into account. It should choose a _set_ of actions such that, taken together, they are 99.999% safe.

Something that might work in our favor here is that verification is usually much easier than generation. Perhaps we could ask the AI to create a “proof” that all proposed actions are safe and run that proof by a panel of skeptical “red-team” AIs. If any of them find anything confusing at all, reject.

I find the idea that “drawing a safe boundary is not that hard” fairly convincing for human values, but not only semi-convincing for predicting the effects of actions. So I’d like to see more debate on this point. (Did I mention that this is the weakest part of my argument?)

### 9. Thus, if an AI system _wants_ to do what we want, the rest of alignment is not that hard.

It AI truly wants to do what we want, then the only thing it really needs to know about our values is “be conservative”. This makes the Knowing and Success problems much easier. Instead of needing to know how good all possible situations are for humans, it just needs to notice that it’s confused. Instead of needing to succeed at everything it tries, it just needs to notice that it’s unsure.

### 10. Thus, making AI systems _want_ to do what we want is necessary and sufficient for AI safety.

Since restrictions won’t work, you need to do alignment. Wanting is hard, but if you can solve Wanting, then you only need to solve easier version of Knowing and Success. So Wanting is the hard part.

Consistency with other views
----------------------------

Again, I _think_ the idea that “wanting is the hard part” is the majority view. Paul Christiano, for example, [proposes](https://ai-alignment.com/clarifying-ai-alignment-cec47cd69dd6) to call an AI “intent aligned” if it is _trying_ to do what some operator wants it to do and states:

> [The broader alignment problem] includes many subproblems that I think will involve totally different techniques than [intent alignment] (and which I personally expect to be less important over the long term).

Richard Ngo also seems to [explicitly endorse this view](https://www.alignmentforum.org/posts/PvA2gFMAaHCHfMXrw/agi-safety-from-first-principles-alignment#:~:text=the%20world.%5B1%5D%20Rather%2C-,my%20main%20concern,-is%20that%20AGIs):

> Rather, my main concern is that AGIs will understand what we want, but just not care, because the motivations they acquired during training weren’t those we intended them to have.

Many people have also told me this is the view of [MIRI](https://intelligence.org/), the most famous AI-safety organization. As far as I can see, this is _compatible_ with the MIRI worldview. But I don’t feel comfortable stating as a fact that MIRI agrees, because I’ve never seen any explicit endorsement, and I don’t fully understand how it fits together with other MIRI concepts like [corrigibility](https://www.lesswrong.com/w/corrigibility-1) or [coherent extrapolated volition](https://www.lesswrong.com/w/coherent-extrapolated-volition).

Counterarguments
----------------

Why might this argument be wrong?

### Maybe restrictions would work.

(I don’t think so, but it’s good to be comprehensive.)

### Maybe Wanting is easy for some reason

Wanting _seems_ hard, to me. And most experts seem to agree. But who knows, maybe it’s easy.

Here’s one esoteric possibility. Above, I’ve implicitly assumed that an AI could in principle [want _anything_](https://arbital.greaterwrong.com/p/orthogonality/). But it’s conceivable that only [certain kinds of wants](https://arbital.greaterwrong.com/p/orthogonality/#:~:text=some%20subset%20of%20tractable%20utility%20functions) are stable. That might make Wanting harder or even quasi-impossible. But it could also conceivably make it easy. Maybe once you cross some threshold of intelligence, you become one with the universal mind and start treating all other beings as a part of yourself? I wouldn’t bet on it.

### Maybe drawing the boundary is hard

A crucial part of my argument is the idea that it would be easy for AI to draw a conservative boundary when trying to predict human values or effects of actions. I find that reasonably convincing for values, but less so for actions. It’s certainly easi _er_ than correctly generalizing to all situations, but it might still be very hard.

It’s also conceivable that AI creates such a large action space that even if humans were allowed to make every single decision, we would destroy ourselves. For example, there _could_ be an undiscovered law of physics that says that if you build a skyscraper taller than 900m, suddenly a black hole forms. But physics provides no “hints”. The only way to discover that is to build the skyscraper and create the black hole.

More plausibly, maybe we do in fact live in a [vulnerable world](https://en.wikipedia.org/wiki/Vulnerable_world_hypothesis), where it’s possible to create a planet-destroying weapon with stuff you can buy at the hardware store for $500, we just haven’t noticed yet. If some such horrible fact is lurking out there, AI might find it much sooner than we would.

### Maybe these are the wrong abstractions

Finally, maybe the whole idea of an AI “wanting” things is bad. It seems like a useful abstraction when we think about people. But if you try to reduce the human concept of “wanting” to neuroscience, it’s extremely difficult. If an AI is a bunch of electrons/bits/numbers/arrays flying around, is it obvious that the same concept will emerge?

### Who is “we”?

I’ve been sloppy in this post in talking about AIs respecting “our” values or “human values”. That’s probably not going to happen. Absent some enormous cultural development, AIs will be trained to advance the interests of _particular human organizations_. So even if AI alignment is solved, it seems likely that different groups of humans will seek to create AIs that help them, even at some expense to other groups.

That’s not technically a flaw in the argument, since it just means Wanting is even harder. But it could be a serious problem, because…

### Arms races might destroy conservatism

Suppose you live in Country A. Say you’ve successfully created a super-intelligent AI that’s very conservative and nice. But people in Country B don’t like you, so they create their own super-intelligent AI and ask it to hack into your critical systems, e.g. to disable your weapons or to prevent you from making an even-more-powerful AI.

What happens now? Well, their AI is too smart to be stopped by the humans in Country A. So your only defense will be to ask your own AI to defend against the hacks. But then, Country B will probably notice that if they give their AI more leeway, it’s better at hacking. This forces you to give your AI more leeway so it can defend you. The equilibrium might be that both AIs are told that, actually, they don’t need to be very conservative at all.

Things I read
-------------

Finally, here’s some stuff I found useful, from people who may or may not agree with the above argument:

*   [The Core of the Alignment Problem is…](https://www.alignmentforum.org/posts/vMM6HmSQaKmKadvBi/the-core-of-the-alignment-problem-is-1), by Thomas Larsen et al.
*   [The Compendium](https://www.thecompendium.ai/), by Connor Leahy et al.
*   [A central AI alignment problem: capabilities generalization, and the sharp left turn](https://www.alignmentforum.org/posts/GNhMPAWcfBCASy8e6/a-central-ai-alignment-problem-capabilities-generalization), by Nate Soares
*   [Corrigibility](https://intelligence.org/files/Corrigibility.pdf), by Nate Soares et al.
*   [AGI Ruin: A List of Lethalities](https://www.alignmentforum.org/posts/uMQ3cqWDPHhjtiesc/agi-ruin-a-list-of-lethalities), by Eliezer Yudkowsky
*   [Where I agree and disagree with Eliezer](https://www.alignmentforum.org/posts/CoZhXrhpQxpy9xw9y/where-i-agree-and-disagree-with-eliezer), by Paul Christiano
*   [(Untitled comment)](https://www.lesswrong.com/posts/uMQ3cqWDPHhjtiesc/agi-ruin-a-list-of-lethalities?commentId=JL29PYktEvpd6fuQ5), by Vanessa Kosoy
*   [(Untitled comment)](https://www.lesswrong.com/posts/2NncxDQ3KBDCxiJiP/cosmopolitan-values-don-t-come-free?commentId=ofPTrG6wsq7CxuTXk), by Paul Christiano
*   [Superforecasting AI](https://goodjudgment.com/superforecasting-ai/), by the Good Judgment project
*   [Is Power-Seeking AI an Existential Risk?](https://arxiv.org/pdf/2206.13353), by Joseph Carlsmith
*   [AGI safety from first principles](https://www.alignmentforum.org/posts/PvA2gFMAaHCHfMXrw/agi-safety-from-first-principles-alignment), by Richard Ngo
*   [A Three-Facet Framework for AI Alignment](https://gracekind.net/threefacets/), by Grace Kind
