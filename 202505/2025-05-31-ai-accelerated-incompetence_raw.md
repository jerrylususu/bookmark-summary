Title: AI: Accelerated Incompetence

URL Source: https://www.slater.dev/accelerated-incompetence/

Markdown Content:
![Image 1: Doug Slater](https://www.slater.dev/images/doug.jpg)

Doug·2025-05-19

_In software engineering, over-reliance on LLMs accelerates incompetence. LLMs can't replace human critical thinking._

_The text in this essay was written without any use of AI._

![Image 2: A chart showing a speculative inverse correlation between LLM dependence and IQ](https://www.slater.dev/llm_dependence.jpg)
A speculative inverse correlation between LLM dependence and IQ

By now much ink has dried on the wave of AI and LLMs which crashed upon the public consciousness in late 2022. As an experienced software engineer, I'd like to speak to two troubling engineering perspectives I've observed on LLMs.

"LLMs are my friend"
--------------------

I don't think anyone believes that a computer program is literally their companion, so let's address the euphemistic intent of the above phrase: namely that an LLM conveys magnificent benefits upon its user.

Engineers who view LLMs as an ally invariably prioritize or feel pressured to prioritize velocity; for them, production trumps perspicacity. While it's true that LLMs can deliver a lot of code quickly, their use carries a long tail of _risks_.

Risks of using LLM
------------------

*   **Output Risk**. An LLM can give output that is blatantly incorrect, for example code that won't compile. More likely and dangerously, it can give output that is subtly and undetectably wrong, like logic bugs. The risk is elevated if the prompter is not qualified to evaluate the output, for example project managers prompting for source code.
*   **Input Risk**. An LLM does not challenge a prompt which is leading[1](https://www.slater.dev/accelerated-incompetence/#references) or whose assumptions are flawed or context is incomplete. Example: An engineer prompts, "Provide a thread-safe list implementation in C#" and receives 200 lines of flawless, correct code. It's still the wrong answer, because the question should have been, "How can I make this code thread-safe?" and whose answer is "Use `System.Collections.Concurrent`" and 1 line of code. The LLM is not able to recognize an instance of the XY problem[2](https://www.slater.dev/accelerated-incompetence/#references) because it was not asked to.
*   **Future Velocity**. This is your typical "tech debt" argument, but more urgent. AI can degrade the quality of your codebase _so fast_. Have you ever seen the fruits of hoarding disorder? From the outside, a house or apartment may look fine. But the inside is unsanitary, reprehensible, and nonfunctional. Developers are discovering that without strong guardrails, code produced by an LLM is like such a space.
*   **User Infantilization**. An extinction of talent will occur within individuals and organizations that outsource thinking and problem solving to LLMs: 
    *   As senior engineers are deprived of the opportunity to learn through productive struggle, their existing problem solving and critical thinking skills atrophy: 
        *   "Microsoft research on knowledge workers found that AI-driven confidence often comes at the expense of critical thinking"[3](https://www.slater.dev/accelerated-incompetence/#references)
        *   "In a world pushing for “reflexive AI usage,” I’m advocating for something different: thoughtful, intentional collaboration with AI that preserves the essence of coding as a craft"[4](https://www.slater.dev/accelerated-incompetence/#references)
        *   "LLMs give me finished thoughts, polished and convincing, but none of the intellectual growth that comes from developing them myself" [5](https://www.slater.dev/accelerated-incompetence/#references)

    *   Junior engineers never develop such skills to begin with and so can never in turn mentor future junior engineers.

*   **Loss of Joy**. Many developers are reporting that using AI robs them of flow state and the joy of creation.[6](https://www.slater.dev/accelerated-incompetence/#references) AI-generated code is miserable to read and change.

In a future post, I plan to write about mitigations for each of these risks. Be sure to subscribe below if that sounds interesting.

"I'll become redundant"
-----------------------

Source[7](https://www.slater.dev/accelerated-incompetence/#references)

No, you won't. That said, there are certainly things you can do to further differentiate yourself from an LLM. To stay on topic, I'll defer that to a future post.

There are two programming competences that LLMs cannot furnish: _program theory_ and _program entropy_.

Program Theory
--------------

> ...programming properly should be regarded as an activity by which the programmers form or achieve a certain kind of insight, a theory, of the matters at hand

-- Peter Naur, _Programming as Theory Building_, 1985[8](https://www.slater.dev/accelerated-incompetence/#references)

Naur was one of the greats in computing. He argued, against popular belief at the time, that a program is not its source code. Rather, the program is a shared mental construct: a _theory_ or _design_. From that, the engineer derives code, but the work product of value is the design, not code.

To help you think about the difference between program theory and program text, consider this thought experiment: Imagine that two engineering teams of equivalent talent, A and B, are locked in separate rooms. Each team is told not to communicate with the other. Team A is tasked to write a program, for example a simple terminal-based Chess game. Team B just waits, plays real Chess, or whatever. When Team A is finished, their source code is handed to Team B. Now each team is asked in parallel to add a feature to the program, for example a virtual chess player so the game can be played solo. (We'll let Team A take a coffee break before they get started).

_Question_: Which team will deliver a better solution?

_Answer_: Team A, because those engineers have a fresh mental model of the program they just created, while Team B has none.

According to Naur, the theory matters because inevitably a program needs to be _maintained_, i.e. modified after its initial creation. If all you have is the source code and not an internalized understanding of its design, the cost for those modifications will be higher. I think we can each remember a time we were introduced to a big existing codebase. At first our productivity was near zero. As we loaded the program theory into our mind, productivity rose.

### LLMs and Program Theory

LLMs as they currently exist cannot master a theory, design, or mental construct because they don't remember beyond their context window. Only humans can can gain and retain program theory.

Program Entropy
---------------

Complexity is a fundamental opposing force of programming[9](https://www.slater.dev/accelerated-incompetence/#references), and it correlates with entropy.

> ...program building is an entropy-decreasing process...program maintenance is an entropy-increasing process, and even its most skillful execution only delays the subsidence of the system into unfixable obsolescence

-- Fred Brooks, _The Mythical Man-Month_, 1975

Brooks, another prominent historical figure in computing, asserted that after initial construction, the changes made to a program can only make the source code more complex. However, changes made in harmony with the design will do so at a slower rate.

### LLMs and Program Entropy

An LLM is a token predictor. It works only at the level of text. It is not capable of working at a conceptual level: it doesn't reason about ideas, diagrams, or requirements specifications. Everyone who has prompted an LLM with a large chunk of code has beheld that the LLM tends to apply unnecessary and bizarre changes, and the longer the conversation drags on, the more it diverges. How often have you witnessed an LLM _reduce_ the complexity of a piece of code?

Only humans can decrease or resist complexity.

Conclusion
----------

We found wisdom for the LLM age by remembering what two forerunners of our discipline had to say about software design and complexity.

If you had hoped that AI would launch your engineering career to the next level, be warned that it could do the opposite. _LLMs can accelerate incompetence._

If you're a skilled, experienced engineer and you fear that AI will make you unemployable, adopt a more nuanced view. _LLMs can't replace human engineering._

The business allure of AI is reduced costs through commoditized engineering, but just like offshore engineering talent brings forth mixed fruit, LLMs fall short and open risks.

The AI hype cycle will eventually peak[10](https://www.slater.dev/accelerated-incompetence/#references). Companies which overuse AI now will inherit a long tail of costs, and they'll either pivot or go extinct. As such, the long-term value proposition for humans in engineering remains unchanged. The world still needs and will pay for technical skills and deep thinking in engineering.

AI will stick around, though. Use it as a tool, not a crutch, and continue to invest in the same fundamental engineering skills that were deemed valuable in 2019.

Next...
-------

Subscribe to my email list below. I plan to write more.

References
----------

1.   [Leading Question](https://en.wikipedia.org/wiki/Leading_question)
2.   [The XY Problem](https://en.wikipedia.org/wiki/XY_problem)
3.   [ThoughtWorks Technology Radar Volume 32](https://www.thoughtworks.com/content/dam/thoughtworks/documents/radar/2025/04/tr_technology_radar_vol_32_en.pdf)
4.   [Coding as Craft: Going Back to the Old Gym](https://cekrem.github.io/posts/coding-as-craft-going-back-to-the-old-gym/)
5.   [Thoughts on Thinking](https://dcurt.is/thinking)
6.   [The Hidden Cost of AI Coding](https://terriblesoftware.org/2025/04/23/the-hidden-cost-of-ai-coding/)
7.   ["I wonder if I'll become redundant"](https://www.reddit.com/r/ExperiencedDevs/comments/1h3xpke/dont_know_if_the_right_place_how_to_work_on/)
8.   [Programming as Theory Building](https://pablo.rauzy.name/dev/naur1985programming.pdf)
9.   [Grug on Complexity](https://grugbrain.dev/#grug-on-complexity)
10.   [Gartner Hype Cycle](https://en.wikipedia.org/wiki/Gartner_hype_cycle)

* * *

[←Tech Risk is Business Risk](https://www.slater.dev/tech-risk-is-business-risk/)
