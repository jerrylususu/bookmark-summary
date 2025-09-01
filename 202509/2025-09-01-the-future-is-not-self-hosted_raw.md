Title: The Future is NOT Self-Hosted

URL Source: https://www.drewlyton.com/story/the-future-is-not-self-hosted/

Published Time: 2025-07-25T11:58:53.000Z

Markdown Content:
Hey friends 👋,

A few months ago, Amazon announced that [Kindle users would no longer be able to download and back up their book libraries to their computers](https://www.theverge.com/news/612898/amazon-removing-kindle-book-download-transfer-usb?ref=drewlyton.com). Thankfully, I still have access to my library because I saw [this video](https://www.youtube.com/watch?v=iK1ZZInYRHY&ref=drewlyton.com) by Jared Henderson warning of the change and downloaded all ~400 of my books immediately.

But for those that didn't, the only way for them to view the books they own is through a Kindle or the Kindle app.

Which raises the question: do they even own those books?

If you can only access an item through an intermediary that decides the terms and means of your access, I'd say _no_. You don't own your books on Kindle. You rent them from Amazon.

And Amazon agrees with this. When they closed this direct way for users to access their eBooks, they also updated the language in the Kindle store to say [users are purchasing _licenses_](https://tech.yahoo.com/general/articles/amazon-wants-know-only-purchase-185937032.html?ref=drewlyton.com) – not books!

Now, this isn't new. Companies like Amazon have been playing dirty with Digital Rights Management (DRM) since the Internet's inception. Purchased digital goods have always been licenses more than owned assets.

What's changed is they're bold enough now to say the quiet part out loud: that we own nothing.

But this situation extends beyond the realms of media. Even your own data: your documents in Dropbox or Google Drive, your photos in iCloud or Google Photos, your emails, chat history, _everything_ is rented space on these large corporations computers.

And at any point, they can choose to change the terms and conditions of that rental agreement. They can (and I'm sure they do) train AI models on all of your content. They can (and do) change the pricing tiers for their plans to upsell you. They can (and do) make it _extremely difficult_ to migrate to different services.

In our techno-feudalistic dystopia, they're the landlords. We're the serfs.

But over the past few weeks – with the help of a growing group of rebels fighting to take back ownership and control over their digital lives – I did something radical: I built my own cloud.

My wife and I now have a computer in our house that runs open-source equivalents to Google Drive, Google Photos, Audible, Kindle, and Netflix. It syncs to all of our devices. It's secured behind our own VPN. And it's wholly, truly owned by us.

And this week, I want to share with you how I did it, what I learned, and why I think self-hosting is NOT the future we should be fighting for.

Let's start by answering the simple question...

What is self-hosting?
---------------------

To explain what self-hosting is, I find it helpful to demystify what we mean when we talk about "the cloud". Cloud-hosted apps like Drive and Google Photos are simply applications running on computers that we access through the internet.

Those computers are colloquially called _servers_. They're usually racked together in large datacenters and programmed to coordinate with computers across the world to distribute workloads and process requests from users as quickly as possible with minimal downtime.

These computers also handle finding, storing, and backing up the data you upload to these apps.

The cloud is a very smart, complicated, interconnected network of computers. That's why engineers and system administrators _love_ when people use this far more reductive but sufficient definition of it:

> The cloud is just someone else's computer.

_Self_-hosting is when you have a computer in your house do those same things, but on a much smaller scale. You maintain the hardware. You set up the servers. You manage the applications. You store and backup your data. You troubleshoot issues when things (inevitably) go wrong.

If that sounds like a lot of work, _it is_. For this reason alone, self-hosting is impractical for most people. There's a reason Jeff Geerling – one of the many online self-hosting gurus – sells a shirt that says, ["Cosplaying as a sys admin"](https://www.jeffgeerling.com/blog/2022/cosplaying-sysadmin?ref=drewlyton.com).

But if you _really_ value control, freedom and flexibility – or you're a software engineer that suffers from mild mania and hyperfixation – it can be a pretty fun time.

So, what's on my home server?
-----------------------------

Before I talk about the services I'm using to backup photos, store files, and stream movies, let me quickly run you through the setup process.

_Deep breath._

After watching [this video](https://www.youtube.com/watch?v=mVtIOtU5eHI&ref=drewlyton.com) by Hardware Haven, I bought a [Lenovo P520](https://www.lenovo.com/us/en/p/workstations/thinkstation-p-series/thinkstation-p520/33ts3tpp520?ref=drewlyton.com) off eBay with a 3.70 GHz Intel Xeon W-2135 and 128GB of RAM.

When it arrived, I installed a GTX 1660Ti graphics card with 6 GB of vRAM, flashed a 500 GB SSD with Proxmox, set up four 8 TB HDDs in a MergerFS pool with Snapraid for parity, and added a 2 TB NVMe SSD to use as a storage cache.

After that, I installed Tailscale and created a fresh Ubuntu LXC. Then, I installed Tailscale and Docker on the virtual machine, pulled down a GitHub repo containing all of my setup scripts and `compose.yml` files, hacked into the mainframe, and ran `docker compose up -d`.

_Gasp._

I understand that to some (maybe most) of you, those words meant nothing. That's kind of the point. All of that took 138 words to describe but took me the better part of two weeks to actually _do_.

But in the end, I had four open-source alternatives to popular cloud-based apps running on my home server:

**1. Immich** - a clone of Google Photos complete with a slick mobile app, great organization and backup options, and local, machine-learning based photo search.

![Image 1](https://www.drewlyton.com/content/images/2025/07/Pasted-image-20250725072924.png)

Photo taken from Immich.app

**2. Calibre-web** - an eBook library management tool that can sync to Kobo and Kindle devices (with some hacks).

![Image 2](https://www.drewlyton.com/content/images/2025/07/Pasted-image-20250725072940.png)

Photo from [Neil Turner's Blog](https://www.google.com/url?sa=i&url=https%3A%2F%2Fneilturner.me.uk%2F2023%2F11%2F22%2Fmanaging-e-books-with-calibre-web%2F&psig=AOvVaw0SbkgsswYaiCXdjpsRkZF7&ust=1753529783995000&source=images&cd=vfe&opi=89978449&ved=0CBkQjhxqFwoTCJiK79H1144DFQAAAAAdAAAAABAE)

**3. Audiobookshelf** - a simple audiobook library host that lets you listen to your books in any podcast player.

![Image 3](https://www.drewlyton.com/content/images/2025/07/Pasted-image-20250725073056.png)

Photo from [Funky Penguin's Geek Cookbook](https://geek-cookbook.funkypenguin.co.nz/recipes/audiobookshelf/?ref=drewlyton.com)

**4. Jellyfin** - a personal streaming service to watch home videos and legally acquired movies and TV shows.

![Image 4](https://www.drewlyton.com/content/images/2025/07/Pasted-image-20250725073248.png)

Photo from [Jeff Geerling](https://www.jeffgeerling.com/tags/jellyfin?ref=drewlyton.com)

The entire computer also runs as one big Network Attached Storage (NAS) device so my wife and I can backup our computers and view all of our files. Tailscale allows us to access all of these services securely from anywhere in the world.

It's only been a week, but I'm very proud of our little home server. And this is only the tip of the iceberg when it comes to self-hosting. Home automation software, ad-blockers, email servers, _local AI_, there's no limit to what's possible.

But there are also some big limitations.

The suburban internet.
----------------------

Barring the technical inaccessibility of self-hosting, it is also fundamentally limited by what makes it interesting: independence.

Right now, I'm self-hosting a private Google Photos alternative. It's fully owned and only accessible to me and my wife.

_So, how do I create a shared photo album with my friends where we can all upload pictures from our latest trip?_

Well...without exposing our services to the public internet and forcing our friends to signup for our weird app...the only _good_ way to do that would probably be using an app like Google Photos or iCloud to collect the photos and then syncing them back to our server...which essentially defeats the purpose of having the server since we still need to use a cloud service.

This highlights the fundamental problem with self-hosting: it assumes isolated, independent systems are virtuous. But in reality, this simply makes them hugely inconvenient.

Self-hosting is steeped in a vision of an internet that's personalizable, private, and individualistic. A kind of internet suburbia where everyone keeps a server in their garage right next to their lawn mower and their car.

But just like the suburbs, this vision is incredibly inefficient and detrimental to creating vibrant, interconnected communities. It necessitates mass amounts of duplicate, unused infrastructure and requires each household to be individually responsible for maintaining that infrastructure. It silos us and makes it harder to share resources.

And what do we get in return? _A worse experience than cloud-based services._

Look, I get it. We're living in a time of digital feudalism where our tech giant lords provide us serfs with cloud infrastructure, tax us to use it, and then claim that the data we grow on their land is their own.

It's understandable that in that system, we'd envision a utopian future where we are all lords of our own land.

But this still imagines the world in feudal terms. It empowers individuals, but it doesn't reject the power dynamic itself. It creates a system where everyone has to provide for themselves instead of a system that provides for everyone.

The internet is designed to _connect_ us, to help us build bridges to communal spaces, not empower us to build moats around our own castles.

Self-hosting is cool. I've had a lot of fun building my home-server. And it does give me some peace of mind as a digital life backup.

But if we want to live in a world where we are not bent at the knee to corporate lords and _also_ don't fall victim to the myth of self-reliance and rugged individualism, we need to think radically differently about how we create communal, shared internet infrastructure.

Here are some initial contributions to that conversation:

Instead of building our own clouds, I want us to own _the_ cloud. Keep all of the great parts about this feat of technical infrastructure, but put it in the hands of the people rather than corporations.

I'm talking publicly funded, accessible, at cost cloud-services.

Imagine a world where your library card includes 100GB of encrypted file storage, photo-sharing and document collaboration tools, and media streaming services — all for free. Your data is encrypted end-to-end, but is shareable to anyone on any other service through standardized protocols.

When you need more storage, you pay for it through metered usage like any other utility.

But I can already hear the naysayers....

> I don't want _the government_to see my photos/documents/files!!!

A few things:

1.   End-to-end encryption means the service provider can't see your data even if they wanted to. This should already be a standard practice enforced by law, but it isn't because companies see _your data_ as an asset _they own_.
2.   Even with this technical solution, I think it makes sense to envision a world with private, market-provided options. And with standardized protocols and portable data standards, you could switch between services much more easily than you could today. No vendor lock-in, no network-effects, no data silos.
3.   By providing a good, baseline public offering with no profit-based incentive, the cost of _private_ options would go down and the service they provide would have to get _better_. Competition is good and at cost competitors disrupt markets in the best ways.

But in case you still aren't convinced, this entire system could still work entirely through the private-market through non-profits or cooperatives. And in our current political climate, I think this path is probably more likely to succeed than getting funding for libraries to start racking servers.

I do believe there's hope for the latter, though. Because while I'm preaching for libraries to provide public web 2.0 infrastructure, they're already providing public web 1.0 services. Across the country, libraries now provide free, publicly available streaming services for movies, books, and music to their communities.

It's not crazy to think in a decade, they could extend this model to provide storage, hosting services, and other digital tools. The precedent might be small, but there is a precedent.

The devil is in the details. But I know this world where we are all free from our corporate landlords through solidarity, mutual aid, and shared, community-owned, privacy-focused, internet infrastructure is possible.

Because the self-hosted community is already doing this – just at the scale of individuals. What we need now from this vibrant community of smart, dedicated, part-time sys-admins is to think...

Beyond individualism
--------------------

I started my self-hosting journey to escape our growing cultural acceptance that buying and _owning_ are two different things. I wanted to take back control over my digital life. I wanted to create my own digital homestead away from the rest of the world.

And I did it.

But through the process, I realized how privileged I am to have the skills required for digital sovereignty. I realized how unattainable, unsustainable, and unrealistic self-hosting is as a mass solution to the problems we face. I realized that self-reliance isn't freedom — it's the luxury of retreating from a system that others can't escape.

Through fighting to free myself and my family from the clutches of corporate greed and control, I realized that:

> Nobody's free until everybody's free.
> 
> – Fannie Lou Hamer

"How do I build my own cloud?" is the question that inspired this journey. But, "How do we build a better cloud?" is the one that I'm left wondering as it comes to an end.

If you have thoughts or questions of your own, leave a comment down below and let's continue this conversation.

Until next time,

Drew

[Join the discussion on Hacker News](https://news.ycombinator.com/item?id=44682175&ref=drewlyton.com)