Title: Only three kinds of AI products actually work

URL Source: https://www.seangoedecke.com/ai-products/

Markdown Content:
The very first LLM-based product, ChatGPT, was just[1](https://www.seangoedecke.com/ai-products/#fn-1) the ability to talk with the model itself: in other words, a pure chatbot. This is still the most popular LLM product by a large margin.

In fact, given the amount of money that’s been invested in the industry, it’s shocking how many “new AI products” are just chatbots. As far as I can tell, **there are only three types of AI product that currently work**.

### Chatbots

For the first couple of years of the AI boom, all LLM products were chatbots. They were branded in a lot of different ways - maybe the LLM knew about your emails, or a company’s helpdesk articles - but the fundamental _product_ was just the ability to talk in natural language to an LLM.

The problem with chatbots is that **the best chatbot product is the model itself**. Most of the reason users want to talk with an LLM is generic: they want to ask questions, or get advice, or confess their sins, or do any one of a hundred things that have nothing to do with your particular product.

In other words, your users will just use ChatGPT[2](https://www.seangoedecke.com/ai-products/#fn-2). AI labs have two decisive advantages over you: first, they will always have access to the most cutting-edge models before you do; and second, they can develop their chatbot harness simultaneously with the model itself (like how Anthropic specifically trains their models to be used in Claude Code, or OpenAI trains their models to be used in Codex).

#### Explicit roleplay

One way your chatbot product can beat ChatGPT is by doing what OpenAI won’t do: for instance, happily roleplaying an AI boyfriend or generating pornography. There is currently a very lucrative niche of products like this, which typically rely on less-capable but less-restrictive open-source models.

These products have the problems I discussed above. But it doesn’t matter that their chatbots are less capable than ChatGPT or Claude: if you’re in the market for sexually explicit AI roleplay, and ChatGPT and Claude won’t do it, you’re going to take what you can get.

I think there are serious ethical problems with this kind of product. But even practically speaking, this is a segment of the industry likely to be eaten alive by the big AI labs, as they become more comfortable pushing the boundaries of adult content. [Grok Companions](https://tremendous.blog/2025/07/15/grok-companions-elons-ai-girlfriend/) is already going down this pathway, and Sam Altman has [said](https://www.theverge.com/news/799312/openai-chatgpt-erotica-sam-altman-verified-adults) that OpenAI models will be more open to generating adult content in the future.

#### Chatbots with tools

There’s a slight variant on chatbots which gives the model _tools_: so instead of just chatting with your calendar, you can ask the chatbot to book meetings, and so on. This kind of product is usually called an “AI assistant”.

This doesn’t work well because **savvy users can manipulate the chatbot into calling tools**. So you can never give a support chatbot real support powers like “refund this customer”, because the moment you do, thousands of people will immediately find the right way to jailbreak your chatbot into giving them money. You can only give your chatbots tools that the user could do themselves - in which case, your chatbot is competing with the usability of your actual product, and will likely lose.

Why will your chatbot lose? Because **chat is not a good user interface**. Users simply do not want to type out “hey, can you increase the font size for me” when they could simply hit “ctrl-plus” or click a single button[3](https://www.seangoedecke.com/ai-products/#fn-3).

I think this is a hard lesson for engineers to learn. It’s tempting to believe that since chatbots have gotten 100x better, they must now be the best user interface for many tasks. Unfortunately, they started out 200x worse than a regular user interface, so they’re still twice as bad.

### Completion

The second real AI product actually came out before ChatGPT did: GitHub Copilot. The idea behind the original Copilot product (and all its imitators, like Cursor Tab) is that a fast LLM can act as a smart autocomplete. By feeding the model the code you’re typing as you type it, a code editor can suggest autocompletions that actually write the rest of the function (or file) for you.

The genius of this kind of product is that **users never have to talk to the model**. Like I said above, chat is a bad user interface. LLM-generated completions allow users to access the power of AI models without having to change any part of their current workflow: they simply see the kind of autocomplete suggestions their editor was already giving them, but far more powerful.

I’m a little surprised that completions-based products haven’t taken off outside coding (where they immediately generated a multi-billion-dollar market). Google Docs and [Microsoft Word](https://support.microsoft.com/en-us/office/editor-text-predictions-in-word-7afcb4f3-4aa2-443a-9b08-125a5d692576) both have something like this. Why isn’t there more hype around this?

*   Maybe the answer is that the people using this product don’t engage with AI online spaces, and are just quietly using the product?
*   Maybe there’s something about normal professional writing that’s less amenable to autocomplete than code? I doubt that, since so much normal professional writing is being copied out of a ChatGPT window.
*   It could be that code editors already had autocomplete, so users were familiar with it. I bet autocomplete is brand-new and confusing to many Word users.

### Agents

The third real AI product is the coding agent. People have been talking about this for years, but it was only really in 2025 that the technology behind coding agents became feasible (with Claude Sonnet 3.7, and later GPT-5-Codex).

Agents are kind of like chatbots, in that users interact with them by typing natural language text. But they’re unlike chatbots in that **you only have to do that once**: the model takes your initial request and goes away to implement and test it all by itself.

The reason agents work and chatbots-with-tools don’t is the difference between asking an LLM to hit a single button for you and asking the LLM to hit a hundred buttons in a specific order. Even though each individual action would be easier for a human to perform, agentic LLMs are now smart enough to take over the entire process.

Coding agents are a natural fit for AI agents for two reasons:

*   It’s easy to verify changes by running tests or checking if the code compiles
*   AI labs are incentivized to produce effective coding models to accelerate their own work

For my money, the current multi-billion-dollar question is **can AI agents be useful for tasks other than coding?** Bear in mind that Claude Sonnet 3.7[4](https://www.seangoedecke.com/ai-products/#fn-4) was released just under _nine months ago_. In that time, the tech industry has successfully built agentic products about their own work. They’re just starting to build agentic products for other tasks. It remains to be seen how successful that will be, or what those products will look like.

#### Research

There’s another kind of agent that isn’t about coding: the research agent. LLMs are particularly good at tasks like “skim through ten pages of search results” or “keyword search this giant dataset for any information on a particular topic”. I use this functionality a lot for all kinds of things.

There are a few examples of AI products built on this capability, like [Perplexity](https://www.perplexity.ai/). In the big AI labs, this has been absorbed into the chatbot products: OpenAI’s “deep research” went from a separate feature to just what GPT-5-Thinking does automatically, for instance.

I think there’s almost certainly potential here for area-specific research agents (e.g. in medicine or law).

### Feeds

If agents are the most recent successful AI product, AI-generated feeds might be the one just over the horizon. AI labs are currently experimenting with ways of producing infinite feeds of personalized content to their users:

*   Mark Zuckerberg has talked about filling Instagram with auto-generated content
*   OpenAI has recently launched a Sora-based video-gen feed
*   OpenAI has also started pushing users towards “Pulse”, a personalized daily update inside the ChatGPT product
*   xAI is [working on](https://www.testingcatalog.com/grok-will-get-infinite-image-gen-and-video-gen-with-sounds/) putting an infinite image and video feed into Twitter

So far none of these have taken off. But scrolling feeds has become the primary way users interact with technology _in general_, so the potential here is massive. It does not seem unlikely to me at all that in five years time most internet users will spend a big part of their day scrolling an AI-generated feed.

Like a completions-based product, the advantage of a feed is that users don’t have to interact with a chatbot. The inputs to the model come from how the user interacts with the feed (likes, scrolling speed, time spent looking at an item, and so on). Users can experience the benefits of an LLM-generated feed (if any) without having to change their consumption habits at all.

The technology behind current human-generated infinite feeds is already a mature application of state of the art machine learning. When you interact with Twitter or LinkedIn, you’re interacting with a model, except instead of generating text it’s generating lists of other people’s posts. In other words, **feeds already maintain a sophisticated embedding of your personal likes and dislikes**. The step from “use that embedding to surface relevant content” to “use that embedding to _generate_ relevant content” might be very short indeed.

I’m pretty suspicious of AI-generated infinite feeds of generated video, but I do think other kinds of infinite feeds are an under-explored kind of product. In fact, I built a feed-based hobby project of my own, called [Autodeck](https://www.autodeck.pro/)[5](https://www.seangoedecke.com/ai-products/#fn-5). The idea was to use an AI-generated feed to generate spaced repetition cards for learning. It works pretty well! It still gets a reasonable amount of use from people who’ve found it via my blog (also, from myself and my partner).

### Games

One other kind of AI-generated product that people have been talking about for years is the AI-based video game. The most speculative efforts in this direction have been full world simulations like DeepMind’s [Genie](https://deepmind.google/blog/genie-3-a-new-frontier-for-world-models/), but people have also explored using AI to generate a subset of game content, such as pure-text games like [AI Dungeon](https://aidungeon.com/) or this [Skyrim mod](https://www.nexusmods.com/skyrimspecialedition/mods/98631) which adds AI-generated dialogue. Many more game developers have incorporated AI art or [audio](https://www.polygon.com/arc-raiders-ai-voices-the-finals-embark-studios/) assets into their games.

Could there be a transformative product that incorporates LLMs into video games? I don’t think ARC Raiders counts as an “AI product” just because it uses AI voice lines, and the more ambitious projects haven’t yet really taken off. Why not?

One reason could be that **games just take a really long time to develop**. When _Stardew Valley_ took the world by storm in 2016, I expected a flood of copycat cozy pixel-art farming games, but that only really started happening in 2018 and 2019. That’s how long it takes to make a game! So even if someone has a really good idea for an LLM-based video game, we’re probably still a year or two out from it being released.

Another reason is that **many gamers really don’t like AI**. Including generative AI in your game is a guaranteed controversy (though it doesn’t seem to be fatal, as the success of ARC Raiders shows). I wouldn’t be surprised if some game developers simply don’t think it’s worth the risk to try an AI-based game idea[6](https://www.seangoedecke.com/ai-products/#fn-6).

A third reason could be that **generated content is just not a good fit for gaming**. Certainly ChatGPT-like dialogue sticks out like a sore thumb in most video games. AI chatbots are also pretty bad at _challenging_ the user: their post-training is all working to make them try to satisfy the user immediately[7](https://www.seangoedecke.com/ai-products/#fn-7). Still, I don’t think this is an insurmountable technical problem. You could simply post-train a language model in a different direction (though perhaps the necessary resources for that haven’t yet been made available to gaming companies).

### Summary

By my count, there are three successful types of language model product:

*   Chatbots like ChatGPT, which are used by hundreds of millions of people for a huge variety of tasks
*   Completions coding products like Copilot or Cursor Tab, which are very niche but easy to get immediate value from
*   Agentic products like Claude Code, Codex, Cursor, and Copilot Agent mode, which have only really started working in the last six months

On top of that, there are two kinds of LLM-based product that don’t work yet but may soon:

*   LLM-generated feeds
*   Video games that are based on AI-generated content

Almost all AI products are just chatbots (e.g. AI-powered customer support). These suffer from having to compete with ChatGPT, which is a superior general product, and not being able to use powerful tools, because users will be able to easily jailbreak the model.

Agentic products are new, and have been wildly successful _for coding_. It remains to be seen what they’ll look like in other domains, but we’ll almost certainly see domain-specific research agents in fields like law. Research agents in coding have seen some success as well (e.g. code review or automated security scanning products).

Infinite AI-generated feeds haven’t yet been successful, but hundreds of millions of dollars are currently being poured into them. Will OpenAI’s Sora be a real competitor to Twitter or Instagram, or will those companies release their own AI-generated feed product?

AI-generated games sound like they could be a good idea, but there’s still no clear working strategy for how to incorporate LLMs into a video game. Pure world models - where the entire game is generated frame-by-frame - are cool demos but a long way from being products.

One other thing I haven’t mentioned is image generation. Is this part of a chatbot product, or a tool in itself? Frankly, I think AI image generation is still more of a toy than a product, but it’s certainly seeing a ton of use. There’s probably some fertile ground for products here, if they can successfully differentiate themselves from the built-in image generation in ChatGPT.

In general, it feels like the early days of the internet. LLMs have so much potential, but we’re still mostly building copies of the same thing. There have to be some really simple product ideas that we’ll look back on and think “that’s so obvious, I wonder why they didn’t do it immediately”.

edit: This post got quite a few comments on [Hacker News](https://news.ycombinator.com/item?id=45946498). Some commenters think [my categories are too broad](https://news.ycombinator.com/item?id=45946878), which is a fair criticism: like saying that there are only two “electricity products”, ones which turn a motor and ones which heat up a wire.

Other commenters argue that summarization, easy translation, and transcription are products I’ve missed. I disagree: have you yourself purchased some piece of LLM-driven summarization, translation or transcription software? Probably not - you just use a chatbot directly, right? I thus think of those as _features_ of the chatbot product, not products in their own right.

One commenter [points out](https://news.ycombinator.com/item?id=45946957) that there may be a bunch of zero-hype products bubbling away under the radar. Fair enough! I don’t know what I don’t know.

* * *

1.   Of course, “just” here covers a raft of progress in training stronger models, and real innovations around RLHF, which made it possible to talk with pure LLMs at all.

[↩](https://www.seangoedecke.com/ai-products/#fnref-1)
2.   This is a big reason why [most AI enterprise projects fail](https://www.seangoedecke.com/why-do-ai-enterprise-projects-fail). Anecdotally, I have heard a lot of frustration with bespoke enterprise chatbots. People just want to use ChatGPT!

[↩](https://www.seangoedecke.com/ai-products/#fnref-2)
3.   If you’re not convinced, take any device you’re comfortable using (say, your phone, your car, your microwave) and imagine having to type out every command. Maybe really good speech recognition will fix this, but I doubt it.

[↩](https://www.seangoedecke.com/ai-products/#fnref-3)
4.   I originally had this incorrectly as “3.5 Sonnet”. Thanks to a reader for the correction.

[↩](https://www.seangoedecke.com/ai-products/#fnref-4)
5.   I wrote about it [here](https://www.seangoedecke.com/autodeck) and it’s linked in the topbar.

[↩](https://www.seangoedecke.com/ai-products/#fnref-5)
6.   Though this could be counterbalanced by what I’m sure is a strong push from executives to get in on the action and “build something with AI”.

[↩](https://www.seangoedecke.com/ai-products/#fnref-6)
7.   If you’ve ever tried to ask ChatGPT to DM for you, you’ll have experienced this first-hand: the model will immediately try and show you something cool, skipping over the necessary dullness that builds tension and lends verisimilitude.

[↩](https://www.seangoedecke.com/ai-products/#fnref-7)

If you liked this post, consider[subscribing](https://buttondown.com/seangoedecke)to email updates about my new posts, or[sharing it on Hacker News](https://news.ycombinator.com/submitlink?u=https://www.seangoedecke.com/ai-products/&t=Only%20three%20kinds%20of%20AI%20products%20actually%20work). Here's a preview of a related post that shares tags with this one.