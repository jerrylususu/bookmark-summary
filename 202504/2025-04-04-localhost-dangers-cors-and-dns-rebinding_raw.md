Title: Localhost dangers: CORS and DNS rebinding

URL Source: https://github.blog/security/application-security/localhost-dangers-cors-and-dns-rebinding/

Published Time: 2025-04-03T16:00:24+00:00

Markdown Content:
At [GitHub Security Lab](https://securitylab.github.com/), one of the most common vulnerability types we find relates to the cross-origin resource sharing (CORS) mechanism. CORS allows a server to instruct a browser to permit loading resources from specified origins other than its own, such as a different domain or port.

Many developers change their CORS rules because users want to connect to third party sites, such as payment or social media sites. However, developers often don’t fully understand the dangers of changing the same-origin policy, and they use unnecessarily broad rules or faulty logic to prevent users from filing further issues.

In this blog post, we’ll examine some case studies of how a broad or faulty CORS policy led to dangerous vulnerabilities in open source software. We’ll also discuss DNS rebinding, an attack with similar effects to a CORS misconfiguration that’s not as well known among developers.

What is CORS and how does it work?[](https://github.blog/security/application-security/localhost-dangers-cors-and-dns-rebinding/#what-is-cors-and-how-does-it-work)
--------------------------------------------------------------------------------------------------------------------------------

CORS is a way to allow websites to communicate with each other directly by bypassing the [same-origin policy](https://developer.mozilla.org/en-US/docs/Web/Security/Same-origin_policy), a security measure that restricts websites from making requests to a different domain than the one that served the web page. Understanding the `Access-Control-Allow-Origin` and `Access-Control-Allow-Credentials` [response headers](https://developer.mozilla.org/en-US/docs/Glossary/Response_header) is crucial for correct and secure CORS implementation.

`Access-Control-Allow-Origin` is the list of origins that are allowed to make cross site requests and read the response from the webserver. If the `Access-Control-Allow-Credentials` header is set, the browser is also allowed to send credentials (cookies, http authentication) if the origin requests it. Some requests are considered simple requests and do not need a CORS header in order to be sent cross-site. This includes the GET, POST, and HEAD requests with content types restricted to `application/x-www-form-urlencoded`, `multipart/form-data`, and `text/plain`. When a third-party website needs access to account data from your website, adding a concise CORS policy is often one of the best ways to facilitate such communication.

To implement CORS, developers can either manually set the `Access-Control-Allow-Origin` header, or they can utilize a CORS framework, such as [_RSCors_](https://github.com/rs/cors), that will do it for them. If you choose to use a framework, make sure to read the documentation—don’t assume the framework is safe by default. For example, if you tell the CORS library you choose to reflect all origins, does it send back the response with a blanket pattern matching star (\*) or a response with the actual domain name (e.g., stripe.com)?

Alternatively, you can create a custom function or middleware that checks the origin to see whether or not to send the `Access-Control-Allow-Origin` header. The problem is, you can make some security mistakes when rolling your own code that well-known libraries usually mitigate.

Common mistakes when implementing CORS[](https://github.blog/security/application-security/localhost-dangers-cors-and-dns-rebinding/#common-mistakes-when-implementing-cors)
--------------------------------------------------------------------------------------------------------------------------------

For example, when comparing the origin header with the allowed list of domains, developers may use the string comparison function equivalents of `startsWith`, `exactMatch`_,_ and `endsWith` functions for their language of choice. The safest function is `exactMatch` where the domain must match the allow list exactly. However, what if _payment.stripe.com_ wants to make a request to our backend instead of _stripe.com_? To get around this, we’d have to add every subdomain to the allow list. This would inevitably cause users frustration when third-party websites change their APIs.

Alternatively, we can use the `endsWith` function. If we want connections from Stripe, let’s just add _stripe.com_ to the allowlist and use `endsWith` to validate and call it a day. Not so fast, since the domain _attackerstripe.com_ is now **also** valid. We can tell the user to only add full urls to the allowlist, such as [_https://stripe.com_](https://stripe.com/), but then we have the same problem as `exactMatch`.

We occasionally see developers using the `startsWith` function in order to validate domains. This also doesn’t work. If the allowlist includes _[https://stripe.com](https://stripe.com/)_ then we can just do _[https://stripe.com.attacker.com](https://stripe.com.attacker.com/)_.

For any origin with subdomains, we must use _.stripe.com_ (notice the extra period) in order to ensure that we are looking at a subdomain. If we combine `exactMatch` for second level domains and `endsWith` for subdomains, we can make a secure validator for cross site requests.

Lastly, there’s one edge case found in CORS: the null origin should never be added to allowed domains. The null origin can be hardcoded into the code or added by the user to the allowlist, and it’s used when requests come from a file or from a privacy-sensitive context, such as a redirect. However, it can also come from a sandboxed iframe, which an attacker can include in their website. For more practice attacking a website with null origin, check out this [CORS vulnerability with trusted null origin exercise](https://portswigger.net/web-security/cors/lab-null-origin-whitelisted-attack) in the Portswigger Security Academy.

How can attackers exploit a CORS misconfiguration?[](https://github.blog/security/application-security/localhost-dangers-cors-and-dns-rebinding/#how-can-attackers-exploit-a-cors-misconfiguration)
--------------------------------------------------------------------------------------------------------------------------------

CORS issues allow an attacker to make actions on behalf of the user when a web application uses cookies (with `SameSite None`) or HTTP basic authentication, since the browser must send those requests with the required authentication.

Fortunately for users, Chrome has defaulted cookies with no `Samesite` to `SameSite Lax`, which has made CORS misconfiguration useless in most scenarios. However, Firefox and Safari are still vulnerable to these issues using [bypass techniques found by PTSecurity](https://swarm.ptsecurity.com/bypassing-browser-tracking-protection-for-cors-misconfiguration-abuse/), whose research we highly recommend reading for knowing how someone can exploit CORS issues.

What impact can a CORS misconfiguration have?[](https://github.blog/security/application-security/localhost-dangers-cors-and-dns-rebinding/#what-impact-can-a-cors-misconfiguration-have)
--------------------------------------------------------------------------------------------------------------------------------

CORS issues can give a user the power of an administrator of a web application, so the usefulness depends on the application. In many cases, administrators have the ability to execute scripts or binaries on the server’s host. These relaxed security restrictions allow attackers to get remote code execution (RCE) capabilities on the server host by convincing administrators to visit an attacker-owned website.

CORS issues can also be chained with other vulnerabilities to increase their impact. Since an attacker now has the permissions of an administrator, they are able to access a broader range of services and activities, making it more likely they’ll find something vulnerable. Attackers often focus on vulnerabilities that affect the host system, such as arbitrary file write or RCE.

Real-world examples[](https://github.blog/security/application-security/localhost-dangers-cors-and-dns-rebinding/#real-world-examples)
--------------------------------------------------------------------------------------------------------------------------------

### A CORS misconfiguration allows for RCE[](https://github.blog/security/application-security/localhost-dangers-cors-and-dns-rebinding/#a-cors-misconfiguration-allows-for-rce)

Cognita is a Python project that allows users to test the retrieval-augmented generation (RAG) ability of LLM models. If we look at how it used to call the FastAPI CORS middleware, we can see it used an unsafe default setting, with `allow_origins` set to `all` and `allow_credentials` set to `true`. Usually if the browser receives `Access-Control-Allow-Origin: *` and `Access-Control-Allow-Credentials: true`, the browser knows not to send credentials with the origin, since the application did not reflect the actual domain, just a wildcard.

```
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

However, FastAPI CORS middleware is unsafe by default and setting these two headers like this resulted in the origin being reflected along with credentials.

Currently, Cognita does not have authentication, but if its developers implemented authentication without fixing the CORS policy, their authentication could be bypassed. As it stands, any website can send arbitrary requests to any endpoint in Cognita, as long as they know how to access it. Due to its lack of authentication, Cognita appears intended to be hosted on intranets or locally. An attacking website can try guessing the local IP of a Cognita instance by sending requests to local addresses such as localhost, or it can enumerate the internal IP address space by continually making requests until it finds the Cognita instance. With this bug alone, our access is limited to just using the RAG endpoints and possibly deleting data. We want to get a foothold in the network. Let’s look for a real primitive.

We found a simple arbitrary file write primitive; the developers added an endpoint for Docker without considering file sanitization, and now we can write to any file we want. The `file.filename` is controlled by the request and `os.path.join` resolves the “..”, allowing `file_path` to be fully controlled.

```
@router.post("/upload-to-local-directory")
async def upload_to_docker_directory(
    upload_name: str = Form(
        default_factory=lambda: str(uuid.uuid4()), regex=r"^[a-z][a-z0-9-]*$"
    ),
    files: List[UploadFile] = File(...),
):
...
        for file in files:
            logger.info(f"Copying file: {file.filename}, to folder: {folder_path}")
            file_path = os.path.join(folder_path, file.filename)
            with open(file_path, "wb") as f:
                f.write(file.file.read())
```

Now that we have an arbitrary file write target, what should we target to get RCE? This endpoint is for Docker users and the Cognita documentation only shows how to install via Docker. Let’s take a look at that Dockerfile.

```
command: -c "set -e; prisma db push --schema ./backend/database/schema.prisma && uvicorn --host 0.0.0.0 --port 8000 backend.server.app:app --reload"
```

Looking carefully, there’s the `--reload` when starting up the backend server. So we can overwrite any file in the server and uvicorn will automatically restart the server to apply changes. Thanks uvicorn! Let’s target the `init.py` files that are run on start, and now we have RCE on the Cognita instance. We can use this to read data from Cognita, or use it as a starting point on the network and attempt to connect to other vulnerable devices from there.

### Logic issues lead to credit card charges and backdoor access[](https://github.blog/security/application-security/localhost-dangers-cors-and-dns-rebinding/#logic-issues-lead-to-credit-card-charges-and-backdoor-access)

Next, let’s look at some additional real life examples of faulty CORS logic.

We found the following code was found on the website [_https://tamagui.dev_](https://tamagui.dev/). Since the source code is found on GitHub, we decided to take a quick look. (Note: The found vulnerability has since been reported by our team and fixed by the developer.)

```
export function setupCors(req: NextApiRequest, res: NextApiResponse) {
  const origin = req.headers.origin

  if (
    typeof origin === 'string' &&
    (origin.endsWith('tamagui.dev') ||
      origin.endsWith('localhost:1421') ||
      origin.endsWith('stripe.com'))
  ) {
    res.setHeader('Access-Control-Allow-Origin', origin)
    res.setHeader('Access-Control-Allow-Credentials', 'true')
  }
}
```

As you can see, the developer added hardcoded endpoints. Taking a guess, the developer most likely used Stripe for payment, localhost for local development and _tamagui.dev_ for subdomain access or to deal with https issues. In short, it looks like the developer added allowed domains as they became needed.

As we know, using `endsWith` is insufficient and an attacker may be able to create a domain that fulfills those qualities. Depending on the _tamagui.dev_ account’s permissions, an attacker could perform a range of actions on behalf of the user, such as potentially buying products on the website by charging their credit card.

Lastly, some projects don’t prioritize security and developers are simply writing the code to work. For example, the following project used the `HasPrefix` and `Contains` functions to check the origin, which is easily exploitable. Using this vulnerability, we can trick an administrator to click on a specific link (let’s say _[https://localhost.attacker.com](https://localhost.attacker.com/)_), and use the user-add endpoint to install a backdoor account in the application.

```
func CorsFilter(ctx *context.Context) {
    origin := ctx.Input.Header(headerOrigin)
    originConf := conf.GetConfigString("origin")
    originHostname := getHostname(origin)
    host := removePort(ctx.Request.Host)

    if strings.HasPrefix(origin, "http://localhost") || strings.HasPrefix(origin, "https://localhost") || strings.HasPrefix(origin, "http://127.0.0.1") || strings.HasPrefix(origin, "http://casdoor-app") || strings.Contains(origin, ".chromiumapp.org") {
        setCorsHeaders(ctx, origin)
        return
    }

func setCorsHeaders(ctx *context.Context, origin string) {
    ctx.Output.Header(headerAllowOrigin, origin)
    ctx.Output.Header(headerAllowMethods, "POST, GET, OPTIONS, DELETE")
    ctx.Output.Header(headerAllowHeaders, "Content-Type, Authorization")
    ctx.Output.Header(headerAllowCredentials, "true")

    if ctx.Input.Method() == "OPTIONS" {
        ctx.ResponseWriter.WriteHeader(http.StatusOK)
    }
}
```

DNS rebinding[](https://github.blog/security/application-security/localhost-dangers-cors-and-dns-rebinding/#dns-rebinding)
--------------------------------------------------------------------------------------------------------------------------

![Image 1: Diagram showing how DNS rebinding utilizes the DNS system to exploit vulnerable web applications.](https://github.blog/wp-content/uploads/2025/04/DNS.png?resize=1024%2C767)

DNS rebinding has the same mechanism as a CORS misconfiguration, but its ability is limited. DNS rebinding does not require a misconfiguration or bug on the part of the developer or user. Rather, it’s an attack on how the DNS system works.

Both CORS and DNS rebinding vulnerabilities facilitate requests to API endpoints from unintended origins. First, an attacker lures the victim’s browser to a domain that serves malicious javascript. The malicious javascript makes a request to a host that the attacker controls, and sets the DNS records to redirect the browser to a local address. With control over the resolving DNS server, the attacker can change the IP address of the domain and its subdomains in order to get the browser to connect to various IP addresses. The malicious javascript will scan for open connections and send their malicious payload requests to them.

This attack is very easy to set up using NCCGroup’s [singularity](https://github.com/nccgroup/singularity?tab=readme-ov-file) tool. Under the [payloads folder](https://github.com/nccgroup/singularity/tree/master/html/payloads), you can view the scripts that interact with singularity and even add your own script to tell singularity how to send requests and respond.

Fortunately, DNS rebinding is very easy to mitigate as it cannot contain cookies, so adding simple authentication for all sensitive and critical endpoints will prevent this attack. Since the browser thinks it is contacting the attacker domain, it would send any cookies from the attacker domain, not those from the actual web application, and authorization would fail.

If you don’t want to add authentication for a simple application, then you should [check that the host header matches an approved host name or a local name](https://github.com/OpenRefine/OpenRefine/pull/3212/files#diff-d1306540c0d68d0039bffa2784661857cbf5c11ee56834d059e3f0d586dccf37). Unfortunately, many newly created AI projects currently proliferating do not have any of these security protections built in, making any data on those web applications possibly retrievable and any vulnerability remotely exploitable.

```
   public boolean isValidHost(String host) {

        // Allow loopback IPv4 and IPv6 addresses, as well as localhost
        if (LOOPBACK_PATTERN.matcher(host).find()) {
            return true;
        }

        // Strip port from hostname - for IPv6 addresses, if
        // they end with a bracket, then there is no port
        int index = host.lastIndexOf(':');
        if (index > 0 && !host.endsWith("]")) {
            host = host.substring(0, index);
        }

        // Strip brackets from IPv6 addresses
        if (host.startsWith("[") && host.endsWith("]")) {
            host = host.substring(1, host.length() - 2);
        }

        // Allow only if stripped hostname matches expected hostname
        return expectedHost.equalsIgnoreCase(host);
    }
```

Because DNS rebinding requires certain parameters to be effective, it is not caught by security scanners for the fear of many false positives. At GitHub, our DNS rebinding reports to maintainers commonly go unfixed due to the unusual nature of this attack, and we see that only the most popular repos have checks in place.

When publishing software that holds security critical information or takes privileged actions, we strongly encourage developers to write code that checks that the origin header matches the host or an allowlist.

Conclusion[](https://github.blog/security/application-security/localhost-dangers-cors-and-dns-rebinding/#conclusion)
--------------------------------------------------------------------------------------------------------------------

Using CORS to bypass the same-origin policy has always led to common mistakes. Finding and fixing these issues is relatively simple once you understand CORS mechanics. New and improving browser protections have mitigated some of the risk and may eliminate this bug class altogether in the future. Oftentimes, finding CORS issues is as simple as searching for “CORS” or `Access-Control-Allow-Origin` in the code to see if any insecure presets or logic are used.

Check out the [Mozilla Developer Network CORS page](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS) if you wish to become better acquainted with how CORS works and the config you choose when using a CORS framework.

If you’re building an application without authentication that utilizes critical functionality, remember to check the Host header as an extra security measure.

Finally, [GitHub Code Security](https://github.com/security/advanced-security/code-security) can help you secure your project by detecting and suggesting a fix for bugs such as [CORS misconfiguration](https://codeql.github.com/codeql-query-help/javascript/js-cors-misconfiguration-for-credentials/)!

Written by
----------

 ![Image 2: Kevin Stubbings](https://avatars.githubusercontent.com/u/11400619?v=4&s=200)
