Title: Mapping the landscape of gen-AI product user experience

URL Source: https://interconnected.org/home/2024/07/19/ai-landscape

Markdown Content:
I talk with a lot of clients and startups about their new generative AI-powered products.

One question is always: how should users use this? Or rather, how _could_ they use this, because the best design patterns haven’t been invented yet? And what we want to do is to look at prior art. We can’t look at existing users because it’s a new product. So what UX challenges can we expect and how have others approached them?

The problem is that there are _so many_ AI products. Everything overlaps and it’s all so noisy – which makes it hard to have a conversation about what kind of product you want to build.

So I’ve been working on mapping the landscape.

As a workshop tool, really.

You’ll recognise the map if you [saw me speak](https://www.actsnotfacts.com/made/speaking) at _Future Frontend_ in Helsinki or _UX London._ I’ve also been testing this landscape recently with clients.

It’s a work in progress, but I think ready to share.

Let me show you…

* * *

### A map of 1st generation AI products (c.2022)

To start, let’s look at the _first generation_ of AI products that came out right after large language models got good enough (i.e. GPT-3) with a public API and sufficient market interest.

So we’re rewinding to around the time of the ChatGPT release in November 2022.

![Image 1](https://interconnected.org/more/2024/07/19/ai-product-map-1st-gen-matt-webb.png)

**What are we looking at?**

A large language model on its own isn’t enough to enable products. We need additional capabilities beyond the core LLM.

Different product archetypes rely on different capabilities to different extents. That gives us a way to tease apart the products into a landscape.

To my mind, there are _three_ capabilities that really matter:

*   **RAG/Large context.** Being able to put more information into the prompt, either using retrieval augmented generation or large context windows. This allows for steering the generation.
*   **Structured generation.** When you can reliably output text as a specific format such as JSON, this enables interop and embedded AI, eventually leading to agents.
*   **Real-time.** Faster means interactive. Computers went through the same threshold once upon a time, going from batch processing to GUIs.

_These aren’t purely technical capabilities. Sure, there’s an element of tuning the models for reliability in various ways. But mainly it’s know-how and software frameworks. RAG was invented in 2020; the ReAct paper (which built on chain-of-thought and led to agents) was published only in October 2022. It takes time for ideas to propagate._

I’ve used these capabilities as axes on a ternary diagram ([I love a good triangle diagram](https://interconnected.org/home/2024/01/05/triangles)).

Now we can plot the original, common gen-AI use cases… what product experiences do these capabilities allow?

*   Reliable large context windows led to products for automating copy and visual assets
*   Combine context and some structure: we’ve got semantic search
*   Combine context and real-time: there’s the “talk to a PDF” archetype, we see a lot of those
*   Structured generation opened up data extraction from unstructured data, like web scraping. It was a huge acceleration; [here’s me from Feb 2023](https://interconnected.org/home/2023/02/07/braggoscope).
*   Pure real-time: we’ve got chat.

**What this map is not** is a prescriptive chart of all possible products. Rather, it’s a way of mapping what we already see emerging, as a way to orient and perhaps inspire thought.

I’m not thinking about games, and I’m not looking (much) at what’s happening in the AIUX prototyping space: I’m looking at where there’s a fit between product and market need.

So this is a map specifically about products and user experience. I don’t think there would be a 1:1 correspondance if we looking at underlying software frameworks, for example.

* * *

### Today’s gen-AI product landscape

As products lean more or less on different capabilities, I think we see four broad areas of user experience.

![Image 2](https://interconnected.org/more/2024/07/19/ai-product-map-groups-matt-webb.png)

Users relate to the AI in different ways:

*   **Tools.** Users control AI to generate something.
*   **Copilots.** The AI works alongside the user in an app in multiple ways.
*   **Agents.** The AI has some autonomy over how it approaches a task.
*   **Chat.** The user talks to the AI as a peer in real-time.

(Note that because I’m mapping out user experience, these are all to do with collaboration.)

Now let’s break this down.

![Image 3](https://interconnected.org/more/2024/07/19/ai-product-map-archetypes-matt-webb.png)

I’ll give some examples to bring these archetypes to life.

**Tools:**

*   There are generative tools like [InteriorAI](https://interiorai.com/) though quickly we see a cluster of workflow products like [Jasper](https://www.jasper.ai/) being used for, say, marketing copy. The watchword here is _dependibility_ and the products need non-AI features like team collaboration to succeed.
*   Get more real-time and the tools become more about individual use and move inline: some of [Notion’s AI tools](https://www.notion.so/product/ai) and [Granola](https://www.granola.so/) are both here, in different ways.
*   Highly real-time tools feel more like sculpting and are great for creative work. See [Adobe Generative Fill](https://www.adobe.com/products/photoshop/generative-fill.html) and [tldraw’s Make Real](https://tldraw.substack.com/p/make-real-the-story-so-far) (the real breakthrough is the iteration). What will matter here is what high-level tools are designed; what’s the AI equivalent of the Photoshop palette?

**Copilots:**

Here we have apps that would work just as well without any AI involved, usually for working on a distinct document type.

[GitHub Copilot](https://github.com/features/copilot/) is the breakthrough copilot product. Also see [Sudowrite](https://www.sudowrite.com/) which has multiple ways to collaborate with you when you’re writing prose fiction.

**Agents:**

A broad church!

Pure structured generation gives you data extraction from fuzzy data, like web scraping or looking at PDFs. But then you have function calling (tool use) and agents…

*   Small agents can be highly reliable and work more like tools, such as [micro-agent](https://www.builder.io/blog/micro-agent) for writing code.
*   Give contained agents more access to context - and integrations - and the product archetype is that they’re presented as virtual employees, like [Lindy](https://www.lindy.ai/). End-user programmability is fascinating here. Look at how Lindy allows for a Zendesk support bot to be programmed in natural language: If the customer seems very angry, just escalate to me.
*   Move in the real-time direction: agents become UI. This is how [new Siri in Apple Intelligence is presented](https://interconnected.org/home/2024/06/11/siri) (see [Lares](https://interconnected.org/more/2024/lares/), my smart home assistant prototype, for another example). You aren’t going to chat with these AIs, they’re super smart button pushers.
*   Even more in that direction, we get malleable interfaces. [LangView](https://github.com/mozilla/langview) ([video](https://x.com/rupertmanfredi/status/1653780093712633859)) is a good example in prototype form; [WebSim](https://websim.ai/) is the same as an open world code sandbox; [Claude Artifacts](https://www.anthropic.com/news/claude-3-5-sonnet) brings micro-apps to regular users.

**Chat:**

*   Purely reliant on the real-time capability is chat. The product archetype that is working here is character chat like [character.ai](https://character.ai/) – easy to dismiss as “virtual girlfriends,” it’s incredibly popular.
*   Assistants: I make a distinction between “agents” (can use tools) and “assistants” (tools plus it presents itself as a general purpose helper). [ChatGPT](https://chatgpt.com/) is an assistant, as is [Google Gemini](https://gemini.google.com/). I’d probably also put [Perplexity](https://www.perplexity.ai/) somewhere around here. They all want to be the user’s point of first intent, competing with traditional search engines.
*   Overlapping with copilots now, and highly real-time: NPCs (non-player characters), when the AI acts like a human user. See [AI Sidekicks from Miro](https://miro.com/ai/), just released, and [my own NPC work](https://interconnected.org/home/2023/09/01/npcs) from last year.

(I have a ton of examples in my notes that I use as references.)

* * *

### What do we learn?

Looking at this landscape, I’m able to see different UX challenges:

*   With generative tools, it’s about reliability and connecting to existing workflows. Live tools are about having the right high-level “brushes,”” being able to explore latent space, and finding the balance between steering and helpful hallucination.
*   With copilots, it’s about integrating the AI into apps that already work, acknowledging the different phases of work. Also helping the user make use of all the functionality… which might mean clear names for things in menus, or it might mean ways for the AI to be proactive.
*   Agents are about interacting with long-running processes: directing them, having visibility over them, correcting them, and trusting them.
*   Chat has an affordances problem. [As Simon Willison says](https://simonwillison.net/2024/Jun/27/ai-worlds-fair/), tools like ChatGPT reward power users.

The affordances problem is more general, of course. I liked [Willison’s analogy here](https://x.com/simonw/status/1799455534506283191):

> It’s like Excel: getting started with it is easy enough, but truly understanding it’s strengths and weaknesses and how to most effectively apply it takes years of accumulated experience.

Which is not necessarily the worst thing in the world! But just as there are startups which are essentially an Excel sheet with a good UI and a bunch of integration and workflow, and that’s how value is unlocked, because of the Excel affordances problem, we may see a proliferation of AI products that perform very similar functions only in different contexts.

* * *

### How am I using this map?

I’ve been using this map to help think around various AI products and how we might interact with them.

One process to do that is:

*   What kind of product are we making? Locate it on the landscape
*   See what others products in this area are doing.

That is, it’s a way of focusing a collection of references in order to have a productive conversation.

But equally another process is:

*   Think about what we’re trying to achieve
*   Now imagine it as a tool, now a live tool, now a copilot, now an agent…

Generative!

It doesn’t help so much for inventing brand new ways of interacting. That’s why I hang out with and pay a ton of attention to the amazing and vibrant [London coding scene](https://www.todepond.com/wikiblogarden/london/). And that’s why I believe in [acts not facts](https://www.actsnotfacts.com/) and rolling my sleeves up.

So it’s not a tool that gives me _answers,_ it’s not that kind of map.

But it helps me communicate, and it’s a decent lens, and it’s a helpful framework in a workshop context.

Scaffolding for the imagination.
