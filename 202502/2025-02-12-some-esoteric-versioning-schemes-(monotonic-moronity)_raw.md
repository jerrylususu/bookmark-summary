Title: Some esoteric versioning schemes (monotonic moronity)

URL Source: https://shkspr.mobi/blog/2025/02/some-esoteric-versioning-schemes-monotonic-moronity/

Published Time: 2025-02-12T12:34:33+00:00

Markdown Content:
Some esoteric versioning schemes (monotonic moronity) – Terence Eden’s Blog
===============      

[![Image 28: Photo of Terence Eden. He has a beard and is smiling.](https://shkspr.mobi/apple-touch-icon.png)](https://shkspr.mobi/blog)

[Terence Eden’s Blog](https://shkspr.mobi/blog)

[![Image 29: Mastodon.](blob:https://shkspr.mobi/fa1da30ab36ffc5a1c66c2463941d260)](https://mastodon.social/@edent) [![Image 30: LinkedIn.](blob:https://shkspr.mobi/87e1e72529620add6a9c9cb38e3d9991)](https://linkedin.com/in/TerenceEden) [![Image 31: GitHub.](blob:https://shkspr.mobi/187b809ff3c95149718df61d27417e84)](https://github.com/edent) [![Image 32: Email.](blob:https://shkspr.mobi/e3392786a2c5f8e780db6ce4a7a1237c)](https://edent.tel/) [![Image 33: Feed.](blob:https://shkspr.mobi/f13fd041ddf51ffb91f31fef928e56d3)](https://shkspr.mobi/blog/feed/atom)

 ⚙ Theme:  

![Image 34: 2025-02-12](blob:https://shkspr.mobi/f82e0f324ce4e2dac630594c5a619223)

[Some esoteric versioning schemes (monotonic moronity)](https://shkspr.mobi/blog/2025/02/some-esoteric-versioning-schemes-monotonic-moronity/)
==============================================================================================================================================

[@edent](https://edent.tel/)![Image 35](https://shkspr.mobi/apple-touch-icon.png)[Computer Science](https://shkspr.mobi/blog/tag/computer-science/) [shitpost](https://shkspr.mobi/blog/tag/shitpost/) [software](https://shkspr.mobi/blog/tag/software/) · [4 comments](https://shkspr.mobi/blog/2025/02/some-esoteric-versioning-schemes-monotonic-moronity/#comments) · 900 words

* * *

[](https://shkspr.mobi/blog/wp-content/uploads/2016/05/A-pet-cat-typing-on-a-computer-keyboard.jpg)

Since time immemorial, software has had version numbers. A developer releases V1 of their product. Some time later, they add new features or fix bugs, and release the next version.

What should that next version be called? Modern software broadly bifurcates into two competing standards; `SemVer` and `CalVer`.

[SemVer](https://shkspr.mobi/blog/2025/02/some-esoteric-versioning-schemes-monotonic-moronity/#semver)
------------------------------------------------------------------------------------------------------

**Sem**antic **Ver**sioning is usually in the form `1.2.3`, the last digit is usually for minor bug fixes, the second digit for new functionality, and the primary digit for big and/or breaking changes.

The semantics are _pretty_ loose. There's no real consensus on when a new "primary" number should be issued. There are two main weaknesses:

1.  The numbers might not be decimals. Is `V1.29` newer or older than `V1.3`?
2.  There's no semantic information about _when_ the software was released.

Which leads us to…

[CalVer](https://shkspr.mobi/blog/2025/02/some-esoteric-versioning-schemes-monotonic-moronity/#calver)
------------------------------------------------------------------------------------------------------

**Cal**endar **Ver**sioning is, ironically, more semantic than SemVer. The version number is the date when the software was released. For example, Ubuntu releases are in the form of `YY.MM` - the latest stable release at the time of writing is `24.04` - so we can tell that it was released in April 2024.

There are three main problems with this approach.

1.  ISO8601 or GTFO! Surely these should use `YYYY-MM` to make it obvious this is a date?
2.  Minor bug fixes are often given a release number like `24.04.1` - is that still obvious it is date-based? Was it really released on the 1st of April?
3.  No information about big and/or breaking changes. Software released several years apart may be functionally identical whereas software released days apart may be incompatible.

[Alternatives](https://shkspr.mobi/blog/2025/02/some-esoteric-versioning-schemes-monotonic-moronity/#alternatives)
------------------------------------------------------------------------------------------------------------------

So, what other ways can we number software versions?

### [EffVer](https://shkspr.mobi/blog/2025/02/some-esoteric-versioning-schemes-monotonic-moronity/#effver)

[**Eff**ort **Ver**sioning](https://jacobtomlinson.dev/effver/) is, I think, a sensible way to standardise SemVer. It attempts to show how much effort it takes to move between versions.

[PrideVer](https://shkspr.mobi/blog/2025/02/some-esoteric-versioning-schemes-monotonic-moronity/#pridever)
----------------------------------------------------------------------------------------------------------

[How much Pride](https://mastodon.online/@nikitonsky/113691789641950263) do you have in your software release?

This is SemVer for people with an ego and the coding chops to match.

### [RuffVer](https://shkspr.mobi/blog/2025/02/some-esoteric-versioning-schemes-monotonic-moronity/#ruffver)

[Ruff](https://docs.astral.sh/ruff/versioning/) is a sort of bastard child between SemVer and CalVer, but adds this delightful complication:

> Stable releases use even numbers in minor version component: `2024.30.0`, `2024.32.0`, `2024.34.0`, … Preview releases use odd numbers in minor version component: `2024.31.0`, `2024.33.0`, `2024.35.0`, …

It's the versioning equivalent of setting up a fully scalable cloud database and hand-chiselling HTML out of stone for the cookery blog you update twice per year.

### [0Ver](https://shkspr.mobi/blog/2025/02/some-esoteric-versioning-schemes-monotonic-moronity/#0ver)

[**Zero**\-based **Ver**sioning](https://0ver.org/) tells us that it is forbidden to ask and a sin to know when a piece of software will be completed.

Essentially, it is SemVer for cowards who are afraid to commit. The opposite of [PriveVer](https://shkspr.mobi/blog/2025/02/some-esoteric-versioning-schemes-monotonic-moronity/#PrideVer).

### [PiVer](https://shkspr.mobi/blog/2025/02/some-esoteric-versioning-schemes-monotonic-moronity/#piver)

The venerable TeX uses [**Pi** **Ver**sioning](https://www.preethamrn.com/posts/piver). The current version is `3.141592653`, the next version will be `3.1415926535`.

As the software gets refined, it gradually reaches a state of perfection. This is a charming versioning scheme which shouldn't be used by anyone other than Knuth lest hubris overtake you!

### [NameVer](https://shkspr.mobi/blog/2025/02/some-esoteric-versioning-schemes-monotonic-moronity/#namever)

Sometimes marketing takes the reins and insists that consumers need a **Name**d **Ver**sion to help prevent confusion.

Ubuntu uses things like `Bionic Beaver`, `Distinct Dropbear`, and `Mantic Minotaur`. By convention, names increase alphabetically, so you should know that `Jaundiced Jackdaw` is before `Killer Kangaroo` - until you've released 26 version and have to wrap around the alphabet again.

NameVer is helpful for _distinct_ products which aren't related, but probably more confusing than necessary.

### [WinVer](https://shkspr.mobi/blog/2025/02/some-esoteric-versioning-schemes-monotonic-moronity/#winver)

Microsoft Windows uses this _very_ logical scheme - 1, 2, 3, 3.11, 98, 2000, Me, XP, Vista, 7, 8, 10, 11.

It starts with more-or-less SemVer, then jumps to CalVer, then 4 digit CalVer, then to NameVer, then back to SemVer - [skipping 9 because of alleged technical reasons](https://www.engadget.com/2014-10-01-windows-10-9-naming-rumor.html).

Do not attempt to use this versioning unless you want to anger _both_ gods and mortals.

### [KelVer](https://shkspr.mobi/blog/2025/02/some-esoteric-versioning-schemes-monotonic-moronity/#kelver)

Absolute Zero is defined as 0K. And so, [**Kel**vin **Ver**sioning](https://rybl.net/software-engineering/2022/06/08/kelvin-versioning.html#kelver) counts _down_ to stability.

Almost the opposite of [PiVer](https://shkspr.mobi/blog/2025/02/some-esoteric-versioning-schemes-monotonic-moronity/#PiVer) - the closer this gets to zero, the closer the code is to being complete.

This versioning scheme is affront to most sane people. But here's to the crazy ones.

[Non-Monotonic](https://shkspr.mobi/blog/2025/02/some-esoteric-versioning-schemes-monotonic-moronity/#non-monotonic)
--------------------------------------------------------------------------------------------------------------------

You will notice that all of the above are _monotonic_. That is, they all proceed in one direction and never reverse. Any subsequent version was _definitely_ released later than a previous version. So, in a sense, they all contain _some_ level of semantics.

But they don't have to.

### [HashVer](https://shkspr.mobi/blog/2025/02/some-esoteric-versioning-schemes-monotonic-moronity/#hashver)

Taking the Cryptographic Hash of the code, or a commit, allows one to create **Hash** **Ver**sioning. For example [`43317b7`](https://github.com/termux/termux-app/commit/43317b78c920a48254f8846f5e14b5f873faa271) is a HashVer for something which would otherwise have the dull and unworthy name of v0.118.1

But, of course, a hash does have a _modicum_ of semantic information - even if it is only loosely related to the content of the code. What if there were something with _no_ semantics and _no_ monotonic behaviour!?!?

### [RandVer](https://shkspr.mobi/blog/2025/02/some-esoteric-versioning-schemes-monotonic-moronity/#randver)

Embrace the weird with **Rand**om **Ver**sioning! It its heart, [RandVer](https://nedbatchelder.com/blog/202305/scriv_on_test_code.html) says pick any number that hasn't been used before.

Perhaps `V7` is followed by `V2.5`, which is overtaken by `V0xDEADBEEF`

Absolutely guaranteed to have zero semantic content.

[What have we learned today?](https://shkspr.mobi/blog/2025/02/some-esoteric-versioning-schemes-monotonic-moronity/#what-have-we-learned-today)
-----------------------------------------------------------------------------------------------------------------------------------------------

The square-root of bugger-all.

* * *

Share this post on…
-------------------

*   [![Image 36: Mastodon](blob:https://shkspr.mobi/fa1da30ab36ffc5a1c66c2463941d260)](https://tootpick.org/#text=Some%20esoteric%20versioning%20schemes%20%28monotonic%20moronity%29%20https%3A%2F%2Fshkspr.mobi%2Fblog%2F2025%2F02%2Fsome-esoteric-versioning-schemes-monotonic-moronity%2F)
*   [![Image 37: Facebook](blob:https://shkspr.mobi/efcf4ed3a77499732e3f66a953f0a16e)](https://www.facebook.com/sharer.php?u=https%3A%2F%2Fshkspr.mobi%2Fblog%2F2025%2F02%2Fsome-esoteric-versioning-schemes-monotonic-moronity%2F&t=Some%20esoteric%20versioning%20schemes%20%28monotonic%20moronity%29)
*   [![Image 38: LinkedIn](blob:https://shkspr.mobi/87e1e72529620add6a9c9cb38e3d9991)](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fshkspr.mobi%2Fblog%2F2025%2F02%2Fsome-esoteric-versioning-schemes-monotonic-moronity%2F)
*   [![Image 39: BlueSky](blob:https://shkspr.mobi/44d0beed31dd94e72f3bec5997d78f73)](https://bsky.app/intent/compose?text=Some%20esoteric%20versioning%20schemes%20%28monotonic%20moronity%29%20https%3A%2F%2Fshkspr.mobi%2Fblog%2F2025%2F02%2Fsome-esoteric-versioning-schemes-monotonic-moronity%2F)
*   [![Image 40: Threads](blob:https://shkspr.mobi/84ba40141e083d143dd851e80d1e3f53)](https://www.threads.net/intent/post?url=https%3A%2F%2Fshkspr.mobi%2Fblog%2F2025%2F02%2Fsome-esoteric-versioning-schemes-monotonic-moronity%2F&text=Some%20esoteric%20versioning%20schemes%20%28monotonic%20moronity%29)
*   [![Image 41: Reddit](blob:https://shkspr.mobi/3c2063ad67740fb653a57a197a750ede)](https://www.reddit.com/submit?url=https%3A%2F%2Fshkspr.mobi%2Fblog%2F2025%2F02%2Fsome-esoteric-versioning-schemes-monotonic-moronity%2F&title=Some%20esoteric%20versioning%20schemes%20%28monotonic%20moronity%29)
*   [![Image 42: HackerNews](blob:https://shkspr.mobi/a75ae78b2f12bebbc6d772bed363defa)](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fshkspr.mobi%2Fblog%2F2025%2F02%2Fsome-esoteric-versioning-schemes-monotonic-moronity%2F&t=Some%20esoteric%20versioning%20schemes%20%28monotonic%20moronity%29)
*   [![Image 43: Lobsters](blob:https://shkspr.mobi/9ccd488cfe94d4cfd9308e29e66b969f)](https://lobste.rs/stories/new?url=https%3A%2F%2Fshkspr.mobi%2Fblog%2F2025%2F02%2Fsome-esoteric-versioning-schemes-monotonic-moronity%2F&title=Some%20esoteric%20versioning%20schemes%20%28monotonic%20moronity%29)
*   [![Image 44: WhatsApp](blob:https://shkspr.mobi/d1f7ee7453e3a1624b3ea643293a0601)](https://api.whatsapp.com/send/?text=https%3A%2F%2Fshkspr.mobi%2Fblog%2F2025%2F02%2Fsome-esoteric-versioning-schemes-monotonic-moronity%2F)
*   [![Image 45: Telegram](blob:https://shkspr.mobi/4081d83a5487986611869a54f839f4cc)](https://telegram.me/share/url?url=Some%20esoteric%20versioning%20schemes%20%28monotonic%20moronity%29&text=https%3A%2F%2Fshkspr.mobi%2Fblog%2F2025%2F02%2Fsome-esoteric-versioning-schemes-monotonic-moronity%2F)

4 thoughts on “Some esoteric versioning schemes (monotonic moronity)”
---------------------------------------------------------------------

1.  [2025-02-12 12:44](https://mastodon.smears.org/@mal3aby/113990974951866974)
    
    ![Image 46](https://mastodon.social/avatars/original/missing.png)
    
    ###  ![Image 47](https://icons.duckduckgo.com/ip9/mastodon.smears.org.ico) [mal3aby](https://mastodon.smears.org/@mal3aby/113990974951866974) said on mastodon.smears.org:
    
    [@Edent](https://mastodon.social/@Edent) Nice! I'm pretty sure there was a version 3.1 of Windows between 3 and 3.11. (In my memory it goes "3, 3.1, 3.11 for Workgroups, 95" but apparently there was a non-workgroups edition of 3.11 too.)
    
    [Reply](https://shkspr.mobi/blog/2025/02/some-esoteric-versioning-schemes-monotonic-moronity/?replytocom=447887#respond) | [Reply to original comment on mastodon.smears.org](https://mastodon.smears.org/@mal3aby/113990974951866974)
    
2.  [2025-02-12 12:47](https://fedimon.uk/@AlisonW/113990988113029309)
    
    ![Image 48](https://files.mastodon.social/cache/accounts/avatars/109/260/355/945/492/112/original/9b893e37b729f7b4.png)
    
    ###  ![Image 49](https://icons.duckduckgo.com/ip9/fedimon.uk.ico) [AlisonW ♿🏳️‍🌈♾️](https://fedimon.uk/@AlisonW/113990988113029309) said on fedimon.uk:
    
    [@Edent](https://mastodon.social/@Edent)  
    In WinVer you missed 95!
    
    [Reply](https://shkspr.mobi/blog/2025/02/some-esoteric-versioning-schemes-monotonic-moronity/?replytocom=447888#respond) | [Reply to original comment on fedimon.uk](https://fedimon.uk/@AlisonW/113990988113029309)
    
3.  [2025-02-12 12:48](https://lor.sh/@0x33/113990993358641762)
    
    ![Image 50](https://files.mastodon.social/cache/accounts/avatars/109/549/032/200/365/106/original/f95bcb3cbc3b8df1.jpg)
    
    ###  ![Image 51](https://icons.duckduckgo.com/ip9/lor.sh.ico) [0x33](https://lor.sh/@0x33/113990993358641762) said on lor.sh:
    
    [@Edent](https://mastodon.social/@Edent) I quite like KelVer.
    
    [Reply](https://shkspr.mobi/blog/2025/02/some-esoteric-versioning-schemes-monotonic-moronity/?replytocom=447889#respond) | [Reply to original comment on lor.sh](https://lor.sh/@0x33/113990993358641762)
    
4.  [2025-02-12 13:01](https://shkspr.mobi/blog/2025/02/some-esoteric-versioning-schemes-monotonic-moronity/#comment-447899)
    
    ![Image 52](https://secure.gravatar.com/avatar/ff6adf689bdadc0c877d244c2165f773?s=64&r=x)
    
    ### Alex Gibson says:
    
    My favourite company for naming and versioning products has to be Creality. Their philosophy is: If it sells, keep selling it, and proliferate more, slightly varied models of it. Make no attempt to prune the product tree, and if our competitors have a popular product, take one of ours and rename it similarly, and then continue the version updating from there. Their most popular machine, the Ender-3, has these versions alone: Ender 3 V3 Plus Ender 3 V3 Ender 3 V3 SE Ender 3 V3 KE Ender 3 S1 Ender 3 S1 Pro Ender 3 S1 Plus Ender 3 V2 Neo Ender 3 Max Neo Ender 3 Neo Ender 3 Ender 3 Pro Ender 3 V2 Ender 3 Max
    
    This is not exhaustive. Wild. Their PCBs, liberally scattered among the models, use SemVer like numbering, like 4.2.1, but with no obvious pattern, could include 8-bit or 32-bit processors, basic or advanced motor drivers... Basically anything goes.
    
    [Reply](https://shkspr.mobi/blog/2025/02/some-esoteric-versioning-schemes-monotonic-moronity/?replytocom=447899#respond)
    
5.  ![Image 53](blob:https://shkspr.mobi/8e64eacbbb49530f56ef3c9fedbc7be9)
    
    ### [More comments on Mastodon](https://mastodon.social/@Edent/113990939671137091).
    

### What are your reckons? [Cancel reply](https://shkspr.mobi/blog/2025/02/some-esoteric-versioning-schemes-monotonic-moronity/#respond)

All comments are moderated and may not be published immediately. Your email address will _not_ be published.

Comment: Allowed HTML: `<a href="" title=""> <abbr title=""> <acronym title=""> <b> <blockquote cite=""> <cite> <code> <del datetime=""> <em> <i> <q cite=""> <s> <strike> <strong> <p> <pre> <br> <img src="" alt="" title="" srcset="">`

Your Name (required):  Your Email (required):  Your Website (optional): 

To respond on your own website, write a post which contains a link to this post - then enter the URl of your page here.  
[Learn more about WebMentions](https://indieweb.org/webmention).

 

🔎 Search
---------

Search for:  

🗓️ Explore The Archives
------------------------

*   2025
    *   [January 17 posts](https://shkspr.mobi/blog/2025/01/)
        
        [February 8 posts](https://shkspr.mobi/blog/2025/02/)
        
        March
        
        April
        
        May
        
        June
        
        July
        
        August
        
        September
        
        October
        
        November
        
        December
        
*   2024
    *   [January 31 posts](https://shkspr.mobi/blog/2024/01/)
        
        [February 29 posts](https://shkspr.mobi/blog/2024/02/)
        
        [March 31 posts](https://shkspr.mobi/blog/2024/03/)
        
        [April 30 posts](https://shkspr.mobi/blog/2024/04/)
        
        [May 31 posts](https://shkspr.mobi/blog/2024/05/)
        
        [June 30 posts](https://shkspr.mobi/blog/2024/06/)
        
        [July 19 posts](https://shkspr.mobi/blog/2024/07/)
        
        [August 18 posts](https://shkspr.mobi/blog/2024/08/)
        
        [September 18 posts](https://shkspr.mobi/blog/2024/09/)
        
        [October 29 posts](https://shkspr.mobi/blog/2024/10/)
        
        [November 31 posts](https://shkspr.mobi/blog/2024/11/)
        
        [December 30 posts](https://shkspr.mobi/blog/2024/12/)
        
*   2023
    *   [January 31 posts](https://shkspr.mobi/blog/2023/01/)
        
        [February 28 posts](https://shkspr.mobi/blog/2023/02/)
        
        [March 31 posts](https://shkspr.mobi/blog/2023/03/)
        
        [April 30 posts](https://shkspr.mobi/blog/2023/04/)
        
        [May 31 posts](https://shkspr.mobi/blog/2023/05/)
        
        [June 30 posts](https://shkspr.mobi/blog/2023/06/)
        
        [July 31 posts](https://shkspr.mobi/blog/2023/07/)
        
        [August 31 posts](https://shkspr.mobi/blog/2023/08/)
        
        [September 30 posts](https://shkspr.mobi/blog/2023/09/)
        
        [October 31 posts](https://shkspr.mobi/blog/2023/10/)
        
        [November 30 posts](https://shkspr.mobi/blog/2023/11/)
        
        [December 31 posts](https://shkspr.mobi/blog/2023/12/)
        
*   2022
    *   [January 30 posts](https://shkspr.mobi/blog/2022/01/)
        
        [February 23 posts](https://shkspr.mobi/blog/2022/02/)
        
        [March 15 posts](https://shkspr.mobi/blog/2022/03/)
        
        [April 19 posts](https://shkspr.mobi/blog/2022/04/)
        
        [May 19 posts](https://shkspr.mobi/blog/2022/05/)
        
        [June 19 posts](https://shkspr.mobi/blog/2022/06/)
        
        [July 19 posts](https://shkspr.mobi/blog/2022/07/)
        
        [August 18 posts](https://shkspr.mobi/blog/2022/08/)
        
        [September 12 posts](https://shkspr.mobi/blog/2022/09/)
        
        [October 8 posts](https://shkspr.mobi/blog/2022/10/)
        
        [November 30 posts](https://shkspr.mobi/blog/2022/11/)
        
        [December 31 posts](https://shkspr.mobi/blog/2022/12/)
        
*   2021
    *   [January 31 posts](https://shkspr.mobi/blog/2021/01/)
        
        [February 28 posts](https://shkspr.mobi/blog/2021/02/)
        
        [March 31 posts](https://shkspr.mobi/blog/2021/03/)
        
        [April 30 posts](https://shkspr.mobi/blog/2021/04/)
        
        [May 31 posts](https://shkspr.mobi/blog/2021/05/)
        
        [June 30 posts](https://shkspr.mobi/blog/2021/06/)
        
        [July 31 posts](https://shkspr.mobi/blog/2021/07/)
        
        [August 31 posts](https://shkspr.mobi/blog/2021/08/)
        
        [September 30 posts](https://shkspr.mobi/blog/2021/09/)
        
        [October 31 posts](https://shkspr.mobi/blog/2021/10/)
        
        [November 30 posts](https://shkspr.mobi/blog/2021/11/)
        
        [December 31 posts](https://shkspr.mobi/blog/2021/12/)
        
*   2020
    *   [January 31 posts](https://shkspr.mobi/blog/2020/01/)
        
        [February 29 posts](https://shkspr.mobi/blog/2020/02/)
        
        [March 31 posts](https://shkspr.mobi/blog/2020/03/)
        
        [April 30 posts](https://shkspr.mobi/blog/2020/04/)
        
        [May 31 posts](https://shkspr.mobi/blog/2020/05/)
        
        [June 30 posts](https://shkspr.mobi/blog/2020/06/)
        
        [July 31 posts](https://shkspr.mobi/blog/2020/07/)
        
        [August 31 posts](https://shkspr.mobi/blog/2020/08/)
        
        [September 30 posts](https://shkspr.mobi/blog/2020/09/)
        
        [October 31 posts](https://shkspr.mobi/blog/2020/10/)
        
        [November 30 posts](https://shkspr.mobi/blog/2020/11/)
        
        [December 31 posts](https://shkspr.mobi/blog/2020/12/)
        
*   2019
    *   [January 31 posts](https://shkspr.mobi/blog/2019/01/)
        
        [February 12 posts](https://shkspr.mobi/blog/2019/02/)
        
        [March 17 posts](https://shkspr.mobi/blog/2019/03/)
        
        [April 12 posts](https://shkspr.mobi/blog/2019/04/)
        
        [May 12 posts](https://shkspr.mobi/blog/2019/05/)
        
        [June 10 posts](https://shkspr.mobi/blog/2019/06/)
        
        [July 7 posts](https://shkspr.mobi/blog/2019/07/)
        
        [August 5 posts](https://shkspr.mobi/blog/2019/08/)
        
        [September 6 posts](https://shkspr.mobi/blog/2019/09/)
        
        [October 14 posts](https://shkspr.mobi/blog/2019/10/)
        
        [November 30 posts](https://shkspr.mobi/blog/2019/11/)
        
        [December 17 posts](https://shkspr.mobi/blog/2019/12/)
        
*   2018
    *   [January 8 posts](https://shkspr.mobi/blog/2018/01/)
        
        [February 4 posts](https://shkspr.mobi/blog/2018/02/)
        
        [March 6 posts](https://shkspr.mobi/blog/2018/03/)
        
        [April 14 posts](https://shkspr.mobi/blog/2018/04/)
        
        [May 5 posts](https://shkspr.mobi/blog/2018/05/)
        
        [June 6 posts](https://shkspr.mobi/blog/2018/06/)
        
        [July 6 posts](https://shkspr.mobi/blog/2018/07/)
        
        [August 13 posts](https://shkspr.mobi/blog/2018/08/)
        
        [September 14 posts](https://shkspr.mobi/blog/2018/09/)
        
        [October 8 posts](https://shkspr.mobi/blog/2018/10/)
        
        [November 30 posts](https://shkspr.mobi/blog/2018/11/)
        
        [December 4 posts](https://shkspr.mobi/blog/2018/12/)
        
*   2017
    *   [January 12 posts](https://shkspr.mobi/blog/2017/01/)
        
        [February 9 posts](https://shkspr.mobi/blog/2017/02/)
        
        [March 8 posts](https://shkspr.mobi/blog/2017/03/)
        
        [April 4 posts](https://shkspr.mobi/blog/2017/04/)
        
        [May 10 posts](https://shkspr.mobi/blog/2017/05/)
        
        [June 5 posts](https://shkspr.mobi/blog/2017/06/)
        
        [July 5 posts](https://shkspr.mobi/blog/2017/07/)
        
        [August 6 posts](https://shkspr.mobi/blog/2017/08/)
        
        [September 3 posts](https://shkspr.mobi/blog/2017/09/)
        
        [October 4 posts](https://shkspr.mobi/blog/2017/10/)
        
        [November 30 posts](https://shkspr.mobi/blog/2017/11/)
        
        December
        
*   2016
    *   [January 10 posts](https://shkspr.mobi/blog/2016/01/)
        
        [February 10 posts](https://shkspr.mobi/blog/2016/02/)
        
        [March 11 posts](https://shkspr.mobi/blog/2016/03/)
        
        [April 9 posts](https://shkspr.mobi/blog/2016/04/)
        
        [May 8 posts](https://shkspr.mobi/blog/2016/05/)
        
        [June 9 posts](https://shkspr.mobi/blog/2016/06/)
        
        [July 6 posts](https://shkspr.mobi/blog/2016/07/)
        
        [August 9 posts](https://shkspr.mobi/blog/2016/08/)
        
        [September 4 posts](https://shkspr.mobi/blog/2016/09/)
        
        [October 2 posts](https://shkspr.mobi/blog/2016/10/)
        
        [November 30 posts](https://shkspr.mobi/blog/2016/11/)
        
        [December 14 posts](https://shkspr.mobi/blog/2016/12/)
        
*   2015
    *   [January 8 posts](https://shkspr.mobi/blog/2015/01/)
        
        [February 11 posts](https://shkspr.mobi/blog/2015/02/)
        
        [March 10 posts](https://shkspr.mobi/blog/2015/03/)
        
        [April 4 posts](https://shkspr.mobi/blog/2015/04/)
        
        [May 9 posts](https://shkspr.mobi/blog/2015/05/)
        
        [June 3 posts](https://shkspr.mobi/blog/2015/06/)
        
        [July 7 posts](https://shkspr.mobi/blog/2015/07/)
        
        [August 9 posts](https://shkspr.mobi/blog/2015/08/)
        
        [September 10 posts](https://shkspr.mobi/blog/2015/09/)
        
        [October 2 posts](https://shkspr.mobi/blog/2015/10/)
        
        [November 30 posts](https://shkspr.mobi/blog/2015/11/)
        
        [December 4 posts](https://shkspr.mobi/blog/2015/12/)
        
*   2014
    *   [January 13 posts](https://shkspr.mobi/blog/2014/01/)
        
        [February 13 posts](https://shkspr.mobi/blog/2014/02/)
        
        [March 15 posts](https://shkspr.mobi/blog/2014/03/)
        
        [April 14 posts](https://shkspr.mobi/blog/2014/04/)
        
        [May 8 posts](https://shkspr.mobi/blog/2014/05/)
        
        [June 7 posts](https://shkspr.mobi/blog/2014/06/)
        
        [July 9 posts](https://shkspr.mobi/blog/2014/07/)
        
        [August 5 posts](https://shkspr.mobi/blog/2014/08/)
        
        [September 5 posts](https://shkspr.mobi/blog/2014/09/)
        
        [October 1 post](https://shkspr.mobi/blog/2014/10/)
        
        [November 30 posts](https://shkspr.mobi/blog/2014/11/)
        
        [December 20 posts](https://shkspr.mobi/blog/2014/12/)
        
*   2013
    *   [January 25 posts](https://shkspr.mobi/blog/2013/01/)
        
        [February 17 posts](https://shkspr.mobi/blog/2013/02/)
        
        [March 15 posts](https://shkspr.mobi/blog/2013/03/)
        
        [April 18 posts](https://shkspr.mobi/blog/2013/04/)
        
        [May 11 posts](https://shkspr.mobi/blog/2013/05/)
        
        [June 14 posts](https://shkspr.mobi/blog/2013/06/)
        
        [July 6 posts](https://shkspr.mobi/blog/2013/07/)
        
        [August 14 posts](https://shkspr.mobi/blog/2013/08/)
        
        [September 6 posts](https://shkspr.mobi/blog/2013/09/)
        
        [October 4 posts](https://shkspr.mobi/blog/2013/10/)
        
        [November 30 posts](https://shkspr.mobi/blog/2013/11/)
        
        [December 15 posts](https://shkspr.mobi/blog/2013/12/)
        
*   2012
    *   [January 14 posts](https://shkspr.mobi/blog/2012/01/)
        
        [February 8 posts](https://shkspr.mobi/blog/2012/02/)
        
        [March 13 posts](https://shkspr.mobi/blog/2012/03/)
        
        [April 15 posts](https://shkspr.mobi/blog/2012/04/)
        
        [May 10 posts](https://shkspr.mobi/blog/2012/05/)
        
        [June 16 posts](https://shkspr.mobi/blog/2012/06/)
        
        [July 8 posts](https://shkspr.mobi/blog/2012/07/)
        
        [August 8 posts](https://shkspr.mobi/blog/2012/08/)
        
        [September 6 posts](https://shkspr.mobi/blog/2012/09/)
        
        [October 6 posts](https://shkspr.mobi/blog/2012/10/)
        
        [November 30 posts](https://shkspr.mobi/blog/2012/11/)
        
        [December 30 posts](https://shkspr.mobi/blog/2012/12/)
        
*   2011
    *   [January 13 posts](https://shkspr.mobi/blog/2011/01/)
        
        [February 11 posts](https://shkspr.mobi/blog/2011/02/)
        
        [March 12 posts](https://shkspr.mobi/blog/2011/03/)
        
        [April 12 posts](https://shkspr.mobi/blog/2011/04/)
        
        [May 8 posts](https://shkspr.mobi/blog/2011/05/)
        
        [June 8 posts](https://shkspr.mobi/blog/2011/06/)
        
        [July 6 posts](https://shkspr.mobi/blog/2011/07/)
        
        [August 5 posts](https://shkspr.mobi/blog/2011/08/)
        
        [September 11 posts](https://shkspr.mobi/blog/2011/09/)
        
        [October 7 posts](https://shkspr.mobi/blog/2011/10/)
        
        [November 30 posts](https://shkspr.mobi/blog/2011/11/)
        
        [December 17 posts](https://shkspr.mobi/blog/2011/12/)
        
*   2010
    *   [January 6 posts](https://shkspr.mobi/blog/2010/01/)
        
        [February 15 posts](https://shkspr.mobi/blog/2010/02/)
        
        [March 12 posts](https://shkspr.mobi/blog/2010/03/)
        
        [April 13 posts](https://shkspr.mobi/blog/2010/04/)
        
        [May 4 posts](https://shkspr.mobi/blog/2010/05/)
        
        [June 3 posts](https://shkspr.mobi/blog/2010/06/)
        
        [July 15 posts](https://shkspr.mobi/blog/2010/07/)
        
        [August 8 posts](https://shkspr.mobi/blog/2010/08/)
        
        [September 11 posts](https://shkspr.mobi/blog/2010/09/)
        
        [October 10 posts](https://shkspr.mobi/blog/2010/10/)
        
        [November 30 posts](https://shkspr.mobi/blog/2010/11/)
        
        [December 9 posts](https://shkspr.mobi/blog/2010/12/)
        
*   2009
    *   [January 1 post](https://shkspr.mobi/blog/2009/01/)
        
        [February 5 posts](https://shkspr.mobi/blog/2009/02/)
        
        [March 3 posts](https://shkspr.mobi/blog/2009/03/)
        
        [April 7 posts](https://shkspr.mobi/blog/2009/04/)
        
        [May 12 posts](https://shkspr.mobi/blog/2009/05/)
        
        [June 8 posts](https://shkspr.mobi/blog/2009/06/)
        
        [July 10 posts](https://shkspr.mobi/blog/2009/07/)
        
        [August 10 posts](https://shkspr.mobi/blog/2009/08/)
        
        [September 12 posts](https://shkspr.mobi/blog/2009/09/)
        
        [October 22 posts](https://shkspr.mobi/blog/2009/10/)
        
        [November 31 posts](https://shkspr.mobi/blog/2009/11/)
        
        [December 15 posts](https://shkspr.mobi/blog/2009/12/)
        
*   2008
    *   [January 2 posts](https://shkspr.mobi/blog/2008/01/)
        
        February
        
        [March 2 posts](https://shkspr.mobi/blog/2008/03/)
        
        [April 3 posts](https://shkspr.mobi/blog/2008/04/)
        
        [May 2 posts](https://shkspr.mobi/blog/2008/05/)
        
        June
        
        [July 1 post](https://shkspr.mobi/blog/2008/07/)
        
        [August 3 posts](https://shkspr.mobi/blog/2008/08/)
        
        [September 1 post](https://shkspr.mobi/blog/2008/09/)
        
        [October 3 posts](https://shkspr.mobi/blog/2008/10/)
        
        [November 2 posts](https://shkspr.mobi/blog/2008/11/)
        
        [December 1 post](https://shkspr.mobi/blog/2008/12/)
        
*   2007
    *   January
        
        February
        
        March
        
        April
        
        May
        
        June
        
        July
        
        August
        
        September
        
        October
        
        [November 4 posts](https://shkspr.mobi/blog/2007/11/)
        
        [December 5 posts](https://shkspr.mobi/blog/2007/12/)
        
*   2006
    *   January
        
        February
        
        March
        
        [April 1 post](https://shkspr.mobi/blog/2006/04/)
        
        May
        
        June
        
        July
   