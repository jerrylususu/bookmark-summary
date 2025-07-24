Title: Developing our position on AI - Blog - Recurse Center

URL Source: https://www.recurse.com/blog/191-developing-our-position-on-ai

Markdown Content:
**If you’re not familiar with us,** RC is a 6 or 12 week retreat for programmers, with an integrated recruiting agency. Ours is a special kind of learning environment, where programmers of all stripes grow by following their curiosity and building things that are exciting and important to them. There are no teachers or curricula. We make money by [recruiting for tech companies](https://www.recurse.com/hire), primarily early-stage startups.

This post started as a question: How should RC respond to AI? Regardless of whether you think large language models present a big opportunity, a looming threat, or something in between, we can likely agree that AI is everywhere, especially in the world of programming, and almost impossible to ignore.

As operators of a programming retreat and recruiting agency, we’ve found ourselves grappling with many of the questions AI raises: What does the existence of code generation tools mean for the craft of programming? In what ways do language models help or harm our ability to learn? Which skills do these tools make less important, and which ones do they make _more_ important? What impact has the proliferation of coding agents and other LLM-powered tools had on software engineering jobs today, and what impact might it have in the coming years?

Our interest in these questions is not academic; it’s practical. AI has popped up in every aspect of our work, from our admissions process (_should we let applicants use Cursor?[1](https://www.recurse.com/blog/191-developing-our-position-on-ai#footnote-p191f1)_) to our retreats (_are AI tools helping or hindering people’s growth?_) to our recruiting business (_what should people focus on to be competitive candidates?_) to community management (_how do we support productive discussion when people have such strong feelings and divergent views?_).

There are no simple answers to these questions. Nevertheless, I think it’s important that we at RC have a thoughtful perspective on AI; this post is about how we’ve tried to develop one.[2](https://www.recurse.com/blog/191-developing-our-position-on-ai#footnote-p191f2)

Our approach
------------

We chose at the outset to limit our focus to the personal and professional implications of LLMs on Recursers, since that’s what we’re knowledgeable about. You won’t find positions or pontification in this post on energy usage, misinformation, industry disruption, centralization of power, existential risk, the potential for job displacement, or responsible training data.

That’s not because we don’t think discussion of any of these issues has merit (it does) but because we think it best to remain focused on the areas closest to our expertise and that are core to our business, and to avoid those that are more inherently political.[3](https://www.recurse.com/blog/191-developing-our-position-on-ai#footnote-p191f3) While the broader societal questions are still being debated, every programmer here has to answer the question of whether and how best to use LLMs in their work during their time at RC.[4](https://www.recurse.com/blog/191-developing-our-position-on-ai#footnote-p191f4)

Our greatest asset is our community. With nearly 3,000 alums, we have easy and direct access to programmers of all stripes, with deep expertise and unique perspectives, from industry to academia. So we started this work by assembling an informal AI advisory group of alums who embody our most important educational values: curiosity, volition, rigor, kindness, learning by doing, and a growth mindset. We sought diversity among not only demographics (age, race, and gender), but also role type, industry, seniority, how recently they attended RC, and most importantly, their views on AI.[5](https://www.recurse.com/blog/191-developing-our-position-on-ai#footnote-p191f5) For the latter, in several cases we were surprised to find people either more or less skeptical of AI than we had originally assumed. In all cases we were pleased to find people’s views thoughtful, nuanced, and more complex than the dominant discourse online.[6](https://www.recurse.com/blog/191-developing-our-position-on-ai#footnote-p191f6)

What we’ve learned from talking with our alums
----------------------------------------------

**Thoughtful, extremely capable programmers disagree on what models can do today, and whether or not they’re currently useful.** On the same day we spoke with an experienced programmer who found existing LLMs to be fairly unhelpful and expected little to change about day-to-day software engineering in the next few years, we met with another who said that LLMs had already dramatically transformed his workflow, which now consisted primarily of reviewing pull requests from a combination of Claude Code agents and non-technical colleagues who were now using LLMs to build features for his company. A third alum we spoke with that day now largely programs _by voice_ using Claude (for the curious, here’s [a video of her process](https://www.youtube.com/watch?v=WcpfyZ1yQRA)).

Still others described having tried the latest models only to find them “extremely confident and almost always wrong.” I expected to find vastly differing views of what future developments might look like, but I was surprised at just how much our alums differed in their assessment of where things are _today_.

We found at least three factors that help explain this discrepancy. First was the duration, depth, and recency of experience with LLMs; the less people had worked with them and the longer ago they had done so, the more likely they were to see little value in them (to be clear, “long ago” here may mean a matter of just a few months). But this certainly didn’t explain _all_ of the discrepancy: The second factor was the _type of programming work people cared about._ By this we mean things like the ergonomics of your language, whether the task you’re doing is represented in model training data, and the amount of boilerplate involved. Programmers working on web apps, data visualization, and scripts in Python, TypeScript, and Go were much more likely to see significant value in LLMs, while others doing systems programming in C, working on carbon capture, or doing novel ML research were less likely to find them helpful. The third factor was whether people were doing smaller, more greenfield work (either alone or on small teams), or on large existing codebases (especially at large organizations). People were much more likely to see utility in today’s models for the former than the latter.

**Recursers have mixed opinions about learning with AI.** There was a little more consistency with how people thought about LLMs in the context of learning. Here, most people saw both real opportunities and pitfalls.

One idea we heard multiple times was that of [turning off the LLM](https://cthulahoops.org/sometimes-turn-off-the-llm) when people really wanted something to stick. One particularly enthusiastic user of LLMs described having two modes: “shipping mode” and “learning mode,” with the former relying heavily on models and the latter involving no LLMs, at least for code generation. Or, as another alum who’s very skeptical of LLMs put it:

> I think a useful analogy would be to compare LLMs to e-bikes. If your goal is to get somewhere quickly, an e-bike is definitely advantageous compared to a bike with no e-assist. If your goal is to become a better / stronger cyclist, an e-bike isn’t really going to help you with that.
> 
> 
> [It’s similar] with AI tools / LLMs. They can let you explore more at a faster pace and get you places faster. This can be really helpful for familiarizing yourself with topics or concepts or doing exploratory research. And if your goal is just to produce code, they will definitely speed that up. But if your goal is to engage with the work of programming on a deeper level, which I think is essential to become a better programmer, the more you rely on them the more you rob yourself of the benefits accrued through engaging with the process.

Or as an alum who helped launch ChatGPT put it:

> LLMs can be the most amazing tool for learning humankind has ever created, or you can rely on it to do your work for you and then your learning will atrophy.
> 
> 
> It’s a next token predictor, and you can use those next tokens to do your work and bypass the learning process, or you can use those tokens to empower you as a programmer and supercharge your learning. I use it to teach me stuff, so that _I_ can go and do it.

Another alum who doesn’t use LLMs or AI tools pointed out that smoothing over all the difficulty of learning something probably isn’t desirable:

> Some amount of friction in the process of learning is important to polishing the technique that you produce. But that doesn’t mean it has to be some kind of masochistic process.
> 
> 
> How we use LLMs to learn still needs to be established — is it eliminating necessary or unnecessary friction?

For learning new things, alums were more likely to see LLMs as useful tutors or rubber ducks. One alum, who helped train foundational models and now works as a Research Scientist, shared that while she didn’t use LLMs much for writing code, she found them very helpful when exploring a new programming domain, so long as she was confident it was well represented in the training data. This is because LLMs allow her to ask as many “extremely dumb questions” as she wants without guilt to quickly bootstrap herself in a new area. Still, she said she keeps [this tweet](https://x.com/shutupmikeginn/status/1898198950349353154) in mind as a check on over-reliance.

Another Recurser shared a similar use case. She had minored in CS before spending many years in data analytics, and returned to work as a software engineer two years ago. She was working remotely, hadn’t programmed recently, and didn’t have nearby teammates to rely on. So, she used ChatGPT essentially as a personalized tutor to get back up to speed. She described having it write code samples for her, and then asking it to explain each line and why it made different choices. She especially appreciated how it completely removed barriers to asking questions, and worries about looking “dumb” or taking up someone’s time. Her takeaway was that LLMs were a huge accelerant to her learning.

Nobody was confident about how people should use AI to learn their _first_ programming language. The overwhelming majority of alums in our advisory group were capable programmers before ChatGPT became a household name, and were anywhere from a few years to a few decades into programming before “agentic coding” became a meme. As such, none had experience using LLMs to learn to program, but some still shared thoughts about the tradeoffs, opportunities, and challenges new programmers might face using LLMs.

The idea that new programmers should avoid using LLMs came up several times, but always with caveats and more questions than conclusions. One alum, who was thankful she already knew how to program before LLMs exploded and worried about new programmers’ over-reliance on AI, _also_ saw its great value for learning, and made an analogy to Google:

> I learned to program before Google existed, and so I was truly helpless then. I didn’t know any programmers, so all I could do was look in books and just feel confused. Google was a tremendous relief — it didn’t have everything, but at least more questions were answered. And so I guess I might feel the same way about AI as I did Google if I didn’t know that much about programming yet.

**Several alums highlighted notable social implications and ways LLMs can impact collaboration at RC.** One alum shared that she found LLMs made certain types of pairing much easier. In particular, they were helpful when pairing on languages or stacks she wasn’t familiar with, since the LLM could handle the syntax. This freed her and her pairing partner to focus on higher-level design questions.

Others worried that LLMs’ ability to patiently answer questions might discourage people from turning to other Recursers. At RC, where everyone is focused on learning rather than deadlines, asking questions often benefits both people involved. As one alum put it:

> When interacting with another person at RC it’s likely the case that both people benefit from the time spent together, maybe not always equally, but I think the sum is greater than the parts. I think when interacting with an LLM, depending on how they’re used, one person can scratch some social itch, and they might benefit from it, but the energy goes kind of into a technological void, instead of into the community where it benefits others.

**Many alums have changed their minds, and expect to change them again.** We’ve all seen how tribal AI has become (especially online), with people quickly labeling each other as either AI boosters or haters. Given that, we were particularly heartened by how nuanced most of the RC alums we spoke with were in how they are thinking about AI. Many shared their views with significant humility, in part because they said they had already changed their minds on some aspects of AI, and expect to do so again. Several alums more skeptical of AI reported that they made a point of periodically testing new tools, to see how they had improved (or not).

The importance of being open to change was another notable point of agreement among alums with very different views on LLMs. One alum, who’s very much embraced programming with LLMs, said she thought her willingness to change and adopt new workflows was one of her biggest strengths. Another alum, who avoids LLMs and has been in the industry since the 90s, said bluntly:

> No one survives being a professional programmer without being willing to learn a whole bunch of new things every couple of years. The people who don’t flee into management as soon as they can.

**Everyone agreed that it’s still important to understand what you’re building**. The most consistent theme we heard from our alums — regardless of their views on AI — was the importance of understanding and critically engaging with what you build and the systems you’re working with.

From one alum who now mostly programs at work using Claude Code:

> I think that mental models of systems are as valuable as ever. Things like knowing how an operating system works, knowing how the Internet works, knowing about recommendation algorithms or audio codecs … having more of these [deep domains] in your head that you can understand and reason about is as important as it’s ever been and more.

Or as an extremely experienced systems programmer who does _not_ use LLMs at all in his programming put it:

> One of the fundamentals of programming is being able to shift back and forth between a bunch of different layers of abstraction and understand a system at [many] levels.
> 
> 
> Everything I’ve seen about LLMs is that they are not able to do this yet, and may never be able to do this, at least not to the degree of fluidity of a really good programmer.

Even the alums with the deepest skepticism of LLMs saw the key factor being about _how_ people who use models choose to use them:

> I don’t worry about the people using these tools and challenging them, and as part of their process going into the code and confirming for themselves what is really happening. But I do worry about people who won’t expend that effort.

That ability to “expend effort” is an expression of will — an act of volition. Alums emphasized not only the importance of expressing our wills, regardless of the tools we use, but also the importance of our ability to make our own judgements:

> I think one of the strongest signals [of who’s a good programmer now] is people who actually know how to say no, because AI will always allow you to have a yes, but the yes will often be a lie. And so somebody who will go, “these numbers seem off,” is really useful.

Whether you call this good judgement, discernment, or taste, we think it’s one of the most important abilities you can develop, not only as a programmer but as a person. How do you develop good judgement and taste? We think you start by learning to direct yourself, which brings us back to the purpose of RC.

Why we run RC
-------------

My cofounders and I started RC in 2011. Fourteen years later, I’m as dedicated to RC as ever because it is the ultimate reflection of my own values and beliefs. As a lifelong unschooler, I believe people learn best when given the freedom to explore their interests deeply, guided by their curiosity and powered by their intrinsic motivation. This is why RC is based firstly on self-direction, and why our mission is to transform lives by helping people direct themselves.

RC’s focus on programming reflects my own love of technology. Growing up in the 90s, I could lose myself in the computer for days. BASIC. HyperCard. NetBSD. C. The Internet. These and so many others presented new systems to understand, new worlds to explore. The potential felt, and still feels, limitless.

The greatest accelerant to my learning was finding kindred spirits. That is, other people who shared my interests and passions, who I could work alongside and with, and who could expose me to things I didn’t know existed. This is why RC is community-driven, and why we frequently say that the people are the most valuable part of RC.

Regardless of what the future brings, these things will remain true about RC.

Our position on AI
------------------

As I reflected on what our alums had shared, I found myself repeatedly coming back to the words of John Holt, the father of unschooling, which is the educational philosophy that RC is based on:

> I doubt very much if it is possible to teach anyone to understand anything, that is to say, to see how various parts of it relate to all the other parts, to have a model of the structure in one’s mind. We can give other people names, and lists, but we cannot give them our mental structures; they must build their own. — John Holt

That is to say: tutorials and teachers can only get you so far. Ultimately, you must build your own mental structures. Stack Overflow can be a helpful resource, but blindly following or copy-pasting from it does little to help you learn. While you can get a lot farther mindlessly using LLMs than Stack Overflow, the same principle holds true.

> Learning is not the product of teaching. Learning is the product of the activity of learners. — John Holt

You must be actively, intellectually engaged in your work and learning for it to represent real growth rather than regurgitation. You can no sooner learn a hard skill like programming by passively consuming LLM output than you can by merely listening to a teacher talk. As Holt put it: **“We learn to do something by doing it. There is no other way.”**

We hear these truths echoed in how Recursers talk about programming and learning with AI. And they’re the foundation of our three [self-directives](https://www.recurse.com/self-directives), our guiding principles for how people grow at RC. Together, they help us frame our view on how AI fits into learning and programming.

The first self-directive is to _work at the edge of your abilities._ Real growth happens at the boundary of what you can do and what you can almost do. Used well, LLMs can help you more quickly find or even expand your edge, but they risk creating a gap between the edge of what you can produce and what you can understand.

**RC is a place for rigor.** You should strive to be more rigorous, not less, when using AI-powered tools to learn, though exactly what you need to be rigorous about is likely different when using them.

You learn best and most effectively when you are learning something that you care about. Your work becomes meaningful and something you can be proud of only when you have chosen it for yourself. This is why our second self-directive is to _build your volitional muscles._ Your volition is your ability to make decisions and act on them. To set your own goals, choose your own path, and decide what matters to you. Like physical muscles, you build your volitional muscles by exercising them, and in doing so you can increase your sense of what’s possible.

LLMs are good at giving fast answers. They’re not good at knowing what questions you care about, or which answers are meaningful. Only you can do that. **You should use AI-powered tools to complement or increase your agency, not replace it.**

The primary value of RC is the people, which is why our third self-directive is to _learn generously_. Learning generously is what makes RC a community. We celebrate each other’s successes, support each other when we struggle, and benefit from each other’s knowledge.

Learning generously with AI means being open about what you’re trying, what’s worked, and what hasn’t. And it means making space for respectful disagreement and exploration, especially now, when people’s experiences with and views on these tools vary so widely, and when the discourse on AI in the rest of the world is so charged. Whether you’re experimenting with totally new workflows, avoiding AI, or somewhere in between, **learning generously means being open to different perspectives, without judgement or dogma.** RC has always been an opportunity to learn from others with different backgrounds, skills, and interests. We encourage everyone here to be curious about one another, and to work with someone whose tooling or usage differs from their own.

And remember, asking questions doesn’t just help you. At RC, it often helps the person you’re asking, too.

In short, whether you choose to embrace or avoid AI in your work at RC, you will need to build your own mental structures to grow as a programmer. When using AI, use it to amplify your ambitions, not to abdicate your agency. And regardless of what you do, be curious about and kind to the people around you.

_Acknowledgments_

_Thank you to my colleagues (especially Emily Bernier and Rachel Petacat) for collaborating on this work, and to the more than a dozen alums who volunteered their time and shared their experience as part of our advisory group. Thanks also to the many other Recursers who shared their experiences through informal chats and writing._

1.   For more on this, see our recently updated [guidance for our pairing interview](https://www.recurse.com/apply#sec-pairing-ai).[↩](https://www.recurse.com/blog/191-developing-our-position-on-ai#footnote-return-p191f1)

2.   My colleagues Emily Bernier and Rachel Petacat and I collaborated on this work. When I write “we,” I’m referring to the work the three of us did and/or writing on behalf of RC. I use “I” here when writing about my own thoughts and experience, and to sound less like a corporate drone.[↩](https://www.recurse.com/blog/191-developing-our-position-on-ai#footnote-return-p191f2)

3.   We understand the argument that all technology is inherently political, but we do not think that is a useful definition of the word. While reasonable people may disagree, we don’t think grouping CPUs, encryption, and LLMs in the same category as abortion, immigration, and foreign policy makes sense, even though computer chips include precious metals, strong encryption was once classified as a munition, and LLMs were trained on copyrighted material.[↩](https://www.recurse.com/blog/191-developing-our-position-on-ai#footnote-return-p191f3)

4.   Even with that limited focus, the questions loom large, the facts are still changing, and reasonable people can disagree. Bluntly, we don’t think it’s practical or even desirable to seek a definitive set of answers to some of these questions, or to prescribe specific advice without nuanced understanding of individuals’ goals and circumstances. Instead, we seek to examine these questions through the lens of our educational values and mission. We hope to provide clarity wherever we can, and useful guideposts for further exploration, growth, and understanding where straightforward answers aren’t accessible today.[↩](https://www.recurse.com/blog/191-developing-our-position-on-ai#footnote-return-p191f4)

5.   In addition to the alums we asked to join our advisory group, we also had less structured discussions with dozens of current and recent Recursers about their own use (or lack thereof) of AI tools and their thoughts on them. Finally, we read voraciously, from blog posts to academic papers.[↩](https://www.recurse.com/blog/191-developing-our-position-on-ai#footnote-return-p191f5)

6.   While this is no doubt primarily a reflection of our wonderful community, I think it also reflects the benefits of face-to-face conversation compared to social media and online discussion forums. This could and may some day be a whole other blog post.[↩](https://www.recurse.com/blog/191-developing-our-position-on-ai#footnote-return-p191f6)
