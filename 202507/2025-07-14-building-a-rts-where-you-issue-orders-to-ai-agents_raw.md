Title: Building a RTS where you issue orders to AI agents

URL Source: https://www.seangoedecke.com/wargame-agents/

Markdown Content:
I’ve always been interested by the third-act turn in Ender’s Game where the child strategists switch from directly controlling units to giving higher-level strategic orders. The communication problem just seems fascinating: you gain a huge amount of flexibility, but you have to adapt to decisions made on the ground by your subordinates. For similar reasons, I’ve been interested in how giving orders [worked](https://acoup.blog/2022/06/03/collections-total-generalship-commanding-pre-modern-armies-part-ii-commands/) in pre-modern battles where sending messages was very difficult.

When I read about [Cataphract](https://news.ycombinator.com/item?id=44320832), a play-by-mail role playing game that leaned into this idea, I thought about LLMs. Their ability to interpret (or misinterpret) text is brand-new. Could it be possible to build a new genre of strategy game where you have no direct control over units, but can only issue text-based orders to individual generals?

### Prototyping the game

Over the weekend, I built [sgoedecke/generals](https://github.com/sgoedecke/generals), a rough draft of this kind of idea. I want to write up what I learned as I was building it, and what decisions felt successful or unsuccessful.

I tried a couple of prototypes before settling on this one - it’s in the `generals3` folder in my filesystem. The main mistake I made when building the first two was trying to build a normal strategy game and then bolting LLMs onto the side. The LLM part was fine, but it was awkward to ad-hoc implement “I want to give an order that might take several turns to complete” on top of an existing turn-based system. **The ability to give standing orders is a complex enough feature that it needs to be part of the design from the ground-up.**

What I ended up doing was beginning with a pure order-based game API. There were two endpoints: `/state`, which returned a JSON blob of the full game state, and `/order`, which allowed users to give two kinds of simple order to units. You can tell a unit to move a certain amount of tiles in a direction (e.g. “3 north” means it’ll try and move north for the next three turns), or to move towards a particular point (e.g. “move to 3,1” means it’ll spend subsequent turns attempting to move to that coordinate). The key idea here is that **the game proceeds on its own one-turn-per-second cycle, but orders can arrive and be enqueued at any time**.

### What I learned about building for AI agents

The general AI-agent principle here is that you should **design an AI-friendly API before you actually hook up any AI work**. What makes for an AI-friendly API? For getting information, it means an endpoint that outputs something that you can put into your AI agent system prompt - so it has to contain the entire state of the world that’s visible to the agent. For taking actions, it means two things:

1.   Having a simple interface that matches how AI agents work (i.e. a small set of powerful tools instead of a ton of niche tools)
2.   Making your action-taking API handle delayed or infrequent orders, since a LLM can take a second or two to generate its response

An `/order` interface that let you move a unit one square in one direction every time might work well for a human player, who can cheerfully issue several instructions per second. But if a LLM is issuing several instructions per second, that’s going to be slow and consume a lot of tokens. A smart LLM won’t be able to keep up the pace (or will be prohibitively expensive).

The natural way to use a LLM for high-frequency actions is to let it make occasional high-level decisions, and then to have non-LLM specialized code execute those decisions turn-by-turn. This is very roughly what AI-powered robotics does, by having a powerful LLM that decides what to say and do, but delegating all individual servo control to a much faster and smaller non-language model. The actual servo control model has to consume input and emit output many times per-second, while the LLM only has to decide anything every couple of seconds.

Even more loosely, this is kind of how humans work. The process by which we decide “I should get up and make a cup of tea”, or “I should go over there” is slower and more reflective than the process that constantly shifts our weight so that we don’t fall over when walking, or that decides exactly how hard to squeeze when we pick up a teabag.

All of this is to say that when you’re building for AI agents, you should allow the LLM to make broad and strategic decisions, and let their individual tools handle the bulk of the mechanical work. For instance, it’s better to give your robot arm a “grab object” tool instead of a set of “move hand”, “close grip”, and “release grip” tools.

### How did it go?

Was the game good? It’s still very rough, but even in its current state I found it pretty fun. The fact that the game proceeds in the background leads to enjoyably frantic situations where you’re typing orders as fast as possible (like “western units, stop and go back to defend the nearest city!”). It was very satisfying to be able to type something like “block the gap to the mountain pass with a unit, while all other units circle around east” and see all the blue units figure it out. When a unit got stuck in the mountains, it made for a fun mode-shift where instead of giving general orders to your army you’re talking one specific unit through getting unstuck (“ok B2, go north a bit and then east two tiles”).

I made a simple non-LLM-powered AI to be the opposite side. Controlling the LLM-powered side was difficult enough that I had to make the non-LLM side pretty dumb. If it made reasonable decisions, it was just too hard to beat.

Part of the problem was that the AI struggled with spatial reasoning. I ran into the same issue in a [previous project](https://github.com/sgoedecke/fish-tank) where I tried to make different LLMs compete against each other in a simple 2D game of “find the fish food”. In both cases, the model struggled with concepts like “surround this point”, “position in between this point and enemy units”, or “go around the left side of the mountain”. Interestingly, it helped a lot when I rendered a simple ASCII grid into the system prompt. I don’t know why a text-based model would have an easier time with a grid than with raw coordinates, but it definitely made things better in my case. It would be interesting to try multimodal input and see if it helps to provide an actual image of the game state.

### Final thoughts

I learned a lot about agents from making this, but honestly my main takeaway was that it was way more fun to frantically type orders than I expected it to be.

I would love to play a realistic RTS where you have limited information and are forced to issue orders via text. It doesn’t seem like it’d be too hard to build (in terms of video games, which are always hard to build). In particular, I think it would be very engaging to play against another human who’s also telling the LLMs what to do. Somebody who’s better at making games than me should make this.

If you liked this post, consider [subscribing](https://buttondown.com/seangoedecke) to email updates about my new posts.
