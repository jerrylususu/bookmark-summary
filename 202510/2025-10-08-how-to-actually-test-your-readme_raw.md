Title: How to *actually* test your readme

URL Source: https://shkspr.mobi/blog/2025/10/how-to-actually-test-your-readme/

Published Time: 2025-10-07T12:34:08+01:00

Markdown Content:
How to *actually* test your readme – Terence Eden’s Blog

===============
[![Image 3: Terence Eden. He has a beard and is smiling.](https://shkspr.mobi/apple-touch-icon.png)](https://shkspr.mobi/blog)[Terence Eden’s Blog](https://shkspr.mobi/blog)[![Image 4: Mastodon](blob:http://localhost/fa1da30ab36ffc5a1c66c2463941d260)](https://mastodon.social/@edent)[![Image 5: LinkedIn](blob:http://localhost/87e1e72529620add6a9c9cb38e3d9991)](https://linkedin.com/in/TerenceEden)[![Image 6: GitHub.](blob:http://localhost/187b809ff3c95149718df61d27417e84)](https://github.com/edent)[![Image 7: Email.](blob:http://localhost/e3392786a2c5f8e780db6ce4a7a1237c)](https://edent.tel/)[![Image 8: Feed.](blob:http://localhost/f13fd041ddf51ffb91f31fef928e56d3)](https://shkspr.mobi/blog/feed/atom)Theme Switcher:🌒 Dark  🌞 Light  📰 eInk  💻 xterm  🥴 Drunk  👻 Nude  ♻️ Reset  ![Image 9: 2025-10-07](blob:http://localhost/f2d766f018c9080f0f77d128fc430bbf)
[How to *actually* test your readme](https://shkspr.mobi/blog/2025/10/how-to-actually-test-your-readme/)
========================================================================================================

[developers](https://shkspr.mobi/blog/tag/developers/)[Free Software](https://shkspr.mobi/blog/tag/free-software/)[linux](https://shkspr.mobi/blog/tag/linux/)[Open Source](https://shkspr.mobi/blog/tag/open-source/) · [7 comments](https://shkspr.mobi/blog/2025/10/how-to-actually-test-your-readme/#comments) · 150 words · Viewed~383 times

* * *

If you've spent any time using Linux, you'll be used to installing software like this:

> The README says to download from this link. Huh, I'm not sure how to unarchive .tar.xz files - guess I'll search for that. Right, it says run `setup.sh` hmm, that doesn't work. Oh, I need to set the permissions. What was the `chmod` command again? OK, that's working. Wait, it needs `sudo`. Let me run that again. Hang on, am I in the right directory? Here it goes. What, it crapped out. I don't have some random library - how the hell am I meant to install that? My distro has v21 but this requires <=19. Ah, I also need to upgrade something which isn't supplied by repo. Nearly there, just need to compile this obscure project from SourceForge which was inexplicably installed on the original dev's machine and then I'll be good to go. Nope. Better raise an issue on GitHub. Oh, look, it is tomorrow.

As a developer, you probably don't want to answer dozens of tickets complaining that users are frustrated with your work. You thought you made the README really clear and - hey! - it works on your machine.

There are various solutions to this problem - developers can release AppImages, or Snaps, or FlatPaks, or Docker or whatever. But that's a bit of stretch for a solo dev who is slinging out a little tool that they coded in their spare time. And, even those don't always work as seamlessly as you'd hope.

There's an easier solution:

1.   Follow the steps in your README
2.   See if they work.
3.   …
4.   That's it.

OK, that's a bit reductive! There are a million variables which go into a test - so I'm going to introduce you to a secret _zeroth_ step.

1.   Spin up a fresh Virtual Machine with a recent-ish distro.

If you are a developer, your machine probably has a billion weird configurations and obscure libraries installed on it - things which _definitely_ aren't on your users' machines. Having a box-fresh VM means than you are starting with a blank-slate. If, when following your README, you discover that the app doesn't install because of a missing dependency, you can adjust your README to include `apt install whatever`.

[OK, but how?](https://shkspr.mobi/blog/2025/10/how-to-actually-test-your-readme/#ok-but-how)
---------------------------------------------------------------------------------------------

Personally, I like [Boxes](https://flathub.org/apps/org.gnome.Boxes) as it gives you a simple choice of VMs - but there are plenty of other Virtual Machine managers out there.

![Image 10: List of Linux OSes.](https://shkspr.mobi/blog/wp-content/uploads/2025/07/OS-Selection.webp)
Pick a standard OS that you like. I think the latest Ubuntu Server is pretty lightweight and is a good baseline for what people are likely to have. But feel free to pick something with a GUI or whatever suits your audience.

Once your VM is installed and set up for basic use, take a snapshot.

![Image 11: Pop up showing a snapshot of a virtual machine.](https://shkspr.mobi/blog/wp-content/uploads/2025/07/revert.webp)
Every time you want to test or re-test a README, revert back to the _original_ state of your box. That way you won't have odd half-installed packages laying about.

Your next step is to think about how much hand-holding do you want to do?

For example, the default Debian doesn't ship with git. Does your README need to tell people to `sudo apt install git` and then walk them through configuring it so that they can `git clone` your repo?

Possibly! Who is your audience? If you've created a tool which is likely to be used by newbies who are just getting started with their first Raspberry Pi then, yeah, you probably will need to include that. Why? Because it will save you from receiving a lot of repeated questions and frustrated emails.

OK, but most developers will have `gcc` installed, right? Maybe! But it doesn't do any harm to include it in a long list of `apt get …` anyway, does it? Similarly, does everyone know how to upgrade to the very latest npm?

If your software is designed for people who are experienced computer touchers, don't fall into the trap of thinking that they know everything you do. I find it best to assume people are intelligent but not experienced; it doesn't hurt to give _slightly_ too much detail.

The best way to do this is to record _everything_ you do after logging into the blank VM.

1.   Restore the snapshot.
2.   Log in.
3.   Run all the commands you need to get your software working.
4.   Once done, run `history -w history.txt`
    *   That will print out _every_ command you ran. 

5.   Copy that text into your README.

Hey presto! You now have README instructions which have been tested to work. Even on the most bare-bones machine, you can say that your README will allow the user to get started with your software with the minimum amount of head-scratching.

Now, this isn't foolproof. Maybe the user has an ancient operating system running on obsolete hardware which is constantly bombarded by cosmic rays. But at least this way your issues won't be clogged up by people saying their install failed because `lib-foobar` wasn't available or that `./configure` had fatal errors.

A great example is [the Opus Codec README](https://github.com/xiph/opus/blob/main/README). I went into a fresh Ubuntu machine, followed the readme, ran the above history command, and got this:

```
sudo apt-get install git autoconf automake libtool gcc make
git clone https://gitlab.xiph.org/xiph/opus.git
cd opus
./autogen.sh
./configure
make
sudo make install
```

Everything worked! There was no missing step or having to dive into another README to figure out how to bind flarg 6.9 with schnorp-unstable.

So that's my plea to you, dear developer friend. Make sure your README contains both the necessary _and_ sufficient information required to install your software. For your sake, as much as mine!

[Wait! You didn't follow your own advice!](https://shkspr.mobi/blog/2025/10/how-to-actually-test-your-readme/#wait-you-didnt-follow-your-own-advice)
----------------------------------------------------------------------------------------------------------------------------------------------------

You're quite right. Feel free to send a pull request to correct this post - as I shall be doing with any unhelpful READMEs I find along the way.

* * *

Share this post on…
-------------------

*   [![Image 12: Mastodon](blob:http://localhost/fa1da30ab36ffc5a1c66c2463941d260)](https://tootpick.org/#text=How%20to%20%2Aactually%2A%20test%20your%20readme%20https%3A%2F%2Fshkspr.mobi%2Fblog%2F2025%2F10%2Fhow-to-actually-test-your-readme%2F)
*   [![Image 13: Facebook](blob:http://localhost/efcf4ed3a77499732e3f66a953f0a16e)](https://www.facebook.com/sharer.php?u=https%3A%2F%2Fshkspr.mobi%2Fblog%2F2025%2F10%2Fhow-to-actually-test-your-readme%2F&t=How%20to%20%2Aactually%2A%20test%20your%20readme)
*   [![Image 14: LinkedIn](blob:http://localhost/87e1e72529620add6a9c9cb38e3d9991)](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fshkspr.mobi%2Fblog%2F2025%2F10%2Fhow-to-actually-test-your-readme%2F)
*   [![Image 15: BlueSky](blob:http://localhost/44d0beed31dd94e72f3bec5997d78f73)](https://bsky.app/intent/compose?text=How%20to%20%2Aactually%2A%20test%20your%20readme%20https%3A%2F%2Fshkspr.mobi%2Fblog%2F2025%2F10%2Fhow-to-actually-test-your-readme%2F)
*   [![Image 16: Threads](blob:http://localhost/84ba40141e083d143dd851e80d1e3f53)](https://www.threads.com/intent/post?url=https%3A%2F%2Fshkspr.mobi%2Fblog%2F2025%2F10%2Fhow-to-actually-test-your-readme%2F&text=How%20to%20%2Aactually%2A%20test%20your%20readme)
*   [![Image 17: Reddit](blob:http://localhost/3c2063ad67740fb653a57a197a750ede)](https://www.reddit.com/submit?url=https%3A%2F%2Fshkspr.mobi%2Fblog%2F2025%2F10%2Fhow-to-actually-test-your-readme%2F&title=How%20to%20%2Aactually%2A%20test%20your%20readme)
*   [![Image 18: HackerNews](blob:http://localhost/a75ae78b2f12bebbc6d772bed363defa)](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fshkspr.mobi%2Fblog%2F2025%2F10%2Fhow-to-actually-test-your-readme%2F&t=How%20to%20%2Aactually%2A%20test%20your%20readme)
*   [![Image 19: Lobsters](blob:http://localhost/9ccd488cfe94d4cfd9308e29e66b969f)](https://lobste.rs/stories/new?url=https%3A%2F%2Fshkspr.mobi%2Fblog%2F2025%2F10%2Fhow-to-actually-test-your-readme%2F&title=How%20to%20%2Aactually%2A%20test%20your%20readme)
*   [![Image 20: WhatsApp](blob:http://localhost/d1f7ee7453e3a1624b3ea643293a0601)](https://api.whatsapp.com/send/?text=https%3A%2F%2Fshkspr.mobi%2Fblog%2F2025%2F10%2Fhow-to-actually-test-your-readme%2F)
*   [![Image 21: Telegram](blob:http://localhost/4081d83a5487986611869a54f839f4cc)](https://telegram.me/share/url?url=https%3A%2F%2Fshkspr.mobi%2Fblog%2F2025%2F10%2Fhow-to-actually-test-your-readme%2F&text=How%20to%20%2Aactually%2A%20test%20your%20readme)

7 thoughts on “How to *actually* test your readme”
--------------------------------------------------

1.   ![Image 22](https://files.mastodon.social/accounts/avatars/108/193/331/678/238/726/original/e3859515a524704f.jpg)
### ![Image 23](https://shkspr.mobi/favicons/?domain=mastodon.social)[Hylke Bons 🥜](https://mastodon.social/@hbons/115332786892768343) [@Edent](https://mastodon.social/@Edent) explains why "just bundle/npm install!" has never ever worked for me. 
[Reply](https://shkspr.mobi/blog/2025/10/how-to-actually-test-your-readme/?replytocom=469075#respond) | [Reply to original comment on mastodon.social](https://mastodon.social/@hbons/115332786892768343)[2025-10-07 13:04](https://shkspr.mobi/blog/2025/10/how-to-actually-test-your-readme/#comment-469075)

2.   ### ![Image 24](https://shkspr.mobi/favicons/?domain=phpc.social)[Lincoln Russell](https://phpc.social/@linc) [@blog](https://shkspr.mobi/blog) 💯

I wrote a 10,000-word essay on a modern MAMP localhost setup because I was so tired of barebones instructions that never give enough context because engineers always want to make it *look* easy instead of acknowledging and helping with the parts that aren't. 
[Reply](https://shkspr.mobi/blog/2025/10/how-to-actually-test-your-readme/?replytocom=469077#respond) | [Reply to original comment on phpc.social](https://phpc.social/@linc/115332973043857158)[2025-10-07 13:51](https://shkspr.mobi/blog/2025/10/how-to-actually-test-your-readme/#comment-469077)

3.   ![Image 25](https://files.mastodon.social/cache/accounts/avatars/109/366/293/058/777/623/original/5c82b8600e9ad1ea.jpg)
### ![Image 26](https://shkspr.mobi/favicons/?domain=hachyderm.io)[Paul Leader](https://hachyderm.io/@Noneeeed/115332977462508878) [@Edent](https://mastodon.social/@Edent) " I find it best to assume people are intelligent but not experienced" - now those are words to live by. 
[Reply](https://shkspr.mobi/blog/2025/10/how-to-actually-test-your-readme/?replytocom=469078#respond) | [Reply to original comment on hachyderm.io](https://hachyderm.io/@Noneeeed/115332977462508878)[2025-10-07 13:52](https://shkspr.mobi/blog/2025/10/how-to-actually-test-your-readme/#comment-469078)

4.   ![Image 27](https://shkspr.mobi/blog/wp-content/litespeed/avatar/ac231b5e24356d0d38459270005e8564.jpg?ver=1759844732)
### Adina Reading this whole post was worth it JUST to learn about history -w history.txt The rest was also smart and great advice but man, that one trick is definitely going to help me. Thanks! 
[Reply](https://shkspr.mobi/blog/2025/10/how-to-actually-test-your-readme/?replytocom=469090#respond)[2025-10-07 14:45](https://shkspr.mobi/blog/2025/10/how-to-actually-test-your-readme/#comment-469090)

5.   ![Image 28](https://files.mastodon.social/cache/accounts/avatars/109/458/524/971/088/305/original/c7ada5506c73f58f.jpg)
### ![Image 29](https://shkspr.mobi/favicons/?domain=dmv.community)[killick](https://dmv.community/@killick/115333701045465296) [@Edent](https://mastodon.social/@Edent)

I hate HOWTO videos for the same reason-- rare is the video where they explain what can go wrong and how to tell and what to do about it. 
[Reply](https://shkspr.mobi/blog/2025/10/how-to-actually-test-your-readme/?replytocom=469114#respond) | [Reply to original comment on dmv.community](https://dmv.community/@killick/115333701045465296)[2025-10-07 16:56](https://shkspr.mobi/blog/2025/10/how-to-actually-test-your-readme/#comment-469114)

6.   ![Image 30](https://cdn.bsky.app/img/avatar/plain/did:plc:uewhttehh6cglkpmtvv55adx/bafkreicikr6ktc735ttq22akvwic25ng3ij5toefgohjbi4bgenqkfvzey@jpeg)
### ![Image 31](https://shkspr.mobi/favicons/?domain=bsky.app)[Gordon Guthrie](https://bsky.app/profile/foundationsofthedigitalstate.com/post/3m2mj52tjlk2a) this all the way. I develop inside docker and do my install as a docker file so that its unambiguos and repeatable[](https://shkspr.mobi/blog/2025/10/how-to-actually-test-your-readme/) 
[Reply](https://shkspr.mobi/blog/2025/10/how-to-actually-test-your-readme/?replytocom=469117#respond) | [Reply to original comment on bsky.app](https://bsky.app/profile/foundationsofthedigitalstate.com/post/3m2mj52tjlk2a)[2025-10-07 17:08](https://shkspr.mobi/blog/2025/10/how-to-actually-test-your-readme/#comment-469117)

7.   ![Image 32](https://cdn.bsky.app/img/avatar/plain/did:plc:ywvrgb5tct53do3cpw2b4sxa/bafkreiabog5xug5flkjbsxdblyew4odwaz2szysgs3x3nihifhsyvzt2ya@jpeg)
### ![Image 33](https://shkspr.mobi/favicons/?domain=bsky.app)[Alex](https://bsky.app/profile/blangry.bsky.social/post/3m2mjvrugbs2c) I may be a minority audience as well, but there's a level of "I know how to do things in the terminal, but I don't usually compile my own programs" level of Linux user, where I'm trying my best to avoid being rm -rf'd by instructions but not a complete newb.[](https://shkspr.mobi/blog/2025/10/how-to-actually-test-your-readme/) 
[Reply](https://shkspr.mobi/blog/2025/10/how-to-actually-test-your-readme/?replytocom=469123#respond) | [Reply to original comment on bsky.app](https://bsky.app/profile/blangry.bsky.social/post/3m2mjvrugbs2c)[2025-10-07 17:21](https://shkspr.mobi/blog/2025/10/how-to-actually-test-your-readme/#comment-469123)

8.   ![Image 34](blob:http://localhost/8e64eacbbb49530f56ef3c9fedbc7be9)
### [More comments on Mastodon](https://mastodon.social/@Edent/115332671275842422).

### What are your reckons? [Cancel reply](https://shkspr.mobi/blog/2025/10/how-to-actually-test-your-readme/#respond)

All comments are moderated and may not be published immediately. Your email address will _not_ be published.

Comment: 

See allowed HTML elements:
```
<a href="" title="">
								<abbr title="">
								<acronym title="">
								<b>
								<blockquote cite="">
								<br>
								<cite>
								<code>
								<del datetime="">
								<em>
								<i>
								<img src="" alt="" title="" srcset="">
								<p>
								<pre>
								<q cite="">
								<s>
								<strike>
								<strong>
```

Your Name (required): Your Email (required): Your Website (optional): 

To respond on your own website, write a post which contains a link to this post - then enter the URl of your page here. [Learn more about WebMentions](https://indieweb.org/webmention).

URl of your article

🔎 Search
---------

Search for: 

🗓️ Explore The Archives
------------------------

*   2025
    *   [January 17 posts](https://shkspr.mobi/blog/2025/01/)[February 20 posts](https://shkspr.mobi/blog/2025/02/)[March 23 posts](https://shkspr.mobi/blog/2025/03/)[April 22 posts](https://shkspr.mobi/blog/2025/04/)[May 16 posts](https://shkspr.mobi/blog/2025/05/)[June 28 posts](https://shkspr.mobi/blog/2025/06/)[July 24 posts](https://shkspr.mobi/blog/2025/07/)[August 20 posts](https://shkspr.mobi/blog/2025/08/)[September 15 posts](https://shkspr.mobi/blog/2025/09/)[October 4 posts](https://shkspr.mobi/blog/2025/10/)
November

December

*   2024
    *   [January 31 posts](https://shkspr.mobi/blog/2024/01/)[February 29 posts](https://shkspr.mobi/blog/2024/02/)[March 31 posts](https://shkspr.mobi/blog/2024/03/)[April 30 posts](https://shkspr.mobi/blog/2024/04/)[May 31 posts](https://shkspr.mobi/blog/2024/05/)[June 30 posts](https://shkspr.mobi/blog/2024/06/)[July 19 posts](https://shkspr.mobi/blog/2024/07/)[August 18 posts](https://shkspr.mobi/blog/2024/08/)[September 18 posts](https://shkspr.mobi/blog/2024/09/)[October 29 posts](https://shkspr.mobi/blog/2024/10/)[November 31 posts](https://shkspr.mobi/blog/2024/11/)[December 30 posts](https://shkspr.mobi/blog/2024/12/)

*   2023
    *   [January 31 posts](https://shkspr.mobi/blog/2023/01/)[February 28 posts](https://shkspr.mobi/blog/2023/02/)[March 31 posts](https://shkspr.mobi/blog/2023/03/)[April 30 posts](https://shkspr.mobi/blog/2023/04/)[May 31 posts](https://shkspr.mobi/blog/2023/05/)[June 30 posts](https://shkspr.mobi/blog/2023/06/)[July 31 posts](https://shkspr.mobi/blog/2023/07/)[August 31 posts](https://shkspr.mobi/blog/2023/08/)[September 30 posts](https://shkspr.mobi/blog/2023/09/)[October 31 posts](https://shkspr.mobi/blog/2023/10/)[November 30 posts](https://shkspr.mobi/blog/2023/11/)[December 31 posts](https://shkspr.mobi/blog/2023/12/)

*   2022
    *   [January 30 posts](https://shkspr.mobi/blog/2022/01/)[February 23 posts](https://shkspr.mobi/blog/2022/02/)[March 15 posts](https://shkspr.mobi/blog/2022/03/)[April 19 posts](https://shkspr.mobi/blog/2022/04/)[May 19 posts](https://shkspr.mobi/blog/2022/05/)[June 19 posts](https://shkspr.mobi/blog/2022/06/)[July 19 posts](https://shkspr.mobi/blog/2022/07/)[August 18 posts](https://shkspr.mobi/blog/2022/08/)[September 12 posts](https://shkspr.mobi/blog/2022/09/)[October 8 posts](https://shkspr.mobi/blog/2022/10/)[November 30 posts](https://shkspr.mobi/blog/2022/11/)[December 31 posts](https://shkspr.mobi/blog/2022/12/)

*   2021
    *   [January 31 posts](https://shkspr.mobi/blog/2021/01/)[February 28 posts](https://shkspr.mobi/blog/2021/02/)[March 31 posts](https://shkspr.mobi/blog/2021/03/)[April 30 posts](https://shkspr.mobi/blog/2021/04/)[May 31 posts](https://shkspr.mobi/blog/2021/05/)[June 30 posts](https://shkspr.mobi/blog/2021/06/)[July 31 posts](https://shkspr.mobi/blog/2021/07/)[August 31 posts](https://shkspr.mobi/blog/2021/08/)[September 30 posts](https://shkspr.mobi/blog/2021/09/)[October 31 posts](https://shkspr.mobi/blog/2021/10/)[November 30 posts](https://shkspr.mobi/blog/2021/11/)[December 31 posts](https://shkspr.mobi/blog/2021/12/)

*   2020
    *   [January 31 posts](https://shkspr.mobi/blog/2020/01/)[February 29 posts](https://shkspr.mobi/blog/2020/02/)[March 31 posts](https://shkspr.mobi/blog/2020/03/)[April 30 posts](https://shkspr.mobi/blog/2020/04/)[May 31 posts](https://shkspr.mobi/blog/2020/05/)[June 30 posts](https://shkspr.mobi/blog/2020/06/)[July 31 posts](https://shkspr.mobi/blog/2020/07/)[August 31 posts](https://shkspr.mobi/blog/2020/08/)[September 30 posts](https://shkspr.mobi/blog/2020/09/)[October 31 posts](https://shkspr.mobi/blog/2020/10/)[November 30 posts](https://shkspr.mobi/blog/2020/11/)[December 31 posts](https://shkspr.mobi/blog/2020/12/)

*   2019
    *   [January 31 posts](https://shkspr.mobi/blog/2019/01/)[February 12 posts](https://shkspr.mobi/blog/2019/02/)[March 17 posts](https://shkspr.mobi/blog/2019/03/)[April 12 posts](https://shkspr.mobi/blog/2019/04/)[May 12 posts](https://shkspr.mobi/blog/2019/05/)[June 10 posts](https://shkspr.mobi/blog/2019/06/)[July 7 posts](https://shkspr.mobi/blog/2019/07/)[August 5 posts](https://shkspr.mobi/blog/2019/08/)[September 6 posts](https://shkspr.mobi/blog/2019/09/)[October 14 posts](https://shkspr.mobi/blog/2019/10/)[November 30 posts](https://shkspr.mobi/blog/2019/11/)[December 17 posts](https://shkspr.mobi/blog/2019/12/)

*   2018
    *   [January 8 posts](https://shkspr.mobi/blog/2018/01/)[February 4 posts](https://shkspr.mobi/blog/2018/02/)[March 6 posts](https://shkspr.mobi/blog/2018/03/)[April 14 posts](https://shkspr.mobi/blog/2018/04/)[May 5 posts](https://shkspr.mobi/blog/2018/05/)[June 6 posts](https://shkspr.mobi/blog/2018/06/)[July 6 posts](https://shkspr.mobi/blog/2018/07/)[August 13 posts](https://shkspr.mobi/blog/2018/08/)[September 14 posts](https://shkspr.mobi/blog/2018/09/)[October 8 posts](https://shkspr.mobi/blog/2018/10/)[November 30 posts](https://shkspr.mobi/blog/2018/11/)[December 4 posts](https://shkspr.mobi/blog/2018/12/)

*   2017
    *   [January 12 posts](https://shkspr.mobi/blog/2017/01/)[February 9 posts](https://shkspr.mobi/blog/2017/02/)[March 8 posts](https://shkspr.mobi/blog/2017/03/)[April 4 posts](https://shkspr.mobi/blog/2017/04/)[May 10 posts](https://shkspr.mobi/blog/2017/05/)[June 5 posts](https://shkspr.mobi/blog/2017/06/)[July 5 posts](https://shkspr.mobi/blog/2017/07/)[August 6 posts](https://shkspr.mobi/blog/2017/08/)[September 3 posts](https://shkspr.mobi/blog/2017/09/)[October 4 posts](https://shkspr.mobi/blog/2017/10/)[November 30 posts](https://shkspr.mobi/blog/2017/11/)
December

*   2016
    *   [January 10 posts](https://shkspr.mobi/blog/2016/01/)[February 10 posts](https://shkspr.mobi/blog/2016/02/)[March 11 posts](https://shkspr.mobi/blog/2016/03/)[April 9 posts](https://shkspr.mobi/blog/2016/04/)[May 8 posts](https://shkspr.mobi/blog/2016/05/)[June 9 posts](https://shkspr.mobi/blog/2016/06/)[July 6 posts](https://shkspr.mobi/blog/2016/07/)[August 9 posts](https://shkspr.mobi/blog/2016/08/)[September 4 posts](https://shkspr.mobi/blog/2016/09/)[October 2 posts](https://shkspr.mobi/blog/2016/10/)[November 30 posts](https://shkspr.mobi/blog/2016/11/)[December 14 posts](https://shkspr.mobi/blog/2016/12/)

*   2015
    *   [January 8 posts](https://shkspr.mobi/blog/2015/01/)[February 11 posts](https://shkspr.mobi/blog/2015/02/)[March 10 posts](https://shkspr.mobi/blog/2015/03/)[April 4 posts](https://shkspr.mobi/blog/2015/04/)[May 9 posts](https://shkspr.mobi/blog/2015/05/)[June 3 posts](https://shkspr.mobi/blog/2015/06/)[July 7 posts](https://shkspr.mobi/blog/2015/07/)[August 9 posts](https://shkspr.mobi/blog/2015/08/)[September 10 posts](https://shkspr.mobi/blog/2015/09/)[October 2 posts](https://shkspr.mobi/blog/2015/10/)[November 30 posts](https://shkspr.mobi/blog/2015/11/)[December 4 posts](https://shkspr.mobi/blog/2015/12/)

*   2014
    *   [January 13 posts](https://shkspr.mobi/blog/2014/01/)[February 13 posts](https://shkspr.mobi/blog/2014/02/)[March 15 posts](https://shkspr.mobi/blog/2014/03/)[April 14 posts](https://shkspr.mobi/blog/2014/04/)[May 8 posts](https://shkspr.mobi/blog/2014/05/)[June 7 posts](https://shkspr.mobi/blog/2014/06/)[July 9 posts](https://shkspr.mobi/blog/2014/07/)[August 5 posts](https://shkspr.mobi/blog/2014/08/)[September 5 posts](https://shkspr.mobi/blog/2014/09/)[October 1 post](https://shkspr.mobi/blog/2014/10/)[November 30 posts](https://shkspr.mobi/blog/2014/11/)[December 20 posts](https://shkspr.mobi/blog/2014/12/)

*   2013
    *   [January 25 posts](https://shkspr.mobi/blog/2013/01/)[February 17 posts](https://shkspr.mobi/blog/2013/02/)[March 15 posts](https://shkspr.mobi/blog/2013/03/)[April 18 posts](https://shkspr.mobi/blog/2013/04/)[May 11 posts](https://shkspr.mobi/blog/2013/05/)[June 14 posts](https://shkspr.mobi/blog/2013/06/)[July 6 posts](https://shkspr.mobi/blog/2013/07/)[August 14 posts](https://shkspr.mobi/blog/2013/08/)[September 6 posts](https://shkspr.mobi/blog/2013/09/)[October 4 posts](https://shkspr.mobi/blog/2013/10/)[November 30 posts](https://shkspr.mobi/blog/2013/11/)[December 15 posts](https://shkspr.mobi/blog/2013/12/)

*   2012
    *   [January 14 posts](https://shkspr.mobi/blog/2012/01/)[February 8 posts](https://shkspr.mobi/blog/2012/02/)[March 13 posts](https://shkspr.mobi/blog/2012/03/)[April 15 posts](https://shkspr.mobi/blog/2012/04/)[May 10 posts](https://shkspr.mobi/blog/2012/05/)[June 16 posts](https://shkspr.mobi/blog/2012/06/)[July 8 posts](https://shkspr.mobi/blog/2012/07/)[August 8 posts](https://shkspr.mobi/blog/2012/08/)[September 6 posts](https://shkspr.mobi/blog/2012/09/)[October 6 posts](https://shkspr.mobi/blog/2012/10/)[November 30 posts](https://shkspr.mobi/blog/2012/11/)[December 30 posts](https://shkspr.mobi/blog/2012/12/)

*   2011
    *   [January 13 posts](https://shkspr.mobi/blog/2011/01/)[February 11 posts](https://shkspr.mobi/blog/2011/02/)[March 12 posts](https://shkspr.mobi/blog/2011/03/)[April 12 posts](https://shkspr.mobi/blog/2011/04/)[May 8 posts](https://shkspr.mobi/blog/2011/05/)[June 8 posts](https://shkspr.mobi/blog/2011/06/)[July 6 posts](https://shkspr.mobi/blog/2011/07/)[August 5 posts](https://shkspr.mobi/blog/2011/08/)[September 11 posts](https://shkspr.mobi/blog/2011/09/)[October 7 posts](https://shkspr.mobi/blog/2011/10/)[November 30 posts](https://shkspr.mobi/blog/2011/11/)[December 17 posts](https://shkspr.mobi/blog/2011/12/)

*   2010
    *   [January 6 posts](https://shkspr.mobi/blog/2010/01/)[February 15 posts](https://shkspr.mobi/blog/2010/02/)[March 12 posts](https://shkspr.mobi/blog/2010/03/)[April 13 posts](https://shkspr.mobi/blog/2010/04/)[May 4 posts](https://shkspr.mobi/blog/2010/05/)[June 3 posts](https://shkspr.mobi/blog/2010/06/)[July 15 posts](https://shkspr.mobi/blog/2010/07/)[August 8 posts](https://shkspr.mobi/blog/2010/08/)[September 11 posts](https://shkspr.mobi/blog/2010/09/)[October 10 posts](https://shkspr.mobi/blog/2010/10/)[November 30 posts](https://shkspr.mobi/blog/2010/11/)[December 9 posts](https://shkspr.mobi/blog/2010/12/)

*   2009
    *   [January 1 post](https://shkspr.mobi/blog/2009/01/)[February 5 posts](https://shkspr.mobi/blog/2009/02/)[March 3 posts](https://shkspr.mobi/blog/2009/03/)[April 7 posts](https://shkspr.mobi/blog/2009/04/)[May 12 posts](https://shkspr.mobi/blog/2009/05/)[June 8 posts](https://shkspr.mobi/blog/2009/06/)[July 10 posts](https://shkspr.mobi/blog/2009/07/)[August 10 posts](https://shkspr.mobi/blog/2009/08/)[September 12 posts](https://shkspr.mobi/blog/2009/09/)[October 22 posts](https://shkspr.mobi/blog/2009/10/)[November 31 posts](https://shkspr.mobi/blog/2009/11/)[December 15 posts](https://shkspr.mobi/blog/2009/12/)

*   2008
    *   [January 2 posts](https://shkspr.mobi/blog/2008/01/)
February

[March 2 posts](https://shkspr.mobi/blog/2008/03/)[April 3 posts](https://shkspr.mobi/blog/2008/04/)[May 2 posts](https://shkspr.mobi/blog/2008/05/)
June

[July 1 post](https://shkspr.mobi/blog/2008/07/)[August 3 posts](https://shkspr.mobi/blog/2008/08/)[September 1 post](https://shkspr.mobi/blog/2008/09/)[October 3 posts](https://shkspr.mobi/blog/2008/10/)[November 2 posts](https://shkspr.mobi/blog/2008/11/)[December 1 post](https://shkspr.mobi/blog/2008/12/)

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

[November 4 posts](https://shkspr.mobi/blog/2007/11/)[December 5 posts](https://shkspr.mobi/blog/2007/12/)

*   2006
    *   January

February

March

[April 1 post](https://shkspr.mobi/blog/2006/04/)
May

June

July

August

September

October

[November 1 post](https://shkspr.mobi/blog/2006/11/)
December

*   2005
    *   January

February

[March 1 post](https://shkspr.mobi/blog/2005/03/)
April

May

June

July

August

[September 1 post](https://shkspr.mobi/blog/2005/09/)
October

November

December

*   2004
    *   [January 1 post](https://shkspr.mobi/blog/2004/01/)
February

March

April

[May 5 posts](https://shkspr.mobi/blog/2004/05/)[June 3 posts](https://shkspr.mobi/blog/2004/06/)[July 1 post](https://shkspr.mobi/blog/2004/07/)
August

September

October

November

December

*   2003
    *   January

February

[March 2 posts](https://shkspr.mobi/blog/2003/03/)
April

May

June

July

August

September

October

November

December

*   2002
    *   January

[February 1 post](https://shkspr.mobi/blog/2002/02/)
March

[April 3 posts](https://shkspr.mobi/blog/2002/04/)
May

June

July

August

September

October

November

December

*   2001
    *   January

February

March

April

May

June

[July 1 post](https://shkspr.mobi/blog/2001/07/)
August

September

[October 1 post](https://shkspr.mobi/blog/2001/10/)
November

December

*   2000
    *   January

February

[March 1 post](https://shkspr.mobi/blog/2000/03/)
April

May

June

July

August

September

[October 1 post](https://shkspr.mobi/blog/2000/10/)[November 1 post](https://shkspr.mobi/blog/2000/11/)
December

*   1999
    *   January

February

March

April

May

June

July

August

[September 1 post](https://shkspr.mobi/blog/1999/09/)
October

November

[December 1 post](https://shkspr.mobi/blog/1999/12/)

*   1998
    *   January

February

March

April

[May 1 post](https://shkspr.mobi/blog/1998/05/)
June

July

August

September

October

November

December

*   1997
    *   [January 1 post](https://shkspr.mobi/blog/1997/01/)
February

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

*   1995
    *   January

February

[March 1 post](https://shkspr.mobi/blog/1995/03/)
April

[May 1 post](https://shkspr.mobi/blog/1995/05/)
June

July

August

September

October

November

December

*   1994
    *   January

February

March

[April 1 post](https://shkspr.mobi/blog/1994/04/)
May

June

July

August

September

October

November

December

*   1993
    *   January

February

March

April

May

[June 1 post](https://shkspr.mobi/blog/1993/06/)
July

August

September

October

November

December

*   1987
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

November

[December 1 post](https://shkspr.mobi/blog/1987/12/)

Subscribe by Email
------------------

*   [© Terence Eden](https://shkspr.mobi/blog/copyright-terence-eden/)
*   [Support My Blog](https://shkspr.mobi/blog/support/)
*   [About Me](https://shkspr.mobi/blog/about/)
*   [Contact Me](https://edent.tel/)
*   [Open Source Contributions](https://shkspr.mobi/blog/open-source-contributions/)
*   [Subscribe](https://shkspr.mobi/blog/subscribe/)
*   [Citations](https://shkspr.mobi/blog/citations/)
*   [Library](https://shkspr.mobi/blog/library/)
*   [On This Day](https://shkspr.mobi/blog/on-this-day/)
*   [Trending Posts](https://shkspr.mobi/blog/trending/)
*   [Random Post](https://shkspr.mobi/blog/random)
*   [Link Rot](https://shkspr.mobi/blog/link-rot/)

[ISSN 2753-1570](https://portal.issn.org/resource/ISSN/2753-1570)ⅯⅯⅩⅩⅤ
ⓒ [Terence Eden](https://shkspr.mobi/blog/)