Title: Examples of Great URL Design

URL Source: https://blog.jim-nielsen.com/2023/examples-of-great-urls/

Markdown Content:
Here’s Kyle Aster on why [thoughtful URL design is important (in 2010)](https://warpspire.com/posts/url-design/):

> URLs are universal. They work in Firefox, Chrome, Safari, Internet Explorer, cURL, wget, your iPhone, Android and even written down on sticky notes. They are the one universal syntax of the web. Don’t take that for granted.

I love this reminder of the ubiquity of URLs. They’re not just for typing into browser bars. They’re used in a plethora of ways:

*   As targets for scripting and scraping and other programmatic data retrieval.
*   As references, printed in the footnotes and appendixes of physical books.
*   As actionable triggers accessible via physical mediums, e.g. scannable QR codes or IoT device buttons.
*   And more!

When I reflect on examples of great URL design[[1]](https://blog.jim-nielsen.com/2023/examples-of-great-urls/#fn:1) I’ve encountered through the years — URLs that, when I saw them, I paused and thought “Wow, that’s really neat!” — these are a few that come to mind.

StackOverflow
-------------

StackOverflow was the first place I remember encountering URLs that struck a nice balance between the needs of computers and humans.

The URLs follow a pattern like this:

`/questions/:id/:slug`

`:id` is a unique identifier for the question that reveals nothing about the content. `:slug`, on the other hand, is a human-readable paraphrasing of the question that allows you to understand the question without ever actually going to the website.

The beauty is `:slug` is an optional parameter in the URL. For example:

[stackoverflow.com/questions/16245767](https://stackoverflow.com/questions/16245767)

Tells you nothing about the question being asked but it’s a valid URL that allows a server to easily find and serve that unique piece of content.

But StackOverflow also supports the `:slug` part of the URL which allows humans to quickly understand the contents living at that URL.

[stackoverflow.com/questions/16245767/creating-a-blob-from-a-base64-string-in-javascript/](https://stackoverflow.com/questions/16245767/creating-a-blob-from-a-base64-string-in-javascript/)

As noted, the `:slug` is optional. It is not required by the server to find and serve the contents in question. In fact, it can easily be changed over time without without breaking the URL (which I find quite elegant).

Granted, it can also be used deceptively. For example, this is the same URL as above but it portends completely different contents (without breaking the link):

[stackoverflow.com/questions/16245767/how-to-bake-a-cake](https://stackoverflow.com/questions/16245767/how-to-bake-a-cake)

But hey, trade-offs in everything.

Slack
-----

I remember when Slack launched a marketing campaign to educate people about the product. They used the language of the marketing campaign – [“Slack is...”](http://web.archive.org/web/20140212215308/slack.com/is) — in the page copy as well as in the URLs, e.g.

*   `slack.com/is`
*   `slack.com/is/team-communication`
*   `slack.com/is/everything-in-one-place`
*   `slack.com/is/wherever-you-are`

I remember being so intrigued at this effort to bring the design of the story-telling campaign all the way up into the URLs themselves.

Since then, I’ve always found delight in URLs that try to form natural languages sentences — `slack.com/is/team-communication` — rather than concatenate a series of hierarchical keywords — `slack.com/product/team-communication`.

Speaking of doing fun things with sentence structure in your URLs...

Jessica Hische
--------------

Jessica Hische has her website under a `.is` domain (which is [for Iceland](https://en.wikipedia.org/wiki/.is), apparently).

[jessicahische.is](https://www.jessicahische.is/)

She riffs on this fun third-person form of “I am” across her site. For example, click on “About” in the primary navigation and it takes you to:

[jessicahische.is/anoversharer](https://www.jessicahische.is/anoversharer)

That’s fun! `mydomain.com/about` is clear too, but I love the whimsy of describing the “about” and doing it in sentence structure.

All of the nouns in her primary navigation follow this pattern, as well as her individual pieces of work. Like this writeup about one of her holiday culinary packaging gigs has the URL:

[jessicahische.is/sofulloffancypopcorn](https://www.jessicahische.is/sofulloffancypopcorn)

Fun!

URLs as Product
---------------

I’ve always loved services whose URLs map nicely to their domain semantics. For example, [GitHub’s URLs map really well to git semantics](https://www.quora.com/Which-sites-have-the-best-URL-design/answer/Simon-Willison) like the three dot diff comparison in git:

`/:owner/:project/compare/ref1...ref2`

e.g.

[github.com/django/django/compare/4.2.7...main](https://github.com/django/django/compare/4.2.7...main)

For technical products, this ability to navigate a website without necessarily seeing the user interface is a cool superpower.

NPM is somewhat similar. Want to see `react-router` on NPM? You don’t have to go to NPM’s home page and click around or use their search box. Once you become familiar with their site structure, you know you can lookup a package using:

`/package/:package-name`

e.g.

[npmjs.com/package/react-router](https://www.npmjs.com/package/react-router)

Want to lookup a specific version of a package?

`/package/:package-name/v/:semver`

e.g.

[npmjs.com/package/react-router/v/5.3.4](https://www.npmjs.com/package/react-router/v/5.3.4)

These kinds of shortcuts are super useful when you’re using a particular product. In the case of NPM, you’re hunting through your `package.json` and need to lookup some details of a specific package pinned at a specific version, you can navigate to NPM’s details of that package by merely identifying the version you want and typing the details into a URL bar.

NPM CDNs [like unpkg](https://unpkg.com/) do a good job at following these semantics as well. Want a file from a published package? The homepage of unpkg says:

`unpkg.com/:package@:version/:file`

In cases like this, _the URL can be the product itself_ which makes its design all the more vital[[2]](https://blog.jim-nielsen.com/2023/examples-of-great-urls/#fn:2).

What’s Yours?
-------------

These are a few examples of URLs I’ve enjoyed using or seeing over the years. I’m sure there are others, but I’d be curious to know what your favorites are? Blog ’em!
