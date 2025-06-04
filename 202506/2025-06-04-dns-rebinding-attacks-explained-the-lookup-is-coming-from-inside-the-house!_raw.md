Title: DNS rebinding attacks explained: The lookup is coming from inside the house!

URL Source: https://github.blog/security/application-security/dns-rebinding-attacks-explained-the-lookup-is-coming-from-inside-the-house/

Published Time: 2025-06-03T16:00:00+00:00

Markdown Content:
DNS rebinding attack without CORS against local network web applications. Explore the topic further and see how it can be used to exploit vulnerabilities in the real-world.

June 3, 2025

|

8 minutes

*    Share: 
*   [](https://x.com/share?text=DNS%20rebinding%20attacks%20explained%3A%20The%20lookup%20is%20coming%20from%20inside%20the%20house%21&url=https%3A%2F%2Fgithub.blog%2Fsecurity%2Fapplication-security%2Fdns-rebinding-attacks-explained-the-lookup-is-coming-from-inside-the-house%2F)
*   [](https://www.facebook.com/sharer/sharer.php?t=DNS%20rebinding%20attacks%20explained%3A%20The%20lookup%20is%20coming%20from%20inside%20the%20house%21&u=https%3A%2F%2Fgithub.blog%2Fsecurity%2Fapplication-security%2Fdns-rebinding-attacks-explained-the-lookup-is-coming-from-inside-the-house%2F)
*   [](https://www.linkedin.com/shareArticle?title=DNS%20rebinding%20attacks%20explained%3A%20The%20lookup%20is%20coming%20from%20inside%20the%20house%21&url=https%3A%2F%2Fgithub.blog%2Fsecurity%2Fapplication-security%2Fdns-rebinding-attacks-explained-the-lookup-is-coming-from-inside-the-house%2F)

My colleague Kevin Stubbs mentioned the topic of DNS rebinding attacks in a[previous](https://github.blog/security/application-security/localhost-dangers-cors-and-dns-rebinding/) blog post. No worries if you haven’t read it yet though—in this article, we’ll walk you through the concept of DNS rebinding from scratch, demystify how it works, and explore why it’s a serious browser-based security issue.

We’ll start by revisiting the same-origin policy, a fundamental part of web security, and show how DNS rebinding bypasses it. You’ll see real-world scenarios where attackers can use this technique to access internal applications running on your local machine or network, even if those apps aren’t meant to be publicly available. We’ll dive into a real vulnerability in the Deluge BitTorrent client, explaining exactly how DNS rebinding could have been used to read arbitrary files from a local system. Finally, we’ll go over practical steps you can take to protect yourself or your application from this often-overlooked but potent attack vector.

Same-origin policy
------------------

Same-origin policy (SOP) is a cornerstone of browser security introduced in 1995 by Netscape. The idea behind it is simple: Scripts from webpages of one origin should not be able to access data from a webpage of another origin. For example, nobody wants arbitrary webpages to be able to read their currently logged-in webmail. So that websites can be distinguishable from the next, they’re each defined with a combination of protocol (schema), host (DNS name), and a port number. Any mismatch in these three parts makes the origin different.

For example, for the webpage: `https://www.somedomain.com/sub/page.html` possible origin comparisons are the following:

| **URL** | **Outcome** | **Reason** |
| --- | --- | --- |
| `https://www.somedomain.com:81/sub/page.html` | Different | The port 81 doesn’t match 443 (the default for https) |
| `https://somedomain.com/sub/page.html` | Different | Exact `www.somedomain.com` match is required |
| `http://www.somedomain.com:443/sub/page.html` | Different | The schema (protocol) HTTP doesn’t match HTTPS |
| `https://www.somedomain.com/admin/login.html` | Same | Only the path differs |

The attack: DNS rebinding
-------------------------

People tend to think running something on localhost completely shields it from the external world. While they understand that they can access what is running on the local machine from their local browser, they miss that the browser may also become the gateway through which unsolicited visitors get access to the web applications on the same machine or local network.

Unfortunately, there is a disconnect between the browser security mechanism and networking protocols. If the resolved IP address of the webpage host changes, the browser doesn’t take it into account and treats the webpage as if its origin didn’t change. This can be abused by attackers.

For example, if an attacker owns the domain name `somesite.com` and delegates it to a DNS server that is under attacker control, they may initially respond to a DNS lookup with a public IP address, such as 172.217. 22.14, and then switch subsequent lookups to a local network IP address, such as 192.168.0.1 or 127.0.0.1 (i.e. localhost). Javascript loaded from the original `somesite.com` will run client-side in the browser, and all further requests from it to `somesite.com` will be directed to the new, now local, IP address. From then on, documents loaded from different IP addresses—but resolved from the same hosts—will be considered to be of the same origin. This gives the attackers the ability to interact with the victim’s local network via Javascript running in the victim’s browser. This makes any web application that runs locally on the same machine or local network as the victim’s browser accessible to the scripts loaded from `somesite.com` too.

One catch is that if the web application requires authentication, its cookies are not made available to the attacker. Since the targeted user originally opened `somesite.com`—and even though subsequent Javascript requests are directed to the new, attacker rebound, IP address—the browser still operates in the context of the `somesite.com` origin. That means the victim’s browser will not use stored authentication or session context for the locally targeted service name.

Other scenarios could include attackers abusing local VPN routes that are available to the targeted user, allowing access to corporate intranet web applications, for example.

The response: caching
---------------------

Browsers try to resist DNS rebinding like this by caching DNS responses, but the defense is far from perfect. Some browsers have implemented [Local Network Access](https://wicg.github.io/local-network-access/) (also known as CORS-RFC1918), a new draft W3C specification. It closed some avenues, but still left some bypasses, such as 0.0.0.0 IP address on Linux and MacOS, so the DNS rebinding behavior is very browser and operating system (OS) dependent. There are so many layers involved (browser DNS cache, OS DNS cache, DNS nameservers) that the attack is often considered unreliable and not taken as a real threat. However, there are also tools that can automate attacks such as Tavis Ormandy’s [Simple DNS Rebinding Service](https://github.com/taviso/rbndr) or NCCGroup’s [Singularity of Origin](https://github.com/nccgroup/singularity).

A real-world vulnerability
--------------------------

Now let’s dive into technicalities of a real-world vulnerability found in BitTorrent client [Deluge](https://deluge-torrent.org/) (fixed in v2.2.0) and how DNS rebinding could have been used to exploit it.

The Deluge BitTorrent client supports starting [two services](https://deluge.readthedocs.io/en/latest/how-to/index.html#deluge-as-a-service)on system boot: daemon and WebUI. The WebUI web application service may also be started by enabling the WebUI plugin (installed, but disabled by default) in the preferences dialog of the Deluge client. It is also convenient to run the WebUI application permanently on a server in the local network. We found a path traversal in an unauthenticated endpoint of the web application that allowed for arbitrary file read.

```
def render(self, request):
	log.debug('Requested path: %s', request.lookup_path)
	lookup_path = request.lookup_path.decode()
	for script_type in ('dev', 'debug', 'normal'):
		scripts = self.__scripts[script_type]['scripts']
		for pattern in scripts:
			if not lookup_path.startswith(pattern): # <-- [1]
				continue

			filepath = scripts[pattern]
			if isinstance(filepath, tuple):
				filepath = filepath[0]

			path = filepath + lookup_path[len(pattern) :] # <-- [2]

			if not os.path.isfile(path):
				continue

			log.debug('Serving path: %s', path)
			mime_type = mimetypes.guess_type(path) # <-- [4]

			request.setHeader(b'content-type', mime_type[0].encode()) # <-- [5]
			with open(path, 'rb') as _file: # <-- [3]
				data = _file.read()
			return data
```

The `/js`[endpoint](https://github.com/deluge-torrent/deluge/blob/7660e2e5cab82167ff95f9f555fcfe9421e554f4/deluge/ui/web/server.py#L422-L445) of the WebUI component didn’t require authentication, since its purpose is to serve JavaScript files for the UI. The `request.lookup_path` was validated to start with a known keyword [1], but it could have been bypassed with `/js/known_keyword/../...` The path traversal happened in [2], when the path was concatenated and later used to read a file [3]. The only limitation was the `mimetypes.guess_type` call at [4], because, in case it returned a mime type `None`, `request.setHeader` at [5] throws an exception.

The path traversal allowed for unauthenticated read of any file on the system as long as its MIME type was recognized.

Even if attackers constrain themselves to Deluge-only files, Deluge uses files with `.conf` extensions to store configuration settings with sensitive information. This extension is identified as `text/plain` by `mimetypes.guess_type`. A request to `/js/deluge-all%2F..%2F..%2F..%2F..%2F..%2F..%2F.config%2Fdeluge%2Fweb.conf`, for example, would return such information as the WebUI admin password SHA1 with salt and a list of sessions. The sessions are written to the file only on service shutdown, and, after the default 1 hour expiration, are not updated. But with some luck, attackers could find a valid session there to authenticate themselves to the service. Otherwise, they would need to brute force the password hash. Since Deluge doesn’t use a [slow password hashing algorithm](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html#password-hashing-algorithms), they could do it very quickly for simple or short passwords.

Once attackers obtain an authenticated session, they could use the exploitation technique from [CVE-2017-7178](https://seclists.org/fulldisclosure/2017/Mar/6) to download, install, and run a malicious plugin on the vulnerable machine by using the `/json` endpoint Web API.

Exploiting it
-------------

If Deluge WebUI is [hosted externally](https://deluge-torrent.org/userguide/webui/reverseproxy/), the exploitation would be straightforward. However, even if the service is accessible only locally, since it is an unauthenticated endpoint, attackers could use a DNS rebinding attack to access the service from a specially crafted web site. For browsers that implement CORS-RFC1918, which segments address ranges into different address spaces (loopback, local network, and public network addresses), attackers could use a known Linux and MacOS bypass—the non-routable [0.0.0.0 IP address](https://www.nccgroup.com/us/research-blog/state-of-dns-rebinding-in-2023/)—to access the local service.

For the sake of simplicity, let’s assume attackers know the port of the vulnerable application (8112 by default for Deluge WebUI), though discovering that the port can be automated with [Singularity](https://github.com/nccgroup/singularity). A Deluge WebUI user opens a web page with multiple IFrames by visiting the malicious `somesite.com`. Each frame fetches `http://sub.somesite.com:8182/attack.html`. In order to bypass SOP, the port number must be the same as the attacked application. The DNS resolver the attackers control may respond alternately with 0.0.0.0, and the real IP address of the server with a very low time to live (TTL). When the DNS resolves with the real IP address, the browser fetches a page with a script that waits for the DNS entry to expire by checking if they can request and read `http://sub.somesite.com:8182/js/deluge-all/..%2F..%2F..%2F..%2F..%2F..%2F.config%2Fdeluge%2Fweb.conf`. If the attack succeeds, the script will have exfiltrated the configuration file.

For the full source of `attack.html` please check this [advisory](https://securitylab.github.com/advisories/GHSL-2024-188_GHSL-2024-191_Deluge/).

How to proactively protect yourself from DNS attacks
----------------------------------------------------

*   DNS rebinding doesn’t work for HTTPS services. Once a transport layer security (TLS) session is established with `somesite.com`, the browser validates the subject of the certificate against the domain. After the IP address changes, the browser needs to establish a new session, but it will fail, because the certificate of the locally deployed web application won’t match the domain name.
*   As already mentioned, the authentication cookies for `somesite.com` won’t be accepted by the locally deployed web application. So be sure to use strong authentication, even if it is over unencrypted HTTP.
*   Check the Host header of the request and deny if it doesn’t strictly match an allow list of expected values. A rebounded request will contain the host `somesite.com` header value.

Take this with you
------------------

Running web applications locally is a common practice by developers. However, a permanently deployed local network web application that doesn’t require authentication and TLS (i.e. no HTTPS encryption) is a red flag. DNS rebinding attacks are a vivid example of how seemingly isolated local services can be exposed through browser behavior and weak network assumptions.

Never assume a service is safe just because it’s “only running locally.” Always enforce strong, password-based authentication—even for internal services or development tools. Any local service without rigorous access control may be exposed through a victim’s browser. Validate the `Host` header. Use HTTPS wherever possible.

DNS rebinding demonstrates that assumptions about network boundaries and browser security can be dangerously misleading. Be sure to include DNS rebinding into your threat model when developing your next web application.

Written by
----------

![Image 1: Jaroslav Lobacevski](https://avatars.githubusercontent.com/u/26652396?v=4&s=200)

Related posts
-------------

### [Bypassing MTE with CVE-2025-0072](https://github.blog/security/vulnerability-research/bypassing-mte-with-cve-2025-0072/)

In this post, I’ll look at CVE-2025-0072, a vulnerability in the Arm Mali GPU, and show how it can be exploited to gain kernel code execution even when Memory Tagging Extension (MTE) is enabled.

We do newsletters, too
----------------------

Discover tips, technical guides, and best practices in our biweekly newsletter just for devs.
