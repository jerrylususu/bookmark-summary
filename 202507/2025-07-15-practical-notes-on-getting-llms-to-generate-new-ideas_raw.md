Title: Practical notes on getting LLMs to generate new ideas

URL Source: https://www.seangoedecke.com/idea-mill/

Markdown Content:
Large language models [struggle](https://www.seangoedecke.com/why-cant-ais-have-new-ideas) to generate new ideas. To AI skeptics, this seems trivially true, since they believe LLMs can only regurgitate content from their training data[1](https://www.seangoedecke.com/idea-mill/#fn-1). To AI believers, this is a puzzle. If a human had the breadth of knowledge of a LLM, wouldn’t they be able to synthesize it and come up with ideas nobody else has had? It may be a consequence of a [training process](https://x.com/VictorTaelin/status/1942409340461183236) that forces LLMs to generate existing text word-for-word. My own view is that it’s a lack of “scaffolding”.

LLMs can’t do much by themselves. To do most important work, they need to be embedded in a computer program that feeds useful data into their inputs and takes action based on their outputs. ChatGPT’s memory is an example of scaffolding that lets a LLM remember facts about who they’re talking to. GitHub Copilot is an example of scaffolding that lets a LLM make changes in your codebase. The story of AI engineering is in part the story of discovering which kinds of scaffolding work the best[2](https://www.seangoedecke.com/idea-mill/#fn-2).

I keep coming back to this question: **how can we scaffold a LLM to come up with brand new ideas?**

Gwern recently [posted](https://gwern.net/ai-daydreaming) about a “day-dreaming loop”, where the model is prompted to retrieve two random facts, think about if there’s a relationship between them, and if so, save that interesting relationship as a new fact. I think this is a good idea. In fact, I think it’s such a good idea that I have been [trying to build it](https://github.com/sgoedecke/idea-mill) for some time! I want to spend the rest of this post sharing what lessons I’ve learned.

**It is not easy to get models to draw _concrete_ connections between random ideas.** The naive approach of “here is idea A and B, what connections can you draw?” is not very good. The models I tried (o3, GPT-4.1, DeepSeek-V3, Claude Sonnet 4, Claude Opus 4) all love to draw vague, hand-wavy connections. For instance, they might connect ideas about mycelial networks and touch-screens by suggesting “touch screen interfaces that leverage the networked nature of mycelium”, with no (or very bad) ideas about what that would actually look like. For my project, I ended up (a) restricting the types of ideas to _mechanisms_, and (b) giving the system a specific problem to think about. Both of these seemed to help avoid this kind of over-vagueness.

**You have to be able to judge the quality of the ideas yourself.** When I began working on this project, my first draft just generated random ideas. I often struggled to tell whether an idea was good or not, because I had no familiarity with the subject matter. It’s easy to be fooled about ideas in domains that aren’t your domain. When I changed the system to focus on a specific problem, and made that specific problem something I knew a lot about, it suddenly became obvious when the system was producing valuable ideas.

**Priming the context with “creative” content doesn’t seem to work.** My first big idea here was to pack the context with snippets of poetry, prose, and facts - like how a human might be half-thinking about several things at once - and then ask the model to come up with new ideas. But the models I tried did not seem easy to influence in this way. They responded in the same way whether I had things in the context or not. I think it’s the “assistant” post-training being too successful - the model ignores “irrelevant” preamble and just answers the question. This could definitely be a prompting issue. I still like this idea and would like it to work. But I ended up abandoning it, at least for now.

**It’s tricky to get models to generate random non-new ideas.** Gwern’s day-dreaming loop requires getting the model to come up with the ideas that it then combines. But I found this surprisingly hard. A single “tell me a concrete fact” prompt gets you a small set of facts. I couldn’t find a prompt that would reliably pull a random piece of knowledge from the model (in other words, a prompt that could be run over and over in the loop to generate new ideas from). I ended up manually prompting Claude Opus to “tell me twenty facts about [discipline]” a bunch of times and then stitching them together in a yml file.

**It kind of works!** My approach is pretty half-assed. But even so, it did generate a few genuinely novel ideas that I hadn’t thought of and that seemed promising. I think there’s something here. If this could be made ~30% better than my prototype, I think it’s a tool that I’d be willing to pay for.

My project is here, if anybody wants to hack on it or build their own: [https://github.com/sgoedecke/idea-mill](https://github.com/sgoedecke/idea-mill).

* * *

1.   I won’t talk about this point any further in this post, but I think it’s obviously incorrect. LLMs can generate trivial new content (e.g. “write a story about a [noun] meeting a [noun]” for two unlikely nouns). Of course, the AI skeptic will say that this is still regurgitation, because the core ideas are still drawn from the training data, just reshuffled. But that’s a much weaker sense of “regurgitation”. At some point it starts to look a lot like the LLM actually has a world model.

[↩](https://www.seangoedecke.com/idea-mill/#fnref-1)
2.   In practice, there’s a symbiotic relationship between scaffolding and raw model capability. Better models can use scaffolding more effectively (like how Codex could generate much better Copilot completions than GPT-3). And sometimes scaffolding is ‘trained into’ the model, like how newer Claude models are trained to use the Claude Code tools.

[↩](https://www.seangoedecke.com/idea-mill/#fnref-2)

If you liked this post, consider [subscribing](https://buttondown.com/seangoedecke) to email updates about my new posts.

July 15, 2025│ Tags: [ai](https://www.seangoedecke.com/tags/ai/)

* * *
