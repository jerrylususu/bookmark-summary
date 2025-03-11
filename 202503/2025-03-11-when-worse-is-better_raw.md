Title: When worse is better

URL Source: https://www.bitecode.dev/p/when-worse-is-better

Published Time: 2025-03-10T20:27:41+00:00

Markdown Content:
_"And how would you do it when money is finite and your infrastructure spend has to be based in reality?" is apparently the question that people didn't want to ask much during the last decade._

_Without making everything terrible, there is still a large margin for making things a bit less sophisticated for a drastic reduction in cost._

You hear about all those "less is more", but I find them hard to understand because less is very specific while we are talking about general outcomes.

"Perfect is the enemy of the good" is nice, but it makes it sound like it's an internal matter, and relevant mostly at the high end of the quality spectrum.

I like "worse is better". It's closer to reality. It's dirty, it's vague, it doesn't assume something profound about people and you can get worse from anywhere, because it's very subjective.

It goes without saying I'm not advocating to be a terrible programmer nor that you should always output crap. Rather, this post is a complement to the [XML is the future](https://www.bitecode.dev/p/hype-cycles) article, to make a case that we are often overdoing it in IT.

My instinct tells me this is going to change, not because we want to, but because we are going to be forced to, by our shifting world.

But change is always better when you go with it, so maybe I can convince a few people to start before the push arrives.

There is a weird obsession in our nerd communities, especially among beginners, about finding "the best". The best language, the best lib, the best tool, the best framework, the best methodology...

In [A year of UV](https://www.bitecode.dev/p/a-year-of-uv-pros-cons-and-should), I forced myself to avoid this word at all costs.

I myself wasted days in my twenties trying to apply design patterns while I should have simply been focusing on solving the problem at hand. Best practices are something you cannot understand nor choose or use effectively without the perspective offered by practical experience.

After all, you can learn to play the piano without opening a single book, but you can't by reading only books and not touching a piano. Practicing a lot, while reading a bit along the way, is an optimum balance for most learners.

But beyond this retrospectively obvious wisdom, there is the simple fact that the universe doesn't have a notion of "best". It's a human thing. We have created this label and started to apply it on stuff, feeling smug about it.

Yet, the world doesn't run on only the best things, whatever that means. In fact, being labeled as "good" by very respectable people is not remotely a decent predictor of popularity.

Lisp, Haskell, Ocaml, Erlang and F# are outstanding technologies, but half the web runs on spaghetti PHP code and a ton of people will tell you they love Javascript.

And one might argue we have fantastic databases and languages for data storage and analytics plus tons of very efficient software to do all sorts of accounting, planning and organisation. Yet Excel is used for that practically everywhere.

I could sell Django Wagtail all day long for its flexibility, power, and security, but WordPress, Wix and Squarespace will win almost every time.

Millions of people use Microsoft web browsers, their OS default media players, earphones with awful sound quality or good sound quality but 4 times more expensive than they should be, and so on.

The only thing such label is a decent predictor of, is your model of the world.

It's all tongue in cheek of course, since there is no more worst than best.

The question is rather, since you DON'T have infinite time and resources, and your team is constrained by the laws of physics, not to mention its own skills and size, what can you compromise on?

Let me throw a few concepts there and try to figure out which one you would be able to compromise on, and which one you would never, ever do:

*   Committing AI generated code.
    
*   Letting a bug in production forever.
    
*   Having your website crash every week.
    
*   Not having any time or money budget to address security.
    
*   Taking down your site for maintenance.
    
*   Working with people forbidding re-usability and refactoring: you can only copy/ paste code around.
    
*   Coding a whole product in a language that has terrible error-handling primitives.
    

I've done a variation of all of the above at least once in my life.

And you know what? It all turned out OK.

Would I commit ChatGPT bash code with 3 copy/pasted functions and a bug in a Nuclear plant reactor heat management system?

No.

But would you inflict any single point among the above on a hotel booking system if I put a gun on your kid's head and told you to do it or I shoot?

Sure you would.

So we established it's not an absolute thing, it's the spectrum all over again. This blog repeats itself a lot.

It's like this BS you see in the 90's TV shows stating grand lines like "you can't assign value to life" or "we don't let anyone behind".

Sure you can, and yes we do. We do both every single day. We do it when we buy things, when we decide to help people or not, how much time we focus on each problem, and so on. We have to, because days have only 24H and thermodynamics are very cruel.

Right now there is someone in your city, dying from thirst, hunger, cold, or something else, who you could save if you dropped everything. The cost to you would be enormous though. And you would have to solve the trolley problem since you have others depending on you.

This is not a philosophy blog, so I'm not going to demonstrate or debate this, but rather say that compared to that, our little issue of not using the best tech move for everything is quite tame.

I was working in India for an American NGO on a data collection tool. One admin would define forms, then give it to field agents, they would use an app to collect the data on site, then bring it back to HQ, upload it and the system would output reports.

Because you couldn't know in advance the shape of the data, forms could look like anything, and so it was decided to use a NoSQL DB. And since the backend was full of heterogeneous tech (Java, Python, JS, a DB, a web server, a pipeline), why not abstract that with Docker?

Well, since we are using Docker, micro-services are a best practice, so let's do that.

But wait, so many micro-services, how do we coordinate them all? Well, docker-compose?

I tried to convince the management that using an in-house duck-taped enterprisey stack for a small team of mostly juniors was not aligned with our resources or timeline, but failed. You see, the entire internet was singing the praise of such decisions at the time. There was no nuance, no "it depends". This was "the best".

I was not in charge, so I dropped it.

The kids kept piling up indirection layers to address their pain points while they should have peeled the onion. The monster grew into something unmanageable. The fact the schema-less DB became full of inconsistent data because the team got too overwhelmed to realize data quality was way more critical didn't help either.

We spent more time dealing with that than actually coding the product, and eventually reached the deadline over budget and without anything to show for it.

I was working with a friend of mine on his main product, and we had a DB migration to do. I started to explain to him that we had to make plans to perform the migrations in several steps. Duplicate some fields, then adapt the code to use both fields, then migrate all fields, then change the code again to use the new field. By using a proper migration tool we could record the change in git as well, backtrack if necessary. I just had to take a few hours to teach him how it worked. Then a bit more to perform it.

He looked at me, turned to his terminal, sshed into the main prod server, and took it down. The whole site went 500. A thousand users crashed, no warning.

He casually performed the migration, manually in PhPMyAdmin, then put the server back up.

I stayed stuck for a moment. WTF?

But he understood something I didn't at the time: his business was profitable because he kept running costs low. This implied a lot of things, but among them:

*   A 10-minute downtime was not very expensive and saved you from doing tons of other things every week that added up to a lot of work.
    
*   He was alone working on this site, he could only do so much in a day, so he had to minimize how much work he had to do.
    
*   He was not the best programmer in the world, and he could not afford the mental capacity to learn new things all the time when the work itself took so much of it.
    

But didn't he suffer from that too? Surely best practices are best practices because they save you from other troubles?

Yes of course. He got intrusions in his system, lost data, got the occasional furious customers, and more.

However, the alternative for him was to not have a business at all.

What's more, what I suggested was not a one time thing, that was how I thought one should do most things most of the time. He knew the implications of that better than I did.

Is it good? Fair? Moral?

There is a case to be made that he should not have a business at all.

Yet the returning 300 thousand users a month disagreed. It was a competitive market with close to zero cost switch. They had a choice.

Pretty much everything.

And you should evaluate everything to see if you could make it worse.

I mean it.

I don't mean just for the purpose of making it worse, obviously (on the internet, one has to state the obvious unfortunately).

But just like people got into the very good habit of asking if we can make things better, and how, we should get into the habit of the opposite.

In fact, it's not really the opposite, it's the same thing: if you can provide almost the same things with a much less sophisticated approach, you may have made it better, by doing it worse.

And yes, I know, worse doesn't necessarily mean less costly or easier. And it may mean cheaper now, but much more expensive later. I assume you can assess the first point, and as for the second, this is only true if you reach later, and if said later is still in the configuration where it matters after all what happened since. It's rarer than you think because context changes so often so fast.

It's why procrastination and short sighted decisions can become quite rewarding, and I suspect it's why our species is kinda biased toward it: because it works. I do understand how this can screw us royally in the grand scheme of things, like technical debt, getting fat or climate change, and I know you can read this without nit picking at every paragraph.

This is just another perspective on KISS, if you think about it.

Let's illustrate that with a taboo in dev.

How secure does your new service need to be? What's the cost of it? What's the risk if it's not?

Say that you want to make a concession on that on HN, and you are crucified. But look at how most companies are really doing things, and you'll note security is often terrible. And most users don't care, they don't seem to want to pay for it, nor put any effort in it.

So _we are_ actually making concessions, it's just not morally acceptable to talk about it. It's the same thing as "you can't put a price on life": pretty words that don't match the reality.

In fact, I suspect talking about it would make things _more_ secure, because then people would have to sign on the shortcut taken and take responsibility. It works today because when shit hits the fan, no individual is blamed for the poor investment.

I hear you, this is how things get worse and worse.

Software is slower despite hardware getting better. We have more vulnerabilities. Ergonomics is being destroyed.

Except... this is not exactly true.

There are some software that is getting slower (electron stuff, text edition), and some that are getting faster (python packaging, 3D rendering, web browsers...), it's not all slower.

But the slow down has been exchanged for crazy new possibilities that have been added. Things look amazing, casual users are empowered, multi-media capabilities are through the roof, encryption is everywhere, people can produce useful apps with much less knowledge, everything is indexed, you can use utf8 without thinking and you got tons of plug and play devices, including wireless ones.

Could you make everything faster? On paper yes. In reality, people didn't pay for it. We got the equilibrium we have today based on a compromise between goodies and cost.

Same with ergonomics. I hate using a phone UI compared to my laptop, yet my 5 years old niece can't use the latter, but can do miracles with the former. It's just a trade-off that doesn't play in my favor, it's not an absolute downgrade.

We never had less malware infections than today. Anybody that has been taking care of family devices since 1995 knows this: normies used to have crippled systems after 2 weeks of use, now one among your social circle may have one problem in 5 years.

The cost of producing software is going down, as is the number of critical bugs, corrupted data and required reboots.

Is everything perfect? Hell no.

Should you still care about producing good software?

Definitely.

I love that uv, sqlite and vlc exist.

I also know that the vast majority of projects have nowhere near the time scale, skilled team, money nor vision to reach that level.

Including some of mine. And some of yours.
