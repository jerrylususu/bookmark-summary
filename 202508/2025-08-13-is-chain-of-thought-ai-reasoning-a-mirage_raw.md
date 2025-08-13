Title: Is chain-of-thought AI reasoning a mirage?

URL Source: https://www.seangoedecke.com/real-reasoning/

Markdown Content:
Reading research papers and articles about chain-of-thought reasoning[1](https://www.seangoedecke.com/real-reasoning/#fn-1) makes me frustrated.

There are many interesting questions to ask about chain-of-thought: how accurately it reflects the actual process going on, why training it “from scratch” often produces chains that switch fluidly between multiple languages, and so on. However, people keep asking the least interesting question possible: **whether chain-of-thought reasoning is “really” reasoning**.

Apple took up this question in their [Illusion of Thinking](https://www.seangoedecke.com/illusion-of-thinking) paper, which I’ve already written about. Now there’s a [paper](https://arxiv.org/pdf/2508.01191) from Arizona State University that’s getting some attention called _Is Chain-of-Thought Reasoning of LLMs a Mirage?_ As will become clear, I do not think this is a very good paper.

### What does the Arizona State paper argue?

Here’s the core point:

> CoT reasoning works effectively when applied to in-distribution or near in-distribution data but becomes fragile and prone to failure even under moderate distribution shifts. In some cases, LLMs generate fluent yet logically inconsistent reasoning steps. The results suggest that what appears to be structured reasoning can be a mirage, emerging from memorized or interpolated patterns in the training data rather than logical inference.

The strategy of the paper is to train a small transformer model (~600k params) on a corpus of non-language data transformations. What does this mean? As far as I can tell, that when prompted with something like “A B C D [M1]”, the model should respond “B C D E”, if the “M1” operation in training data means “advance each letter forward by one”[2](https://www.seangoedecke.com/real-reasoning/#fn-2). The training data contained several kinds of operation, which were composed arbitrarily (e.g. “A B C D [M1] [M1]” should produce “C D E F”). Finally, the training data included chains-of-thought like:

```
A B C D [M1] [M1]
<think>
B C D E [M1]
</think>
C D E F
```

Overall, the idea is to teach the model a very simple way of expressing chains-of-thought to solve toy alphabet problems, which has the good effect of making it trivial to determine at scale if and when the model made a mistake in its reasoning. You can straightforwardly generate ten thousand completions and then algorithmically check the model’s work, which is what the paper did.

The paper draws all kinds of conclusions from these reasoning traces:

*   When a requested reasoning path (like ”[M1] [K1]”) doesn’t appear in the training data (even though the individual “M1” and “K1” operations do), their model struggled to actually perform the operations requested instead of outputting a similar path that was in the training data.
*   When the requested reasoning path is even a little bit longer than those in the training data, performance drops noticeably.
*   Any changes (even minor ones) to the format, like adding a meaningless “noise” token, cause the model to make many more mistakes.
*   The model can be rapidly fine-tuned to cope with any of these issues, but that only addresses the specific pattern being fine-tuned for.

From all this, the paper concludes that model chain-of-thought reasoning does not operate out-of-distribution, and is instead just copying specific reasoning patterns that occurred in the training data.

### What do I think about it?

I don’t like it. I am unconvinced that you can draw broad conclusions about reasoning models from the toy example in this paper, for a few reasons.

#### Reasoning and language

The first is that **reasoning probably requires language use**. Even if you don’t think AI models can “really” reason - more on that later - even simulated reasoning _has to be reasoning in human language_. Reasoning model traces are full of phrases like “wait, what if we tried” and “I’m not certain, but let’s see if” and “great, so we know for sure that X, now let’s consider Y”. In other words, reasoning is a sophisticated task that requires a sophisticated tool like human language.

Why is that? Because reasoning tasks require choosing between several different options. “A B C D [M1] -> B C D E” isn’t reasoning, it’s **computation**, because it has no mechanism for thinking “oh, I went down the wrong track, let me try something else”. That’s why the most important token in AI reasoning models is “Wait”. In fact, you can control how long a reasoning model thinks by arbitrarily [appending](https://arxiv.org/abs/2501.19393) “Wait” to the chain-of-thought. Actual reasoning models change direction all the time, but this paper’s toy example is structurally incapable of it.

#### Model size

The second problem is that **the model is just too small**. Reasoning models are a pretty recent innovation, but the idea is pretty obvious. Why is that? I’m pretty sure it’s because (prior to September 2024) the models were just not smart enough to reason. You couldn’t have built a reasoning model on top of GPT-3.5 - there’s just not enough raw brainpower there to perform the relevant operations, like holding multiple possible solutions “in memory” at the same time.

In other words, a 600k parameter model is smart enough to learn how to apply transformations in sequence, but not necessarily smart enough to decompose those transformations into their individual components. I appreciate that research has to be done on small models, but we _know_ that reasoning is an emergent capability! Even if you grant that what they’re measuring is reasoning, I am profoundly unconvinced that their results will generalize to a 1B, 10B or 100B model.

#### How do humans reason?

Even if both of my previous objections were invalid, this paper would still not justify its grandiose conclusions about a “mirage” of reasoning, because **it does not compare to how humans actually reason**. Here are some quotes from the paper:

> LLMs construct superficial chains of logic based on learned token associations, often failing on tasks that deviate from commonsense heuristics or familiar templates Models often incorporate … irrelevant details into their reasoning, revealing a lack of sensitivity to salient information models may overthink easy problems and give up on harder ones Together, these findings suggest that LLMs are not principled reasoners but rather sophisticated simulators of reasoning-like text

I want to tear my hair out when I read quotes like these, because _all of these statements are true of human reasoners_. Humans rely on heuristics and templates, include irrelevant details, overthink easy problems, and give up on hard ones all the time! The big claim in the paper - that reasoning models struggle when they’re out of domain - is true about even the strongest human reasoners as well.

**The “principled reasoner” being compared to here simply does not exist.** It’s a Platonic ideal. If you compared the messy way even very intelligent humans reason in practice to this ideal, they would fail as well. It’s almost a cliche that human experts can reason magnificently in their field, but fall apart entirely when reasoning outside of their field[3](https://www.seangoedecke.com/real-reasoning/#fn-3). Why would we be surprised that reasoning models reason like humans do, when they’re trained on large quantities of human or human-like reasoning text?

### Final thoughts

Whether AI reasoning is “real” reasoning or just a mirage can be an interesting question, but it is primarily a _philosophical_ question. It depends on having a clear definition of what “real” reasoning is, exactly. I’ve been out of the philosophy game for a while now, but I was in it long enough to know that there is no single consensus definition of ideal reasoning, and any candidate definitions run into serious problems very quickly. It’s not something you can handwave away in the introduction section of a machine learning paper.

I think the idea of training a toy model to do something kind of like reasoning is a really interesting strategy. If the _Is Chain-of-Thought Reasoning of LLMs a Mirage?_ paper had just been about that, I would have no problem with it. But these papers keep stapling on broad philosophical claims about whether models can “really reason” that are just completely unsupported by the content of the research.

I suggest the following heuristic when you’re reading a paper about model reasoning:

1.   If it claims that AI reasoning is somehow “fake”, check for a section where it (at minimum) directly assesses the quality of human reasoning skills, or ideally provides a tight philosophical definition of what “real” reasoning is.
2.   If it points at reasoning tasks that AI models fail at, check the task itself to see if it’s a task that actually requires reasoning (i.e. considering multiple approaches) or if it simply requires _computation_ (following a set algorithm).

Good model reasoning papers[4](https://www.seangoedecke.com/real-reasoning/#fn-4) pass both these conditions. Even though they’re skeptical of the power of chain-of-thought, they use tasks that have many paths to success (like mathematics or language puzzles), and they don’t draw sweeping conclusions about “real” reasoning.

* * *

1.   The process where language models “think out loud” before arriving at an answer, which forms the backbone of AI “reasoning models” like o1 and now GPT-5-Thinking.

[↩](https://www.seangoedecke.com/real-reasoning/#fnref-1)
2.   The paper itself doesn’t use “M1” - I’m picking an overly simple example here to make it easier to explain.

[↩](https://www.seangoedecke.com/real-reasoning/#fnref-2)
3.   See [this](https://www.smbc-comics.com/comic/2012-03-21), [epistemic trespassing](https://philpapers.org/archive/BALET-2.pdf), or the old observation that engineers are disproportionately represented among creationists.

[↩](https://www.seangoedecke.com/real-reasoning/#fnref-3)
4.   Like [https://arxiv.org/pdf/2402.14897](https://arxiv.org/pdf/2402.14897) and [https://arxiv.org/pdf/2505.05410](https://arxiv.org/pdf/2505.05410).

[↩](https://www.seangoedecke.com/real-reasoning/#fnref-4)

If you liked this post, consider [subscribing](https://buttondown.com/seangoedecke) to email updates about my new posts, or [sharing it on Hacker News](https://news.ycombinator.com/submitlink?u=https://www.seangoedecke.com/real-reasoning/).

August 13, 2025│ Tags: [ai](https://www.seangoedecke.com/tags/ai/)

* * *