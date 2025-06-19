Title: Every service should have a killswitch

URL Source: https://www.seangoedecke.com/killswitches/

Markdown Content:
The more time you spend designing systems, the more paranoid you get about things going wrong. The most experienced and paranoid engineers I know build a killswitch into every single piece of automation.

### What a killswitch looks like

If your company has a feature flagging system - which it should - this can be as simple as adding a `return if feature_enabled?(pdf_converter_job_killswitch)` to the top of your scheduled job. If the job ever goes out of control (running way too often, or using too many resources) you can turn it off by creating or enabling that feature. Enabling a feature flag is usually many minutes quicker than a code deploy. During an incident, when deploying is difficult, it can be _hours_ quicker.

A recent example I noticed of this was this Google [incident report](https://status.cloud.google.com/incidents/ow5i3PPK96RduMcb1SsW), which describes:

*   killswitches for features being a normal part of Google software,
*   the killswitch not working being a contributing factor to the incident, and
*   the on-call SREs rushing out a code deploy with a functioning killswitch during the incident.

It doesn’t always have to be a feature flag. I’ve seen “safety files” that automation won’t run without - so you can stop the automation by deleting the file. I’ve also heard of packaged software that needs to “phone home” to some external API before it’ll function. But in the world of SaaS tech companies, it’s usually a feature flag.

### Features going out of control

When might you want to use a killswitch? Sometimes it’s a way to instantly remediate a software bug. If you’ve got code that’s systematically deleting user data, or adding nonsense comments to their posts, it’s useful to be able to turn that off.

In the world of LLMs, this is especially important: it’s very hard to track all the possible failure modes of a LLM-driven feature. If someone jailbreaks your LLM chatbot to start handing out recipes for anthrax, the quicker you can turn it off, the better.

The more common time you might want a killswitch is when the system goes _down_.

### Going down fast, coming up slow

Bringing a service back up once it fails is often much harder than remediating the specific failure. Suppose you’re down because your database has died under query load. Well, nothing causes database query spikes like all of your users refreshing broken pages, or all of your automated jobs retrying failed operations, or all your unprocessed queues trying to empty out at the same time.

There are lots of ways to make this easier. Exponential backoff is one: if you’re writing code that retries a failure, don’t retry every five seconds, but instead retry after five, then ten, then twenty, and so on. That way if a service is down, you’re making your own load on it lighter instead of heavier, which makes it easier for that service to come back up. Another classic is “jitter”: adding some extra randomness to the delay so your services aren’t all retrying at exactly the same time.

However, in my experience, there’s no substitute for being able to just turn off some high-volume low-importance feature via a killswitch. When things are really bad, sometimes you want to turn everything remotely non-essential off in the hopes that you’ll be able to get the essentials running sooner.

### Final thoughts

The biggest problem with killswitches is that you don’t use them. Any code that isn’t regularly executed is a problem waiting to happen - it can silently break in any number of unpredictable and exciting ways.

However, killswitches by definition are _simple_. They just turn off a system. To me, that’s a lot less scary than a whole feature that sits there and doesn’t get executed.

I don’t think you should add a killswitch to every code path. That’d be too much cruft and make everything impossible to reason about. Some code paths are so essential that you can’t turn them off - they’re the systems that you kill _other_ systems to protect. But in general if you’re writing code that’s triggered by an event, or by some frequent customer action, a wisely paranoid engineer will want to have an easy way to turn that off without needing to deploy.

If you liked this post, consider [subscribing](https://buttondown.com/seangoedecke) to email updates about my new posts.
