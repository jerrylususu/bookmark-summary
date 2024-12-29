Title: My Approach to Building Large Technical Projects

URL Source: https://mitchellh.com/writing/building-large-technical-projects

Published Time: 2023-06-01T00:00:00.000Z

Markdown Content:
Whether it's building a new project from scratch, implementing a big feature, or beginning a large refactor, it can be difficult to stay motivated and complete large technical projects. A method that works really well for me is to continuously see real results and to order my work based on that.

We've all experienced that feeling of excitement starting a new project. The first few weeks you can't wait to get on the computer to work. Then slowly over time you get distracted or make up excuses and work on it less. If this is for real work, you forcibly slog your way to the finish line but every day is painful. If this is for fun, you look back years from now and remember what could've been.

I've learned that when I break down my large tasks in chunks that result in seeing tangible forward progress, I tend to finish my work and retain my excitement throughout the project. People are all motivated and driven in different ways, so this may not work for you, but as a broad generalization I've not found an engineer who doesn't get excited by a good demo. And the goal is to always give yourself a good demo.

I'm not claiming that anything I say in this post is novel. It definitely shares various aspects of well-known software engineering or management practices. I'm just sharing the way I approach the larger technical work that I do and why I do it this way.

I'll use [my terminal emulator project](https://twitter.com/mitchellh/status/1662217955424493570) as an example throughout this post so that there is realistic, concrete experience I can share. There's plenty of other projects I could've used but I'll choose this one since it's not related to my professional work and it is recent enough to be fresh in my mind.

I want to be crystal clear that I am not shaming anyone for not completing projects. As long as you're having fun and feel accomplished (or simply don't care), good for you and more power to you. This blog post is aimed at people who _want to finish projects more_ or simply want to learn how I strive to finish projects more.

* * *

The Starting Line
-----------------

Initially, you have some large project and you have to figure _how to start_. For me, this is the hardest part and I can spend hours -- sometimes days -- waffling over the right starting point.

For my terminal emulator, there were a number of large components that I knew would have to exist if I ever intended to finish this project: terminal parsing, running and managing a shell process, font rendering, grid rendering, input handling (keyboard/mouse), etc. There are hundreds of relatively large sub-projects on the path to "done."

If my initial goal was to see a launchable terminal that could run Neovim, I'd be in big trouble. Even with [unknown unknowns](https://en.wikipedia.org/wiki/There_are_unknown_unknowns), this goal just _sounds too big_. I can intuitively realize that there are a lot of components on that path: rendering a GUI, process launching, terminal parsing and state management. This is a bad goal, it's too big and I'd probably lose interest a month or two in.

Instead, I try to think what a _realistic_ project is where I can _see results as soon as possible_. Once you apply that filter, the number of viable sub-projects shrinks dramatically. Here are some examples:

*   VT Parsing - parsing the terminal escape sequences
*   Blank window rendering - open a window and draw a blank canvas
*   Child process lanching - launch a child shell such as bash, zsh, fish, setup the TTY and be able to read output from it (i.e. the initial shell prompt)

I don't try to enumerate all the big sub-projects at this stage. I just kind of get an idea of the _rough shape_ the project will take and find one that I can build in isolation and also physically see some sort of real results.

This is the phase where experience helps the most. Engineers with more experience are usually able to more effectively paint the picture of the rough shape a project will take. They can identify various subcomponents with more accuracy and see how they pieces fit together. With less experience, or in a domain I'm unfamiliar with, I just take a best guess and expect there is a higher likelihood I'll throw my work away at some point.

* * *

Early Results
-------------

Early work tends to not be very _visible_ and that makes seeing tangible results seem difficult. For example, if I chose to work on VT parsing for my terminal, I can't _see_ it work without also hooking up a UI of some sort. Or for some other project if I chose to work on a database schema and minimal API, I similarly can't see that work without writing a client along with a CLI or GUI.

If the initial subproject you choose to work on is a UI, then you can quickly see some results of course! For various reasons, I rarely start frontend first and usually start backend first. And in any situation, you'll eventually get to the backend and reach a similar challenge.

The best tool to get past this phase is automated testing (usually unit testing at this stage). Automated tests let you actually run some code and see it is working and also has the benefit of being good hygiene.

This gives you another guiding point for picking out your first few tasks: if it isn't graphical, you want to pick something that is testable without too much fuss so you can see some results.

For my terminal, I decided to start with VT parsing first, because it was a part of a terminal at the time that I didn't know too much about and it felt like something that I could very easily test: give it some example input as a string, expect some parsed action or event as output.

Seeing the progression of "1 test passed", "4 tests passed," "13 tests passed" and so on is super exciting to me. I'm running some code I wrote _and it's working_. And I know that I'm progressing on some critical sub-component of a larger project.

* * *

Sprint to Demos
---------------

My goal with the early sub-projects isn't to build a _finished sub-component_, it is to build a _good enough sub-component_ so I can move on to the next thing on the path to a _demo_. ✨

This tradeoff isn't just manifested in functionality. It may be manifested in algorithmic or design considerations. For example, you may know that in the future, you'll need to use something like a real database or a fancy data structure or support streaming data. But for the initial set of work, you can just use in-memory contents, built-in data structures such as dictionaries, and require all your inputs/outputs up front.

I think this is an important tradeoff so I will repeat it: **do not let perfection be an enemy of progress.** Going further, do not let future improvements you _know you'll have to make_ stop you from moving on to the next thing. The goal is to get to a demo.

No matter what I'm working on, I try to build one or two demos per week intermixed with automated test feedback as explained in the previous section.

Building a demo also provides you with invaluable product feedback. You can quickly intuit whether something _feels good_, even if it isn't fully functional. These aren't "minimum viable products", because they really aren't viable, but they're good enough to provide an engineer some valuable self-reflection.

This is an area where I think experience actually hurts. I've seen senior engineers get bogged down building the perfect thing and by the time they get a demo, they realize _it sucks_. The implementation doesn't suck, but the product or feature itself actually sucks.

Recall that for the terminal the first task I chose was VT parsing. In the early stages, I only saw automated tests work. To get to my first demo, I built a shell script that would run some command, capture its output, feed it to my VT parser, and output everything it parsed (or couldn't). Over time, I iterated on this CLI as my first "UI" -- I would render the terminal grid using ASCII.

This gave me immense satisfaction since I could run simple programs like `man` or `ls` or more complex programs like `vim` and see my parser work (or break, which is equally exciting in its own way).

In this scenario, the CLI I was writing was relatively useless long term (I ended up throwing it away rather quickly). But the day or two I spent building it as a demo provided me with an important feeling of progress and _seeing_ something work helped keep me motivated.

* * *

Build for Yourself
------------------

This section will apply more to personal projects than to work-assigned projects. Even if you aspire to release some software for others, build _only what you need as you need it_ and _adopt your software as quickly as possible_.

I'm always more motivated working on a problem I'm experiencing myself[1](https://mitchellh.com/writing/building-large-technical-projects#user-content-fn-1). And if a product designed for you doesn't work for you, it's very likely not going to work well for others, either. Therefore, my path from demos to an actual real-world usable product is to find the shortest path to building only the functionality I think I need.

For my terminal, that meant first being able to load my shell configuration (fish) and from there being able to launch and use Neovim. So I beelined all my work to only the functionality needed for that: only the escape sequences those programs used, only rendering the font I use daily, etc. Examples of features I initially omitted: scrolling, mouse selection, search, tabs/splits, etc.

Then I started using my terminal as a daily driver. This step usually has a few false starts; you realize you actually need some feature you omitted or forgot. In my initial runs of my terminal, I realized my arrow keys didn't do anything, there were subtle (but workflow-breaking) rendering bugs, etc. So I'd go abandon using it, but it gave me tangible tasks to work on next.

Additionally, I always feel a lot of pride using software with code that I wrote and that usually helps keep me motivated to continue working on it.

* * *

Packaging it Up
---------------

1.  Decompose a large problem into smaller problems. Importantly, each small problem must have some clear way you can see the results of your work.
    
2.  Only solve the smaller problem enough to progress on a demo-aspect of the larger problem, then move on to the next small problem.
    
3.  Only solve enough small problems to be able to begin building runnable demos of your software, then continue to iterate on more functionality. Make demos as frequently as you can.
    
4.  Prioritize functionality that enables you to adopt your own software, if applicable (a personal project, a work project solving a problem you actually have, etc.). Then continue to solve your own problems first.
    
5.  Go back and iterate on each component as needed for future improvements, repeating this process as needed.
    

* * *

Conclusion
----------

And that's pretty much it. I've followed this general pattern on personal projects, group projects, work projects, school projects, etc. and it's how I keep myself motivated[2](https://mitchellh.com/writing/building-large-technical-projects#user-content-fn-2).

Note that I didn't mention a lot of things! I don't talk about shipping. I know a lot of people find shipping motivational. I don't think you need to ship a project for it to be successful. And for me, I find shipping too big of an event to motivate me long-term. I don't talk about tooling (Git workflows, CI, etc.). I've used my process across multiple jobs and fit it into whatever process is established. And so on.

I think that helps show how much of a _personal process_ this is. Everyone I think needs to find some process to reinforce their motivation in a healthy way. I realized seeing results motivates me really strongly, I've built my work style around that, and it has worked well for me thus far.

1.  This is why I've tried to only ever worked at companies that build or sell products that I would use. A personal choice. [↩](https://mitchellh.com/writing/building-large-technical-projects#user-content-fnref-1)
    
2.  Ironically, my preferred method of _learning_ is to read reference material cover to cover, which is pretty much the exact opposite of the way I approach _building_ something. [↩](https://mitchellh.com/writing/building-large-technical-projects#user-content-fnref-2)
