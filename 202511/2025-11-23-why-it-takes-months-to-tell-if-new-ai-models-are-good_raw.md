Title: Why it takes months to tell if new AI models are good

URL Source: https://www.seangoedecke.com/are-new-models-good/

Markdown Content:
**Nobody knows how to tell if current-generation models are any good**. When GPT-5 launched, the overall mood was very negative, and the consensus was that it wasn’t a strong model. But three months later it turns out that GPT-5 (and its derivative GPT-5-Codex) is a very strong model for agentic work[1](https://www.seangoedecke.com/are-new-models-good/#fn-1): enough to break Anthropic’s monopoly on agentic coding models. In fact, GPT-5-Codex is my preferred model for agentic coding. It’s slower than Claude Sonnet 4.5, but in my experience it gets more hard problems correct. Why did it take months for me to figure this out?

### Evals systematically overstate how good frontier models are

The textbook solution for this problem is evals - datasets of test cases that models can be scored against - but **evals are largely unreliable**. Many models score very well on evals but turn out to be useless in practice. There are a couple of reasons for this.

First, **it’s just really hard to write useful evals for real-world problems**, since real-world problems require an enormous amount of context. Can’t you take previous real-world problems and put them in your evals - for instance, by testing models on already-solved open-source issues? You can, but you run into two difficulties:

*   Open-source coding is often meaningfully different from the majority of programming work. For more on this, see my comments in [_METR’S AI productivity study is really good_](https://www.seangoedecke.com/impact-of-ai-study), where I discuss an AI-productivity study that was done on open-source codebases.
*   You’re still only covering a tiny subset of all programming work. For instance, the well-known SWE-Bench set of coding evals are just in Python. A model might be really good at Python but struggle with other languages.

Another problem is that **evals are a target for AI companies**. How well Anthropic or OpenAI’s new models perform on evals has a direct effect on the stock price of those companies. It’d be naive to think that they don’t make some kind of effort to do well on evals: if not by directly training on public eval data[2](https://www.seangoedecke.com/are-new-models-good/#fn-2), then by training on data that’s close enough to eval data to produce strong results. I’m fairly confident that big AI companies _will not release a model_ unless they can point to a set of evals that their model does better than competitors. So you can’t trust that strong evals will mean a strong model, because every single new model is released with strong evals.

### Vibe checks are not reliable

If you can’t rely on evals to tell you if a new model is good, what can you rely on? For most people, the answer is the “vibe check”: interacting with the model themselves and making their own judgement.

Often people use a set of their own pet questions, which are typically questions that other LLMs get wrong (say, word puzzles). Trick questions can be useful, but plenty of strong models struggle with specific trick questions for some reason. My sense is also that current models are too strong for obvious word puzzles. You used to be able to trip up models with straightforward questions like “If I put a ball in a box, then put the box in my pocket, where is the ball?” Now you have to be more devious, which gives less signal about how strong the model is.

Sometimes people use artistic prompts. Simon Willison [famously](https://simonwillison.net/2024/Oct/25/pelicans-on-a-bicycle/) asks new models to produce a SVG of a pelican riding a bicycle. It’s now a common Twitter practice to post side-by-side “I asked two models to build an object in Minecraft” screenshots. This is cool - you can see at a glance that bigger models produce better images - but at some point it becomes difficult to draw conclusions from the images. If Claude Sonnet 4.5 puts the pelican’s feet on the pedals correctly, but GPT-5.1 adds spokes to the wheels, which model is better?

Finally, many people rely on pure vibes: the intangible sense you get after using a model about whether it’s good or not. This is sometimes described as “big model smell”. I am fairly agnostic about people’s ability to determine model capability from vibes alone. It seems like something humans might be able to do, but also like something that would be very easy to fool yourself about. For instance, I would struggle to judge a model with the conversational style of GPT-4o as very smart, but there’s nothing in principle that would prevent that.

### Evaluating practical use takes time

Of course, for people who engage in intellectually challenging pursuits, there’s an easy (if slow) way to evaluate model capability: just give it the problems you’re grappling with and see how it does. I often ask a strong agentic coding model to do a task I’m working on in parallel with my own efforts. If the model fails, it doesn’t slow me down much; if it succeeds, it catches something I don’t, or at least gives me a useful second opinion.

The problem with this approach is that it takes a fair amount of time and effort to judge if a new model is any good, **because you have to actually do the work**: if you’re not engaging with the problem yourself, you will have no idea if the model’s solution is any good or not. So testing out a new model can be risky. If it’s no good, you’ve wasted a fair amount of time and effort! I’m currently trying to decide whether to invest this effort into testing out Gemini 3 Pro or GPT-5.1-Codex - right now I’m still using GPT-5-Codex for most tasks, or Claude Sonnet 4.5 on some simpler problems.

### Is AI progress stagnating?

Each new model release reignites the debate over whether AI progress is stagnating. The most prominent example is Gary Marcus, who has written that [GPT-4](https://cacm.acm.org/blogcacm/gpt-4s-successes-and-gpt-4s-failures/), [GPT-4o](https://garymarcus.substack.com/p/hot-take-on-openais-new-gpt-4o), [Claude 3.5 Sonnet](https://x.com/GaryMarcus/status/1803800800277545266?lang=en), [GPT-5](https://garymarcus.substack.com/p/gpt-5-overdue-overhyped-and-underwhelming) and [DeepSeek](https://garymarcus.substack.com/p/five-ways-in-which-the-last-3-months) all prove that AI progress has hit a wall. But almost everyone who writes about AI seems to be interested in the topic. Each new model launch is watched to see if this is the end of the bubble, or if LLMs will continue to get more capable. The reason this debate never ends is that **there’s no reliable way to tell if an AI model is good**.

Suppose that base AI models were getting linearly smarter (i.e. that GPT-5 really was as far above GPT-4 as GPT-4 was above GPT-3.5, and so on). **Would we actually be able to tell?**

When you’re talking to someone who’s less smart than you[3](https://www.seangoedecke.com/are-new-models-good/#fn-3), it’s very clear. You can see them failing to follow points you’re making, or they just straight up spend time visibly confused and contradicting themselves. But when you’re talking to someone smarter than you, it’s far from clear (to you) what’s going on. You can sometimes feel that you’re confused by what they say, but that doesn’t necessarily mean they’re smarter. It could be that they’re just talking nonsense. And smarter people won’t confuse you all the time - only when they fail to pitch their communication at your level.

Talking with AI models is like that. GPT-3.5 was very clearly less smart than most of the humans who talked to it. It was mainly impressive that it was able to carry on a conversation at all. GPT-4 was probably on par with the average human (or a little better) in its strongest domains. GPT-5 (at least in thinking mode) is smarter than the average human across most domains, I believe.

Suppose we had no objective way of measuring chess ability. Would I be able to tell if computer chess engines were continuing to get better? I’d certainly be impressed when the chess engines went from laughably bad to beating me every time. But I’m not particularly good at chess. I would lose to chess engines from the _early 1980s_. It would thus seem to me as if chess engine progress had stalled out, when in fact modern chess engines have _double_ the rating of chess engines from the 1980s.

I acknowledge that “the model is now at least partly smarter than you” is an underwhelming explanation for why AI models don’t appear to be rapidly getting better. It’s easy to point to cases where even strong models fall over. But it’s worth pointing out that **if models were getting consistently smarter, this is what it would look like**: rapid subjective improvement as the models go from less intelligent than you to on par with you, and then an immediate plateau as the models surpass you and you become unable to tell how smart they are.

### Summary

*   Nobody knows how good a model is when it’s launched. Even the AI lab who built it are only guessing and hoping it’ll turn out to be effective for real-world use cases.
*   Evals are mostly marketing tools. It’s hard to figure out how good the eval is, or if the model is being “taught to the test”. If you’re trying to judge models from their public evals you’re fighting against the billions of dollars of effort going into gaming the system.
*   Vibe checks don’t test the kind of skills that are useful for real work, but testing a model by using it to do real work takes a lot of time. You can’t figure out if a brand new model is good that way.
*   Because of all this, it’s very hard to tell if AI progress is stagnating or not. Are the models getting better? Are they any good right now?
*   Compounding that problem, it’s hard to judge between two models that are both smarter than you (in a particular domain). If the models _do_ keep getting better, we might expect it to feel like they’re plateauing, because once they get better than us we’ll stop seeing evidence of improvement.

* * *

1.   By “agentic work” I mean “LLM with tools that runs in a loop”, like Copilot Agent Mode, Claude Code, and Codex. I haven’t yet tried GPT-5.1-Codex enough to have a strong opinion.

[↩](https://www.seangoedecke.com/are-new-models-good/#fnref-1)
2.   If you train a model on the actual eval dataset itself, it will get very good at answering those specific questions, even if it’s not good at answering those _kinds_ of questions. This is often called “benchmaxxing”: prioritizing evals and benchmarks over actual capability.

[↩](https://www.seangoedecke.com/are-new-models-good/#fnref-2)
3.   I want to bracket the question of whether “smart” is a broad category, or how exactly to define it. I’m talking specifically about the way GPT-4 is smarter than GPT-3.5 - even if we can’t define exactly how, we know that’s a real thing.

[↩](https://www.seangoedecke.com/are-new-models-good/#fnref-3)

If you liked this post, consider[subscribing](https://buttondown.com/seangoedecke)to email updates about my new posts, or[sharing it on Hacker News](https://news.ycombinator.com/submitlink?u=https://www.seangoedecke.com/are-new-models-good/&t=Why%20it%20takes%20months%20to%20tell%20if%20new%20AI%20models%20are%20good). Here's a preview of a related post that shares tags with this one.

> Only three kinds of AI products actually work
> 
> 
> 
> The very first LLM-based product, ChatGPT, was just the ability to talk with the model itself: in other words, a pure chatbot. This is still the most popular LLM product by a large margin.
> 
> 
> In fact, given the amount of money that’s been invested in the industry, it’s shocking how many “new AI products” are just chatbots. As far as I can tell, **there are only three types of AI product that currently work**.
> 
> [Continue reading...](https://www.seangoedecke.com/ai-products/)

* * *