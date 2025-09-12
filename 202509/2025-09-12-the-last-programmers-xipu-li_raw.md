Title: The Last Programmers || Xipu Li

URL Source: https://www.xipu.li/posts/the-last-programmers

Markdown Content:
I quit my job at Amazon in May to join a startup called [Icon](https://icon.com/). Best career decision I ever made, but not for the reasons you might think.

At Amazon, I was on the [Amazon Q Developer](https://aws.amazon.com/q/developer/) team, building their AI coding assistant. You'd think being at the center of Amazon's AI developer tools would be exciting, but it was actually deeply frustrating. It was apparent to anyone outside the Amazon bubble that we were losing the AI game badly. The leadership was constantly playing catch-up because there was very little true product vision. They kept saying they wanted to move like a startup, but then had the risk tolerance of IBM.

Everything took forever. AppSec reviews, design doc reviews, architectural review boards. By the time we shipped anything, companies like [Cursor](https://cursor.com/) and [Anthropic](https://www.anthropic.com/) had already iterated through ten versions. We'd spend months debating whether a feature was safe enough to release while our competitors were shipping weekly updates based on actual user feedback.

What really struck me was how Amazon's product decisions were driven by internal KPIs rather than user empathy. The most obvious example was authentication. GitHub auth is the standard for developer tools because it removes friction for the exact audience you're trying to serve. But Amazon insisted on funneling users through [Builder ID](https://docs.aws.amazon.com/signin/latest/userguide/sign-in-aws_builder_id.html), their own auth system. From an internal metrics perspective, it probably looked great (more Builder ID signups!). From a user perspective, it was just another barrier to trying the product. I watched potential users bounce off that requirement constantly.

I felt like I was reaching the ceiling of what I could learn about AI and building good products within Amazon's constraints. That's why I joined Icon. At Icon, we move at a completely different speed. We ship features in days that would have taken Amazon months to approve.

But that's not the interesting part. The interesting part is watching how my teammates work. One of them hasn't looked at actual code in weeks. Instead, he writes design documents in plain English and trusts AI to handle the implementation. When something needs fixing, he edits the document, not the code.

It made me realize something profound: we're living through the end of an era where humans translate ideas into code by hand. Within a few years, that skill will be as relevant as knowing how to shoe a horse.

[](https://www.xipu.li/posts/the-last-programmers#what-im-seeing-right-now)What I'm Seeing Right Now
----------------------------------------------------------------------------------------------------

My teammate has six [Claude Code](https://www.anthropic.com/claude-code) terminal windows open at once, each one handling a different task or feature. He literally speaks to them one by one using [Whispr Flow](https://wisprflow.ai/), and they all execute in parallel. Most of his day is spent reviewing design documents and looking at the actual web app to see the changes being made in real time. Only in very rare cases does he actually dive into the code to debug something.

This developer isn't becoming less valuable. If anything, he's becoming more valuable because he can focus on the hard problems that actually matter. Now I see him spending most of his time doing what product managers traditionally do: talking to users, understanding their problems deeply, figuring out what's actually worth building. Coding has become maybe 20% of his job, and even that 20% is mostly about understanding requirements and translating them into clear specifications. The actual implementation work that used to consume 80% of his time is now handled by machines.

The only bottleneck is model speed and quality. But with billions of dollars pouring into generative AI every year, we will see instant voice-to-code capabilities + bug-free quality in 2-5 years.

The code itself has become an implementation detail, like the electrical wiring behind your drywall. You know it's there, you trust that it works, but you don't think about it unless something breaks. And increasingly, nothing breaks.

That will change everything about how products get made and who gets to make them.

[](https://www.xipu.li/posts/the-last-programmers#the-split-im-watching)The Split I'm Watching
----------------------------------------------------------------------------------------------

Something interesting is happening on our team right now, and I think it's a preview of how the entire industry will divide over the next few years.

There are two camps emerging, and the difference isn't really about skill level or experience. It's about fundamental attitudes toward what programming should be.

On one side, we have what I call the experimenters. These are people who spend their lunch breaks trying out new AI coding tools, setting up workflows that generate entire features from voice commands, and constantly pushing the boundaries of how little manual coding they can get away with. To traditionalists, they might look lazy. They're always looking for shortcuts, always asking "can AI do this for me?" instead of just buckling down and writing the code themselves.

But here's what I've realized watching them: they're not lazy. They're just following the natural path that technology has always followed. Every major advancement in programming has been about abstracting away complexity so humans can focus on higher-level problems. We moved from machine code to assembly to high-level languages to frameworks to libraries. Each step made things "easier" and each step had people complaining that developers were getting soft.

These experimenters understand something fundamental: laziness wins in technology. The person who finds a way to accomplish the same result with less effort doesn't just make their own life better. They often discover the path that everyone else will eventually follow.

On the other side, we have the guardians. These are people who believe deeply that understanding code at a fundamental level is non-negotiable. They can spot inefficient algorithms, they know why certain design patterns exist, they understand the underlying systems well enough to debug problems that AI tools can't handle. They see the experimenters as shortcuts artists who are building on shaky foundations.

And honestly? They're not wrong. When the AI-generated code breaks in subtle ways, when performance becomes an issue, when edge cases emerge that the AI didn't anticipate, these are the people who can actually fix it. They have a depth of understanding that the experimenters often lack.

But here's what I think the guardians are missing: the world is changing faster than their gatekeeping can keep up with. The bar for "good enough" code keeps dropping while the bar for understanding users and building valuable products keeps rising. A slightly inefficient implementation that ships next week is often better than a perfectly optimized implementation that ships next month.

I watch these two groups work on the same problems, and it's fascinating. The experimenters ship faster, iterate more, and often end up with products that users prefer (even if the underlying code makes the guardians cringe). The guardians build more robust, maintainable systems, but they sometimes spend so much time perfecting the implementation that they miss opportunities to learn what users actually want.

Neither approach is completely right, but I have a prediction about which one wins in the long run. Technology trends toward convenience and abstraction. The tools get better, the AI gets smarter, and the "shortcuts" that look like cheating today become standard practice tomorrow.

The experimenters aren't just being lazy. They're adapting to a world where the bottleneck isn't code quality. It's everything else.

[](https://www.xipu.li/posts/the-last-programmers#the-great-commoditization)The Great Commoditization
-----------------------------------------------------------------------------------------------------

The entire game changes from "can we build this?" to "should we build this?" and "how do we get people to use it?"

Anyone can learn to make chocolate. The ingredients are commoditized. The manufacturing process is well-understood. You can literally buy chocolate-making equipment on Amazon and start a brand tomorrow.

But look at who wins in the chocolate industry. It's not the people with the best manufacturing processes. It's Hershey's, Cadbury, Lindt. These are brands that figured out distribution, marketing, and customer psychology decades ago. The product quality matters, but it's table stakes. What matters is whether people know your brand exists and trust it enough to buy it.

Software is heading exactly the same direction. The gap between software products and consumer goods is shrinking every month. Both compete on branding, distribution, and understanding customer psychology rather than pure functionality.

I can already imagine (and I bet someone is building this right now) AI that can clone any app from a URL. You feed it a competitor's website or app store listing, and it spits out a functionally identical product in minutes. When that happens, and it will happen soon, the product itself becomes completely commoditized. Success depends entirely on whether you can market and distribute better than the original.

[](https://www.xipu.li/posts/the-last-programmers#what-actually-survives)What Actually Survives
-----------------------------------------------------------------------------------------------

Three things become incredibly valuable when technical implementation gets commoditized.

First is understanding what people actually need. Not what they say they need in surveys or focus groups, but what they'll actually pay for and use every day. This is harder than it sounds. I've seen brilliant product managers get this wrong constantly. It requires talking to users, watching how they actually behave, understanding the gap between stated preferences and revealed preferences. It's part psychology, part anthropology, part business intuition.

Second is knowing what to build and what not to build. This is taste, but it's also strategy. Understanding which features will create real value versus which will just add complexity. Recognizing when a product is good enough versus when it needs more polish. Seeing the difference between a feature users will try once and a feature they'll use every day. Most people are terrible at this. They either build everything anyone suggests or they build nothing because they can't decide what's important.

Third is getting products in front of the right people and convincing them to care. Distribution and marketing, but also positioning, timing, and understanding customer psychology. Building trust and brand recognition. Creating word-of-mouth growth. Understanding how people discover new products and what motivates them to switch from existing solutions.

These skills don't get automated away. If anything, they become more valuable as technical implementation becomes commoditized. Because when everyone can build software, **the winners are the people who understand humans**.

[](https://www.xipu.li/posts/the-last-programmers#what-this-means-if-youre-starting-out)What This Means If You're Starting Out
------------------------------------------------------------------------------------------------------------------------------

If you're learning to code today, please don't stop. But don't make coding your only skill. The developers who thrive in this new world will be the ones who understand users, markets, and business models as well as they understand technology.

Spend time talking to people who use software. Not other developers but actual users. Learn what frustrates them about existing products. Understand how they discover new tools and what convinces them to adopt something new.

Study successful products in industries you care about. Not just their features, but their go-to-market strategies. How did they get their first thousand users? How do they retain customers? What makes people recommend them to friends?

Practice communicating complex ideas simply. The most valuable skill in an AI-assisted world might be the ability to translate fuzzy human problems into clear, implementable specifications.

[](https://www.xipu.li/posts/the-last-programmers#what-this-means-if-youre-already-building)What This Means If You're Already Building
--------------------------------------------------------------------------------------------------------------------------------------

If you're already a developer or building a company, remember that your technical implementation will soon be replicable by anyone with access to good AI tools. Your competitive advantage needs to be something else.

Better user understanding. Stronger distribution channels. Clearer market positioning. Faster learning cycles. Better taste in what to build. Superior execution on the parts that can't be automated: talking to customers, understanding their problems, iterating based on feedback.

Start making this shift now while you still have time. If you're a senior developer, spend more time with your product team. Sit in on user interviews. Understand the business metrics that actually matter. Learn why certain features get prioritized and others don't.

If you're leading a team, stop hiring purely for coding skills. Look for people who can think about systems holistically, who can communicate clearly with non-technical stakeholders, who have strong opinions about user experience. The developers who thrive will be the ones who can bridge technical possibilities with business needs.

The transition is already happening. The question is whether you'll adapt proactively or get caught off guard when your current skills become less relevant.

[](https://www.xipu.li/posts/the-last-programmers#the-last-generation)The Last Generation
-----------------------------------------------------------------------------------------

We're the last generation of people who translate ideas into code by hand. Our children will describe what they want and watch it appear on screen, the same way we describe what we want to search engines and watch results appear.

They'll judge us the way we judge people who manually calculated ledgers before spreadsheets existed. Impressive dedication to craft, but ultimately unnecessary effort spent on problems that got solved by better tools.

The question isn't whether this future arrives. Looking at the money and talent flowing into AI development, it's inevitable. The question is whether you'll be ready when it does, and whether you'll be working on the parts of product development that actually matter in that world.

The parts that have always mattered, really. Understanding people. Building things they want. Getting those things in front of them. Everything else was just implementation details.