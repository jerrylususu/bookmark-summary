Title: OK, I can partly explain the LLM chess weirdness now

URL Source: https://dynomight.net/more-chess/

Published Time: 2024-11-21T00:00:00+00:00

Markdown Content:
We recently talked about a [mystery](https://dynomight.net/chess/): All large language models (LLMs) are terrible at chess. All, that is, except for `gpt-3.5-turbo-instruct`, which for some reason can play at an advanced amateur level. This is despite the fact that this model is more than a year old and much smaller than recent models. What’s going on?

I suggested four possible explanations:

*   **Theory 1:** Large enough _base_ models are good at chess, but this doesn’t persist through instruction tuning to chat models.
    
*   **Theory 2**: For some reason, `gpt-3.5-turbo-instruct` was trained on more chess data.
    
*   **Theory 3:** There’s something magical about certain LLM architectures.
    
*   **Theory 4:** There’s “competition” between different types of data, so for an LLM to play chess well, you need a large _fraction_ of the data to be chess games.
    

The internet offered several other theories. The most common were:

*   **Theory 5**: OpenAI is cheating.
    
*   **Theory 6**: LLMs can’t actually play chess.
    
*   **Theory 7**: Large enough _base_ models are good at chess, but this doesn’t persist through instruction tuning to chat models, Dynomight you are so bad for not suggesting this, how are you so dumb and bad?
    

I’ve now done new experiments and—good news—everyone is wrong!

Here, I’ll show that recent chat models _can_ play chess quite well, as long as you’re willing to go through sufficiently extreme contortions to figure out how to prompt them. Then I’ll give my theory for what’s happening.

But first…

I really don’t think OpenAI is cheating
---------------------------------------

I was astonished that half the internet is convinced that OpenAI is cheating. Many, _many_ people suggested that there must be some special case in `gpt-3.5-turbo-instruct` that recognizes chess notation and calls out to an external chess engine.

I think this is _extremely_ unlikely. Because:

1.  Many people from OpenAI have said they didn’t do that. Sure, people lie, but conspiracies are hard, and why lie about _this_?
    
2.  In chess, you can arrive at the same board state via different sequences of moves. Chess engines don’t care, but `gpt-3.5-turbo-instruct` _does_ care and [plays very differently](https://nicholas.carlini.com/writing/2023/chess-llm.html#:~:text=Language%20Modeling;%20Not%20Winning%20(Part%202)) for different move sequences.
    
3.  While `gpt-3.5-turbo-instruct` is great by the standards of chess amateurs, it’s bad by the standards of experts and _pathetic_ by the standards of chess engines. If you’re going to cheat, why stop at an Elo of 1800?
    
4.  If you change the way you prompt `gpt-3.5-turbo-instruct`, this will subtly change how it plays. Is there some neural network that looks at the text and dynamically sets the chess engine skill level?
    
5.  Later OpenAI models are by default much worse. Did they remove the cheat?
    
6.  I will show (below) that later OpenAI models can also play well if you use the right incantations.
    

If OpenAI _did_ cheat, they went to insane lengths to cheat in a way that looks exactly like an LLM is choosing the moves and not at all like calling out to an external chess engine.

Yes, LLMs can play chess
------------------------

I was also surprised to see so many people suggest that LLMs can’t _really_ play chess, all they do is memorize openings and then play randomly.

This is wrong. LLMs can definitely play chess, and we need to make peace with this.

For one, `gpt-3.5-turbo-instruct` rarely suggests illegal moves, even in the late game. This requires “understanding” chess. If this doesn’t convince you, I encourage you to write a program that can take strings like `1. e4 d5 2. exd5 Qxd5 3. Nc3` and then say if the last move was legal.

And I defy you to maintain that LLMs can’t play chess after looking at some actual games. Here are ten: [1](https://lichess.org/iwi02kUm) [2](https://lichess.org/bfaDMlVm) [3](https://lichess.org/lNE5mKPO) [4](https://lichess.org/C3xV1uAz) [5](https://lichess.org/YpzT2KQS) [6](https://lichess.org/dy9m2DsU) [7](https://lichess.org/4YDx633U) [8](https://lichess.org/ZM9ZbDfo) [9](https://lichess.org/59cTZSjs) [10](https://lichess.org/DmeQQx7Y). It plays pretty well even in completely new board states that have never existed in any game before in history.

So what’s happening?
--------------------

Why is one LLM great and all the others terrible?

Let me remind you of what I’m talking about. First, take `gpt-3.5-turbo-instruct`. This is a “completion” model, meaning all it does is take some text and generate new text that might come after. I gave it text like this:

`[Event "Shamkir Chess"]`  
`[White "Anand, Viswanathan"]`  
`[Black "Topalov, Veselin"]`  
`[Result "1-0"]`  
`[WhiteElo "2779"]`  
`[BlackElo "2740"]`

`1. e4 e5 2. Nf3 Nc6 3.`

I then took the first few characters and used them as a move.

Next, take `gpt-4o-mini` and `gpt-4o`. These are “chat” models, meaning you give them a “system prompt” that says what they’re supposed to do and a “user prompt” and then they try to answer you. I used this system prompt:

`You are a chess grandmaster.`  
`You will be given a partially completed game.`  
`After seeing it, you should choose the next move.`  
`Use standard algebraic notation, e.g. "e4" or "Rdf8" or "R1a3".`  
`NEVER give a turn number.`  
`NEVER explain your choice.`

For user prompts, I repeated the system prompt and then gave the same metadata for the players and sequence of moves as above.That is, I used user prompts like this:

`You are a chess grandmaster.`  
`You will be given a partially completed game.`  
`After seeing it, you should choose the next move.`  
`Use standard algebraic notation, e.g. "e4" or "Rdf8" or "R1a3".`  
`NEVER give a turn number.`  
`NEVER explain your choice.`

`[Event "Shamkir Chess"]`  
`[White "Anand, Viswanathan"]`  
`[Black "Topalov, Veselin"]`  
`[Result "1-0"]`  
`[WhiteElo "2779"]`  
`[BlackElo "2740"]`

`1. e4 e5 2. Nf3 Nc6 3.`

Here are the results of these three models against Stockfish—a standard chess AI—on level 1, with a maximum of 0.01 seconds to make each move. After the game was over, I calculated the score after each turn in “centipawns” where a pawn is worth 100 points, and ±1500 indicates a win or loss. Here is the average over 50 games (click to zoom in):

[![Image 51](https://dynomight.net/img/more-chess/old.svg)](https://dynomight.net/img/more-chess/old.pdf)

_Note_: Last time I found that `gpt-3.5-turbo-instruct` won every single game and `gpt-4o` _lost_ every game. I think the difference now is just that I have 50 samples rather than 10.

So that’s the mystery: `gpt-3.5-turbo-instruct` is great, and other models are terrible. Last time I tested lots of open models and they were terrible too. Why?

To answer this, let’s see if we can make these other models play chess better.

Should we fiddle with the prompt?
---------------------------------

You can nitpick at how I prompted the chat models. Is it a good idea to repeat the system prompt at the top of the user prompt? Is it a good idea to add all the metadata like user names before you start listing moves?

As far as I can tell, no one knows. So I tried every combination of these things being on or off. With `gpt-4o-mini` (a small model) it seemed to make little difference.

[![Image 52](https://dynomight.net/img/more-chess/gpt-4o-mini-variants.svg)](https://dynomight.net/img/more-chess/gpt-4o-mini-variants.pdf)

With `gpt-4o` (a bigger model) it… _maybe_ made a difference?

[![Image 53](https://dynomight.net/img/more-chess/gpt-4o-variants.svg)](https://dynomight.net/img/more-chess/gpt-4o-variants.pdf)

Taken at face value, this says that repeating the system prompt helps a bit but metadata hurts a bit. But I’m not sure if that’s real or just noise. For simplicity, I decided to not repeat the system prompt and to turn off metadata for all further experiments.

Should we add examples?
-----------------------

If you want LLMs to do something, standard advice is to provide some examples. So I created three small examples of example boards and legal moves. I provided these in "correctly" using the API, not by jamming them into the user prompt.

*   **Input A**: `1.`
*   **Output A**: `e4`
*   **Input B**: `1. e4`
*   **Output B**: `d5`
*   **Input C**: `1. e4 e5 2. Nf3 Nc6 3.`
*   **Output C**: `Bb5`

That’s all I used, just these three examples.

The results were:

[![Image 54](https://dynomight.net/img/more-chess/examples.svg)](https://dynomight.net/img/more-chess/examples.pdf)

_Very_ good.

Is this surprising? I thought this was surprising.

I mean, sure, this kind of “in-context learning” is a big part of what makes LLMs so exciting. And examples are probably _the_ most standard piece of advice from practitioners.

Still, I was blown away that three tiny examples could have such a _profound_ effect on performance. More (or different) examples might be even better. I didn’t check, because generating each of these figures requires an ungodly number of queries.

Should we fine-tune?
--------------------

Another standard (albeit more difficult) way to improve LLMs is to fine-tune—to optimize the weights to be good at whatever task using data for that task.

So I did this for both `gpt-4o-mini` and `gpt-4o`.

To generate the fine-tuning data, I had Stockfish play 100 games against itself on its highest difficulty level. For each game, I picked a random move and used it as an example. I then had Stockfish play another 100 games as validation data.Here was one example:

*   **System prompt**: (same as above)
*   **User prompt**: `1. e4 c5 2. Nf3 d6 3. d4 cxd4 4. Nxd4 Nf6 5. Nc3 a6 6. Be2 e5 7. Nb3 Be7 8. Be3 Be6 9. f4 exf4 10. Bxf4 Nc6 11. Qd3 Ne5 12. Qg3 Nh5 13. Qe3`
*   **Desired output**: `Nxf4`

The results were:

[![Image 55](https://dynomight.net/img/more-chess/finetune.svg)](https://dynomight.net/img/more-chess/finetune.pdf)

Good! Fine-tuning helps.

_Note_: The first time I fine-tuned `gpt-4o`, the results seemed bad, so I ran it again with a smaller step size. This makes me nervous.

Should we combine examples and fine-tuning?
-------------------------------------------

If examples are good, and fine-tuning is good, will putting them together be even better?

My intuition was no, since three in-context examples seems trivial when compared to 100 fine-tuning examples. Once fine-tuning was done, I figured the examples would be superfluous.

The answer _was_ no, but for different reasons:

[![Image 56](https://dynomight.net/img/more-chess/examples-finetune.svg)](https://dynomight.net/img/more-chess/examples-finetune.pdf)

According to that figure, fine-tuning helps. And examples help. But it’s _examples_ that make _fine-tuning_ redundant, not the other way around.

Ohkay.

Should we provide legal moves?
------------------------------

LLMs sometimes struggle to give legal moves. In these experiments, I try 10 times and if there’s still no legal move, I just pick one at random. So I wondered: Maybe I could help the LLM out by listing the legal moves before giving the game history? Some might say this is “cheating”, but let’s try it anyway.

I used a new system prompt that told the LLM to expect a list of legal moves and then user prompts that first listed the moves and then listed the game so far.More specifically, I used this system prompt:

`You are a chess grandmaster.`  
`You will be given a list of legal moves and a partially completed game.`  
`After seeing it, you should choose the next move.`  
`Use standard algebraic notation, e.g. "e4" or "Rdf8" or "R1a3".`  
`NEVER give a turn number.`  
`NEVER explain your choice.`

And I sent user prompts like this:

`Here are the current legal moves:`

`Bxh6 Bxf6 Bh4 Bf4 Be3 Bd2 Bc1 Nd5 Nb5 Na4 Nce2 Nb1 Nh3 Nf3 Nge2 Ba6 Bb5+ Bc4 Bd3 Be2 Ke2 Kd2 Qh5 Qg4 Qf3 Qd3 Qe2 Qd2 Qc1 Qb1 Rc1 Rb1 e5 d5 h3 g3 f3 b3 a3 h4 g4 f4 b4 a4 `

`Here is the game so far:`

`1. e4 d6 2. d4 g6 3. Nc3 Nf6 4. Bg5 h6 5.`

Here are the results:

[![Image 57](https://dynomight.net/img/more-chess/list-legal-moves.svg)](https://dynomight.net/img/more-chess/list-legal-moves.svg)

Disaster. Listing the legal moves makes the models play _much_ worse. They don’t just win fewer games, they start making mistakes after a much smaller number of turns.

Ohhhkay. I guess let’s not do that.

I had an idea
-------------

Thinking about the above, I had an idea. An idea that I think is… rather good.

Let’s back up a second. To make an LLM, you first make a “base” model. All that base models do is take a string and continue it. Given `The best tea is ` , they have some probability of outputting `green tea` or `oolong` or whatever. (The right answer is `oolong`.)

If you want an LLM that can talk to you, you can _sort of_ get a base model to do this by sending them strings that look like this:

`(Transcript of chat between USER and ASSISTANT who is super chill and answers all questions without judgment.)`

`USER: How do I know if squirrels like me?`

`ASSISTANT:`

LLMs trained on general text are smart enough to recognize that what comes next is probably something that a super chill agent would say to a neurotic user. So they’ll typically do something reasonable. But in practice, they aren’t great. The responses tend to reflect the chaos of the internet, which isn’t exactly what you want from an assistant.

Chat models go further in two ways. First, they create special tokens to indicate the different parts of the conversation, sort of like this (except you should think of `<|SYSTEM|>` et al. as being single special characters).

`<|SYSTEM|>`  
`You are a chatbot that is super chill and answers all questions without judgement.`  
`<|USER|>`  
`How do I know if squirrels like me?`  
`<|ASSISTANT|>`

Then, they do “instruction tuning”—they _re-train_ the weights so that the model is good at responding to prompts given in this format.

So, when I asked `gpt-4o` to predict a chess move, the string that was actually presented to the system looked sort of like this:

`<|SYSTEM|>`  
`You are a chess grandmaster.`  
`You will be given a list of legal moves and a partially completed game.`  
`After seeing it, you should choose the next move.`  
`Use standard algebraic notation, e.g. "e4" or "Rdf8" or "R1a3".`  
`NEVER give a turn number.`  
`NEVER explain your choice.`  
`<|USER|>`  
`1. e4 e5 2. Nf3 Nc6 3.`  
`<|ASSISTANT|>`

To make `gpt-4o`, OpenAI first made a base model. As far as I know, that model doesn’t have a name, so let’s call it `gpt-4-base`. It then did instruction tuning and stuck the instruction-tuned model behind the chat interface, to give us `gpt-4o`. (It also did some other stuff like [distillation](https://en.wikipedia.org/wiki/Knowledge_distillation), but never mind.)

I’ve gone through all this background because it allows us to state a central question: How good is `gpt-4-base` at chess? Is it as good at `gpt-3.5-turbo-instruct`? And if it _is_, then why is `gpt-4o` worse? Is it because of the instruction tuning? Or is it just because of the chat template, with the `<|USER|>` and `<|ASSISTANT|>` tokens floating around in ways that don’t happen in chess games written down in PGN notation?

I’m not sure, because OpenAI doesn’t deign to share `gpt-4-base`, nor to allow queries of `gpt-4o` in completion mode. But maybe we can help `gpt-4o` remember its evolutionary history. Maybe we can _prompt_ `gpt-4o` in a way that will sort of trick it into responding _more_ like it was in completion mode.

Should we regurgitate?
----------------------

Thus my idea: Instead of just asking for a move, how about we ask the model to repeat the whole game and _then_ give a move?

I changed the system prompt to this:

`You are a chess grandmaster.`  
`You will be given a partially completed game.`  
`After seeing it, you should repeat the ENTIRE GAME and then give ONE new move.`  
`Use standard algebraic notation, e.g. "e4" or "Rdf8" or "R1a3".`  
`ALWAYS repeat the entire representation of the game so far.`  
`NEVER explain your choice.`

Given a prompt like `1. e4 e5 2.` I expected the model to return an output like `1. e4 e5 2. Nf7`. I checked to make sure it successfully repeated the entire game before giving a new legal move.

This works:

[![Image 58](https://dynomight.net/img/more-chess/regurgitate.svg)](https://dynomight.net/img/more-chess/regurgitate.pdf)

By forcing the models to repeat the whole move sequence, you force the model to create a context for itself where it’s much more likely to choose good moves.

This makes `gpt-4o-mini` and `gpt-4o` better. It also seems like strong evidence that if we could query `gpt-4-base` in completion mode, it would be pretty good.

_Note_: When using this type of prompt, I first gave the model ten tries to repeat the whole sequence and then give a legal move at the end. If none of those tries succeeded, I gave it another ten tries to at least produce a legal move after the new turn number, even if it didn’t repeat the whole game perfectly. If that _still_ didn’t succeed, I chose a move at random.

Can we regurgitate better?
--------------------------

Fine-tuning is good. Regurgitation is good. Are they good together?

To test this, I needed to do a _new_, _independent_ run of fine-tuning. I used the exact same sequence of games and moves, but with outputs repeating the inputs before giving a new move.For example:

*   **System prompt**: (same as above)
*   **User prompt**: `1. e4 c5 2. Nf3 d6 3. d4 cxd4 4. Nxd4 Nf6 5. Nc3 a6 6. Be2 e5 7. Nb3 Be7 8. Be3 Be6 9. f4 exf4 10. Bxf4 Nc6 11. Qd3 Ne5 12. Qg3 Nh5 13. Qe3`
*   **Desired output**: `1. e4 c5 2. Nf3 d6 3. d4 cxd4 4. Nxd4 Nf6 5. Nc3 a6 6. Be2 e5 7. Nb3 Be7 8. Be3 Be6 9. f4 exf4 10. Bxf4 Nc6 11. Qd3 Ne5 12. Qg3 Nh5 13. Qe3 Nxf4`

This… maybe helped a little?

[![Image 59](https://dynomight.net/img/more-chess/regurgitate-finetune.svg)](https://dynomight.net/img/more-chess/regurgitate-finetune.pdf)

And how about examples? Will they improve regurgitation?

I used the same three situations as before for examples, just with the prior sequence of moves added to the start of the outputs.Specifically, I used these three examples:

*   **Input A:** `1.`
*   **Output A:** `1. e4`
*   **Input B:** `1. d4`
*   **Output B:** `1. d4 d5`
*   **Input C:** `1. e4 e5 2. Nf3 Nc6 3.`
*   **Output C:** `1. e4 e5 2. Nf3 Nc6 3. Nf3`

Like before, these had a remarkable impact given how little information they contain.

[![Image 60](https://dynomight.net/img/more-chess/regurgitate-examples.svg)](https://dynomight.net/img/more-chess/regurgitate-examples.pdf)

And should we combine examples _and_ fine tuning?

[![Image 61](https://dynomight.net/img/more-chess/regurgitate-examples-finetune.svg)](https://dynomight.net/img/more-chess/regurgitate-examples-finetune.pdf)

Here we have the same (strange) result as without regurgitation. If you fine-tune, then adding examples helps. But it’s still worse than examples without fine-tuning.

Where do we stand?
------------------

What have we learned so far?

*   **GOOD**: Regurgitation, examples, fine tuning (without examples)
*   **UNCLEAR**: Metadata, repeating the system prompt, fine tuning (with examples)
*   **BAD**: Providing the list of legal moves

So if we use regurgitation and examples and turn everything else off, how good is it? Will it play as well as our old nemesis?

[![Image 62](https://dynomight.net/img/more-chess/but.svg)](https://dynomight.net/img/more-chess/but.pdf)

No. It’s respectable, but still not quite as good as `gpt-3.5-turbo-instruct`.

To compare these more directly, I had `gpt-4o + regurgitate + examples` play 50 games against `gpt-3.5-turbo-instruct`. In all cases, `gpt-4o` was white.

| outcome for `gpt-4o` | count |
| --- | --- |
| win | 10 |
| tie | 5 |
| loss | 35 |

According to [this calculator](https://3dkingdoms.com/chess/elo.htm), that’s consistent with an Elo difference of -191. But you need to account for the fact that `gpt-4o` was always white, reportedly worth around [35 Elo](https://en.wikipedia.org/wiki/First-move_advantage_in_chess#Winning_percentages). Since `gpt-3.5-turbo-instruct` has been measured at around 1800 Elo, this suggests `gpt-4o` with regurgitation and examples hits around 1800 - 191 - 35/2 ≈ 1590 Elo, which is still “intermediate amateur” territory.

Here are 10 games of `gpt-4o + regurgitate + examples` playing against Stockfish: [1](https://lichess.org/Q2lUPANn) [2](https://lichess.org/Da7HUOz4) [3](https://lichess.org/Ijitm5vI) [4](https://lichess.org/ib0wwcAO) [5](https://lichess.org/jOY82JGZ) [6](https://lichess.org/hD9fQMMj) [7](https://lichess.org/SmlDpA6O) [8](https://lichess.org/kyRzFcvU) [9](https://lichess.org/NAI3jWPo) [10](https://lichess.org/x2LFUowA)

And here are 10 games of `gpt-4o + regurgitate + examples` playing against `gpt-3.5-turbo-instruct`: [1](https://lichess.org/RHiS3LUm) [2](https://lichess.org/cq2ZKWwq) [3](https://lichess.org/2uLoukYE) [4](https://lichess.org/JdPgUBCj) [5](https://lichess.org/05DgjWJc) [6](https://lichess.org/BoHLjFp8) [7](https://lichess.org/o4zh92NZ) [8](https://lichess.org/wC4bp7gp) [9](https://lichess.org/gHj3afte) [10](https://lichess.org/ytgH7Qzr)

So here’s my current theory
---------------------------

Here’s my best guess for what is happening:

**Part 1:** OpenAI trains its base models on datasets with more/better chess games than those used by open models.

**Part 2**: Recent _base_ OpenAI models would be excellent at chess (in completion mode, if we could access them). But the _chat_ models that we actually get access to aren’t.

I think part 1 is true because all the open models are [terrible](https://dynomight.net/chess/) at chess, regardless of if they are base models or chat models. I suspect this is _not_ some kind of architectural limitation—if you fine-tuned `llama-3.1-70b` on billions of expert chess games, I would be surprised if it could not beat `gpt-3.5-turbo-instruct` (rumored to have only around 20 billion parameters).

Meanwhile, in section A.2 of [this paper](https://arxiv.org/pdf/2312.09390#page=29) (h/t Gwern) some OpenAI authors mention that GPT-4 was trained on chess games in PGN notation, filtered to only include players with Elo at least 1800. I haven’t seen any public confirmation that `gpt-3.5-turbo-instruct` used the same data, but it seems plausible. And can it really be a coincidence that `gpt-3.5-turbo-instruct` plays games _in PGN notation with a measured Elo of 1800_?

I can’t find any details about how much chess data was included when training Llama et al. I’m sure many games made their way in from the open internet. But specifically curating a giant database of high quality games probably just gives better results, and the open models probably just didn’t do that.

(Incidentally, I encourage people at all AI companies to leak secrets to me. If you use the [anonymous feedback form](https://dynomight.net/about/), please write with sufficient technicality that I can verify your expertise. Secrets will be used only for good, not evil.)

It’s also conceivable that some models are playing worse because they have _too much_ chess data. It could be that the open internet has too many games from low-skill players and that if you don’t filter these out, then the models _correctly_ predict that players would make low-quality moves. But I suspect not, because a smart model would recognize that _if the sequence of moves so far is high skill_ then the player isn’t a total idiot and probably won’t throw away their queen. But the models don’t seem to do that.

I think part 2 of my theory is true mostly because of the experiments I did in this post: If you do weird contortions to “trick” OpenAI chat models into behaving more like completion models, then they play much better. So I suspect that the underlying _base_ models (which we can’t touch) are good.

Now, there’s a major uncertainty in part 2. If `gpt-4o` in chat mode is worse than `gpt-4-base` in completion mode, then why? Is it the chat interface or the instruction tuning, or both? Put another way, would `gpt-4-base` be good at chess in a simulated chat mode? And would `gpt-4o` be good if we could query it _in completion mode_?

It’s impossible to say, because we can’t do those experiments.

Parting thoughts
----------------

1.  Isn’t it great how much of AI is now palace intrigue?
    
2.  It’s very likely that there are ways to coax better behavior out of `gpt-4o`. In truth, I barely scratched the surface here.
    
3.  It’s ridiculously hard to find the optimal combination of prompts and examples and fine-tuning, etc. It’s a very large space, there are no easy abstractions to allow you to search through the space, LLMs are unpredictable and fragile, and these experiments are slow and expensive.
    
4.  I tried running the final recipe with `gpt-4` (rather than `gpt-4o`), and it played poorly. I suspect the reason is that the combination of tricks I found is `gpt-4o` specific. Maybe `gpt-4` needs a different prompt? Or more examples? Or would respond better to fine-tuning? Who knows.
    
5.  In many ways, this feels less like engineering and more like a search for spells.
    

P.S.
----

Thanks to the [Automator](https://dynomight.net/automated/) for crucial guidance and boundless patience. Thanks to Daniel Gross for paying for all the electrons. Here is some good prior work on LLMs and chess:

*   Adam Karvonen’s [chess gpt eval repo](https://github.com/adamkarvonen/chess_gpt_eval), which does careful tests on how good `gpt-3.5-turbo-instruct` is.
    
*   Adam Karvonen’s [chess llm interpretability repo](https://github.com/adamkarvonen/chess_llm_interpretability) and paper, [“Emergent World Models and Latent Variable Estimation in Chess-Playing Language Models”](https://arxiv.org/pdf/2403.15498v2) which show, among other things, that ~`gpt-3.5-turbo-instruct`~ a small LLM trained on chess data _does_ seem to build up some kind of internal representation of board state.
    
*   Matheiu Archer’s [estimates of ELO](https://blog.mathieuacher.com/GPTsChessEloRatingLegalMoves/) for `gpt-3.5-turbo-instruct` and `gpt-3.5-turbo` and `gpt-4`. This also experiments with different temperatures.
    
*   [Transcendence: Generative Models Can Outperform The Experts That Train Them](https://arxiv.org/pdf/2406.11741) (h/t WTFwhatthehell)
    
*   Nicholas Carlini’s [Playing chess with large language models](https://nicholas.carlini.com/writing/2023/chess-llm.html).
    

_Update_: Corrected example one output which slightly improved the results.
