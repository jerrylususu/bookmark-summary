Title: AI Mistakes Are Very Different from Human Mistakes - Schneier on Security

URL Source: https://www.schneier.com/blog/archives/2025/01/ai-mistakes-are-very-different-from-human-mistakes.html

Published Time: 2025-01-21T12:02:47+00:00

Markdown Content:
Humans make mistakes all the time. All of us do, every day, in tasks both new and routine. Some of our mistakes are minor and some are catastrophic. Mistakes can break trust with our friends, lose the confidence of our bosses, and sometimes be the difference between life and death.

Over the millennia, we have created security systems to deal with the sorts of mistakes humans commonly make. These days, casinos rotate their dealers regularly, because they make mistakes if they do the same task for too long. Hospital personnel write on limbs before surgery so that doctors operate on the correct body part, and they count surgical instruments to make sure none were left inside the body. From copyediting to double-entry bookkeeping to appellate courts, we humans have gotten really good at correcting human mistakes.

Humanity is now rapidly integrating a wholly different kind of mistake-maker into society: AI. Technologies like [large language models](https://spectrum.ieee.org/tag/llms) (LLMs) can perform many cognitive tasks traditionally fulfilled by humans, but they make plenty of mistakes. It seems [ridiculous](https://www.buzzfeed.com/carleysuthers/weird-and-wrong-ai-responses) when chatbots tell you to eat rocks or add glue to pizza. But it’s not the frequency or severity of AI systems’ mistakes that differentiates them from human mistakes. It’s their weirdness. AI systems do not make mistakes in the same ways that humans do.

Much of the friction—and risk—associated with our use of AI arise from that difference. We need to invent new [security](https://spectrum.ieee.org/tag/security) systems that adapt to these differences and prevent harm from AI mistakes.

### Human Mistakes vs AI Mistakes

Life experience makes it fairly easy for each of us to guess when and where humans will make mistakes. Human errors tend to come at the edges of someone’s knowledge: Most of us would make mistakes solving calculus problems. We expect human mistakes to be clustered: A single calculus mistake is likely to be accompanied by others. We expect mistakes to wax and wane, predictably depending on factors such as fatigue and distraction. And mistakes are often accompanied by ignorance: Someone who makes calculus mistakes is also likely to respond “I don’t know” to calculus-related questions.

To the extent that AI systems make these human-like mistakes, we can bring all of our mistake-correcting systems to bear on their output. But the current crop of AI models—particularly LLMs—make mistakes differently.

AI errors come at seemingly random times, without any clustering around particular topics. LLM mistakes tend to be more evenly distributed through the knowledge space. A model might be equally likely to make a mistake on a calculus question as it is to propose that [cabbages](https://arxiv.org/html/2405.19616v1) eat goats.

And AI mistakes aren’t accompanied by ignorance. A LLM will be [just as confident](https://spectrum.ieee.org/chatgpt-reliability) when saying something completely wrong—and obviously so, to a human—as it will be when saying something true. The seemingly random [inconsistency](https://arxiv.org/pdf/2305.14279) of LLMs makes it hard to trust their reasoning in complex, multi-step problems. If you want to use an AI model to help with a business problem, it’s not enough to see that it understands what factors make a product profitable; you need to be sure it won’t forget what money is.

### How to Deal with AI Mistakes

This situation indicates two possible areas of research. The first is to engineer LLMs that make more human-like mistakes. The second is to build new mistake-correcting systems that deal with the specific sorts of mistakes that LLMs tend to make.

We already have some tools to lead LLMs to act in more human-like ways. Many of these arise from the field of “[alignment](https://arxiv.org/abs/2406.18346)” research, which aims to make models [act in accordance](https://spectrum.ieee.org/the-alignment-problem-openai) with the goals and motivations of their human developers. One example is the technique that was [arguably](https://venturebeat.com/ai/how-reinforcement-learning-with-human-feedback-is-unlocking-the-power-of-generative-ai/) responsible for the breakthrough success of [ChatGPT](https://spectrum.ieee.org/tag/chatgpt): [reinforcement learning with human feedback](https://arxiv.org/abs/2203.02155). In this method, an AI model is (figuratively) rewarded for producing responses that get a thumbs-up from human evaluators. Similar approaches could be used to induce AI systems to make more human-like mistakes, particularly by penalizing them more for mistakes that are less intelligible.

When it comes to catching AI mistakes, some of the systems that we use to prevent human mistakes will help. To an extent, forcing LLMs to [double-check](https://arxiv.org/pdf/2308.00436) their own work can help prevent errors. But LLMs can also [confabulate](https://arxiv.org/pdf/2406.02061) seemingly plausible, but truly ridiculous, explanations for their flights from reason.

Other mistake mitigation systems for AI are unlike anything we use for humans. Because machines can’t get fatigued or frustrated in the way that humans do, it can help to ask an LLM the same question repeatedly in slightly different ways and then [synthesize](https://arxiv.org/abs/2210.02441) its multiple responses. Humans won’t put up with that kind of annoying repetition, but machines will.

### Understanding Similarities and Differences

Researchers are still struggling to understand where LLM mistakes diverge from human ones. Some of the weirdness of AI is actually more human-like than it first appears. Small changes to a query to an LLM can result in wildly different responses, a problem known as [prompt sensitivity](https://arxiv.org/pdf/2311.07230). But, as any survey researcher can tell you, humans behave this way, too. The phrasing of a question in an opinion poll can have drastic [impacts](https://psycnet.apa.org/record/1992-97329-001) on the answers.

LLMs also seem to have a bias towards [repeating](http://proceedings.mlr.press/v139/zhao21c/zhao21c.pdf) the words that were most common in their training data; for example, guessing familiar place names like “America” even when asked about more exotic locations. Perhaps this is an example of the human “[availability heuristic](https://arxiv.org/pdf/2305.04400)” manifesting in LLMs, with machines spitting out the first thing that comes to mind rather than reasoning through the question. And like humans, perhaps, some LLMs seem to get [distracted](https://arxiv.org/html/2404.08865v1) in the middle of long documents; they’re better able to remember facts from the beginning and end. There is already progress on improving this error mode, as researchers have found that LLMs trained on [more examples](https://www.anthropic.com/news/claude-2-1-prompting) of retrieving information from long texts seem to do better at retrieving information uniformly.

In some cases, what’s bizarre about LLMs is that they act more like humans than we think they should. For example, some researchers have tested the [hypothesis](https://minimaxir.com/2024/02/chatgpt-tips-analysis/) that LLMs perform better when offered a cash reward or threatened with death. It also turns out that some of the best ways to “[jailbreak](https://www.usenix.org/system/files/sec24fall-prepub-1500-yu-zhiyuan.pdf)” LLMs (getting them to disobey their creators’ explicit instructions) look a lot like the kinds of social engineering tricks that humans use on each other: for example, pretending to be someone else or saying that the request is just a joke. But other effective jailbreaking techniques are things no human would ever fall for. One group [found](https://arxiv.org/abs/2402.11753) that if they used [ASCII art](https://en.wikipedia.org/wiki/ASCII_art) (constructions of symbols that look like words or pictures) to pose dangerous questions, like how to build a bomb, the LLM would answer them willingly.

Humans may occasionally make seemingly random, incomprehensible, and inconsistent mistakes, but such occurrences are rare and often indicative of more serious problems. We also tend not to put people exhibiting these behaviors in decision-making positions. Likewise, we should confine AI decision-making systems to applications that suit their actual abilities—while keeping the potential ramifications of their mistakes firmly in mind.

_This essay was written with Nathan E. Sanders, and originally appeared in [IEEE Spectrum](https://spectrum.ieee.org/ai-mistakes-schneier)._

Tags: [AI](https://www.schneier.com/tag/ai/), [LLM](https://www.schneier.com/tag/llm/)

[Posted on January 21, 2025 at 7:02 AM](https://www.schneier.com/blog/archives/2025/01/ai-mistakes-are-very-different-from-human-mistakes.html) • [5 Comments](https://www.schneier.com/blog/archives/2025/01/ai-mistakes-are-very-different-from-human-mistakes.html#comments)

Sidebar photo of Bruce Schneier by Joe MacInnis.
