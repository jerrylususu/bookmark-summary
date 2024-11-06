Title: What's a Single-Page App? | jakelazaroff.com

URL Source: https://jakelazaroff.com/words/whats-a-single-page-app/

Markdown Content:
The web development community talks a lot about single-page apps, but are we all on a single page?

Heydon Pickering tackled this question in his similarly-named article [What Is A Single-Page Application?](https://heydonworks.com/article/what-is-a-single-page-application/)  [![Image 1](https://heydonworks.com/images/unofficial.png) What Is A Single-page Application? A quick explainer about single-page applications are what they are good for. ![Image 2](https://heydonworks.com/android-icon-192x192.png) heydonworks.com/article/what-is-a-single-page-application/](https://heydonworks.com/article/what-is-a-single-page-application/) The TL;DR — spoiler alert! — is that it’s a website that uses a ton of JavaScript to improve user experience by showing you a loading spinner.

That’s obviously tongue-in-cheek, but it’s a reaction to the working definition that most people use. For better or worse, “single-page app” is usually a euphemism for “JavaScript framework app”.

I recently wrote about [building a single-page app with htmx](https://jakelazaroff.com/words/building-a-single-page-app-with-htmx/)  [![Image 3](https://jakelazaroff.com/og/building-a-single-page-app-with-htmx.png) Building a Single-Page App with htmx | jakelazaroff.com People talk about htmx as though it's saving the web from single-page apps. Well, I guess I missed the memo, because I used htmx to build a single-page app. ![Image 4](https://jakelazaroff.com/favicon.ico) jakelazaroff.com/words/building-a-single-page-app-with-htmx/](https://jakelazaroff.com/words/building-a-single-page-app-with-htmx/) using service workers to render everything client-side — no loading spinners in sight! In response, Thomas Broyer objected to the premise that htmx and single-page apps were opposites. He showed me an article that he wrote called [Naming things is hard, SPA edition](https://blog.ltgt.net/naming-things-is-hard-spa-edition/)  [![Image 5](https://blog.ltgt.net/image/2023/03/ssr-csr.png) Naming things is hard, SPA edition What is a single-page application (SPA) exactly? How does it relate to client-side rendering (CSR)? (spoiler: SPA doesn't necessarily imply CSR.) ![Image 6](https://blog.ltgt.net/favicon.ico) blog.ltgt.net/naming-things-is-hard-spa-edition/](https://blog.ltgt.net/naming-things-is-hard-spa-edition/) (which you should also go read!) that breaks down rendering into a spectrum.

<p>Schema of SSR, ESR, SWSR and CSR, with grouping representing SSR-in-the-broader-sense (SSR and ESR) vs. BSR (SWSR and CSR), and which generate HTML (SSR, ESR and SWSR) or manipulate the DOM (CSR)</p>

The rendering spectrum, by Thomas Broyer.

In a bid to cement my burgeoning reputation as a [Quadrant Chart Guy](https://jakelazaroff.com/words/the-website-vs-web-app-dichotomy-doesnt-exist/)  [![Image 7](https://jakelazaroff.com/og/the-website-vs-web-app-dichotomy-doesnt-exist.png) The Website vs. Web App Dichotomy Doesn't Exist | jakelazaroff.com A one-dimensional spectrum can't sufficiently capture the tradeoffs involved in web development. ![Image 8](https://jakelazaroff.com/favicon.ico) jakelazaroff.com/words/the-website-vs-web-app-dichotomy-doesnt-exist/](https://jakelazaroff.com/words/the-website-vs-web-app-dichotomy-doesnt-exist/) , I feel compelled to add even _more_ nuance to the situation:

<p>A graph with two axes that intersect in the exact center, labeled SSR/CSR horizontally and SPA/MPA vertically.</p>I’m sorry. Kinda.

Okay, let’s define the extrema of each axis:

*   Server-side rendering (SSR) is when HTML is produced on a server and sent to the browser.
*   Client-side rendering (CSR) is when HTML (or some other representation, such as the result of a JSX transform) is produced on the _client_ and applied to the DOM.
*   A multi-page app (MPA) is when a hyperlink click or form submission results in the browser replacing the current page with an entirely new document.
*   A single-page app (SPA) is when the browser _never_ replaces the page with a new document, and instead makes all changes through client-side DOM manipulation.

If you just came here for an answer to the title, that’s it; I guess you can go home now. But I think it’s interesting to look at the various tools people use and how they fit in.

Most tools for building websites don’t lock you into just one quadrant. After all, _any_ tool lets you drop in a plain un-enhanced `<a>` tag and at the very least get MPA behavior, and most JavaScript usage outside of Google Tag Manager relies on client-side rendering (even if done manually).

So: without casting any aspersions, here’s my ontology of web app architectures organized by rendering and navigation.

### Traditional Web Frameworks and Static Site Generators

This is a pretty large tent, encompassing WordPress, Django, Rails (pre-Turbolinks) Jekyll, Hugo, Eleventy and myriad others. It also includes hand-authored HTML, though I wouldn’t describe that as a “tool” so much as a “way of life”.

Tools in this category are on the bottom left of the chart: server-side rendered multi-page apps.

<p>A graph with two axes that intersect in the exact center, labeled SSR/CSR horizontally and SPA/MPA vertically. A shaded region labeled “Traditional Frameworks & Static Site Generators” covers the quadrant where SSR and SPA intersect.</p>The tradeoffs of this quadrant are well known:

*   The browser takes care of a lot of important accesibility features, such as letting screen readers know when the user navigates to a new page.
*   Delivering HTML first allows the content to be visible even if CSS or JavaScript fail to load.
*   Pages can load _even faster_ if HTML is streamed in, rather than delivered all at once.
*   The full page must be downloaded and replaced on each navigation.
*   In fact, _every_ interaction requires a network round trip.

This experience has remained mostly unchanged for 30 years. And it’s great! With only a little bit of HTML and CSS, you can make a _pretty good_ website; the [many](http://motherfuckingwebsite.com/) [Motherfucking Website ![Image 9](http://motherfuckingwebsite.com/favicon.ico) motherfuckingwebsite.com](http://motherfuckingwebsite.com/) [Motherfucking](http://bettermotherfuckingwebsite.com/) [Better Motherfucking Website ![Image 10](http://bettermotherfuckingwebsite.com/favicon.ico) bettermotherfuckingwebsite.com](http://bettermotherfuckingwebsite.com/) [Website](https://evenbettermotherfucking.website/) [Even Better Motherfucking Website It's even more fucking perfect than the others motherfucking websites. ![Image 11](https://evenbettermotherfucking.website/favicon.ico) evenbettermotherfucking.website](https://evenbettermotherfucking.website/) [variations](https://perfectmotherfuckingwebsite.com/) [Perfect Motherfucking Website 🖕 And it’s really more fucking perfect than the last guy’s. ![Image 12](https://perfectmotherfuckingwebsite.com/data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxMDAgMTAwIj48dGV4dCB5PSIuOWVtIiBmb250LXNpemU9IjkwIj7wn5aVPC90ZXh0Pjwvc3ZnPgo=) perfectmotherfuckingwebsite.com](https://perfectmotherfuckingwebsite.com/) show just how far a few tags and properties get you. The low barrier to entry is one of the main reasons the web flourished.

Three decades on, improvements in HTML and CSS are starting to mitigate some of the downsides. Preloading resources, for example, allows the browser to preemptively download associated files, which can make navigation almost instantaneous. And cross-document view transitions — not yet well supported, but hopefully soon! — promise to allow multi-page apps to navigate with fancy animations.

That said: requiring a network request and a whole new page for every interaction is a pretty strong constraint! As developers’ ambitions grew, they leaned more and more heavily on JavaScript, which led to…

### JavaScript Frameworks

Although JavaScript was invented way back in 1995, I don’t think a schism truly happened until 2010 or so. That’s when the stereotypical single-page apps began to emerge: rather than using small snippets of JavaScript to add client-side functionality to server-side rendered HTML, people started building apps with a JavaScript _framework_ and rendering them on the client.

Note that I’m not talking about Next.js or similar tools (I’ll get to them in the next section). I’m talking about Backbone, Angular 1, React with a custom Webpack setup… basically, JavaScript apps before circa 2018, when people would ship an HTML file with an empty `<body>` except for one lonely `<script>` tag.

Used thusly, JavaScript frameworks are the diametric opposite of traditional web frameworks: both navigation and rendering happens on the client. As such, they fit neatly into the top right quadrant: client-side rendered single-page apps.

<p>A graph with two axes that intersect in the exact center, labeled SSR/CSR horizontally and SPA/MPA vertically. A shaded region labeled “JavaScript Frameworks” covers the quadrant where CSR and SPA intersect.</p>What are the benefits of this quadrant?

*   The initial page load can be much faster once the JavaScript bundle is cached.
*   Page navigations can be instantaneous, since all the relevant state is already on the client.
*   Elements can persist across navigations, enabling e.g. uninterrupted media playback and fancy transition animations.
*   Modifying the UI without first going through the network enables much richer client-side interactions.

In practice, I think many of the purported benefits of client-side rendered SPAs turned out to be wishful thinking:

*   When bundles are cached with a hash of the full app code, every deploy busts the cache and forces the user to download the whole bundle again.
*   Page navigations tend to wait for API responses from a server and database in the same datacenter that would have served the HTML anyway.
*   Aspirations of being richly interactive are often fantasy; most websites are really just gussied up forms.

There are also more general drawbacks:

*   The client needs to download 100% of the UI code.
*   The initial page load (before the JavScript bundle is cached) will always be slower.
*   Page navigations are not accessible by default.
*   It’s way more difficult for apps here to be indexed by search engines.

If I sound critical of this category, it’s only because the industry has largely recognized these drawbacks and moved on to other architectures. While JavaScript frameworks are more popular than ever, they tend to exist as components of larger systems rather than than as app frameworks in and of themselves.

Client-side rendered SPAs still have their uses, though. When I made [my local-first trip planning app](https://jakelazaroff.com/words/a-local-first-case-study/)  [![Image 13](https://jakelazaroff.com/og/a-local-first-case-study.png) A Local-First Case Study | jakelazaroff.com How I built a local-first app for planning trips, and what I learned about the current state of the local-first ecosystem along the way. ![Image 14](https://jakelazaroff.com/favicon.ico) jakelazaroff.com/words/a-local-first-case-study/](https://jakelazaroff.com/words/a-local-first-case-study/) , I built it as a client-side rendered SPA. There was really no other way to build it — since the client has the canonical copy of the data, there’s not even a server to do any rendering! As local-first picks up steam, I hope and expect to see this architecture make a resurgence in a way that _does_ capture the upside of the quadrant’s tradeoffs.

### JavaScript Metaframeworks

JavaScript frameworks had about half a decade of client-side rendering glory before people realized that delivering entire applications that way was bad for performance. To address that, developers starting building _meta_frameworks[1](https://jakelazaroff.com/words/whats-a-single-page-app/#user-content-fn-metaframeworks) — Next.js, Remix, SvelteKit, Nuxt and Solid Start, among others — that rendered on the server as well.

In metaframeworks, rendering happens in two different ways:

1.  When the user requests a page, the app runs on the _server_, rendering the appropriate HTML and serving it to the browser. This step is _server-side rendered_.
2.  Next, the browser requests the JavaScript bundle. That same app then runs in the _browser_, “hydrating” the already-rendered HTML and taking over any further interactions. This step is _client-side rendered_.

These steps slot neatly into the top left and top right quadrants, respectively:

<p>A graph with two axes that intersect in the exact center, labeled SSR/CSR horizontally and SPA/MPA vertically. A shaded region labeled “JavaScript Metaframeworks” covers the SPA half, covering both SSR and CSR.</p>JavaScript metaframeworks are an attempt to get the “best of both worlds” between server-side rendered multi-page apps and client-side rendered single-page apps. In particular, they fix the cold cache initial page load and SEO drawbacks of the latter. With React Server Components, React-based metaframeworks can omit UI code from the JavaScript bundle as well.[2](https://jakelazaroff.com/words/whats-a-single-page-app/#user-content-fn-rsc)

Depending on whom you ask, this is either good because it really _is_ a “best of both worlds” situation, or bad because your UI is probably useless before it hydrates with the JavaScript (that your users still need to download). But “probably” in that sentence is doing at least some amount of lifting; many metaframeworks like SvelteKit and Remix embrace progressive enhancement and work without JavaScript by default.

A couple years ago, Nolan Lawson [attempted to bridge the two camps](https://nolanlawson.com/2022/06/27/spas-theory-versus-practice/)  [![Image 15](https://nolanlawson.com/wp-content/uploads/2022/06/vlcsnap-2022-06-25-16h27m34s714-small.png?w=1200) SPAs: theory versus practice I’ve been thinking a lot recently about Single-Page Apps (SPAs) and Multi-Page Apps (MPAs). I’ve been thinking about how MPAs have improved over the years, and where SPAs still have an … ![Image 16](https://secure.gravatar.com/blavatar/86a4db4d496aa2fad7e47b11a865e80cfbbbac38285b65ff518b9c98aa47f7d7?s=32) nolanlawson.com/2022/06/27/spas-theory-versus-practice/](https://nolanlawson.com/2022/06/27/spas-theory-versus-practice/) :

> At the risk of grossly oversimplifying things, I propose that the core of the debate can be summed up by these truisms:
> 
> 1.  The best SPA is better than the best MPA.
> 2.  The average SPA is worse than the average MPA.

I think that’s a fair take, but there are a couple other architectures still remaining that make things a little blurrier.

### Islands Frameworks

Recently we’ve seen the emergence of a new category: server-side rendered multi-page frameworks that embrace [islands of interactivity](https://www.patterns.dev/vanilla/islands-architecture)  [![Image 17](https://res.cloudinary.com/ddxwdqwkr/image/upload/f_auto/v1633286240/patterns.dev/islandsarchitecture.jpg) Islands Architecture The islands architecture encourages small, focused chunks of interactivity within server-rendered web pages ![Image 18](https://www.patterns.dev/img/favicon/favicon.ico) www.patterns.dev/vanilla/islands-architecture](https://www.patterns.dev/vanilla/islands-architecture) for rich client-side behavior. While the idea itself isn’t new, the current crop of frameworks built around it are — Astro, Deno Fresh and Enhance, among others.

In case you’re unfamiliar: an island of interactivity is a region of an otherwise static HTML page that is controlled by JavaScript. It’s an acknowledgment that while richly interactive applications do exist, the richly interactive part is often surrounded by a more traditional website. The classic example is a carousel, but the pattern is broadly useful; the [interactive demos on this very blog](https://jakelazaroff.com/words/web-components-will-outlive-your-javascript-framework/)  [![Image 19](https://jakelazaroff.com/og/web-components-will-outlive-your-javascript-framework.png) Web Components Will Outlive Your JavaScript Framework | jakelazaroff.com If we're building things that we want to work in five or ten or even 20 years, we need to avoid dependencies and use the web with no layers in between. ![Image 20](https://jakelazaroff.com/favicon.ico) jakelazaroff.com/words/web-components-will-outlive-your-javascript-framework/](https://jakelazaroff.com/words/web-components-will-outlive-your-javascript-framework/) are built as islands within static HTML.

What that means in practice is that these websites will fit mostly into the bottom left quadrant — except for the namesake islands of interactivity, which fit into the bottom right.

<p>A graph with two axes that intersect in the exact center, labeled SSR/CSR horizontally and SPA/MPA vertically. A shaded region labeled “Islands Frameworks” covers the MPA half, covering both SSR and CSR.</p>Similar to JavaScript metaframeworks, islands frameworks also try to get the “best of both worlds” between client-side and server-side rendering — albeit as MPAs rather than SPAs. The bet is that reducing complexity around the static parts of a page is a better tradeoff than giving developers more control. As with traditional web frameworks, the gap between them should narrow as support for view transitions gets better.

### Partial Swapping

This pattern is less all-encompassing than some of the others, but it’s worth mentioning because the past few years have seen it explode in popularity. By “partial swapping”, I mean making an HTTP request for the server to render an HTML fragment that gets inserted directly into the page.

To wit, websites using partial swapping generally fall on the server-side rendered side of the chart, spanning both the single-page _and_ multi-page quadrants:

<p>A graph with two axes that intersect in the exact center, labeled SSR/CSR horizontally and SPA/MPA vertically. A shaded region labeled “Partial Swapping” covers the SSR half, covering both SPA and MPA.</p>The most famous partial swapping tool is htmx, which people tend to use in conjunction with “traditional” server-side rendered frameworks. Other libraries like Unpoly and Turbo work similarly. Some frameworks in other categories, such as Rails (with Turbo) and Deno Fresh, have adopted partial swapping as well.

As I’ve written before, people act as though this pattern is saving the web from SPAs. Once we widen our view like this, though, we can see that’s a false dichotomy. In fact, by making it easier for developers to replace finer-grained regions of the page, partial swapping is actually a tool for _creating SPAs_[3](https://jakelazaroff.com/words/whats-a-single-page-app/#user-content-fn-lesshtmx) — albeit server-side rendered ones.

It’s not all or nothing! The htmx documentation outlines [how this pattern can work in conjunction with client-side scripting approaches such as islands](https://htmx.org/essays/hypermedia-friendly-scripting/) [</\> htmx ~ Hypermedia-Friendly Scripting ![Image 21](https://htmx.org/favicon.ico) htmx.org/essays/hypermedia-friendly-scripting/](https://htmx.org/essays/hypermedia-friendly-scripting/) . I won’t make a chart with three of the four quadrants filled in, but you get the idea: these boundaries are fluid, and good tools don’t lock developers into a specific region.

Partial swapping can also be used as a polyfill for cross-document view transitions. Frameworks like Astro allow authors to load full pages asynchronously, progressively enhancing MPAs into server-side rendered SPAs.

### Did We Learn Anything?

None of this is particularly groundbreaking. But I agree with Thomas that imprecise terminology doesn’t help whatever discourse plays out on the hot-take-fueled Internet argument fora. Hopefully, this can serve as a reference point when we talk about when and where these architectures are appropriate.

1.  Not to be confused with Meta Frameworks, which just means React. [↩](https://jakelazaroff.com/words/whats-a-single-page-app/#user-content-fnref-metaframeworks)
    
2.  Dan Abramov gives an example of this in [The Two Reacts](https://overreacted.io/the-two-reacts/)  [![Image 22](https://github.com/gaearon.png) The Two Reacts — overreacted UI = f(data)(state) ![Image 23](https://overreacted.io/icon.png) overreacted.io/the-two-reacts/](https://overreacted.io/the-two-reacts/) . Imagine a blog with posts written in Markdown. An app fetching those posts from across the network and rendering them on the client would need to include a full Markdown parser in the JavaScript bundle. React Server Components allow the _server_ to parse the Markdown, and send only the _result_ to the client to be rendered. [↩](https://jakelazaroff.com/words/whats-a-single-page-app/#user-content-fnref-rsc)
    
3.  Of course, you don’t _have_ to use partial swapping to create a full-on SPA. In [Less htmx is More](https://unplannedobsolescence.com/blog/less-htmx-is-more/) [Less htmx is More How to build great websites with htmx by learning a couple browser features alongside it. ![Image 24](https://unplannedobsolescence.com/favicon-128.png) unplannedobsolescence.com/blog/less-htmx-is-more/](https://unplannedobsolescence.com/blog/less-htmx-is-more/) , htmx maintainer Alexander Petros advocates using it judiciously and relying on regular links and form submissions that cause the browser to do a full-page navigation (in other words, progressive enhancement). [↩](https://jakelazaroff.com/words/whats-a-single-page-app/#user-content-fnref-lesshtmx)
