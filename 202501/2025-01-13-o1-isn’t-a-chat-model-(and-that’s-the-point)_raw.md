Title: o1 isn’t a chat model (and that’s the point)

URL Source: https://www.latent.space/p/o1-skill-issue

Published Time: 2025-01-12T00:26:49+00:00

Markdown Content:
_swyx here: We’re proud to feature our first guest post[1](https://www.latent.space/p/o1-skill-issue#footnote-1-154642736) of 2025! It has spawned great discussions on [gdb](https://x.com/gdb/status/1878489681702310392), [Ben](https://x.com/benhylak/status/1878237490194366744), and [Dan’s](https://x.com/daniel_mac8/status/1878423666309902404) pages._

_Since o1’s launch in October and o1 pro/o3’s announcement in December, many have been struggling to figure out their takes, both [positive](https://x.com/tigransloyan/status/1864845328752808167?s=46) and [negative](https://news.ycombinator.com/item?id=42565606). We took a [strongly positive stance](https://www.latent.space/p/chatgpt-max) at the [nadir of o1 Pro sentiment](https://x.com/jasondeanlee/status/1870883464767242360?s=46) and mapped out what it would likely take for OpenAI to have a $2000/month agent product ([rumored to be launched in the next few weeks](https://www.theverge.com/2024/11/13/24295879/openai-agent-operator-autonomous-ai)). Since then, [o1 has sat comfortably at #1](https://x.com/lmarena_ai/status/1873695386323566638) across ALL LMArena leaderboards (soon to have default [Style Control as we discussed on pod](https://latent.space/p/lmarena))._

_We’ve been following Ben Hylak’s work on the Apple VisionOS for a bit, and invited him to [speak at the World’s Fair](https://www.youtube.com/watch?v=5nOLb27hQ5w). He has since launched [Dawn Analytics](https://x.com/benhylak/status/1839014819753775167), and continued to publish unfiltered thoughts about o1 — initially as a loud skeptic, and slowly becoming a daily user. We love [mind-changers](https://www.swyx.io/guo-lai-ren) in both its meanings, and think this same conversation is happening all over the world as people struggle to move from the chat paradigm to the brave new world of reasoning and $x00/month prosumer AI products like Devin ([spoke at WF](https://www.youtube.com/watch?v=T7NWjoD_OuY), [now GA](https://www.cognition.ai/blog/devin-generally-available)). Here are our thoughts._

_PSA: Due to overwhelming demand (\>15x applications:slots), we are closing CFPs for [AI Engineer Summit](https://apply.ai.engineer/) tomorrow. Last call! Thanks, we’ll be reaching out to all shortly!_

**How did I go from hating o1 to using it everyday for my most important questions?**

**I learned how to use it.**

When [o1 pro was announced](https://buttondown.com/ainews/archive/ainews-200-chatgpt-pro-and-o1-fullpro-with-vision/), I subscribed without flinching. **To justify the $200/mo price tag, it just has to provide 1-2 Engineer hours a month** (the less we have to hire at [dawn](http://dawnai.com/), the better!)

But at the end of a day filled with earnest attempts to get the model to work — I concluded that **it was garbage**.

Every time I asked a question, I had to wait 5 minutes only to be greeted with a massive wall of self-contradicting gobbledygook, complete with unrequested architecture diagrams + pro/con lists.

I [tweeted as much](https://x.com/benhylak/status/1864835651725910023) and a lot of people agreed — but more interestingly to me, some disagreed vehemently. In fact, they were mind-blown by just how good it was.

Sure, people often get very hypey about OpenAI after launches (it’s the second best strategy to go viral, right after being negative.)

But this felt different — these takes were coming from folks deep in the trenches.

The more I started talking to people who disagreed with me, the more I realized I was getting it completely wrong:

**I was using o1 like a chat model — but o1 is not a chat model.**

If o1 is not a chat model — what is it?

I think of it like a “report generator.” If you give it enough context, and tell it what you want outputted, it’ll often nail the solution in one-shot.

> _swyx’s Note: OpenAI does [publish advice on prompting o1](https://platform.openai.com/docs/guides/reasoning#advice-on-prompting), but we find it incomplete, and in a sense you can view this article as a “Missing Manual” to lived experience using o1 and o1 pro in practice._

Give a ton of context. Whatever you think I mean by a “ton” — 10x that.

[![Image 31](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5407ad16-67a5-4683-aa4c-0af8caaa0f5f_2020x1682.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5407ad16-67a5-4683-aa4c-0af8caaa0f5f_2020x1682.png)

When you use a chat model like Claude 3.5 Sonnet or 4o, you often start with a simple question and some context. If the model needs more context, it’ll often ask you for it (or it’ll be obvious from the output).

You iterate back and forth with the model, correcting it + expanding on requirements, until the desired output is achieved. It’s almost like pottery. **The chat models essentially pull context from you** via this back and forth. Overtime, our questions get quicker + lazier — as lazy as they can be while still getting a good output.

o1 will just take lazy questions at face value and doesn’t try to pull the context from you. Instead, you need to **push as much context as you can into o1**.

Even if you’re just asking a simple engineering question:

*   Explain everything that you’ve tried that didn’t work
    
*   Add a full dump of all your database schemas
    
*   Explain what your company does, how big it is (and define company-specific lingo)
    

In short, treat o1 like a new hire. Beware that _o1’s mistakes include reasoning about how much it should reason._ Sometimes the variance fails to accurately map to task difficulty. e.g. if the task is really simple, it will often spiral into reasoning rabbit holes for no reason. _Note: the o1 API allows you to [specify low/medium/high reasoning\_effort](https://buttondown.com/ainews/archive/ainews-o1-api-4o4o-mini-in-realtime-api-webrtc/), but that is not exposed to ChatGPT users._

> **Tips to make it easier giving o1 context**
> 
> 1.  I suggest using the **Voice Memos app** on your mac/phone. I just describe the entire problem space for 1-2 minutes, and then paste that transcript in.
>     
>     *   I actually have a note where I keep long segments of context to re-use.
>         
>     *   _swyx: I use [Careless Whisper](https://carelesswhisper.app/) by Sarav from the LS Discord_
>         
> 2.  The AI assistants that are popping up inside of products can often make this extraction easier. For example, if you use Supabase, try asking the Supabase Assistant to dump/describe all of the relevant tables/RPC’s/etc.
>     

Once you’ve stuffed the model with as much context as possible — _**focus on explaining what you want the output to be.**_

With most models, we’ve been trained to tell the model _how_ we want it to answer us. e.g.“You are an expert software engineer. Think slowly + carefully”

This is the opposite of how I’ve found success with o1. I don’t instruct it on the _how_ — only the _what_. Then let o1 take over and plan and resolve its own steps. This is what the autonomous reasoning is for, and can actually be much faster than if you were to manually review and chat as the “human in the loop”.

[![Image 32](https://substackcdn.com/image/fetch/w_2400,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F022016e9-09a2-4070-bf64-e2f1bbe56955_2120x1448.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F022016e9-09a2-4070-bf64-e2f1bbe56955_2120x1448.png)

swyx’s poor illustration attempt

> _**swyx’s pro tip**: developing really good criteria for what you consider to be “good” vs “bad” helps you **give the model a way to evaluate its own output** and self-improve/fix its own mistakes. Essentially **you’re [moving the LLM-as-Judge](https://x.com/swyx/status/1878554396784820662) into the prompt and letting o1 run it whenever needed.**_
> 
> [![Image 33](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe4d8ee50-e218-4389-b485-bf44ff275188_1182x740.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe4d8ee50-e218-4389-b485-bf44ff275188_1182x740.png)
> 
> _As a bonus, this eventually gives you LLM-as-Judge evaluators you can use for [Reinforcement Finetuning](https://www.interconnects.ai/p/openais-reinforcement-finetuning) when it is GA._

This requires you to **really know exactly what you want** (and you should really ask for one specific output per prompt — it can only reason at the beginning!)

Sounds easier than it is! Did I want o1 to implement a specific architecture in production, create a minimal test app, or just explore options and list pros/cons? These are all entirely different asks.

o1 often defaults to explaining concepts with a report-style syntax — completely with numbered headings and subheadings. If you want to skip the explanations and output complete files — you just need to explicitly say that.

Since learning how to use o1, I’ve been pretty mind-blown by its ability to generate the right answer the first time. It’s really pretty much better in every single way (besides cost/latency). Here are a few little moments where this has particularly stood out:

**What o1 does well:**

*   **Perfectly one-shotting entire/multiple files**: This, by far, is o1’s most impressive ability. I copy/paste a ton of code in, a ton of context about what I’m building, and it’ll completely one-shot the entire file (or files!), usually free of errors, following existing patterns I have in my codebase.
    
*   **Hallucinates Less**: In general, it just seems to confuse things less. For example, o1 really nails bespoke query languages (like ClickHouse and New Relic), where Claude often confuses the syntax for Postgres.
    
*   **Medical Diagnoses:** My girlfriend is a dermatologist — so whenever any friend or anyone in my extended family has any sort of skin issue, they’re sure to send her a picture! Just for fun, I started asking o1 in parallel. It’s usually shockingly close to the right answer — maybe 3/5 times. More useful for medical professionals — **it almost always provides an extremely accurate differential diagnosis.**
    
*   **Explaining Concepts:** I’ve found that it is very good at explaining very difficult engineering concepts, with examples. It’s almost like it generates an entire article.
    
    When I’m working on difficult architectural decisions, I will often have o1 generate multiple plans, with pros/cons for each, and even compare those plans. I’ll copy/paste the responses as PDF’s, and compare them — almost like I’m considering proposals.
    
*   **Bonus: Evals.** I have historically been very skeptical of using LLM as a Judge for Evals, because fundamentally the judge model often suffers from the same failure modes as what generated the outputs in the first place. o1, however, shows a ton of promise — it is often able to determine if a generation is correct or not with very little context.
    

**What o1 doesn’t do well (yet):**

*   **Writing in specific voices/styles:** No, I did not use o1 to write this post :)
    
    I’ve found that it’s pretty bad at writing anything, especially in specific voices or styles. It has a very academic/corporate report style that it wants to follow. I think that there are just so many reasoning tokens biasing the tone in that direction, it’s very hard to break free from that.
    
    Here’s an example of me trying to get it to write this post — this is after much back and forth — it just wants to produce a bland school report.
    
    [![Image 34](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5a333a21-de27-4e1b-adba-558d743d811d_1382x930.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5a333a21-de27-4e1b-adba-558d743d811d_1382x930.png)
    
*   **Building an Entire App:** o1 is mindblowingly good at one-shotting entire files. that being said, despite some of the more… optimistic… demos you might see on twitter — o1 is not going to build an entire SaaS for you, at least not with a _**lot**_ of iteration. **But it** _**can**_ **pretty much one-shot entire features, especially if they’re front-end or simple backend features**.
    

**Latency fundamentally changes our experience of a product.**

> _swyx: we agree - as much as [6 grades of AI latency](https://www.latent.space/p/inference-fast-and-slow) are common now._
> 
> [![Image 35: Inference, Fast and Slow](https://substackcdn.com/image/fetch/w_140,h_140,c_fill,f_auto,q_auto:good,fl_progressive:steep,g_auto/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9b148d1c-c5ee-4345-bc8f-6c4c79992894_1071x446.png)](https://www.latent.space/p/inference-fast-and-slow)

Consider the differences between mail, email and texting — it’s mainly just latency. A voice message vs. a phone call — latency. A video vs a Zoom — latency. And so on.

I call o1 a “report generator” because it’s clearly not a chat model — it feels a lot more like email.

This hasn't yet manifested in o1's product design. I would love to see the design more honestly reflected in the interface.

Here are some **specific AI** **UX tips for anyone building o1-based products**:

1.  Make it easier to see the hierarchy of the response (think a **mini table of contents**)
    
2.  **Similarly, make the hierarchy more easily navigable.** Since every request is usually larger than the height of the window, I would take a Perplexity like approach where each question/answer page gets a section vs. freeform scroll. Within an answer, things like sticky headers, collapsible headers, etc. could really help)
    
3.  **Make it easier to manage and see the context you’re providing** to the model. (Ironically Claude’s UI does a much better job of this — when you paste in a long piece of text, it renders as a little attachment). I also find that ChatGPT Projects don’t work nearly as well as Claude’s, so I’m copying and pasting stuff _a lot._
    

Side note:

*   Separately ChatGPT is _REALLY_ buggy when it comes to o1. The descriptions of reasoning are comical, it often completely fails to generate, and most often doesn’t work on the mobile app.
    
    [![Image 36](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ffaaa7faf-3a1c-4675-b1e1-e929a7143dc3_962x390.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ffaaa7faf-3a1c-4675-b1e1-e929a7143dc3_962x390.png)
    
    A beautiful day in… Kenya??
    

I’m really excited to see how these models actually get used.

I think o1 will make certain products possible for the first time — for example, products that can benefit from high-latency, long running background intelligence.

What sort of tasks is a user willing to wait 5 minutes for? An hour? A day? 3-5 business days?

A bunch, I think, if it’s designed correctly.

As models get more expensive, experimentation gets harder to justify. It’s easier than ever to waste $1000s of dollars in just minutes.

o1-preview and o1-mini support streaming, but they don’t support structured generation or system prompts. o1 supports structured generation and system prompts, but not streaming yet.

Given how long a response takes, streaming feels like a requirement.

It will be very cool to see what developers actually do with the model as they get to work in 2025.

_swyx: Thanks Ben! Last plug - if you’re **building agents** with o1, or managing a team of AI engineers, you should definitely apply to [AIES NYC](https://www.latent.space/p/2025-summit)._
