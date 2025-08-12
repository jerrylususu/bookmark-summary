Title: Using GitHub Pages as a URL shortener / redirection service

URL Source: https://christianheilmann.com/2025/08/11/using-github-pages-as-a-url-shortener-redirection-service/

Markdown Content:
With the fate of Goo.gl in the balance and many URL shortening/redirection services being either expensive or spammy, I wondered if I could find a free/cheap way of achieving the same. So I got myself a short domain (CLXI.org) and looked at using a GitHub repo with pages to redirect URLs. Turns out, this is pretty straight forward.

I’ve put together all the tips here in a repository that you can fork and get started: [https://github.com/codepo8/gh-pages-urlshortener](https://github.com/codepo8/gh-pages-urlshortener)

 You can see the experience in action here – one of them: [https://codepo8.github.io/gh-pages-urlshortener/go/chris10s](https://codepo8.github.io/gh-pages-urlshortener/go/chris10s) or [https://clxi.org/go/wad](https://clxi.org/go/wad)

Redirecting on GitHub pages
---------------------------

In order to redirect any pages from a GitHub page, you need to load the right gem and set it up. You do that in your `_config.yml` file:

gems:   - jekyll-redirect-from whitelist:   - jekyll-redirect-from plugins:   - jekyll-redirect-from

If you now add a markdown file called `offwego.md` to the page and you can give it this Frontmatter to redirect it:

---
redirect_to:
  - https://christianheilmann.com
---

You can try this here: [https://clxi.org/offwego](https://clxi.org/offwego) .

However, this is a simple server redirect – like you would do on your own server. The user won’t be notified and has no chance to cancel the redirect. If that is what you want, you are done. I wanted to give people more options.

Building an own redirect with preview
-------------------------------------

Instead of creating lots of markdown files in the root folder I use a /go/ folder to store them. In GitHub pages the best way to do that is to create a collection. I created a folder called `_go` and added it to the `_config.yml` file:

collections: go: output: true

Make sure to set the `output` to `true`.

This now allows me to add lots of markdown files there. In order to make them look differently and provide more control over the redirection, I created a template file. To this end, create a `_layouts` folder and add a `redirection.html` in there. The [final template](https://github.com/codepo8/gh-pages-urlshortener/blob/main/_layouts/redirect.html) has a lot of features we don’t need to cover here, but the main trick was to make the HTTP redirection a variable both in time – the {{page.delay}} bit – and in the URL to send folks to ({{page.goto}}):

<meta http-equiv="refresh" content="{{page.delay}}; url={{page.goto}}">

That way I can now add markdown files in in the `_go` folder and define both the time and the place to redirect to in the frontmatter:

---
goto: https://christianheilmann.com
layout: redirect
delay: 10
---

I choose the `redirect` layout, the `goto` URL as mine and a delay of ten seconds.

This is as far as meta redirects get us. I also wanted to add a preview progress bar and a chance to cancel the redirect. One of the annoying bits about a meta redirect is that you can’t cancel it. HTML rules supreme and even removing it with JavaScript won’t make a difference.

Adding a chance to cancel the redirect and other fancy bits
-----------------------------------------------------------

To get more granular control, I use JavaScript instead to redirect. This could break, but it gives the user more options.

The script is no magic and I pipe in the data from the frontmatter:

let countdown = document.getElementById("countdown");
let bar = document.getElementById("progressBar");
let full = bar.max;
let delay = {{page.delay}};
let interval = setInterval(() => {
    delay--;
    countdown.textContent = delay;
    bar.value = full - delay;
    if (delay <= 0) {
        window.location.href = "{{page.goto}}";
        clearInterval(interval);
    }
}, 1000);
document.querySelector("button").addEventListener("click", () => {
    clearInterval(interval);
    document.querySelector("section").innerHTML = `
        <h1>Redirect Cancelled</h1>
        <p>You can close this page now or go to
        <a href="{{page.goto}}">{{page.goto}}</a> yourself.
        </p>`;
});

And that’s that, now you can see the place the link is going to and you can cancel if you want to. Both in dark and light mode. Here’s the progress bar in action:

![Image 1: Delayed redirection with progress bar](https://codepo8.github.io/gh-pages-urlshortener/dark.gif)

Cancelling the redirect (this time showing the light mode):

![Image 2: Cancellation experience](https://codepo8.github.io/gh-pages-urlshortener/light.gif)

Feel free to fork, add comments and improve on GitHub!