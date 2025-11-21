Title: Programmers and Sadomasochism

URL Source: https://apenwarr.ca/log/20090222

Markdown Content:
**Programmers and Sadomasochism**

Quick! Take a look at the following snippet of HTML, and tell me what's wrong with it.

    <div align=right>Hello, world!</div>
If you said, "It's completely invalid and unparseable because you forgot the quotes around 'right'!" then you're... hold on, wait a second.(1)

Unparseable? Every web browser in history can parse that tag. Non-conforming XML, yes, but unparseable? Hardly. There are millions of web pages where people forgot (or didn't bother) to quote the values of their attributes. And because those pages exist, everyone who parses HTML _has_ to support that feature. So they do.

That's the difference between HTML and XML. With HTML, programmers answer to end users. And the end users are very clear: if your browser can't parse the HTML that every other browser can parse, then I'm switching to another browser.

XML is different. XML doesn't have any "end users." The only people who use XML parsers are other programmers. And programmers, apparently, aren't like normal people.

Real, commercial XML parsers, if fed a tag like the one above, would give me an error message. They would tell me to go back and fix my input. Apparently, I'm a bad person for even _suggesting_ that we should try parsing that file.

Now, as it happens, the [XML parser I wrote in 500 lines of Pascal](https://apenwarr.ca/log/?m=200902#20.html) a few days ago would _not_ reject this input. It would just pretend the quotes were there. In fact, if my program parses the file and then you ask it to print the XML back out, it'll helpfully add the missing quotes in for you.

Let's phrase this another way. The painstakingly written, professional-grade, "high quality" XML parser, when presented this input that I received from some random web site, will stab me in the back and make me go do unspecified things to try to correct the problem by hand. Avery's cheeseball broken XML parser, which certainly doesn't claim to be good or complete, would parse the input just fine.(2)

This, an innocent bystander might think, would imply that my parser is the better one to use. But it's not, you see, because, as [cdfrey points out](http://www.advogato.org/person/cdfrey/diary/50.html):

Interoperability is hard. Anyone can write their own parsers. And everyone has. That's why the monstrosity called XML was invented in the first place. It all starts with someone writing a quick and dirty parser, thereby creating their own unique file format whether they realize it or not.(3) And since they probably don't realize it, they don't document it. So the next person comes along, and either has to reverse engineer the parser code, or worse, guess at the format from existing examples.

Got it? By creating a permissive parser that just corrects simple input errors, **I've made things worse for everybody else.** I would make the world a better place if my parser would just _reject_ bad XML, and then everyone would be forced to produce files with _valid_ XML, and that would make life easier for people like me! Don't you see?

Well, no. There's a fallacy here. Let's look at our options:

**Option 1:** Bob produces invalid XML file and gives it to Avery. Avery uses professional-grade fancy pants parser, which rejects it. Avery is sad, but knows what to do: he phones up Bob and asks him to fix his XML producer. Bob is actually a guy in Croatia who hired a contractor five years ago to write his web site for him, and doesn't know where to find that contractor anymore, but because he knows it's better for the world, he finds a new contractor who fixes the output of his web site. Three weeks later, Bob sends a new XML file to Avery, who is now able to parse it.

**Option 2:** Bob produces invalid XML file and gives it to Avery. Avery's permissive parser that he wrote in an afternoon reads it just fine. Avery goes on with his work, and Bob doesn't need to pay a contractor.

**Option 3:** Bob produces valid XML in the first place, dammit, because he made sure his contractor ran his program's output successfully through a validator before he accepted the work as complete. Avery parses it easily, and is happy.

Now, obviously option 3 is preferable. The problem is, it's also not a real option. Bob already screwed up, and he's producing invalid XML. Avery has received the invalid data, and he's got to do something with it. Only options 1 and 2 are real.

Now, XML purists are telling me that I should pursue option 1. My question is: why? Option 1 keeps me from getting my work done. Then I have to go bother Bob, who wouldn't care except that I'm so obnoxious. And now he has to pay a contractor to fix it. The only reason I would take option 1 is if I enjoy pain, or inflicting pain on others. Apparently, lots of programmers out there enjoy pain.

Meanwhile, option 2 - the one that everybody frowns upon - is painless for _everyone_.

The usual argument for option 1 is that if enough people do it, then eventually people will Just Start Producing Valid XML Dammit, and you won't ever have this problem again. But here's the thing: we have a world _full_ of people trying option 1. XML is _all about_ the people who try option 1. And _still_ Bob is out there, and he's still producing invalid XML, and I, not Bob, am still the one getting stabbed in the back by your lametarded strict XML parsers. **Strict receiver-side validation doesn't actually improve interoperability, ever.**

As programmers, we've actually known all this for a long time. It's called [Postel's Law](http://en.wikipedia.org/wiki/Postel's_law), in honour of Jon Postel, one of the inventors of the Internet Protocol. "Be liberal in what you accept, and conservative in what you send."

The whole Internet runs on this principle. That's why HTML is the way it is. It's why Windows can talk to Linux, even though both have lots of bugs.

I have my own way of phrasing Postel's law: "It takes two to miscommunicate."

As long as _either_ side of any transaction is following Postel's law - either the sender strictly checks his XML for conformance _or_ the receiver doesn't - the transaction will be a success. If _both_ sides disregard his advice, that's when you have a problem.

Yes, Bob should have checked his data before he sent it to me. He didn't. That makes him a bad person - or at least an imperfect one. But if I refuse the data just because it's not perfect, then that doesn't solve the problem. It just makes me a bad person too.

**Footnotes**

(1) People who, instead, were going to complain that I should avoid the obsolete HTML 'align' attribute and switch to CSS would be the subject of a completely different rant.

(2) Note that there's plenty of perfectly valid XML that my cheeseball incomplete XML parser wouldn't parse, because it's cheeseball and incomplete. The ideal parser would be permissive _and_ complete. But if I have to choose one or the other, I'm going to choose the one that actually parses the files I got from the customer. Wouldn't you?

(3) If you didn't catch it, the precise error in cdfrey's argument is this: You don't create a new file format by _parsing_ wrong. You create a new file format by _producing_ wrong. Ironically, a lot of people use strict professional-grade XML _parsers_ but seem to believe that _producing_ XML is easy.

**Side note**

By the way, even strict XML validation doesn't actually mean the receiver will understand your data correctly. It's semantics vs. syntax. You can easily write a perfectly valid HTML4-Strict compliant document and have it render differently in different browsers. Why? Because they all _implement_ the CSS differently. Web browser interoperability problems actually have nothing to do with HTML parsing; it's all about the rendering, which is totally unrelated. It's amazing to me how many people think strict HTML validation will actually solve any real-world problems.

**Update (2009/02/22):**[cdfrey responds](http://www.advogato.org/person/cdfrey/diary/52.html) to my response. Then he wrote an interesting essay about [Postel's law](http://www.advogato.org/person/cdfrey/diary/53.html), too. See also the [ycombinator discussion](http://news.ycombinator.com/item?id=490366) of this article, and the [reddit discussion](http://www.reddit.com/r/programming/comments/7zbp5/programmers_and_sadomasochism/).

::li