Title: Bootstrapping HTTP/1.1, HTTP/2, and HTTP/3

URL Source: https://www.netmeister.org/blog/http-123.html

Markdown Content:
May 28th, 2025

The Hypertext Transfer Protocol (HTTP) has come a long way from its humble beginnings on Tim Berners-Lee's [NeXT cube at CERN](https://en.wikipedia.org/wiki/NeXTcube#/media/File:NeXTcube_first_webserver.JPG). It went through a number of iterations, has been abused in just about any conceivable way, chained with proxies, tunnels and caches, intercepted by middleboxes, and is for all intents and purposes _the_ universal internet pipe and primary content delivery mechanism.

[RFC1945](https://www.rfc-editor.org/rfc/rfc1945.html) describing HTTP/1.0 was fairly easy to read, but since then, things have gotten pretty complex: as of May 2025, the number of HTTP-related RFCs ranges from about a conservatively estimated dozen (focused on core protocol definitions and HTTP semantics) to a few hundred (based on title searches across [the RFC index](https://www.rfc-editor.org/rfc-index.html)).

HTTP/1.1 ([RFC2616](https://www.rfc-editor.org/rfc/rfc2616.html) and onwards) remains the lowest common denominator that clients and servers need to support, and of course modern stacks will want to use HTTP/2 ([RFC9113](https://www.rfc-editor.org/rfc/rfc9113.html)) and HTTP/3 ([RFC9114](https://www.rfc-editor.org/rfc/rfc9114.html)), but just how do they determine each others' capabilities and bootstrap their connection?

Let's take a look...

### HTTP -> HTTPS

First, let's get from plain text HTTP to HTTPS. Even though modern browsers may default to HTTPS these days ([Chrome](https://blog.chromium.org/2021/03/a-safer-default-for-navigation-https.html) and [Safari](https://developer.apple.com/documentation/safari-release-notes/safari-15-release-notes) do so since 2021, [Firefox](https://www.mozilla.org/en-US/firefox/129.0/releasenotes/) since 2024), other tools or libraries might not. So how do we get to HTTPS if we're making our initial connection via HTTP?

#### 3xx Redirect

The most obvious approach here is for the server to return a 300 level [HTTP status code](https://github.com/jschauma/httpstatus):

$ curl -I http-123.test.netmeister.org
HTTP/1.1 301 Moved Permanently
Connection: keep-alive
Location: https://http-123.test.netmeister.org/

Easy. A client receiving this result will then automatically follow the redirect, establish a TLS connection and then repeat the request:

$ curl --http1.1 -L -I http-123.test.netmeister.org
HTTP/1.1 301 Moved Permanently
Connection: keep-alive
Location: https://http-123.test.netmeister.org/

HTTP/1.1 200 OK
Alt-Svc: h3=":443", h2=":443"
Strict-Transport-Security: max-age=31536000; includeSubDomains; preload
Content-Type: text/html

Here, I specified `--http1.1` to explicitly use HTTP/1.1. In the case of plain HTTP that isn't necessary: even though HTTP/2 in the clear (aka `h2c`) is _technically allowed_ by the specification, it's not supported by the overwhelming majority of implementations. On the other hand, `curl(1)` supports (and offers) HTTP/2 by default, but we'll discuss that upgrade path below. So let's stick with HTTP/1.1 for the time being and see what the above request looks like on the wire, using Wireshark:

[![Image 1: Wireshark screenshot showing the HTTP - > HTTPS redirect](https://www.netmeister.org/blog/images/http-301.tcpdump.png)](https://www.netmeister.org/blog/images/http-301.tcpdump.png)

Seeing the packets here helps us understand the cost of the redirect: After the initial DNS lookup (packets 1 and 2), we make a TCP connection (packets 3-5) and issue our `HEAD` request (packet 6). We receive the 301 redirect (packet 7) and now have to make a _new_ TCP connection to the same host (packets 9-11), then begin our TLS handshake (packets 13-23) before we can then make the now encrypted HTTP request.

Since the packets are now encrypted, we can't see the HTTP request. Unless...

#### Using `SSLKEYLOGFILE` to debug TLS connections

Several applications honor the `SSLKEYLOGFILE` environment variable, which allows you to log the TLS session key, and which e.g., Wireshark can read to then decrypt the TLS packets.[1](https://www.netmeister.org/blog/http-123.html#1) To use it, simply `export SSLKEYLOGFILE=/tmp/tlskeys`, invoke the HTTP client (e.g., `curl(1)`[2](https://www.netmeister.org/blog/http-123.html#2) or `/Applications/Google\ Chrome.app`), and then drill down in Wireshark->Preferences->Protocols->TLS and set the pathname for "(Pre)-Master-Secret log filename" to `/tmp/tlskeys`.

Once you've loaded the TLS secrets in Wireshark, the same packets from above then become:

[![Image 2: Wireshark screenshot showing the HTTP - > HTTPS redirect with HTTPS packets decrypted](https://www.netmeister.org/blog/images/https-301.tcpdump.png)](https://www.netmeister.org/blog/images/https-301.tcpdump.png)

The only difference here is that we now can now see the TLS encrypted extensions and certificates (packet 21) and then the application layer protocol (i.e., HTTP/1.1; packets 24 and 26).

#### Remembering to use HTTPS

Now given the overhead of the redirect, we probably want to convince the client to remember to talk to us over HTTPS in the future. For that, we are sending back the [HTTP Strict Transport Security](https://en.wikipedia.org/wiki/HTTP_Strict_Transport_Security) (HSTS) header (in yellow above). Since the initial request triggering the redirect was made using plain HTTP, an active MitM attacker could remove such a header were it included in the plain HTTP response, and could of course alter the redirect altogether. For this reason, popular browsers also offer the option to hard code a domain into the browsers to only ever talk to that domain using HTTPS.

This preloading is done via the [HSTS preload](https://hstspreload.org/) list, and can be applied to the entire domain, including all subdomains.[3](https://www.netmeister.org/blog/http-123.html#3) This can at times cause surprising behavior when you want to offer a subdomain of a preloaded domain over HTTP, and you suddenly find your browser refusing to visit it using HTTP.

You can inspect the HSTS list in your (Chrome based[4](https://www.netmeister.org/blog/http-123.html#4)) browser via `chrome://net-internals/#hsts`. If you enter a raw domain name (i.e., without an explicit `http` or `https`), you can see the HTTPS upgrade in the Developer Tools network console shown as a 
```
307 Internal
Redirect
```
:

Now that `307` is a bit of a lie, since the client did not actually _make_ any request to the server, but I suppose that's just how the static HSTS preload list is implemented.

### Upgrading to HTTP/2

Ok, so the next time we make a request, our client will know to use HTTPS. But how does it know whether to use HTTP/1.1 or HTTP/2?

In some cases, you may see an `Upgrade: h2` header (see [RFC7230](https://www.rfc-editor.org/rfc/rfc7230#section-6.7)), asking the client to use HTTP/2. This is a bit of an oddity, since the HTTP/2 specification mandates that HTTP/2 negotiation _MUST_ happen via the TLS Application-Layer Protocol Negotiation Extension (ALPN, [RFC7301](https://www.rfc-editor.org/rfc/rfc7301.html)). Some web servers may, however, set this header for e.g., backwards compatibility or the (as noted above effectively unused) `h2c` mode. (I'm looking at you, Apache [mod_http2](https://httpd.apache.org/docs/2.4/mod/mod_http2.html).)

Much better: set the `Alt-Svc` header (see [RFC7838](https://www.rfc-editor.org/rfc/rfc7838.html)), telling the client that your server supports both HTTP/2 and HTTP/3.[5](https://www.netmeister.org/blog/http-123.html#5) The client may then cache this information and the next time it makes a connection to this server, it would then utilize the given protocol. (There does not appear to be a way to inspect the `Alt-Svc` cache in the different browsers; flushing it requires flushing all data for the given site.)

But this doesn't help us for _this_ connection which the client _could_ have made using HTTP/2, if it had known that the server supports it. As noted above, HTTP/2 mandates protocol negotiation to happen via ALPN. As a TLS extension, this happens in the TLS `ClientHello`, and thus allows the client to determine the application layer protocol to use at TLS handshake time. Let's observe that in action:

$ curl -L -I http-123.test.netmeister.org
HTTP/1.1 301 Moved Permanently
Content-Type: text/html
Connection: keep-alive
Location: https://http-123.test.netmeister.org/

HTTP/2 200 
content-type: text/html
content-length: 272
alt-svc: h3=":443", h2=":443"
strict-transport-security: max-age=31536000; includeSubDomains; preload

And on the wire:

[![Image 3: Wireshark screenshot showing the HTTP - > HTTPS redirect with HTTP/2 negotiated via ALPN](https://www.netmeister.org/blog/images/http2-alpn.tcpdump.png)](https://www.netmeister.org/blog/images/http2-alpn.tcpdump.png)

As before, we see the plain text HTTP/1.1 redirect (packet 7) lead to a new TCP handshake (packets 9-11), the client offering `h2` in the ALPN extension (packet 13), the server selecting `h2` (in packet 21), and the client then speaking HTTP/2 immediately (packet 24).

### Upgrading to HTTP/3

Ok, so we're able to get from HTTP to HTTPS and from HTTP/1.1 to HTTP/2. How do we get from here to HTTP/3? So far, our client hasn't offered `h3`, although the server has advertised in in the `Alt-Svc` header.

Since HTTP/3 uses [QUIC](https://en.wikipedia.org/wiki/QUIC) over UDP for transport instead of TCP, any client that wants to speak HTTP/3 must be built against a QUIC-enabled TLS library, which... is a bit of [a mess](https://www.haproxy.com/blog/state-of-ssl-stacks). `curl(1)`, for examples, regards HTTP/3 support as [experimental](https://curl.se/docs/http3.html), so we'll switch to using an actual browser for the next part. Fortunately, both Chrome and Firefox honor the `SSLKEYLOGFILE` environment variable, making dissecting packets nice and easy.

$ export SSLKEYLOGFILE=/tmp/tlskeys
$ /Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome http-123.test.netmeister.org

Once Chrome has loaded the site, we then _reload_ the page to trigger the protocol upgrade. The resulting sequence of packets observed is then:

[![Image 4: Wireshark screenshot showing the HTTP/2 - > HTTP/3 upgrade for subsequent connections](https://www.netmeister.org/blog/images/http3.tcpdump.png)](https://www.netmeister.org/blog/images/http3.tcpdump.png)

Here, we see Chrome completing the TCP handshake (packets 5-7), the TLS ClientHello (including the offer to use HTTP/2 in the ALPN extension; packet 9), the server selecting HTTP/2 (packet 17), and Chrome then speaking HTTP/2 (packets 20 - 25).

The HTTP `Alt-Svc` header it received in packet 25 included the directive `h3=":443"`, so when we then reloaded the page (note: _not_ shift-reload, which would have caused Chrome to "forget" the `Alt-Svc` for this site), Chrome could switch over to QUIC (packets 31 onwards) and then make the request using HTTP/3 (packets 44-45).

#### Going straight to HTTP/3

Ok, cool, cool, we can get to HTTP/3, but that took several round trips and multiple handshakes and _then_ required the client to remember a setting from the server before switching protocols. That's far from ideal.

Fortunately, we have a much better way: note that in the above packet capture we're seeing the client perform not only the `A` record lookup for our domain, but also query the [RFC9460](https://www.rfc-editor.org/rfc/rfc9460.html)`HTTPS` DNS record. And that record supports the `alpn` "SvcParamKey". So let's add such a record to our domain:[6](https://www.netmeister.org/blog/http-123.html#6)

$ host http-123.test.netmeister.org
http-123.test.netmeister.org has address 45.79.180.226
http-123.test.netmeister.org has IPv6 address 2600:3c03::f03c:95ff:fe49:a5b
http-123.test.netmeister.org has HTTP service bindings 1 . alpn="h3,h2" \
        ipv4hint=45.79.180.226 ipv6hint=2600:3c03::f03c:95ff:fe49:a5b
$ 

Now if we flush our DNS cache, delete all data from the browser and start it fresh from the command-line, we see:

[![Image 5: Wireshark screenshot showing parallel use of HTTP/2 and HTTP/3](https://www.netmeister.org/blog/images/http3-https.tcpdump.png)](https://www.netmeister.org/blog/images/http3-https.tcpdump.png)

Wait, this is showing us that Chrome is doing _both_ HTTP/2 and HTTP/3 in parallel? The HTTPS DNS record lookup provides the ALPN hint in packet 4, but then we are seeing Chrome initiate a TCP connection (packet 5) as well as a QUIC connection (packet 6). The TLS handshake over TCP is completed (in packet 34) when the HTTP/3 request has already been handled (packets 23 and 30), so Chrome then abandons its efforts and doesn't bother to speak HTTP/2 over the established TCP+TLS connection.

This is an example of [QUIC-TCP Racing](https://groups.google.com/a/chromium.org/g/proto-quic/c/igD7dLSct24) ([see also](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=10453353)) following a modified "[happy eyeballs](https://everything.curl.dev/usingcurl/connections/happy.html#http3-racing)" approach. We also observe that HTTP/3 is (in this case, anyway) faster than HTTP/2, which, after all, is the whole point to begin with.

#### Other browsers

Ok, that's Chrome - what about other browsers?

Firefox behaves somewhat differently. For starters, Firefox only performs `HTTPS` DNS lookups if it is using DNS-over-HTTPS. When that is enabled, and the `HTTPS` lookup provides a result with an `alpn` SvcParamKey, then Firefox does _not_ appear to race QUIC/TCP and instead directly attempts HTTP/3. However, it will _fall back_ to HTTP/2 if the QUIC handshake cannot complete within a given tolerance time.

Finally, Safari will perform the `HTTPS` lookup immediately and [directly use HTTP/3](https://developer.apple.com/videos/play/wwdc2021/10094/) if that was advertised in the `alpn` SvcParamKey and fall back to HTTP/2 only if needed.

Oh, and one quick note: if you are using a proxy it may be the case that you _can't_ talk HTTP/3 at all, unless the proxy also handles UDP. For example, even though SOCKS5 supports UDP, [Tor](https://www.torproject.org/) does _not_, and you may spend an hour trying to `tcpdump(8)` and debug Firefox and wonder why the fresh eff it just won't talk H3 - ask me how I know...

### Summary

Ok, so let's summarize how we get from HTTP/1.1 to HTTP/2 to HTTP/3. It's useful to keep in mind the high-level differences between the three protocols, so let's reference this useful image from Wikipedia:

With that in mind, we have seen the promotion from one protocol to the other via the following means:

*   From HTTP to HTTPS: 
    *   HTTP server-side redirect via status code `301`; this incurs an additional TCP handshake
    *   clients remember the redirect if the server sets an [RFC6797](https://www.rfc-editor.org/rfc/rfc6797) HSTS header
    *   clients may have a _static_ (i.e., hard-coded) HSTS list (see [hstspreload.org](https://hstspreload.org/))
    *   set an [RFC9460](https://www.rfc-editor.org/rfc/rfc9460.html)`HTTPS` DNS record (`IN HTTPS 1 .`)

*   From HTTP/1.1 to HTTP/2: 
    *   negotiation of the protocol for _this_ connection in the TLS handshake via the [RFC7301](https://www.rfc-editor.org/rfc/rfc7301.html) ALPN extension
    *   servers may set the [RFC7838](https://www.rfc-editor.org/rfc/rfc7838.html)`Alt-Svc` header to influence _future_ connections
    *   set an [RFC9460](https://www.rfc-editor.org/rfc/rfc9460.html)`HTTPS` DNS record with an `alpn` SvcParamKey (`IN HTTPS 1 . alpn="h2"`)
    *   clients may cache either result for future connections

*   From HTTP/1.1 or HTTP/2 to HTTP/3: 
    *   you _cannot_ use the ALPN extension _within a TLS+TCP handshake_ to upgrade _this_ connection to HTTP/3, since this requires a protocol switch to QUIC
    *   negotiation of the protocol for _this_ connection in the TLS handshake _inside QUIC_ via the [RFC7301](https://www.rfc-editor.org/rfc/rfc7301.html) ALPN extension
    *   servers may set the [RFC7838](https://www.rfc-editor.org/rfc/rfc7838.html)`Alt-Svc` header to influence _future_ connections
    *   set an [RFC9460](https://www.rfc-editor.org/rfc/rfc9460.html)`HTTPS` DNS record with an `alpn` SvcParamKey (`IN HTTPS 1 . alpn="h3"`)
    *   clients may cache either result for future connections
    *   clients may "race" TCP and QUIC or fallback to HTTP/2 if QUIC fails

Or, even more terse: use ALPN to affect the current connection, `Alt-Svc` to influence future requests, and use `HTTPS` DNS records to minimize guessing and allow the client to immediately jump to HTTP/3.

And yes, things have gotten just a smidgen more complex since the olden days of yore when all you had to do was make a TCP connection to port 80 and merely send `GET /`...

May 28th, 2025

* * *

Footnotes:

[1] There's even an [IETF draft](https://datatracker.ietf.org/doc/html/draft-ietf-tls-keylogfile) in the TLS Working Group proposing a standardization of that file format, although there's [some discussion](https://mailarchive.ietf.org/arch/browse/tls/?q=sslkeylogfile) around whether key logging is something that should be encouraged by such a standardization.[↩](https://www.netmeister.org/blog/http-123.html#b1)

[2] Note that on macOS the system `curl(1)` does _not_ support key logging, since that uses Apple's `SecureTransport` TLS backend. You'd have to install `curl(1)` from e.g., HomeBrew and use _that_ to get support for `SSLKEYLOGFILE`. [↩](https://www.netmeister.org/blog/http-123.html#b2)

[3] For example, my own domain is indeed hard coded [in Chromium](https://source.chromium.org/chromium/chromium/src/+/main:net/http/transport_security_state_static.json;l=15618) (and from there dynamically included in Firefox and Safari, both of which consume the Chromium list).[↩](https://www.netmeister.org/blog/http-123.html#b3)

[4] Firefox used to expose HSTS information under `about:networking#security`; nowadays there doesn't appear to be a way to inspect the dynamic or static HSTS list any longer). [↩](https://www.netmeister.org/blog/http-123.html#b4)

[5] Note: The `Alt-Svc` header is generally _not_ honored by clients if set via plain HTTP, since this would allow an active MitM attacker to redirect traffic. You will note that it was hence _not_ set by the server when we talked HTTP.[↩](https://www.netmeister.org/blog/http-123.html#b5)

[6] Recent versions of the `host(1)` command shipping with Bind perform the `HTTPS` lookup automatically; you can also use recent versions of the `dig(1)` command.[↩](https://www.netmeister.org/blog/http-123.html#b6)

* * *

Links:

*   [Use of HTTPS Resource Records](https://www.netmeister.org/blog/https-rrs.html)
*   [CS615 System Administration; HTTP](https://stevens.netmeister.org/615/07.pdf)
*   [CS615 System Administration; HTTPS](https://stevens.netmeister.org/615/08.pdf)
