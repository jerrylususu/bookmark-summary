Title: Systems design 3: LLMs and the semantic revolution

URL Source: https://apenwarr.ca/log/20251120

Markdown Content:
**Systems design 3: LLMs and the semantic revolution**

Long ago in the 1990s when I was in high school, my chemistry+physics teacher pulled me aside. "Avery, you know how the Internet works, right? I have a question."

I now know the correct response to that was, "Does anyone _really_ know how the Internet works?" But as a naive young high schooler I did not have that level of self-awareness. (Decades later, as a CEO, that's my answer to almost everything.)

Anyway, he asked his question, and it was simple but deep. How do they make all the computers connect?

We can't even get the world to agree on 60 Hz vs 50 Hz, 120V vs 240V, or which kind of physical power plug to use. Communications equipment uses way more frequencies, way more voltages, way more plug types. Phone companies managed to federate with each other, eventually, barely, but the ring tones were different everywhere, there was pulse dialing and tone dialing, and some of them _still_ charge $3/minute for international long distance, and connections take a long time to establish and humans seem to be involved in suspiciously many places when things get messy, and every country has a different long-distance dialing standard and phone number format.

So Avery, he said, now they're telling me every computer in the world can connect to every other computer, in milliseconds, for free, between Canada and France and China and Russia. And they all use a single standardized address format, and then you just log in and transfer files and stuff? How? How did they make the whole world cooperate? And who?

When he asked that question, it was a formative moment in my life that I'll never forget, because as an early member of what would be the first Internet generation… I Had Simply Never Thought of That.

I mean, I had to stop and think for a second. Wait, is protocol standardization even a hard problem? Of course it is. Humans can't agree on anything. We can't agree on a unit of length or the size of a pint, or which side of the road to drive on. Humans in two regions of Europe no farther apart than Thunder Bay and Toronto can't understand each other's speech. But this Internet thing just, kinda, worked.

"There's… a layer on top," I uttered, unsatisfyingly. Nobody had taught me yet that the OSI stack model existed, let alone that it was at best a weak explanation of reality.

"When something doesn't talk to something else, someone makes an adapter. Uh, and some of the adapters are just programs rather than physical things. It's not like everyone in the world agrees. But as soon as one person makes an adapter, the two things come together."

I don't think he was impressed with my answer. Why would he be? Surely nothing so comprehensively connected could be engineered with no central architecture, by a loosely-knit cult of mostly-volunteers building an endless series of whimsical half-considered "adapters" in their basements and cramped university tech labs. Such a creation would be a monstrosity, just as likely to topple over as to barely function.

I didn't try to convince him, because honestly, how could I know? But the question has dominated my life ever since.

When things don't connect, why don't they connect? When they do, why? How? …and who?

**Postel's Law**

The closest clue I've found is this thing called Postel's Law, one of the foundational principles of the Internet. It was best stated by one of the founders of the Internet, Jon Postel. "Be conservative in what you send, and liberal in what you accept."

What it means to me is, if there's a standard, do your best to follow it, when you're sending. And when you're receiving, uh, assume the best intentions of your counterparty and do your best and if that doesn't work, guess.

A rephrasing I use sometimes is, "It takes two to miscommunicate." Communication works best and most smoothly if you have a good listener and a clear speaker, sharing a language and context. But it can still bumble along successfully if you have a poor speaker with a great listener, or even a great speaker with a mediocre listener. Sometimes you have to say the same thing five ways before it gets across (wifi packet retransmits), or ask way too many clarifying questions, but if one side or the other is diligent enough, you can almost always make it work.

This asymmetry is key to all high-level communication. It makes network bugs much less severe. Without Postel's Law, triggering a bug in the sender would break the connection; so would triggering a bug in the receiver. With Postel's Law, we acknowledge from the start that there are always bugs and we have twice as many chances to work around them. Only if you trigger both sets of bugs at once is the flaw fatal.

…So okay, if you've used the Internet, you've probably observed that fatal connection errors are nevertheless pretty common. But that misses how _incredibly much more common_ they would be in a non-Postel world. That world would be the one my physics teacher imagined, where nothing ever works and it all topples over.

And we know that's true because we've tried it. Science! Let us digress.

**XML**

We had the Internet ("OSI Layer 3") mostly figured out by the time my era began in the late 1900s, but higher layers of the stack still had work to do. It was the early days of the web. We had these newfangled hypertext ("HTML") browsers that would connect to a server, download some stuff, and then try their best to render it.

Web browsers are and have always been an epic instantiation of Postel's Law. From the very beginning, they assumed that the server (content author) had absolutely no clue what they were doing and did their best to apply some kind of meaning on top, despite every indication that this was a lost cause. List items that never end? Sure. Tags you've never heard of? Whatever. Forgot some semicolons in your javascript? I'll interpolate some. Partially overlapping italics and bold? Leave it to me. No indication what language or encoding the page is in? I'll just guess.

The evolution of browsers gives us some insight into why Postel's Law is a law and not just, you know, Postel's Advice. The answer is: competition. It works like this. If your browser interprets someone's mismash subjectively better than another browser, your browser wins.

I think economists call this an iterated prisoner's dilemma. Over and over, people write web pages (defect) and browsers try to render them (defect) and absolutely nobody actually cares what the HTML standard says (stays loyal). Because if there's a popular page that's wrong and you render it "right" and it doesn't work? Straight to jail.

(By now almost all the evolutionary lines of browsers have been sent to jail, one by one, and the HTML standard is effectively whatever Chromium and Safari say it is. Sorry.)

This law offends engineers to the deepness of their soul. We went through a period where loyalists would run their pages through "validators" and proudly add a logo to the bottom of their page saying how valid their HTML was. Browsers, of course, didn't care and continued to try their best.

Another valiant effort was the definition of "quirks mode": a legacy rendering mode meant to document, normalize, and push aside all the legacy wonko interpretations of old web pages. It was paired with a new, standards-compliant rendering mode that everyone was supposed to agree on, starting from scratch with an actual written spec and tests this time, and public shaming if you made a browser that did it wrong. Of course, outside of browser academia, nobody cares about the public shaming and everyone cares if your browser can render the popular web sites, so there are still plenty of quirks outside quirks mode. It's better and it was well worth the effort, but it's not all the way there. It never can be.

We can be sure it's not all the way there because there was another exciting development, HTML Strict (and its fancier twin, XHTML), which was meant to be the same thing, but with a special feature. Instead of sending browsers to jail for rendering wrong pages wrong, we'd send page authors to jail for writing wrong pages!

To mark your web page as HTML Strict was a vote against the iterated prisoner's dilemma and Postel's Law. No, your vote said. No more. We cannot accept this madness. We are going to be Correct. I certify this page is correct. If it is not correct, you must sacrifice me, not all of society. My honour demands it.

Anyway, many page authors were thus sacrificed and now nobody uses HTML Strict. Nobody wants to do tech support for a web page that asks browsers to crash when parsing it, when you can just… not do that.

**Excuse me, the above XML section didn't have any XML**

Yes, I'm getting to that. (And you're soon going to appreciate that meta joke about schemas.)

In parallel with that dead branch of HTML, a bunch of people had realized that, more generally, HTML-like languages (technically SGML-like languages) had turned out to be a surprisingly effective way to build interconnected data systems.

In retrospect we now know that the reason for HTML's resilience is Postel's Law. It's simply easier to fudge your way through parsing incorrect hypertext, than to fudge your way through parsing a Microsoft Word or Excel file's hairball of binary OLE streams, which famously even Microsoft at one point lost the knowledge of how to parse. But, that Postel's Law connection wasn't really understood at the time.

Instead we had a different hypothesis: "separation of structure and content." Syntax and semantics. Writing software to deal with structure is repetitive overhead, and content is where the money is. Let's automate away the structure so you can spend your time on the content: semantics.

We can standardize the syntax with a single Extensible Markup Language (XML). Write your content, then "mark it up" by adding structure right in the doc, just like we did with plaintext human documents. Data, plus self-describing metadata, all in one place. Never write a parser again!

Of course, with 20/20 hindsight (or now 2025 hindsight), this is laughable. Yes, we now have XML parser libraries. If you've ever tried to use one, you will find they indeed produce parse trees automatically… if you're lucky. If you're not lucky, they produce a stream of "tokens" and leave it to you to figure out how to arrange it in a tree, for reasons involving streaming, performance, memory efficiency, and so on. Basically, if you use XML you now have to _deeply_ care about structure, perhaps more than ever, but you also have to include some giant external parsing library that, left in its normal mode, [might spontaneously start making a lot of uncached HTTP requests that can also exploit remote code execution vulnerabilities haha oops](https://cheatsheetseries.owasp.org/cheatsheets/XML_External_Entity_Prevention_Cheat_Sheet.html).

If you've ever taken a parser class, or even if you've just barely tried to write a parser, you'll know the truth: the value added by outsourcing _parsing_ (or in some cases only tokenization) is not a lot. This is because almost all the trouble of document processing (or compiling) is the _semantic_ layer, the part where you make sense of the parse tree. The part where you just read a stream of characters into a data structure is the trivial, well-understood first step.

Now, semantics is where it gets interesting. XML was all about separating syntax from semantics. And they did some pretty neat stuff with that separation, in a computer science sense. XML is neat because it's such a regular and strict language that you can completely _validate_ the syntax (text and tags) without knowing what any of the tags _mean_ or which tags are intended to be valid at all.

…aha! Did someone say _validate?!_ Like those old HTML validators we talked about? Oh yes. Yes! And this time the validation will be completely strict and baked into every implementation from day 1. And, the language syntax itself will be so easy and consistent to validate (unlike SGML and HTML, which are, in all fairness, bananas) that nobody can possibly screw it up.

A layer on top of this basic, highly validatable XML, was a thing called XML Schemas. These were documents (mysteriously not written in XML) that described which tags were allowed in which places in a certain kind of document. Not only could you parse and validate the basic XML syntax, you could also then validate its XML schema as a separate step, to be totally sure that every tag in the document was allowed where it was used, and present if it was required. And if not? Well, straight to jail. We all agreed on this, everyone. Day one. No exceptions. Every document validates. Straight to jail.

Anyway XML schema validation became an absolute farce. Just parsing or understanding, let alone writing, the awful schema file format is an unpleasant ordeal. To say nothing of complying with the schema, or (heaven forbid) obtaining a copy of someone's custom schema and loading it into the validator at the right time.

The core XML syntax validation was easy enough to do while parsing. Unfortunately, in a second violation of Postel's Law, almost no software that _outputs_ XML runs it through a validator before sending. I mean, why would they, the language is highly regular and easy to generate and thus the output is already perfect. …Yeah, sure.

Anyway we all use JSON now.

**JSON**

Whoa, wait! I wasn't done!

This is the part where I note, for posterity's sake, that XML became a decade-long fad in the early 2000s that justified billions of dollars of software investment. None of XML's technical promises played out; it is a stain on the history of the computer industry. But, a lot of legacy software got un-stuck because of those billions of dollars, and so we did make progress.

What was that progress? Interconnection.

Before the Internet, we kinda didn't really need to interconnect software together. I mean, we sort of did, like cut-and-pasting between apps on Windows or macOS or X11, all of which were surprisingly difficult little mini-Postel's Law protocol adventures in their own right and remain quite useful when they work ([except "paste formatted text," wtf are you people thinking](https://news.ycombinator.com/item?id=31356896)). What makes cut-and-paste possible is top-down standards imposed by each operating system vendor.

If you want the same kind of thing on the open Internet, ie. the ability to "copy" information out of one server and "paste" it into another, you need _some_ kind of standard. XML was a valiant effort to create one. It didn't work, but it was valiant.

Whereas all that money investment _did_ work. Companies spent billions of dollars to update their servers to publish APIs that could serve not just human-formatted HTML, but also something machine-readable. The great innovation was not XML per se, it was serving data over HTTP that wasn't always HTML. That was a big step, and didn't become obvious until afterward.

The most common clients of HTTP were web browsers, and web browsers only knew how to parse two things: HTML and javascript. To a first approximation, valid XML is "valid" (please don't ask the validator) HTML, so we could do that at first, and there were some Microsoft extensions. Later, after a few billions of dollars, true standardized XML parsing arrived in browsers. Similarly, to a first approximation, valid JSON is valid javascript, which woo hoo, that's a story in itself (you could parse it with eval(), tee hee) but that's why we got here.

JSON (minus the rest of javascript) is a vastly simpler language than XML. It's easy to consistently parse ([other than that pesky trailing comma](https://github.com/tailscale/hujson)); browsers already did. It represents only (a subset of) the data types normal programming languages already have, unlike XML's weird mishmash of single attributes, multiply occurring attributes, text content, and CDATA. It's obviously a tree and everyone knows how that tree will map into their favourite programming language. It inherently works with unicode and only unicode. You don't need cumbersome and duplicative "closing tags" that double the size of every node. And best of all, no guilt about skipping that overcomplicated and impossible-to-get-right schema validator, because, well, nobody liked schemas anyway so nobody added them to JSON ([almost](https://json-schema.org/)).

Today, if you look at APIs you need to call, you can tell which ones were a result of the $billions invested in the 2000s, because it's all XML. And you can tell which came in the 2010s and later after learning some hard lessons, because it's all JSON. But either way, the big achievement is you can call them all from javascript. That's pretty good.

(Google is an interesting exception: they invented and used protobuf during the same time period because they disliked XML's inefficiency, they did like schemas, and they had the automated infrastructure to make schemas actually work (mostly, after more hard lessons). But it mostly didn't spread beyond Google… maybe because it's hard to do from javascript.)

**Blockchain**

The 2010s were another decade of massive multi-billion dollar tech investment. Once again it was triggered by an overwrought boondoggle technology, and once again we benefited from systems finally getting updated that really needed to be updated.

Let's leave aside cryptocurrencies (which although used primarily for crime, at least demonstrably have a functioning use case, ie. crime) and look at the more general form of the technology.

Blockchains in general make the promise of a "distributed ledger" which allows everyone the ability to make claims and then later validate other people's claims. The claims that "real" companies invested in were meant to be about manufacturing, shipping, assembly, purchases, invoices, receipts, ownership, and so on. What's the pattern? That's the stuff of businesses doing business with other businesses. In other words, data exchange. Data exchange is exactly what XML didn't really solve (although progress was made by virtue of the dollars invested) in the previous decade.

Blockchain tech was a more spectacular boondoggle than XML for a few reasons. First, it didn't even have a purpose you could explain. Why do we even need a purely distributed system for this? Why can't we just trust a third party auditor? Who even wants their entire supply chain (including number of widgets produced and where each one is right now) to be visible to the whole world? What is the problem we're trying to solve with that?

…and you know there really was no purpose, because after all the huge investment to rewrite all that stuff, which was itself valuable work, we simply dropped the useless blockchain part and then we were fine. I don't think even the people working on it felt like they needed a real distributed ledger. They just needed an _updated_ ledger and a budget to create one. If you make the "ledger" module pluggable in your big fancy supply chain system, you can later drop out the useless "distributed" ledger and use a regular old ledger. The protocols, the partnerships, the databases, the supply chain, and all the rest can stay the same.

In XML's defense, at least it was not worth the effort to rip out once the world came to its senses.

Another interesting similarity between XML and blockchains was the computer science appeal. A particular kind of person gets very excited about _validation_ and _verifiability._ Both times, the whole computer industry followed those people down into the pits of despair and when we finally emerged… still no validation, still no verifiability, still didn't matter. Just some computers communicating with each other a little better than they did before.

**LLMs**

In the 2020s, our industry fad is LLMs. I'm going to draw some comparisons here to the last two fads, but there are some big differences too.

One similarity is the computer science appeal: so much math! Just the matrix sizes alone are a technological marvel the likes of which we have never seen. Beautiful. Colossal. Monumental. An inspiration to nerds everywhere.

But a big difference is verification and validation. If there is one thing LLMs absolutely are not, it's _verifiable._ LLMs are the flakiest thing the computer industry has ever produced! So far. And remember, this is the industry that brought you HTML rendering.

LLMs are an almost cartoonishly amplified realization of Postel's Law. They write human grammar perfectly, or almost perfectly, or when they're not perfect it's a bug and we train them harder. And, they can receive just about any kind of gibberish and turn it into a data structure. In other words, they're conservative in what they send and liberal in what they accept.

LLMs also solve the syntax problem, in the sense that they can figure out how to transliterate (convert) basically any file syntax into any other. Modulo flakiness. But if you need a CSV in the form of a limerick or a quarterly financial report formatted as a mysql dump, sure, no problem, make it so.

In theory we already had syntax solved though. XML and JSON did that already. We were even making progress interconnecting old school company supply chain stuff the hard way, thanks to our nominally XML- and blockchain- investment decades. We had to do every interconnection by hand – by writing an adapter – but we could do it.

What's really new is that LLMs address _semantics._ Semantics are the biggest remaining challenge in connecting one system to another. If XML solved syntax, that was the first 10%. Semantics are the last 90%. When I want to copy from one database to another, how do I map the fields? When I want to scrape a series of uncooperative web pages and turn it into a table of products and prices, how do I turn that HTML into something structured? (Predictably [microformats](https://microformats.org/), aka schemas, did not work out.) If I want to query a database (or join a few disparate databases!) using some language that isn't SQL, what options do I have?

LLMs can do it all.

Listen, we can argue forever about whether LLMs "understand" things, or will achieve anything we might call intelligence, or will take over the world and eradicate all humans, or are useful assistants, or just produce lots of text sludge that will certainly clog up the web and social media, or will also be able to filter the sludge, or what it means for capitalism that we willingly invented a machine we pay to produce sludge that we also pay to remove the sludge.

But what we can't argue is that LLMs interconnect things. Anything. To anything. Whether you like it or not. Whether it's bug free or not (spoiler: it's not). Whether it gets the right answer or not (spoiler: erm…).

This is the thing we have gone through at least two decades of hype cycles desperately chasing. (Three, if you count java "write once run anywhere" in the 1990s.) It's application-layer interconnection, the holy grail of the Internet.

And this time, it actually works! (mostly)

**The curse of success**

LLMs aren't going away. Really we should coin a term for this use case, call it "b2b AI" or something. For this use case, LLMs work. And they're still getting better and the precision will improve with practice. For example, imagine asking an LLM to write a data translator in some conventional programming language, instead of asking it to directly translate a dataset on its own. We're still at the beginning.

But, this use case, which I predict is the big one, isn't what we expected. We expected LLMs to write poetry or give strategic advice or whatever. We didn't expect them to call APIs and immediately turn around and use what it learned to call other APIs.

After 30 years of trying and failing to connect one system to another, we now have a literal universal translator. Plug it into any two things and it'll just go, for better or worse, no matter how confused it becomes. And everyone is doing it, fast, often with a corporate mandate to do it even faster.

This kind of scale and speed of (successful!) rollout is unprecedented, even by the Internet itself, and especially in the glacially slow world of enterprise system interconnections, where progress grinds to a halt once a decade only to be finally dislodged by the next misguided technology wave. Nobody was prepared for it, so nobody was prepared for the consequences.

One of the odd features of Postel's Law is it's irresistible. Big Central Infrastructure projects rise and fall with funding, but Postel's Law projects are powered by love. A little here, a little there, over time. One more person plugging one more thing into one more other thing. We did it once with the Internet, overcoming all the incompatibilities at OSI layers 1 and 2. It subsumed, it is still subsuming, everything.

Now we're doing it again at the application layer, the information layer. And just like we found out when we connected all the computers together the first time, naively hyperconnected networks make it easy for bad actors to spread and disrupt at superhuman speeds. We had to invent firewalls, NATs, TLS, authentication systems, two-factor authentication systems, phishing-resistant two-factor authentication systems, methodical software patching, CVE tracking, sandboxing, antivirus systems, EDR systems, DLP systems, everything. We'll have to do it all again, but faster and different.

Because this time, it's all software.