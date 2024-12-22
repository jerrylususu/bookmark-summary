Title: The Untold Story of SQLite - CoRecursive Podcast

URL Source: https://corecursive.com/066-sqlite-with-richard-hipp/

Markdown Content:
_Note: This podcast is designed to be heard. If you are able, we strongly encourage you to listen to the audio, which includes emphasis that’s not on the page_

**Introduction**
----------------

**Adam:** Hello and welcome to CoRecursive. I’m Adam Gordon Bell. Each episode of CoRecursive, someone shares the fascinating story behind some piece of software being built. On April 1st, 2014, an open source maintainer got an email from Google about a security issue, and this was not an April Fool’s joke. This was HeartBleed and the project was OpenSSL. 17% of the world’s web servers were affected, and by the time the dust settled, people started asking questions like, “Why was this open source maintainer who received only $2,000 in donations a year responsible for 17% of the world’s encrypted web traffic?”

Ever since then, I’ve been curious about these critical pieces of infrastructure. What happens if your fun side project ended up powering the world? Do you try to monetize it? Do you focus on it full time? Does the weight of the maintenance crush you and you just leave computers and go to focus on building furniture? I have a purpose guest for discussing this topic.

**Richard:** I’m Richard Hipp and I work on SQLite.

**Adam:** Today’s show, I’m talking to Richard about how to survive becoming core infrastructure for the world. SQLite is everywhere. It’s in your web browser, it’s in your phone, it’s probably in your car, and it’s definitely in commercial planes. It’s where your iMessages and WhatsApp messages are stored, and if you just do a find on your computer for \*.db, you’ll be amazed at how many SQLite databases you find. Today, Richard is going to share his story. The idea for SQLite actually came out of his frustrations with an existing database called Informix that was installed on a literal battleship.

**The Battleship**
------------------

**Adam:** Richard was a contractor for Bath Iron Works working on software for the DDG-79 Oscar Austin. That is a battleship, the type that protects a fleet by being armed to the hilt.

**Richard:** There’s a big, complex ship, and stuff’s always breaking. Suppose a pipe ruptures. You need to isolate that damage by closing valves on either side of the pipe, but then you also need to open valves elsewhere to restore the working fluid to other systems that are downstream so that they don’t go offline, and locating all those valves and whether you open them or close them can get very complicated, and so Automated Common Diagrams is a program that says, “Oh, here’s the problem. Here’s the valves you close. Here’s the valves you open. Here’s where they’re located.”

That was the original problem, and all the data for where all the pipes are running and all the valves are located, that was in the database. The computer was already installed on the ship. We didn’t have any control over that. The database was already installed on the ship. We didn’t have any control over that. We just had to use what was there.

**NP-Complete Problems**
------------------------

**Adam:** Richard was brought in because the solution to this problem was computationally complex and Richard was known for solving hard problems.

**Richard:** Really, when you come right down to it, the types of systems that are designed by humans tend to be solvable in polynomial time. It’s just, the general description of the problem, where you have an arbitrary directed graph, is NP-complete, so, they were trying to write code that would solve this, and they hadn’t analyzed it and they didn’t realize this. They were, “You know, we’re not getting a solution. It’s just running forever and chewing up CPU cycles. What’s going on?” Well, that’s because it’s in NP-complete, and so you have to use heuristics that will find fast approximate solutions and put lots of things in there to verify that it’s not stuck in a loop somehow, and really, for the way they design these ships, the heuristics can find the exact solution, the optimal solution pretty quickly in every case, but it’s just, you can’t write a simple, naïve algorithm and expect it to finish quickly because you will get stuck in an exponential search, trying every valve combination to see which one’s going to give you the best solution.

I was leading a team that was working on this, but Informix just wasn’t really working really well. Once it was working, it worked great, but sometimes the server would go down, and then our application wouldn’t run, and that was embarrassing. Dialog box would pop. They’d double click on the thing and a dialog box would pop that says, “Can’t connect to database server,” and it wasn’t our fault. We didn’t have any control over the database server, but what do you do if you can’t connect to the server, so we got the blame all the same because we were painting the dialog box.

**Adam:** Yeah. I can imagine, when some pipe bursts and they try to use your program and they get a database error, they’re not too happy.

**Richard:** No. No, and of course, it’s a war ship, so, of course, things are always breaking and they use it all the time, but the idea is it’s supposed to be able to work if you take battle damage, so it’s more than one pipe breaking and there’s going to be a lot of stuff broke, and people are going to be crazy and there’s going to be smoke and blood and chaos, and in a situation like that they don’t want a dialog box that says, “Cannot connect to database server.” That’s just not what they want to see, so it needs to be reliable. All we’re doing is reading the data into RAM. We’re not doing transactions. We’re not doing anything like that. It’s just, we’re pulling a bunch of data into memory so that we can solve this problem.

Why do we even need a server? Why can’t I pull this directly off the disk drive? That way if the computer is healthy enough, it can run our application at all, we don’t have dependencies that can fail and cause us to fail, and I looked around and there were no SQL database engines that would do that, and one of the guys I was working with says, “Richard, why don’t you just write one?” “Okay, I’ll give it a try.” I didn’t do that right away, but later on, it was a funding hiatus. This was back in 2000, and if I recall correctly, Newt Gingrich and Bill Clinton were having a fight of some sort, so all government contracts got shut down, so I was out of work for a few months, and I thought, “Well, I’ll just write that database engine now.”

**Building SQLite V1**
----------------------

**Adam:** This is the year 2000. Wikipedia didn’t exist yet. People with internet were mainly using dial-up, and only 1% of US households had broadband internet. You couldn’t just Google how to build a database and get pointed in the right direction, but Richard had a plan based on his previous experience building compilers.

**Richard:** If we think about each SQL statement as a program, my task is to take that program and compile it into some sort of executable code, so I wrote a byte code engine that would actually run a query and then I wrote a compiler that would translate SQL into that byte code and voila, SQLite was born. It wasn’t really used for that project that I was working on, because, well, that one was shut down at the time, but it started back up later, and we incorporated it into that project for testing purposes because the customer’s insisting on Informix, so that’s fine, but Informix is a real hassle to use for development.

For development purposes, we would use my engine just for testing and whatnot, but it was never an official part of the project, but I put it out there on the internet and other people started picking it up. I remember, this was before Twitter or anything like that, but there was netnews back then, and \[inaudible 00:07:42\] somebody put a posting \[inaudible 00:07:43\], was like, “Wow, I’ve got an SQL database running on my Palm Pilot.” I’m not kidding. It really attracted a lot of attention, and that encouraged me to work on it.

**Motorola Phones**
-------------------

**Adam:** Richard kept tinkering with his database project on the side until he got a phone call from a tech giant.

**Richard:** It was from Motorola. Back, 2002, 2001 when this happened, Motorola was one of the tech giants, and these days, the tech giants are Apple and Android and Google and Microsoft and Facebook, but back then the tech giants were things, people like AOL and Motorola and Nokia, so I got a phone call from some people at Motorola and they said, “Listen, we’re designing a new cell phone operating system and we want SQLite to be part of it. Can you support this for us?” Of course, I was real cool about it, said, “Oh, sure, sure. I can do that for you,” but they said, “Well, do you have any pricing information?” “Well, look, I tell you what, let’s have a call tomorrow and I’ll get back to you on that.”

Of course, inside, I was like, “What? You can make money with open source software? How does this work? How do I price this? I have no idea how to do this.” I scrambled around and came up with some pricing strategy. They wanted some enhancements to it so it could go in their phones, and I gave them a quote and at the time, I thought this was a quote for all the money in the world. It was just huge.

**Adam:** What was it? Can you share?

**Richard:** I think it was $80,000 or something like that. It was not very much money by today’s standards, but for me, that was everything, and I brought three of the guys that I’d worked with on to work on it, and we worked that project and that was sort of the beginning.

**America Online Phones**
-------------------------

**Adam:** After Motorola, the next tech giant to reach out was America Online, who wanted Richard to visit their office and talk about a contract for some enhancements they needed.

**Richard:** This was back when AOL was the world’s leading service provider. Maybe you’re too young to remember, Adam. We used to get …

**Adam:** The CDs …

**Richard:** yeah, CDs in the mail. Yeah, you know, the CD. Put this in your thing and $10 a month. They needed a database on that CD, and they had some ad hoc thing and they wanted to use SQLite on that. They had limited space, and so, “Hey, we need to put this on the CD.” I just put in this new feature which I thought was a really cool idea, that you could create a temp index on a real table, so a table is shared amongst processes, you can create a temporary index on it, and I thought that was a really cool idea. I was up there telling them about this, and mid-sentence, as I was getting ready to explain what this temp index, it suddenly occurred to me that if you have a temporary index, only one of the users of the database sees that index and if somebody else, one of the other users, updates the primary table, the index will go stale. I was sitting in their office, had several people there, they were getting ready to hire me to do something, and I was getting ready to brag to them about this new feature when it suddenly occurred to me that it was fundamentally broken, and so, mid-sentence, I had to change my thought and come up with something else to say.

**Adam:** That’s awesome.

**Symbian OS and Nokia**
------------------------

**Adam:** Is that how the engagements usually happened? Did they ask you to come down to their office?

**Richard:** Yeah, that’s how that happened. One of big early customers that really set us on the road to making this work well was Symbian. The Symbian OS was the operating system on Nokia phones, and they gave me a call and they wanted me to fly over to London to their headquarters, want to have a discussion. The meeting was going to be Thanksgiving day. They didn’t know this. They gave me the date. It’s Thanksgiving Day. I didn’t tell them, because they don’t do Thanksgiving in UK. You don’t do Thanksgiving in Canada.

**Adam:** We do. We have it on a different day, though.

**Richard:** Okay. Well, yeah, you don’t do the American Thanksgiving, so, sure, I’ll fly to London on Thanksgiving day and have a meeting there. Traditionally, we go to my wife’s family for Thanksgiving, so that year, she showed up to the big family … Because, all the cousins are there and everything, she shows up there without me and everybody’s thinking, “Uh oh. Is there something wrong?” She had to go and explain, “Oh, no. Richard’s in London at a meeting,” but they flew me over, and come to find out that they had run a big bake-off. They wanted a database engine for Symbian OS and they had a bake-off. They had 10 different database engines, two other open-source entrants, and seven proprietary entrants, and they’d run them all on the data set to see which one would best suit their needs, and SQLite had won.

All the other nine, they’d given the vendors the opportunity to tune, but we won. Who knew? They flew me over and said, “Hey, yeah, this is great. We want this but we need some enhancements.” I said, “Great,” and we cut a contract to do some development work for them.

**The Bus Factor and the Consortium**
-------------------------------------

**Richard:** At this point, we were really into this, and I was kind of doing this full time, but they came to us and said, “Look, we need you to increase the bus factor.” The bus factor means, the number of people who have to be hit by a bus in order to stop all development work, and they felt like the bus factor at SQLite was too … This was their words. They wanted us to start the SQLite Consortium, which was a way of funding the project and getting more people involved to guarantee that it was going to be available long term, so we started this big thing and I came up with a bunch of ideas, and it was this crazy thing where all the Consortium members had voting rights, and it was this big thing.

Somehow or another, and I don’t know how this happened, Mitchell Baker, she’s the woman who runs the Mozilla Foundation, she got wind of this and called me up, says, “Richard, you’re doing this all wrong. Let me tell you how to set up a consortium.” She laid down the law, says, “Look, the developers have to be in control. Their decision is final. No voting rights on what gets to go into it. The companies that are using, they get the honor of contributing money, but you make all the decisions.” She was very adamant about this and she laid out everything. She’s a lawyer.

I’m like, “How do we get people to join? What’s the incentive?” Said, “Don’t worry about that. They will join. Just don’t worry about it, and in fact, if you do this, Mozilla will be one of the founding members.” Put it out there and sure enough, we got support from Mozilla and Symbian and Adobe, and they started the SQLite Consortium with those three, but we’re very blessed to have been this … Like I say, I didn’t plan any of this. When Symbian said, “Oh, you need a consortium,” I didn’t know what to do. I don’t know how Mitchell Baker heard about it, and literally phoned me up and said, “You’re doing it wrong.”

I don’t know how that happened, but it did, and it’s been such an amazing journey, because we would not be in this situation were it not for these circumstances.

**Enter Android**
-----------------

**Adam:** By this time, all major smartphones were using SQLite, and so Richard got to see early smartphone development from all sides. Embedded development like building a smartphone can be a slow process, long iteration loops, time spent waiting for things to be flashed onto new prototypes, people working off breadboards that look nothing like finished products. At this point Richard was contacted by Google: an outsider to cellphones and embedded development.

**Richard:** This was back in 2005 or so, and we were in meetings with Android, and this was before Android was a thing. This was before iPhone, and I was in Mt. View and we were working with a fella, and they had a prototype of their Android phone, and this was before iPhone, so back then, the phones, they had the full QWERTY keyboard at the bottom and a smaller window up on top, like a Blackberry, but we were debugging something with SQLite and we were plugging into the phone and we were running the debugger on a workstation which was pretty amazing. Nobody else could do that, but we had the phone in the debugger and the phone rings, and he looks at it and he says, “Oh, this is my wife. I have to take this call, excuse me.”

I left the room so he could have this conversation, and of course I stayed completely cool about this, but inside my mind it was exploding because, here we were, we were debugging an application in GDB on a phone that was on the public network, and this was utterly mind blowing. Nobody at Motorola, nobody at Symbian, nobody at Nokia had anything close to that, and in that one moment, I knew that Android was going to be huge.

**Guys, This Is Important**
---------------------------

**Adam:** How did they work on phones, like, Nokia? A much slower process, I assume.

**Richard:** There was a much longer cycle time between hardware and software updates, and that was the thing, is that the Android people were burning a new operating system and pushing it onto working phones that they were carrying around and working on the public network, multiple times per day, whereas that was a 30 day cycle for anybody else. I was under NDA. It was clearly a prototype. The case looked like it had been 3D printed. It wasn’t like it was a production ready phone, but it was portable, whereas the engineers that other companies, they had the big breadboard prototypes, the big full sized prototyping board, and the phone would run on that, and it was not connected to a radio so they couldn’t actually use it as a phone.

I could not tell anybody. I could not go to Motorola. I could not go to Symbian and said, “Guys, this is important. You need to fix this. I couldn’t tell them,” and that made the difference. That was kind of their undoing, I’m afraid.

**Testing and Aviation Standards**
----------------------------------

**Adam:** By this point, Richard’s database is really picking up steam. He’s a talented guy and I’m sure his team is super capable, but some software consulting company of one to four people supporting the install base of every Android and Motorola and Nokia phone, and this is a database. Developers are hard on databases, and people don’t like it when their data has issues.

**Richard:** We were going around boasting to everybody naively that SQLite didn’t have any bugs in it, or no serious bugs, but Android definitely proved us wrong. Look, I used to think that I could write software with no bugs in it. It’s amazing how many bugs will crop up when your software suddenly gets shipped on millions of devices.

**Adam:** I bet.

**Richard:** It is truly amazing. They were getting crashes constantly, and about that same time or slightly before them, I’d been doing some work for Rockwell Collins, an avionics manufacturer, Rockwell Collins, and they introduced me to this concept of DO-178B. It’s a quality standard for safety-critical aviation products, and unlike so many quality standards, this one’s actually readable. Now, it does have a lot of bureaucratic stuff in it, but you can actually buy a copy of this. You do have to buy it. It’s a couple hundred dollars, but it’s a reasonably thin volume and you can read through it, and with sufficient study you can understand what they’re talking about, so I did that, and I actually started following some of their processes, and one of the key things that they push is, they want 100% MCDC test coverage.

That’s modified condition decision coverage of the code. Your tests have to cause each branch operation in the resulting binary code to be taken and to fall through at least once.

**Adam:** Oh, so it’s at the level of actual assembly, at the machine code level.

**Richard:** At the machine code level. Yeah. Actually, MCDC’s a little stricter than that. Let’s not dwell on the details, but I had this idea, I’m going to write tests to bring SQLite up to the quality of 100% MCDC, and that took a year of 60 hour weeks. That was hard, hard work. I was putting in 12 hour days every single day. I was just getting so tired of this because with this sort of thing, it’s the old joke of, you get 95% of the functionality with the first 95% of your budget, and the last 5% on the second 95% of your budget. It’s kind of the same thing. It’s pretty easy to get up to 90 or 95% test coverage. Getting that last 5% is really, really hard and it took about a year for me to get there, but once we got to that point, we stopped getting bug reports from Android.

**Adam:** Oh, wow.

**Richard:** Yeah. IT just worked from there on out. It made a huge, huge difference. We just didn’t really have any bugs for the next eight or nine years.

**Billions of Tests**
---------------------

**Adam:** How many test cases is that? What does that look like?

**Richard:** The first test was just written in TCL, and that was normal developer tests.

**Adam:** Then, after that you had the airplane ones? How much was that?

**Richard:** Right. We still maintain the first one, the TCL tests. They’re still maintained. They’re still out there in the public. They’re part of the source tree. Anybody can download the source code and run my test and \[inaudible 00:21:55\] run all those. They don’t provide 100% test coverage but they do test all the features very thoroughly. The 100% MCD tests, that’s called TH3. That’s proprietary. I had the idea that we would sell those tests to avionics manufacturers and make money that way. We’ve sold exactly zero copies of that so that didn’t really work out. It did work out really well for us in that it keeps our product really solid and it enables us to turn around new features and new bug fixes very fast.

How do you count tests? We’ll have a test case but it’ll be parametrized, so that one test case might run 100, 1,000, 100,000 tests, just by looping, by changing one of the parameters. For a typical release, we’ll do billions of tests, but we have, I think it’s on the order of 100,000 distinct test cases.

**Adam:** 100,000 distinct test cases, and then they’re parametrized, so then, how many …

**Richard:** Yes, so we’ll do billions of tests.

**Adam:** Oh, wow.

**Richard:** Yeah. We have a check list and we will run tests for at least three days prior to a release.

**Adam:** Is that on one machine or do you …

**Richard:** No, but we intentionally test on different operating systems. I’ve got some old equipment around here, because these days, all CPUs are little endian, Intel by order, but it wasn’t so long ago that there was a lot of big endian CPUs around. I’ve got a PowerPC iBook up here that we run tests one. We make sure that SQLite works correctly on a big endian platform. We test on 32-bit platforms, test on ARM. We test on Intel chips. We test on 64-bit platforms. We test on Windows and Linux and Mac, OpenBSD, so we test on as many different platforms, as many different operating systems as we can, but we also have lots of different test suites that we run, but we’ve got the original TCL tests. We’ve got TH3. We’ve got the custom fuzzer stuff that are running constantly. We’ve got a thing called SQL logic test.

Shane Harrelson did this for us about 10 years ago. He came up with this huge corpus of SQL statements, and he ran them against every database engine that he could get his hands on. We wanted to make sure everybody got the same answer, and he managed to segfault every single database engine he tried, including SQLite, except for Postgres. Postgres always ran and gave the correct answer. We were never able to find a fault in that. The Postgres people tell me that we just weren’t trying hard enough. It is possible to fault Postgres, but we were very impressed.

We crashed Oracle, including commercial versions of Oracle. We crashed DB2. Anything we could get our hands on, we tried it and we managed to crash it, but the point was that we wanted to make sure that SQLite got the same answers for all of these queries, or equivalent answers, because a lot of these queries, they’re indeterminate and the rows might come out in a different order because you \[crosstalk 00:25:10\] order by clause, so we wanted to make sure that all the database engines got equivalent answers. Mostly, we wanted to make sure that SQLite was getting the same answers everybody else is.

That’s another test suite, and then we have lots of smaller ones, as well. Between them all, it’s a lot of testing code, and it takes a long time to run.

**Building From First Principles**
----------------------------------

**Adam:** It’s these tests that allow SQLite to continue improving and evolving. They let Richard be confident in each release, even if large parts of the code base change, and large parts do occasionally get rewritten, as improved ways to structure things are discovered. Remember, Richard built SQLite to run first principles.

**Richard:** Origonally, when I set out to write it, I went around looking, is there a reference on how to write an SQL database engine, I found nothing, and so I just had to kind of invent it myself, so it was a completely independent mission. Most of the theory was happening at MIT and Harvard up in Cambridge, or down at Berkeley, but if you didn’t go to one of those three schools, you didn’t even know this body of theory existed, and there wasn’t a real good way to find it. It’s curious, though, if you go back and look at the volcano model used by Postgres and the byte code model used to be SQLite, we converged on all the same ideas.

They start out very differently at the top but we converge in all the same areas of how to make it go faster, so I think that that’s kind of a validation in theory. Two independent lines of development came up with the same answer. I had never heard of, for example, a covering index. I was invited to fly to a conference, it was a PHP conference in Germany somewhere, because PHP had integrated SQLite into the project. They wanted me to talk there, so I went over and I was at the conference, but David Axmark was at that conference, as well. He’s one of the original MySQL people.

David was giving a talk and he explained about how MySQL did covering indexes. I thought, “Wow, that’s a really clever idea.” A covering index is when you have an index and it has multiple columns in the index and you’re doing a query on just the first couple of columns in the index and the answer you want is in the remaining columns in the index. When that happens, the database engine can use just the index. It never has to refer to the original table, and that makes things go faster if it only has to look up one thing.

**Adam:** It becomes like a key value store, but just on the index.

**Richard:** Right, right, so, on the fly home, on a Delta Airlines flight, it was not a crowded flight. I had the whole row. I spread out. I opened my laptop and I implemented covering indexes for SQLite mid-Atlantic.

**Adam:** That’s awesome.

**B-Trees and the Art of Computer Programming**
-----------------------------------------------

**Richard:** You just pick things up. People tell you these things, and that happened to some with Bloomberg. They’d come to us and say, “Hey, why aren’t you doing this optimization,” and I said “Never occurred to me.” “Well, can you do it?” “Let’s see what we can do,” and then it would go in, so, yeah, kind of figure it out as you went along. I had to invent a lot of this myself. Nobody ever taught me about a B tree. I had heard of it. When I went to write my own B tree, on the bookshelf behind me, I’ve got Don Knuth’s The Art of Computer Programming, so I just pulled that down, I flipped to the chapter on searching and looked up B trees and he described the algorithm. That’s what I did.

Funny thing, Don gives us details on the algorithm for searching a B tree and for inserting into a B tree. He does not provide an algorithm for deleting from the B tree. That’s an exercise at the end of the chapter, so before I wrote my own B tree I had to solve the exercise at the end. Thanks, Don. I really appreciate it.

**Adam:** That’s awesome. Did you pull anything else from that book?

**Richard:** Well, it’s an amazing volume. I can’t give you a specific example, but from my era, everybody has to have read or at least skimmed through, at least browsed through The Art of Computer Programming, and know that algorithms that are there, maybe not Don’s exact implementation. I mean, I never took the time to learn MIX, which is his assembly language, but it’s useful to flip through and look at all the algorithms he talks about. I think that just a year or two ago I needed a pseudorandom number generator, and I was, “Let’s see what Don recommends.” You pull it off. You see what he does.

**Freedom To Build It Yourself**
--------------------------------

**Adam:** Building your own random number generator, starting from an algorithm description in The Art of Computer Programming that you literally have on the shelf behind you in your office, it seems like such a different way to work than I’m used to. SQLite has basically no dependencies that Richard didn’t build himself, except the C compiler and a couple of things from libc. He even built his own source control system and his own bug tracker. What this gives Richard is freedom.

**Richard:** Have you ever thought about the word freedom, what that means? Freedom means taking care of yourself. People go backpacking or stuff, they go on these long hikes, backpacking, where they carry everything they need on their back and they talk about how freeing that is because they are taking care of themselves. That’s what freedom means, and so, when you write the whole thing yourself, there’s a certain element of freedom in that, because you’re not tied to somebody else. You’re not dependent on different vendor providing you something. Suppose I had elected to go with Berkeley DB as the storage engine for SQLite version two.

Well, at that time Berkeley DB was open source, but then later it was sold off to Oracle, and it became a duel source proprietary model and you can’t get hold of the source code to the later versions without paying license fees, yada, yada, yada, so, suddenly it becomes a problem. The parser generator in SQLite is one that I wrote myself years ago called Lemon, and because, rather than using Yak or Bison, I used my own, and you think, “Why did you do that?” Well, it turns out that when I needed some new language features that you couldn’t get out of Yacc or GNU Bison, because I owned the parser generator I could change it to do what I wanted when I needed a version control system for SQLite. It started out using CVS because, back in 2000, every project used CVS. That was the dominant version control system, but moving on into the mid-2000s, we needed something better and the whole idea of distributed version control had become a thing.

**Building Fossil**
-------------------

I looked at Git, I looked at Mercurial, and I looked at my requirements and I thought, “You know what? I’m just going to write my own,” so I wrote my own version control system, which is now a project unto itself, and that worked out very, very well, because think, Linus Torvalds wrote Git to support the Linux kernel, and it is perfectly designed to serve the needs of the Linux kernel development community. If you’re working on the Linux kernel, Git is absolutely the perfect version control system.

Now, if you’re working on something else, though, maybe not so much, and so, it’s a perfectly atrocious version control system for working for SQLite. Fossil is absolutely the perfect version control system for working in SQLite, and I wrote it for that purpose, and so, because I wrote it myself, it exactly meets my needs and is the perfect product for what it’s doing, so by doing things yourself, you control your own destiny, you have more freedom, you’re not dependent upon third parties.

**Being Self Sufficient**
-------------------------

**Richard:** It’s a very liberating experience. I kind of think of myself … I don’t know whether it’s this phenomenon that you can see on YouTube about people living off-grid and they go out and they buy a little bit of land and they’re going to raise their own food and they’re going to live off grid and stuff. What do they call that?

**Adam:**

Survivalist, or preppers?

**Richard:** Preppers, maybe. Maybe it’s preppers, but they’re not necessarily loo