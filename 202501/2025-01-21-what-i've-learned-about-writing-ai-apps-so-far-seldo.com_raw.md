Title: What I've learned about writing AI apps so far

URL Source: https://seldo.com/posts/what-ive-learned-about-writing-ai-apps-so-far

Markdown Content:
I started writing a post called "how to write AI apps" but it was over-reach so I scaled it back to this. Who am I to tell you how to write anything? But here's what I'll be applying to my own writing of AI-powered apps, specifically LLM applications.

A battle I've already lost is that we shouldn't call LLMs "AI" at all; they are machine learning and not the general intelligence that is implied to the layman by the name. It is an even less helpful name than "serverless", my previous candidate for worst technology name. But alas, we're calling LLMs AI and any parts of the field that are not LLMs are being drowned out by the noise around LLMs. I do this a lot at my day job; I am certainly part of the problem.

But if we can't call it what it is we can at least know, as practitioners, what it is: very fancy autocomplete. At scale, autocomplete can perform tasks that look like reasoning, and at some level "looks like reasoning" and "is reasoning" have blurred boundaries. Nevertheless, as the inventor of software you should be clear-eyed about the limitations of these systems, and not try to get them to do things they can't do.

LLMs are good at transforming text into less text
-------------------------------------------------

This is the biggest and most fundamental thing about LLMs, and a great rule of thumb for what's going to be an effective LLM application. Is what you're doing taking a large amount of text and asking the LLM to convert it into a smaller amount of text? Then it's probably going to be great at it. If you're asking it to convert into a roughly equal amount of text it will be so-so. If you're asking it to create more text than you gave it, forget about it. The rest of this post is really just examples of this rule in action.

LLMs only reliably know what you just told them, don't rely on training data
----------------------------------------------------------------------------

LLMs are trained on gigantic quantities of information found on the Internet. As a result, tools like Claude and ChatGPT can answer various general-knowledge questions. This creates a huge temptation to create an app that uses what the LLM already knows to perform some task. This is never effective. You don't know what the LLM has been trained on (famously, because it's often illegally acquired, so those training them refuse to say), therefore you don't know the limits of its knowledge or when it will start to hallucinate.

The way to get around this is to give it the answers. Want to know what a contract says? Give it the contract. Want to know what a video is about? Give it the transcript of the video. Want it to make a decision? Give it all the same information you would use to make that decision. These are all just turning text into less text. It's great at that. (Yes, you can try and get around LLMs only knowing specifically what you just told them by fine-tuning your LLM. Good luck with that.)

This is why Retrieval-Augmented Generation (RAG) is not going anywhere. RAG is basically the practice of telling the LLM what it needs to know and then immediately asking it for that information back in condensed form. LLMs are great at it, which is why RAG is so popular.

LLMs cannot write for you
-------------------------

This is firmly in the "less text into more text" category. If you give an LLM a prompt, it can spew out a novel-sized block of text if you ask it to. But LLMs only know what you tell them. Give it a short prompt and ask for long text and you will get endless waffle, drivel, pointless rambling, and hallucinations. There is no way to get an LLM to perform the thought necessary to write something for you. You have to do the thinking. To get an LLM to write something good you have to give it a prompt so long you might as well have just written the thing yourself.

Let them self-correct, multiple times if necessary
--------------------------------------------------

A wild thing about LLMs is that they can observe what they've done and decide whether they've done a good job. This is sometimes called self-reflection and it's a key part of what agents do, and I can't emphasize enough what a good idea it is to give your LLM the chance to figure out if it fucked up, and a chance to try again. It adds complexity to your app but it will pay you back in reliability many times over. LLMs are bad at one-shotting but if you give them a couple of swings they often get it. It's both the curse and the magic of them being nondeterministic.

Have the LLM do as little as possible
-------------------------------------

Per the above about reliability: you know what's really reliable? Regular programming. It takes inputs and turns them into outputs, the same way every time, according to extremely precise instructions. If there is anything you are asking the LLM to do that could be accomplished by writing some regular code, write that code. It will be faster, cheaper, and way more reliable to run. LLMs are capable of handling ambiguity and complexity, and it's amazing, but the less of it you give them to handle the better they're going to do. Regular, declarative programming can work wonders and you should use it.

LLMs can help a human perform tasks, they cannot replace a human
----------------------------------------------------------------

This is really a corollary of all of the above. If you have a really great prompt containing lots of careful instructions, and provide all the data needed to perform that task, plus lots of chances to reflect and try again, with as much regular code as possible, LLMs are going to be able to perform that task. If you have a whole lot of these collections of prompts and data and code you can create an agent that can perform \*lots\* of tasks. At that point, it's tempting to look at somebody's whole job and say "this job is really just these 20 tasks, I have created an agent that can do all of these tasks, therefore I can replace this person". It's tempting but I have never, ever seen it work.

Jobs are more than collections of tasks. Jobs require prioritization, judgement of exceptional situations, the ability to communicate ad-hoc with other sources of information like colleagues or regulations, the ability to react to entirely unforseen circumstances, and a whole lot of experience. As I said, LLMs can deal with a certain amount of ambiguity and complexity, but the less the better. Giving them a whole, human-sized job is way more ambiguity and complexity than they can handle. It's asking them to turn text into \*more\* text. It's not going to work.

It's easy to argue that as LLMs get bigger context windows and agent tools get more sophisticated that the ability to replace a whole human will show up: after all, LLMs are good at turning text into less text. How much text do you need to replicate everything a human knows? I don't know but it's a lot more than any LLM can handle right now. In the meantime, your attempts to replace humans with LLMs are going to suck. Let your app augment and accelerate a human, I've seen that work lots of times and be very effective.

In particular, because I see this over and over at hackathons: please stop trying to write an LLM app that replaces a doctor or a lawyer. The LLM does not have a law degree or a medical degree baked into its training, and you definitely cannot fit 7 years of medical training into even the biggest prompt. I don't think you can reliably get an LLM to replace any human but especially not a doctor, do not trust your health to autocomplete that is just trying to be helpful. Do not get sued into oblivion because you ChatGPTed your legal terms.

LLMs are awesome and limited
----------------------------

Depending how much of the hype around AI you've taken on board, the idea that they "take text and turn it into less text" might seem gigantic back-pedal away from previous claims of what AI can do. But taking text and turning it into less text is still an enormous field of endeavour, and a huge market. It's still very exciting, all the more exciting because it's got clear boundaries and isn't hype-driven over-reaching, or dependent on LLMs overnight becoming way better than they currently are. Take a look at the possibilities, find something that fits within these boundaries, and then have fun with it.
