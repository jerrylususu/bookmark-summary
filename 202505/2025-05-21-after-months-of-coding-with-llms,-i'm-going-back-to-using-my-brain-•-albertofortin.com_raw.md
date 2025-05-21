Title: After months of coding with LLMs, I'm going back to using my brain • albertofortin.com

URL Source: https://albertofortin.com/writing/coding-with-ai

Markdown Content:
A few months ago I needed to build a new infrastructure for my SaaS, as the current PHP+MySQL combo was not fit for purpose anymore. I was excited about the opportunity to make the most of all the new LLMs I'd been playing with, so I set aside my SWE hat and I started acting as a product manager, chatting with Claude about best practices, doing some research on my own and then coming up with a plan, after many back and forths. I ended up choosing Go+Clickhouse.

When it was time to start coding, I asked Claude to give me a big and complicated markdown file outlining my existing infrastructure, my desired new infrastructure, what I’m trying to achieve, why I'm doing it, etc.

So I put it all inside Cursor Notepads and I start prompting away. Cursor writes code, I build it and test it. I'm quite happy with how things are going, the codebase isn't the tidiest but things seems to work. I'm aiming for speed more than code cleanliness - my SaaS business customers told me they need specific data and this new infrastructure is the only way I can deliver it. I have a few more potential customers who are waiting for me to tell them this is ready so they can purchase a plan. Every day I don’t have this ready, I’m literally losing money.

But then a few weeks go by, and the cracks start to show. I start getting frustrated. Every day I feel like I’m really close to the end product, then I find another issue that sets me back for days. 

I justify it thinking that I’ve never used Go or Clickhouse before, so it makes sense that it takes me a bit longer than I’m used to to fix those issues. The problems continue though, and I’m getting more frustrated. Cursor is not helping as much anymore. I paste in error messages, and I get a fix in response but then something breaks somewhere else. The more detailed the problem, the harder it is for the LLM to provide the actual solution. So I start actually looking at the code more closely, trying to understand it. 

I’ve been a software engineer for 15 years, and I studied C++ and Java in school, so I do have a rough idea of what’s happening in these Go files. But I have no concept of Go or Clickhouse best practices.

I start educating myself a bit more about those. I read some documentation, articles, I watch a YouTube video about Clickhouse. I become more inquisitive with Claude, asking detailed questions and challenging its answers.

One morning, I decide to actually inspect closely what’s all this code that Cursor has been writing. It’s not like I was blindly prompting without looking at the end result, but I was optimizing for speed and I hadn’t actually sat down just to review the code. I was just building building building.

So I do a “coding review” session. And **the horror ensues.**

Two service files, in the same directory, with similar names, clearly doing a very similar thing. But the method names are different. The props are not consistent. One is called "WebAPIprovider", the other one "webApi". They represent the same exact parameter. The same method is redeclared multiple times across different files. The same config file is being called in different ways and retrieved with different methods.

No consistency, no overarching plan. It’s like I'd asked 10 junior-mid developers to work on this codebase, with no Git access, locking them in a room without seeing what the other 9 were doing.

And before you ask, yes, I was feeding context to LLMs, lots of it. I was mostly using Gemini specifically for its larger context window. Every time I needed a different iteration of the same kind of file I gave specific instructions to take example from those. But it wasn’t enough.

**Taking a step back**

By now it’s clear that I need to change my approach. I’m a software engineer first and foremost, so it’s stupid not to make the most of my skills. I’ve been teaching myself more about Go and Clickhouse, and I’ve taken a step back from building at full speed. I’m going through files and rewriting code. Not everything, just the things that make me want to vomit. The language might be different but I know in my head what I want things to look like and how to organise them.

Since I’ve taken a step back, debugging has become easier. Maybe I’m not as fast but I don’t have this weird feeling of “_I kinda wrote this code but I actually have no idea what’s in it_”. I’m still using LLMs, but for dumber things: "rename all occurrences of this parameter", or "here’s some pseudo code, give me the Go equivalent".

The hardest part in all of this has been resisting the urge to use AI. I have this amazing tool available and it could write these 10 files in a minute. I’m wasting time by not using it! And that’s when it hit me. **I’ve not been using my brain as much.**I'm subconsciously defaulting to AI for all things coding.

I’ve been using pen and paper less. As soon as I need to plan a new feature, my first thought is asking o4-mini-high how to do it, instead of my neurons. I hate this. And I’m changing it.

So yes, I’m worried about the impact of AI, but I’m not worried about the jobs, I’m worried about losing my mental sharpness, my ability to plan out features and write tidy and functional code.

So I’m taking a big step back, really limiting how much AI I use. I’m defaulting to pen and paper, I’m defaulting to coding the first draft of that function on my own. And if I’m not sure I’ll use an LLM to check if that’s a good solution, if that’s a good naming convention, or how I can finish that last part.

But I’m not asking it to write new things from scratch, to come up with ideas or to write a whole new plan. I’m writing the plan. I’m the senior dev. The LLM is the assistant.

**A happy medium**

Now that I've changed my approach, I’m not frustrated with LLMs anymore. I have once again very low expectations, so when they do something well it’s a nice surprise. I’m trying to be smart about how I use them, they're such a great tool for learning for example. I’m leveraging them to learn Go, to upskill myself. And then I apply this new knowledge when I code.

But I feel worried for non coders. I almost feel like they’re in a worse position now with AI than they were in the no-code era. At least a no-code tool has been written by a human with common sense, and even if its features are limited, at least there’s some sort of structure.

“Vibe coding”, or whatever “coding with AI without knowing how to code” is called, is as of today a recipe for disaster, if you’re building anything that’s not a quick prototype.

I cannot imagine what coding with Cursor must feel like, for a non coder. Or maybe I can. Walls of code you don’t understand, error after error that you keep pasting into a chat box, which gives you back more code, which makes things even messier and complicated and, at some point, just wrong. And impossible to fix.

**A note for AI enthusiasts**

I can hear the horde of AI coding experts screaming at me: you should have used <newest-model>! You should have used Cursor rules! You should have followed this 15 step gamechanger workflow I found on Reddit the other day!

I have. I tried, I really did. There’s some things that AI cannot do just yet.

And while I haven’t tried every single combination of tools, agentic workflows, etc, I remain confident in my statement.If you don’t believe me, try being someone with no prior knowledge of Clickhouse, asking an LLM to write a complicated query involving multiple 100M+ rows tables, without triggering memory errors, on a server with limited RAM. 

It just can’t, even if you give it the whole SQL schema, even if you link the latest Clickhouse documentation, even if you outline in granular detail your business needs and infrastructure constraints. Newest Gemini can’t, o4-mini-high can’t, o3 can’t, Sonnet 3.7 can’t.

Also, if I need hours to set up a complicated system just so the AI doesn’t build a house of cards instead of the app I needed, is it really worth it? Especially when there’s no consistency in the model's performance, so even if you find the absolutely perfect workflow, it doesn’t last for long. Or it stops working as soon as you need it for something slightly different.

Let me be clear: I'm writing this as someone super excited about new tech, someone who loves to be an early adopter, someone who is still really enthusiastic about AI. I think and hope we’ll get there eventually, but as of right now we’re in a very weird time, where the tools look amazing, everyone tells you they’re amazing, but they’re actually good-but-not-great, and they're potentially making us dumber.

It’s a confusing experience. It’s like I need to get somewhere and I can either walk, or jump on this spaceship that travels at 900mph, but its controls are half in Hungarian and half in Ancient Greek. With enough trial and error I can probably get the spaceship to take me to my destination, but that’s a lot of work in itself and at the end of the day I’m left wondering if I should have just walked.

To make it all worse, I feel like we’re constantly being gaslighted by benchmarks, by influencers who can now sell you this new magic shovel, and by a flurry of companies that are trying to convince us that it’s an “agent” and definitely not just another cron job.

Some days I feel like we’re also being gaslit by LLM providers. Just look at any AI related subreddit, and you’ll see people having completely opposite experiences, with the same exact model, with the same prompt, on the same day. If you code with AI long enough you’ll be able to relate. One day it’s amazing, the next day it’s incredibly stupid.

Are they throttling the GPUs? Are these tools just impossible to control? What the fuck is going on?
