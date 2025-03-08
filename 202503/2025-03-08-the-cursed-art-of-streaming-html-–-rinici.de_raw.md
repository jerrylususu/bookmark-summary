Title: The Cursed Art of Streaming HTML – rinici.de

URL Source: https://rinici.de/posts/streaming-html

Markdown Content:
When I talk about streaming HTML, I am not talking about incrementally requesting HTML to hydrate a page, or whatever the fancy thing is web frameworks do nowadays—no, I am talking about streaming an actual HTML response, creating live updates much like a [WebSocket](https://developer.mozilla.org/docs/WebSockets) (or actually just an [SSE](https://developer.mozilla.org/docs/Server-sent_events)) does, without the need for any JavaScript.

Turns out, it's really easy to do! Basically every single web browser (even ancient ones) will request HTML with `Connection: keep-alive`, which means you get to be as slow as you want responding!

Realistically, this can be used to make sure the most important parts of the page are loaded first,[1](https://rinici.de/posts/streaming-html#fn1) while the rest is loaded later. While mostly forgotten, it's already been explored a bunch. Here, we'll be looking into a more interesting use-case: real-time applications!

Real-time chat, sans JS
-----------------------

Here's a simple webpage to get started with. We'll be embedding the magic chat endpoint into an iframe, and have a little form to send messages:

```
<!doctype html>
<html lang="en">
  <h1>hello, chat!</h1>
  <iframe src="/chat/history" frameborder="0"></iframe>
  <form method="post" action="/chat/history">
    <input id="text" name="text" placeholder="Send a message...">
  </form>
</html>
```

Well... this doesn't actually work as intended, because sending a message causes the page to reload. Does anyone even still use no-JS forms? It's such a pain. Anyways, we could avoid reloading the page by setting a `target`, but lets go a step further and make the chatbox another iframe:

`index.html`:

```
<iframe src="/chat/history" frameborder="0"></iframe> <hr>
<iframe src="/chat" frameborder="0"></iframe>
```

`chat.html`:

```
<form method="post" action="/chat/history">
  <input id="text" name="text" placeholder="Send a message...">
</form>
```

This has the cursed bonus of automatically clearing the form, and now you wont lose chat history!

So, how do we stream HTML? It's no magic, it works exactly how you'd implement [SSEs](https://developer.mozilla.org/docs/Server-sent_events) or [WebSockets](https://developer.mozilla.org/docs/WebSockets). In Node frameworks, it's [`res.write()`](https://nodejs.org/api/http.html#responsewritechunk-encoding-callback), in Sinatra, it's [`stream`](https://sinatrarb.com/intro.html#streaming-responses), in Actix, it's [`HttpResponse::streaming()`](https://actix.rs/docs/handlers#streaming-response-body), etc etc.

Here, we'll be using [Express](http://expressjs.com/), simply because it's probably the most universally known framework. I actually have this website in Haskell, which if you're in to read some unholy code you can do so [here](https://github.com/rniii/rinici.de). We'll also use an [`EventEmitter`](https://nodejs.org/api/events.html) to send messages to clients. In a better language, this would be a proper broadcast channel, but oh well.

```
const chat = new EventEmitter()

app.get("/chat/history", (req, res) => {
  res.set("Content-Type", "text/html")
  res.write("<!doctype html>")
  res.write("<meta charset=utf-8>")
  res.write("<body><ul>")

  chat.on("message", (text) => {
    res.write("<li>" + text)
  })
})
```

That's a resource leak. Okay, let's try:

```
app.get("/chat/history", (req, res) => {
  // ...

  const listen = (text) => res.write("<li>" + text)

  chat.on("message", listen)
  res.on("close", () => chat.off("message", listen))
})
```

How to avoid XSS is left as an excercise for the reader. Now, to receive messages:

```
app.use(express.urlencoded({ extended: true }))

app.post("/chat/history", (req, res) => {
  chat.emit("message", req.body.text)
  res.redirect("/chat#text")
})
```

And there's another neat trick: by redirecting to `/chat#text`, the textbox is automatically focused. Add cache and you can't even tell the thing is an iframe!

Conclusion
----------

> _Oh my god the page doesn't finish loading_

If you actually try this code now, you'll see the page just... doesn't finish loading. Probably because we don't actually close it. So, uh, I actually don't know how to fix this for now, if you do figure it out, shoot me a DM or email!

*   `loading="lazy"`. In theory should delay loading of the iframe, making it not count into page load, but doesn't do anything, and wouldn't work with JS disabled.

My solution for now is to have a short snippet to trick the browser into loading the page. Sadly, this means a little JS is necessary. But hey, it's actually fully functional without it, yay for progressive-enhancement!

```
<script>
chat.src = ""
setTimeout(() => chat.src = "/chat/history", 300)
</script>
```

* * *

1.  As does eBay! [Async Fragments: Rediscovering Progressive HTML Rendering with Marko](https://innovation.ebayinc.com/tech/engineering/async-fragments-rediscovering-progressive-html-rendering-with-marko).[↩︎](https://rinici.de/posts/streaming-html#fnref1)
