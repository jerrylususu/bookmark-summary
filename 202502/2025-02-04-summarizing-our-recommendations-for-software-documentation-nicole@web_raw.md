Title: Summarizing our recommendations for software documentation

URL Source: https://ntietz.com/blog/our-case-study-on-software-documentation/

Markdown Content:
Last year, my coworker Suzanne and I got a case study accepted into an ethnography conference! She's an anthropologist by training, and I'm a software engineer. How'd we wind up there?

The short version is I asked her what I thought was an interesting question, and _she_ thought it was an interesting question, and we wound up doing research. We have a lot more to go on the original question—we're studying the relationship between the values we hold as engineers and our documentation practices—and this case study is the first step in that direction.

The title of the case study is a mouthful: "Foundations of Practice: An Ethnographic Exploration of Software Documentation and its Cultural Implications for an Agile Startup". I mean, it's intended for a more academic audience, and in a field that's _not_ software engineering. But what we studied is relevant for software engineers, so let's talk about it here in more familiar language! If you want to read the full case study, it's [open access](https://www.epicpeople.org/foundations-of-practice-ethnographic-software-documentation/).

I'll start with the recommendations we provided, share a little bit about our methodology, and finish us out with a little about where we can go from here.

Our recommendations
-------------------

The case study concluded with recommendations. This is an area I'd like us to do a lot more work in, because recommendations based on a case study are based on _one_ example, and they'd obviously be much stronger based on more data! But for the conference submission, they were a necessary component. I think that the specific recommendations we gave hold up based on my experience (I'm biased, so take this as it is).

These were our core recommendations.

**Start with high-level documentation.** If you don't have _any_ docs today, or all your docs are just in a bad way, the biggest bang-for-buck is with your high-level systems docs and process documentation. Don't have a system architecture diagram? Make it! Don't have a CI process diagram? Make it! These help you get your bearings on everything quickly, and they're also usually _much_ faster to make than detailed documentation of more focused pieces.

**Use design reviews!** Here, "design review" means putting your architecture changes—or any proposal for a major code change—through a review process analogous to a code review. This is one of the things we implemented at my company over four years ago, and it's incredibly useful. It makes us think more deeply on our designs, so we make fewer errors in the design phase of any given feature. And it makes the design visible to the whole team, so we get much better knowledge transfer. _If I could drop these into every software company, I would._ They're _that_ useful.

**Think about your audience.** This is just plain good writing advice, and it bears repeating. Not every kind of documentation has the same audience, and if you don't take that into account you'll write bad docs that your end user won't be able to use effectively. You may use too much jargon for the lay user, or too _little_ jargon for efficient communication with the engineers working on a feature.

**Maintain the docs, updating them as part of your workflow.** I think we all know that docs should be updated. The recommendation here is that updating docs should be part of your workflow. If you run into something that's out of date, go ahead and fix it. If someone asks you a question because it wasn't in a given doc, go ahead and add it there.

**Document test plans.** QA processes are woefully underappreciated in software engineering. I don't quite understand why QA engineering is so looked down upon, because y'all, that stuff is _hard_. At any rate, testing? That's something you should document! Assuming you run tests before you release (you do, don't you?) then you need to have some organization and documentation around _what_ those tests are, why they're there, etc. This needs to be shared between both QA and product engineers since if the test fails, it's probably, you know, the _product engineer's_ change that broke it—so the better those docs are, the faster they can find the issue.

**Make onboarding docs.** We know that good onboarding is important for bringing new team members up to productive contribution quickly. And we know that documentation is a big part of that. So focus on your documentation as part of your onboarding strategy.

**Run post-mortems and retrospectives.** Mistakes will happen, and when they do? It's imperative that we go back through why they happened and what changes (if any) are merited to our processes as a result. Maybe there's work to be done to prevent similar incidents, or there's something we could do to detect this quicker in the future. Whatever you find, also update your docs: point to the post-mortems in the design docs that led to these decisions so that if someone reads those, they'll also see the longer-term impacts of those decisions.

**Encourage collaboration on documentation.** You can do this by involving multiple team members in creating and reviewing design docs. This is a tool for mentoring and professional development. It also improves all the documentation quality. If you involve team members at _all_ levels (not just your senior engineers!), you'll be able to ensure the docs and processes meet everyone's actual needs.

**Prioritize critical, complex areas for docs.** You can't document everything. We mentioned earlier that you want to start with a high-level documentation overview, but you _also_ want to focus your efforts on things which are critical or particularly complex. This will pay off by reducing the difficulty of understanding these areas, reducing rates of defects and speeding up development.

**Eliminate ineffective docs, focus on friction points.** If your team says that documentation isn't serving a useful purpose, trust them and get rid of it. Change what you do to do something more effective. Focus your documentation efforts on resolving friction points between teams or in the development process.

The methodology
---------------

Our research comprised two main pieces: a literature review and interviews with our engineering team.

We did the literature review first, to get our bearings. And, honestly, I was hoping to find answers to what we ultimately were setting out to answer. I'd rather _not_ have to do this research to get our answers! The existing papers gave us a good grounding. I won't repeat too much here—you can read the section in the case study if you're interested.

The bulk of the new research we did was through interviews, and analysis of those interviews[1](https://ntietz.com/blog/our-case-study-on-software-documentation/#question). We interviewed nine of our software engineers who were present at a critical transition in the company's history, when we implemented a major new documentation process as a result of transitioning to remote work. Each interview was recorded with the consent of the participants. We then transcribed them and did qualitative coding to extract themes. We were looking for some pre-defined themes (collaboration, learning, and knowledge sharing) and we were also interested in emergent themes.

From there, we were able to extract out five values that are represented by documentation practices at the company. These values (collaboration, learning, continuous improvement, accountability, and technical excellence) are exhibited _through_ our documentation practices. They are also reinforced by the documentation practices, so it's not wholly a causal relationship one way or the other.

At this point we were able to take the results of the interviews and combine that with the literature review to figure out recommendations based on our case study. These are, of course, not universal. And they're to some extent conjecture: by the nature of a case study, we're not able to ground this in data across multiple companies. But they're a launching off point for teams in need and for future research.

What's next?
------------

Ultimately, we want to drive toward answering the bigger questions we have around software engineering and documentation. One of those is: a lot of software engineers say their documentation is bad, and we also say that we value good documentation, so why do we not make the documentation better? Why are we not able to live our what we value there? Or do we _not_ value documentation?

To answer these questions to a satisfying end, we'll need to do a larger study. That means we'll need to recruit participants across many companies, and we'll need to design a study that can cut to the heart of these issues.

I'm not sure when we'll have the time or energy to approach that, but I know we've both been completely sucked in by these questions. So we'll get there eventually!

* * *

If this post was enjoyable or useful for you, **please share it!** If you have comments, questions, or feedback, you can email [my personal email](mailto:me@ntietz.com). To get new posts and support my work, subscribe to the [newsletter](https://ntietz.com/newsletter/). There is also an [RSS feed](https://ntietz.com/atom.xml).
