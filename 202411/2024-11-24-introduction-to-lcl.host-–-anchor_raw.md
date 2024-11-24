Title: Nextra: the next docs builder

URL Source: https://anchor.dev/docs/lcl-host/why-lcl

Markdown Content:
What is lcl.host?[](https://anchor.dev/docs/lcl-host/why-lcl#what-is-lclhost)
-----------------------------------------------------------------------------

With just two easy commands, you can setup HTTPS in your local environment with lcl.host. The [lcl.host CLI](https://anchor.dev/docs/lcl-host/why-lcl#what-is-anchor-lcl) will walk you through the steps to create a secure browsing context in your local browser using HTTPS.

lcl.host is made by the [Anchor team (opens in a new tab)](https://anchor.dev/) that makes production-grade private [Certificate Authorities](https://anchor.dev/docs/getting-started/concepts#ca), and now you can use the same technology in your development environment.

When do I need HTTPS locally?[](https://anchor.dev/docs/lcl-host/why-lcl#when-do-i-need-https-locally)
------------------------------------------------------------------------------------------------------

There are a number of reasons why you will need HTTPS in your development environment to reduce pain and suffering.

### You're dealing with...[](https://anchor.dev/docs/lcl-host/why-lcl#youre-dealing-with)

*   ##### Mixed Content[](https://anchor.dev/docs/lcl-host/why-lcl#mixed-content)
    
    In an ideal world, all content is served over HTTPS. Unfortunately in the real world a secure webpage may request unprotected content over HTTP. You will need to add HTTPS to your local environment to mimic the mixed content in your production environment.
    
*   ##### CORS errors[](https://anchor.dev/docs/lcl-host/why-lcl#cors-errors)
    
    When a webpage loads content from multiple origins, the browser's [security context](https://anchor.dev/docs/getting-started/concepts#secure-context) may change, causing a CORS error. By keeping the browser in the same security context as production, you can reproduce and debug the CORS issues locally.
    
*   ##### HTTP/2[](https://anchor.dev/docs/lcl-host/why-lcl#http2)
    
    HTTP/2 and HTTP/3 require (or make it hard to avoid) using TLS. If you want to test something like loading performance on HTTP/2 or reproduce behavior specific to HTTP/2 then you will need HTTPS in your local environment as insecure HTTP/2 isn't supported on localhost.
    
*   ##### Secure Cookies[](https://anchor.dev/docs/lcl-host/why-lcl#secure-cookies)
    
    Generally browsers handle cookies in localhost the same as in production, with the exception of secure cookies. To keep behavior consistent across browsers, use HTTPS in your local environment so that it matches your production environment.
    
*   ##### OAuth and secure 3rd Party endpoints[](https://anchor.dev/docs/lcl-host/why-lcl#oauth-and-secure-3rd-party-endpoints)
    
    Many external organizations require HTTPS in their callbacks for security, even in local development, such as Facebook's OAuth. To test them out, you'll need to switch your local development to HTTPS.
    
*   ##### Localhost Apps and Marketplaces[](https://anchor.dev/docs/lcl-host/why-lcl#localhost-apps-and-marketplaces)
    
    There are tools that run a webserver on a local port and are accessible from the browser via [http://localhost:\[PORT (opens in a new tab)](http://localhost:%5BPORT)\] that occasionally require HTTPS. Many marketplaces such as Heroku, Slack, and AWS also require HTTPS for developing marketplace apps.
    
*   ##### Requirement for tools[](https://anchor.dev/docs/lcl-host/why-lcl#requirement-for-tools)
    
    Certain development tools require HTTPS in development to ensure that they function correctly.
    

### You are developing...[](https://anchor.dev/docs/lcl-host/why-lcl#you-are-developing)

*   ##### On the Public Web[](https://anchor.dev/docs/lcl-host/why-lcl#on-the-public-web)
    
    Your production environment has a public certificate, and you want to mimic that environment locally.
    
*   ##### SaaS[](https://anchor.dev/docs/lcl-host/why-lcl#saas)
    
    With services that are connected to the internet, such as a Ruby on Rails SaaS project.
    
*   ##### Microservices[](https://anchor.dev/docs/lcl-host/why-lcl#microservices)
    
    A React app that talks to a separate backend API, setting cookies and making API requests.
    

Benefits of lcl.host[](https://anchor.dev/docs/lcl-host/why-lcl#benefits-of-lclhost)
------------------------------------------------------------------------------------

### Dev/Prod Parity[](https://anchor.dev/docs/lcl-host/why-lcl#devprod-parity)

It's important to maintain [development/production parity (opens in a new tab)](https://12factor.net/dev-prod-parity) to keep development and production as similar as possible so that the gap between the environments is kept small. Within a [secure browser context](https://anchor.dev/docs/getting-started/concepts#secure-context) like lcl.host you can develop in similarly secure conditions. Browsers treat lcl.host subdomains like an ordinary, secure domain, but you don't have to register, setup, or maintain it to use it.

Usually localhost acts like HTTPS and correctly handles Service Workers, Progressive Web Apps (PWAs), payment APIs, credential APIs, and web authentication APIs. However in certain cases you will need HTTPS in your development environment to make it act like your production environment.

Another benefit of using HTTPS locally is that some features of WebRTC and Web Workers require it, even on localhost. Similarly, when using [gRPC (opens in a new tab)](https://grpc.io/) you will need HTTP/2 to establish bidirectional streaming, which also requires TLS.

What is `anchor lcl`?[](https://anchor.dev/docs/lcl-host/why-lcl#what-is-anchor-lcl)
------------------------------------------------------------------------------------

The Anchor CLI has many commands for setting up your certificates in all environments. When you run `anchor lcl`, the CLI does the following:

1.  Configures your local certificate stores to trust Anchor-provided certificates from your account, and your account only.
2.  Detects the application name and language/server type, then provisions the application's service and resources through Anchor's API.
3.  Provisions a certificate for your app (or service), and writes the certificate and key pair to files in your application directory. You can then use this certificate to manually enable HTTPS/TLS in your development environment.
4.  Adds WebPKI-linted, [CA](https://anchor.dev/docs/getting-started/concepts#ca) certificates to your filesystem that are specific to your app or service.
5.  Finally, the Anchor Setup Guide shows you a few easy steps to set up and use [ACME](https://anchor.dev/docs/getting-started/concepts#acme) for future certificate provisioning. [Read about the benefits of automated provisioning with ACME](https://anchor.dev/docs/lcl-host/why-lcl#why-should-i-setup-acme-automatic-provisioning-on-my-project)

How do subdomains of lcl.host work?[](https://anchor.dev/docs/lcl-host/why-lcl#how-do-subdomains-of-lclhost-work)
-----------------------------------------------------------------------------------------------------------------

lcl.host subdomains always resolve to the loopback interface address (127.0.0.1), the same address that [http://localhost (opens in a new tab)](http://localhost/) resolves to in your browser. You can use any lcl.host subdomain address as a replacement for a localhost address in development.

For example, if you use [http://localhost:3000 (opens in a new tab)](http://localhost:3000/) in development for your project, you can use [https://project.lcl.host:3000 (opens in a new tab)](https://project.lcl.host:3000/) instead. [Learn more about the lcl.host subdomains](https://anchor.dev/docs/lcl-host/lcl-overview).

FAQ[](https://anchor.dev/docs/lcl-host/why-lcl#faq)
---------------------------------------------------

#### What is TLS and why do I need it?[](https://anchor.dev/docs/lcl-host/why-lcl#what-is-tls-and-why-do-i-need-it)

TLS, formerly called SSL, ensures that your data and users are safe from attacks by encrypting the traffic between the client and the server. Learn more about [TLS here](https://anchor.dev/docs/getting-started/concepts#tls).

#### Once I setup lcl.host, can I share my certificate so my team can use it too?

lcl.host is free for personal projects & personal use, and it is free for team projects in development environments. Instead of sharing certificates and credentials on your personal account, you can create an organization account for your organization and invite team members.

If you're interested in using Anchor to secure your application in a non-development environment, you can join our preview program for staging and production environments.

#### Can I use lcl.host in prod or staging?[](https://anchor.dev/docs/lcl-host/why-lcl#can-i-use-lclhost-in-prod-or-staging)

For production and staging environments, go to [Anchor.dev (opens in a new tab)](https://anchor.dev/) to setup your certificate so that it can be used in staging or production.

#### Why should I setup ACME automatic provisioning on my project?[](https://anchor.dev/docs/lcl-host/why-lcl#why-should-i-setup-acme-automatic-provisioning-on-my-project)

By default, the certificate you create with `anchor lcl` is only valid for 28 days. That means every 4 weeks you will have to rerun the provision command. But as an efficient engineer you will want to automate the provisioning process to run in the background whenever you start your local server. Then your certificates are always valid. Anchor configures your app so that if it doesn't have a certificate, or it's close to expiring, that it will automatically renew the certificate. This is all done for you by your languages standard ACME client or with an Anchor ACME plugin.

Put in a couple minutes to set it up now and save yourself from the headaches later.

#### My team already added lcl.host to the project. As a new employee (or on a new laptop), what do I need to do to get setup?[](https://anchor.dev/docs/lcl-host/why-lcl#my-team-already-added-lclhost-to-the-project-as-a-new-employee-or-on-a-new-laptop-what-do-i-need-to-do-to-get-setup)

Your team has already added the ACME package or dependency to your project, so you can skip that step in the Setup Guide. You may need to follow a couple more steps to set it up depending on the language (Ruby, Go, etc).

Run `anchor lcl` to setup your local system to provision and trust the certificates, which will create the project in your personal Anchor account. Finally put in the variables in your setup guide into your `.env` file.

#### Can I use a development VM or containers with lcl.host?[](https://anchor.dev/docs/lcl-host/why-lcl#can-i-use-a-development-vm-or-containers-with-lclhost)

VM based development environments like [GitHub Codespaces (opens in a new tab)](https://github.com/features/codespaces) and [WSL (opens in a new tab)](https://learn.microsoft.com/en-us/windows/wsl/install) have seperate system trust stores than the host system where your browsers run. This is also the case for container based development environments like [Docker (opens in a new tab)](https://www.docker.com/).

This means that the running `anchor lcl` on a container or VM will _not_ update the system trust stores used by your browsers. To configure the trust stores on your host system, install the Anchor CLI and run `anchor lcl config` on your host system.

Once you have configured your host system, a certificate presented by a server running in a container or VM will work in your browsers.

#### Can I use `anchor lcl` with my own domain?[](https://anchor.dev/docs/lcl-host/why-lcl#can-i-use-anchor-lcl-with-my-own-domain)

`anchor lcl` does not support custom domains, but Anchor's organization features allow you to create a development workspace for your team with a custom domain. If you are interested, please reach out [support@anchor.dev](mailto:support@anchor.dev?subject=custom%20org%20domain).

Your personal CA (used by `anchor lcl`) is only permitted to issue certificates for `lcl.host` and `localhost` subdomains, so it is not possible for your CA to issue valid certificates for a domain you own, or any other. Your CA certificates include a special X.509 extension called a name constraint which enforces this restriction.

#### Does my project need to have globally unique name?[](https://anchor.dev/docs/lcl-host/why-lcl#does-my-project-need-to-have-globally-unique-name)

No, does not. Since each subdomain always routes to your local system and your certificates only work for you, there's no worry about project names overlapping.

#### Will my dev environment be publicly accessible (on the internet)?[](https://anchor.dev/docs/lcl-host/why-lcl#will-my-dev-environment-be-publicly-accessible-on-the-internet)

No, your dev environment is still secure on your machine. If someone else tries to visit `yoursubdomain.lcl.host`, the request will be sent to their own local machine, and they will get an error. This is because `yoursubdomain.lcl.host` routes to their own loopback address, not yours. Your apps on lcl.host subdomains are only accessible from your local dev machine.

#### What is a `.pem` file?[](https://anchor.dev/docs/lcl-host/why-lcl#what-is-a-pem-file)

Privacy Enhanced Mail (PEM) is a file type for Public Key Infrastructure (PKI) files used for keys and certificates. The certificate created by lcl.host will end in `cert.pem` and the key will end in `key.pem`. The chain file includes the end-user certificate and the intermediate certificate that issues the end-user certificate.

#### Why use a FQDN instead of localhost?[](https://anchor.dev/docs/lcl-host/why-lcl#why-use-a-fqdn-instead-of-localhost)

lcl.host, a FQDN, maintains a secure context and is lightweight to setup. Localhost sometimes acts like a secure context but other times it does not, so it's easier to always use a FQDN like lcl.host.

#### How is `anchor lcl` different from self-signed certificate tools?[](https://anchor.dev/docs/lcl-host/why-lcl#how-is-anchor-lcl-different-from-self-signed-certificate-tools)

`mkcert` (and other tools like it) issue self-signed certificates whereas `anchor lcl` uses an Anchor-hosted Private CA to issue certificates. There are a few advantages to using a Private CA over self-signed certificates:

*   `anchor lcl` is easy to transfer between development environments.
*   Anchor's built-in certificate linting and validations prevent invalid, expired, or otherwise broken certificates from being created.
*   Anchor-hosted Private CAs support ACME-based certificate provisioning and the renewal process can be automated, but a self-signed certificate must be manually renewed.
*   Finally, `mkcert` can only encrypt your local dev environment. Anchor encrypts all of your environments with lcl.host for development and Anchor for staging and production.

#### Why isn't lcl.host working?[](https://anchor.dev/docs/lcl-host/why-lcl#why-isnt-lclhost-working)

If a lcl.host subdomain is not resolving in your browser or system, it usually means the domain is not a valid URL, or [DNS rebinding (opens in a new tab)](https://en.wikipedia.org/wiki/DNS_rebinding) protection is interfering with DNS resolution.

To bypass DNS rebinding protection, try using a public DNS server like 8.8.8.8 (Google) or 1.1.1.1 (CloudFlare) instead. Or add an entry for lcl.host subdomain to your /etc/hosts file (e.g. subdomain.lcl.host 127.0.0.1). Please reach out at [support@anchor.dev](mailto:support@anchor.dev) if you're having trouble with it.

Last updated on October 31, 2024

[Core Concepts & Terminology](https://anchor.dev/docs/getting-started/concepts "Core Concepts & Terminology")[Learn about lcl.host](https://anchor.dev/docs/lcl-host/lcl-overview "Learn about lcl.host")
