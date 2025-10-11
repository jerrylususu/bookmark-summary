Title: Quick and dirty bar-charts using HTML's meter element

URL Source: https://shkspr.mobi/blog/2025/10/quick-and-dirty-bar-charts-using-htmls-meter-element/

Published Time: 2025-10-11T12:34:57+01:00

Markdown Content:
Quick and dirty bar-charts using HTML’s meter element – Terence Eden’s Blog

===============
[![Image 3: Terence Eden. He has a beard and is smiling.](https://shkspr.mobi/apple-touch-icon.png)](https://shkspr.mobi/blog)[Terence Eden’s Blog](https://shkspr.mobi/blog)[![Image 4: Mastodon](blob:http://localhost/fa1da30ab36ffc5a1c66c2463941d260)](https://mastodon.social/@edent)[![Image 5: LinkedIn](blob:http://localhost/87e1e72529620add6a9c9cb38e3d9991)](https://linkedin.com/in/TerenceEden)[![Image 6: GitHub.](blob:http://localhost/187b809ff3c95149718df61d27417e84)](https://github.com/edent)[![Image 7: Email.](blob:http://localhost/e3392786a2c5f8e780db6ce4a7a1237c)](https://edent.tel/)[![Image 8: Feed.](blob:http://localhost/f13fd041ddf51ffb91f31fef928e56d3)](https://shkspr.mobi/blog/feed/atom)Theme Switcher:🌒 Dark  🌞 Light  📰 eInk  💻 xterm  🥴 Drunk  👻 Nude  ♻️ Reset  ![Image 9: 2025-10-11](blob:http://localhost/4a3f3dc270930b1947c35d2ecb139553)
[Quick and dirty bar-charts using HTML's meter element](https://shkspr.mobi/blog/2025/10/quick-and-dirty-bar-charts-using-htmls-meter-element/)
===============================================================================================================================================

[css](https://shkspr.mobi/blog/tag/css/)[HTML](https://shkspr.mobi/blog/tag/html/) · 300 words

* * *

"If it's stupid but it works, it's not stupid."

I want to draw some vertical bar charts. I don't want to use a 3rd party library, or bundle someone else's CSS, or learn how to build SVGs.

HTML contains a `<meter>` element. It is used like this:

![Image 10](https://shkspr.mobi/blog/wp-content/plugins/tempest-highlight//svg/html.svg) HTML
```
<meter min="0" max="4000" value="1234">1234</meter>
```

Which looks like this: 1234

There isn't _much_ you can do to style it. Browser manufacturers seem to have forgotten it exists and the CSS standard kind of ignores it.

It _is_ possible to use CSS to rotate it using:

![Image 11](https://shkspr.mobi/blog/wp-content/plugins/tempest-highlight//svg/css.svg) CSS
```
meter {
   transform: rotate(-90deg);
}
```

But then you have to mess about with origins and the box model gets a bit confused.

See what 1234 I mean?

You can hack your way around that with `<div>`s and bludgeoning your layout into submission.

But that is a bit tedious.

Luckily, there's another way. As suggested by [Marius Gundersen](https://mastodon.social/@gundersen/115168958609140525), it's possible to set the [writing direction](https://developer.mozilla.org/en-US/docs/Web/CSS/writing-mode) of the element to be vertical.

That means you can have them "written" vertically, while having them laid out horizontally. Giving a nice(ish) bar-chart effect.

1000 2000 3000 4000

As well as the normal sort of CSS spacing, there is basic colour support for values which are inside a specific range:

1000 2000 3000 4000

The background colour can also be set.

1000

I dare say they're slightly more accessible than a raster image - even with good alt text. They can be targetted with JS, if you want to do fancy things with them.

Or, if you just want a quick and dirty bar-chart, they're basically fine.

* * *

Share this post on…
-------------------

*   [![Image 12: Mastodon](blob:http://localhost/fa1da30ab36ffc5a1c66c2463941d260)](https://tootpick.org/#text=Quick%20and%20dirty%20bar-charts%20using%20HTML%27s%20meter%20element%20https%3A%2F%2Fshkspr.mobi%2Fblog%2F2025%2F10%2Fquick-and-dirty-bar-charts-using-htmls-meter-element%2F)
*   [![Image 13: Facebook](blob:http://localhost/efcf4ed3a77499732e3f66a953f0a16e)](https://www.facebook.com/sharer.php?u=https%3A%2F%2Fshkspr.mobi%2Fblog%2F2025%2F10%2Fquick-and-dirty-bar-charts-using-htmls-meter-element%2F&t=Quick%20and%20dirty%20bar-charts%20using%20HTML%27s%20meter%20element)
*   [![Image 14: LinkedIn](blob:http://localhost/87e1e72529620add6a9c9cb38e3d9991)](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fshkspr.mobi%2Fblog%2F2025%2F10%2Fquick-and-dirty-bar-charts-using-htmls-meter-element%2F)
*   [![Image 15: BlueSky](blob:http://localhost/44d0beed31dd94e72f3bec5997d78f73)](https://bsky.app/intent/compose?text=Quick%20and%20dirty%20bar-charts%20using%20HTML%27s%20meter%20element%20https%3A%2F%2Fshkspr.mobi%2Fblog%2F2025%2F10%2Fquick-and-dirty-bar-charts-using-htmls-meter-element%2F)
*   [![Image 16: Threads](blob:http://localhost/84ba40141e083d143dd851e80d1e3f53)](https://www.threads.com/intent/post?url=https%3A%2F%2Fshkspr.mobi%2Fblog%2F2025%2F10%2Fquick-and-dirty-bar-charts-using-htmls-meter-element%2F&text=Quick%20and%20dirty%20bar-charts%20using%20HTML%27s%20meter%20element)
*   [![Image 17: Reddit](blob:http://localhost/3c2063ad67740fb653a57a197a750ede)](https://www.reddit.com/submit?url=https%3A%2F%2Fshkspr.mobi%2Fblog%2F2025%2F10%2Fquick-and-dirty-bar-charts-using-htmls-meter-element%2F&title=Quick%20and%20dirty%20bar-charts%20using%20HTML%27s%20meter%20element)
*   [![Image 18: HackerNews](blob:http://localhost/a75ae78b2f12bebbc6d772bed363defa)](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fshkspr.mobi%2Fblog%2F2025%2F10%2Fquick-and-dirty-bar-charts-using-htmls-meter-element%2F&t=Quick%20and%20dirty%20bar-charts%20using%20HTML%27s%20meter%20element)
*   [![Image 19: Lobsters](blob:http://localhost/9ccd488cfe94d4cfd9308e29e66b969f)](https://lobste.rs/stories/new?url=https%3A%2F%2Fshkspr.mobi%2Fblog%2F2025%2F10%2Fquick-and-dirty-bar-charts-using-htmls-meter-element%2F&title=Quick%20and%20dirty%20bar-charts%20using%20HTML%27s%20meter%20element)
*   [![Image 20: WhatsApp](blob:http://localhost/d1f7ee7453e3a1624b3ea643293a0601)](https://api.whatsapp.com/send/?text=https%3A%2F%2Fshkspr.mobi%2Fblog%2F2025%2F10%2Fquick-and-dirty-bar-charts-using-htmls-meter-element%2F)
*   [![Image 21: Telegram](blob:http://localhost/4081d83a5487986611869a54f839f4cc)](https://telegram.me/share/url?url=https%3A%2F%2Fshkspr.mobi%2Fblog%2F2025%2F10%2Fquick-and-dirty-bar-charts-using-htmls-meter-element%2F&text=Quick%20and%20dirty%20bar-charts%20using%20HTML%27s%20meter%20element)

### What are your reckons? [Cancel reply](https://shkspr.mobi/blog/2025/10/quick-and-dirty-bar-charts-using-htmls-meter-element/#respond)

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
    *   [January 17 posts](https://shkspr.mobi/blog/2025/01/)[February 20 posts](https://shkspr.mobi/blog/2025/02/)[March 23 posts](https://shkspr.mobi/blog/2025/03/)[April 22 posts](https://shkspr.mobi/blog/2025/04/)[May 16 posts](https://shkspr.mobi/blog/2025/05/)[June 28 posts](https://shkspr.mobi/blog/2025/06/)[July 24 posts](https://shkspr.mobi/blog/2025/07/)[August 20 posts](https://shkspr.mobi/blog/2025/08/)[September 15 posts](https://shkspr.mobi/blog/2025/09/)[October 6 posts](https://shkspr.mobi/blog/2025/10/)
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