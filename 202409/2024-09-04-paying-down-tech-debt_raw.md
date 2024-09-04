Title: Paying down tech debt

URL Source: https://newsletter.pragmaticengineer.com/p/paying-down-tech-debt

Published Time: 2024-09-03T18:56:57+00:00

Markdown Content:
> #### **Q: “I’d like to make a better case for paying down tech debt on my team. What are some proven approaches for this?”**

The tension in finding the right balance between shipping features and paying down accumulated tech debt is as old as software engineering. There’s no one answer on how best to reduce tech debt, and opinion is divided about whether zero tech debt is even a good thing to aim for. But approaches for doing it exist which work well for most teams.

To tackle this eternal topic, I turned to industry veteran [Lou Franco](https://www.linkedin.com/in/loufranco/), who’s been in the software business for over 30 years as an engineer, EM, and executive. He’s also worked at four startups and the companies that later acquired them; most recently Atlassian as a Principal Engineer on the Trello iOS app.

He’s currently an operating partner at private equity firm SilverTree Equity, and technical co-founder at a new startup. Lou says he isn’t delighted about the volume of tech debt accumulated during his career, but is satisfied with how much of it he’s managed to pay down.

In this guest post, Lou shares insights about how to approach tech debt. Later this year, he’s publishing [a book on the subject](https://loufranco.com/tech-debt-book). For updates on this upcoming release, [subscribe here](https://loufranco.com/tech-debt-book).

In this article, we cover:

1.  **Pay down tech debt to go faster, now**. It’s common for less experienced engineering leaders to assume that focusing on features and ignoring tech debt is how to move faster. Lou used to agree, but not any more.
    
2.  **Use tech debt to boost productivity.** Three examples of when tackling tech debt empowered engineering teams to move faster, right away.
    
3.  **Link tech debt and value delivery.** When tech debt is tackled sensibly, it delivers business value. At Trello and Atalasoft, this was how Lou got engineers and management to appreciate the task.
    
4.  **Make tech debt’s effects visible.** Dashboards are an effective way to visualize the impact of tech debt. A few examples.
    
5.  **Factor in time saved when thinking about productivity.** Reducing tech debt typically improves coding, reviewing, and deployment for everyone.
    

_With that, it’s over to Lou:_

What is tech debt?

I define tech debt as any problem in the codebase that affects programmers by making it harder to make necessary changes. As a programmer, I wanted to fix such issues because they slowed me down. But as a manager, I had to ensure the team delivered value to stakeholders. I’ve gone back and forth between these roles during my career, and made mistakes in both directions – but I also learned a lot about getting the balance right.

In 2010, I was head of development at Atalasoft, a company in the .NET developer tools space. I was obsessed with shipping, and spent all my time worrying about delivering the features in our roadmap. Over time, we improved at this, which showed up in our revenue growth and eventually led to an acquisition.

We were in a competitive market with more opportunities than we could handle. We had fewer than ten developers, but we were bootstrapped, so had to stay profitable and couldn’t just hire ahead of revenue.

The stakes got even higher after we were acquired. We had two years to deliver on an ambitious roadmap, for which there was an earnout bonus contingent upon delivery. If we didn’t deliver, we’d likely be classified as a failed acquisition. Our new owners had just had one such failure, which led to downsizing and an office closure.

**My mindset was that any time spent on technical debt meant we’d fail to deliver on the roadmap.** We couldn’t risk the deadline by wasting time cleaning up old messes, and had to choose between tech debt and roadmap delivery. In hindsight, I see this was wrong. I learned that the mindset of ignoring tech debt hurt my team.

Following an exit interview in which a departing engineer mentioned tech debt had contributed to their decision to leave, I started asking people during 1:1s how they felt about it. Their responses showed their frustration with me.

By then, I had been a developer for over fifteen years, and had worked in codebases with a lot of debt, so I knew what it was like. But by now, I was a manager who sometimes contributed code, but had forgotten what it was like to be thwarted by the codebase every day. To my team, I was part of the problem. They had been trying to tell me this, but I didn’t get it. Their departing colleague with nothing to lose in their exit interview finally got through to me and helped me understand the depth of the issue, and that it was slowing everyone down.

**I learned an important lesson: the cost of tech debt is borne daily by your team, and you risk damaging motivation and raising attrition by ignoring it.** Even if you have every reason to move forward without addressing tech debt, being an empathic manager requires you at least do something. Doing nothing – like I did – is not a good option.

So we started making changes. The biggest problems were with our build system and installer because they affected every developer and every product. It was a tangled bag of legacy code that needed constant maintenance, but it wasn’t very big, and I approved a plan to rewrite it with modern tools. It was a small experiment but paid off right away in quicker CI builds and an easier-to-modify codebase. Most importantly, I saw it didn’t derail our roadmap, so we took on other small initiatives.

This taught me another lesson about addressing technical debt. I had thought of it as something that might pay off in the long run. _Might_. This belief made it hard to justify doing it when I had to deliver on short-term goals. But instead, something else happened:

**We paid off tech debt and increased productivity instantly!** We had a build with faster feedback loops, less cognitive load, and which didn’t make developers frustrated when they had to add to it, which happened regularly. Updates were made with less code and without breaking things. It was an example of tech debt reduction paying off in increased developer productivity, right away.

I got my next lesson at Trello where I worked on the iOS app. The codebase was three years old when I joined in 2014. It had understandable tech debt because they needed to move fast, after going from 0 to 6 million sign ups. The devs working on it were founding engineers, working as described by _The Pragmatic Engineer_ in _[Thriving as a Founding Engineer](https://newsletter.pragmaticengineer.com/p/thriving-as-a-founding-engineer)_, and seeking product-market fit. Our biggest tech debt issue were some frameworks that made it fast to build a simple app, but held us back as the app got more complex.

Our own choices were influenced by the speed of Apple’s updates to iOS. The iOS 7 update completely changed the iOS design language and its network APIs. Later, iOS 8 introduced presentation controllers that gave developers much control over the animation when new views are shown. Unfortunately, the iOS 8 change broke our navigation code and caused crashes. These added up and started to make our code seem antiquated.

[![Image 1](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F21fc82f0-527d-4dfa-84ea-dd68a15a1b85_1208x1052.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F21fc82f0-527d-4dfa-84ea-dd68a15a1b85_1208x1052.png)

Left: how most iOS 6 apps looked like. Right: the iOS 7 version. iOS 7 introduced a ‘flatter’ look, and required lots of code changes to implement this new UI. Screenshot is from my app called Habits

Our code got even more complex when Apple decided to feature Trello on physical iPhones at Apple Stores. To be in stores, we needed a build that worked without an account or a network, so a mock backend was embedded in it for demo purposes. We didn’t want to maintain a separate codebase, so had a lot of random bits of demo-mode logic that stayed for years.

At Trello, I was coding every day and all this was in my face. Luckily, we were a small team of three developers, so my direct manager was also coding every day and was empathetic to the problems.

**We did rewrites as we went, but sometimes went too far.** To deal with the presentation controller problem of iOS 8, we developed a new paradigm for screen navigation inside the app, and rewrote all navigation to use it. This approach was the exact opposite of what I did at Atalasoft, where I’d ignored all tech debt.

Unfortunately, the approach of rewriting early turned out to be overkill. In hindsight, we could have just corrected the places that had crashed, and then lived with the code we had. Instead, we spent a few months designing and implementing a new, non-standard way of writing navigation code, but forgot a vital lesson that one of our founders, Joel Spolsky, identified in 2000 in [Things You Should Never Do](https://www.joelonsoftware.com/2000/04/06/things-you-should-never-do-part-i/):

> “We’re programmers. Programmers are, in their hearts, architects, and the first thing they want to do when they get to a site is to bulldoze the place flat and build something grand. We’re not excited by incremental renovation: tinkering, improving, planting flower beds.
> 
> There’s a subtle reason that programmers always want to throw away the code and start over. The reason is that they think the old code is a mess. And here is the interesting observation: they are probably wrong. The reason that they think the old code is a mess is because of a cardinal, fundamental law of programming:
> 
> It’s harder to read code than to write it.”

On the Trello engineering team, we were all very familiar with this article and quoted it to each other often, but it still sometimes bit us. The urge to rewrite a system instead of fixing it is strong, and we couldn’t resist! We should have addressed the few complex navigation cases that crashed our code without the full rewrite.

**Size tech debt payment to be proportional to value.** This is the biggest lesson I learned on this project.

I’ve seen both extremes of dealing with tech debt:

*   As a manager, I was overly resistant to devoting time to dealing with technical debt
    
*   As an engineer, I was exposed to its problems every day and didn’t resist the urge to pay it off enough
    

These two extremes form the fundamental tension of dealing with tech debt. As usual, there needs to be a balance, but finding it is not so easy.

**The heuristic I use to pay tech debt these days is this:** by reducing a specific tech debt, can I increase developer productivity and deliver business value _right now?_

If I can’t, then I don’t pay it down.

When the debt is so big that it couldn’t possibly deliver value now, or the value is invisible so nobody sees it, I do something else. Let me break down my heuristic…

I try to pay down a little bit of tech debt regularly by making small cleanup commits as I go. I started doing this more intentionally after reading Kent Beck’s book, _Extreme Programming Explained,_ in 1999, which introduced me to automated unit tests and continuous integration. Then, when I read Martin Fowler’s _Refactoring_, I started to see how to improve a codebase over time with very small, behavior-preserving changes checked by unit tests. In both books, and in others like _Working Effectively with Legacy Code_ by Michael Feathers, and Kent Beck’s recent, _[Tidy First?](https://newsletter.pragmaticengineer.com/p/dead-code-getting-untangled-and-coupling)_, the authors stress that technical debt is inevitable, and that the main way to curtail it is to be constantly fixing it with small improvements enabled by unit tests and mechanical refactoring. I agree.

**Unit tests, refactoring, and continuous integration are ubiquitous in the kinds of software I write,** which are B2B SaaS productivity applications. Even making small improvements on an ongoing basis is common among my coworkers. It doesn’t take long, and there are usually quick wins to be had, like making the code more readable, or using a unit test to show how the code is supposed to work. Even in frontend code, Trello iOS adopted Model-View-ViewModel (MVVM) so we could test view-logic. We got the immediate productivity benefit of being able to run view code repeatedly without needing to manipulate a running app through several screens to check that our changes worked.

The issue is when the debt is large, which is where I struggled. My problem at Atalasoft was not with small improvements; it was with the bigger ones where I’d have to trade off current benefits like delivering features for the roadmap, for uncertain future benefits.

But I realized something.

You can get productivity benefits immediately, even with larger initiatives. If you do it right, you will deliver feature work faster and with higher quality. In fact, I view tech debt proposals that don’t deliver instant developer productivity gains as suspect.

**Rewriting the build and installer at Atalasoft brought an immediate productivity boost.** We had a backlog of problems and new additions, but the rewrite took one developer around a month, and when it was done many of the problems just went away because the new system was based on a framework wherein many problems could not occur, meaning we could close a bunch of reported bugs. The new system was unit testable, so we didn’t need to build and install the entire system during development to test our new changes while we were writing it. We also got more benefits later, but the instant benefits justified it.

**At Trello, adding unit tests to a codebase helped me finish a project faster.** When I joined in 2014, we were just about to start our internationalization (i18n) project, which I took on for the iOS app. One part was to write support for i18n-safe string interpolation (inserting variables or expressions into a string,) and pluralization (adjusting words to plural forms based on the number they refer to, to make the phrases grammatically correct) – which was only partially supported in iOS at the time. It’s standard string manipulation at its core, but in 2014 our iOS app didn’t have unit tests.

Without unit tests, if I had wanted to run the code, I’d need to run the app and then tap-tap-tap until I got to a specific string. I would have to do this for each kind of string I generated. But with unit-tests, I could just list all the examples with their expected results, and run tests in less than a second. So, I proposed to the team to add unit tests to our build and CI.

No one was against unit tests, but it hadn’t been a priority. Most of the code was UI or network code, for which unit tests are harder to write. But the code I was writing was highly testable, and in fact, it’s harder to write without tests. So, I added the unit test project to our workspace and wrote the string code. With the unit test project there, the other developers added tests to their work. I was there for six more years, and saw the benefits of the tests over time, especially in complex code like our sync engine. But that’s not why I did it: I added the unit tests to go faster immediately.

**Also at Trello, creating an abstraction layer for the design system made us more productive.** Eventually, we created a design system with a reduced set of fonts, colors, and other design attributes and specific rules for using them. Before, it was common to see hardcoded values in view controllers throughout the app, as each screen implemented the designer’s specification for that screen, which wasn’t always consistent. We could have just updated those lines to the new approved values, but it was the perfect time to make an abstraction for the design system itself. Doing this made it faster to write code that matched a design, and when a default in the design system changed, it would be reflected everywhere.

These three examples also adhere to another heuristic I use for finding the right balance with tech debt: coupling it with delivery of value.
