Title: What I learned building an AI-driven spaced repetition app

URL Source: https://www.seangoedecke.com/autodeck/

Markdown Content:
I spent the last couple of weeks building an AI-driven [spaced repetition](https://en.wikipedia.org/wiki/Spaced_repetition) app. You can try it out [here](https://www.autodeck.pro/).

### Spaced repetition

Like many software engineering types who were teenagers in the early 2000s[1](https://www.seangoedecke.com/autodeck/#fn-1), I’ve been interested in this for a long time. The main reason is that, unlike many other learning approaches, spaced repetition _works_. If you want to learn something, study it now, then study it an hour later, then a day later, then a week later, and so on. You don’t have to spend much time overall, as long as you’re consistent about coming back to it. Eventually you only need to refresh your memory every few years in order to maintain a solid working knowledge of the topic.

Spaced repetition learning happens more or less automatically as part of a software engineering job. Specific engineering skills will come up every so often (for instance, using `/proc/net` to inspect open network sockets, or the proper regex syntax for backtracking). If they come up often enough, you’ll internalize them.

It’s more difficult to use spaced repetition to deliberately learn new things. Even if you’re using a spaced repetition tool like [Anki](https://apps.ankiweb.net/), you have to either write your own deck of flashcards (which requires precisely the kind of expertise you don’t have yet), or search for an existing one that exactly matches the area you’re trying to learn[2](https://www.seangoedecke.com/autodeck/#fn-2).

### Doing spaced repetition with LLMs

One way I learn new things is from LLMs. I wrote about this in [_How I use LLMs to learn new subjects_](https://www.seangoedecke.com/learning-from-llms), but the gist is that I ask a ton of follow-up questions about a question I have. The best part about this approach is that it requires zero setup cost: if at any moment I want to learn more about something, I can type a question out and rapidly dig in to something I didn’t already know.

What if you could use LLMs to make spaced repetition easier? Specifically, what if you could ask a LLM to give you an infinite feed of spaced repetition flashcards, adjusting the difficulty based on your responses? That’s the idea behind [AutoDeck](https://www.autodeck.pro/). You give it a topic and it gives you infinite flashcards about that topic. If it’s pitched too easy (e.g. you keep saying “I know”) or too hard, it’ll automatically change the difficulty.

### AI apps without a chat interface

The thing I liked most about building AutoDeck is that it’s an AI-driven app where the interface _isn’t chat_. I think that’s really cool - almost every kind of killer AI app presents a chat interface. To use Claude Code, you chat with an agent. The various data analysis tools are typically in a “chat with your data” mode. To use ChatGPT, you obviously chat with it. That makes sense, since (a) the most unusual thing about LLMs is that you can talk with them, and (b) most AI apps let the user take a huge variety of possible actions, for which the only possible interface is some kind of chat.

The problem with chat is that it demands a lot of the user. That’s why most “normal” apps have the user click buttons instead of type out sentences, and that’s why [many](https://blog.logrocket.com/beyond-chat-rethinking-how-we-use-llms/)[engineering](https://www.sanity.io/blog/the-future-beyond-ai-chat-bots)[and](https://artium.ai/insights/beyond-chat-how-ai-is-transforming-ui-design-patterns)[design](https://elizlaraki.substack.com/p/beyond-the-chat-box-ais-interface)[blogs](https://reconfigured.io/blog/beyond-the-chat-box-future-ai-interfaces-marko-jevremovic) have been writing about how to build AI apps that aren’t chat-based. Still, it’s easier said than done.

I think spaced repetition flashcards are a good use-case for AI. Generating them for any topic is something that would be impossible without LLMs, so it’s a compelling idea. But you don’t have to interact with them via text (beyond typing out what topic you want at the outset).

### Building infinite feeds with AI

How do you use AI to generate an infinite feed of content? I tried a bunch of different approaches here. The two main problems here are _speed_ and _consistency_.

Speed is difficult because AI generation can be pretty slow: counting the time-to-first-token, it’s a few hundred ms, even for quick models. If you’re generating each flashcard with a single request, a user who’s familiar with the subject matter can click through flashcards faster than the AI can generate them. Batching up flashcard generation is quicker (because you only wait for time-to-first-token once) but it forces the user to wait much longer before they see their first card.

What if you generate flashcards in parallel? That has two problems of its own. First, you’re still waiting for the time-to-first-token on every request, so throughput is still much slower than the batched approach. Second, it’s very easy to generate duplicate cards that way. Even with a high temperature, if you ask the same model the same question with the same prompt, you’re likely to get similar answers. The parallel-generation flashcard feed was thus pretty repetitive: if you wanted to learn about French history, you’d get “what year was the Bastille stormed” right next to “in what year was the storming of the Bastille”, and so on.

The solution I landed on was **batching the generation, but saving each card as it comes in**. In other words, I asked the model to generate ten cards, but instead of waiting for the entire response to be over before I saved the data, I made each card available to the client as soon as it was generated. This was trickier than it sounds for a few reasons.

First, it means you can’t use JSON [structured outputs](https://platform.openai.com/docs/guides/structured-outputs). Structured outputs are great for ensuring you get a response that your code can parse, but you can’t (easily) parse chunks of JSON mid-stream. You have to wait for the entire output before it’s valid JSON, because you need the closing `}` or `]` characters[3](https://www.seangoedecke.com/autodeck/#fn-3). Instead, I asked the model to respond in XML `<card></card>` chunks, which could be easily parsed as they came in.

Second, it meant I couldn’t simply have the client request a card and get a card back. The code that generated cards had to be able to run in the background without blocking the client, which forced the client to periodically check for available cards.

### Building with AI agents

I built most of AutoDeck with OpenAI’s Codex. It was pretty good! I had to intervene in maybe one change out of three, and I only had to _seriously_ intervene (i.e. completely change the approach) in one change out of ten. Some examples of where I had to intervene:

*   Codex wanted to build a background job system with job IDs, polling and so on, which I thought was overkill
*   Codex didn’t realize that the Stripe payment link wasn’t including metadata because of how we were encoding the name, so it went off and tried to build a much more involved Stripe Connect integration instead
*   Codex really wanted to track cards by index instead of by card ID, which caused a few annoying re-rendering bugs before I caught it

I tried Claude Code at various parts of the process and honestly found it underwhelming. It took longer to make each change and in general required more intervention, which meant I was less comfortable queueing up changes. This is a pretty big win for OpenAI - until very recently, Claude Code has been much better than Codex in my experience.

I cannot imagine trying to build even a relatively simple app like this without being a competent software engineer already. Codex saved me a lot of time and effort, but it made a lot of bad decisions that I had to intervene. It wasn’t able to fix every bug I encountered. At this point, I don’t think we’re in the golden age of vibe coding. You still need to know what you’re doing to actually _ship_ an app with one of these tools.

### The economics of AI side projects

One interesting thing about building AI projects is that it kind of forces you to charge money. I’ve released previous apps I’ve built for free, because I wanted people to use them and I’m not trying to do the software entepreneur thing. But an app that uses AI costs me money for each user - not a _ton_ of money, but enough that I’m strongly incentivized to charge a small amount for users who want to use the app more than just kicking the tires.

I think this is probably a good thing. Charging money for software is a forcing function for actually making it work. If AI inference was free, I would probably have shipped AutoDeck in a much more half-assed state. Since I’m obliged to charge money for it, I spent more time making sure it was actually useful than I would normally spend on a side project.

### Final thoughts

I had a lot of fun building AutoDeck! It’s still mainly for me, but if you’ve read this far I hope you [try it out](https://www.autodeck.pro/) and see if you like it as well.

I’m still trying to figure out the best model. GPT-5 was actually pretty bad at generating spaced repetition cards: the time-to-first-token was really slow, and the super-concise GPT-5 style made the cards read awkwardly. You don’t need the smartest available model for spaced repetition, just a model with a good grasp of a bunch of textbook and textbook-adjacent facts.

* * *

1.   The surviving ur-text for this is probably Gwern’s 2009 post [_Spaced Repetition for Efficient Learning_](https://gwern.net/spaced-repetition).

[↩](https://www.seangoedecke.com/autodeck/#fnref-1)
2.   Most existing decks are tailored towards students doing particular classes (e.g. anatomy flashcards for med school), not people just trying to learn something new, so they often assume more knowledge than you might have.

[↩](https://www.seangoedecke.com/autodeck/#fnref-2)
3.   I think this is just a lack of maturity in the ecosystem. I would hope that in a year or two you can generate structured XML, JSONL, or other formats that are more easily parseable in chunks. Those formats are just as easy to express as a grammar that the logit sampler can adhere to.

[↩](https://www.seangoedecke.com/autodeck/#fnref-3)