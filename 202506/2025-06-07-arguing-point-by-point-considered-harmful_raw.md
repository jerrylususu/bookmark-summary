Title: Arguing point-by-point considered harmful

URL Source: https://www.seangoedecke.com/point-by-point-considered-harmful/

Markdown Content:
Engineers love to have technical discussions point-by-point: replying to every idea in turn, treating each as its own mini-discussion. It just makes sense! A good engineer has multiple reasons for any position, so why not articulate them all? And if someone has made multiple points, you ought to respond to each of those points individually when you reply, right? This pulls on the same instinct that we feel when we write code: factoring problems out into sub-components and solving those components one at a time. Why shouldn’t you also communicate the same way?

Sometimes you should. If someone gives you a list of tasks, you ought to respond task-by-task. If you’ve been given a checklist to follow (for instance, before you deploy), you should address each item on the checklist individually. But in cases of **disagreement** - especially disagreement about technical topics, like planning a software feature - it’s not always wise to go point-by-point.

If you work at a large tech company for long enough, you’ll see a pattern where two engineers have a completely unproductive point-by-point argument. It goes like this:

*   Engineer A suggests a course of action
*   Engineer B responds with a list of reasons why that might not be a good idea
*   Engineer A responds with many arguments
*   Engineer B responds with even more arguments
*   Engineer A responds to all of those
*   The whole thing devolves into mini-arguments about each of these individual points, with no decision made about the original course of action

Not all point-by-point arguments go like this. Successful ones can explore a difficult technical issue in depth. But they go badly often enough that it’s worth thinking about how to avoid this failure mode.

### Focus on the affirmative case

If someone raises multiple concerns, and you don’t respond point-by-point, what are you supposed to do? It’s rude to ignore what someone’s said, so obviously you can’t just pick the first point and respond to that alone. Instead, you should try to convince them that **it’s worth taking the time to figure out those concerns together**. For instance, suppose you’re asking an engineer on some other team to write some code in support of your feature, and they say this:

*   I’m worried about the performance impact, since the code you want is in the hot path
*   Users don’t use your feature that much - is this _really_ worth it?
*   We’re really busy right now and probably can’t spare the time to help

The core point here is the second one: they don’t think your feature is worth it. If they thought your feature was really valuable, they’d probably be willing to accept some performance hit (or figure out a way around it), and they’d probably be willing to carve out the time to help. Whether they’re right or wrong about it, that’s the point at issue.

If you respond with a long technical discussion about exactly how big the performance hit is (e.g. “here’s why going to be 2ms, not 4ms”), or how easy it would be to implement (“it’s just a couple of hours work, here’s how you’d make the change”), it likely won’t be helpful: if they don’t care about your feature, they won’t even want to spend 2ms or a couple of hours of work on it.

Instead, you should make the case for why your feature is valuable enough to spend the developer time and CPU time on it. Maybe they don’t know that your feature would unlock deals with Large Customers X and Y, or that it actually does have an enthusiastic group of users, or whatever. If they’re convinced about that, they’ll come around on the other points as well.

### Identify the real problem

In the example I gave, the other engineer explicitly stated their real problem as one of the items in the list. However, often people won’t actually tell you what’s really motivating their position. Sometimes they don’t even know themselves, they just have a strong intuition. This is dangerous for point-by-point communicators, because you can end up in a situation like this:

*   Engineer A asks for something
*   Engineer B has a strong intuition that it’s a bad idea, so they respond with five reasons not to do it
*   Engineer A addresses all five reasons
*   Engineer B introduces five different reasons not to do it
*   Engineer A is justifiably frustrated

Engineer A is frustrated because it feels like Engineer B is cheating in the debate rules - you can’t just keep introducing new arguments indefinitely! Engineer B is frustrated because to them the original idea seems _obviously_ bad, but Engineer A is nitpicking the individual reasons and can’t see that the whole thing is doomed.

If someone isn’t explicitly telling you their reasons, how can you find out what they are? Typically you can’t - **you need to give them the space to find that out themselves.** If you leap into direct technical responses to all of their points, they’ll do the same thing with your responses, and you’ll end up in the vicious cycle I mentioned above. It’s usually more productive to make the central affirmative case for why you hold your position, and give them the space to articulate the central affirmative case for theirs.

### Avoid arguing about small technical points

One reason why point-by-point conversations go badly is that many engineers hate being called out for being wrong about a technical point of fact. I’m one of those people! Being [usually right](https://www.seangoedecke.com/being-right-a-lot) about the technical details is a core part of my professional identity as a software engineer. It’s emotionally difficult to hear someone say “actually you’re wrong, operation X will only take 2ms” and not respond with arguments for why it’ll take more than 2ms, or why 2ms is actually a lot of time to spend in this particular operation.

This means that **if you’re not making a narrow technical point, you should avoid making narrow technical claims**. Arguments about technical details are the absolute worst way to persuade another engineer to do something for you. If you get them on your side, you can work out the technical details together. If they don’t believe in your mission, you’ll never convince them by proving that they’re wrong about the technical points. Even if you succeed, some engineers will be so resentful about being comprehensively proven wrong that they won’t want to help you anyway.

### Points multiply over time

Why do point-by-point conversations often get stuck on narrow technical points? One reason is that **the number of points multiplies as a conversation goes on**. It’s normal to give a couple of different responses to each idea. But since each response to an idea is an idea of its own, two engineers doing this rapidly increases the number of minor points at stake. When someone concedes a point, the number of points goes down, but in my experience this is much less common than someone responding with multiple points. Even when engineers do concede points, they often do it while introducing a new point: “yes, I agree you’re right about X in this context, but it’s still concerning in this other context, right?”

If the number of points at stake in a conversation increases, and engineers feel honor-bound to address every point, the chances of the conversation going off the rails is very high. That’s because **each point of argument is an opportunity to have a fight**. All it takes is one sloppy mis-communication on one of the points for one of the engineers involved to take offense. Once that happens, the “we’re carefully examining each other’s arguments” vibe becomes a debate, which is bad news.

### Avoid giving a list of points yourself

So far I’ve cautioned against allowing yourself to be drawn into a point-by-point argument. But it’s also important to avoid drawing other people into those arguments, if you can. The best way to avoid this is to **limit the number of points you make at the same time**. If you have ten points you could make, don’t make all ten: think hard about what the most important one or two are, and just say those. You can always come back to the less important points later, once the most important ones are addressed.

Engineers like being exhaustive. For better or worse, software engineering culture rewards public displays of competence (like rattling off ten separate technical reasons why approach X is a good or bad idea). It feels good to do and it definitely makes you look smart. But it doesn’t help you convince people (or make it easy for them to convince you, if they’re right and you’re wrong).

The flip-side of this advice is that giving a list of points can _deliberately_ derail an argument, if that’s what you want to do. When someone comes with a suggestion that you don’t want to do, “helpfully” raising ten separate concerns will often bait them into a detailed technical discussion that you can drag on for days or weeks. In other words, you can do _tactically_ what many engineers do _accidentally_. **I don’t recommend doing this, for two reasons:**

1.   It’s more important to build good relationships with other engineers and to preserve your own energy than to win on any single technical dispute
2.   Endless arguments about technical minutiae may impress other engineers, but it makes you look bad in the eyes of senior management, who (rightfully) think you’re wasting time

However, it’s useful to be aware of this tactic so you recognize when it’s being used against you.

### Code reviews

What about code reviews? This could be its own post, but briefly: I think there are two types of point-by-point code review. If the purpose of the review is “let’s get this into good shape so we can merge it”, going point-by-point is appropriate. However, if the purpose of the review is “I’m not convinced by this, let’s not do it”, then it becomes the kind of point-by-point technical disagreement I’m talking about in this post. In that case, you’re often better off avoiding point-by-point replies and just having a general discussion with the reviewer.

### Summary

There are lots of times when it’s correct to respond point-by-point. For instance:

*   When you’re already aligned on the same goals
*   When there’s very high trust
*   When you’re dealing with a list of tasks or checklist

But be careful about talking point-by-point about technical disagreements or when you’re trying to convince someone. Conversations like that often get derailed into the technical details instead of addressing the core reasons behind the disagreement.

When you’re in a point-by-point discussion that’s going badly, you’ll rapidly end up with a huge number of arguments and counter-arguments to track. The longer you talk, the more of these you’ll uncover. And _even if you do address all of them, nobody’s mind will be changed_.

Instead, try and spend your time articulating the main reason why you believe what you believe, and give the other engineer space to articulate theirs. Don’t put them on the defensive by giving them a barrage of individual points to respond to.

If you liked this post, consider [subscribing](https://buttondown.com/seangoedecke) to email updates about my new posts.
