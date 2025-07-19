Title: The EU can be shut down with a few keystrokes

URL Source: https://www.bitecode.dev/p/the-eu-can-be-shut-down-with-a-few

Published Time: 2025-07-18T14:33:55+00:00

Markdown Content:
_Europe has excellent infrastructure but lacks sovereignty regarding Operating Systems, SaaS platforms, and Chips._

_We dug ourselves into a dark dependency hole with those, and now the US can turn off the light at any time if it feels like it._

It's kinda out of character for this blog, and I promise, I'm not going to become politically vindictive. I have plenty of political opinions, but I want this blog to focus on tech, not on preaching.

But this is a discussion I wish we had, and we are not currently having it, at a time when it's becoming increasingly relevant.

Plus, this is about tech, really.

Europe's software and hardware independence hasn't been the center of enough attention for the last few decades, with only timid discussions and very limited action. Partly because globalisation meant delegating a lot of stuff, and partly because we were simply incapable of dealing with it anyway.

Now I'm not talking about infrastructure. Our infra is top-notch, land line/fiber/5G coverage is great and cheap compared to most places in the world. The irony is, going to the Silicon Valley will make you cringe if you are European because of the expensive and average quality connection you get there compared to home.

Hosting is terrific, with providers like [OVH](https://www.ovhcloud.com/), [Scaleway](https://www.scaleway.com/), [Hetzner](https://www.hetzner.com/), or [Leaseweb](https://www.leaseweb.com/) offering a wide spectrum of options in terms of price, power, bandwidth, and service.

Even getting a domain name through [Gandi](https://www.gandi.net/) (although less so nowadays) and [Infomaniak](https://www.infomaniak.com/) is pretty good. Not [Namecheap](https://www.namecheap.com/) level of pricing, but decent.

No, the weak links are what we use for OS, SaaS, and Chips.

This year, there was a blip about European software independence, [through the ICC & Microsoft email story](https://www.politico.eu/article/microsoft-did-not-cut-services-international-criminal-court-president-american-sanctions-trump-tech-icc-amazon-google/). It was quickly forgotten, that's the reality of our attention span and news cycle, and it didn't have a definitive conclusion: A says they did shut down the emails, B says they did not, and nobody is going to spend more time and energy to check into the matter.

Yet it did raise an interesting question, as to quote the article:

> Khan's email disconnection has sparked Europe's fears that Trump could flip a "kill switch" to cut digital services through American tech giants

Because the reality is, yes, they can do that.

Definitely, YES.

And not just digital services.

Hell, if you are a pessimist, you can argue that they have the ability to `rm -fr` half of the laptops and towers on our continent overnight.

And yes, this is a huge issue given the current state of our relationship.

At this stage, you may think I'm exaggerating or fear-mongering, so let me develop.

I'm not talking about cutting us from things like SWIFT or the DNS root servers. For the former, Russia has proven it's not a death sentence, and for the latter, local cache, decentralization, and monitoring mean we will have time to detect, react, and compensate for the blow. It would cause disruption, but we would recover quickly, and some good would come out of it: we would rely more on our own stuff.

I'm talking about all the emails, chat, calendars, ticket systems, design tools, observability services, file hosting, synchronization servers, authentication portals, code repositories, and payment providers that are all transiting and storing their data through the other side of the pond.

The ICC thought their emails were a big deal? What happens if you can't pay, if you don't have access to any document, if you can't even sign in?

Even my lawyer and my doctor use Gmail + Google Docs. And no, they don't encrypt anything. Professional secrecy is a joke in 2025.

Third-party sign-up is particularly an issue: many sites delegate their auth to Google, Apple, Facebook, Twitter, or GitHub. You can't use iPhones without an iCloud account, and the vast majority of users wouldn't even know how to use an Android phone without being logged in.

Shutting those down is just a few entries in a few databases. It's nothing. For each company, a phone call, a meeting, one engineer in front of a machine running a few queries, and you say "Ciao!" to millions of users.

This alone would cripple the countries that are victims of the excommunication because nobody has been careful with their digital dependencies:

*   Regular people don't have backups. Many institutions don't even have one. Among those who have, a non-trivial amount don't test them anyway.

*   It has become a habit to put everything online and nothing locally. Only nerds insist on IMAP, choose a software because it has an offline mode, and download things to keep a copy. Normies use webmails, online editors, and automatic upload.

*   Humans HATE friction. I got bullied for not joining Facebook. For not wanting to be in pictures. For refusing to create a WhatsApp account, this very week. The social pressure is immense because few want to take even a modicum of effort to co-create their society if they are not forced to. It's not a moral stance I'm taking. I'm not better, I do it too, just on different things.

*   Institutions didn't fight the loss of power, preferring to focus their efforts on their core business. Their Office suite is now online, their permissions system does a round-trip across the Atlantic, and their knowledge base has no copy on their own machine. Only sensitive industries have been careful with this.

*   They just don't know. When you live in this stuff, it looks like stating the obvious, but for someone who is not, it is technical and abstract. And the danger is hypothetical, far away, why worry about that?

So the entire society would be affected by an executive order asking to cut Europe out.

While the previous part of the article was something possible to explain to your non-geek guest at dinner, this one is tougher: even if you don't see a direct dependency on American services, you have some because someone in the chain does, and you depend on this chain.

Let's say you have a business and you have been super careful not to ever depend on any service based in the USA (good luck with that, I'm very careful with this, and even I have to make many compromises). Now you might think you are out of the water, but of course, far from it, one of the critical partners in your workflow WILL depend on a US service, and if it shuts down, its failure would cascade to you.

The number of companies that rely on AWS or Azure is immense, for example. Are you going to exclude all of them? Then you won't have a business. But if their cloud provider shuts them down, they stop. Plain and simple.

Ask around you, very few of your friends will even know what those two names stand for, nor what it would mean if they did abruptly close the door on a private venture. Or even the public sector!

Yet we are so dependent on them that it would crash the economy, and quite literally, lead people to die, as we would be crippled by the shock.

The causality flow is not necessarily obvious; it can be quite twisted. Let me give you an example:

In 2026, French companies will have the legal obligation to use a so-called PDP (Plateformes de Dématérialisation Partenaire, for Digitization Platform Partner) to share digital invoices with their clients and the government. There is a list of [orgs](https://www.pennylane.com/fr/fiches-pratiques/facture-electronique/liste-des-pdp) you can use.

A quick search shows me that the second one, Accenture, is using both AWS and Azure. Maybe if they get the boot, they won't be able to process your invoice. Now what?

If amazon.com stops delivering to the old continent, you might say, good riddance? But now you are left with the entire ecosystem of delivery drivers, trucks, packaging, port handling, import systems, shops, and sellers, all light-struck. It won't be the death of us alone. But we will feel it badly if we have no time to prepare for the transition.

Your bank may be using a Microsoft LDAP, your accountant could have all his files in Dropbox, your phone company their clients’ data in an Oracle data lake.

They don’t even realize this. Only a tiny minority is even picturing the scale of this.

It's not a few, but hundreds of thousands of things like this that slowly got intertwined over the years that, if disrupted, would send a death ripple through a Union that is not in the best shape right now.

And it’s all online. It’s automated. It can be changed at a distance.

It would cost the Americans a lot, too. But again, this matters only if the person with the finger on the button cares about that.

You know this joke about two fish meeting, and the older fish says:

> Morning boy, how’s the water?

And the younger fish asks:

> What the hell is water?

Well, that's kinda our situation here. We have been swimming in this for so long that we don't even notice the obvious walls of the aquarium we trapped ourselves into: virtually all user devices run American-controlled OS on American-designed chips.

Windows, MacOS, iOS, and Android, riding on Qualcomm, Intel, AMD, NVidia, or Apple metal.

Even if you didn't believe all of them had backdoors at that point (which, given the track record of those companies, 30 years of news, historical records of the US institutions, 9/11 aftershock, and Snowden revelations, is more delusional than naive IMO):

*   The [PRISM](https://en.wikipedia.org/wiki/PRISM) scandals tell us that they don't need to; the gov can just ask for things.

*   For the OS, it's a simple update away. Wait, for the [hardware as well](https://en.wikipedia.org/wiki/Intel_Management_Engine).

Then it is game over.

It's nice and all to have your servers running Linux, but if Jean and Julie can't connect to your service because, "Ah ah ah, you didn't say the magic word", this is all moot.

So the US can not only cut part of the banking system and the domain names of a piece of the world on a whim, but also 80% of the emails, the documents, the authentication, the storage, the computer power, and apps.

And if they really want to, they can tell our OS to refuse to boot, and instruct our CPU and GPU to go on strike.

That's the nice scenario; the not-so-nice one is taking partial control of it to do damage, but it's much harder, longer, and costlier to do.

If you don’t believe this capability is available yet, they can certainly create it. If a single big red button doesn't exist somewhere to do that for a whole territory with a push, they can build it. They just need the desire to do so.

I'm not a doomer, but I'm not stupid either. Laws and treaties are only as good as they are enforced, alliances shift, and the world is in constant change.

And they already built [XKeyscore](https://en.wikipedia.org/wiki/XKeyscore), this is not SciFi we are talking about.

I'm using the recent cross-Atlantic tension to draw attention to the topic, but I do believe we should work on solving this issue even if we were still BFF with everyone, and world peace was achieved.

As usual with these things, the first step is recognizing there is a problem and making sure we understand the ramifications. Right now, not only does the public know nothing about it, but it's not on the radar of our leaders either, and they don't have the knowledge to understand it on their own. Politicians, especially, are very tech-illiterate.

The second thing is to start early. Like, right now. Because a transition will take decades. Not years. It's expensive. It's difficult. And Europe's economy is not at its best, not to mention our border is quite hot at the moment.

But start what?

I'm not an advocate of using laws for everything, and we have a tendency to overdo it in the EU, but in this case, it's definitely important. We should mandate that:

*   Our administration uses software and hardware that we control. If we don't build it, we should have the specs or sources and have people checking that they match. **The rest don't matter if the OS or a chip can betray you**.

*   Some data and processing simply cannot be dependent on foreign infra. Health, Law, energy, transport... Critical stuff should be isolated from this mode of failure. We have enough SPF already.

*   The education system teaches why this is important, trains students on stuff we understand and have mastery over, and advises to prefer that in the long run as well.

*   Important documents must always be accessible offline. You can't just put them in the cloud and be done with it. Sync if you want, but a local copy must exist.

*   Foreign third-party authentication should be restricted to inconsequential services like entertainment. Sure, it’s convenient, but it’s also poison for our autonomy.

Laws are not enough; if the local alternatives suck, this will just downgrade everything. And that would be paying a real cost right now for the solution to a hypothetical future potential problem (that hopefully will never present itself).

Nobody would be happy with this.

That's why we need to:

*   Support local alternative. We have great industries here, but they are not supported at all. Even the so-called Sovereign Cloud is partnering with... [Microsoft](https://pro.orange.fr/lemag/cloud-souverain-cloud-de-confiance-ou-en-sommes-nous-en-france-CNT000001SZQoi.html). OVH? Don't know those guys.

*   Get the help of people who have been doing it for a long time. We have amazing teams like [Framasoft](https://framasoft.org/en/) that were already in the game circa 2001 and are still at it. You don't know what you are doing at the top? Surround yourself with people who do, we have that.

*   Be aggressive about promoting FOSS and open standards. **Consider that a national priority**. Invest money, hire teams. You can't switch to LibreOffice if it keeps losing your documents.

*   Consider OS and Chips as important as electricity and water, and act like it in the government. If you don't control them, you control **nothing**. Ideally, we should make our own or derive our version from existing ones. We need an official country org dedicated to this.

*   Create huge incentives for local IT companies. Considerably huge, in fact, for the next 20 years, but only if they perform well. They do need skin in the game, or you'll get parasites.

*   Partner with elite schools like Central, Polytechnic, les Mines, etc. to give a special focus to this. We need more Fabrice Bellard.

The good news is that doing that is not just good as a plan B, it's good for the economy in general: money will flow inbound instead of bleeding overseas. And with that, talent.

So it can be an investment that pays off, and above all, something that can be touted as such to the public, since if you can’t get mass adoption, it will keep going down the path of least resistance.

You know, like water.
