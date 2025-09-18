Title: From suspicion to published curl CVE

URL Source: https://daniel.haxx.se/blog/2025/09/18/from-suspicion-to-published-curl-cve/

Published Time: 2025-09-18T09:32:47+02:00

Markdown Content:
![Image 1](https://daniel.haxx.se/blog/wp-content/uploads/2025/09/CVE.jpg)

![Image 2](https://daniel.haxx.se/blog/wp-content/uploads/2016/04/good_curl_logo-1200x459.png)

Every curl security report starts out with someone submitting an issue to us on [https://hackerone.com/curl](https://hackerone.com/curl). The reporter tells us what they suspect and what they think the problem is. This report is kept private, visible only to the curl security team and the reporter while we work on it.

![Image 3](https://daniel.haxx.se/blog/wp-content/uploads/2019/01/hackerone_logo_gray-1200x271.png)

In recent months we have gotten 3-4 security reports per week. The program has run for over six years now, with almost 600 reports accumulated.

On average, someone in the team makes a first response to that report already within the first hour.

Assess
------

The curl security team right now consists of seven long time and experienced curl maintainers. We immediately start to analyze and assess the received issue and its claims. Most reports are not identifying actual security problems and are instead quickly dismissed and closed. Some of them identify plain bugs that are not security issues and then we move the discussion over to the public bug tracker instead.

This part can take anything from hours up to multiple days and usually involves several curl security team members.

If we think the issue might have merit, we ask follow-up questions, test reproducible code and discuss with the reporter.

Valid
-----

A small fraction of the incoming reports is actually considered valid security vulnerabilities. We work together with the reporter to reach a good understanding of what exactly is required for the bug to trigger and what the flaw can lead to. Together we set a _severity_ for the problem (low, medium, high, critical) and we work out a first patch – which also helps to make sure we understand the issue. Unless the problem is deemed serious we tend to sync the publication of the new vulnerability with the pending next release. Our normal release cycle is eight weeks so we are never farther than 56 days away from the next release.

Fix
---

For security issues we deem to be severity low or medium we create a pull request for the problem in the public repository – but we don’t mention the security angle of the problem in the public communication of it. This way, we also make sure that the fix gets added test exposure and time to get polished before the pending next release. Over the last five or so years, only two in about eighty confirmed security vulnerabilities have been rated a higher severity than medium. Fixes for vulnerabilities we consider to be severity high or critical are instead merged into the git repository when there is approximately 48 hours left to the pending release – to limit the exposure time before it is announced properly. We need to merge it into the public before the release because our entire test infrastructure and verification system is based on public source code.

Advisory
--------

Next, we write up a detailed security advisory that explains the problem and exactly what the mistake is and how it can lead to something bad – including all the relevant details we can think of. This includes version ranges for affected curl versions and the exact git commits that introduced the problem as well as which commit that fixed the issue – plus credits to the reporter and to the patch author etc. We have the ambition to provide the best security advisories you can find in the industry. (We also provide them in JSON format etc on the site for the rare few users who care about that.) We of course want the original reporter involved as well so that we make sure that we get all the angles of the problem covered accurately.

As we are a CNA (CVE Numbering Authority), we reserve and manage CVE Ids for our own issues ourselves.

Pre-notify
----------

About a week before the pending release when we also will publish the CVE, we inform the [distros@openwall mailing list](https://oss-security.openwall.org/wiki/mailing-lists/distros) about the issue, including the fix, and when it is going to be released. It gives Open Source operating systems a little time to prepare their releases and adjust for the CVE we will publish.

Publish
-------

On the release day we publish the CVE details and we ship the release. We then also close the HackerOne report and disclose it to the world. We disclose all HackerOne reports once closed for maximum transparency and openness. We also inform all the [curl mailing lists](https://curl.se/mail/) and the [oss-security mailing list](https://www.openwall.com/lists/oss-security/) about the new CVE. Sometimes we of course publish more than one CVE for the same release.

Bounty
------

Once the HackerOne report is closed and disclosed to the world, the vulnerability reporter can claim a bug bounty from [the Internet Bug Bounty](https://www.hackerone.com/company/internet-bug-bounty) which pays the researcher a certain amount of money based on the severity level of the curl vulnerability.

(The original text I used for this blog post was previously provided to the [interview I made for Help Net Security](https://www.helpnetsecurity.com/2025/09/18/daniel-stenberg-running-curl-project/). Tweaked and slightly extended here.)

The team
--------

The heroes in the curl security team who usually work on all this in silence and without much ado, are currently (in no particular order):

*   Max Dymond
*   Dan Fandrich
*   Daniel Gustafsson
*   James Fuller
*   Viktor Szakats
*   Stefan Eissing
*   Daniel Stenberg

Post navigation
---------------