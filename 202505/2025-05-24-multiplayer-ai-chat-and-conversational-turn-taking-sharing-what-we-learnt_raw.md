Title: Multiplayer AI chat and conversational turn-taking: sharing what we learnt

URL Source: https://interconnected.org/home/2025/05/23/turntaking

Markdown Content:
I subscribe to ChatGPT and I subscribe to Claude and I chat with both AIs a ton – but why can’t I invite a friend into the chatroom with me?

Or multiple chatbots even! One that’s a great coder and another that’s more creative, with identity so I know automatically who is good at what?

The thing is, multiplayer is hard. The tech is solved but the design is still hard.

In a nutshell:

If you’re in a chatroom with >1 AI chatbots and you ask a question, who should reply?

And then, if you respond with a quick follow-up, how does the “system” recognise the conversational rule and have the same bot reply, without another interrupting?

Conversational turn-taking isn’t a problem when I use ChatGPT today: it’s limited to one human user and one AI-powered bot, and the bot always replies whenever the user says something (never ignoring them; never spontaneously speaking up).

But, when we want to go multiplayer, the difficulties compound…

*   multiple bots – how does a bot know when it has something to contribute? How do bots negotiate between one another? Do bots reply to other bots?
*   multiple human users – a bot replying to every message would be noisy, so how does it identify when it’s appropriate to jump in and when it should leave the humans to get on with it?

You can’t leave this to the AI to decide (I’ve tried, it doesn’t work).

To have satisfying, natural chats with multiple bots and human users, we need heuristics for conversational turn-taking.

* * *

### This post is a multiplayer trailhead

Via [Acts Not Facts](https://www.actsnotfacts.com/) I’ve been working with the team at [Glif](https://glif.app/) to explore future products.

[Glif](https://glif.app/) is a low-code platform for creative AI workflows. Like, if you want to make weird medieval memes [there’s a glif for that](https://glif.app/@fab1an/glifs/cm1926mxf0006ekfvp3xr69da).

And one part of what we’ve been experimenting with is chatbots with personality and tools. i.e. they can make things for you and also research on Wikipedia etc.

The _actual_ product is still to come. Let me say, it is _wild._ Friday demos always overrun and I cannot wait for you to see what’s cooking and what you can build with it.

But along the way we had a side-quest into **multiplayer AI chat.**

And I wanted to note down what we learnt here as a trailhead for future work.

Technically the bots are _agents_[which I’ve previously defined as](https://interconnected.org/home/2024/06/07/agenda) LLM-powered software that (a) uses tools, and (b) has autonomy on how to reach its goal and when to halt.

You chat with the bots. In our side-quest, you chat in an environment: a chat is a themeable container that also holds media artifacts (like HTML) and multiple bots and multiple human users.

So there’s a lot you can do with these primitives, but for the sake of this multiplayer scenario, imagine a room called _Infinite Seinfeld_ and it’s populated with bots that are prompted to behave like the main characters, plus a Showrunner bot that gives them a plot.

Then you improv a random show together. (I built this one, it’s super fun.)

Another scenario, a work-based one: imagine you have a multi-user chat (like a Slack channel) with a stenographer for capturing actions, and a researcher bot that can dig around in your company Google Drive, on demand and proactively. Who should speak up when?

Or perhaps you’re in a group WhatsApp with some friends and you invite in one bot for laughs and another to help you find and book restaurants, and it has to speak with the brand voice.

(I found from [my previous work with AI NPC teammates](https://interconnected.org/home/2023/09/01/npcs) that it’s useful to split out functionality into different agents because then you can develop a “theory of mind” about each, and reason about what each one knows and is good at. I discussed this more in my [Thingscon talk last year](https://youtu.be/vDP24ARdGDA?si=moKgQSWKZgqSX8y5&t=1335)_(YouTube, starting at 22:15)._)

The rest of this post is how we made this work.

* * *

### Three approaches that don’t work

If a chatbot isn’t going to reply every single time, how can it decide?

**shouldReply**

I got the multi-user/single-bot scenario working when I was helping out at PartyKit. Here’s what worked:

> we don’t want the AI to reply every time. It’s multi-user chat! The humans should be able to have a conversation without an AI response to every message.
> 
> 
> the best conversational models are expensive. Can we use a cheaper, local model to decide whether to reply, then escalate only if necessary?

So there’s a quick call to an LLM with the context of the chat, before the full LLM call is used to generate a response (or not). I called this pattern shouldReply.

[Here’s the GitHub repo explaining shouldReply.](https://github.com/partykit/templates/blob/main/templates/chat-room/README.md#adding-ai-discrimination-with-multiple-models)

And [here’s the prompt in the code](https://github.com/partykit/templates/blob/2904fa3e88eefc196e6d3ce669ccbfeb13e86243/templates/chat-room/party/server.ts#L114): the bot replies if it being addressed by name.

This should also work in a multi-bot scenario!

It doesn’t.

LLMs aren’t smart enough yet.

The failure modes:

*   all the bots replying at once and talking over each other
*   no allowance for personality: a chatty researcher should be more likely to reply than a helpful but taciturn stenographer
*   no coordination: bots talk over each other
*   generally, the conversation feels unnatural: bots don’t accept follow-ups, interrupt each other too much or not all, and so on.

So we need a more nuanced shouldReply discriminator for multi-bot.

**Could a centralised decider help?**

One approach is to take the shouldReply approach and run it once for an entire chatroom, on behalf of all the bots, and figure out who should be nominated to reply.

It works… but it’s like having a strict meeting chair instead of a real conversation? It feels weird.

And besides, architecturally this approach doesn’t scale.

When different bots having different personalities (some chatty, some shy) the discriminator needs to see their prompts. But how can this work when multiple bots are “dialling in” from different places, one hosted on Glif, another hosted on Cloudflare, yet another somewhere else, each with their own potentially secret internal logic?

In Glif parlance, bot “personality” is a prompt to the agent for how to achieve its goals – not always the same as the stated user goals. It may include detailed step-by-step instructions, a list of information to gather first, strategies, confidential background information… and, of course, the traditional personality qualities of tone of voice and a simulated emotional state. “Personality” is what makes Claude Sonnet a well-spoken informative bot and ChatGPT an enthusiastic, engaging conversation partner. It matters, and every bot is different.

No, bots need to decide for themselves whether to reply.

**How does conversational turn-taking work in the real world?**

Let’s draw inspiration from the real world.

IRL multi-party conversations are complicated!

It’s great at this point to be able to go to the social science literature…

I found [A Simplest Systematics for the Organization of Turn-Taking for Conversation](https://www.jstor.org/stable/412243) (Sacks, Schegloff and Jefferson, 1974) super illuminating for unpacking what conversation _involves_ (JSTOR is one of the few journal repositories I can access.)

Particularly the overview of turn allocation rules: “current selects next” is the default group of strategies, then “self-selection” strategies come into play if they don’t apply.

That paper also opens up body language, which is so key: the paper I would love to read, ~~but can’t access in full~~, is [Some signals and rules for taking speaking turns in conversations](https://psycnet.apa.org/record/1973-00754-001) (Duncan, 1972). _(Update: a couple people shared the PDF with me overnight - thank you! - and it looks like everything I hoped.)_

Everything from intonation to gesture comes into play. Gaze direction is used to select the next speaker; “attempt-suppression” signals come into play too.

Ultimately what this means is we need body language for bots: side-channel communications in chatrooms to negotiate who speaks when.

But we can’t do body language. Not in web chatrooms. Too difficult (for now).

Turn allocation rules, on the other hand, are a handy wedge for thinking about all of this.

* * *

### Breaking down conversational turn-taking to its bare essentials

Fortunately chatrooms are simpler than IRL.

They’re less fluid, for a start. You send a message into a chat and you’re done; there’s no interjecting or both starting to talk at the same time and then one person backing off with a wave of the hand. There is no possibility for non-verbal cues.

In the parlance of the _“Systematics”_ paper, linked above, we can think about “turn-taking units,” which we’ll initially think about as messages; there are transitions, which take place potentially after every message; and there are our turn allocation rules.

So all we really need to do is figure out some good rules to put into shouldReply, and have each bot decide for itself whenever a new message comes through.

What should those rules be?

Well here are the factors we found that each bot needs to consider, in decreasing order of priority, after every single message in the room. (We’ll bring these together into an algorithm later.)

**Who is being addressed?**

Is this bot being addressed, or is any other bot or human being addressed?

From the _“Systematics”_ paper (3.3 Rules):

> If the turn-so-far is so constructed as to involve the use of a ‘current speaker selects next’ technique, then the party so selected has the right and is obliged to take next turn to speak; no others have such rights or obligations, and transfer occurs at that place.

So this is an over-riding factor.

**Is this a follow-up question?**

Consider this conversation when multiple humans and multiple bots are present:

> Human #1: hey B how do I make custard?
> 
> 
> Mr B, a bot: (replies with a custard recipe)
> 
> 
> Human #1: oh I meant mustard

…then how does Mr B know to respond (and other bots know to make space)? The message from Human #1 isn’t clearly a question, nor does it directly address Mr B.

In [Grounding in communication theory](https://en.wikipedia.org/wiki/Grounding_in_communication)_(Wikipedia)_ conversations are seen as exercises in establishing mutual knowledge, mutual beliefs, and mutual assumptions and therefore the turn-taking unit is _not_ single messages.

Instead a unit has this form:

> 1.   New contribution: A partner moves forward with a new idea, and waits to see if their partner expresses confusion.
> 
> 2.   Assertion of acceptance: The partner receiving the information asserts that he understands by smiling, nodding, or verbally confirming the other partner. They may also assert their understanding by remaining silent.
> 
> 3.   Request for clarification: The partner receiving the information asks for clarification

Clark and Schaefer (1989). The clarification step is optional.

So we need all bots to understand whether we’re in a follow-up situation, because it has a big impact on turn-taking.

**Would I be interrupting?**

Before we can move onto self-selection rules, the bot needs to check for any other cues of an established sub-conversation.

We do this without looking at content at all! What matters is simply the participant history of who has spoken recently and in what order.

(The inspiration for looking at participants, not content, comes from [Participation Shifts: Order and Differentiation in Group Conversation](https://www.jstor.org/stable/3598117?seq=1) (Gibson, 2003), but that paper is way more sophisticated than what we’re doing here.)

In our case, we can just feed the list of recent speakers into the large language model and ask it what it thinks should happen next.

**Self-selection**

Those are the self-selection rules out of the way.

Finally a bot can judge for itself whether it has something relevant to say, and _also_ whether it has the kind of personality that would let it interject. Here’s the prompt we use:

> do you have a skill or personality specifically relevant to the most recent message? Also consider whether your personality would want to chime in based on what was said.

We ask the LLM to use a score from 0 to 9.

(A “skill” is something a bot can do, for example looking up an article on Wikipedia. If a user has asked for a particular skill to be used, the bot with that skill should return a score of 9.)

This kind of judgement is where large language models really shine.

* * *

### Enthusiasm: how a bot combines all these factors to decide whether to reply

So, in a multi-user, multi-bot chatroom, every time a message comes through, we have the bot run a quick algorithm to calculate an “Enthusiasm” score:

*   calculate all the necessary information for the turn-taking rules above
*   if this bot is clearly involved in the current part of the conversation, return 9. If someone else is clearly involved instead, return 0
*   otherwise return the self-selection score (how confident this bot is about having something relevant to say).

(There are some other nuances: we don’t want bots to reply to other bots or themselves, for example.)

When all bots in a chatroom have returned a score, we consider only the ones above some threshold (e.g. 5) and then pick the highest one.

This works because:

*   As in _“Systematics,”_ typically only one participant speaks at a time; and
*   Typically, in real-world situations, the quickest person to respond grabs the turn. The enthusiasm score is a proxy for that.

Of course we’re still missing prosody and body language: I’ve run across the term “turn-competitive incoming” which describes how volume and pitch are used to grab the turn, even when starting late. Our bots don’t have volume or pitch, so all of this is such a simplification.

Yet… the result? It’s pretty good. Not perfect, but pretty good!

If you’re on Glif, [you can see the source code of the Enthusiasm workflow here](https://glif.app/@gliffyglif/glifs/cm92gipb30001jp03ayp3j3xg/source), prompts and all.

* * *

### What still needs work?

Working in these multi-user, multi-bot chatrooms, we found a couple areas for future work:

*   **Group norms.** Different chatrooms have different norms and roles. Like, an improv room is open to everyone to speak, but a meeting should be led by humans and participants in a D&D game should always defer to the DM. We have the ability to attach a prompt to a room (remember, rooms are already “containers” with themes and so on) so the bot also takes that into account – but it would be good to have a way to assess norms automatically. (Even ChatGPT chats have “norms”: discursive explorations are very different from direct problem-solving, for example.)
*   **Back-off.** Humans often reply with a sequence of short messages – a bot shouldn’t reply until the sequence is complete. But it’s tricky to tell when this is happening. A simple solution would be to double check if the human has sent a second message after calculating enthusiasm for the first.

More speculatively…

I’d love to think about “minimum viable side-channel” in a multiplayer environment. Given we don’t want to add voice or VR (like, text is great! Let’s still with text!) then could we actually take advantage of something like _timing_ to communicate?

I’m reminded of [Linus’ work on prototyping short message LLMs](https://x.com/thesephist/status/1861298457174004149) (@thesephist on X) which (a) looks like an actual naturalistic WhatsApp conversation even though it’s a human/AI chat, and (b) he suggests:

> Timing is actually a really key part of nonverbal communication in texting - things like how quickly you respond, and double-texting if there’s no response. There’s nothing built into any of the popular models around this so this has to be thought up from the ground up. Even trivial things like “longer texts should take more seconds to arrive” because we want to “simulate” typing on the other end. If it arrives too quickly, it feels unnatural.

So can quick messages understood as “more urgent”? Could we identify the user tapping on a bot’s avatar as “gaze” ([it’s a significant turn-allocation rule](https://www.pnas.org/doi/10.1073/pnas.0903616106))? Or tapped in an agitated fashion as a pointed loop?

And so on. What would feel natural?

* * *

### Wrapping this up for now…

My premise for a long time is that single-human/single-AI should _already_ be thought of as a “multiplayer” situation: an AI app is not a single player situation with a user commanding a web app, but instead two actors sharing an environment.

I mean, this is the [whole schtick of Acts Not Facts](https://www.actsnotfacts.com/), that you have to think of AI and multiplayer simultaneously, using the real world as your design reference.

And, as for a specific approach, yes, large language models would ideally be able to natively tell when it’s their turn in a multiplayer conversation… but they can’t (yet).

So the structured shouldReply/enthusiasm approach is a decent one.

For me it rhymes with [how Hey Siri works on the iPhone](https://interconnected.org/home/2020/05/26/voice) (as previously discussed, 2020):

> iPhone’s “Hey Siri” feature (that readies it to accept a voice instruction, even when the screen is turned off) is a personalised neural network that runs on the motion coprocessor. The motion coprocessor is the tiny, always-on chip that is mainly responsible for movement detection, i.e. step counting.
> 
> 
> If that chip hears you say “Hey Siri”, without hitting the cloud, it then wakes up the main processor and sends the rest of what you say up to the cloud. This is from 2017 by the way, ancient history.

Same same!

* * *

While Glif isn’t pushing forward with multiplayer right this second, I’ve experienced it enough, and hacked on it enough, and thought about it enough to really want it in the world. The potential is so tantalising!

When it’s working well, it’s fun _and_ powerful. Bots with varying personalities riffing off each other gets you to fascinating places so fast. It feels like a technique at least as powerful as - let’s say - chain of thought.

So I’m happy to leave this trailhead here to contribute to the discourse and future work.

There is so much work on AI agents and new chat interfaces this year – my strong hope is to see more multi-bot and multi-user AIUX in the mix, whether at the applied layer or even as a focus in AI research.

This is how we live our lives, after all. We’d be happier and more productive with our computers, I’m sure, if we worked on not only tools for thought but also tools for togetherness, human and AI both.

Thank you to the team, especially [Fabian](https://fabian.ai/), Florian, Andrew and William as we worked on all of this together, and thank you Glif for being willing to share the fruits of this side-quest.
