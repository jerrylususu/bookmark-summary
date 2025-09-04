Title: Documents: The architect’s programming language

URL Source: https://stackoverflow.blog/2025/08/20/documents-the-architect-s-programming-language/

Markdown Content:
From junior developer to senior/principal, career paths are typically straightforward. The better you get at coding, and at the technical and non-technical skills that enable you to code more effectively, the faster you’ll advance. But once you hit senior, there’s a major fork in the road.

Many developers take the management track. It’s a great way to expand your influence and move up the ladder. But one downside is you’ll inevitably spend less time programming—a lot of engineering managers don’t get time to code at all—and if you’re like me, that’s a deal breaker. The time you used to spend heads-down, translating tricky processes into beautiful abstractions, will instead be spent in meetings, removing roadblocks for your team, mediating disagreements, and checking boxes for HR. It’s challenging and important work, but it’s very different.

The other common option is the architect track. This lets you stay knee-deep in code while increasing your impact and leveraging your tenure. At many companies, the architect track has similar compensation and job title advancement opportunities to the management track, and either one can lead to a C-suite role (like CTO).

But the architect track may seem poorly-defined by comparison. When you move into people management, your day-to-day work changes completely. Your schedule changes, your team structure changes—your work output is measured in a totally different way. But being an architect looks a lot like being a senior developer: writing code in an IDE, reviewing pull requests, talking about things like deployment pipelines and data structures. So what makes an architect different? Or in other words, if you want to [prove you’re ready for an architect role](https://stackoverflow.blog/2022/06/29/skilling-up-to-architect-what-you-need-to-land-high-paying-it-roles/), how do you do it?

It’s not just about being knowledgeable or smart. That’s how you got to where you are. And it’s not just about shipping resilient and well-designed systems, though that’s important too.

In my opinion, the difference comes down to one main thing:

*   Senior developers know how to deploy code to systems made of code.
*   Architects know how to deploy ideas to systems made of people.

This may sound like an empty metaphor. I promise it isn’t.

To clarify: I don’t just mean that architects are good communicators or that they work well with others, though both things matter. Nor is this my flowery way of saying soft skills are important, though they are. I mean that **an architect knows effective, repeatable processes for organizing and deploying _ideas_**, above and beyond the processes that organize and deploy machines and applications. They know there are limits to what you can achieve with a code push; the most important issues require input, collaboration, and consensus from people with different perspectives and job titles.

In other words, most engineers at most companies can’t kick off a multi-month project, rewrite a web service, or choose the programming language for a new product without buy-in from multiple other developers and leaders. The biggest bottlenecks in the software lifecycle have nothing to do with code. They’re people problems: communication, persuasion, decision-making.

So in order to make an impact, architects have to consistently make those things happen, sprint after sprint, quarter after quarter. How do you reliably get the right people in the right place, at the right time, talking about the right things? Is there a transfer protocol or infrastructure-as-code tool that works on human beings?

As it happens, yes.

There are several tools, actually: Confluence, Google Docs, Notion, XWiki, BookStack…you get the idea. If you can write bullet points and link between documents, you can deploy ideas. The most effective way to get something done in most organizations is to write a document, share it with the people most likely to care, and listen to their feedback.

A lot of programmers don’t feel confident in their writing skills, though. It’s hard to switch from something you’re experienced at, where quality speaks for itself (programming) to something you’re unfamiliar with, where quality depends on the reader’s judgment (writing). So what follows is a crash course: just enough information to help you confidently write good (even great) documents, no matter who you are. You don’t have to have an English degree, or know how to spell “idempotent,” or even write in your native language. You just have to learn a few techniques.

This is my manifesto on documentation.

> As a documentation geek, I’ve come to value:

> JOTTING THINGS DOWN over worrying about how to structure them

> A CULTURE OF DOCUMENTATION over box-checking behavior

> THINKING ABOUT WHAT’S RELEVANT over using a template

> POINT-IN-TIME DOCUMENTATION over constant updates

This is intentionally similar to the Agile manifesto. The items on the right have value, but the ones on the left are more important.

I’ll go into greater detail on some of these points later on, including ideas about how to structure different types of documents, but keep in mind the first and third points: it’s better to write down what you know than to get stuck figuring out the right format. And the format doesn’t even need to be the same from one document to the next. Focus on what works for the information you’re presenting right now, not what’s worked before.

Even if you don’t have a lot of practice with technical writing, you can still write excellent documentation. There’s one simple yet ridiculously effective hack that will improve practically any document you write: **bullet points**.

Bullet points are magical. They put you in a mindset of completeness and structure, rather than sentence flow and style. People reading a technical document are trying to find information quickly—in fact, one of the best metrics for documentation is how fast people stop reading it. If they find what they need in ten seconds and leave, that’s a win. And since bullet points tend to be information-dense and easy to skim, they’re the perfect tool for the job.

Here are the last two paragraphs as bullet points:

*   Bullet points are good for technical writing
    *   Help you focus on completeness and structure
    *   Don’t require as much writing skill
    *   Make documents easier to skim

That’s almost 100% of the same information in 25% of the page space. It was easier to write, too. That’s why bullet points are an architect’s best friend.

The second most valuable technique you can use is **headers**. Unless your information can be expressed in very few bullet points, it’s worth breaking it into sections with meaningful titles.

For example, most of the documents I write start with a “Context” section. Its purpose is to provide information and links about the history, business domain, or predetermined constraints of a topic. You might know all that information offhand, since you’re actively working on it from day to day, but other readers will appreciate the memory jog. And in a year when you refer back to your own document, you’ll appreciate it too.

Of course, people who already have a deep understanding of the topic at hand can skim or skip the Context section. That’s the great thing about headers: they make it even easier for someone to find whatever tidbit of information they’re looking for and ignore whatever they aren’t. (If you’ve got more than a handful of headers and want to optimize even further, a linked table of contents is a great addition.)

If you don’t know what headers to use at first, just write bullet points in whatever order comes to mind. Then organize them into logical groups and label them. This isn’t so different from programming: you might write a 200-line method as a first draft, but once you’ve got it working, you usually refactor by breaking it into steps and extracting common patterns into functions.

The main thing you want to avoid is a giant wall of text. Often the people whose attention your document needs most are the people with the most demands on their time. If you send them a four-page essay, there’s a good chance they’ll never have the time to get through it. A well-organized set of bullet points, on the other hand, makes it possible for them to scroll through, glean the information they need, and respond whenever they have a minute to spare.

Once you’ve got all the necessary information written down, consider doing a sanity check. Send it to someone you work closely with and ask them to point out anything that seems wrong or doesn’t make sense. Then use their feedback to clarify, reorganize, or rephrase.

Keep in mind that most documents are more like one-off Bash scripts than living SaaS applications. Once a document has done its job, you probably won’t ever update it again. As an architect, you can easily write a hundred documents a year; you definitely don’t have time to maintain them all.

This has two implications. First, you should make sure each document is good enough to be useful later, even as it gradually goes obsolete. It’s worth putting in some extra effort now so you can forget about it until it comes up again. Second, you should make it easy to tell when the document was originally written, and conversely, easy to find documents that were written around the same time. Point-in-time documentation is a lot more useful when it’s obvious how out-of-date it is.

My approach to this may seem counterintuitive. Most people start out organizing documents according to topic: one folder for this feature, another folder for that one. But this leads to having a bunch of apparently-equal folders that aren’t all equally valuable. Some of them are full of recent, highly-relevant documents; others don’t have any documentation from the last five years; still others have a mix of new and old documents, some of which directly contradict each other, and it’s not immediately clear what order they should be in.

So instead, I organize nearly all documents chronologically: by year and then by sprint. This helps keep the timeline visible. For example, in Confluence, I create a “space” (which other tools may call a “workspace,” “wiki,” or “book”) for each team or product—some high-level logical separation is useful—but within each space, the folder structure looks something like this:

*   📄 Overview
*   📄 Architecture
*   📁 2025
    *   📁 Jan 1 Sprint
        *   📄 Proposal: SSO login
        *   📄 APP-132 Research on user sessions

    *   📁 Jan 15 Sprint
        *   📄 APP-135 Allow SSO login for configured clients

    *   📁 Feb 2 Sprint
        *   📄 Problems with SSO login and user roles
        *   📄 Dev forecast: escalating role-permission complexity

Note that for a small number of high-level documents, continuous maintenance makes sense. If someone’s curious about the product in general, it’s good to have an up-to-date landing page and maybe an architecture diagram. But most documents have a shelf life: they’ll get less and less relevant as time goes on.

You might ask, “Isn’t this the opposite of how people think? I’m usually looking for docs about a specific project or feature, not about what happened in March of 2020.” My answer is, “There’s a search box for that.” Organizing documents by topic is like categorizing jelly beans: no two people can agree on the right way to do it. That means every time you write a document you’ll waste time trying to figure out where it belongs, and every time you go looking for a document you’ll waste time browsing the wrong folder before you find the right one. It’s like organizing CSS properties logically instead of alphabetically: it might feel good to have `left` and `top` on adjacent lines, but it doesn’t actually accomplish anything. For CSS, alphabetical order is faster, simpler, and always good enough. For documents, chronological order wins for the same reasons.

Besides, searching is usually the right move anyway. Browsing is good for discovering what documents exist, but if you’re looking for specific information it’s too easy to overlook documents that have info you need, but whose titles don’t immediately seem relevant. Searching, on the other hand, is fast and turns up everything that matches your search terms. A chronological approach to organization practically forces people to search, which is what they should do. And when they click a search result, they’ll get immediate context about when it was written and what other things were happening at the same time.

Once you’ve got your document peer-reviewed and published, the last step is to grab the link and spread it around. If it overrides or extends another document, update that document with the link. If it’s attached to an issue-tracking ticket, add it there too. And finally, send it to the people whose feedback, approval, or consensus you need.

Following are a few of the most effective types of documents for engineering organizations.

_Purpose:_ To help others quickly get up to speed on the structure and design of a system.

_Audience:_ All stakeholders in a system: managers, developers, operations engineers, product owners, etc.

_When to write one:_ Before you build a new system or restructure an existing one. Also useful when any existing system proves difficult to understand.

_Content:_ Describes the major components of a system (databases, applications, cloud services, load balancers, etc.) and how they communicate with each other. May also describe internal components, like data models and classes, though you should avoid excessive detail.

_Structure:_ May be a diagram with symbols such as cylinders, boxes, and arrows, a multi-page document with sections and subsections, or just a list of nested bullet points. Common formats include [arc42](https://arc42.org/overview) and [C4](https://c4model.com/).

_How it orchestrates ideas:_ An up-to-date architecture overview, or even a somewhat outdated one, can help contributors form a mental model of a system so they can build on, troubleshoot, and reason about it. It also helps leaders and ops engineers understand how to deliver it, what it costs, and how it interacts with existing systems, which is essential to getting it approved in the first place.

_Tips:_ Remember, jotting things down is more important than worrying about how to structure them. Don’t stress about following a strict format or using all the right symbols (unless you want to). An imperfect architecture document that exists is better than a perfect one that doesn’t.

_Purpose:_ To get feedback on code you intend to write; to help you surface unknowns and complications before you write a bunch of half-baked code that ends up getting thrown away.

_Audience:_ Other developers on your team; future developers who want to understand the evolution of a system.

_When to write one:_ Before you start working on any non-trivial coding task. Can also be written after you’ve started working on something that seemed trivial, but is turning out to be more complicated.

_Content:_ The level of detail is up to you. Don’t spell out anything obvious or mundane, but include enough information that other developers can call out incorrect assumptions and recommend existing logic/patterns that you might not have been aware of.

_Structure:_ A list of steps that will be followed. For example, class A will be modified by adding a method that does X, class B will be created to contain data about Y, a database migration will be created that does Z, and so on. You can also include an Open Questions section with anything that needs to be addressed before you can get started, or an Alternative Approaches section with different implementations you’d like your teammates to weigh in on.

_How it orchestrates ideas:_ Dev designs help developers share knowledge and preserve the core patterns and abstractions of a system. They also create a permanent record of how a system came to be the way it is. If your team doesn’t do pair/mob programming, dev designs can give you many of the same benefits while also helping future contributors learn the system.

_Tips:_ This sounds false, but it’s true: the more documentation you write, the less code you have to write. Documentation can help you avoid the types of misunderstandings, incorrect assumptions, and design mistakes that lead to PR back-and-forth and rewrites. It can also help you avoid sinking a lot of time into exploratory coding that won’t lead anywhere.

_Purpose:_ To communicate the value and cost of a project so time and money can be allocated to it.

_Audience:_ Leaders and product owners.

_When to write one:_ When planning meetings are on the horizon, or whenever you see an opportunity to meaningfully improve or expand the company’s products and systems.

_Content:_ Summarizes everything a leader needs to know to evaluate one project’s priority versus another. Why is it important? Who will it affect? How long will it take? And so on.

_Structure:_ A few clearly-labeled sections like Context, Problem to be Solved, Proposed Solution, User Impact, and Estimated Engineering Effort.

_How it orchestrates ideas:_ Project proposals are how big, impactful, months-long undertakings are born. They set the roadmap for entire teams.

_Tips:_ Make your proposal easy to say “yes” to by making it understandable for both technical and non-technical stakeholders. Remember that other people aren’t thinking about what you’re doing all the time, so you need more context than you think. Consider doing some research beforehand, whether that’s data mining to determine how many users would be affected, asking around to find out how frustrating the problem really is, or reading up on how other teams and companies have approached similar projects.

_Purpose:_ To raise the possibility of worse-than-expected outcomes, especially ones that your experience makes you uniquely qualified to foresee, then suggest ways to respond to them.

_Audience:_ The stakeholders of a business decision.

_When to write one:_ When a decision is made that, for you as an engineer, feels risky or likely to disappoint.

_Content:_ Start by summarizing why the decision was made and what goals the decisionmakers hoped to achieve. Explain the factors leading you to believe negative outcomes are likely. Describe what those outcomes are. Then suggest ways to mitigate them, even if the decision ultimately doesn’t change.

_Structure:_ A well-organized document with sections like Decision, Motivations, Issues, Likely Outcomes, and Solutions.

_How it orchestrates ideas:_ A developer forecast helps you share your professional foresight and get people thinking about the pitfalls of a plan. It also prepares the organization to respond quickly and adeptly when something goes wrong, instead of repeatedly painting over the problem. When and if a plan starts to fail, your forecast can become a North Star of sorts, demonstrating the growing contrast between expectations and outcomes.

_Tips:_ Maintain a neutral tone so you don’t sound like a doom-and-gloomer. Consider multiple possibilities and don’t try to turn the whole ship around; just point at the iceberg and suggest ways to handle it.

_Purpose:_ To reduce decision-making time when spinning up a new application.

_Audience:_ A development team or organization.

_When to write one:_ When you’re planning a project and there are differing opinions about what technologies to use.

_Content:_ For a given type of technology (programming languages, runtimes, frameworks, platforms, etc.), focus on the options you and your colleagues favor most. Compare the strengths of each: How familiar is your organization with it (not just building with it, but deploying and maintaining it)? Is it easy to hire developers that know and like it? Does it have a healthy open-source ecosystem and good documentation? How quickly can the average dev go from zero to a useful application with it? Does it encourage standards, structures, and patterns that are recognizable across codebases? Is it performant when it needs to be? Once you’ve got a well-rounded picture of the technical and non-technical pros and cons, make recommendations for when to use each. One might be your default for web services, another for serverless functions, yet another for prototypes and internal apps.

_Structure:_ A comparison chart followed by clear recommendations for a few different situations.

_How it orchestrates ideas:_ The technology menu helps create a consensus about how things are built, freeing developers to spin up useful tech without getting bogged down in this-versus-that debates. It can also challenge company defaults that have survived by virtue of tradition rather than suitability or popularity.

_Tips:_ Try to avoid championing your personal preferences. If you’re the one writing the menu, take it through a few rounds of feedback with developers who have worked with different technologies. Give their opinions as much weight as your own; it’s more important to get the team on the same page than to choose the absolute “best” technology.

_Purpose:_ To quickly reach consensus about how to solve or work around a problem.

_Audience:_ Stakeholders in a project.

_When to write one:_ Whenever you encounter a problem with no obvious solution and you need the organization to make a clear decision about it.

_Content:_ Explain the nature of the problem in simple terms. If it has a clear business impact, describe (or estimate) the scope and severity. Most problems involve two or more constraints that can’t be satisfied at the same time; if that’s the case here, make it very clear what those constraints are and why they contradict. Then present a few possible ways to move forward, summarizing the pros and cons of each.

_Structure:_ Sections like Context, Problem, Impact, Constraints, and Possible Solutions.

_How it orchestrates ideas:_ A well-written problem statement makes it possible for anyone, regardless of role, to understand the nature of a problem and why it matters, then weigh in on their preferred solution. It also leaves a permanent record of the conversation so you can refer back to it—the bigger a problem is, the more likely it will reappear or be rehashed later.

_Tips:_ Don’t skip the last section, even if none of the solutions that come to mind seem particularly good. Any engineer can find problems, but an architect’s job is to find solutions. If nothing else, presenting a few bad ideas can pave the way for someone to suggest a good one.

_Purpose:_ To keep catastrophic problems from recurring.

_Audience:_ Anyone with an interest in a recent outage, failure, or high-priority bug.

_When to write one:_ When a technological problem has had an abnormal impact. Most bugs don’t need a postmortem, but if there’s a major disruption to the flow of business—like an on-call developer getting paged or customers calling in to complain—it’s probably time to take things a step further.

_Content:_ Describe, in a blameless way, the apparent problem and how it came to your attention. Include links to any related conversations, pull requests, and issue-tracking tickets. Add details about who was affected, how long the problem took to resolve, and what was done to try to mitigate it in the meantime. Conclude by explaining the root causes of the problem, then recommending ways to prevent it from happening again.

_Structure:_ Sections like Context, Problem, Impact, Timeline, Root Causes, and Recommended Process Changes.

_How it orchestrates ideas:_ Postmortems help organizations move from the fear and anxiety of “this can never happen again” to the confidence and security of “we’ll make sure of it.” When used correctly, they also help shift culture away from individual blame, toward organizational competence and automatic safeguards.

_Tips:_ Postmortems are opportunities to take accountability for your mistakes, but they’re not exercises in self-flagellation. Everyone has bad days and makes mistakes. The purpose of an organization is to create resilience above and beyond what any one person can offer. Acknowledge the role you played, but keep your focus on what the organization as a whole can do better.