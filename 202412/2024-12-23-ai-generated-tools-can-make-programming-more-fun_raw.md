Title: AI-generated tools can make programming more fun

URL Source: https://www.geoffreylitt.com/2024/12/22/making-programming-more-fun-with-an-ai-generated-debugger.html

Markdown Content:
I want to tell you about a neat experience I had with AI-assisted programming this week. What’s unusual here is: **the AI didn’t write a single line of my code.** Instead, I used AI to build a _custom debugger UI_… which made it more fun for me to do the coding myself.

\* \* \*

I was hacking on a Prolog interpreter as a learning project. [Prolog](https://en.wikipedia.org/wiki/Prolog) is a logic language where the user defines facts and rules, and then the system helps answer queries. A basic interpreter for this language turns out to be an elegant little program with surprising power—a perfect project for a fun learning experience.

The trouble is: it’s also a bit finicky to get the details right. I encountered some bugs in my implementation of a key step called [_unification_](https://en.wikipedia.org/wiki/Unification_(computer_science))—solving symbolic equations—which was leading to weird behavior downstream. I tried logging some information at each step of execution, but I was still parsing through screens of text output looking for patterns.

I needed better visibility. So, I asked [Claude Artifacts](https://support.anthropic.com/en/articles/9487310-what-are-artifacts-and-how-do-i-use-them) to whip up a custom UI for viewing one of my execution traces. After a few iterations, here’s where it ended up:

I could step through an execution and see a clear visualization of my interpreter’s stack: how it has broken down goals to solve; which rule it’s currently evaluating; variable assignments active in the current context; when it’s come across a solution. The timeline shows an overview of the execution, letting me manually jump to any point to inspect the state. I could even leave a note annotating that point of the trace.

Oh yeah, and don’t forget the most important feature: the retro design 😎.

Using this interactive debug UI gave me far clearer visibility than a terminal of print statements. I caught a couple bugs immediately just by being able to see variable assignments more clearly. A repeating pattern of solutions in the timeline view led me to discover an infinite loop bug.

**And, above all: I started having more fun!** When I got stuck on bugs, it felt like I was getting stuck in interesting, essential ways, not on dumb mistakes. I was able to get an intuitive grasp of my interpreter’s operation, and then hone in on problems. As a bonus, the visual aesthetic made debugging feel more like a puzzle game than a depressing slog.

\* \* \*

Two things that stick out to me about this experience are 1) how fast it was to get started, and 2) how fast it was to iterate.

When I first had the idea, I just copy-pasted my interpreter code and a sample execution trace into Claude, and asked it to build a React web UI with the rough functionality I wanted. I also specified “a fun hacker vibe, like the matrix”, because why not? About a minute later (after a single iteration for a UI bug which Claude fixed on its own), I had a solid first version up and running:

![Image 6: My prompt to Claude](https://www.geoffreylitt.com/images/article_images/debugger/prompt.png?1734903615)

**That fast turnaround is absolutely critical, because it meant I didn’t need to break focus from the main task at hand.** I was trying to write a Prolog interpreter here, not build a debug UI. Without AI support, I would have just muddled through with my existing tools, lacking the time or focus to build a debug UI. Simon Willison says: [“AI-enhanced development makes me more ambitious with my projects”](https://simonwillison.net/2023/Mar/27/ai-enhanced-development/). In this case: AI-enhanced development made me more ambitious with my _dev tools_.

By the way: I was confident Claude 3.5-Sonnet would do well at this task, because it’s great at building straightforward web UIs. That’s all this debugger is, at the end of the day: a simple view of a JSON blob; an easy task for a competent web developer. In some sense, you can think of this workflow as a technique for turning that narrow, limited programming capability—rapidly and automatically building straightforward UIs—into an accelerant for more advanced kinds of programming.

Whether you’re an AI-programming skeptic or an enthusiast, the reality is that many programming tasks are beyond the reach of today’s models. But many decent _dev tools_ are actually quite easy for AI to build, and can help the rest of the programming go smoother. In general, these days any time I’m spending more than a minute staring at a JSON blob, I consider whether it’s worth building a custom UI for it.

\* \* \*

As I used the tool in my debugging, I would notice small things I wanted to visualize differently: improving the syntax display for the program, allocating screen real estate better, adding the timeline view to get a sense of the full history.

Each time, I would just switch windows, spend a few seconds asking Claude to make the change, and then switch back to my code editor and resume working. When I came back at my next breaking point, I’d have a new debugger waiting for me. Usually things would just work the first time. Sometimes a minor bug fix was necessary, but I let Claude handle it every time. I still haven’t looked at the UI code.

Eventually we landed on a fairly nice design, where each feature had been motivated by an immediate need that I had felt during use:

![Image 7](https://www.geoffreylitt.com/images/article_images/debugger/debugger-annotated.png?1734903615)

Claude wasn’t perfect—it did get stuck one time when I asked it to add a [flamegraph](https://www.brendangregg.com/flamegraphs.html) view of the stack trace changing over time. Perhaps I could have prodded it into building this better, or even resorted to building it myself. But instead I just decided to abandon that idea and carry on. **AI development works well when your requirements are flexible** and you’re OK changing course to work within the current limits of the model.

Overall, **it felt incredible that it only took seconds to go from noticing something I wanted in my debugger to having it there in the UI.** The AI support let me stay in flow the whole time; I was free to think about interpreter code and not debug tool code. I had a yak-shaving intern at my disposal.

This is the dream of [malleable software](https://www.geoffreylitt.com/2023/03/25/llm-end-user-programming): editing software at the speed of thought. Starting with just the minimal thing we need for our particular use case, adding things immediately as we come across new requirements. Ending up with a tool that’s molded to our needs like a leather shoe, not some complicated generic thing designed for a million users.

*   For more zoomed-out thoughts on the possibilities of custom AI-generated tools, check out [Malleable software in the age of LLMs](https://www.geoffreylitt.com/2023/03/25/llm-end-user-programming)
*   I’ve written before about using AI to develop one-off custom personal tools, like [a Japanese text message translation app with a formality slider](https://www.geoffreylitt.com/2023/07/25/building-personal-tools-on-the-fly-with-llms).
*   A few months ago, a collaborator and I had a similar experience building [a custom visualization tool for bounding boxes on PDFs](https://x.com/geoffreylitt/status/1821666220644683950).
*   The idea of custom tools for debugging programming systems has been explored in depth by many live programming tools; e.g. check out [Glamorous Toolkit](https://gtoolkit.com/) and [Clerk](https://clerk.vision/).
