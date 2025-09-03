Title: 40 years later, are Bentley's "Programming Pearls" still relevant?

URL Source: https://shkspr.mobi/blog/2025/09/40-years-later-are-bentleys-programming-pearls-still-relevant/

Published Time: 2025-09-03T12:34:14+01:00

Markdown Content:
In September 1985, Jon Bentley published [Programming Pearls](https://dl.acm.org/doi/10.1145/4284.315122). A collection of aphorisms designed to reveal truths about the field of programming.

It's 40 years later - long enough to see several revolutions in the field - so surely these are obsolete, right? They belong in the same category as "always carry a bundle of hay for the horses" or "you won't always have a pocket calculator with you" or "tie an onion on your belt to stay stylish".

Ah, my sweet summer child! _Plus ça change, plus c'est la même chose._ You'll find nearly everything in here depressingly relevant.

Before we dive in, a word for Bentley on the provenance of this collection:

[Programming Pearls.](https://shkspr.mobi/blog/wp-content/uploads/2025/09/4284.315122.pdf)

> Although there is some truth in each saying in this column, all should be taken with a grain of salt. A word about credit. The name associated with a rule is usually the person who sent me the rule, even if they in fact attributed it to their Cousin Ralph (sorry, Ralph). In a few cases I have listed an earlier reference, together with the author’s current affiliation (to the best of my knowledge). I’m sure that I have slighted many people by denying them proper attribution, and to them I offer the condolence that Plagiarism is the sincerest form of flattery.

Here we go!

[![Image 1: Gnarly monochrome scan of Programming Pearls.](https://shkspr.mobi/blog/wp-content/uploads/2025/09/pp-fs8.png)](https://dl.acm.org/doi/10.1145/4284.315122)

[Coding](https://shkspr.mobi/blog/2025/09/40-years-later-are-bentleys-programming-pearls-still-relevant/#coding)
----------------------------------------------------------------------------------------------------------------

> When in doubt, use brute force. Ken Thompson - Bell Labs

Straight off the bat, a winner! Almost all problems are solvable through brute force. It may take time - but throw more resources at it! Once you know it _can_ be done, then it is time to see _how_ it can be done better.

> Avoid arc-sine and arc-cosine functions - you can usually do better by applying a trig identity or computing a vector dot-product. Jim Conyngham - Arvin/Calspan Advanced Technology Center

And then, just like that, something broadly irrelevant today. These sorts of mathematical functions have been optimised so far that it probably doesn't matter which way you calculate them.

> Allocate four digits for the year part of a date: a new millenium is coming. David Martin - Norristown, Pennsylvania

_*weeps*_ Why didn't they listen to you, David? While I would hope any code written this side of Y2K uses ISO8601, it is amusing that you still occasionally encounter people who want to save two bytes _somewhere_. Handy in some small systems, but mostly just a recipe for disaster. Looking at you, [GPS](https://www.gps.gov/support/user/rollover/)!

> Avoid asymmetry. Andy Huber - Data General Corporation

I'll be honest, I'm not sure what Andy is going on about here. I _assume_ that he's talking about having the ability to go A->B without being able to go B->A. Equally, it could be about accepting data in one format and outputting it in a different format. [Some more discussion on the topic](https://news.ycombinator.com/item?id=33739184).

> The sooner you start to code, the longer the program will take. Roy Carlson - University of Wisconsin

_Bam!_ Right in the truth. Much like [the woodsman who spends his time sharpening his axe](https://quoteinvestigator.com/2014/03/29/sharp-axe/), we know that diving into code is probably the least efficient way to create something.

> If you can’t write it down in English, you can’t code it. Peter Halpern - Brooklyn, New York

So many bugs come from us not understanding the requirements of the user / customer.

> Details count. Peter Wrinberger - Bell Labs

Hard agree, Pete! It's very easy to go for the "big picture" view of the software. But unless all those sharp edges are filed down, the code isn't going to have a happy life.

> If the code and the comments disagree, then both are probably wrong. Norm Schyer - Belt Labs

Ah, the dream of self-documenting code will never be realised. Again, this goes back to our (in)ability to properly describe our requirements and our (in)adequacies at turning those comments into code.

> A procedure should fit on a page. David Tribble - Arlington, Texas

Famously, [Amazon has a "Two Pizza" rule](https://www.theguardian.com/technology/2018/apr/24/the-two-pizza-rule-and-the-secret-of-amazons-success) which defines the maximum size of a team. The larger and more complex something is, the more likely it is to go wrong. Yes, there are limits to DRY and YAGNI - but we seem firmly in the paradigm that large procedures / functions are ruinous to one's health.

> If you have too many special cases, you are doing it wrong. Craig Zerouni - Computer FX Ltd. London, England

`IF/ELSE` and `CASE/SWITCH` still really test our patience. Beautifully clean code which is ruined by special subroutines for rarely occurring situations. But it is hard to call them "wrong". Sometimes the world is complex and it is the job of computers to do the hard work for us.

> Get your data structures correct first, and the rest of the program will write itself. David Jones. Assen, The Netherlands

Dave is right. A well-defined data structure is _still_ the essence of most CRUD systems.

[User Interfaces](https://shkspr.mobi/blog/2025/09/40-years-later-are-bentleys-programming-pearls-still-relevant/#user-interfaces)
----------------------------------------------------------------------------------------------------------------------------------

> [The Principle of Least Astonishment] Make a user interface as consistent and as predictable as possible. Contributed by several readers

_*weeps*_ Why isn't this hammered into every programmer? Today's tools are filled with hidden UI gestures, random menus, and a complete disregard for the user's time.

> A program designed for inputs from people is usually stressed beyond the breaking point by computer-generated inputs. Dennis Ritchie. Bell Labs

I think this one is mostly irrelevant now. Humans can only type at a limited speed, but computers can generate massive amounts of data instantly. But our machines' abilities to ingest that data has also grown. I suppose the nearest thing is the DDoS - where a webserver designed for a few visitors is overwhelmed by a flood of automated and malicious requests.

> Twenty percent of all input forms filled out by people contain bad data. Vic Vyssotsky. Bell Labs

Ha! Vic didn't know that we'd have `<input type...` validation in the 21st century! But, yeah, people write all sorts of crap into forms.

> Eighty percent of all input forms ask questions they have no business asking. Mike Garey. Bell Labs

Mike was sent from the future to warn the people of the past - but they paid him no heed.

> Don't make the user provide information that the system already knows. Rick Lemons. Cardinal Data Systems

I'm going to slightly disagree with Rick here. Asking for repeated information is a reasonable way to double-check you've got that information correct. It also helps to validate that the user is who they say they are.

> For 80 percent of all data sets, 95 percent of the information can be seen in a good graph. William S. Cleveland. Bell Labs

Those of us who have seen [Anscombe's quartet](https://en.wikipedia.org/wiki/Anscombe's_quartet) know how true this is.

[Debugging](https://shkspr.mobi/blog/2025/09/40-years-later-are-bentleys-programming-pearls-still-relevant/#debugging)
----------------------------------------------------------------------------------------------------------------------

> Of all my programming bugs, 80 percent are syntax errors. Of the remaining 20 percent, 80 percent are trivial logical errors. Of the remaining 4 percent, 80 percent are pointer errors. And the remaining 0.8 percent are hard. Marc Donner. IBM T. J. Watson Research Center

Syntax errors are rarer now that we have IDEs. And I hope visual programming languages will further reduce them. Logic errors still plague us. Pointer errors have been eradicated unless you're working at the very lowest levels. And I'd say the number of "hard" bugs is probably higher now due to the complex interaction of multiple libraries and systems.

> It takes three times the effort to find and fix bugs in system test than when done by the developer. It takes ten times the effort to find and fix bugs in the field than when done in system test. Therefore, insist on unit tests by the developer. Larry Bernstein. Bell Communications Research

We can quibble about the numbers and the ratios - but it is generally harder to fix in prod. That said, getting crash logs from the field has considerable shortened those ratio.

> Don’t debug standing up. It cuts your patience in half, and you need all you can muster. Dave Storer. Cedar Rapids, Iowa

I'm with Team-Standing-Desk! So I think Dave is wrong.

> Don’t get suckered in by the comments - they can be terribly misleading. Debug only the code. Dave Storer. Cedar Rapids, Iowa

Hmmm. Yes, this is probably correct. I'm not going to say code is self-documenting these days; but it certainly is a lot easier to read.

> Testing can show the presence of bugs, but not their absence. Edsger W. Dijkstra. University of Texas

Dare we disagree with Dijkstra?! Well, perhaps a little. With modern fuzzing tools we can show the absence of certain kinds of bugs.

> Each new user of a new system uncovers a new class of bugs. Brian Kernighan. Bell Labs

Yup! Our code would be bug-free if it weren't for those pesky users!

> If it ain’t broke, don’t fix it. Ronald Reagan. Santa Barbara, California

Amongst the many things about which to disagree with the former President, this is up there! Code needs maintenance. Some things aren't broke until all of a sudden they are. Sure, maybe don't change your app's layout because a manager wants a bonus; but things constantly need fixing.

> [The Maintainer’s Motto] If we can’t fix it, it ain’t broke. Lieutenant Colonel Walt Weir. United States Army

I believe in you. Self deprecation is fine, but self confidence is better.

> The first step in fixing a broken program is getting it to fail repeatably. Tom Duff. Bell Labs

Yes! Transient errors are the worst! And a huge source of the "it works for me" antipattern.

[Performance](https://shkspr.mobi/blog/2025/09/40-years-later-are-bentleys-programming-pearls-still-relevant/#performance)
--------------------------------------------------------------------------------------------------------------------------

> [The First Rule of Program Optimization] Don’t do it. [The Second Rule of Program Optimization - for experts only] Don't do it yet. Michael Jackson. Michael Jackson Systems Ltd.

As true now as it ever was.

> The fastest algorithm can frequently be replaced by one that is almost as fast and much easier to understand. Douglas W. Jones. University of Iowa

I'm only _mostly_ in agreement here. Many of the security bugs we see in modern code are due to "clever" tricks which turn out to have nasty strings attached. But, at the microcode level, performance is still everything. And a well-tested fast algorithm may be necessary. As part of the climate crisis we should all be thinking about the efficiency of our code.

> On some machines indirection is slower with displacement, so the most-used member of a structure or a record should be first. Mike Morton. Boston, Massachusetts

We live in an age of ridiculously fast SSD and RAM access times. Sequential reads are still slightly faster than random jumps, and structures like [B-Tree](https://en.wikipedia.org/wiki/B-tree) give us a good mix of the two. We don't need to align data to the physical tracks of a spinning disk any more.

> In non-I/O-bound programs, a few percent of the source code typically accounts for over half the run time. Don Knuth. Stanford University

I wonder how true this now is? Perhaps we could replace "I/O" with "Internet requests" and still be accurate?

> Before optimizing, use a profiler to locate the “hot spots” of the program. Mike Morton. Boston, Massachusetts

Mostly true. But you don't lose much by doing some manual optimisations that you know (from bitter experience) will make a difference.

> [Conservation of Code Size] When you turn an ordinary page of code into just a handful of instructions for speed, expand the comments to keep the number of source lines, constant. Mike Morton. Boston, Massachusetts

I don't think this is relevant these days. Perhaps it is useful to spend time explaining exactly what trickery you're pulling off with weird syntax. But our tools are now line-count agnostic. Mostly.

> If the programmer can simulate a construct faster than the compiler can implement the construct itself, then the compiler writer has blown it badly. Guy L. Steele, Jr. Tartan Laboratories

I think this is rather self-evident. But compilers are so ridiculously optimised that this scenario is increasingly rare.

> To speed up an I/O-bound program, begin by accounting for all I/O. Eliminate that which is unnecessary or redundant, and make the remaining as fast as possible. David Martin. Norristown, Pennsylvania

I think this can be generalised even further. I'm reminded of [NPM's progress bar slowdown issue](https://github.com/npm/npm/issues/11283). There's a lot of redundancy which can be removed in many programs.

> The fastest I/O is no I/O. Nils-Peter Nelson. Bell Labs

Man! They were _obsessed_ with I/O back in the day! At large volumes, it is still an issue. But perhaps now we can relax just a little?

> The cheapest, fastest, and most reliable components of a computer system are those that aren’t there. Gordon Bell. Encore Computer Corporation

A little unfair, I think. It's cheaper to have less RAM, but that doesn't make my laptop faster.

> [Compiler Writer’s Motto-Optimization Pass] Making a wrong program worse is no sin. Bill McKeeman. Wang Znstitute

Personally, I don't think it is the compiler's job to tell me I'm doing it wrong.

> Electricity travels a foot in a nanosecond. Commodore Grace Murray Hopper. United States Navy

And a nano-Century is Pi seconds! One of those pub-trivia facts which are irrelevant to modern computing.

> LISP programmers know the value of everything but the cost of nothing. Alan Perlis. Yale University

Nowadays LISP programmers are a protected species and shouldn't be subject to such harsh treatment.

> [Little’s Formula] The average number of objects in a queue is the product of the entry rate and the average holding time. Richard E. Fairley. Wang Institute

Another of those truisms which kinda don't matter in a world with infinite disk space. Speed is our greatest worry.

[Documentation](https://shkspr.mobi/blog/2025/09/40-years-later-are-bentleys-programming-pearls-still-relevant/#documentation)
------------------------------------------------------------------------------------------------------------------------------

> [The Test of Negation] Don’t include a sentence in documentation if its negation is obviously false. Bob Martin. AT&T Technologies

I don't know if that's the same guy as [Uncle Bob](https://blog.wesleyac.com/posts/robert-martin) - but it sounds like the sort of claptrap he'd come up with. What's obvious to you might not be obvious to others. Test your writing with your audience to see if they understand your meaning.

> When explaining a command, or language feature, or hardware widget, first describe the problem it is designed to solve. David Martin. Norristown, Pennsylvania

Agreed. It doesn't need to be an essay, but documentation needs context.

> [One Page Principle] A (specification, design, procedure, test plan) that will not fit on one page of 8.5-by-11 inch paper cannot be understood. Mark Ardis. Wang Institute

I do have some sympathy with this - see the Two-Pizza rule above - but I think this ignores the reality of modern systems. Yes, we should keep things simple, but we also have to recognise that complexity is unavoidable.

> The job’s not over until the paperwork’s done. Anon

Amen!

[Managing Software](https://shkspr.mobi/blog/2025/09/40-years-later-are-bentleys-programming-pearls-still-relevant/#managing-software)
--------------------------------------------------------------------------------------------------------------------------------------

> The structure of a system reflects the structure of the organization that built it. Richard E. Fairley. Wang Institute

This is [Conway's Law](https://en.wikipedia.org/wiki/Conway%27s_law) and it is still fairly true. [Some studies show it is possible to break out of the paradigm](https://dl.acm.org/doi/10.1109/RESER.2013.14) but it holds remarkable power.

> Don’t keep doing what doesn’t work. Anon

If only we could tattoo this on the inside of our eyelids, eh?

> [Rule of Credibility] The first 90 percent of the code accounts for the first 90 percent of the development time. The remaining 10 percent of the code accounts for the other 90 percent of the development time. Tom Cargill. Bell Labs

Agile methodology has _somewhat_ dimmed the potency of this prediction. I think people are _generally_ better at estimating now. But it is hard to escape [Zeno's Paradox](https://shkspr.mobi/blog/2022/12/zenos-paradox-and-why-modern-technology-is-rubbish/).

> Less than 10 percent of the code has to do with the ostensible purpose of the system; the rest deals with input-output, data validation, data structure maintenance, and other housekeeping. May Shaw. Carnegie-Mellon University

How many times have you installed a simple program only to see it pull in every dependency under the sun? We need an awful lot of scaffolding to keep our houses standing.

> Good judgment comes from experience, and experience comes from bad judgment. Fred Brooks. University of North Carolina

I lean _slightly_ towards this. I also strongly believe that you can pick up a lot of good judgement by listening to your users.

> Don’t write a new program if one already does more or less what you want. And if you must write a program, use existing code to do as much of the work as possible. Richard Hill. Hewlett-Packard S.A. Geneva, Switzerland

This is the open source way. Much easier to fork than start again. But at some point you'll run up against an unwanted design decision which will be load-bearing. Think carefully before you re-use.

> Whenever possible, steal code. Tom Duff. Bell Labs

ITYM "Respect the terms of an OSI approved Open Source licence" - don't you, Tom?

> Good customer relations double productivity. Larry Bernstein. Bell Communications Research

A lesson learned by Apple and ignored by Google.

> Translating a working program to a new language or system takes 10 percent of the original development time or manpower or cost. Douglas W. Jones University of Iowa

I honestly don't know how true that is any more. Automated tools must surely have improved that somewhat?

> Don’t use the computer to do things that can be done efficiently by hand. Richard Hill. Hewlett-Packard S.A. Geneva, Switzerland

A rare disagreement! Things can be efficiently done by hand _once or twice_ but after that, go nuts! Even if it's something as simple as renaming a dozen files in a directory, you'll learn something interesting from automating it.

> I’d rather write programs to write programs than write programs. Dick Sites. Digital Equipment Corporation

There will always be people who love working on the meta-task. They're not wrong for doing so, but it can be an unhelpful distraction sometimes.

> [Brooks’s Law of Prototypes] Plan to throw one away, you will anyhow. Fred Brooks. University of North Carolina

I'd go further an suggest throwing out even more. It can be hard to sell that to management - but it is necessary.

> If you plan to throw one away, you will throw away two. Craig Zerouni. Computer FX Ltd. London, England

Craig with the double-tap!

> Prototyping cuts the work to produce a system by 40 percent. Larry Bernstein. Bell Communications Research

Minor disagreement. Prototyping _is_ part of the work. And it should probably take a considerable amount of time.

> [Thompson’s rule for first-time telescope makers] It is faster to make a four-inch mirror then a six-inch mirror than to make a six-inch mirror. Bill McKeeman. Wang Institute

Yes. It is always tempting to go for the big win. But baby-steps!

> Furious activity is no substitute for understanding. H. H. Williams. Oakland, California

Goodness me, yes! It's always tempting to rush in pell-mell. But that's a poor use of time.

> Always do the hard part first. If the hard part is impossible, why waste time on the easy part? Once the hard part is done, you’re home free. Always do the easy part first. What you think at first is the easy part often turns out to be the hard part. Once the easy part is done, you can concentrate all your efforts on the hard part. Al Schapira. Bell Labs

Oh, Al! You card! Luckily, there are very few "basic" problems to be solved in modern computing. We know what most of the hard problems are. Perhaps Agile teaches us to always leave software in a working state, so we start with the easy parts?

> If you lie to the computer, it will get you. Perry Farrar. Germantown, Maryland

We shouldn't anthropomorphise computers; they don't like it. Actually, nowadays it's is quite common to "lie" to computers with dummy data and virtualised environments. It's fine.

> If a system doesn’t have to be reliable, it can do anything else. H. H. Williams. Oakland, California

Perhaps it is my imagination, but we seem less concerned with reliability these days. A Tesla car is a wonderful example of that.

> One person’s constant is another person’s variable. Susan Gerhart. Microelectronics and Computer Technology Corp.

I wonder about this one a lot. Scoped access to variables possibly makes this less of an issue in the 21st century?

> One person’s data is another person’s program. Guy L. Steele, Jr. Tartan Laboratories

I don't quite get this. Anyone care to explain?

> Eschew clever rules. Joe Condon. Bell Labs

The pearls end with this gem.

[What have we learned today?](https://shkspr.mobi/blog/2025/09/40-years-later-are-bentleys-programming-pearls-still-relevant/#what-have-we-learned-today)
---------------------------------------------------------------------------------------------------------------------------------------------------------

The majority of my disagreements are minor quibbles. And while disk-bound I/O is rarely a problem, network latency has replaced it as the main cause of delays. We've managed to fix some things, but many seem irrevocably tied to the human condition.

Which one was your favourite?