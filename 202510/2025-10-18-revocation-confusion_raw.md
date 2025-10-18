Title: Revocation Confusion

URL Source: https://nullpxl.com/post/revocation-confusion/

Markdown Content:
Back in December 2024 I needed to get to Vancouver from Waterloo. I looked for the cheapest direct flight and found the best option to be from Flair airlines. Trying to get to the website, flyflair.com, resulted in a big scary security warning screen from Firefox.

[![Image 1: firefox security warning screen indicating the SSL certificate was revoked](https://nullpxl.com/revoked/securityriskahead.png)](https://nullpxl.com/revoked/securityriskahead.png)
firefox security warning screen indicating the SSL certificate was revoked

I found a [Reddit thread](https://www.reddit.com/r/flairairlines/comments/1hpdq1w/flyflaircom_ssl_certificate_invalid/) created on that day by someone with the same issue, but no one else in the comments seemed to be having any problems. A Moderator of the page even said in a reply to a comment “The issue was with [the original poster]. The site is working fine”. The creator of the post got gaslit HARD. And to the commenters’ credit, the site was appearing to be completely fine when using Chrome– the most popular browser.

[![Image 2](https://nullpxl.com/revoked/rc_1.png)](https://nullpxl.com/revoked/rc_1.png)[![Image 3](https://nullpxl.com/revoked/rc_2.png)](https://nullpxl.com/revoked/rc_2.png)

As it turns out, different browsers (and operating systems) [behave wildly differently](https://www.ssl.com/blogs/how-do-browsers-handle-revoked-ssl-tls-certificates/) when an SSL certificate is revoked. Obviously this will eventually lead to confused users! Chrome will essentially not care and allow the user to browse the website, and Firefox will show the scary security screen. Mobile browsers vs Desktop browsers is a whole other thing too.

> “What does it mean to revoke an ssl cert?": owner of the website says ‘hey btw it’s not safe to encrypt communications to my website using this certificate anymore’

I really have two big points to make here. If you're interested in more technical stuff please read on otherwise just keep this in mind:

*   User experience and security are interwoven 
    *   In this case, even though the individual browsers themselves were internally consistent, they responded completely differently when trying to access the EXACT SAME website… this is bad for both the users and website owners. There’s a reason why web standards exist.

*   People (on Reddit especially) speak with so much authority on things they don’t really know about, even moderators! DON'T TRUST REDDIT.

### Ok so what was actually going on

Technical background time! When you start a session of encrypted communication between your computer and a website, you need the website's Public Key. The website uses the fact that it has the corresponding Private Key to this Public Key to communicate back. _How can you know that you have the correct public key for each domain?_ There’s a ton of networking architecture built around this idea of trusted ‘certificate authorities’ (CAs): organizations that can sign intermediary and ‘leaf certificates’ which ultimately allow for certificates to verifiably map public keys to an identity/website.

_“What if you accidentally post your private key somewhere, or someone gets it through some other way?"_ Well first of all thanks to forward secrecy the actual impact is limited. But still it's not good. In this circumstance you can [revoke your certificate](https://letsencrypt.org/docs/revoking/). A certificate can include a URL for an ‘Online Certificate Status Protocol’ (OCSP) server. This can be queried prior to trusting a website’s certificate to first see if the cert has been revoked by the owner or issuing org. Alternatively, there are also ‘certificate revocation lists’ (CRLs) which as far as I can tell are typically managed by each CA. There can be a URL pointing towards a big list full of serial/identification numbers inside of each certificate. The idea is you compare the current certificates serial number against all of the ones in that big list to see if it’s revoked.

There are a lot of problems with both of the above methods which have led to neither really being used to the fullest extent. Let's look at OCSP first.

#### Why is OCSP bad?

*   CA/owner of the OCSP server will know what domains the user is visiting. And, the request to the ocsp server isn't encrypted, so the domain gets leaked on the network. Clearly these are privacy issues, and these properties could be used for censorship too.
*   Making the request and waiting for the response adds latency. bad user experience.
*   _“What happens if the ocsp server is down?? do you just not get to visit the website even if everything else is fine?"_ Most browsers (even firefox) by default will ‘soft-fail’ meaning if the ocsp server is down, it will just assume everything is alright and let you browse the website. hmmmm.
*   Lots of other reasons. this article is quite good: [https://www.feistyduck.com/newsletter/issue_121_the_slow_death_of_ocsp](https://www.feistyduck.com/newsletter/issue_121_the_slow_death_of_ocsp)
*   there's something called ‘OCSP stapling’ which solves a ton of these issues but most web servers and browsers just never took the time to implement it properly.

#### Why are CRLs bad?

*   The lists grow really big and are hard to check quickly

So pretty much what ended up happening is most browsers more or less ignored OCSP, and then created their own internal mini-CRLs. Chrome for instance doesn’t check OCSP responses OR all the CRLs available. Instead, they developed ‘[CRLSets](https://www.chromium.org/Home/chromium-security/crlsets/)’

> CRLSets ([background](https://www.imperialviolet.org/2012/02/05/crlsets.html)) are the primary means by which Chrome quickly blocks certificates in emergency situations. As a secondary function, they can also contain some number of non-emergency revocations. These latter revocations are obtained by crawling CRLs published by CAs.

Firefox (as of writing in July 2025) will check via OCSP by default, although is [moving to CRLite](https://bugzilla.mozilla.org/show_bug.cgi?id=1429800), which is a giant CRL that’s made usable with a cascade of bloom filters.

Let's Encrypt (massive CA that offers free certificates) even [announced at the end of 2024](https://letsencrypt.org/2024/12/05/ending-ocsp/) that they're ending support for OCSP in favor of CRLs and [shorter certificate lifetimes](https://letsencrypt.org/2025/02/20/first-short-lived-cert-issued/).

> We plan to end support for OCSP primarily because it represents a considerable risk to privacy on the Internet […] For every year that we have existed, operating OCSP services has taken up considerable resources that can soon be better spent on other aspects of our operations

> Let’s Encrypt has supported OCSP Must Staple for a long time, because of the potential to improve both privacy and security. However, Must Staple has failed to get wide browser support after many years. And popular web servers still implement OCSP Stapling in ways that create serious risks of downtime. […] As part of removing OCSP, we’ll also be removing support for OCSP Must Staple.

#### Alright but what was the issue with Flair?

The [certificate in use](https://crt.sh/?q=6e73866d10147cb7d0891d40eb67800a31cf91551c4c565b1aa61323c9008dce) was revoked, with the reason given being ‘cessationOfOperation’. [A new one was issued](https://crt.sh/?id=15830964410) almost immediately after the former was revoked, but my guess is that flair forgot to re-configure their web servers or something so it wasn't being used right away. Since people seem to disagree on if it's okay to risk trusting a certificate the website owner themself says not to use, some users could access the website and some couldn't.

### What's next?

shorter certificate lifetimes + clever CRL checking methods like CRLite probably. And ideally better security warning screens and consistency across browsers and operating systems :)