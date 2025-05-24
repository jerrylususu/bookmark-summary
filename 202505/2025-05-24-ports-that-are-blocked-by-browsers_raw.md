Title: Ports that are blocked by browsers

URL Source: https://www.keenformatics.com/ports-that-are-blocked-by-browsers

Published Time: 2023-03-20T14:36:00+01:00

Markdown Content:
Today I was experimenting with a small project using Docker and Flask. I just created two identical services and exposed them on two different ports: nothing fancy. However, to my surprise, only one of the two seemed to be working.

The first service was hosted on port `8000`. As expected, I could visit `localhost:8000` and find the rendered HTML code that I had written. However, the second service hosted on port `6000` wasn’t giving me the same outcome. Instead of showing the HTML code I had prepared, my browser (Chrome) returned this error:

> This site can’t be reached
> 
> 
> The web page at http://localhost:6000/ might be temporarily down or it may have moved permanently to a new web address.
> 
> 
> ERR_UNSAFE_PORT

Being curious, I tried to reproduce the issue without Docker, just with the bare minimum setup. I created two webservers using [Python’s `http.server`](https://docs.python.org/3/library/http.server.html):

```
$ python -m http.server 8000
$ python -m http.server 6000
```

The two commands serve an HTTP server on port `8000` and `6000` respectively. And there it is again: while the first webserver works flawlessly, trying to reach the one on port `6000` returns the error described above. So what’s the problem?

Cross-protocol scripting
------------------------

Turns out that some ports are explicitly blocked by browsers. This is done in response to the so-called **Cross-protocol scripting** vulnerability ([VU#476267](https://www.kb.cert.org/vuls/id/476267)). Through this vulnerability, an attacker could forge malicious HTML code to send data to other services used by the victim (for example crafting spam emails, or [printing through a network printer](http://aaron.weaver2.googlepages.com/CrossSitePrinting.pdf)). IMAP, SMTP, NNTP and POP3 are just a small portion of the affected services.

Mozilla and other browser vendors [fixed this vulnerability](https://www-archive.mozilla.org/projects/netlib/portbanning) by explicitly banning ports that belong to the vulnerable services. This way, when the malicious HTML code tries to send its data, it will basically receive the same error that I received above.

What I find confusing is that each browser seems to show (or not show) a different message for the same situation. As we saw above, Chrome shows the `ERR_UNSAFE_PORT` message. Safari seems to just shrug its shoulders and return a completely blank page. Firefox, instead, shows the most informative message:

> This address is restricted
> 
> 
> This address uses a network port which is normally used for purposes other than Web browsing. Firefox has canceled the request for your protection.

The wording in Firefox’s message allows us to understand one more thing: the request we’re sending to port `6000` never reaches the webserver, because it’s being immediately **canceled** by the browser. We can double-check this by having a look at the server logs, that will not show any request for that address. At this point it’s clear that we don’t even need to spawn a webserver at all to see this behaviour in place! If we just head to `http://localhost:6000` when all of our webservers are shut down, we will receive the same error. The browser doesn’t care about the server: it just stops the request before it’s sent.

Testing without browser
-----------------------

If you want to prove that this restriction is actually implemented directly at the browser level, you can bypass the browser checks and request the same URL using **cURL** from terminal:

```
$ curl http://localhost:6000/
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<title>Directory listing for /</title>
</head>
<body>
<h1>Directory listing for /</h1>
<hr>
<ul>
<li><a href="some_file.txt">some_file.txt</a></li>
</ul>
<hr>
</body>
</html>
```

As you can see, this request doesn’t get blocked and it correctly shows the output produced by the Python webserver.

List of blocked ports
---------------------

For curious people, this is the list of the ports blocked by Firefox together with their respective services:

| Port | Service |
| --- | --- |
| 1 | tcpmux |
| 7 | echo |
| 9 | discard |
| 11 | systat |
| 13 | daytime |
| 15 | netstat |
| 17 | qotd |
| 19 | chargen |
| 20 | ftp data |
| 21 | ftp control |
| 22 | ssh |
| 23 | telnet |
| 25 | smtp |
| 37 | time |
| 42 | name |
| 43 | nicname |
| 53 | domain |
| 77 | priv-rjs |
| 79 | finger |
| 87 | ttylink |
| 95 | supdup |
| 101 | hostriame |
| 102 | iso-tsap |
| 103 | gppitnp |
| 104 | acr-nema |
| 109 | POP2 |
| 110 | POP3 |
| 111 | sunrpc |
| 113 | auth |
| 115 | sftp |
| 117 | uucp-path |
| 119 | NNTP |
| 123 | NTP |
| 135 | loc-srv / epmap |
| 139 | netbios |
| 143 | IMAP2 |
| 179 | BGP |
| 389 | LDAP |
| 465 | SMTP+SSL |
| 512 | print / exec |
| 513 | login |
| 514 | shell |
| 515 | printer |
| 526 | tempo |
| 530 | courier |
| 531 | chat |
| 532 | netnews |
| 540 | uucp |
| 556 | remotefs |
| 563 | NNTP+SSL |
| 587 | submission |
| 601 | syslog |
| 636 | LDAP+SSL |
| 993 | IMAP+SSL |
| 995 | POP3+SSL |
| 2049 | nfs |
| 4045 | lockd |
| 6000 | X11 |

References
----------

*   [Standard HTML form implementation allows access to IMAP, SMTP, NNTP, POP3, and other services via crafted HTML page](https://www.kb.cert.org/vuls/id/476267)
*   [Mozilla Port Blocking](https://www-archive.mozilla.org/projects/netlib/portbanning)
