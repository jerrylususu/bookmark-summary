Title: What can strong engineers do that weak engineers can't?

URL Source: https://www.seangoedecke.com/weak-engineers/

Markdown Content:
Right now people are blowing up on Twitter about whether the USA needs to import top talent from other countries, and if that means that American home-grown engineering talent is weak. Last month, people were blowing up over a [study](https://x.com/yegordb/status/1859290734257635439) that purported to show that ~9.5% of software engineers do effectively zero work, and are effectively defrauding the company. And for the last ten years, people have been talking and writing about the fabled “10x engineer”.

What does it really mean to be a strong software engineer?

Strong engineers
----------------

In my experience, the real measure of talent is not the speed or volume of output, but **the capability to do tasks that other engineers can’t**. In other words, strong engineers can do things that weaker engineers just can’t, even with all the time in the world. Therefore, the strongest engineers are stronger than people think they are: not 10x as strong as the median engineer, or even 100x, but infinity-x on some problems. The weakest engineers are weaker than people think they are: not 0.1x, but 0x. They can’t do almost any of the tasks that need doing in a large software organization.

For example, there’s a hard division between engineers [who can ship complex projects](https://www.seangoedecke.com/how-to-ship) and engineers who can’t. It’s not as if weaker engineers do it more slowly - they just can’t seem to do it _at all_. Either a nearby strong engineer ghost-leads the project or the project fails. Some more examples of capabilities that are like this:

*   Solving very difficult bugs (e.g. race conditions across multiple services)
*   Delivering meaningful improvements to the thorniest parts of legacy codebases
*   Successfully making changes that require a big architectural rework

For the top-end of the strongest engineers, the capabilities become things like “improving the SOTA for large language models” and “making self-driving cars work”.

Not every strong engineer can do all of these tasks. Somebody might be great at solving difficult bugs but can’t ship projects, or great at legacy codebases but can’t move fast. However, if someone is great at one of these things, they’re likely to be great at most of the others. I don’t really know why: maybe it’s just raw intelligence, or that being good at one thing helps you learn others, or that these capabilities are more similar than they look, or that these types of engineers try really hard at everything. But in my experience it’s definitely true.

I want to be clear that while being able to do an individual task is pretty black-and-white, the strong/regular/weak categories exist on a spectrum. It’s possible to have a “regular engineer” who can excel at fixing hard bugs, or a “weak engineer” who is genuinely good at keeping their dev environment running. You can be on the fuzzy border between two categories.

### Regular engineers

Right below strong engineers, you have the regular engineers who make up the bulk of most companies. Here’s some examples of capabilities you’d expect these engineers to have:

*   Solving 95% of bugs (e.g. normal, non-cursed bugs)
*   Picking up and delivering most JIRA tickets
*   Unsticking themselves from dev env issues most of the time

A long-ago colleague once referred to this type of engineer as a “plodder”: they aren’t particularly fast, but they’ll make steady progress on a normal-difficulty engineering task. I now think “plodder” is an unnecessarily pejorative name for this, because the more experience I get the more I love these colleagues. They _help_. They _do the work_. They’re just not burning with ambition to excel at the next promo cycle, or to blow their peers away with really impressive output. Probably they have other things going on in their lives!

I have very little to say about this group, except to warn against confusing it with the final group: weak engineers.

### Weak engineers

The other category is truly weak engineers. These people have little to no capabilities at all. In other worse, the baseline difficulty of a normal-to-easy software task is above what they’re comfortable with. I suppose a few of these people are overemployed or fraudulent in some similar way, but I think mostly it’s a lack of ability. I want to be clear that I’m not exaggerating here: weak engineers _cannot complete almost any engineering task_. I’ve worked on teams without any, but if you’re in the industry long enough you’ll encounter them[2](https://www.seangoedecke.com/weak-engineers/#fn-2).

Ironically, while people like this exist at almost all seniority levels, you’re more likely to encounter weak engineers in senior roles. I think this is probably for two reasons. First, the bar to hire juniors is explicitly capability-based, so it’s harder to slip past it. In interviews, seniors can talk about work they were tangentially involved with, which is hard to distinguish from work they _did_. Second, a weak junior is often given more opportunity to learn, because it’s socially acceptable for them to not know things. A weak senior has to conceal their lack of knowledge and learn in secret, which is much harder.

I don’t have a lot to say about weak juniors. You should help them out, point them at challenging problems, and see if they can step up and learn. Weak seniors, however, are a lot more interesting.

### How do weak senior engineers survive?

How do weak engineers survive at the senior+ level? They do a lot of one-way pairing. If you’ve ever paired with these engineers, it’s a very unpleasant experience, since you have to do all the work, whether driving or navigating. Often the pairing is discreet - they’ll quietly reach out to another engineer on the team in DMs for help on every single task they have. Sometimes there’ll be one unlucky victim who gets their time used like this: for instance, an effective junior on the team who’s happy to help and too inexperienced to know better. More savvy weak engineers will round-robin their pairing across the team, so each individual member might only need to chip in every week or so. Only when everyone compares notes does it become clear that the weak engineer is pairing on 100% of their tasks.

Weak engineers are often surprisingly active in work-related discussions. This is partially because they’ve got a lot of time - unless they can find someone to “pair” with, they’re not really working. It’s also an effective defense mechanism. If questions come up about their individual output, they can gesture at their public communications as evidence that they’re leveling up the team instead of grinding out concrete work. One way to tell a weak engineer in a discussion thread about some problem is to see who is bringing in specific facts about how the system currently works, and who is making purely general recommendations that could apply to any system. If their messages could all be public tweets, they’re probably not adding much value.

### Some tips on working with weak senior engineers

The first and most important thing is to remember that **it’s just work**. Somebody being bad at their job does not make them a bad person. Do not be an asshole! People can be weak through laziness and lack of talent, but also for all kinds of personal reasons that are none of your business. Act with the generosity that you hope would be extended to you if you endured some personal tragedy that meant you couldn’t focus on work. Even lack of talent can be context-specific: for instance, maybe they’re an embedded-systems whiz trying out a different field and not having much success, or a big-company employee struggling to adapt to startup norms.

Still, you should try to protect your time. Don’t quietly give up hours of your workday to helping them stay afloat. One tactic is to **avoid time-asymmetrical helping**. Don’t do work for them that takes much more time than it took them to ask about it. For instance, if you’re asked “hey, I have this issue, how would you approach it”, don’t take the time to work out the actual solution and hand it to them. Fire off a _quick_ response that points them at the next immediate step (e.g. “oh yeah, looks like something in the billing code, you should see how service X handles it”). This means they can’t spend minutes of their day tying up hours of yours.

Relatedly, you should try to protect the time of the junior members of your team. Don’t let them be exploited by weak seniors who will ask them to solve their problems and then frame it to management as them helping the juniors level up. The best way to do that is to (professionally) make sure your manager knows the situation. It can be a hellishly difficult process to manage people out at some companies (and there might be things going on that you’re not aware of), so don’t expect that this person will be fired/pipped/told to shape up. But you still have a responsibility to make sure your manager’s aware.

### Conclusion

Engineering talent isn’t extra speed or output, it’s the capability to do tasks that other engineers can’t. That’s why the weakest engineers output so little, and why tech CEOs obsess about hiring the strongest engineers.

Most engineers can do a broad set of normal job tasks, but some can do really hard ones and some can barely do any. You should probably try to expand the set of tasks you’re comfortable doing. If you’re working with a weak engineer, be nice but protect your time.
