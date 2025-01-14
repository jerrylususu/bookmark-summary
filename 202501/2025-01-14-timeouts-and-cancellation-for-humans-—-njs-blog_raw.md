Title: Timeouts and cancellation for humans — njs blog

URL Source: https://vorpus.org/blog/timeouts-and-cancellation-for-humans/

Markdown Content:
_Your_ code might be perfect and never fail, but unfortunately the outside world is less reliable. Sometimes, other people's programs crash or freeze. Networks go down; printers [catch on fire](https://en.wikipedia.org/wiki/Lp0_on_fire). Your code needs to be prepared for this: every time you read from the network, attempt to acquire an inter-process lock, or send an HTTP request, there are at least three possibilities you need to think about:

*   It might succeed.
*   It might fail
*   It might hang forever, never succeeding or failing: days pass, leaves fall, winter comes, yet still our request waits, yearning for a response that will never come.

The first two are straightforward enough. To handle that last case, though, you need timeouts. Pretty much every place your program interacts with another program or person or system, it needs a timeout, and if you don't have one, that's a latent bug.

Let's be honest: if you're like most developers, your code probably has _tons_ of bugs caused by missing timeouts. Mine certainly does. And it's weird – since this need is so ubiqituous, and so fundamental to doing I/O correctly, you'd think that every programming environment would provide easy and robust ways to apply timeouts to arbitrary operations. But... they don't. In fact, most timeout APIs are so tedious and error-prone that it's just not practical for developers to reliably get this right. So don't feel bad – it's not your fault your code has all those timeout bugs, it's the fault of those I/O libraries!

But now I'm, uh, [writing an I/O library](https://trio.readthedocs.io/). And not just any I/O library, but one whose whole selling point is that it's obsessed with being easy to use. So I wanted to make sure that in my library – Trio – you can easily and reliably apply timeouts to arbitrary I/O operations. But designing a user-friendly timeout API is a surprisingly tricky task, so in this blog post I'm going to do a deep dive into the landscape of possible designs – and in particular the many precursors that inspired me – and then explain what I came up with, and why I think it's a real improvement on the old state-of-the-art. And finally, I'll discuss how Trio's ideas could be applied more broadly, and in particular, I'll demonstrate a prototype implementation for good old synchronous Python.

So – what's so hard about timeout handling?

**Contents:**

*   [Simple timeouts don't support abstraction](https://vorpus.org/blog/timeouts-and-cancellation-for-humans/#simple-timeouts-don-t-support-abstraction)
*   [Absolute deadlines are composable (but kinda annoying to use)](https://vorpus.org/blog/timeouts-and-cancellation-for-humans/#absolute-deadlines-are-composable-but-kinda-annoying-to-use)
*   [Cancel tokens](https://vorpus.org/blog/timeouts-and-cancellation-for-humans/#cancel-tokens)
    *   [Cancel tokens encapsulate cancellation state](https://vorpus.org/blog/timeouts-and-cancellation-for-humans/#cancel-tokens-encapsulate-cancellation-state)
    *   [Cancel tokens are level-triggered and can be scoped to match your program's needs](https://vorpus.org/blog/timeouts-and-cancellation-for-humans/#cancel-tokens-are-level-triggered-and-can-be-scoped-to-match-your-program-s-needs)
    *   [Cancel tokens are unreliable in practice because humans are lazy](https://vorpus.org/blog/timeouts-and-cancellation-for-humans/#cancel-tokens-are-unreliable-in-practice-because-humans-are-lazy)
*   [Cancel scopes: Trio's human-friendly solution for timeouts and cancellation](https://vorpus.org/blog/timeouts-and-cancellation-for-humans/#cancel-scopes-trio-s-human-friendly-solution-for-timeouts-and-cancellation)
    *   [How cancel scopes work](https://vorpus.org/blog/timeouts-and-cancellation-for-humans/#how-cancel-scopes-work)
    *   [Where do we check for cancellation?](https://vorpus.org/blog/timeouts-and-cancellation-for-humans/#where-do-we-check-for-cancellation)
    *   [An escape hatch](https://vorpus.org/blog/timeouts-and-cancellation-for-humans/#an-escape-hatch)
    *   [Cancel scopes and concurrency](https://vorpus.org/blog/timeouts-and-cancellation-for-humans/#cancel-scopes-and-concurrency)
    *   [Summary](https://vorpus.org/blog/timeouts-and-cancellation-for-humans/#summary)
*   [Who else can benefit from cancel scopes?](https://vorpus.org/blog/timeouts-and-cancellation-for-humans/#who-else-can-benefit-from-cancel-scopes)
    *   [Synchronous, single-threaded Python](https://vorpus.org/blog/timeouts-and-cancellation-for-humans/#synchronous-single-threaded-python)
    *   [asyncio](https://vorpus.org/blog/timeouts-and-cancellation-for-humans/#asyncio)
    *   [Other languages](https://vorpus.org/blog/timeouts-and-cancellation-for-humans/#other-languages)
*   [Now go forth and fix your timeout bugs!](https://vorpus.org/blog/timeouts-and-cancellation-for-humans/#now-go-forth-and-fix-your-timeout-bugs)
*   [Comments](https://vorpus.org/blog/timeouts-and-cancellation-for-humans/#comments)

[Simple timeouts don't support abstraction](https://vorpus.org/blog/timeouts-and-cancellation-for-humans/#id11)
---------------------------------------------------------------------------------------------------------------

The simplest and most obvious way to handle timeouts is to go through each potentially-blocking function in your API, and give it a timeout argument. In the Python standard library you'll see this in APIs like threading.Lock.acquire:

lock = threading.Lock()

# Wait at most 10 seconds for the lock to become available
lock.acquire(timeout=10)

If you use the socket module for networking, it works the same way, except that the timeout is set on the socket object instead of passed to every call:

sock = socket.socket()

# Set the timeout once
sock.settimeout(10)
# Wait at most 10 seconds to establish a connection to the remote host
sock.connect(...)
# Wait at most 10 seconds for data to arrive from the remote host
sock.recv(...)

This is a little more convenient than having to remember to pass in explicit timeouts every time (and we'll discuss the convenience issue more below) but it's important to understand that this is a purely cosmetic change. The semantics are the same as we saw with threading.Lock: each method call gets its own separate 10 second timeout.

So what's wrong with this? It seems straightforward enough. And if we always wrote code directly against these low level APIs, then it would probably be sufficient. But – programming is about abstraction. Say we want to fetch a file from [S3](https://en.wikipedia.org/wiki/Amazon_S3). We might do that with boto3, using [S3.Client.get\_object](https://botocore.readthedocs.io/en/latest/reference/services/s3.html#S3.Client.get_object). What does S3.Client.get\_object do? It makes a series of HTTP requests to the S3 servers, by calling into the [requests](http://python-requests.org/) library for each one. And then each call to requests internally makes a series of calls to the socket module to do the actual network communication [\[1\]](https://vorpus.org/blog/timeouts-and-cancellation-for-humans/#id6).

From the user's point of view, these are three different APIs that fetch data from a remote service:

s3client.get\_object(...)
requests.get("https://...")
sock.recv(...)

Sure, they're at different levels of abstraction, but the whole idea of abstracting away such details is that the user doesn't have to care. So if our plan is to use timeout= arguments everywhere, then we should expect these each to take a timeout= argument:

s3client.get\_object(..., timeout\=10)
requests.get("https://...", timeout\=10)
sock.recv(..., timeout\=10)

Now here's the problem: if this is how we're doing things, then actually implementing these functions is a pain in the butt. Why? Well, let's take a simplified example. When processing HTTP response, there comes a point when we've seen the Content-Length header, and now we need to read that many bytes to fetch the actual response body. So somewhere inside requests there's a loop like:

def read\_body(sock, content\_length):
    body \= bytearray()
    while len(body) < content\_length:
        max\_to\_receive \= content\_length \- len(body)
        body += sock.recv(max\_to\_receive)
    assert len(body) \== content\_length
    return body

Now we'll modify this loop to add timeout support. We want to be able to say "I'm willing to wait at most 10 seconds to read the response body". But we can't just pass the timeout argument through to recv, because imagine the first call to recv takes 6 seconds – now for our overall operation to complete in 10 seconds, our second recv call has to be given a timeout of 4 seconds. With the timeout= approach, every time we pass between levels of abstraction we need to write some annoying gunk to recalculate timeouts:

def read\_body(sock, content\_length, timeout):
    read\_body\_deadline \= timeout + time.monotonic()    body \= bytearray()
    while len(body) < content\_length:
        max\_to\_receive \= content\_length \- len(body)
        recv\_timeout \= read\_body\_deadline \- time.monotonic()        body += sock.recv(max\_to\_receive, timeout\=recv\_timeout)    assert len(body) \== content\_length
    return body

(And even this is actually simplified because we're pretending that sock.recv takes a timeout argument – if you wanted to this for real you'd have to call settimeout before every socket method, and then probably use some try/finally thing to set it back or else risk confusing some other part of your program.)

In practice, nobody does this – all the higher-level Python libraries I know of that take timeout= arguments, just pass them through unchanged to the lower layers. And this breaks abstraction. For example, here are two popular Python APIs you might use today, and they look like they take similar timeout= arguments:

import threading
lock \= threading.Lock()
lock.acquire(timeout\=10)

import requests
requests.get("https://...", timeout\=10)

But in fact these two timeout= arguments mean totally different things. The first one means "try to acquire the lock, but give up after 10 seconds". The second one means "try to fetch the given URL, but give up if at any point any individual low-level socket operation takes more than 10 seconds". Probably the whole reason you're using requests is that you don't want to think about low-level sockets, but sorry, you have to anyway. In fact it is currently **not possible** to guarantee that requests.get will return in **any** finite time: if a malicious or misbehaving server sends at least 1 byte every 10 seconds, then our requests call above will keep resetting its timeout over and over and never return.

I don't mean to pick on requests here – this problem is everywhere in Python APIs. I'm using requests as the example because Kenneth Reitz is famous for his obsession with making its API as obvious and intuitive as possible, and this is one of the rare places where he's failed. I think this is the only part of the requests API that gets a [big box in the documentation warning you that it's counterintuitive](http://docs.python-requests.org/en/master/user/quickstart/#timeouts). So like... if even Kenneth Reitz can't get this right, I think we can conclude that "just slap a timeout= argument on it" does not lead to APIs fit for human consumption.

[Absolute deadlines are composable (but kinda annoying to use)](https://vorpus.org/blog/timeouts-and-cancellation-for-humans/#id12)
-----------------------------------------------------------------------------------------------------------------------------------

If timeout= arguments don't work, what can we do instead? Well, here's one option that some people advocate. Notice how in our read\_body example above, we converted the incoming relative timeout ("10 seconds from the moment I called this function") into an absolute deadline ("when the clock reads 12:01:34.851"), and then converted back before each socket call. This code would get simpler if we wrote the whole API in terms of deadline= arguments, instead of timeout= arguments. This makes things simple for library implementors, because you can just pass the deadline down your abstraction stack:

def read\_body(sock, content\_length, deadline):
    body \= bytearray()
    while len(body) < content\_length:
        max\_to\_receive \= content\_length \- len(body)
        body += sock.recv(max\_to\_receive, deadline\=deadline)
    assert len(body) \== content\_length
    return body

 \# Wait 10 seconds total for the response body to be downloaded
 deadline \= time.monotonic() + 10
 read\_body(sock, content\_length, deadline)

(A well-known API that works like this is [Go's socket layer](https://golang.org/pkg/net/#Conn).)

But this approach also has a downside: it succeeds in moving the annoying bit out of the library internals, and and instead puts it on the person using the API. At the outermost level where timeout policy is being set, your library's users probably want to say something like "give up after 10 seconds", and if all you take is a deadline= argument then they have to do the conversion by hand every time. Or you could have every function take both timeout= and deadline= arguments, but then you need some boilerplate in every function to normalize them, raise an error if both are specified, and so forth. Deadlines are an improvement over raw timeouts, but it feels like there's still some missing abstraction here.

[Cancel tokens](https://vorpus.org/blog/timeouts-and-cancellation-for-humans/#id13)
-----------------------------------------------------------------------------------

### [Cancel tokens encapsulate cancellation state](https://vorpus.org/blog/timeouts-and-cancellation-for-humans/#id14)

Here's the missing abstraction: instead of supporting two different arguments:

\# What users do:
requests.get(..., timeout\=...)
\# What libraries do:
requests.get(..., deadline\=...)
\# How we implement it:
def get(..., deadline\=None, timeout\=None):
    deadline \= normalize\_deadline(deadline, timeout)
    ...

we can encapsulate the timeout expiration information into an object with a convenience constructor:

class Deadline:
    def \_\_init\_\_(self, deadline):
        self.deadline \= deadline

def after(timeout):
    return Deadline(time.monotonic() + timeout)

\# Wait 10 seconds total for the URL to be fetched
requests.get("https://...", deadline\=after(10))

That looks nice and natural for users, but since it uses an absolute deadline internally, it's easy for library implementors too.

And once we've gone this far, we might as well make things a bit more abstract. After all, a timeout isn't the only reason you might want to give up on some blocking operation; "give up after 10 seconds have passed" is a special case of "give up after <some arbitrary condition becomes true\>". If you were using requests to implement a web browser, you'd want to be able to say "start fetching this URL, but give up when the 'stop' button gets pressed". And libraries mostly treat this Deadline object as totally opaque in any case – they just pass it through to lower-level calls, and trust that eventually some low-level primitives will interpret it appropriately. So instead of thinking of this object as encapsulating a deadline, we can start thinking of it as encapsulating an arbitrary "should we give up now" check. And in honor of its more abstract nature, instead of calling it a Deadline let's call this new thing a CancelToken:

\# This library is only hypothetical, sorry
from cancel\_tokens import cancel\_after, cancel\_on\_callback

\# Returns an opaque CancelToken object that enters the "cancelled"
\# state after 10 seconds.
cancel\_token \= cancel\_after(10)
\# So this request gives up after 10 seconds
requests.get("https://...", cancel\_token\=cancel\_token)

\# Returns an opaque CancelToken object that enters the "cancelled"
\# state when the given callback is called.
cancel\_callback, cancel\_token \= cancel\_on\_callback()
\# Arrange for the callback to be called if someone clicks "stop"
stop\_button.on\_press \= cancel\_callback
\# So this request gives up if someone clicks 'stop'
requests.get("https://...", cancel\_token\=cancel\_token)

So promoting the cancellation condition to a first-class object makes our timeout API easier to use, and _at the same time_ makes it dramatically more powerful: now we can handle not just timeouts, but also arbitrary cancellations, which is a very common requirement when writing concurrent code. (For example, it lets us express things like: "run these two redundant requests in parallel, and as soon as one of them finishes then cancel the other one".) This is a _great_ idea. As far as I know, it originally comes from Joe Duffy's [cancellation tokens](https://blogs.msdn.microsoft.com/pfxteam/2009/05/22/net-4-cancellation-framework/) work in C#, and Go [context objects](https://golang.org/pkg/context/) are essentially the same idea. Those folks are pretty smart! In fact, cancel tokens also solve some other problems that show up in traditional cancellation systems.

### [Cancel tokens are level-triggered and can be scoped to match your program's needs](https://vorpus.org/blog/timeouts-and-cancellation-for-humans/#id15)

In our little tour of timeout and cancellation APIs, we started with timeouts. If you start with cancellation instead, then there's another common pattern you'll see in lots of systems: a method that lets you cancel a single thread (or task, or whatever your framework uses as a thread-equivalent), by waking it up and throwing in some kind of exception. Examples include asyncio's [Task.cancel](https://docs.python.org/3/library/asyncio-task.html#asyncio.Task.cancel), Curio's [Task.cancel](https://curio.readthedocs.io/en/latest/reference.html#Task.cancel), pthread cancellation, Java's [Thread.interrupt](https://docs.oracle.com/javase/8/docs/api/java/lang/Thread.html#interrupt--), C#'s [Thread.Interrupt](https://msdn.microsoft.com/en-us/library/system.threading.thread.interrupt(v=vs.110).aspx), and so forth. In their honor, I'll call this the "thread interrupt" approach to cancellation.

In the thread-interrupt approach, cancellation is a point-in-time _event_ that's directed at a _fixed-size entity_: one call → one exception in one thread/task. There are two issues here.

The problem with scale is fairly obvious: if you have a single function you'd like to call normally _but_ you might need to cancel it, then you have to spawn a new thread/task/whatever just for that:

http\_thread = spawn\_new\_thread(requests.get, "https://...")
# Arrange that http\_thread.interrupt() will be called if someone
# clicks the stop button
stop\_button.on\_click = http\_thread.interrupt
try:
    http\_response = http\_thread.wait\_for\_result()
except Interrupted:
    ...

Here the thread isn't being used for concurrency; it's just an awkward way of letting you delimit the scope of the cancellation.

Or, what if you have a big complicated piece of work that you want to cancel – for example, something that internally spawns multiple worker threads? In our example above, if requests.get spawned some additional backgrounds threads, they might be left hanging when we cancel the first thread. Handling this correctly would require some complex and delicate bookkeeping.

Cancel tokens solve this problem: the work they cancel is "whatever the token was passed into", which could be a single function, or a complex multi-tiered set of thread pools, or anything in between.

The other problem with the thread-interrupt approach is more subtle: it treats cancellation as an _event_. Cancel tokens, on the other hand, model cancellation as a _state_: they start out in the uncancelled state, and eventually transition into the cancelled state.

This is subtle, but it makes cancel tokens less error-prone. One way to think of this is the [edge-triggered/level-triggered distinction](https://lwn.net/Articles/25137/): thread-interrupt APIs provide edge-triggered notification of cancellations, as compared to level-triggered for cancel tokens. Edge-triggered APIs are notoriously tricky to use. You can see an example of this in Python's [threading.Event](https://docs.python.org/3/library/threading.html#threading.Event): even though it's called "event", it actually has an internal boolean state; cancelling a cancel token is like setting an Event.

That's all pretty abstract. Let's make it more concrete. Consider the common pattern of using a try/finally to make sure that a connection is shut down properly. Here's a rather artificial example of a function that makes a Websocket connection, sends a message, and then makes sure to close it, regardless of whether send\_message raises an exception: [\[2\]](https://vorpus.org/blog/timeouts-and-cancellation-for-humans/#id7)

def send\_websocket\_messages(url, messages):
    open\_websocket\_connection(url)
    try:
        for message in messages:
            ws.send\_message(message)
    finally:
        ws.close()

Now suppose we start this function running, but at some point the other side drops off the network and our send\_message call hangs forever. Eventually, we get tired of waiting, and cancel it.

With a thread-interrupt style edge-triggered API, this causes the send\_message call to immediately raise an exception, and then our connection cleanup code automatically runs. So far so good. But here's an interesting fact about the websocket protocol: it has [a "close" message](https://tools.ietf.org/html/rfc6455#section-5.5.1) you're supposed to send before closing the connection. In general this is a good thing; it allows for cleaner shutdowns. So when we call ws.close(), it'll try to send this message. But... in this case, the reason we're trying to close the connection is because we've given up on the other side accepting any new messages. So now ws.close() also hangs forever.

If we used a cancel token, this doesn't happen:

def send\_websocket\_messages(url, messages, cancel\_token):
    open\_websocket\_connection(url, cancel\_token\=cancel\_token)
    try:
        for message in messages:
            ws.send\_message(message, cancel\_token\=cancel\_token)
    finally:
        ws.close(cancel\_token\=cancel\_token)

Once the cancel token is triggered, then _all_ future operations on that token are cancelled, so the call to ws.close doesn't get stuck. It's a less error-prone paradigm.

It's kind of interesting how so many older APIs could get this wrong. If you follow the path we did in this blog post, and start by thinking about applying a timeout to a complex operation composed out of multiple blocking calls, then it's obvious that if the first call uses up the whole timeout budget, then any future calls should fail immediately. Timeouts are naturally level-triggered. And then when we generalize from timeouts to arbitrary cancellations, the insight carries over. But if you only think about timeouts for primitive operations then this never arises; or if you start with a generic cancellation API and then use it to implement timeouts (like e.g. Twisted and asyncio do), then the advantages of level-triggered cancellation are easy to miss.

### [Cancel tokens are unreliable in practice because humans are lazy](https://vorpus.org/blog/timeouts-and-cancellation-for-humans/#id16)

So cancel tokens have really great semantics, and are certainly better than raw timeouts or deadlines, but they still have a usability problem: to write a function that supports cancellation, you have to accept this boilerplate argument and then make sure to pass it on to every subroutine you call. And remember, a correct and robust program has to support cancellation in _every function that ever does I/O, anywhere in your stack_. If you ever get lazy and leave it out, or just forget to pass it through to any particular subroutine call, then you have a latent bug.

Humans suck at this kind of boilerplate. I mean, not you, I'm sure you're a very diligent programmer who makes sure to implement correct cancellation support in every function and also flosses every day. But... perhaps some of your co-workers are not so diligent? Or maybe you depend on some library that someone else wrote – how much do you trust your third-party vendors to get this right? As the size of your stack grows then the chance that everyone everywhere always gets this right approaches zero.

Can I back that up with any real examples? Well, consider this: in both C# and Go, the most prominent languages that use this approach and have been advocating it for a number of years, the underlying networking primitives _still do not have cancel token support_ [\[3\]](https://vorpus.org/blog/timeouts-and-cancellation-for-humans/#id8). These are like... THE fundamental operations that might hang for reasons outside your control and that you need to be prepared to time out or cancel, but... I guess they just haven't gotten around to implementing it yet? Instead their socket layers support an older mechanism for setting [timeouts](https://msdn.microsoft.com/en-us/library/system.net.sockets.socket.receivetimeout(v=vs.110).aspx) or [deadlines](https://golang.org/pkg/net/#IPConn.SetDeadline) on their socket objects, and if you want to use cancel tokens you have to figure out how to bridge between the two different systems yourself.

The Go standard library does provide one example of how to do this: their function for establishing a network connection (basically the equivalent of Python's socket.connect) does accept a cancel token. Implementing this requires [40 lines of source code](https://github.com/golang/go/blob/bf0f69220255941196c684f235727fd6dc747b5c/src/net/fd_unix.go#L99-L141), a background task, and the first try [had a race condition that took a year to be discovered in production](https://github.com/golang/go/issues/16523). So... in Go if you want to use cancel tokens (or Contexts, in Go parlance), then I guess that's what you need to implement every time you use any socket operation? Good luck?

I don't mean to make fun. This stuff is hard. But C# and Go are huge projects maintained by teams of highly-skilled full-time developers and backed by Fortune 50 companies. If they can't get it right, who can? Not me. I'm one human trying to reinvent I/O in Python. I can't afford to make things that complicated.

[Cancel scopes: Trio's human-friendly solution for timeouts and cancellation](https://vorpus.org/blog/timeouts-and-cancellation-for-humans/#id17)
-------------------------------------------------------------------------------------------------------------------------------------------------

Remember way back at the beginning of this post, we noted that Python socket methods don't take individual timeout arguments, but instead let you set the timeout once on the socket so it's implicitly passed to every method you call? And in the section just above, we noticed that C# and Go do pretty much the same thing? I think they're on to something. Maybe we should accept that when you have some data that has to be passed through to every function you call, that's something the computer should handle, rather than making flaky humans do the work – but in a general way that supports complex abstractions, not just sockets.

### [How cancel scopes work](https://vorpus.org/blog/timeouts-and-cancellation-for-humans/#id18)

Here's how you impose a 10 second timeout on an HTTP request in Trio:

\# The primitive API:
with trio.open\_cancel\_scope() as cancel\_scope:
    cancel\_scope.deadline \= trio.current\_time() + 10
    await request.get("https://...")

Of course normally you'd use a [convenience wrapper](https://trio.readthedocs.io/en/latest/reference-core.html#trio.move_on_after), like:

\# An equivalent but more idiomatic formulation:
with trio.move\_on\_after(10):
    await requests.get("https://...")

But since this post is about the underlying design, we'll focus on the primitive version. (Credit: the idea of using with blocks for timeouts is something I first saw in Dave Beazley's Curio, though I changed a bunch. I'll hide the details in a footnote: [\[4\]](https://vorpus.org/blog/timeouts-and-cancellation-for-humans/#id9).)

You should think of with open\_cancel\_scope() as creating a cancel token, but it doesn't actually expose any CancelToken object publically. Instead, the cancel token is pushed onto an invisible internal stack, and automatically applied to any blocking operations called inside the with block. So requests doesn't have to do anything to pass this through – when it eventually sends and receives data over the network, those primitive calls will automatically have the deadline applied.

The cancel\_scope object lets us control cancellation status: you can change the deadline, issue an explicit cancellation by calling cancel\_scope.cancel(), and [so forth](https://trio.readthedocs.io/en/latest/reference-core.html#trio.The%20cancel%20scope%20interface). If you know C#, it's analogous to a [CancellationTokenSource](https://msdn.microsoft.com/en-us/library/system.threading.cancellationtokensource(v=vs.110).aspx). One useful trick it allows is implementing the kind [raise-an-error-if-the-timeout-fires API that people are used to](https://github.com/python-trio/trio/blob/07d144e701ae8ad46d393f6ca1d1294ea8fc2012/trio/_timeouts.py#L96-L118), on top of the more primitive cancel scope unwinding semantics.

When an operation is cancelled, it raises a Cancelled exception, which is used to unwind the stack back out to the appropriate with open\_cancel\_scope block. Cancel scopes can be nested; Cancelled exceptions know which scope triggered them, and will keep propagating until they reach the corresponding with block. (As a consequence, you should always let the Trio runtime take care of raising and catching Cancelled exceptions, so that it can properly keep track of these relationships.)

Supporting nesting is important because some operations may want to use timeouts internally as an implementation detail. For example, when you ask Trio to make a TCP connection to a hostname that has multiple IP addresses associated with it, it uses a "happy eyeballs" algorithm to [run multiple connections attempts in parallel with a staggered start](https://trio.readthedocs.io/en/latest/reference-io.html#trio.open_tcp_stream). This requires an [internal timeout](https://github.com/python-trio/trio/blob/d063d672de15edc231b14c0a9bc3673e5275a9dc/trio/_highlevel_open_tcp_stream.py#L260-L265) to decide when it's time to initiate the next connection attempt. But users shouldn't have to care about that! If you want to say "try to connect to example.com:443, but give up after 10 seconds", then that's just:

with trio.move\_on\_after(10):
    tcp\_stream \= await trio.open\_tcp\_stream("example.com", 443)

And everything works; thanks to the cancel scope nesting rules, it turns out open\_tcp\_stream handles this correctly with no additional code.

### [Where do we check for cancellation?](https://vorpus.org/blog/timeouts-and-cancellation-for-humans/#id19)

Writing code that's correct in the face of cancellation can be tricky. If a Cancelled exception were to suddenly materialize in a place the user wasn't prepared for it – perhaps when their code was half-way through manipulating some delicate data structure – it could corrupt internal state and cause hard-to-track-down bugs. On the other hand, a timeout and cancellation system doesn't do much good if you don't notice cancellations relatively promptly. So an important challenge for any system is to first pick a "goldilocks rule" that checks often enough, but not too often, and then somehow communicate this rule to users so that they can make sure their code is prepared.

In Trio's case, this is pretty straightforward. We already, for other reasons, use Python's async/await syntax to annotate blocking functions. The main thing does is let you look at the text of any function and immediately see which points might block waiting for something to happen. Example:

async def user\_defined\_function():
    print("Hello!")
    await trio.sleep(1)
    print("Goodbyte!")

Here we can see that the call to trio.sleep blocks, because it has the special await keyword. You can't call trio.sleep – or any other of Trio's built-in blocking primitives – without using this keyword, because they're marked as async functions. And then Python enforces that if you want to use the await keyword, then you have to mark the calling function as async as well, which means that all _callers_ of user\_defined\_function will also