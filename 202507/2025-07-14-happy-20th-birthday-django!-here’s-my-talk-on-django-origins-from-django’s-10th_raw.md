Title: Happy 20th birthday Django! Here’s my talk on Django Origins from Django’s 10th

URL Source: https://simonwillison.net/2025/Jul/13/django-birthday/

Published Time: Mon, 14 Jul 2025 13:34:00 GMT

Markdown Content:
13th July 2025

Today is the [20th anniversary](https://www.djangoproject.com/weblog/2025/jul/13/happy-20th-birthday-django/) of [the first commit](https://github.com/django/django/commit/d6ded0e91bcdd2a8f7a221f6a5552a33fe545359) to the public Django repository!

Ten years ago we threw a multi-day 10th birthday party for Django back in its birthtown of Lawrence, Kansas. As a personal celebration of the 20th, I’m revisiting the talk I gave at _that_ event and writing it up here.

Here’s [the YouTube video](https://www.youtube.com/watch?v=wqii_iX0RTs). Below is a full transcript, plus my slides and some present-day annotations.

#### Django Origins (and some things I have built with Django)

_Presented 11th July 2015 at Django Birthday in Lawrence, Kansas_

My original talk title, as you’ll see on your programs, was “Some Things I’ve Built with Django.” But then I realized that we’re here in the birthplace of Django, celebrating the 10th birthday of the framework, and nobody’s told the origin story yet. So, I’ve switched things around a little bit. I’m going to talk about the origin story of Django, and then if I have time, I’ll do the self-indulgent bit and talk about some of the projects I’ve shipped since then.

I think Jacob’s introduction hit on something I’ve never really realized about myself. I do love shipping things. The follow-up and the long-term thing I’m not quite so strong on. And that came to focus when I was putting together this talk and realized that basically every project I’m going to show you, I had to dig out of the Internet Archive.

_Ten years on from writing this talk I’m proud that I’ve managed to overcome my weakness in following-up—I’m now actively maintaining a bewildering array of projects, having finally figured out how to [maintain things](https://simonwillison.net/2022/Nov/26/productivity/) in addition to creating them!_

But that said, I will tell you the origin story of Django.

![Image 1: adrian holovaty blog post  May 31, 2003, 11:49 AM ET Job opportunity: Web programmer/developer  I interrupt this blogging hiatus to announce a job opportunity.  World Online, my employer here in beautiful Lawrence, Kansas, is looking for another Web programmer to help build cool stuff for our three sites, ljworld.com, lawrence.com and kusports.com ... ](https://static.simonwillison.net/static/2025/django-birthday/django-birthday02.jpg)

[#](https://simonwillison.net/2025/Jul/13/django-birthday/#django-birthday02.jpg)

For me, the story starts very much like Jacob’s. I was reading RSS feeds back in 2003, and I saw [this entry on Adrian’s blog](https://www.holovaty.com/writing/211/), talking about a job opportunity for a web programmer or developer in Lawrence, Kansas.

Now, I was in England. I was at university. But my university had just given me the opportunity to take a year abroad, to take a year out to do an internship year in industry. My girlfriend at the time was off to Germany to do her year in industry. So I was like, well, you know, do I stay at university? And then this comes along.

So I got in touch with Adrian and said, you know, could this work as a year-long internship instead? And he was reading my blog and I was reading his blog, and we knew that we aligned on a bunch of things. So we thought we’d give it a go.

Now, if you look through this job ad, you’ll see that this is all about expert knowledge of PHP and experience designing and maintaining databases, particularly MySQL. So this was a PHP and MySQL gig.

But when I arrived in Kansas, we quickly realized that we were both kind of over PHP. You know, we’d both built substantial systems in PHP, and we were running up against the limits of what you can do in PHP and have your code still be clean and maintainable.

And at the same time, we were both reading [Mark Pilgrim’s blog](https://web.archive.org/web/20020324174618/http://diveintomark.org/) (archive link). Mark Pilgrim had been publishing Dive into Python and making a really strong case for why Python was a great web language.

So we decided that this was the thing we wanted to do. But we both had very strong opinions about how you should build websites. Things like URL design matters, and we care about the difference between get and post, and we want to use this new thing called CSS to lay out our web pages. And none of the existing Python web frameworks really seemed to let us do what we wanted to do.

![Image 2: Lawrence JOURNAL-WORLD ](https://static.simonwillison.net/static/2025/django-birthday/django-birthday03.jpg)

[#](https://simonwillison.net/2025/Jul/13/django-birthday/#django-birthday03.jpg)

Now, before I talk more about that, I’ll back up and talk about the organization we’re working for, the [Lawrence Journal World](https://en.wikipedia.org/wiki/Lawrence_Journal-World).

David [gave a great introduction](https://www.youtube.com/watch?v=FDsqFD4pDy4) to why this is an interesting organization. Now, we’re talking about a newspaper with a circulation of about 10,000, like a tiny newspaper, but with a world-class newsroom, huge amounts of money being funneled into it, and like employing full-time software developers to work at a local newspaper in Kansas.

![Image 3: Rob Curley (and a photo of Rob)](https://static.simonwillison.net/static/2025/django-birthday/django-birthday04.jpg)

[#](https://simonwillison.net/2025/Jul/13/django-birthday/#django-birthday04.jpg)

And part of what was going on here was this guy. This is Rob Curley. He’s been mentioned a few times before already.

![Image 4: Unofficial mission statement: “build cool shit” ](https://static.simonwillison.net/static/2025/django-birthday/django-birthday05.jpg)

[#](https://simonwillison.net/2025/Jul/13/django-birthday/#django-birthday05.jpg)

And yeah, Rob Curley set this unofficial mission statement that we “build cool shit”. This is something that Adrian would certainly never say. It’s not really something I’d say. But this is Rob through and through. He was a fantastic showman.

And this was really the appeal of coming out to Lawrence, seeing the stuff they’d already built and the ambitions they had.

![Image 5: Screenshot of Lawrence.com - Focus on Kansas. Community blogs, calendars, merch, links to movies, video games, eating out and more.](https://static.simonwillison.net/static/2025/django-birthday/django-birthday06.jpg)

[#](https://simonwillison.net/2025/Jul/13/django-birthday/#django-birthday06.jpg)

This is Lawrence.com. This is actually the Lawrence.com written in PHP that Adrian had built as the sole programmer at the Lawrence Journal World. And you should check this out. Like, even today, this is the best local entertainment website I have ever seen. This has everything that is happening in the town of Lawrence, Kansas population, 150,000 people. Every gig, every venue, all of the stuff that’s going on.

And it was all written in PHP. And it was a very clean PHP code base, but it was really stretching the limits of what it’s sensible to do using PHP 4 back in 2003.

So we had this goal when we started using Python. We wanted to eventually rebuild Lawrence.com using Python. But in order to get there, we had to first build -- we didn’t even know it was a web framework. We called it the CMS.

![Image 6: 6 Weather Lawrence. An image shows the Lawrence skyline with different conditions for the next 6 days.](https://static.simonwillison.net/static/2025/django-birthday/django-birthday07.jpg)

[#](https://simonwillison.net/2025/Jul/13/django-birthday/#django-birthday07.jpg)

And so when we started working on Django, the first thing that we shipped was actually this website. We had a lot of the six-news Lawrence. This is the six-news Lawrence -- six-news is the TV channel here -- six-news Lawrence weather page.

And I think this is pretty cool. So Dan Cox, the designer, was a fantastic illustrator. We actually have this illustration of the famous Lawrence skyline with each panel could be displayed with different weather conditions depending on the weather.

And in case you’re not from Kansas, you might not have realized that the weather is a big deal here. You know, you have never seen more excited weathermen than when there’s a tornado warning and they get to go on local news 24 hours a day giving people updates.

![Image 7: 6 News Lawrence - 6 TV news anchor portrait photos in the heading.](https://static.simonwillison.net/static/2025/django-birthday/django-birthday08.jpg)

[#](https://simonwillison.net/2025/Jul/13/django-birthday/#django-birthday08.jpg)

So we put the site live first. This was the first ever Django website. We then did the rest of the 6 News Lawrence website.

And this -- Adrian reminded me this morning -- the launch of this was actually delayed by a week because the most important feature on the website, which is clearly the photograph of the news people who are on TV, they didn’t like their hairdos. They literally told us we couldn’t launch the website until they’d had their hair redone, had the headshots retaken, had a new image put together. But, you know, image is important for these things.

So anyway, we did that. We did six-news Lawrence. And by the end of my year in Kansas, Adrian had rewritten all of Lawrence.com as well.

![Image 8: Lawrence.com with a new design, it looks very cool.](https://static.simonwillison.net/static/2025/django-birthday/django-birthday09.jpg)

[#](https://simonwillison.net/2025/Jul/13/django-birthday/#django-birthday09.jpg)

So this is the Lawrence.com powered by Django. And one thing I think is interesting about this is when you talk to like David Heinemeier Hansson about Rails, he’ll tell you that Rails is a framework that was extracted from Basecamp. They built Basecamp and then they pulled out the framework that they used and open sourced it.

I see Django the other way around. Django is a framework that was built up to create Lawrence.com. Lawrence.com already existed. So we knew what the web framework needed to be able to do. And we just kept on iterating on Django or the CMS until it was ready to produce this site here.

![Image 9: LJWorld.com Game 2006 - photos of kids playing sports, stories about kid sports, links to photo galleries and playing locations and schedules and more.](https://static.simonwillison.net/static/2025/django-birthday/django-birthday10.jpg)

[#](https://simonwillison.net/2025/Jul/13/django-birthday/#django-birthday10.jpg)

And for me, the moment I realized that we were onto something special was actually when we built this thing. This is a classic Rob Curley project. So Rob was the boss. He had the crazy ideas and he didn’t care how you implemented them. He just wanted this thing done.

And he came to us one day and said, you know, the kids’ little league season is about to start. Like kids playing softball or baseball. Whatever the American kids with bats thing is. So he said, kids’ little league season is about to start. And we are going to go all out.

![Image 10: A Game page showing DCABA 10K Blue - a local team plus their schedule.](https://static.simonwillison.net/static/2025/django-birthday/django-birthday11.jpg)

[#](https://simonwillison.net/2025/Jul/13/django-birthday/#django-birthday11.jpg)

I want to treat these kids like they’re the New York Yankees. We’re going to have player profiles and schedules and photos and results.

![Image 11: A form to sign up for cell phone updates for that team.](https://static.simonwillison.net/static/2025/django-birthday/django-birthday12.jpg)

[#](https://simonwillison.net/2025/Jul/13/django-birthday/#django-birthday12.jpg)

And, you know, we’re going to have the ability for parents to get SMS notifications whenever their kid scores.

![Image 12: An index page showing 360 degree field photos for 12 different venues around town.](https://static.simonwillison.net/static/2025/django-birthday/django-birthday13.jpg)

[#](https://simonwillison.net/2025/Jul/13/django-birthday/#django-birthday13.jpg)

And we’re going to have 360 degree, like, interactive photos of all of the pitches in Lawrence, Kansas, that these kids are playing games on.

They actually did send a couple of interns out with a rig to take 360 degree virtual panoramas of Fenway Park and Lawrence High School and all of these different places.

![Image 13: ... in three days ](https://static.simonwillison.net/static/2025/django-birthday/django-birthday14.jpg)

[#](https://simonwillison.net/2025/Jul/13/django-birthday/#django-birthday14.jpg)

And he said -- and it starts in three days. You’ve got three days to put this all together.

And we pulled it off because Django, even at that very early stage, had all of the primitives you needed to build 360 degree interactives. That was all down to the interns. But we had all of the pieces we needed to pull this together.

![Image 14: "The CMS"](https://static.simonwillison.net/static/2025/django-birthday/django-birthday15.jpg)

[#](https://simonwillison.net/2025/Jul/13/django-birthday/#django-birthday15.jpg)

So when we were working on it back then, we called it the CMS.

![Image 15: brazos webbing physique anson The Tornado Publishing System private dancer fizgig lavalier pythy  https://jacobian.org/writing/private_dancer/ ](https://static.simonwillison.net/static/2025/django-birthday/django-birthday16.jpg)

[#](https://simonwillison.net/2025/Jul/13/django-birthday/#django-birthday16.jpg)

A few years ago, [Jacob found a wiki page](https://jacobian.org/2005/sep/9/private_dancer/) with some of the names that were being brainstormed for the open source release. And some of these are great. There’s Brazos -- I don’t know where that came from -- Webbing, Physique, Anson.

![Image 16: Highlighted: The Tornado Publishing System](https://static.simonwillison.net/static/2025/django-birthday/django-birthday17.jpg)

[#](https://simonwillison.net/2025/Jul/13/django-birthday/#django-birthday17.jpg)

This is my favorite name. I think this is what I proposed -- is the Tornado Publishing System.

![Image 17: Screenshot from Office Space. Lumbergh says "Yeah, if you could go ahead and get those TPS reprots to me as soon as possible... that'd be great".](https://static.simonwillison.net/static/2025/django-birthday/django-birthday18.jpg)

[#](https://simonwillison.net/2025/Jul/13/django-birthday/#django-birthday18.jpg)

And the reason is that I was a really big fan of [Office Space](https://en.wikipedia.org/wiki/Office_Space). And if we had the Tornado, we could produce TPS reports, which I thought would be amazing.

But unfortunately, this being Kansas, the association of Tornadoes isn’t actually a positive one.

Private Dancer, Physgig, Lavalia, Pithy -- yeah. I’m very, very pleased that they picked the name that they did.

![Image 18: “Wouldn't It be cool If...” ](https://static.simonwillison.net/static/2025/django-birthday/django-birthday19.jpg)

[#](https://simonwillison.net/2025/Jul/13/django-birthday/#django-birthday19.jpg)

So one of our philosophies was build cool shit. The other philosophy we had was what we called “Wouldn’t it be cool if?”

So there were no user stories or careful specs or anything. We’d all sit around in the basement and then somebody would go “Wouldn’t it be cool if...”, and they’d say something. And if we thought it was a cool idea, we’d build it and we’d ship it that day.

![Image 19: Lawrence.com featured audio page - a list of bands each with links to their music and information about where they are playing in town this week.](https://static.simonwillison.net/static/2025/django-birthday/django-birthday20.jpg)

[#](https://simonwillison.net/2025/Jul/13/django-birthday/#django-birthday20.jpg)

And my favorite example of “Wouldn’t it be cool if?” -- this is a classic Adrian one -- is “Wouldn’t it be cool if the downloads page on Lawrence.com featured MP3s you could download of local bands?” And seeing as we’ve also got the schedule of when the bands are playing, why don’t we feature the audio from bands who you can go and see that week?

So this page will say, “OK Jones are playing on Thursday at the Bottleneck. Get their MP3. Listen to the radio station.” We had a little MP3 widget in there. Go and look at their band profile. All of this stuff.

Really, these kinds of features are what you get when you take 1970s relational database technology and use it to power websites, which -- back in 2003, in the news industry -- still felt incredibly cutting edge. But, you know, it worked.

And that philosophy followed me through the rest of my career, which is sometimes a good idea and often means that you’re left maintaining features that seemed like a good idea at the time and quickly become a massive pain!

![Image 20: YAHOO! ](https://static.simonwillison.net/static/2025/django-birthday/django-birthday21.jpg)

[#](https://simonwillison.net/2025/Jul/13/django-birthday/#django-birthday21.jpg)

After I finished my internship, I finished my degree in England and then ended up joining up with Yahoo. I was actually working out of the Yahoo UK office but for a R&D team in the States. I was there for about a year and a half.

One of the things I learned is that you should never go and work for an R&D team, because the problem with R&D teams is you never ship. I was there for a year and a half and I basically have nothing to show for it in terms of actual shipped features.

We built some very cool prototypes. And actually, after I left, one of the projects I worked on, [Yahoo FireEagle](https://en.wikipedia.org/wiki/Fire_Eagle), did end up getting spun out and turned into a real product.

![Image 21: YAHOO! ASTRONEWSOLOGY  Dick Cheneey (age 65)  Compare their horoscope with our recent news stories!  A very close friend or a member of your current peer group -- who means a great deal to you -- has recently found it necessary to go out of their way to tick you off. At least, that's the way it seems. It's worked, too -- better than it should have. You're not just angry, you're furious. Before you let go and let them have it, be sure you're right. Feeling righteous is far better than feeling guilty  Fox News wins battle for Cheney interview (Reuters) - 16th February, 12:13 Cheney Says He Has Power to Declassify Info (AP) - 16th February, 09:56 Cheney Mishap Takes Focus Off CIA Leak (AP) - 16th February, 09:13 ](https://static.simonwillison.net/static/2025/django-birthday/django-birthday22.jpg)

[#](https://simonwillison.net/2025/Jul/13/django-birthday/#django-birthday22.jpg)

But there is one project -- the first project I built at Yahoo using Django that I wanted to demonstrate. This was for Yahoo’s internal hack day. And so Tom Coates and myself, who were working together, we decided that we were going to build a mashup, because it was 2005 and mashups were the cutting edge of computer science.

So we figured, OK, let’s take the two most unlikely Yahoo products and combine them together and see what happens. My original suggestion was that we take Yahoo Dating and Yahoo Pets. But I was told that actually there was this thing called Dogster and this other thing called Catster, which already existed and did exactly that.

So the next best thing, we went for Yahoo News and Yahoo Horoscopes. And what we ended up building -- and again, this is the first Django application within Yahoo -- was Yahoo Astronewsology.

And the idea was you take the news feed from Yahoo News, you pull out anything that looks like it’s a celebrity’s name, look up their birth date, use that to look up their horoscope, and then combine them on the page. And in a massive stroke of luck, we built this the week that Dick Cheney [shot his friend in the face](https://en.wikipedia.org/wiki/Dick_Cheney_hunting_accident) while out hunting.

Dick Cheney’s horoscope for that week says, “A very close friend who means a great deal to you has found it necessary to go out of their way to tick you off. You’re not just angry, you’re furious. Before you let go and let them have it, be sure you’re right. Feeling righteous is far better than feeling guilty.”

And so if Dick Cheney had only had only been reading his horoscopes, maybe that whole situation would have ended very differently.

![Image 22: The Guardian](https://static.simonwillison.net/static/2025/django-birthday/django-birthday23.jpg)

[#](https://simonwillison.net/2025/Jul/13/django-birthday/#django-birthday23.jpg)

So after Yahoo, I spent a while doing consulting and things, mainly [around OpenID](https://simonwillison.net/tags/openid/) because I was determined to make OpenID work. I was absolutely convinced that if OpenID didn’t take off, just one company would end up owning single sign-on for the entire internet, and that would be a total disaster.

And with hindsight, it didn’t quite happen. Facebook login looked like it was going to do that a few years ago, but these days there’s enough variety out there that I don’t feel like we all have to submit to our Facebook masters.

But, you know, I was enjoying freelancing and consulting and so on. And then I ended up going for coffee with somebody who worked for [The Guardian](https://www.theguardian.com/).

I’m sure you’ve all heard of The Guardian. It’s one of England’s most internationally focused newspapers. It’s a very fine publication. And I realized that I really missed working in a newsroom environment. And I was incredibly jealous of people like Adrian, who’d gone off to the Washington Post and was doing data journalism there, and Derek Willis as well, who bounced from the Post and The New York Times. There was all of this cool data journalism stuff going on.

And The Guardian’s pitch was basically, we’ve been building a CMS from scratch in Java with a giant team of engineers, and we’ve built it and it’s really cool, but we’re not shipping things quickly. We want to start exploring this idea of building things much faster to fit in with the news cycle.

And that was a very, very tempting thing for me to get involved with. So I went to work for The Guardian.

![Image 23: Photo of Simon Rogers, looking like a man who can find you the right data.](https://static.simonwillison.net/static/2025/django-birthday/django-birthday24.jpg)

[#](https://simonwillison.net/2025/Jul/13/django-birthday/#django-birthday24.jpg)

And The Guardian have a really interesting way of doing onboarding of new staff. The way they do it is they set you up on coffee dates with people from all over the organization. So one day you’ll be having coffee with somebody who sells ads, and the next day it’ll be the deputy editor of the newsroom, and the next day it’ll be a journalist somewhere. And each of these people will talk to you and then they’ll suggest other people for you to meet up with. So over the first few weeks that you’re there, you meet a huge variety of people.

And time and time again, as I was talking to people, they were saying, “You know what? You should go and talk to Simon Rogers, this journalist in the newsroom.”

This is Simon Rogers. I went down to talk to him, and we had this fascinating conversation. So Simon is a journalist. He worked in the newsroom, and his speciality was gathering data for The Guardian’s infographics. Because they are in the paper. They post, they have graphs and charts and all sorts of things like that that they publish.

It turns out that Simon was the journalist who knew how to get that data out of basically any source you can imagine. If you wanted data, he would make some phone calls, dig into some government contacts and things, and he’d get those raw numbers. And all of the other journalists thought he was a bit weird, because he liked hanging out and editing Excel spreadsheets and stuff.

So I said to him halfway through this conversation, “Just out of interest, what do you do with those Excel spreadsheets?” And he’s like, “Oh, I keep them all on my hard drive.” And showed me this folder with hundreds and hundreds of meticulously researched, properly citable news quality spreadsheets full of data about everything you could imagine. And they lived on his hard drive and nowhere else.

And I was like, “Have you ever talked to anyone in the engineering department upstairs?” And we made this connection.

And so from then on, we had this collaboration going where he would get data and he’d funnel it to me and see if we could, see if I or someone else in the engineering department at Guardian could do something fun with it.

![Image 24: Guardian website screenshot.  BNP members: the far right map of Britain  A court injunction prevents the distribution of the names on the BNP membership leaked online. This map shows you which constituencies have the most BNP members  Then a BNP membership by constituency colourful map. ](https://static.simonwillison.net/static/2025/django-birthday/django-birthday25.jpg)

[#](https://simonwillison.net/2025/Jul/13/django-birthday/#django-birthday25.jpg)

And so that was some of the most rewarding work of my career, because it’s journalism, you know, it’s news, it’s stuff that matters. The deadlines are ridiculous. If a news story breaks and it takes you three weeks to turn around a piece of data journalism around it, why did you even bother? And it’s perfect for applying Django to.

So the first story I got to work on at the Guardian was actually one of the early WikiLeaks things. This is before WikiLeaks was like massively high profile. But quite early on, WikiLeaks leaked a list of all of the members of the British National Party, basically the British Nazis. They leaked a list of all of their names and addresses.

And the Guardian is an ethical newspaper, so we’re not going to just publish 18,000 people’s names and addresses. But we wanted to figure out if there was something we could do that would make use of that data but wouldn’t be violating anyone’s individual privacy.

And so what we did is we took all of the addresses, geocoded them, figured out which parliamentary constituency they lived in, and used that to generate a heat map that’s actually called a choropleth map, I think, of the UK showing where the hotspots of BNP activity were.

And this works because in the UK a parliamentary constituency is, they’re designed to all have around about the same population. So if you just like make the color denser for the larger numbers of BNP members, you get this really interesting heat map of the country.

![Image 25: A photo of that same map shown in a paper newspaper](https://static.simonwillison.net/static/2025/django-birthday/django-birthday26.jpg)

[#](https://simonwillison.net/2025/Jul/13/django-birthday/#django-birthday26.jpg)

And what was really cool about this is that I did this using SVG, because we have an infographics department with Illustrator who are good at working with SVG. And it’s very easy with an SVG file with the right class names on things to set colors on different regions.

And because we produced it in SVG, we could then hand it over to the print department, and the next day it was out in the paper. It was like a printed thing on paper, on like dead trees distributed all over the country, which I thought was super cool.

So that was the first data journalism project that we did at The Guardian. And it really helped prove that given the right data sets and like the right tools and a bit of freedom, you can do some really cool things.

The first few times I did this, I did it by hand. Then we had The Guardian’s first hack day and I was like, well okay, I’m going to build a little self-service tool for our infographics journalists to like dump in a bunch of CSV numbers and get one of these maps out of it.

So I built this tool. I didn’t have anywhere official to deploy it, so I just ran it on my Linux desktop underneath my desk. And they started using it and putting things in the paper and I kind of forgot about it. And every now and then I get a little feature request.

A few years after I left The Guardian, I ran into someone who worked there. And he was like, yeah, you know that thing that you built? So we had to keep your desktop running for six months after you left. And then we had to like convert it into a VMware instance. And as far as I know, my desktop is still running as a VMware instance somewhere in The Guardian.

Which ties into the Simon database, I guess. The hard thing is building stuff is easy. Keeping it going it turns out is surprisingly difficult.

![Image 26: Website:  Investigate your MP's expenses mps-expenses.guaraian.co.uk  Join us in digging through the documents of MPs' expenses to identify individual claims, or documents that you think merit further investigation. You can work through your own MP's expenses, or just hit the button below to start reviewing.   A progress bar shows 28,801 of you have reviewed 221,220 of them, only 237o612 to go...](https://static.simonwillison.net/static/2025/django-birthday/django-birthday27.jpg)

[#](https://simonwillison.net/2025/Jul/13/django-birthday/#django-birthday27.jpg)

This was my favorite project at The Guardian. There was [a scandal in the UK a few years ago](https://en.wikipedia.org/wiki/United_Kingdom_parliamentary_expenses_scandal) where it turned out that UK members of parliament had all been fiddling their expenses.

And actually the background on this is that they’re the lowest paid MPs anywhere in Europe. And it seems like the culture had become that you become an MP and on your first day somebody takes you aside and goes, look, I know the salary is terrible. But here’s how to fill your expenses and make up for it.

This was a scandal that was brewing for several years. The Guardian had actually filed freedom of information requests to try and get these expense reports. Because they were pretty sure something dodgy was going on. The government had dragged their heels in releasing the documents.

And then just when they were a month before they finally released the documents, a rival newspaper, the Telegraph, managed to get hold of a leaked copy of all of these expenses. And so the Telegraph had 30 days lead on all of the other newspapers to dig through and try and find the dirt.

So when they did release the expenses 30 days later, we had a race on our hands because we needed to analyze 20,000 odd pages of documents. Actually, here it says 450,000 pages of documents in order to try and find anything left that was newsworthy.

![Image 27: Page 34 of Janet Dean's Incidental Expenses Provision 2007/08  Much of the page is redacted.   What kind of page is this? Buttons for: Claim, Proof, Blank, Other  Is this page interesting? Should we investigate it further?](https://static.simonwillison.net/static/2025/django-birthday/django-birthday28.jpg)

[#](https://simonwillison.net/2025/Jul/13/django-birthday/#django-birthday28.jpg)

And so we tackled this with crowdsourcing. We stuck up a website. We told people, we told Guardian readers, come to this website, hit the button, we’ll show you a random page from someone’s expenses. And then you can tell us if you think it’s not interesting, interesting, or we should seek an investigative reporter on it.

![Image 28: Hywel Francis MP's expenses  Labour MP for Aberavon. A photo of him smiling. Below is a table of documents each showing progress through reviewing each one.](https://static.simonwillison.net/static/2025/django-birthday/django-birthday29.jpg)

[#](https://simonwillison.net/2025/Jul/13/django-birthday/#django-birthday29.jpg)

And one of the smartest things we did with this is we added a feature where you could put in your postcode, we’d figure out who your MP was, and then we would show you their smug press photo. You know, their smug face next to all of their expense claims that they’d filed.

And this was incredibly effective. People were like, “Ooh, you look so smug. I’m going to get you.” And once we put this up, and within 18 hours, our community had burned through hundreds of thousands of pages of expense documents trying to find this stuff.

![Image 29: Screenshot showing thumbnails of a document that is being processed.](https://static.simonwillison.net/static/2025/django-birthday/django-birthday30.jpg)

[#](https://simonwillison.net/2025/Jul/13/django-birthday/#django-birthday30.jpg)

And again, this was built in Django. We had, I think, five days warning that these documents are coming out. And so it was a total, like, I think I built a proof of concept on day one. That was enough to show that it was possible. So I got a team with a designer and a couple of other people to help out. And we had 