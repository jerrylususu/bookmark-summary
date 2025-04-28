Title: Design system documentation is essential–as long as it’s good

URL Source: https://pjonori.blog/posts/design-system-documentation/

Markdown Content:
Documentation, of all things, is a contentious topic within design systems. Never in a million years would I expect something as boring as documentation to get folks up in arms. Some people (like me) think it’s essential. Others think it’s useless.

Part of me thinks this is due to modern-day internet hyperbole. If something isn’t the best thing ever, it’s the worst thing ever. Another part thinks this is due to people’s experience with documentation.

As mentioned, I think documentation is essential. Specifically, I think _good_ documentation is essential. You’ll have my full agreement on the worthlessness of _bad_ documentation.

So I thought I’d write a short-ish articulation of what good documentation looks like and what it can do.

Good documentation is short, simple, structured, and actionable
---------------------------------------------------------------

Writing a bunch of stuff down may technically be documentation. But it doesn’t mean it’s good. Getting to good is hard work. Below are the qualities necessary to get to _good_.

### Succinct

Documentation should not be flowery or poetic. Each word should have meaning. Use the fewest words needed to get the point across. It can be tempting to “fill the space” to create the feeling of rigor. No one benefits from that approach.

### Predictable

A reader should know how to consume design system documentation in less than a day. The structure/format of content should be logical and consistent. Guidelines and best-practices will always evolve. But readers should know what to expect to see when they look for information.

As an example, component documentation should lead with, what it is, what it does, and what it’s for. Order the remaining content should by what readers need to know next. The goal should be to get readers using the component _as quick as possible_.

### Concrete

Design system guidance must be explicit, objective and not subject to interpretation. Phrases like, “Use sparingly” or, “Avoid when possible” are subjective. What does “sparingly” mean? What’s the definition of “when possible”? Many words can have wildly different individual interpretations. The goal of documentation is to replace individual interpretation with shared definition. If a component should only be used once on a surface, say _that_.

### Exact

Words in documentation must be used precisely. Use the same words to mean the same thing. For example, it’s problematic to use “quality” and “high craft” to reference the same subject. As mentioned, words have different individual interpretations. It’s already difficult to align on the meaning of one word. Don’t make it harder by using other words. Yes, this will make the writing repetitive. That’s a feature, not a bug. Repetition helps build familiarity.

Similarly, use different words to mean different things. Terms like “font”, “typography”, and “text” all have distinct meanings. Resist glomming terms together for the sake of convenience.

### Approachable

Documentation doesn’t need fancy words. Use clear, simple language. Our work isn’t a science, so our language doesn’t need to be scientific.

Small words can have big meaning. The harder it is to read documentation, the fewer people will read it. That’s a basic, but important truth.

In a similar vein, avoid jargon and acronyms. Don’t make up new words that don’t need to be made up. Remember that a company’s dialect is not inherently understood–meaning it represents a dependency for people to understand the documentation.

A a rule, a junior-level employee should be able to understand a design system’s documentation.

### Encapsulated

Individual guidelines should be self-contained and understandable on their own. The reader shouldn’t have to read the entire Button component’s docs to know when to add an icon. Each specific guideline should be able to guide the reader on its own. Readers need to be able to skim and digest documentation piecemeal.

Principles for a design system can be helpful. But they should be able to perform basis tasks without reading them.

### Actionable

People’s relationship with documentation is transactional. A person needs to know how to do a thing–they read the documentation to find out. 99% of the time they are not interested in design principles or mission statements. They _just_ need to know how to do a thing.

Documentation should be tuned for action. Remove preamble. Frame guidance in a way that enables people to act with certainty in the least amount of steps.

Similarly, only telling readers what not to do\* isn’t actionable. People aren’t interested in what \_not\* to do. They’re need to know what _to_ do. Documentation will not have all the answers. But it’s important for documentation to avoid being the “Book of Don’ts”. “Don’t dos” should be paired with “…do _this_ instead”.

### Justified

Documentation should be able to answer, “But, why?” Recommending a reader not do something without justification is not actionable or educational. It does not guide the reader to better understand how the system works or how to interpret its rules. Including rationale is critical to help readers understand the system’s underlying logic.

Best practices are a clear area of opportunity for providing rationale. Ideally this rationale is rooted in evidence with cited sources. Sharing this information is a window into how the system works. It’ll drive a deeper understanding.

90% of the time this info will not be needed or desired. It can counter-intuitively make the documentation less actionable. To remain succinct, this may mean including footnotes or linking to an appendix. Receipts should be available when readers come asking for them.

### Definitive (in a chill kind of way)

Remember that documentation is _guidance_. It’s a recommendation based on _known_ use cases and needs. The unknowns are just that. Design system documentation will _always_ be imperfect and incomplete.

In that spirit, the tone of documentation should always reinforce that reality. Recommendations are _just that_. They are not a dictate or an ultimatum. Words like _must_ should be used with extreme care and precision.

Good documentation can help transform the way work is done
----------------------------------------------------------

Yeah, those are strong words. But I believe them–strongly. Below are all things (except for one) that I’ve seen documentation do with my own two eyes.

### It forces a point of view

A design system team without documentation is dangerous. It gives them room to waffle. Today, only one primary button on a surface is allowed. Tomorrow, maybe not. Without documentation, a point of view can change at any moment. With no accountability.

Design system consumers deserve a clear, stable point of view on how to use it. They should be able to push back when feedback doesn’t align with documented guidelines. Documentation keeps a design system team honest and answerable to those who use it.

### It improves the thinking behind the system

I believe writing documentation is valuable even if no one reads it. Look, it’s been said a million times–the act of writing fortifies the thinking behind it.

A design system’s component or pattern isn’t complete until it’s been documented. Documentation is a design system’s mental QA. It’s one thing to think a component or pattern’s logic works in your head. It’s another to prove it by writing that logic out.

Writing documentation has resulted in more component revisions than I can count. The process is worth it for that reason alone.

### It keeps the design system team aligned

It’s naive to think the entire design system team shares the same understanding of every token, component and pattern. Quite the opposite–I’d say there’s far more misalignment than there’s alignment on the average team. Documentation can correct that _quickly_.

Documentation acts as a team’s handbook and rallying point. It helps team members catch up on areas they have less exposure to. In times of disagreement, it can help ground conversations. Docs can be the mental glue between all team members.

### It keeps thinking available when people aren’t

A lot of design system teams rely on Slack or Teams to answer questions as they come in. It’s common for those mediums to be the de facto form of documentation. Which, I’ll say, is the least efficient form of documentation possible. But on top of that, what happens when the person answering the questions isn’t available?

The thinking behind a design system is–far and away–its most valuable piece. It’s a huge risk to for all that thinking to stay bottled up in one person’s head. That person will be too busy to respond. They’ll get sick. They’ll go on vacation. Those moments represent blockers to anyone with questions about the system.

And someday, that person will leave. At which point that knowledge is gone _forever_.

### It creates a common language

Design system docs help folks understand a product’s design/engineering best practices. Duh. But it also creates shared terminology and definitions. Which allows people to effectively communicate.

It’s hard to have conversations when people use different words with the same meaning. Or the same words with different meaning. A component with different names between design and code can screw things up big time. Take a guess at what shines a light on issues like that?

Words matter–now more than ever. Documentation produces a shared set of words to help generate shared understanding.

### It levels the playing field (maybe)

This one’s a little aspirational and admittedly not proven. But I believe in it nonetheless. Documentation can be a (hypothetical) leveling agent within organizations. It’s far too common for decisions to suffer from highest-paid-opinion-In-the-room-syndrome. I see documentation as a way for people to fortify their decisions to those above them.

Will this always work? No. Will it work the majority of situations? Probably not. But even if it works on occasion, that’s damned valuable.

Naive/idealistic? Guilty as charged.

### It reduces team overhead

Design system support is as important as it is costly. Make no mistake, support is a key part of a design system’s success. But support doesn’t need to be only handled by humans.

[People do read](https://pjonori.blog/posts/everybody-reads). Good documentation _is_ read. Every question documentation answers is one that a person doesn’t. I’ve seen cases where growth in docs usage coincided with decreases in support volume. Cases–as in plural.

That decrease in support is time saved. And that saved time is free to apply elsewhere–like improving the system. Or writing _more_ documentation. Time is always money. Good documentation prints it.

### It acts as a feeder for AI

Yeah, I said it. I’ve yet to see AI perform effectively in typical design systems work. I remain uncertain what role it will play within design and engineering. But I am certain that design system documentation is an _ideal_ source to train LLMs. Those who are pursuing AI in their internal processes should be documenting.

This is an area I continue to explore with mixed opinions. But it shows enough promise to keep chipping away at it with interest.

People read good stuff. So write good stuff.
--------------------------------------------

There may come a day where humans invent a better form of information transfer than written text. I’ll back off this crusade once that day comes. But it ain’t here yet.

Until then, take the time to document your system.
