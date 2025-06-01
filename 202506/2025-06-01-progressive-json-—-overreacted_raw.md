Title: Progressive JSON — overreacted

URL Source: https://overreacted.io/progressive-json/

Markdown Content:
Do you know about Progressive JPEGs? Here’s a [nice explanation](https://www.liquidweb.com/blog/what-is-a-progressive-jpeg/) of what a Progressive JPEG is. The idea is that instead of loading the image top to bottom, the image instead is fuzzy at first and then progressively becomes more crisp.

What if we apply the same idea to transferring JSON?

Suppose you have a JSON tree with some data:

```
{
  header: 'Welcome to my blog',
  post: {
    content: 'This is my article',
    comments: [
      'First comment',
      'Second comment',
      // ...
    ]
  },
  footer: 'Hope you like it'
}
```

Now imagine you want to transfer it over the wire. Because the format is JSON, you’re not going to have a valid object tree until the last byte loads. You have to wait for the _entire_ thing to load, then call `JSON.parse`, and then process it.

The client can’t do _anything_ with JSON until the server sends the _last_ byte. If a part of the JSON was slow to generate on the server (e.g. loading `comments` took a slow database trip), **the client can’t _start any_ work until the server _finishes all_ the work.**

Would you call that good engineering? And yet it’s the status quo—that’s how 99.9999%* of apps send and process JSON. Do we dare to improve on that?

* I made it up

* * *

### [Streaming JSON](https://overreacted.io/progressive-json/#streaming-json)

We can try to improve this by implementing a _streaming_ JSON parser. A streaming JSON parser would be able to produce an object tree from an incomplete input:

```
{
  header: 'Welcome to my blog',
  post: {
    content: 'This is my article',
    comments: [
      'First comment',
      'Second comment'
```

If you ask for the result at this point, a streaming parser would hand you this:

```
{
  header: 'Welcome to my blog',
  post: {
    content: 'This is my article',
    comments: [
      'First comment',
      'Second comment'
      // (The rest of the comments are missing)
    ]
  }
  // (The footer property is missing)
}
```

However, this isn’t too great either.

One downside of this approach is that the objects are kind of malformed. For example, the top-level object was supposed to have three properties (`header`, `post`, and `footer`), but the `footer` is missing because it hasn’t appeared in the stream yet. The `post` was supposed to have three `comments`, but you _can’t actually tell_ whether more `comments` are coming or if this was the last one.

In a way, this is inherent to streaming—didn’t we _want_ to get incomplete data?—but **this makes it very difficult to actually _use_ this data on the client.** None of the types “match up” due to missing fields. We don’t know what’s complete and what’s not. That’s why streaming JSON isn’t popular aside from niche use cases. It’s just too hard to actually take advantage of it in the application logic which generally assumes the types are correct, “ready” means “complete”, and so on.

In the analogy with JPEG, this naïve approach to streaming matches the default “top-down” loading mechanism. The picture you see is crisp but you only see the top 10%. So despite the high fidelity, you don’t actually see _what’s_ on the picture.

Curiously, this is also how streaming _HTML itself_ works by default. If you load an HTML page on a slow connection, it will be streamed in the document order:

```
<html>
  <body>
    <header>Welcome to my blog</header>
    <article>
      <p>This is my article</p>
        <ul class="comments">
          <li>First comment</li>
          <li>Second comment</li>
```

This has some upsides—the browser is able to display the page partially—but it has the same issues. The cutoff point is arbitrary and can be visually jarring or even mess up the page layout. It’s unclear if more content is coming. Whatever’s below—like the footer—is cut off, even if it _was_ ready on the server and _could_ have been sent earlier. When we stream data _in order_, **one slow part delays _everything_.**

Let’s repeat that: when we stream things in order they appear, a _single_ slow part delays _everything_ that comes after it. Can you think of some way to fix this?

* * *

### [Progressive JSON](https://overreacted.io/progressive-json/#progressive-json)

There is another way to approach streaming.

So far we’ve been sending things _depth-first_. We start with the top-level object’s properties, we go into that object’s `post` property, then we go into _that_ object’s `comments` property, and so on. If something is slow, everything else gets held up.

However, we could also send data _breadth-first_.

Suppose we send the top-level object like this:

```
{
  header: "$1",
  post: "$2",
  footer: "$3"
}
```

Here, `"$1"`, `"$2"`, `"$3"` refer to pieces of information that _have not been sent yet_. These are placeholders that can progressively be filled in later in the stream.

For example, suppose the server sends a few more rows of data to the stream:

```
{
  header: "$1",
  post: "$2",
  footer: "$3"
}
/* $1 */
"Welcome to my blog"
/* $3 */
"Hope you like it"
```

Notice that we’re not obligated to send the rows in any particular order. In the above example, we’ve just sent both `$1` and `$3`—but the `$2` row is still pending!

If the client tried to reconstruct the tree at this point, it could look like this:

```
{
  header: "Welcome to my blog",
  post: new Promise(/* ... not yet resolved ... */),
  footer: "Hope you like it"
}
```

We’ll represent the parts that haven’t loaded yet as Promises.

Then suppose the server could stream in a few more rows:

```
{
  header: "$1",
  post: "$2",
  footer: "$3"
}
/* $1 */
"Welcome to my blog"
/* $3 */
"Hope you like it"
/* $2 */
{
  content: "$4",
  comments: "$5"
}
/* $4 */
"This is my article"
```

This would “fill in” some of the missing pieces from the client’s perspective:

```
{
  header: "Welcome to my blog",
  post: {
    content: "This is my article",
    comments: new Promise(/* ... not yet resolved ... */),
  },
  footer: "Hope you like it"
}
```

The Promise for the `post` would now resolve to an object. However, we still don’t know what’s inside the `comments`, so now _those_ are represented as a Promise.

Finally, the comments could stream in:

```
{
  header: "$1",
  post: "$2",
  footer: "$3"
}
/* $1 */
"Welcome to my blog"
/* $3 */
"Hope you like it"
/* $2 */
{
  content: "$4",
  comments: "$5"
}
/* $4 */
"This is my article"
/* $5 */
["$6", "$7", "$8"]
/* $6 */
"This is the first comment"
/* $7 */
"This is the second comment"
/* $8 */
"This is the third comment"
```

Now, from the client’s perspective, the entire tree would be complete:

```
{
  header: "Welcome to my blog",
  post: {
    content: "This is my article",
    comments: [
      "This is the first comment",
      "This is the second comment",
      "This is the third comment"
    ]
  },
  footer: "Hope you like it"
}
```

By sending data breadth-first in chunks, we gained the ability to progressively handle it on the client. As long as the client can deal with some parts being “not ready” (represented as Promises) and process the rest, this is an improvement!

* * *

### [Inlining](https://overreacted.io/progressive-json/#inlining)

Now that we have the basic mechanism, we’ll adjust it for more efficient output. Let’s have another look at the entire streaming sequence from the last example:

```
{
  header: "$1",
  post: "$2",
  footer: "$3"
}
/* $1 */
"Welcome to my blog"
/* $3 */
"Hope you like it"
/* $2 */
{
  content: "$4",
  comments: "$5"
}
/* $4 */
"This is my article"
/* $5 */
["$6", "$7", "$8"]
/* $6 */
"This is the first comment"
/* $7 */
"This is the second comment"
/* $8 */
"This is the third comment"
```

We may have gone a _little_ too far with streaming here. Unless generating some parts actually _is_ slow, we don’t gain anything from sending them as separate rows.

Suppose that we have two different slow operations: loading a post and loading a post’s comments. In that case, it would make sense to send three chunks in total.

First, we would send the outer shell:

```
{
  header: "Welcome to my blog",
  post: "$1",
  footer: "Hope you like it"
}
```

On the client, this would immediately become:

```
{
  header: "Welcome to my blog",
  post: new Promise(/* ... not yet resolved ... */),
  footer: "Hope you like it"
}
```

Then we’d send the `post` data (but without the `comments`):

```
{
  header: "Welcome to my blog",
  post: "$1",
  footer: "Hope you like it"
}
/* $1 */
{
  content: "This is my article",
  comments: "$2"
}
```

From the client’s perspective:

```
{
  header: "Welcome to my blog",
  post: {
    content: "This is my article",
    comments: new Promise(/* ... not yet resolved ... */),
  },
  footer: "Hope you like it"
}
```

Finally, we’d send the comments in a single chunk:

```
{
  header: "Welcome to my blog",
  post: "$1",
  footer: "Hope you like it"
}
/* $1 */
{
  content: "This is my article",
  comments: "$2"
}
/* $2 */
[
  "This is the first comment",
  "This is the second comment",
  "This is the third comment"
]
```

That would give us the whole tree on the client:

```
{
  header: "Welcome to my blog",
  post: {
    content: "This is my article",
    comments: [
      "This is the first comment",
      "This is the second comment",
      "This is the third comment"
    ]
  },
  footer: "Hope you like it"
}
```

This is more compact and achieves the same purpose.

In general, this format gives us leeway to decide when to send things as a single chunks vs. multiple chunks. As long as the client is resilient to chunks arriving out-of-order, the server can pick different batching and chunking heuristics.

* * *

### [Outlining](https://overreacted.io/progressive-json/#outlining)

One interesting consequence of this approach is that it _also_ gives us a natural way to reduce repetition in the output stream. If we’re serializing an object we’ve already seen before, we can just outline it as a separate row, and reuse it.

For example, suppose we have an object tree like this:

```
const userInfo = { name: 'Dan' };
 
[
  { type: 'header', user: userInfo },
  { type: 'sidebar', user: userInfo },
  { type: 'footer', user: userInfo }
]
```

If we were to serialize it to plain JSON, we’d end up repeating `{ name: 'Dan' }`:

```
[
  { type: 'header', user: { name: 'Dan' } },
  { type: 'sidebar', user: { name: 'Dan' } },
  { type: 'footer', user: { name: 'Dan' } }
]
```

However, if we’re serving JSON progressively, we could choose to outline it:

```
[
  { type: 'header', user: "$1" },
  { type: 'sidebar', user: "$1" },
  { type: 'footer', user: "$1" }
]
/* $1 */
{ name: "Dan" }
```

We could also pursue a more balanced strategy—for example, to inline objects by default (for compactness) until we see some object being used two or more times, at which point we’ll emit it separately and dedupe the rest of them in the stream.

This also means that, unlike with plain JSON, we can support serializing cyclic objects. A cyclic object just has a property that points to its own stream “row”.

* * *

### [Streaming Data vs Streaming UI](https://overreacted.io/progressive-json/#streaming-data-vs-streaming-ui)

The approach described above is essentially how React Server Components work.

Suppose you write a page with React Server Components:

```
function Page() {
  return (
    <html>
      <body>
        <header>Welcome to my blog</header>
        <Post />
        <footer>Hope you like it</footer>
      </body>
    </html>
  );
}
 
async function Post() {
  const post = await loadPost();
  return (
    <article>
      <p>{post.text}</p>
      <Comments />
    </article>
  );
}
 
async function Comments() {
  const comments = await loadComments();
  return <ul>{comments.map(c => <li key={c.id}>{c.text}</li>)}</ul>;
}
```

React will serve the output of the `Page` as a progressive JSON stream. On the client, it will be reconstructed as a progressively loaded React tree.

Initially, the React tree on the client will appear like this:

```
<html>
  <body>
    <header>Welcome to my blog</header>
    {new Promise(/* ... not resolved yet */)}
    <footer>Hope you like it</footer>
  </body>
</html>
```

Then, as `loadPost` resolves on the server, more will stream in:

```
<html>
  <body>
    <header>Welcome to my blog</header>
    <article>
      <p>This is my post</p>
      {new Promise(/* ... not resolved yet */)}
    </article>
    <footer>Hope you like it</footer>
  </body>
</html>
```

Finally, when `loadComments` resolves on the server, the client receives the rest:

```
<html>
  <body>
    <header>Welcome to my blog</header>
    <article>
      <p>This is my post</p>
      <ul>
        <li key="1">This is the first comment</li>
        <li key="2">This is the second comment</li>
        <li key="3">This is the third comment</li>
      </ul>
    </article>
    <footer>Hope you like it</footer>
  </body>
</html>
```

However, here’s the kicker.

You don’t actually _want_ the page to jump arbitrarily as the data streams in. For example, maybe you never want to show the page _without_ the post’s content.

**This is why React doesn’t display “holes” for pending Promises. Instead, it displays the closest declarative loading state, indicated by [`<Suspense>`](https://react.dev/reference/react/Suspense).**

In the above example, there are no `<Suspense>` boundaries in the tree. This means that, although React will receive the _data_ as a stream, it will not actually display a “jumping” page to the user. It will wait for the _entire_ page to be ready.

However, you can _opt into_ a progressively revealed loading state by wrapping a part of the UI tree into `<Suspense>`. This doesn’t change how the data is sent (it’s still as “streaming” as possible), but it changes _when_ React reveals it to the user.

For example:

```
import { Suspense } from 'react';
 
function Page() {
  return (
    <html>
      <body>
        <header>Welcome to my blog</header>
        <Post />
        <footer>Hope you like it</footer>
      </body>
    </html>
  );
}
 
async function Post() {
  const post = await loadPost();
  return (
    <article>
      <p>{post.text}</p>
      <Suspense fallback={<CommentsGlimmer />}>
        <Comments />
      </Suspense>
    </article>
  );
}
 
async function Comments() {
  const comments = await loadComments();
  return <ul>{comments.map(c => <li key={c.id}>{c.text}</li>)}</ul>;
}
```

Now the user will perceive the loading sequence in two stages:

*   First, the post “pops in” together with the header, the footer, and a glimmer for comments. The header and the footer never appear on their own.
*   Then, the comments “pop in” on their own.

**In other words, the stages in which the UI gets revealed are decoupled from how the data arrives. The data is streamed as it becomes available, but we only want to _reveal_ things to the user according to intentionally designed loading states.**

In a way, you can see those Promises in the React tree acting almost like a `throw`, while `<Suspense>` acts almost like a `catch`. The data arrives as fast as it can in whatever order the server is ready to send it, but React takes care to present the loading sequence gracefully and let the developer control the visual reveal.

Note that what I described so far has nothing to do with “SSR” or HTML. I was describing a general mechanism for streaming a UI tree represented as JSON. You can _turn_ that JSON tree into progressively revealed HTML (and [React can do that](https://gal.hagever.com/posts/out-of-order-streaming-from-scratch)), but the idea is broader than HTML and applies to SPA-like navigations as well.

* * *

### [In Conclusion](https://overreacted.io/progressive-json/#in-conclusion)

In this post, I’ve sketched out one of the core innovations of RSC. Instead of sending data as a single big chunk, it sends the props for your component tree outside-in. As a result, as soon as there’s an intentional loading state to display, React can do that while the rest of the data for your page is being streamed in.

I’d like to challenge more tools to adopt progressive streaming of data. If you have a situation where you can’t _start_ doing something on the client until the server _stops_ doing something, that’s a clear example of where streaming can help. If a _single slow thing_ can slow down _everything after it,_ that’s another warning sign.

Like I showed in this post, streaming _alone_ is not enough—you also need a programming model that can _take advantage_ of streaming and gracefully handle incomplete information. React solves that with intentional `<Suspense>` loading states. If you know systems that solve this differently, I’d love to hear about them!

[Pay what you like](https://ko-fi.com/gaearon)

* * *

[Discuss on Bluesky](https://bsky.app/search?q=https%3A%2F%2Foverreacted.io%2Fprogressive-json%2F)·[Edit on GitHub](https://github.com/gaearon/overreacted.io/edit/main/public/progressive-json/index.md)
