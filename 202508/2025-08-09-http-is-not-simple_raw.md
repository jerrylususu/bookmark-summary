Title: HTTP is not simple

URL Source: https://daniel.haxx.se/blog/2025/08/08/http-is-not-simple/

Published Time: 2025-08-08T11:27:17+02:00

Markdown Content:
I often hear or see people claim that _HTTP is a simple protocol_. Primarily of course from people without much experience or familiarity with actual implementations. I think I personally also had thoughts in that style back when I started working with the protocol.

After personally having devoted soon three decades on writing client-side code doing HTTP and having been involved in the IETF on all the HTTP specs produced since 2008 or so, I think I am in a decent position to give a more expanded view on it. _HTTP is not a simple protocol._ Far from it. Even if we presume that people actually mean HTTP/1 when they say that.

HTTP/1 may appear simple because of several reasons: it is readable text, the most simple use case is not overly complicated and existing tools like curl and browsers help making HTTP easy to play with.

The HTTP _idea_ and _concept_ can perhaps still be considered simple and even somewhat ingenious, but the actual machinery is not.

But yes, you _can_ telnet to a HTTP/1 server and enter a GET / command manually and see a response. However I don’t think that is enough to qualify the entire thing as simple.

I don’t believe anyone has tried to claim that HTTP/2 or HTTP/3 are simple. In order to properly implement version two or three, you pretty much have to also implement version one so in that regard they are accumulating complexity and bring quite a lot of extra challenges in their own respective specifications.

Let me elaborate on some aspects of the HTTP/1 protocol that make me say it is not simple.

newlines
--------

HTTP is not only text-based, it is also _line-based_; the header parts of the protocol that is. A line can be arbitrarily long as there is no limit in the specs – but they need to have a limit in implementations to prevent DoS etc. How long can they be before a server rejects them? Each line ends with a carriage-return and linefeed. But in some circumstances only a linefeed is enough.

Also, headers are not UTF-8, they are octets and you must not assume that you can just arbitrarily pass through anything you like.

whitespace
----------

Text based protocols easily gets this problem. Between fields there can be one or more whitespace characters. Some of these are mandatory, some are optional. In many cases HTTP also does _tokens_ that can either be a sequence of characters without any whitespace, or it can be text within double quotes (“). In some cases they are _always_ within quotes.

end of body
-----------

There is not one single way to determine the end of a HTTP/1 download – the “body” as we say in protocol lingo. In fact, there are not even two. There are at least three (Content-Length, chunked encoding and Connection: close). Two of them require that the HTTP client parses content size provided in text format. These many end-of-body options have resulted in countless security related problems involving HTTP/1 over the years.

parsing numbers
---------------

Numbers provided as text are slow to parse and sometimes error-prone. Special care needs to be taken to avoid integer overflows, handle whitespace, +/- prefixes, leading zeroes and more. While easy to read for humans, less ideal for machines.

folding headers
---------------

As if the arbitrary length headers with unclear line endings are not enough, they can also be “folded” – in two ways. First: a proxy can _merge_ multiple headers into a single one, comma-separated – except some headers (like cookies) that cannot. Then, a server can send a header as a _continuation_ of the previous header by adding leading whitespace. This is rarely used (and discouraged in recent spec versions), but a protocol detail that an implementation needs to care about because it _is_ used.

never-implemented
-----------------

HTTP/1.1 ambitiously added features that at the time were not used or deployed onto the wide Internet so while the spec describes how for example HTTP Pipelining works, trying to use it in the wild is asking for a series of problems and is nothing but a road to sadness.

Later HTTP versions added features that better fulfilled the criteria that Pipelining failed to: mostly in the way of _multiplexing_.

The 100 response code is in similar territory: specified, but rarely actually used. It complicates life for new implementations. The fact that there is [a discussion](https://lists.w3.org/Archives/Public/ietf-http-wg/2025JulSep/0088.html)_this week_ about particulars in the 100 response state handling, twenty-eight years since it was first published in a spec I think tells something.

so many headers
---------------

The HTTP/1 spec details a lot of headers and their functionality, but that is not enough for a normal current HTTP implementation to support. This, because things like cookies, authentication, new response codes and much more that an implementation may want to support today are features outside of the main spec and are described in additional separate documents. Some details, like NTLM, are not even found in RFC documents.

Thus, a modern HTTP/1 client needs to implement and support and a whole range of additional things and headers to work fine across the web. “HTTP/1.1” is mentioned in _at least_ 40 separate RFC documents. Some of them quite complex by themselves.

not all methods are alike
-------------------------

While the syntax should ideally be possible to work exactly the same independently of which _method_ that is used (sometimes referred to as _verb_), that is not how the reality works.

For example, if the method is GET we can also indeed send a body in the request similar to how we typically do with POST and PUT, but due to how it was never properly spelled out in the past, that is not interoperable today to the extend that doing it is just recipe for failure in a high enough share of attempts across the web.

This is one of the reasons why there is now work on a new HTTP method called QUERY which is basically what GET + request body should have been. But that does not simplify the protocol.

not all headers are alike
-------------------------

Because of the organic way several headers were created, deployed and evolved, a proxy for example cannot blindly just combine two headers into one, as the generic rules say it could. Because there are headers that specifically don’t follow there rules and need to be treated differently. Like for example cookies.

spineless browsers
------------------

Remember how browser implementations of protocols always tend to prefer to show the user something and _guess_ the intention rather than showing an error because if they would be stringent and strict they risk that users would switch to another browsers that is not.

This impacts how the rest of the world gets to deal with HTTP, as users then come to expect that what works with the browsers should surely also work with non-browsers and their HTTP implementations.

This makes interpreting and understanding the spec secondary compared to just following what the major browsers have decided to do in particular circumstances. They may even change their stances over time and they may at times contradict explicit guidance in the specs.

size of the specs
-----------------

The first HTTP/1.1 RFC 2068 from January 1997 was 52,165 words in its plain text version – which almost tripled the size from the HTTP/1.0 document RFC1945 at merely 18,615. A clear indication how the _perhaps_ simple HTTP 1.0 was no longer simple anymore in 1.1.

In June 1999, the updated RFC 2616 added several hundred lines and clocked in at 57,897 words. Almost 6K more words.

A huge work was then undertaken within the IETF and in the fifteen years following the single document HTTP/1.1 spec was instead converted into _six_ separate documents.

RFC7230 to RFC7235 were published in June 2014 and they hold a total of 90,358 words. It had grown another 56%. It is comparable to an average sized novel in number of words.

The whole spec was subsequently rearranged and reorganized again to better cater for the new HTTP versions, and the latest update was published in June 2022. The HTTP/1.1 parts had then been compacted into three documents RFC 9110 to RFC9112, with a total of 95,740 words.

For the argument sake, let’s say we can read two hundred words per minute when plowing this. It is probably a little slower than average reading speed, but I imagine we read standard specs a little slower than we read novels for example. Let’s say that 10% of the words are cruft we don’t need to read.

If we read only the three latest HTTP/1.1 related RFC documents non-stop, it would still take more than seven hours.

Must die?
---------

In a recent [conference talk with this click bait title](https://http1mustdie.com/), it was suggested that HTTP/1 is so hard to get implemented right that we should all stop using it.

Necessarily so?
---------------

All this, and yet there are few other Internet protocols that can compete with HTTP/1 in terms of use, adoption and popularity. HTTP is a big shot on the internet. Maybe this level of complication has been necessary to reach this success?

Comparing with other popular protocols still in use like DNS or SMTP I think we can see similar patterns: started out as something simple a long time ago. Decades later: not so simple anymore.

Perhaps this is just life happening?

Conclusion
----------

HTTP is not a simple protocol.

The future is likely just going to be even more complicated as more things are added to HTTP over time – for all versions.