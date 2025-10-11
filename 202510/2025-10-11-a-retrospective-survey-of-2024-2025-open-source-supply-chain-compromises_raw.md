Title: A Retrospective Survey of 2024/2025 Open Source Supply Chain Compromises

URL Source: https://words.filippo.io/compromise-survey/

Published Time: 2025-10-10T14:33:11.841216Z

Markdown Content:
Lack of memory safety is such a predominant cause of security issues that we have a responsibility as professional software engineering to robustly mitigate it in security-sensitive use cases—by using memory safe languages.

Similarly, I have the growing impression that software supply chain compromises have a few predominant causes which we might have a responsibility as a professional open source maintainers to robustly mitigate.

To test this impression and figure out any such mitigations, I collected all 2024/2025 open source supply chain compromises I could find, and categorized their root cause. (If you find more, do email me!)

Since I am interested in mitigations we can apply as maintainers of depended-upon projects to avoid compromises, I am ignoring: intentionally malicious packages (e.g. typosquatting), issues in package managers (e.g. internal name shadowing), open source infrastructure abuse (e.g. using package registries for post-compromise exfiltration), and isolated app compromises (i.e. not software that is depended upon).

Also, I am specifically interested in how an attacker got their first unauthorized access, not in what they did with it. Annoyingly, there is usually a lot more written about the latter than the former.

2024/2025 Open Source Supply Chain Compromises
----------------------------------------------

In no particular order, but kind of grouped.

[XZ Utils](https://en.wikipedia.org/wiki/XZ_Utils_backdoor)

 Long term pressure campaign on the maintainer to hand over access.

**Root cause**: control handoff.

 Contributing factor: non-reproducible release artifacts.

[Nx S1ingularity](https://nx.dev/blog/s1ngularity-postmortem)

 Shell injection in GitHub Action with `pull_request_target` trigger and unnecessary read/write permissions[4](https://words.filippo.io/compromise-survey/#fn:1), used to extract a npm token.

**Root cause**: pull_request_target.

 Contributing factors: read/write CI permissions, long-lived credential exfiltration, post-install scripts.

[Shai-Hulud](https://www.wiz.io/blog/shai-hulud-npm-supply-chain-attack)

 Worm behavior by using compromised npm tokens to publish packages with malicious post-install scripts, and compromised GitHub tokens to publish malicious GitHub Actions workflows.

**Root cause**: long-lived credential exfiltration.

 Contributing factor: post-install scripts.

[npm debug/chalk/color](https://news.ycombinator.com/item?id=45169794)

 Maintainer phished with an “Update 2FA Now” email. Had TOTP 2FA enabled.

**Root cause**: phishing.

[polyfill.io](https://tag-security.cncf.io/community/catalog/compromises/2024/polyfill/)

 Attacker purchased CDN domain name and GitHub organization.

**Root cause**: control handoff.

[MavenGate](https://blog.oversecured.com/Introducing-MavenGate-a-supply-chain-attack-method-for-Java-and-Android-applications/)

 Expired domains and changed GitHub usernames resurrected to take control of connected packages.

**Root causes**: domain resurrection, username resurrection.

[reviewdog and tj-actions/changed-files](https://www.wiz.io/blog/new-github-action-supply-chain-attack-reviewdog-action-setup)

 Contributors deliberately granted automatic write access for GitHub Action repository[5](https://words.filippo.io/compromise-survey/#fn:2). Malicious tag re-published to compromise GitHub PAT of more popular GitHub Action[6](https://words.filippo.io/compromise-survey/#fn:3).

**Root cause**: control handoff.

 Contributing factors: read/write CI permissions, long-lived credential exfiltration, mutable GitHub Actions tags.

[Ultralytics](https://blog.yossarian.net/2024/12/06/zizmor-ultralytics-injection)

 Shell injection in GitHub Action with `pull_request_target` trigger (which required read/write permissions), pivoted to publishing pipeline via GitHub Actions cache poisoning. Compromised again later using an exfiltrated PyPI token.

**Root cause**: pull_request_target.

 Contributing factors: GitHub Actions cache poisoning, long-lived credential exfiltration.

[Kong Ingress Controller](https://konghq.com/blog/product-releases/december-2024-unauthorized-kong-ingress-controller-3-4-0-build)

 GitHub Action with `pull_request_target` trigger restricted to trusted users but bypassed via Dependabot impersonation[7](https://words.filippo.io/compromise-survey/#fn:4), previously patched but still available on old branch. GitHub PAT exfiltrated and used.

**Root causes**: pull_request_target, Dependabot impersonation.

 Contributing factors: per-branch CI configuration, long-lived credential exfiltration.

[Rspack](https://github.com/web-infra-dev/rspack/releases/tag/v1.1.8)

 Pwn request[1](https://words.filippo.io/compromise-survey/#fn:pwn) against `issue_comment` workflow[2](https://words.filippo.io/compromise-survey/#fn:workflow) in other project, leading to a GitHub classic token of a maintainer with permissions to the web-infra-dev organization[8](https://words.filippo.io/compromise-survey/#fn:5) (kindly confirmed via email by the Rspack Team). Similar to previously reported and fixed vulnerability[3](https://words.filippo.io/compromise-survey/#fn:prev) in the Rspack repository.

**Root causes**: issue_comment.

 Contributing factor: long-lived credential exfiltration.

[eslint-config-prettier](https://github.com/prettier/eslint-config-prettier/issues/339)

 “Verify your account”[9](https://words.filippo.io/compromise-survey/#fn:6) npm phishing.

**Root cause**: phishing.

[num2words](https://blog.pypi.org/posts/2025-07-31-incident-report-phishing-attack/)

 “Email verification” PyPI phishing.

**Root cause**: phishing.

[@solana/web3.js](https://xcancel.com/0xMert_/status/1864069157257613719)

 A “phishing attack on the credentials for publishing npm packages.”

**Root cause**: phishing.

[rustfoundation.dev](https://blog.rust-lang.org/2025/09/12/crates-io-phishing-campaign/)

 Fake compromise remediation[10](https://words.filippo.io/compromise-survey/#fn:7) Crates.io phishing. Unclear if successful.

**Root cause**: phishing.

[React Native ARIA & gluestack-ui](https://gluestack.io/blogs/public-incident-report)

 “[U]nauthorized access to publishing credentials.” Colorful and long Incident Report lacks any details on “sophisticated” entry point. Presumably an exposed npm token.

**Root cause**: long-lived credential exfiltration(?).

[lottie-player](https://github.com/LottieFiles/lottie-player/issues/254#issuecomment-2448993225)

 Unclear, but mitigation involved “remov[ing] all access and associated tokens/services accounts of the impacted developer.”

**Root cause**: long-lived credential exfiltration(?) or control handoff(?).

[rand-user-agent](https://www.aikido.dev/blog/catching-a-rat-remote-access-trojian-rand-user-agent-supply-chain-compromise)

 Unclear. Malicious npm versions published, affected company seems to have deleted the project. Presumably npm token compromise.

**Root cause**: long-lived credential exfiltration(?).

[DogWifTool](https://www.bleepingcomputer.com/news/security/solana-pumpfun-tool-dogwiftool-compromised-to-drain-wallets/)

 GitHub token extracted from distributed binary.

**Root cause**: long-lived credential exfiltration.

Summary of vectors and mitigations
----------------------------------

### Phishing (5 root)

Surprising no one, the most popular confirmed initial compromise vector is phishing. It works against technical open source maintainers. It works against 2FA TOTP. It. Works. It is also very fixable.

It’s 2025 and every professional open source maintainer should be using phishing-resistant authentication (passkeys or WebAuthn 2FA) on all developer accounts, and accounts upstream of them.

Upstream accounts include email, password manager, passkey sync (e.g. Apple iCloud), web/DNS hosting, and domain registrar.

Some services, such as GitHub, require a phishable 2FA method along with phishing-resistant ones. In that case, the best option is to enable TOTP, and delete the secret or write it down somewhere safe and never ever use it—effectively disabling it. This does _not_ work with SMS, since SIM jacking is possible even without action by the victim.

### Control handoff (3+1? root)

Actually surprisingly—to me—a number of compromises are due to, effectively, giving access to the attacker.

This is a nuanced people issue. The solution is obviously “don’t do that” but that really reduces to the decades-old issue of open source maintenance sustainability. In a sense, since this analysis is aimed at professional maintainers who can afford it, control handoff is easily avoided by not doing it.

### pull_request_target and issue_comment (4 root)

Kind of incredible that a specific feature has a top 3 spot, but projects get compromised by “pwn requests” all the time.

The `pull_request_target` workflow trigger runs privileged CI with a context full of attacker-controlled data in response to pull requests. It makes a meek attempt to be safer by not checking out the attacker’s code, instead checking out the upstream target. That’s empirically not enough, with shell injection attacks causing multiple severe compromises.

The [zizmor](https://zizmor.sh/) static analyzer can help detect injection vulnerabilities, but it seems clear that `pull_request_target` is unsafe at any speed, and should just never be used.

Other triggers that run privileged with attacker-controlled context should be avoided for the same reason. The Rspack compromise, for example, was due to checking out attacker-controlled code on an `issue_comment` trigger if the PR receives a comment.

```
on:
  issue_comment:
    types: [created]
jobs:
  issue_comment:
    if: github.event.issue.pull_request && contains(github.event.comment.body, '!canary')
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
        with:
          ref: refs/pull/${{ github.event.issue.number }}/head
```

What are the alternatives?

*   One option is to implement an external service in a language that can safely deal with untrusted inputs (i.e. not YAML’d shell), and use webhooks. That unfortunately requires long-lived credentials (see below).
*   GitHub itself [recommends](https://securitylab.github.com/resources/github-actions-preventing-pwn-requests/) using the unprivileged `pull_request` trigger followed by the `workflow_run` trigger, but it’s unclear to me how safer that would actually be against injection attacks.
*   Finally, since two out of three compromises were due to shell injection, it might be safer to use a proper programming language, like JavaScript with [actions/github-script](https://github.com/actions/github-script), or any other language accessing the context via environment variables instead of YAML interpolation. This means not using any third-party actions, as well.
*   Allowlisting actors and read-only steps are not robust mitigations, see _Read/write CI permissions_ and _Dependabot impersonation_ below.

Overall, none of the mitigations are particularly satisfactory, so the solution might be simply to eschew features that require `pull_request_target` and other privileged attacker-controlled triggers. (To be honest, I am not a fan of chatty bots on issues and PRs, so I never needed them.)

### Long-lived credential exfiltration (2+3? root, 5 contributing)

Attackers love to steal tokens. There is no universal solution, but it’s so predominant that we can consider piecemeal solutions.

Long-lived credentials are only a root cause when they are accidentally exposed. Otherwise, they are a secondary compromise mechanism for lateral movement or persistence, after the attacker got privileged code execution. Mitigating the latter is somewhat less appealing because an attacker with code execution can find more creative ways to carry out an attack, but we can prune some low-hanging fruit.

Go removes the need for package registry tokens by simply not having accounts. (Instead, the go command fetches modules directly from VCS, with caching by the Go Modules Proxy and universality and immutability guaranteed by the Go Checksum Database.) In other ecosystems Trusted Publishing replaces long-lived private tokens with short-lived OIDC tokens, although there is no way to down-scope the capabilities of an OIDC token.

GitHub Personal Access Tokens are harder to avoid for anything that’s not supported by GitHub Actions permissions. Chainguard has [a third-party Security Token Service that trades OIDC tokens for short-lived tokens](https://www.chainguard.dev/unchained/the-end-of-github-pats-you-cant-leak-what-you-dont-have), and their article has a good list of cases in which PATs end up otherwise necessary. Given the risk, it might be worth giving up on non-critical features that would require powerful tokens.

Gerrit “git cookies” (which are actually just OAuth refresh tokens for the Gerrit app) can be replaced with… well, OAuth refresh tokens but kept in memory instead of disk, using [git-credential-oauth](https://github.com/hickford/git-credential-oauth). They can also be stored a little more safely in the platform keychain by treating them as an HTTP password, although that’s [not well documented](https://github.com/golang/go/issues/73761).

In the long term, it would be great to see the equivalent of [Device Bound Session Credentials](https://github.com/w3c/webappsec-dbsc) for developer and automated workflows.

### Dependabot impersonation (1 root)

Turns out [you can just exfiltrate a token from a GitHub Actions runner to impersonate Dependabot with arbitrary PRs](https://www.synacktiv.com/publications/github-actions-exploitation-dependabot)???

I guess! Fine! Just don’t allowlist Dependabot. Not sure what a deeper meta-mitigation that didn’t require knowing this factoid would have been.

### Domain and username resurrection (1 root)

Multiple ecosystems (Go and Maven, for example) are vulnerable to name takeovers, whether expired domain names or changed GitHub user/org names. The new owner of the name gets to publish updates for that package.

From the point of view of the maintainer, the mitigation is just not to change GitHub names (at least without registering the old one), and to register critical domains for a long period, with expiration alerting.

### Read/write CI permissions (0 root, 2 contributing)

Some CI compromises happened in contexts that could or should have been read-only. It _sounds_ like giving GitHub Actions workflows only read permissions like `contents: read` should be a robust mitigation for any compromise of the code they run.

Unfortunately, and kind of incredibly, even a read-only workflow is handed a token that can write to the cross-workflow cache for any key. This cache is then used implicitly by a number of official actions, allowing cross-workflow escalation by [**GitHub Actions cache poisoning**](https://adnanthekhan.com/2024/05/06/the-monsters-in-your-build-cache-github-actions-cache-poisoning/).

This contradicts some of GitHub’s own recommendations, and makes the existence of a setting to make GitHub Actions read-only by default more misleading than useful.

The behavior does not extend to regular `pull_request` triggers, which are actually read-only (otherwise anyone could poison caches with a PR). GitHub simply doesn’t seem to offer a way to opt in to it.

I can see no robust mitigation in the GitHub ecosystem. I would love to be wrong, this is maddening.

### Post-install scripts (0 root, 2 contributing)

Two compromises propagated by injecting npm post-install scripts, to obtain code execution as soon as a dependency was installed.

This can be disabled with

```
npm config set ignore-scripts true
```

which is worth doing for defense in depth. However, it’s only useful if the dependency is not going to be executed in a privileged context, e.g. to run tests in Node.js.

Go, unlike most ecosystems, considers code execution during fetch _or compilation_ to be a security vulnerability, so has this safety margin by default.

### Non-reproducible release artifacts (0 root, 1 contributing)

The XZ backdoor was hidden in a release artifact that didn’t match the repository source. It would be great if that was more detectable, in the form of reproducible artifacts.

The road to a fail-closed world where systems automatically detect non-reproducing artifacts is still long, though.

### Mutable GitHub Actions tags (0 root, 1 contributing)

How supply chain attacks usually work these days is that an attacker gets the ability to publish new versions for a package, publishes a malicious version, and waits for dependents to update (maybe with the help of Dependabot) or install the latest version ex novo.

Not with GitHub Actions! The recommended and most common way to refer to a GitHub Action is by its major version, which is resolved to a git tag that is _expected to change arbitrarily_ when new versions are published. This means that an attacker can instantly compromise every dependent workflow.

This was an unforced error already in 2019, when GitHub Actions launched while Go had already shipped an immutable package system. This has been [discussed many times since](https://research.swtch.com/npm-colors) and most other ecosystems have improved somewhat. A roadmap item for immutable Actions [has been silent since 2022](https://github.com/github/roadmap/issues/592). The new [immutable releases](https://docs.github.com/en/code-security/supply-chain-security/understanding-your-software-supply-chain/immutable-releases) feature doesn’t apply to non-release tags, and the GitHub docs [still recommend changing tags](https://docs.github.com/en/actions/how-tos/create-and-publish-actions/using-immutable-releases-and-tags-to-manage-your-actions-releases) for Actions.

As maintainers, we can opt in to pinning where it’s somehow still not the default. For GitHub Actions, that means using unreadable commit hashes, which can be somewhat ameliorated with [tooling](https://github.com/suzuki-shunsuke/pinact). For npm, it means using `npm ci` instead of `npm install`.

### Per-branch CI configuration (0 root, 1 contributing)

One compromise was due to a vulnerability that was already fixed, but had persisted on an old branch. Any time we make a security improvement (including patching a vulnerable Action) on a GitHub Actions workflow, we need to remember to cherry-pick it to all branches, including stale ones.

Can’t think of a good mitigation, just yet another sharp edge of GitHub Actions you need to be aware of, I suppose.

Summary
-------

There are a number of useful mitigations, but the ones that appear to be as clearly a professional responsibility as memory safety are

1.   phishing-resistant authentication;
2.   not handing over access to attackers; and
3.   avoiding privileged attacker-controlled GitHub Actions triggers (e.g. `pull_request_target`).

This research was part of an effort to compile a [Geomys](https://geomys.org/) Standard of Care that amongst other things mitigates the most common security risks to the projects we are entrusted with. We will publish and implement it soon, to keep up to date follow me on Bluesky at [@filippo.abyssdomain.expert](https://bsky.app/profile/filippo.abyssdomain.expert) or on Mastodon at [@filippo@abyssdomain.expert](https://abyssdomain.expert/@filippo).

The Picture
-----------

On Saturday, between 250,000 and 1,000,000 people (depending on who you believe, 0.4–1.7% of the whole population of Italy) took part in a demonstration against the genocide unfolding in Gaza. Anyway, here’s a picture of the Archbasilica of San Giovanni in Laterano at the end of the march.

![Image 1: A large basilica is set against a dusk sky, with pink clouds. A crowd is visible at the bottom of the picture, with Palestinian and other red flags.](https://assets.buttondown.email/images/8fc19fa4-3874-4bce-a8ee-9620a86966fb.jpeg?w=960&fit=max)

My work is made possible by [Geomys](https://geomys.org/), an organization of professional Go maintainer, which is funded by [Smallstep](https://smallstep.com/), [Ava Labs](https://www.avalabs.org/), [Teleport](https://goteleport.com/), [Tailscale](https://tailscale.com/), and [Sentry](https://sentry.io/). Through our retainer contracts they ensure the sustainability and reliability of our open source maintenance work and get a direct line to my expertise and that of the other Geomys maintainers. (Learn more in the [Geomys announcement](https://words.filippo.io/geomys).)

Here are a few words from some of them!

Teleport — For the past five years, attacks and compromises have been shifting from traditional malware and security breaches to identifying and compromising valid user accounts and credentials with social engineering, credential theft, or phishing. [Teleport Identity](https://goteleport.com/platform/identity/?utm=filippo) is designed to eliminate weak access patterns through access monitoring, minimize attack surface with access requests, and purge unused permissions via mandatory access reviews.

Ava Labs — We at [Ava Labs](https://www.avalabs.org/), maintainer of [AvalancheGo](https://github.com/ava-labs/avalanchego) (the most widely used client for interacting with the [Avalanche Network](https://www.avax.network/)), believe the sustainable maintenance and development of open source cryptographic protocols is critical to the broad adoption of blockchain technology. We are proud to support this necessary and impactful work through our ongoing sponsorship of Filippo and his team.

* * *

1.   [https://github.com/module-federation/core/pull/3324](https://github.com/module-federation/core/pull/3324)[↩](https://words.filippo.io/compromise-survey/#fnref:pwn "Jump back to footnote 1 in the text")

2.   [https://github.com/module-federation/core/tree/c3aff14a4b9de2588122ec24cf456dc1fdd742f0/.github/workflows](https://github.com/module-federation/core/tree/c3aff14a4b9de2588122ec24cf456dc1fdd742f0/.github/workflows)[↩](https://words.filippo.io/compromise-survey/#fnref:workflow "Jump back to footnote 2 in the text")

3.   [https://www.praetorian.com/blog/compromising-bytedances-rspack-github-actions-vulnerabilities/](https://www.praetorian.com/blog/compromising-bytedances-rspack-github-actions-vulnerabilities/)[↩](https://words.filippo.io/compromise-survey/#fnref:prev "Jump back to footnote 3 in the text")

4.   [https://github.com/nrwl/nx/security/advisories/GHSA-cxm3-wv7p-598c#:~:text=20%20AM%20EDT-,Attack%20Vector,-Vulnerable%20Workflow](https://github.com/nrwl/nx/security/advisories/GHSA-cxm3-wv7p-598c#:~:text=20%20AM%20EDT-,Attack%20Vector,-Vulnerable%20Workflow)[↩](https://words.filippo.io/compromise-survey/#fnref:1 "Jump back to footnote 4 in the text")

5.   [https://github.com/reviewdog/reviewdog/issues/2079](https://github.com/reviewdog/reviewdog/issues/2079)[↩](https://words.filippo.io/compromise-survey/#fnref:2 "Jump back to footnote 5 in the text")

6.   [https://github.com/tj-actions/changed-files/issues/2464#issuecomment-2727020537](https://github.com/tj-actions/changed-files/issues/2464#issuecomment-2727020537)[↩](https://words.filippo.io/compromise-survey/#fnref:3 "Jump back to footnote 6 in the text")

7.   [https://www.synacktiv.com/publications/github-actions-exploitation-dependabot](https://www.synacktiv.com/publications/github-actions-exploitation-dependabot)[↩](https://words.filippo.io/compromise-survey/#fnref:4 "Jump back to footnote 7 in the text")

8.   [https://github.com/web-infra-dev/rspack/issues/8767#issuecomment-2563345582](https://github.com/web-infra-dev/rspack/issues/8767#issuecomment-2563345582)[↩](https://words.filippo.io/compromise-survey/#fnref:5 "Jump back to footnote 8 in the text")

9.   [https://github.com/prettier/eslint-config-prettier/issues/339#issuecomment-3090304490](https://github.com/prettier/eslint-config-prettier/issues/339#issuecomment-3090304490)[↩](https://words.filippo.io/compromise-survey/#fnref:6 "Jump back to footnote 9 in the text")

10.   [https://github.com/rust-lang/crates.io/discussions/11889#discussion-8886064](https://github.com/rust-lang/crates.io/discussions/11889#discussion-8886064)[↩](https://words.filippo.io/compromise-survey/#fnref:7 "Jump back to footnote 10 in the text")