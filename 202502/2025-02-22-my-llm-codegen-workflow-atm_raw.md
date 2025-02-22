Title: My LLM codegen workflow atm

URL Source: https://harper.blog/2025/02/16/my-llm-codegen-workflow-atm/

Published Time: 2025-02-16T18:00:00-05:00

Markdown Content:
_tl:dr; Brainstorm spec, then plan a plan, then execute using LLM codegen. Discrete loops. Then magic. ✩₊˚.⋆☾⋆⁺₊✧_

I have been building so many small products using LLMs. It has been fun, and useful. However, there are pitfalls that can waste so much time. A while back a friend asked me how I was using LLMs to write software. I thought “oh boy. how much time do you have!” and thus this post.

(p.s. if you are an AI hater - scroll to the end)

I talk to many dev friends about this, and we all have a similar approach with various tweaks in either direction.

Here is my workflow. It is built upon my own work, conversations with friends (thx [Nikete](https://www.nikete.com/), [Kanno](https://nocruft.com/), [Obra](https://fsck.com/), [Kris](https://github.com/KristopherKubicki), and [Erik](https://thinks.lol/)), and following many best practices shared on the various terrible internet [bad](https://news.ycombinator.com/) [places](https://twitter.com/).

This is working well **NOW**, it will probably not work in 2 weeks, or it will work twice as well. ¯\\\_(ツ)\_/¯

Let’s go
--------

![Image 1: Juggalo Robot](https://harper.blog/images/posts/llm-coding-robot.webp)

I always find these AI-generated images to be suspect. Say hi to my juggalo coding robot angel!

There are many paths for doing dev, but my case is typically one of two:

*   Greenfield code
*   Legacy modern code

I will show you my process for both paths

Greenfield
----------

I find the following process works well for greenfield development. It provides a robust planning and documentation approach, and allows you to execute easily in small steps.

![Image 2: Green field](https://harper.blog/images/posts/greenfield.jpg)

Technically, there is a green field on the right. Leica Q, 5/14/2016

### Step 1: Idea honing

Use a conversational LLM to hone in on an idea (I use ChatGPT 4o / o3 for this):

```
Ask me one question at a time so we can develop a thorough, step-by-step spec for this idea. Each question should build on my previous answers, and our end goal is to have a detailed specification I can hand off to a developer. Let’s do this iteratively and dig into every relevant detail. Remember, only one question at a time.

Here’s the idea:

<IDEA>
```

At the end of the brainstorm (it will come to a natural conclusion):

```
Now that we’ve wrapped up the brainstorming process, can you compile our findings into a comprehensive, developer-ready specification? Include all relevant requirements, architecture choices, data handling details, error handling strategies, and a testing plan so a developer can immediately begin implementation.
```

This will output a pretty solid and straightforward spec that can be handed off to the planning step. I like to save it as `spec.md` in the repo.

> You can use this spec for a number of things. We are doing codegen here, but I have used it to bolster ideas by asking a reasoning model to poke holes in the idea (must go deeper!), to generate a white paper, or to generate a business model. You can pop it into deep research and get a 10k word supporting document in return.

### Step 2: Planning

Take the spec and pass it to a proper reasoning model (`o1*`, `o3*`, `r1`):

(This is the TDD prompt)

```
Draft a detailed, step-by-step blueprint for building this project. Then, once you have a solid plan, break it down into small, iterative chunks that build on each other. Look at these chunks and then go another round to break it into small steps. Review the results and make sure that the steps are small enough to be implemented safely with strong testing, but big enough to move the project forward. Iterate until you feel that the steps are right sized for this project.

From here you should have the foundation to provide a series of prompts for a code-generation LLM that will implement each step in a test-driven manner. Prioritize best practices, incremental progress, and early testing, ensuring no big jumps in complexity at any stage. Make sure that each prompt builds on the previous prompts, and ends with wiring things together. There should be no hanging or orphaned code that isn't integrated into a previous step.

Make sure and separate each prompt section. Use markdown. Each prompt should be tagged as text using code tags. The goal is to output prompts, but context, etc is important as well.

<SPEC>
```

(This is the non-tdd prompt)

```
Draft a detailed, step-by-step blueprint for building this project. Then, once you have a solid plan, break it down into small, iterative chunks that build on each other. Look at these chunks and then go another round to break it into small steps. review the results and make sure that the steps are small enough to be implemented safely, but big enough to move the project forward. Iterate until you feel that the steps are right sized for this project.

From here you should have the foundation to provide a series of prompts for a code-generation LLM that will implement each step. Prioritize best practices, and incremental progress, ensuring no big jumps in complexity at any stage. Make sure that each prompt builds on the previous prompts, and ends with wiring things together. There should be no hanging or orphaned code that isn't integrated into a previous step.

Make sure and separate each prompt section. Use markdown. Each prompt should be tagged as text using code tags. The goal is to output prompts, but context, etc is important as well.

<SPEC>
```

It should output a prompt plan that you can execute with aider, cursor, etc. I like to save this as `prompt_plan.md` in the repo.

I then have it output a `todo.md` that can be checked off.

```
Can you make a `todo.md` that I can use as a checklist? Be thorough.
```

You can save it as `todo.md` in the repo.

Your codegen tool should be able to check off the `todo.md` while processing. This is good for keeping state across sessions.

#### Yay. Plan!

Now you have a robust plan and documentation that will help you execute and build your project.

This entire process will take maybe **15 minutes**. It is pretty quick. Wild tbh.

### Step 3: Execution

There are so many options available for execution. The success really depends on how well step 2 went.

I have used this workflow with [github workspace](https://githubnext.com/projects/copilot-workspace), [aider](https://aider.chat/), [cursor](https://www.cursor.com/), [claude engineer](https://github.com/Doriandarko/claude-engineer), [sweep.dev](https://sweep.dev/), [chatgpt](https://chatgpt.com/), [claude.ai](https://claude.ai/), etc. It works pretty well with all the tools I have tried, and I imagine it will work well with any codegen tool.

I, however, prefer **raw** claude and aider:

### Claude

I essentially pair program with [claude.ai](https://claude.ai/) and just drop each prompt in iteratively. I find that works pretty well. The back and forth can be annoying, but it largely works.

I am in charge of the initial boilerplate code, and making sure tooling is set up correctly. This allows for some freedom, choice, and guidance in the beginning. Claude has a tendency to just output react code - and having a solid foundation with the language, style, and tooling of your choice will help quite a bit.

I will then use a tool like [repomix](https://github.com/yamadashy/repomix) to iterate when things get stuck (more about that later).

The workflow is like this:

*   set up the repo (boilerplate, uv init, cargo init, etc)
*   paste in prompt into claude
*   copy and paste code from claude.ai into IDE
*   run code, run tests, etc
*   …
*   if it works, move on to next prompt
*   if it doesn’t work, use repomix to pass the codebase to claude to debug
*   rinse repeat ✩₊˚.⋆☾⋆⁺₊✧

### Aider

[Aider](https://aider.chat/) is fun and weird to use. I find that it slots in well to the output of step 2. I can get really far with very little work.

The workflow is essentially the same as above but instead of pasting into claude, I am pasting the prompts into aider.

Aider will then “just do it” and I get to play [cookie clicker](https://orteil.dashnet.org/cookieclicker/).

> An aside: Aider does really great benchmarking of new models for codegen in their [LLM leaderboards](https://aider.chat/docs/leaderboards/). I find it to be a really great resource for seeing how effective new models are.

Testing is nice with aider, because it can be even more hands off as aider will run the test suite and debug things for you.

The workflow is like this:

*   set up the repo (boilerplate, uv init, cargo init, etc)
*   start aider
*   paste prompt into aider
*   watch aider dance ♪┏(・o･)┛♪
*   aider will run tests, or you can run app to verify
*   if it works, move on to next prompt
*   if it doesn’t work, Q&A with aider to fix
*   rinse repeat ✩₊˚.⋆☾⋆⁺₊✧

### Results

I have built so so many things using this workflow: scripts, expo apps, rust cli tools, etc. It has worked across programming languages, and contexts. I do like it.

If you have a small or large project that you are procrastinating on, I would recommend giving it a shot. You will be surprised how far you can get in a short amount of time.

My hack to-do list is empty because I built everything. I keep thinking of new things and knocking them out while watching a movie or something. For the first time in years, I am spending time with new programming languages and tools. This is pushing me to expand my programming perspective.

Non-greenfield: Iteration, incrementally
----------------------------------------

Sometimes you don’t have greenfield, and instead need to iterate or do increment work on an established code base.

![Image 3: a brown field](https://harper.blog/images/posts/brownfield.jpg)

This is not a green field. A random photo from my grandfather’s camera - somewhere in Uganda in the 60s

For this I have a slightly different method. It is similar to above, but a bit less “planning based.” The planning is done per task, not for the entire project.

### Get context

I think everyone who is knee-deep in AI dev has a different tool for this, but you need something to grab your source code and efficiently jam it into the LLM.

I currently use a tool called [repomix](https://github.com/yamadashy/repomix). I have a task collection defined in my global `~/.config/mise/config.toml` that allows me to do various things with my code base ([mise rules](https://mise.jdx.dev/)).

Here is the LLM task list:

```
LLM:clean_bundles           Generate LLM bundle output file using repomix
LLM:copy_buffer_bundle      Copy generated LLM bundle from output.txt to system clipboard for external use
LLM:generate_code_review    Generate code review output from repository content stored in output.txt using LLM generation
LLM:generate_github_issues  Generate GitHub issues from repository content stored in output.txt using LLM generation
LLM:generate_issue_prompts  Generate issue prompts from repository content stored in output.txt using LLM generation
LLM:generate_missing_tests  Generate missing tests for code in repository content stored in output.txt using LLM generation
LLM:generate_readme         Generate README.md from repository content stored in output.txt using LLM generation
```

I generate an `output.txt` that has the context from my code base. If I am blowing through tokens, and it is too big - I will edit the generate command to ignore parts of the code base that are not germane to this task.

> One thing really nice about `mise` is that the tasks can be redefined and overloaded in the working directory’s `.mise.toml`. I can use a different tool to dump/pack the code, and as long as it generates an `output.txt` I can use my LLM tasks. This is helpful when various codebases differ so much. I regularly override the `repomix` step to include broader ignore patterns, or just use a more effective tool to do the packing.

Once the output.txt is generated, I pass it to the [LLM](https://github.com/simonw/LLM) command to do various transformations and then save those as a markdown file.

Ultimately, the mise task is running this: `cat output.txt | LLM -t readme-gen > README.md` or `cat output.txt | LLM -m claude-3.5-sonnet -t code-review-gen > code-review.md`. This isn’t super complicated. the `LLM` command is doing the heavy lifting (supporting different models, saving keys, and using prompt templates).

For example, if I need a quick review and fix of test coverage I would do the following:

#### Claude

*   go to the directory where the code lives
*   run `mise run LLM:generate_missing_tests`
*   look at the generated markdown file (`missing-tests.md`)
*   grab the full context for the code: `mise run LLM:copy_buffer_bundle`
*   paste that into claude along with the first missing test “issue”
*   copy the generated code from claude into my ide.
*   …
*   run tests
*   rinse repeat ✩₊˚.⋆☾⋆⁺₊✧

#### Aider

*   go to the directory where the code lives
*   run aider (always make sure you are on a new branch for aider work)
*   run `mise run LLM:generate_missing_tests`
*   look at the generated markdown file (`missing-tests.md`)
*   paste the first missing test “issue” into aider
*   watch aider dance ♪┏(・o･)┛♪
*   …
*   run tests
*   rinse repeat ✩₊˚.⋆☾⋆⁺₊✧

This is a pretty good way to incrementally improve a code base. It has been super helpful to do small amounts of work in a big code base. I have found that I can do any sized tasks with this method.

### Prompt magic

These quick hacks work super well to dig into places where we can make a project more robust. It is super quick, and effective.

Here are some of my prompts that I use to dig into established code bases:

#### Code review

```
You are a senior developer. Your job is to do a thorough code review of this code. You should write it up and output markdown. Include line numbers, and contextual info. Your code review will be passed to another teammate, so be thorough. Think deeply  before writing the code review. Review every part, and don't hallucinate.
```

#### GitHub Issue generation

(I need to automate the actual issue posting!)

```
You are a senior developer. Your job is to review this code, and write out the top issues that you see with the code. It could be bugs, design choices, or code cleanliness issues. You should be specific, and be very good. Do Not Hallucinate. Think quietly to yourself, then act - write the issues. The issues will be given to a developer to executed on, so they should be in a format that is compatible with github issues
```

#### Missing tests

```
You are a senior developer. Your job is to review this code, and write out a list of missing test cases, and code tests that should exist. You should be specific, and be very good. Do Not Hallucinate. Think quietly to yourself, then act - write the issues. The issues  will be given to a developer to executed on, so they should be in a format that is compatible with github issues
```

These prompts are pretty _old and busted_ (“boomer prompts” if I may). They need some refactoring. If you have ideas to make them better lmk.

Skiing ᨒ↟ 𖠰ᨒ↟ 𖠰
-----------------

When I describe this process to people I say “you have to aggressively keep track of what’s going on because you can easily get ahead of yourself.”

For some reason I say “over my skies” a lot when talking about LLMs. I don’t know why. It resonates with me. Maybe it’s because it is beautiful smooth powder skiing, and then all of a sudden you are like “WHAT THE FUCK IS GOING ON!,” and are completely lost and suddenly fall off a cliff.

I find that using a **planning step** (ala the Greenfield process above) can help keep things under control. At least you will have a doc you can double-check against. I also do believe that testing is helpful - especially if you are doing wild style aider coding. Helps keep things good, and tight.

Regardless, I still do find myself **over my skis** quite a bit. Sometimes a quick break or short walk will help. In this regard it is a normal problem-solving process, but accelerated to a breakneck speed.

> We will often ask the LLM to include ridiculous things in our not very ridiculous code. For instance, we asked it to create a lore file and then reference the lore in the user interface. This is for python cli tools. Suddenly there is lore, glitchy interfaces, etc. All to manage your cloud functions, your todo list or whatever. The sky is the limit.

I am so lonely (｡•́︿•̀｡)
------------------------

My main complaint about these workflows is that it is largely a solo endeavor - i.e. the interfaces are all _single player mode_.

I have spent years coding by myself, years coding as a pair, and years coding in a team. It is always better with people. These workflows are not easy to use as a team. The bots collide, the merges are horrific, the context complicated.

I really want someone to solve this problem in a way that makes coding with an LLM a multiplayer game. Not a solo hacker experience. There is so much opportunity to fix this and make it amazing.

GET TO WORK!

ⴵ Time ⴵ
--------

All this codegen has accelerated the amount of code that I as a single person am able to generate. However, there is a weird side effect. I find myself having a huge amount of “downtime” while waiting for the LLM to finish burning its tokens.

![Image 4: Printing](https://harper.blog/images/posts/apple-print-shop-printing.png)

I remember this like it was yesterday

I have changed how I work enough to start incorporating some practice that will try and eat the waiting time:

*   I start the “brainstorming” process for another project
*   I listen to records
*   I play [cookie clicker](https://orteil.dashnet.org/cookieclicker/)
*   I talk with friends and robots

It is awesome to be able to hack like this. Hack Hack Hack. I can’t think of another time I have been this productive in code.

Haterade ╭∩╮( •̀\_•́ )╭∩╮
-------------------------

A lot of my friends are like “fuck LLMs. They are terrible at everything.” I don’t mind this POV. I don’t share it, but I think it is important to be skeptical. There are an awful lot of reasons to hate AI. My main fear is about power consumption and the environmental impact. But… the code must flow. Right… sigh.

If you are open to learning more, but don’t want to dig in and become a cyborg programmer - my recommendation is not to change your opinion, but to read Ethan Mollick’s book about LLMs and how they can be used: [**Co-Intelligence: Living and Working with AI.**](https://www.penguinrandomhouse.com/books/741805/co-intelligence-by-ethan-mollick/)

It does a good job of explaining the benefits without being a tech anarcho-capitalist bro type tome. I found it very helpful, and have had so many good and nuanced conversations with friends who have read it. Highly recommended.

If you are skeptical, but a bit curious - feel free to hit me up and let’s talk through all this madness. I can show you how we use LLMs, and maybe we could build something together.

_thanks to [Derek](https://derek.broox.com/), [Kanno](https://nocruft.com/), [Obra](https://fsck.com/), and [Erik](https://thinks.lol/) for taking a look at this post and suggesting edits. I appreciate it._
