Title: Vibe code is legacy code

URL Source: https://blog.val.town/vibe-code

Published Time: Thu, 31 Jul 2025 13:49:55 GMT

Markdown Content:
Despite [widespread](https://simonwillison.net/2025/Mar/19/vibe-coding/)[confusion](https://simonwillison.net/2025/May/1/not-vibe-coding/), Andrej Karpathy [coined "vibe coding"](https://x.com/karpathy/status/1886192184808149383?lang=en) as a kind of AI-assisted coding where you **"forget that the code even exists."**

Legacy code
-----------

We already have a phrase for code that nobody understands: **legacy code**.

Legacy code is universally despised, and for good reason. But why? You have the code, right? Can't you figure it out from there?

Wrong. Code that nobody understands is tech debt. It takes a lot of time to understand unfamiliar code enough to debug it, let alone introduce new features without also introducing bugs.

Programming is fundamentally [_theory building_](https://pages.cs.wisc.edu/~remzi/Naur.pdf), not producing lines of code. We know this. This is why we make fun of business people who try to measure developer productivity in lines of code.

When you vibe code, you are incurring tech debt as fast as the LLM can spit it out. Which is why vibe coding is _perfect_ for prototypes and throwaway projects: It's only legacy code if you have to maintain it!

Prototypes & throwaway code
---------------------------

I've happily vibe coded apps to:

*   [Calculate weekly growth rates](https://growth.val.run/)
*   [Rate NYT Connections](https://www.val.town/x/stevekrouse/rate-connections)
*   [Propose to my fiance](https://stevekrouse.com/proposal)

I don't needed to continue developing those apps, so it hasn't been a problem that I don't understand their code. These apps are also very small, which means that I haven't incurred that much debt if I need to jump in and read the code at some point. I was able to vibe code these apps way faster than I could've built them, and it was a blast.

Vibe coding is a spectrum
-------------------------

Vibe coding is on a spectrum of how much you understand the code. The more you understand, the less you are vibing.

![Image 1: shapes at 25-07-30 10.32.53.png](https://imagedelivery.net/iHX6Ovru0O7AjmyT5yZRoA/a93f8e81-c9b8-4277-6d19-525d2b8d5400/public)

Simply by being an engineer and asking for a web app with a persistent database, you are already vibing less than than a non-programmer who asks for an "app" without understanding the distinction between a web app and a native app, or how persistent data storage works.

Giving a credit card to a child
-------------------------------

The worst possible situation is to have a non-programmer vibe code a large project that they intend to maintain. This would be the equivalent of giving a credit card to a child without first explaining the concept of debt.

As you can imagine, the first phase is ecstatic. _I can wave this little piece of plastic in stores and take whatever I want!_

Which is a lot like _AI can build anything now! Nobody needs to learn how to code! Look at what it just made for me!_

But if you wait a month, you'll get the credit card bill. _Did I actually need to buy all those things? How will I get myself out of this hole?_

It's similar for the vibe coder. _My code broken. What do all these files and folders even do? How will I ever get this fixed? Can I get a refund for the $400 I spent vibe coding?_

If you don't understand the code, your only recourse is to ask AI to fix it for you, which is like paying off credit card debt with another credit card.

Serious coding with AI in 2025
------------------------------

If you're building something serious that you intend to maintain in 2025, Andrej has the right of it:

> [Keep] a very tight leash on this new over-eager junior intern savant with encyclopedic knowledge of software, but who also bullshits you all the time, has an over-abundance of courage and shows little to no taste for good code. And emphasis on being slow, defensive, careful, paranoid, and on always taking the inline learning opportunity, not delegating.
> 
> 
> — Andrej Karpathy, [twitter](https://x.com/karpathy/status/1915581920022585597)

How we approach building for AI
-------------------------------

At Val Town, we've built AI into our product in dozens of ways. [Townie](https://townie.val.run/) is our AI asisstant that agentically reads & writes code, runs it, views the logs, and keeps iterating until it's done.

[Townie](https://townie.val.run/) is an awesome tool for vibe coding. I heartily recommend it to folks who understand these tradeoffs. I use it to vibe code sometimes. Other times I keep in on a tight leash as it makes surgical edits to a project I care about. Both are fun and useful.

Coding with AI is changing so quickly that it's hard to know what tomorrow will bring, but I'm confident that theory building will remain central to the activity of building complex software. Our technical expertise will still be relevant! And I'm optimistic that AI will continue to make programming better in suprising ways.

But if you know any non-programmers spending thousands of dollars vibe coding their billion dollar app idea today, please send them this post. Vibe coding is not going to get them where they want to go. They're going to have to learn to use their human eyes to read the code 😱, and learn that sometimes it's easier to start over with building a well-written code base from scratch than to fix a legacy one that nobody understands.

* * *

_This essay is a distillation of a talk I gave last month, [The Role of the Human Brain in Programming](https://www.youtube.com/watch?v=1WC8dxMC4Xw). Thanks to my fiance Emily for listening to me rant about these topics for months, and for filming my talk. Thanks Malte and Rippling for hosting the talk._

_Thanks Geoffrey Litt, Jimmy Koppel, Max McDonnell, Tom MacWright, Charmaine Lee, Brent Jackson, and Dan Shipper for feedback on this post. Thanks Simon Willison and Andrej Karpathy for being voices of reason amidst all the AI hype and naysayers._
