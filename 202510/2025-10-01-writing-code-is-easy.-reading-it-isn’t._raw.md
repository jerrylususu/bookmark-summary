Title: Writing Code Is Easy. Reading It Isn’t.

URL Source: https://idiallo.com/blog/writing-code-is-easy-reading-is-hard

Markdown Content:
Writing code is easy. Once you have a solution in mind, and have mastered the syntax of your favorite programming language, writing code is easy. Having an LLM write entire functions for you? Even easier. But the hard part isn’t the writing. It’s the reading. It’s the time it takes to load the mental model of the system into your head. That’s where all the cost really is.

A **mental model** is the thing you build when you read code. It’s your internal map of how the system works, where the tricky parts are, what depends on what. Without it, you’re just staring at lines of text.

When I worked as a contractor, most of my jobs started the same way. I’d get a task to fix a bug or add a new feature in an application I’d never seen before. My mental model was clean and empty at first. To start filling it, I’d check the homepage to see what it looked like. I’d look at the page source: is this React? jQuery? A third-party plugin? I’d scan the codebase to see if the carousel they are requesting on the front page was used elsewhere. I’d check their build process, their testing setup, the tools they leaned on. Every little detail I discovered got appended to the model in my head.

It was like moving into a new city. You start at the foot of your apartment, wander a few streets, notice which roads lead to the freeway, where the grocery store is, and slowly you start to orient yourself. That’s what reading code feels like: you’re building a mental map so you don’t get lost every time you move around.

Say you need to understand a simple function like `getUserPreferences(userId)`. To build your mental model, you need to trace:

*   Where is this function defined?
*   What does it return? Is it a Promise? What's the shape of the data?
*   Does it hit a database directly or go through an API?
*   Are there caching layers involved?
*   What happens if the user doesn't exist?
*   Who else calls this function and in what contexts?
*   Are there side effects?

Understanding that one function means jumping between database schemas, API definitions, error handling middleware, and multiple call sites. Only after building this web of relationships do you have enough context to safely modify anything.

And it’s slow. Reading code is harder than writing it. Much harder. Writing code is forward motion: you’re laying down fresh pavement. Reading code means retracing someone else’s steps, which usually means jumping between files, chasing function calls, inferring side effects, and deciphering intentions that aren’t written down. Understanding one function often means looking at five other files. Only after all that do you have enough of a map to even begin.

It’s the same reason debugging is harder than coding. On Stack Overflow, one of the most common comments you’ll see under a bad question is: _“Can you show us what you did?”_ Without seeing the steps, no one can load the right model in their head to help. It’s also why the [XY problem](https://xyproblem.info/) keeps coming up. People ask about a symptom without giving the context that would let others reconstruct the whole picture.

I'm still fascinated by the lawyer who used [ChatGPT in court](https://www.forbes.com/sites/mollybohannon/2023/06/08/lawyer-used-chatgpt-in-court-and-cited-fake-cases-a-judge-is-considering-sanctions/). He filed a brief that cited six cases which turned out not to exist. Everyone asked: why didn’t he read them? The answer is the same: it takes time and effort to build the model. He would have had to chase down each case, read them, and slot them into a broader understanding of legal precedent. Reading is the hard part. Generating is easy.

Reading isn't just about going through the code and examining it line by line. It's also about going through the documentation, code reviews, and peer programming. In fact, these are solutions for accelerating the process of building our mental model. But with that in mind, you still have to, well, read and understand. You'll notice that programmers often want to rewrite things from scratch, because "the old code sucks". What sucks is taking the time to read and understand it.

And this is what makes LLMs both powerful and dangerous in programming. Whether the AI generates perfect code or complete hallucinations, you still have to read it. You still have to trace through what it’s supposed to do, how it interacts with the rest of the system, and what the side effects are. The longer the generated code, the longer it takes to build your mental model. And only once you’ve done that can you spot the issues, the places where the generated code doesn’t quite fit, or quietly breaks something else.

When an LLM can produce an infinite amount of code or text, it tempts us to skip the reading. But you can’t skip the model. You wouldn’t want to load someone else’s saved game and be dropped in the middle of a boss fight. That’s what it feels like to inherit or generate code you don’t understand.

This is why the real bottleneck in software development isn’t writing, it’s understanding.

* * *

For now, we don't have the LLM equivalent for understanding. Something that could instantly transfer a complete mental model from the system to your head. Until we do, the bottleneck hasn't moved. We've solved the "typing speed" problem. We can generate more code than we could ever hope to read. But until we solve the "understanding" problem, the cost of software development remains the same: the time it takes for someone to make sense of it all.

This has real implications for how we use AI tools. Instead of asking AI to generate large blocks of code, we might be better off asking it to help us understand existing code. Instead of measuring productivity by lines of code written, we should measure it by how quickly teams can build accurate mental models of their systems.

The future of programming might not be about generating more code faster. It might be about generating understanding faster. And that's a much harder problem to solve.

* * *