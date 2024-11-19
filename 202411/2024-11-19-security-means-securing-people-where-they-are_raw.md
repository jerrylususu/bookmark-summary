Title: Security means securing people where they are

URL Source: https://blog.yossarian.net/2024/11/18/Security-means-securing-people-where-they-are

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

_Nov 18, 2024_     Tags: [oss](https://blog.yossarian.net/tags#oss), [security](https://blog.yossarian.net/tags#security)


---------------------------------------------------------------------------------------------------------------------------

* * *

**Standard disclaimer**: These are my personal opinions, not the opinions of my employer, PyPI, or any open source I projects I participate in (either for funsies or because I’m paid to). In particular, **nothing** I write below can be interpreted to imply (_or_ imply the negation of) similar opinions by any of the above, except where explicitly stated.

**TL;DR:** If you don’t bother to read the rest of the post, here is the gloss: being serious about security at scale means **meeting users where they are**. In practice, this means deciding how to divide a **limited pool of engineering resources** such that the **largest demographic of users benefits** from a security initiative. This results in a **fundamental bias** towards institutional and pre-existing services, since the average user belongs to these institutional services and does not personally particularly care about security. Participants in open source **can and should** work to counteract this institutional bias, but doing so as a matter of **ideological purity undermines our shared security interests.**

* * *

I was ~sniped into writing~ encouraged to write this by [Seth Larson](https://sethmlarson.dev/), following voluminous public discourse about [PEP 740](https://peps.python.org/pep-0740/) and its [recently announced](https://blog.pypi.org/posts/2024-11-14-pypi-now-supports-digital-attestations/) implementation on PyPI.

Many people were concerned about decisions that went into the implementation of PEP 740 on PyPI, and expressed these these concerns in a wide variety of ways. A sampling of shpilkes, from “eminently reasonable” to “unhinged”:

*   PyPI’s sourcing of attestations from large IdPs like GitHub will result in **unfair social pressure** on projects that _do everything right but on their own infrastructure_, which includes major OSS projects that run their own Jenkins, private CI/CD, &c.
*   PyPI’s decision to enable GitHub-based attestations before others is effectively a form of **vendor bias**, and encourages the OSS community to deepen its dependency on GitHub.
    *   A sub-variant of this criticism is “intentional,” i.e. “attestations are **intended** to cause lock-in” versus “double-effect,” i.e. “there’s a **risk** of vendor dependence, but the goal itself is building out a new security feature for the ecosystem.”
        
        The former is in effect a way of accusing the people who did this work of having evil motives, while the latter is a reasonable expression that the feature didn’t _sufficiently consider_ vendor dependency.
        
*   Attestations are just plain bad™ and PyPI should go back to (weakly) tolerating long-lived PGP signing keys since, [**despite all evidence to the contrary**](https://blog.yossarian.net/2023/05/21/PGP-signatures-on-PyPI-worse-than-useless), people _swear_ that these signatures are being verified and form a security boundary _somewhere_[1](https://blog.yossarian.net/2024/11/18/Security-means-securing-people-where-they-are#fn:serious).
*   PyPI has been captured by the Micro$oft/NSA/Unit 8200 and has developed attestations to complete this year’s `$SINISTER_PLOT_TO_BACKDOOR_AND_OR_DESTROY_OPEN_SOURCE`.

These concerns range from containing reasonable (and concerning!) inferences to being nakedly factually incorrect. In the interest of establishing a factual baseline, here’s my list of priors:

1.  **Trusted Publishing is not limited to GitHub**. A persistent form of misinformation around PyPI’s support for attestations stems from misinformation about Trusted Publishing, as the layer beneath it.
    
    When Trusted Publishing was originally released on PyPI, it originally only supported GitHub. Other providers ([GitLab](https://docs.pypi.org/trusted-publishers/using-a-publisher/#gitlab-cicd), [Google Cloud](https://docs.pypi.org/trusted-publishers/using-a-publisher/#google-cloud), [ActiveState](https://docs.pypi.org/trusted-publishers/using-a-publisher/#activestate) [2](https://blog.yossarian.net/2024/11/18/Security-means-securing-people-where-they-are#fn:more)) came a few months later, but are now fully supported as Trusted Publishing providers.
    
    The reason for this approach (GitHub first, then others) had nothing to do with a sinister Microsoft plot (as was insinuated then), but instead came from the **exact same reasoning** that will be elaborated in this post: the largest demographic that stood to immediately benefit from Trusted Publishing’s usability and security benefits was on GitHub, so they were targeted first.
    
2.  **Trusted Publishing and PEP 740 are built on open standards**. More precisely, both are built on top of [OpenID Connect](https://openid.net/developers/how-connect-works/), which allows independent services to _federate_ with each other via claims that are signed with public-key cryptography.
    
    This underlying technical choice is what made onboarding GitLab, &c., relatively easy: there **was no vendor or otherwise closed dependency** that needed to be removed or replaced. This remains true to this day.
    
3.  **Adding a new Trusted Publisher and/or attestation source is not hard, but also not trivial.** Adding a new Trusted Publishing provider is _not_ as trivial as adding a well-known OIDC discovery URL to PyPI’s codebase: each new provider needs to be **reviewed** for claim contents, to ensure that the provider’s _principals_ can be distinguished from each other in a way that PyPI can model.
    
    In other words: it would be **catastrophic** for PyPI to support an OIDC IdP that can’t distinguish between its users, or permitted claim malleability such that users could impersonate each other.
    
    Ensuring that each accepted IdP meets these conditions requires a **nontrivial time commitment** that gets balanced against the expected real-world usage of a given IdP: an IdP with one-to-few users is not worth the tradeoff in review time.
    
4.  **Not everything makes sense as a Trusted Publisher/attestation provider**. As a corollary to the point above: it doesn’t make sense (for either PyPI, or individual project maintainers) to attempt to do _all_ package uploading via Trusted Publishing. OIDC fundamentally benefits from scale, and it doesn’t make sense (in terms of operational complexity[3](https://blog.yossarian.net/2024/11/18/Security-means-securing-people-where-they-are#fn:complexity) and diminished rewards[4](https://blog.yossarian.net/2024/11/18/Security-means-securing-people-where-they-are#fn:rewards)) for every individual maintainer to run their own OIDC IdP.
    
5.  **Neither Trusted Publishing nor PEP 740 _increases_ trust in an already-used CI/CD provider.** This one can be a little unintuitive, but it follows from existing workflows: if you were **already** using GitHub/GitLab/&c. to publish with a plain old API token, then you were **already** trusting your CI/CD provider to securely store that credential (and only use it when _you_ want it used).
    
    In a broader sense, Trusted Publishing and PEP 740 _reduce_ unnecessary trust in the CI/CD provider, since they force the provider to make a **publicly auditable and verifiable claim** in order to receive a _temporary_ API token.
    

This is the baseline, as I see it. Now let’s talk a bit about why PyPI’s initial attestations rollout focused on GitHub (like what happened with Trusted Publishing), and why it was (1) not a conspiracy, and (2) the **strategic thing to do**. I’ll then end with some thoughts on how we can better address the **unfair social pressure** case.

You[5](https://blog.yossarian.net/2024/11/18/Security-means-securing-people-where-they-are#fn:you) can’t force people to care about security
--------------------------------------------------------------------------------------------------------------------------------------------

**And they shouldn’t have to care.** This is the hard truth beneath everything else: most open source maintainers are not security experts (they’re experts in _other things_, like the projects they maintain), and they don’t want to _become_ security experts. Security **is a hump that people get over** while attempting to achieve their actual goals.

At the same time, expectations change over time: MFA was a relative rarity a decade ago, and is now mandatory across a wide swath of popular OSS-adjacent services (or mandatory for demographic subsets, such as “critical” package maintainers on NPM and RubyGems).

This sets up a **fundamental tension**: most maintainers want to just keep doing whatever has always worked, while security is a _moving target_ that sometimes requires universal change.

There aren’t many ways to eliminate this tension, but there are (at least) two ways to _ameliorate_ it:

1.  **Make security features into usability features.** This was one of the core objectives behind Trusted Publishing’s design: users found the experience of context-switching between PyPI and their CI/CD frustrating, so we found a way to **eliminate those context switches** while improving the security of the credentials involved.
2.  **Delegate some (if not all) responsibility for security to services.** The reasoning behind this is intuitive: big services have **both the staff _and_ the financial incentive** to maintain a strong default security posture, as well as keep up with the latest changes in baseline security expectations. This, too, has a usability angle: it’s **just plain easier**[6](https://blog.yossarian.net/2024/11/18/Security-means-securing-people-where-they-are#fn:personal) to maintain a project when an external service hums along and provides source control, CI/CD, release management, &c. for you.

For the Python ecosystem, in 2024, that service is _overwhelmingly_ GitHub.

GitHub is the current watering hole
-----------------------------------

The history of open source on the public internet has long favored a small and stable (but not static), group of watering holes at which the **overwhelming majority** of projects concentrate.

Past watering holes include [SourceForge](https://sourceforge.net/) and [Google Code](https://code.google.com/archive/), along with specialized project hosts like [Savannah](https://savannah.gnu.org/).

Today, that watering hole is GitHub. Using [last week’s `pypi-data` dump](https://github.com/sethmlarson/pypi-data/releases/tag/2024.11.14):

```
1
2
3
4
5
6
7
8
sqlite> SELECT COUNT(DISTINCT package_name)
        FROM package_urls
        WHERE public_suffix = 'github.com';
378613
sqlite> SELECT COUNT(DISTINCT package_name) FROM package_urls;
447148
sqlite> SELECT COUNT(*) FROM packages;
566404
```

Of the 447,148 packages that have URLs[7](https://blog.yossarian.net/2024/11/18/Security-means-securing-people-where-they-are#fn:total), a full 378,613 list `github.com` in their metadata. That’s **84.7%** of all projects that list URLs in their metadata.

By contrast, here are the next 10 most popular hosts:

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
10
11
12
13
14
15
sqlite> SELECT public_suffix, COUNT(DISTINCT package_name) AS cnt
        FROM package_urls
        GROUP BY public_suffix ORDER BY cnt DESC
        LIMIT 11;
github.com|378613
gitlab.com|8923
python.org|6012
bitbucket.org|5177
pythonhosted.org|3588
pypi.org|3325
saythanks.io|3247
gitee.com|1375
ya.ru|1274
google.com|1208
headfirstlabs.com|1047
```

The drop-off is stark: GitLab is #2, but with only **1.99%** of all projects[8](https://blog.yossarian.net/2024/11/18/Security-means-securing-people-where-they-are#fn:significant).

This tells an important baseline story: if PyPI builds a security feature that _needs_ to interoperate with source forges or CI/CD providers, then **overwhelming majority of its packages** can be best served by starting with GitHub.

That doesn’t mean that PyPI should _stop_ with just GitHub, or GitHub plus GitLab, or anything else of the sort. It just tells us **where the starting point should be**.

The bottom line
---------------

This _finally_ gets us to the point of this post:

1.  Most maintainers (reasonably!) don’t _especially_ care about security and, as a corollary, have selected infrastructure and services that compartmentalize most of the boring, operational aspects of open source security (like maintaining a set of trusted committers and a secure CI/CD);
2.  GitHub is _overwhelmingly_ the target of that selection process.

The conclusion: if a new feature needs to interact with services outside of PyPI itself, then the _purely practical_ course to take is to start with the services that will yield the most immediate benefit to the Python community.

Does PyPI have a responsibility to (try and) move the watering hole?
--------------------------------------------------------------------

A recurring strain of thought in conversations around PEP 740 (and centralized infrastructure more generally) is whether the ethics of open source impute a similar ethic[9](https://blog.yossarian.net/2024/11/18/Security-means-securing-people-where-they-are#fn:which) of independence and decentralization.

Or in other words: does PyPI (or OSS more generally) have a responsibility to try and avoid corporate-associated integrations?

I would argue **no**: PyPI’s primary responsibility is to the community that uses it, both upstream and downstream, and that community is **best served** by using _open standards_ to interoperate with the services the community **overwhelmingly uses**.

This does **not** however imply that PyPI _should_ ignore smaller opportunities for integration, such as adding Trusted Publishing providers for independent GitLab hosts with large user bases, or [Codeberg](https://codeberg.org/) instances, or anything else.

On the contrary: **I would like to see PyPI integrate more** of these as Trusted Publishing providers, _provided_ that the usage statistics and operational complexity for each **actually benefit** the community as a whole. Enrolling a few thousand projects on a single self-hosted forge would be great; having to review dozens of forges with under a dozen users would not be. I would like to see a similar thing occur for attestations.

In sum: PyPI shouldn’t (and doesn’t) pick winners, but it should (and does) pick battles to fight **and the order in which it fights them**.

There’s a flip side to all of this: despite effusive attempts to emphasize that attestations are **not** a “trusted bit” and that consumers shouldn’t treat them as a signal of package quality or security, we are **almost certainly** going to see people (and companies[10](https://blog.yossarian.net/2024/11/18/Security-means-securing-people-where-they-are#fn:supply)) do exactly that.

In practice, that means that maintainers who **do everything right but not in a way that’s currently legible to the attestations feature** are going to receive annoying emails, issues, &c. asking them why they’re “less secure”[11](https://blog.yossarian.net/2024/11/18/Security-means-securing-people-where-they-are#fn:secure) than other packages.

In the medium term, I think the way to address this is to:

1.  Support email identities for attestations, since PyPI already has a notion of “verified” email to cross-check attestations against.
2.  Continue to widen the number of Trusted Publishing providers and enable attestation support for each, within reason.

Those two, combined, should address the _overwhelming majority of the remainder_: people who can’t (or simply don’t want to) use Trusted Publishing, and those who do but can’t yet. I’ll be working on those.

* * *

* * *

Discussions: [Mastodon](https://infosec.exchange/@yossarian/113504719158109951) [Reddit](https://reddit.com/r/enosuchblog/comments/1gu7mkf/security_means_securing_people_where_they_are/) [Bluesky](https://bsky.app/profile/yossarian.net/post/3lbab4ffrsh2n)

* * *
