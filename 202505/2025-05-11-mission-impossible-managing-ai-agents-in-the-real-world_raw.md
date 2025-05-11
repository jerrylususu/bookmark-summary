Title: Mission Impossible: Managing AI Agents in the Real World

URL Source: https://levelup.gitconnected.com/mission-impossible-managing-ai-agents-in-the-real-world-f8e7834833af

Published Time: 2025-04-23T16:31:45.484Z

Markdown Content:
[![Image 1: David Bethune](https://miro.medium.com/v2/resize:fill:64:64/1*POq_2Vv7JC1P5mL03D_76w.png)](https://medium.com/@mimixco?source=post_page---byline--f8e7834833af---------------------------------------)

35 min read

Apr 23, 2025

![Image 2](https://miro.medium.com/v2/resize:fit:700/1*dYVW_8naZyT62WihlvxxtQ.png)

> We are at a new frontier with AI tools in every industry, and particularly in software development. They are changing underneath us faster than any human can adapt, and charging us for the privilege. Maintaining control of these robots feels like an impossible mission. Today I’ll share some battle-tested techniques that you can use to rein in your AI agents, chats, and other tools.

This article is part of my **AI Library**. If you’re new to agentic coding, start with _License to Kill_. To dig deep into why and how this stuff works the way it does, check out _Something from Nothing_.

Your Mission
------------

After many successes and failures I’ve had with AI agents, the mission comes down to careful planning and restraining the context of what your agents can do.

> Everything that can be done wrong, I’ve done wrong.

If you can set the right guidelines, agents can deliver better results. Everything than can be done wrong, I’ve done wrong and learned from it. It should be no surprise that agents write software this way. Humans do, too, and that’s where agents get their ideas.

1.  Choosing Your Tools
2.  Choosing What to Work On
3.  Finding a Route
4.  Making a Plan
5.  Revising the Plan
6.  Testing the Plan
7.  Finding Bigger Problems
8.  Making Rules
9.  Performance Payback
10.  Choosing Models
11.  Cost Controls
12.  Model Context Protocol (MCP)

> **Fair Warning:** All screenshots and UI mentions are likely to be outdated by the time you read this, owing to how fast these tools change. The concepts will be there in different parts of the app if you hunt around.

![Image 3](https://miro.medium.com/v2/resize:fit:700/1*MxsHeEBZuenOEwYJcc7gMQ.png)

**_Wheatfield with Crows_** is my favorite Van Gogh painting. It’s stunning in person and [can’t be reproduced](https://artsandculture.google.com/asset/wheatfield-with-crows-vincent-van-gogh/dwFdD5AMQfpSew?ms=%7B%22x%22%3A0.5%2C%22y%22%3A0.5%2C%22z%22%3A11%2C%22size%22%3A%7B%22width%22%3A0.7299686341602509%2C%22height%22%3A0.7667865707434053%7D%7D) in any medium. Oil paint impasto reflects photons into your eye in ways that aren’t duplicated by ink on paper or by emissive screens. In the same way, the materials and techniques in your existing code and your prompts determine the true qualities of the finished app.

1\. Tools Are Not Materials, Nor Technique
------------------------------------------

**Choosing Your Tools**

I’m putting this issue here not because it’s the most important but because folks _think_ it is. In art, there is a great difference between **tools, materials,** and **technique**. When the work is done, only the materials remain, transformed as they were by your tools and technique.

When you work with AI tools, the materials are your inputs — your code, diagrams, data, and prompts. The technique is how you weave these materials together and the order in which you present them. You’ll find a recurring theme throughout this article: the quality of the materials you provide will be the single most important factor in your AI agent’s success.

My examples will be from [Cursor](https://www.cursor.com/) but I want to emphasize that the tool _du jour_ has very little impact on what you can do, just like all washing machines have similar functions but different buttons.

AI tools change **daily**. If you haven’t updated yours today, it’s probably behind. The trick is to find the tool that offers a workflow that you like — one that offers a balance of investigation and action and boosts your own workflow.

You can apply everything I’ll talk about in Cursor with tools like [Windsurf](https://windsurf.com/), [Copilot](https://github.com/features/copilot) for VS Code, or even by pasting stuff into ChatGPT or Google Gemini. You can also use all of these tools for free but, as with everything in life, the paid version is significantly better, so don’t judge the paid version of something by the free results.

> Will non-devs create high quality output with these tools? **Absolutely not.**

It’s also important to know your tool deeply and keep up with its [changelog](https://www.cursor.com/changelog) and documentation. I know no one reads that anymore but, ironically, in the age of “ask an AI anything,” the user of such an AI would do well to read the doc directly as the true secrets of its power are revealed only in the pages of those cryptic tomes.

Know Thyself
------------

When working with AI, you must be realistic about your own abilities and shortcomings, for they will permeate everything the agent builds for you. When is it time to _investigate_, and when is the time to take _action_? You have to be the one to know and control that flow.

With AI tools, different skills pay the bills. Does that mean that non-devs (or non-artists) will create high quality output with these tools? **Absolutely not**. It means just the opposite.

In addition to your standard set of coding skills, you’ll need deep architectural insights and an ability to communicate them in plain English. That’s not a skill set that’s common among programmers. Don’t be upset at the LLM when its output is just as bad as your input.

![Image 4](https://miro.medium.com/v2/resize:fit:700/1*P0_zoLk6dPR2ZtHEuLjLCw.jpeg)

Roland’s new V-Stage, shown here with music legend Patrice Rushen of [Forget Me Nots](https://www.youtube.com/watch?v=jtMHsNhQBvI) fame, reminds me of how far pianos have come. Did you know that the keyboard we have today wasn’t standardized at first? Prior to the adoption of [equal temperament](https://en.wikipedia.org/wiki/Equal_temperament) tuning, the musician before you might have composed their piece with entirely different frequencies than yours. Talk about bad vibes.

2\. Bad Vibes
-------------

**Choosing What to Work On**

You might notice a heavy emphasis on planning in the topics I’ve picked for this article. That’s because, with agents, 90% of your work is going to be planning. The popular term “vibe coding” suggests that you can just ask for anything or say anything and get results. What’s shocking about this idea is that it’s true.

> Vibe coding is the exact wrong approach unless you only want an _artifact_ to show someone.

Today’s models have progressed far enough to literally write anything. And that’s now a problem, as I covered extensively in my last article. Vibe coding is the exact wrong approach unless you only want an _artifact_ to show someone.

If you’re making code that’s expected to ship, you can only think of vibe outputs as prototypes. They look great but, like paper airplanes, don’t really fly. That doesn’t mean they’re not useful. The “M” in LLM means model. It was always a model all along. If we keep that in mind, we can use the model only where we need it, while we control building the final product.

> We need to make a reusable plan for things we only plan to do **once**. That seems insane.

It may seem like the amount of planning I’m suggesting will take longer than just writing something shippable yourself. And that’s very likely to be true. The difference is that we get a **reusable plan** out of this process, something we are not likely to have around for any other kind of code we wrote ourselves.

![Image 5](https://miro.medium.com/v2/resize:fit:700/1*LzhWxlnGHywukDg1p-cQtg.png)

Here I reference both a file to work on and a reusable plan, written previously (by Cursor, of course!). Notice that it is better able to follow a plan like this than just trying to complete the same actions from the original prompt that created the plan.

We need to make a reusable plan for things we only plan to do once. That seems insane. Why would it need to be reusable if we’re only doing it once? There are two reasons. The most glaring is that the agent is **unlikely** to do it all correctly the first time. If your plan isn’t written with multiple runs in mind, you’ll waste time backtracking and re-explaining the plan instead of just nuking your repo and changing the plan, then re-running it.

> If you’re not sure if the plan will work, the agent won’t be sure either.

If writing a reusable, runnable thing that outputs data and a UI sounds a lot like programming, Welcome to the New Age. The second benefit of this reusable plan (that lives in your repo) is that you or the agent can read it again when you want to refactor or extend your design.

With this in mind, it’s important to carefully **scope** your work. Don’t ask for the finish line at the beginning. Try to divide the work you ask for into modular parts that can be completed successfully. If you’re not sure they can be completed successfully, send the agent back to the investigation phase to improve the plan.

If you’re not sure if the plan will work, the agent won’t be sure either. Agents that lack confidence in their own plans tend to go wildly off track, a recurring theme in recent Mission Impossible movies, now that I think about it. AI agents will make up a solution on-the-fly if your plan doesn’t adequately cover a situation. This is a side effect of having been trained on every kind of code. The agent thinks, “I’ve got it! I have a solution!”

The more steps your solution requires, the less likely the agent is to be able to make up a missing step. It will invent one that could break other areas of your app or appear to work in prototype but fall apart in practice. You must plan for only small, deliverable steps.

![Image 6](https://miro.medium.com/v2/resize:fit:700/1*oNQOdRywArOiHv1HpFuiSw.png)

The outstanding narrative game [Road 96](https://road96.com/) uses randomness to create different interactions for you, the player character, based on the stories of the game’s seven NPCs. All of the NPCs are going the same place but by different routes. These interactions result in new objects and skills that you retain. In the same way, you must choose actions, questions, and answers that are appropriate for each AI model to get to the finish line — and keep those artifacts around for future use.

3\. The Road Less Traveled
--------------------------

**Finding a Route**

Once you’ve selected your agent’s target, you must also a find a route for it to travel. This seems laborious, too, and always elicits cries of, “But if I have to do _that_, I might as well code it myself!”

**Sometimes** that’s true. If a change is so small that you could just make it immediately, then you should make it. If a change requires so much explanation that you are having trouble explaining it, your code needs architectural help (much more on this later).

> The agent is not following any “rules” no matter how many ways we try to pretend that it is.

You will find that procedures that seem very simple to a person, like “Take the third item off of there and do something to it,” cause serious problems for LLMs. Simple console operations like copying files or running builds are also problematic.

To understand why, we need to adjust our expectations. The agent is not following any “rules” no matter how many ways we try to pretend that it is. It’s merely predicting the next most likely piece of text to output from whatever series of prompts it has in the thread at the moment.

It’s exhilarating to watch an agent code a feature out of thin air and then go play with it minutes later. It can lull us into a false sense of security where we start asking for things we shouldn’t ask for — things we should do ourselves. We see one great miracle and then ask for a small one in the same codebase, not realizing we are on an agent high.

> If you’re not sure how to implement it, that’s fine — just ask the agent. The more you reference your own code and data, the better the answer will be.

You should probably try it at least once with something inconsequential just to have the resulting crash. If you try vibe coding something you plan to keep, be prepared to spend precious hours or days rescuing the beautiful baby you created together because you’re in love with your “progress.” Your rescue will involve combing through the agent’s code and **your existing code** to find out how and why it came to be.

Thus, I would recommend that you begin at the beginning and ensure that you know exactly **how to implement** the thing you’re asking for. If you’re not sure how to implement it, that’s fine — just ask the agent. Put it in “planning” or “asking” mode first or just say, “I’d like to understand how…,” or “I’m trying to understand the implications of…” The more programmer-speak you use in your question, referencing your own code and data, the better the answer will be.

![Image 7](https://miro.medium.com/v2/resize:fit:700/1*8fjEIST3qmONNl-VqU3ixQ.jpeg)

Star Trek was already in reruns when I was born in 1968. My mother didn’t let us watch it because it was “too scary.” The series premise, to go where no man has gone before, certainly implies risk, and Kirk was quick to make a plan and communicate it before anyone teleported to a new planet or ship. You, too, must quickly make and revise plans in this new AI space.

4\. Where No Man Has Gone Before
--------------------------------

**Making a Plan**

It would be great if we could just make the plan in one step. It’s like asking to learn to play the piano in one step. You’ll get better with time as you realize the problems with agentic coding stem mostly from your poor plans and your bad code, rather than from bad models or broken tools.

Some people will not be able to admit this. Developers are famously bad at communicating with other humans, yet this is exactly the #2 skill that agentic coding requires (#1 still being regular programming).

Often programmers live in a world of “Well, it worked when I tested it locally,” and we won’t want to fess-up to architectural nightmares or implementation problems in our own codebase, which we don’t normally show anyone.

![Image 8](https://miro.medium.com/v2/resize:fit:700/1*HoLuAUYwazsOh7260jYc-Q.png)

In this earliest part of the conversation about a new plan, the model suggested some things and I hated all of them, but some pushback from me and some manually-coded architectural changes before I asked the agent to “just do it” resulted in a very different and very clean technique of pure editable JSON files for the metadata so that it can be separated from any individual game and injected at build time. The agent’s suggestions didn’t take into account that JS-based solutions don’t show up for social shares like Discord or Slack, which don't run JS and would wind up with only the template metadata.

Thus we arrive at the **new programming language**, some mash-up of English and pseudocode, brimming with arcane references to your own existing app and its files, functions, and data structures.

Tools like Cursor that let you `@mention` these parts of your code do an even better job with plans than tools that just use a typing or cut-and-paste (or even file upload) interface.

Plans Are First Class Citizens
------------------------------

In my repos now, a `/plans` folder is a first-class citizen. I start every new complex request with asking Cursor to write a plan and put it in `my-plan-for-this.md`, a Markdown file in that folder.

By saving these with the repo commits, they become **usable programs** that I can run later by `@mentioning` them. I can even start a new thread (and often do) by mentioning a plan by name, then asking for revisions or asking to take a single step inside it while I retain control of the repo. I make constant commits with clear messages about which plans have been written or changed and which steps have been run.

> We’ve heard the term “code as doc” and here it is in practice.

1.  Plans are runnable programs.
2.  Written in Markdown.
3.  That contain real code and data.
4.  And get saved in your repo.
5.  With plan-related commits and messages.

Whew! This concept of developing, revising, and saving your own plans is far more important than trying to download someone else’s plans or rules file, despite the fact that hundreds of those appeared overnight on the web.

You can get a book about renovation from Home Depot but that book doesn’t have a plan for your house. The same is true here.

> Look inside a plan and you’ll see what enables the magic. They are light years beyond what a person would write.

By letting a tool like Cursor create its own plans, we gain fascinating insights into how the app crafts its own prompts — the ones that are actually fed to a model. We know it’s prompts all the way down. When you write a prompt in the chat box that references a plan you made, the contents of that plan are attached to the prompt. That’s the sum total of the magic.

![Image 9](https://miro.medium.com/v2/resize:fit:700/1*2ZLfzjcJp1EysCrk0KjmpQ.png)

Here you can see the actual plan I had Cursor write, along with the interactive chat window while it was being composed. Notice the level of detail and markdown formatting which humans wouldn’t take the time to add. This is very helpful when you want to edit or run these plans. Also notice that Cursor wants to be updated (bottom left), like always!

But look inside one of these files and you’ll see what enables the magic. Its plans are **light years beyond** what a person would write. They’re fully commented, described with narrative text, full of examples in real JSON or TS (in my app — yours will be in your languages), and use abundant Markdown formatting to make them both machine readable and pretty when you look at them in an IDE preview pane.

When was the last time we had code/doc like that? Remember, these plans are runnable software which you invoke by saying, “Let’s go ahead and do step 2 in `@world-domination-plan.md`. When you change the plan, commit your repo with a human-readable comment. When you run a step, commit again and comment that you “ran step 2” or something similar.

You will need these _commit breadcrumbs_ when you later want to roll-back something or look at ideas from old plans you’ve since changed or removed. Often old plans contain juicy bits that we might want to look at later — things where the AI’s inventiveness or clever problem solving might be useful after all, even if the way it describes isn’t implementable in the code you have now.

![Image 10](https://miro.medium.com/v2/resize:fit:700/1*PZ0aAJfFCllO5jY0d_h5PQ.jpeg)

Chappell Roan’s [Pink Pony Club](https://www.youtube.com/watch?v=GR3Liudev18) is arresting enough and it‘s already mass market. No wonder Momma screamed when she saw it. An AI agent will plan and do things that seem just as off-the-rails and that comes from their mass exposure to other people’s programming, which weighs more heavily on the training set than your code or your prompts — unless you specifically tell it otherwise.

5\. Pink Pony Club
------------------

**Revising the Plan**

As soon as your plan is written into the Markdown file, it will be wrong. That’s all the time it takes!

Should this be frustrating? That depends. Yes, it’s irritating to see it go off the rails here in the plan, before we even get started. It’s not very comforting and doesn’t bode well for actually _executing_ on the plan. We start to scream, “God, what have you done!” when it wants to be a Pink Pony girl.

To make this work, you have to find out if the **finished product** with the correct architecture and design takes less time overall using this process than with pure manual coding (or even just autocomplete). An individual step like revising the plan seems annoying because we didn’t have to do that before. Of course, the only reason we didn’t have to do it before is that **there was no plan before**.

> It’s unhelpful to lecture the LLM about what’s wrong because you are just **adding more context** to something that falls apart the more context you give it.

We all code stuff out of our heads. If we write doc, it’s mostly after we coded something. If we try to write doc before code, it’s also wrong immediately because the code deviates from the plan in practice.

![Image 11](https://miro.medium.com/v2/resize:fit:700/1*RXVaS85d6niVylneret9qQ.png)

In this closeup from one of my plans, you can see that they actually contain real example code like CSS, TS, and JSON. You can use this ability to avoid having to say where or what to copy from when doing a repeated step. Ask Cursor to take your example (from wherever it is, like one that works) and include it in the plan. This comprehensive plan, hundreds of lines long, took several revisions to get right.

Don’t be starstruck when you see the new plan. It looks so complete, so _professional,_ how could it be wrong? Trust me. It’s wrong. You really need to read all of it. If there are simple things wrong, like whole sections that shouldn’t be there, just yank them yourself. Don’t yell at your spouse that they should have taken out the trash. Just dump it.

It’s unhelpful to lecture the LLM about what’s wrong because you are just **adding more context** to a prompt chain that falls apart the more context you give it. Having said that, if there are changes _across_ the plan, like widespread implications, data formats, techniques, etc. that are wrong, you don’t need to re-write those. Just tell the model to change the plan and why and let it go through the whole thing again, making all the necessary updates. Then read it again.

> You’ll be impressed when you craft your first plan that looks right. Then you’ll run it…

When you first start writing plans, you’ll likely need more than two revision steps before you even run it. You are learning a new style of programming. When I loaded cassettes into the [ADAM](https://en.wikipedia.org/wiki/Coleco_Adam) and tried to edit them, they often didn’t work the first time. You’ll be impressed when you craft your first plan that looks like it’s right, down to the letter.

Then you’ll run it and find out it’s not.

![Image 12](https://miro.medium.com/v2/resize:fit:700/1*YHMEPmFl8oju-zsQHUHD4g.png)

GTA Online is certainly a game where one must make plans and quickly revise them, and they have consequences as you can see in my mugshot. A running theme of Grand Theft Auto is the gleeful way you must drive through road signs, blockades, and even people to meet your goals. Without adult supervision, your AI agent will adopt its plans to do bad things because you said it had to get to the goal.

6\. Pedal to the Metal
----------------------

**Testing the Plan**

After seeing your plan written out better than you could write it yourself, the agent will undoubtedly offer to just go ahead and shoot to kill. And you should absolutely **not** do this.

I’ll stop here to say that, even if you have no intention of letting an agent change your code, it can be very useful to have it generate documentation for you or others in the form of these plans. You can ask it to describe how something works in your existing code, put it in an `.md` file in a `/docs` folder, and grow that library of doc.

It’s smart to do this even if no one else reads your code because you can `@mention` these doc files to attach them to prompts, thus making “mini-rules,” and we’ll look at how to turn those into other kinds of rules, including automated ones, in a moment.

Often, all the right steps are in the plan but, for various reasons, they might need to be done in a different order than the model suggested. You might decide to do file or terminal operations locally, for example. Don’t bother changing the plan or telling Cursor anything. Just tell it to do step 3 when you want that, even if it’s first. Don’t spend credits on _edumacation_ that ain’t goin’ nowhere, as we know LLMs don’t increase their understanding through more talking.

> Testing your plan vs. your actual code will reveal many **ugly truths** about what you, the human, have written.

Often, you’ll want to make some other refactor or cleanup **before** having the agent start the plan, and you should do anything you can to “clear the path.”

This is another place where we lose folks on the AI road. “But if I just code it myself, I don’t have to do any of that.” Hard to argue that one. The truth is that testing what’s written in your plan vs. what’s actually in your codebase will reveal many **ugly truths** about what you, the human, have written.

It’s easy to say, “I don’t have to time to cleanup my code right now. I need to ship this.” And that, my friends, is how we get tech debt.

One of the best uses of agents is in **refactoring** — and yet we hear people saying it can’t be done! I’m here to exclaim the opposite. A careful refactoring of something _pointed out by the AI_ is extremely useful. It’s shining light onto a cavity that you haven’t seen. Drill, baby, drill!

As long as your refactoring follows the plan for making plans that I’m laying out here, you’ll wind up with less tech debt across the codebase. You’ll have code that’s much easier for you and for the agent to work with in the future — code that won’t get left behind because nobody understands and it nobody can really work on it anymore.

Whether or not you choose to refactor from something you see in the plan, you should do that as a separate thread with its own plan. Avoid the temptation to keep injecting that drug from Dr. Feelgood. Whichever plan you’re on, only allow the tool to do one step at a time, and commit and test yourself after each step.

> If you tell the AI what you want, you might be heard one day and ignored the next.

It’s exasperating to find that the AI keeps missing “obvious” things, but they are only obvious to you from the time you spent working on this codebase and others. LLMs don’t accumulate knowledge like people. Even having millions of lines of code in their training doesn’t give them any understanding of code, it only gives them a terrific predictive ability based on repeated exposure to code in other contexts.

A large training base actually makes it **less likely** that it will correctly guess custom code that applies to your environment. The retrieval system always shows the most likely answer (in the context of the prompt and the current random seed). This means that the most likely answer will not be the solution that exactly matches your custom architecture. It won’t be the predominate stuff in the training set.

This is why we see LLMs constantly try to steer you toward rando solutions that they are “certain” will work. It’s because they’ve seen these in their training sets in the context of the question you asked. That doesn’t mean that the meaning or use of your code is taken into account when giving the answer.

If we tell a human, “Look, Larry, we always use composition and don’t write things that inherit from each other,” you would expect that to be a one-time mention or maybe even something you add to a code style manual. If you tell the AI that, you might be heard one day and ignored the next. It’s not “learning” anything from you. It’s predicting what you want to hear.

You can improve some of these predictions with plans and rules, but we’ll never get to 100%. LLMs are not databases and don’t reproduce the code they were trained on directly. It can even be hard for them to reproduce your own code exactly, since that’s not the most likely code to be predicted. And they have no way to understand your code’s meaning and purpose unless you describe how those intersect with the way it’s written.

Trust But Verify
----------------

After the model exclaims that all your steps are finished and the app is working, it might — depending on its mood — offer to run it in the terminal. I would say, “Never mind,” at least with web apps. There are agent wiring tools that supposedly can round-trip between writing code and viewing the browser results (to go back and fix the code), but I’m not a believer in that just yet.

> Your original “goal” could be very far away in the thread and no longer considered important.

I run all builds and tests in my own terminal window and you probably should, too. And I look at all user-facing output in the browser, just as a user would and gradually as the app develops. Asking the LLM to test its own output has a chance of sending it down a wrong road to make a fix, or faking the test to make it work (like inserting mock data or changing the test criteria), or even outright lying and saying the tests work when they clearly don’t.

In a real example of this, I had Cursor help me fix text with ellipses. It’s supposed to happen with CSS and grow or shrink with other items but is notoriously difficult to get right inside a series of shifting containers. After giving up on its own solution, Cursor **changed the Typescript code** to trim off some number of characters from the string and put “…” at the end! This might look the same in some cases but very much is not. It took me a bit to notice. Trust, but verify.

The reason for this is the same reason for all the other behavior we hate. These are predictive answers, not provable ones. The AI is predicting that the code works and then predicting a solution that will work when the first one doesn’t. Your original “goal” isn’t even part of the predictive process. It could be very far away in the thread and no longer considered important. People do this, too. We forget a fact or a name after a convo or a movie scene goes on for a long time.

> Take the time to write a good ticket and you’ll get back a real fix.

When your real, human test fails, don’t ask the AI to correct the problem immediately. Instead, you guessed it, ask for a plan for the fix. Provide screenshots of the output that’s a problem and explain exactly why. Provide console or terminal messages and screen captures of the browser inspector where those would help the agent in finding the fix.

![Image 13](https://miro.medium.com/v2/resize:fit:700/1*sb57guVSp-gVWHEyXv7JIA.png)

I pasted this screenshot into a Cursor chat while debugging the text that ends with ellipses. I used a trick that works like dental disclosing tablets — putting red boxes (with CSS) around the problem elements. Then you can mention that in your prompt to help Cursor see what it should be working on. You can also paste architectural diagrams if you have those or need to draw one to explain something better than words.

In other words, don’t write a shitty JIRA ticket. Take the time to write a good ticket and you’ll get back a real fix. The fix itself may take more than one try (thus having a plan for it), but you’ll be surprised at how many flowers bloom from these crazy planting sessions. The joy we all feel as software developers when it “just works” is very much there when you get the agent to the finish line — after following **your** plan!

There is no secret tech debt left behind, either. This method forces you to become a ninja over your own codebase and to write and review documentation about how it works. The AI isn’t replacing you as a developer, it’s helping you level-up.

And those three dots? In the end, I had to manually fix the ellipses everywhere I wanted them. Because it’s tricky and not often used, there aren’t many examples in the model’s training — and you’ll find this true of every cool thing in your code. You will have to _‘splain_ all the cool stuff and the most unique parts, your secret sauce, you will have to design and somewhat implement manually.

![Image 14](https://miro.medium.com/v2/resize:fit:700/1*MPwyKDmmNbrt5xXFmBQzfw.jpeg)

I visited this set in Rosarito, Mexico where [Titanic was filmed](https://en.wikipedia.org/wiki/Baja_Studios) during the brief time it was open for tours. What’s not shown here is that the ship has **no other side**. When shots from the port side were needed they were taken through a reversing lens. Luggage tags and signage for those scenes were printed with mirrored text to appear correctly on film. How many illusions in your code will working with an AI agent uncover?

7\. A Disaster of Titanic Proportions
-------------------------------------

**Finding Bigger Problems**

The most humbling part of agentic coding, and possibly the most beneficial, is the realization that all of the bad code is your fault. I’ve been in many standup 