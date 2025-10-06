Title: You Want Technology With Warts

URL Source: https://entropicthoughts.com/you-want-technology-with-warts

Published Time: Tue, 16 Sep 2025 09:17:51 GMT

Markdown Content:
I normally skip presentations because I prefer reading, but [Building the Hundred-Year Web Service (YouTube)](https://www.youtube.com/watch?v=lASLZ9TgXyc) was worth the time.1 1 Note that despite “htmx” featuring in the title, very little of the presentation is actually about htmx. It is about choosing and using technology in such a way that it won’t require maintenance suddenly due to external factors changing. That’s a drum I’ve been banging for the last few years too, although less visibly.

* * *

Petros observes that we know how to build bridges that last hundreds of years: stone, concrete, and steel can all do this with the right engineering. We also know how to build hypertext that is likely to last at least a few decades: use plain html and css. But, Petros asks, how do we create database-y web services that lasts for decades?

Where do we store the data? Where do we perform business logic? He answers thusly:

*   sql ite for data storage,
*   sql queries for most of the application logic,
*   Express-on-Node.js for routing and presentation logic,
*   Jinja2 templates for additional presentation logic, and
*   html and vanilla js for triggering http requests.

I won’t debate the specifics here. 2 2 I’d be tempted to jam Perl into the backend instead of Node.js if I wanted truly low maintenance. I have a feeling a Perl script is more likely to run unmodified 20 years from now than some Node.js thing. But maybe I’m wrong on this. But there were other nuggets in the presentation. For example:

*   I’ve frequently wondered why I turn to the web browser when I want to make cross-platform software. There’s a chart in the presentation that shows how environmental churn and api deprecation leads desktop applications to have an expected lifetime of maybe a decade, and phone apps closer to a couple of years. On the other hand, simple web pages have worked unmodified for over 40 years! That’s a good reason to default to the web as a technology.
*   When a page load is fast enough, the browser does not do the whole flicker-a-blank-page-before-doing-a-full-repaint, it just shows the new content right away as a sort of partial update. This is apparently a recent browser innovation, but it is what allows e.g. [Decision Drill](https://xkqr.org/decision/) to do a full page reload when a user interacts with it, and it still feels like one of them smooth xml HttpRequest things. Rest assured, it’s a full page reload.

But then the thing that triggered this article: sql ite. One of the more powerful arguments I’ve read against sql ite is that it has a few warts in its defaults, such tables being flexibly typed, foreign keys not being enforced, primary keys being nullable, etc.

I’ve usually thought of these warts as a bad thing. Haskell has them too, like how the built in `String` type is bad data structure for storing text, and how we’re stuck with a bunch of misnamed functions (mapM, ap, msum, etc.) because we didn’t know better. Oh and the list of Perl’s warts is probably longer than its implementation.

Petros reframes this problem. Every single wart that annoys us today, used to be a reasonable feature that someone relied on in their production code. Every wart we see today is a testament to the care the maintainers put into backward compatibility. If we choose a technology today, we want one that saves us from future maintenance by keeping our wartful code running – even if we don’t yet know it is wartful. The best indicator of this is whether the technology has warts today.

> I would much rather, the first time I install an application, “enable foreign keys” – it’s just one line of config – I’d rather do that once, build the thing correctly, and then be confident that if there’s any other built-in behaviour that I didn’t account for, that behaviour isn’t going to change on me and break my application at some point in the future.

Right on.