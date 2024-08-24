Title: Tacit Knowledge is Dangerous

URL Source: https://er4hn.info/blog/2023.08.26-tacit-knowledge-dangerous/

Published Time: 2023-08-26T00:00:00Z

Markdown Content:
Update 2023-12-16
-----------------

Hello readers, some minor clarifications to this post. On 2023-12-12 I made it to the front page of Hacker News! As is tradition this made many people upset and and has been widely regarded as a bad move. I want to add a few notes based on feedback I got in: [https://news.ycombinator.com/item?id=38614195](https://news.ycombinator.com/item?id=38614195).

*   The author confused Tacit Knowledge with Tribal Knowledge, they are different things!
    *   Okay, it’s fair that they are defined differently. I will accept that Tacit knowledge is considered knowledge gained through experience, whereas Tribal Knowledge is information not written down that people keep in their heads. However I do not feel that means that Tacit Knowledge cannot be written down nor is it worthwhile to write down what you know. Saying that something is only learnable through experience and cannot be written down means that the ideas can never be challenged nor explained. “We will use the database with these settings because I have 10 years of database experience” is not testable. Saying “We use the database with these settings because it meets these performance criteria and avoids issues with X” allows for testing, shares experience, and opens the door to opportunities for improvement.
*   It takes too long to write down documentation!
    *   If your work becomes important enough it will take longer to explain it over and over.
*   You can’t possibly document everything!
    *   I agree, but you can try your best to capture everything that seems important or reoccurring.

I’ve decided to capture these points rather than re-write my post to acknowledge that they are valuable, but since I object to them, I’m not going to change the original content.

Original Post
-------------

Tacit knowledge, often called “tribal knowledge” in tech, is prevalent in this industry. Documentation is a common afterthought and is frequently wrong, out of date, or lacking crucial information. New hires join a company and go through onboarding exercises intended to have them learn by doing. Often that learning means asking others when they get stuck. It becomes natural for an engineer to end up having key information in their head. When others need it, the engineer freely shares it. Until, the inevitable happens.

![Image 1: Colleague out of office](https://er4hn.info/blog/2023.08.26-tacit-knowledge-dangerous/out_of_office.png)

> You need to know something not written down. You won’t be able to get an answer for a long time from the person who knows it best.

The person who knows what you need is not there. Maybe they left the company, maybe they are on vacation. You may really need to know about the whizbang service, but it’s been 4 years since anyone last worked on it and no-one remembers how it works. You’ve now fallen into the trap of tacit knowledge.

It’s easy, even efficient, to rely on tacit knowledge early on. It is often called tribal knowledge because it’s shared by people close to you, the proverbial tribe. This passing on of knowledge helps bond junior and senior members. The tribe passes this knowledge from seniors to juniors via rituals of song and dance. These songs will take form of video calls, ☕chats, instant message exchanges. Dances transmit information by moving the hand to ctrl+c from a notebook of useful commands, and pressing ctrl+v to send to a colleague. Other more advanced dances involve connecting to a colleagues machine to fix an issue or show a manual setup process that isn’t written down. These song and dance routines will hit their limit at some point.

![Image 2: Relative time scales for learning](https://er4hn.info/blog/2023.08.26-tacit-knowledge-dangerous/graph_relative_time.png)

> Graph showing relative time scales for different ways of learning something at work.

Where sharing tribal knowledge breaks down is at scale. It’s faster to shoot someone who knows the answer a message than to read the documentation, but only if that wise sage can respond quickly. If the holder of the knowledge is busy, in another timezone and you missed the end of their day, or are on vacation, you are out of luck until they return. The timezone problem is particularly painful. 3:30 pm pacific has 1.5 hours left in the 9 - 5 working day. But if you need help from someone on the east coast of the US, it’s 6:30 pm and they have gone home. That same time is 8 am in Australia, and 4 am in India. If you need help from someone on the other side of the world, you’ll be waiting for a while. This doesn’t even attempt to account for different countries having their own set of national holidays.

As a company scales, reliance on tacit knowledge becomes more of a burden. The amount of time it takes to answer a question is a blocker and needing to ask someone begins to consume more time due to both timezones as well as the busy nature of some senior people.

![Image 3: Graph showing time to get answers](https://er4hn.info/blog/2023.08.26-tacit-knowledge-dangerous/graph_getting_answers.png)

> Graph showing how it takes a long time to get answers when distributed. Asking a fourth question doesn’t even fit on the “large, distributed” row.

The longer it takes to get answers, the longer an engineer is blocked. These blockers begin to act as a drag on the ability of an engineer to be productive, and at scale slows down the company itself. Features took longer to ship, bugs take longer to fix. The company itself becomes less nimble and vulnerable to smaller players. This situation always existed, but was exacerbated by COVID and the rise of remote work. Coworkers that used to sit next to each other would now work from home. People moved to different cities, and sometimes moved across timezones. How then, can one try to regain productivity?

![Image 4: Having docs and videos is the middle ground of scaling](https://er4hn.info/blog/2023.08.26-tacit-knowledge-dangerous/scaling_middle_ground.png)

> Graph showing how reading docs and watching videos is still slower than asking people who know (and can respond quickly) but far faster than waiting for large, distributed teams to reply to you.

The answer lies in the original chart: As teams scale up and knowledge becomes more distributed, it is faster to read documentation and watch video lectures than it is to ask others for help. Personally, I am an avid reader and prefer reading (and grepping) for what I need to know. Others learn topics better through video lectures and that is fine. Both have a place, but documentation should always be there because it is easily searchable and easy to reference. By investing the time to create a library of information, both written and video, a middle ground is reached. It will never have that small co-located team efficiency, but it will scale far better than anything relying on tacit knowledge.

For those who need help in getting started with writing documentation, a previous blog post of mine discusses that as well. [Good Docs Take Great Effort](https://er4hn.info/blog/2023.07.22-good_docs_great_effort/index.md) is where I would suggest anyone start when they need to figure out how to write documentation or see where they may improve.
