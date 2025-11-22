Title: We should all be using dependency cooldowns

URL Source: https://blog.yossarian.net/2025/11/21/We-should-all-be-using-dependency-cooldowns

Published Time: Fri, 21 Nov 2025 19:23:56 GMT

Markdown Content:
ENOSUCHBLOG
-----------

_Programming, philosophy, pedaling._
------------------------------------

*   [Home](https://blog.yossarian.net/)
*   [Tags](https://blog.yossarian.net/tags)
*   [Series](https://blog.yossarian.net/series)
*   [Favorites](https://blog.yossarian.net/favorites)
*   [Archive](https://blog.yossarian.net/archive)
*   [Main Site](https://yossarian.net/)
*   [TILs](https://yossarian.net/til)

* * *

_Nov 21, 2025_ Tags: [oss](https://blog.yossarian.net/tags#oss), [security](https://blog.yossarian.net/tags#security)
---------------------------------------------------------------------------------------------------------------------

* * *

**TL;DR**: Dependency cooldowns are a free, easy, and **incredibly effective** way to mitigate the _large majority_ of open source supply chain attacks. More individual projects should apply cooldowns (via tools like Dependabot and Renovate) to their dependencies, and packaging ecosystems should invest in first-class support for cooldowns directly in their package managers.

* * *

“Supply chain security” is a serious problem. It’s also **seriously overhyped**, in part because dozens of vendors have a vested financial interest in convincing your that their _framing_ of the underlying problem[1](https://blog.yossarian.net/2025/11/21/We-should-all-be-using-dependency-cooldowns#fn:problem) is (1) correct, and (2) worth your money.

What’s consternating about this is that most open source supply chain attacks have the same basic structure:

1.   An attacker compromises a popular open source project, typically via a stolen credential or CI/CD vulnerabilty (such as [“pwn requests”](https://securitylab.github.com/resources/github-actions-preventing-pwn-requests/) in GitHub Actions).

2.   The attacker introduces a malicious change to the project and uploads it somewhere that will have **maximum effect** (PyPI, npm, GitHub releases, &c., depending on the target).

At this point, the _clock has started_, as the attacker has moved into the public.

3.   Users pick up the compromised version of the project via automatic dependency updates or a lack of dependency pinning.

4.   Meanwhile, the aforementioned vendors are scanning public indices as well as customer repositories for signs of compromise, and provide alerts upstream (e.g. to PyPI).

Notably, vendors are _incentivized_ to report quickly and loudly upstream, as this increases the perceived value of their services in a crowded field.

5.   Upstreams (PyPI, npm, &c.) remove or disable the compromised package version(s).

6.   End-user remediation begins.

The key thing to observe is that the gap between (1) and (2) can be very large[2](https://blog.yossarian.net/2025/11/21/We-should-all-be-using-dependency-cooldowns#fn:gap) (weeks or months), while the gap between (2) and (5) is **typically very small**: hours or days. This means that, once the attacker has moved into the actual exploitation phase, their _window of opportunity_ to cause damage is pretty limited.

![Image 1: Figure: a not very scientific visualization of the phases above.](https://blog.yossarian.net/assets/supply-chain-attack-timeline.png)

We can see this with numerous prominent supply chain attacks over the last 18 months[3](https://blog.yossarian.net/2025/11/21/We-should-all-be-using-dependency-cooldowns#fn:filippo):

| Attack | Approx. Window of Opportunity | References |
| --- | --- | --- |
| xz-utils | ≈ 5 weeks[4](https://blog.yossarian.net/2025/11/21/We-should-all-be-using-dependency-cooldowns#fn:outlier) | [Source](https://research.swtch.com/xz-timeline) |
| Ultralytics (phase 1) | 12 hours | [Source](https://blog.yossarian.net/2024/12/06/zizmor-ultralytics-injection#appendix-rough-timeline-of-events) |
| Ultralytics (phase 2) | 1 hour | [Source](https://blog.yossarian.net/2024/12/06/zizmor-ultralytics-injection#appendix-rough-timeline-of-events) |
| tj-actions | 3 days | [Source](https://www.legitsecurity.com/blog/github-actions-tj-actions-changed-files-attack) |
| chalk | < 12 hours | [Source](https://cycode.com/blog/npm-debug-chalk-supply-chain-attack-the-complete-guide/) |
| Nx | 4 hours | [Source](https://www.stepsecurity.io/blog/supply-chain-security-alert-popular-nx-build-system-package-compromised-with-data-stealing-malware) |
| rspack | 1 hour | [Source](https://github.com/web-infra-dev/rspack/releases/tag/v1.1.8) |
| num2words | < 12 hours | [Source](https://blog.pypi.org/posts/2025-07-31-incident-report-phishing-attack/#impact-analysis) |
| Kong Ingress Controller | ≈ 10 days | [Source](https://konghq.com/blog/product-releases/december-2024-unauthorized-kong-ingress-controller-3-4-0-build) |
| web3.js | 5 hours | [Source](https://threats.wiz.io/all-incidents/solana-web3js-supply-chain-attack) |

(Each of these attacks has significant downstream effect, of course, but only _within_ their window of opportunity. Subsequent compromises from each, like [Shai-Hulud](https://www.wiz.io/blog/shai-hulud-npm-supply-chain-attack), represent _new_ windows of opportunity where the attackers regrouped and pivoted onto the _next_ set of compromised credentials.)

My takeaway from this: some windows of opportunity are bigger, but the _majority_ of them are under a week long. Consequently, ordinary developers can _avoid the bulk_ of these types of attacks by instituting **cooldowns** on their dependencies.

Cooldowns
---------

A “cooldown” is exactly what it sounds like: a window of time between when a dependency is published and when it’s considered suitable for use. The dependency is public during this window, meaning that “supply chain security” vendors can work their magic while the rest of us wait any problems out.

I **love** cooldowns for several reasons:

*   They’re empirically effective, per above. They won’t stop _all_ attackers, but they _do_ stymie the majority of high-visibiity, mass-impact supply chain attacks that have become more common.

*   They’re _incredibly_ easy to implement. Moreover, they’re **literally free** to implement in most cases: most people can use [Dependabot’s functionality](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/dependabot-options-reference#cooldown-), [Renovate’s functionality](https://docs.renovatebot.com/key-concepts/minimum-release-age/), or the functionality build directly into their package manager[5](https://blog.yossarian.net/2025/11/21/We-should-all-be-using-dependency-cooldowns#fn:pkgmanager).

This is how simple it is in Dependabot:

```
1
2
3
4
5
6
7
8
9
  version: 2

  # update once a week, with a 7-day cooldown
  - package-ecosystem: github-actions
    directory: /
    schedule:
      interval: weekly
    cooldown:
      default-days: 7
``` 
(Rinse and repeat for other ecosystems as needed.)

*   Cooldowns **enforce positive behavior** from supply chain security vendors: vendors are still incentivized to discover and report attacks quickly, but are _not_ as incentivized to emit volumes of blogspam about “critical” attacks on largely underfunded open source ecosystems.

Concluding / assorted thoughts
------------------------------

In the very small sample set above, 8/10 attacks had windows of opportunity of less than a week. Setting a cooldown of 7 days would have prevented the vast majority of these attacks from reaching end users (and causing knock-on attacks, which several of these were). Increasing the cooldown to 14 days would have prevented all but 1 of these attacks[6](https://blog.yossarian.net/2025/11/21/We-should-all-be-using-dependency-cooldowns#fn:apt).

Cooldowns are, obviously, **not a panacea**: some attackers _will_ evade detection, and delaying the inclusion of potentially malicious dependencies by a week (or two) does not fundamentally alter the fact that supply chain security is a _social trust_ problem, not a purely technical one. Still, an 80-90% reduction in exposure through a technique that is free and easy seems hard to beat.

Related to the above, it’s unfortunate that cooldowns aren’t baked _directly_ into more packaging ecosystems: Dependabot and Renovate are great, but _even better_ would be if the package manager itself (as the source of ground truth) could enforce cooldowns directly (including of dependencies not introduced or bumped through automated flows).

* * *

1.   The problem being, succinctly: modern software stacks are complex and opaque, with little to no difference in privilege between first-party code and third-party dependencies.[↩](https://blog.yossarian.net/2025/11/21/We-should-all-be-using-dependency-cooldowns#fnref:problem)

2.   In part because of the prevalence of long-lived, overscoped credentials. Long-lived credentials let attackers operate on their own (comfortable) timelines; this is why [Trusted Publishing](https://docs.pypi.org/trusted-publishers/) is such a useful (but not wholly sufficient) technique for reducing the attacker’s _attack staging window_.[↩](https://blog.yossarian.net/2025/11/21/We-should-all-be-using-dependency-cooldowns#fnref:gap)

3.   Filippo Valsorda has an excellent compilation of recent supply chain compromises [here](https://words.filippo.io/compromise-survey/).[↩](https://blog.yossarian.net/2025/11/21/We-should-all-be-using-dependency-cooldowns#fnref:filippo)

4.   The xz-utils attack is a significant outlier, both in its scope and the length of its window of opportunity. In this case, I’ve measured from the attacker’s first backdoored release (v5.6.0, 2024-02-24) to the time of rollback within Debian (2024-03-28).[↩](https://blog.yossarian.net/2025/11/21/We-should-all-be-using-dependency-cooldowns#fnref:outlier)

5.   For example, pnpm’s [`minimumReleaseAge`](https://pnpm.io/settings#minimumreleaseage). uv also has [`exclude-newer`](https://docs.astral.sh/uv/guides/scripts/#improving-reproducibility), although this specifies an absolute cutoff rather than a rolling cooldown.[↩](https://blog.yossarian.net/2025/11/21/We-should-all-be-using-dependency-cooldowns#fnref:pkgmanager)

6.   Notably, the only attack that would have stymied a 14-day cooldown is xz-utils, which is _also_ the most technically, logistically, and socially advanced of all of the attacks.[↩](https://blog.yossarian.net/2025/11/21/We-should-all-be-using-dependency-cooldowns#fnref:apt)

* * *