Title: Lessons on thinking from large language models

URL Source: https://www.seangoedecke.com/learning-from-how-llms-think/

Markdown Content:
Large language models have gotten much better at thinking in the past few years[1](https://www.seangoedecke.com/learning-from-how-llms-think/#fn-1). Billions of dollars have been spent to study how they think and how they can be made to think better. It would be surprising if none of those insights applied to how humans think. What can we learn about thinking from how LLMs think?

Rich Sutton’s “bitter lesson” famously [claimed](https://www.cs.utexas.edu/~eunsol/courses/data/bitter_lesson.pdf) that encoding symbolic logic into LLMs or using other clever tricks will always be an inferior approach to just scaling up the training data or spending more compute time doing search. This claim has been borne out spectacularly by the latest developments in AI research. Similarly, time spent theorizing about what a software engineering job involves is less useful than time spent writing more code or solving more problems. You’re probably better off _just doing more work_ than trying to master a theoretical approach to software engineering.

LLMs often exhibit “error reinforcement”. When you’re trying to get them to solve a tricky problem, sometimes their first mistake stays in the context and pushes them to keep repeating it, no matter what you say. If you start again in a fresh chat with a slightly tweaked prompt, they avoid the trap. Humans do this too. When you feel like you’re in a loop and making the same mistakes, clear your own context window: get up, go do things that are the opposite of writing code, and fill your short-term memory with completely different content. When you pick the problem back up you might have a better chance at fixing it.

LLMs do better when given tokens to think with before answering. If you ask a LLM to immediately answer, it’ll often get it wrong; if you ask a LLM to write down how it might approach the problem and then answer, it has a much higher chance of getting it right. When you’re thinking about a problem of your own, write down your thoughts step-by-step. I do this one a lot. In fact, my written chain-of-thought looks a lot like a LLM’s chain of thought: one sentence per line, with each sentence beginning with words like “Then”, “Wait,” or “Hold on”. This also helps me get back into the problem after taking a break.

The [s1](https://arxiv.org/abs/2501.19393) paper showed that you can significantly increase the power of a fine-tuned reasoning model by artificially inserting a “wait” token whenever it tries to stop thinking. The model will continue by finding a reason to double-check its answer. Likewise, when you come up with a solution or a block of code, think “wait” and find your own reason why your solution might not be the best one.

Reasoning LLMs are qualitatively different from non-reasoning LLMs. Even the smartest non-reasoning LLMs have to be taught (or to teach themselves) how to think for a long time about a single problem. Likewise, the ability to spend a long time on a single problem is a distinct skill for humans as well. Many people have a lot of brainpower and can instantly solve a wide array of easy problems, but struggle when they can’t see an instant solution. Spending time consciously reasoning about hard problems trains that skill. If you can’t sit and reason about a hard problem, you’ll get beaten by less intelligent people who can (just as GPT-4 and Claude get beaten by much smaller reasoning models).

In summary:

*   Don’t learn by building theories, learn by doing the work
*   If you’re going in circles on a problem, clear your context window before trying again
*   Write down your own chain-of-thought when you’re solving a hard problem
*   When you get a solution, force yourself to re-evaluate before accepting it
*   Your ability to reason about a hard problem is as important as your raw brainpower, and ought to be trained separately

February 15, 2025

* * *
