Title: Coding with LLMs in the summer of 2025 (an update)

URL Source: https://antirez.com/news/154

Markdown Content:
[antirez](https://antirez.com/user/antirez) 1 day ago. 119666 views. Frontier LLMs such as Gemini 2.5 PRO, with their vast understanding of many topics and their ability to grasp thousands of lines of code in a few seconds, are able to extend and amplify the programmer capabilities. If you are able to describe problems in a clear way and, if you are able to accept the back and forth needed in order to work with LLMs, you can reach incredible results such as:

1. Eliminating bugs you introduced in your code before it ever hits any user: I experienced this with Vector Sets implementation of Redis. I would end eliminating all the bugs eventually, but many were just removed immediately by Gemini / Claude code reviews.

2. Explore faster how a given idea could work, by letting the LLM write the throw away code to test ASAP in order to see if a given solution is actually more performant, if it is good enough, and so forth.

3. Engage in pair-design activities where your instinct, experience, design taste can be mixed with the PhD-level knowledge encoded inside the LLM. In this activity, the LLM will sometimes propose stupid paths, other times incredibly bright ideas: you, the human, are there in order to escape local minimal and mistakes, and exploit the fact your digital friend knows of certain and various things more than any human can.

4. Accelerate your work by writing part of the code under your clear specifications.

5. Work with technologies far from your expertise but contiguous with what you can do (for instance: coding in 68000 assembly for an Amiga demo?) using LLMs as an extension of specific parts of your mind, for the knowledge you don't have.

One and half years ago I wrote a blog post called “LLMs and programming in the first days of 2024”. There, I found LLMs to be already useful, but during these 1.5 years, the progresses they made completely changed the game. However, in order to leverage their capabilities, humans interacting with LLMs must have certain qualities and follow certain practices. Let’s explore them.

## Refuse vibe coding most of the times

In this historical moment, LLMs are good amplifiers and bad one-man-band workers. There are still small throwaway projects where letting the LLM write all the code makes sense, like tests, small utilities of a few hundreds lines of codes. But while LLMs can write part of a code base with success (under your strict supervision, see later), and produce a very sensible speedup in development (or, the ability to develop more/better in the same time used in the past — which is what I do), when left alone with nontrivial goals they tend to produce fragile code bases that are larger than needed, complex, full of local minima choices, suboptimal in many ways. Moreover they just fail completely when the task at hand is more complex than a given level. Tomorrow all this may change, but right now after daily experience writing code with LLMs I strongly believe the maximum quality of work is reached using the human+LLM equation. I believe that humans and LLMs together are more productive than just humans, but this requires a big “if”, that is, if such humans have extensive communication capabilities and LLMs experiences: the ability to communicate efficiently is a key factor in using LLMs.

## Provide large context

When your goal is to reason with an LLM about implementing or fixing some code, you need to provide extensive information to the LLM: papers, big parts of the target code base (all the code base if possible, unless this is going to make the context window so large than the LLM performances will be impaired). And a brain dump of all your understanding of what should be done. Such braindump must contain especially the following:

* Hints about bad solutions that may look good, and why they could be suboptimal.
* Hints about very good potential solutions, even if not totally elaborated by the humans still: LLMs can often use them in order to find the right path.
* Clear goals of what should be done, the invariants we require, and even the style the code should have. For instance, LLMs tend to write Python code that is full of unnecessary dependencies, but prompting may help reducing this problem. C code tends to be, in my experience, much better.

When dealing with specific technologies that are not so widespread / obvious, it is often a good idea to also add the documentation in the context window. For example when writing tests for vector sets, a Redis data type so new that LLMs don’t yet know about, I add the README file in the context: with such trivial trick, the LLM can use vector sets at expert level immediately.

## Use the right LLMs

The most famous LLMs are not the best. Coding activities should be performed mostly with:

* Gemini 2.5 PRO
* Claude Opus 4

Gemini 2.5 PRO is, in my experience, semantically more powerful. Can spot more complex bugs, reason about more complex problems. Claude Opus may be better at writing new code sometimes (sometimes not), the user interface is more pleasant, and in general you need at least two LLMs to do some back and forth for complex problems in order to enlarge your (human) understanding of the design space. If you can pick just one, go for Gemini 2.5 PRO.

The fundamental requirement for the LLM to be used is: don’t use agents or things like editor with integrated coding agents. You want to:

* Always show things to the most able model, the frontier LLM itself.
* Avoid any RAG that will show only part of the code / context to the LLM. This destroys LLMs performance. You must be in control of what the LLM can see when providing a reply.
* Always be part of the loop by moving code by hand from your terminal to the LLM web interface: this guarantees that you follow every process. You are still the coder, but augmented.

## Conclusions

Despite the large interest in agents that can code alone, right now you can maximize your impact as a software developer by using LLMs in an explicit way, staying in the loop. This will inevitably change in the future, as AI will improve, and eventually many coding tasks will be better served by AI alone: in this future, the human will decide the what & how, which is still crucial. But we are not yet there. In this exact moment taking control allows to use LLMs to produce the sharpest code possible: minimal when needed, using complex ideas when required.

You will be able to do things that are otherwise at the borders of your knowledge / expertise while learning much in the process (yes, you can learn from LLMs, as you can learn from books or colleagues: it is one of the forms of education possible, a new one). Yet, everything produced will follow your idea of code and product, and will be of high quality and will not random fail because of errors and shortcomings introduced by the LLM. You will also retain a strong understanding of all the code written and its design.

From time to time, it is wise to test what agents can do. But each time you feel they can’t do as well as you can, return to your terminal, and code with the help of AI (when you feel it can improve your output; there are times where you just are better alone). When this will be true, that agents will perform superb work, I’ll be the first to switch, and I’ll keep coding by myself just for passion. But for now, let’s skip the hype, and use AI at its best, that is: retaining control. There is another risk, however: of avoiding LLMs for some ideological or psychological refusal, accumulating a disadvantages (and failing to develop a large set of skills - hard to describe - needed to work with LLMs). Maybe this is really a case of "In medio stat virtus".
