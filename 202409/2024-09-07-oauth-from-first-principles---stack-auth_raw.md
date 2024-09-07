Title: OAuth from First Principles - Stack Auth

URL Source: https://stack-auth.com/blog/oauth-from-first-principles

Markdown Content:
I've wanted to write a blog post for everyone who learns things the same way that I do; by trying to break them.

I'll start off with an awfully flawed implementation that authorizes a user with a 3rd-party app, and then continuously attack it until we arrive at something that's secure, kind of.

N.B.: This is not for you if you're looking to implement OAuth 2.0 in production. You're probably better off reading the [relevant RFCs](https://datatracker.ietf.org/doc/html/rfc6749), but even then I'd ask why you're trying to reinvent the wheel.

_By the way, we are building [Stack Auth](https://stack-auth.com/), the open-source Auth0 alternative. You can learn more about us and/or contribute on our [GitHub repo](https://github.com/stack-auth/stack)._

The world without OAuth
-----------------------

Big Head wants to save storage space on his Hooli Cloud drive. He finds Pied Piper, an app that promises to compress his files. But for Pied Piper to work its magic, it needs access to his Hooli drive.

The simplest way for Pied Piper to get that access is to ask Big Head for his Hooli username and password. With those, Pied Piper can log into Hooli on his behalf and access his files.

Here's how that would go:

![Image 1: Big Head gives his Hooli username and password to Pied Piper](https://stack-auth.com/images/blog/oauth/p1.png)

The screen Big Head sees in his browser might look something like this:

![Image 2: Big Head sees the Hooli login screen](https://stack-auth.com/images/blog/oauth/p2.png)

Attack #1: Big Head's credentials are exposed
---------------------------------------------

By handing over his username and password, Big Head gives Pied Piper full access to his entire Hooli account. This includes Hooli Mail, Hooli Chat, and even the ability to change his password! Furthermore, if someone ever hacks Pied Piper, they will get to see Big Head's password in plain text.

So, they come up with a new plan: generate an access token. This is a key that lets Pied Piper access Big Head's data on Hooli with limited permissions.

![Image 3: Big Head gives an access token to Pied Piper](https://stack-auth.com/images/blog/oauth/p3.png)

And this is how it would look like to Big Head:

![Image 4: Big Head sees the Hooli access token screen](https://stack-auth.com/images/blog/oauth/p4.png)

While this approach is secure, it's not particularly user-friendly. Big Head doesn't want to generate an access token manually every single time he compresses a file, or signs in to a service. He wants Pied Piper to do it for him.

### Automation

Instead of Big Head generating access tokens manually and copying them to Pied Piper, Pied Piper can ask Hooli to generate access tokens on his behalf.

![Image 5: Big Head gives Pied Piper access to his Hooli drive](https://stack-auth.com/images/blog/oauth/p5.png)

This would be amazing if there were no bad actors on this world! Big Head just needs to click a button, and everything is done automatically. But, there is an obvious problem here.

Attack #2: Anyone can just claim to be anyone else
--------------------------------------------------

![Image 6: We might have a problem](https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExcDdhYXo3eTBmaGMwdnp5eWVhZmo1bngyZTZyMGx6ZTd3aHFidHF4OSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/26BRuyxFdtlQq5VPa/giphy.webp)

There is absolutely no security in this approach! Pied Piper can just pretend to be acting on behalf of anyone, and Hooli will happily generate an access token.

So, to ensure the request is really from Big Head, Hooli needs to ask him for confirmation.

![Image 7: Big Head sees the Hooli login screen](https://stack-auth.com/images/blog/oauth/p7.png)

In the wide world of the web, step 3 is usually done by redirecting Big Head to a page on a `hooli.com` domain. So, his browser would show this:

![Image 8: Big Head sees the Hooli login screen](https://stack-auth.com/images/blog/oauth/p8.png)

Hooli can now verify that the person sitting in front of the browser is Big Head. In step 3, Hooli can freely design the confirmation process. Hooli could ask Big Head to confirm his email/password login, do 2FA, and/or ask for consent.

### Putting a name on it: Implicit flow

Early implementations of OAuth looked exactly like this; we call it the _implicit flow_. Though, we're not even half-way through this post, so maybe you can guess that you shouldn't use this in your production apps.

But, let's start giving names to things, in accordance with what OAuth calls them:

![Image 9: OAuth implicit flow](https://stack-auth.com/images/blog/oauth/p9.png)

The query parameters in the URL are:

*   `client_id=piedpiper`: This tells Hooli which app is asking for access (in this case, Pied Piper).
*   `redirect_uri=https://piedpiper.com/callback`: This is where Hooli should send Big Head back to after he approves the connection.
*   `scope=drive`: The permissions Pied Piper needs.
*   `response_type=token`: Tells Hooli that we are using the implicit flow.

So far so good!

Attack #3: Redirect URI manipulation
------------------------------------

Endframe, a malicious competitor to Pied Piper, wants to steal Big Head's Hooli drive data.

1.  Endframe sends Big Head an email with the subject, "Connect your Hooli account with Pied Piper".
    *   They include a link to `https://hooli.com/authorize?...`, with the same `client_id` and `scope` as a real request from Pied Piper.
    *   But, they change the `redirect_uri` parameter to `https://endframe.com`.
2.  Big Head checks the domain and sees it is `hooli.com`, so he clicks on the link.
3.  The Hooli consent screen pops up. Big Head confirms that it is Pied Piper's client ID, so he logs in and confirms access.
4.  However, after Big Head clicks "Allow," Hooli redirects him to `https://endframe.com` instead of `https://piedpiper.com/callback`, sending the access token to Endframe.
5.  Now, Endframe has access to Big Head's Hooli drive!

The problem is that Hooli didn't verify that the `client_id` and `redirect_uri` match.

The solution is to require Pied Piper to register all possible redirect URIs first. Then, Hooli should refuse to redirect to any other domain.

Attack #4: Cross-site request forgery (CSRF)
--------------------------------------------

There are some more advanced attacks however. Endframe can still trick Big Head into logging in with a malicious Hooli account:

1.  Endframe registers an account with Pied Piper.
2.  They log into Pied Piper and generate an access token `access_token_456` for their own Hooli drive.
3.  They send Big Head an email with the title "Check out our Bachmanity photo album" and a link `https://piedpiper.com/callback?access_token=access_token_456`.
4.  Big Head checks the domain, sees it is `piedpiper.com`, and clicks on it.
5.  The Pied Piper website opens the callback and logs in Big Head into Endframe's Hooli drive, so any files he uploads will go to Endframe's Hooli drive.

How can we prevent this? We need to make sure that we only finish the OAuth flow if we initiated it.

To do so, Pied Piper can generate a random string (we call it `state`), store it in cookies, and send it to Hooli. Hooli will then send this `state` back to Pied Piper when it redirects Big Head back. Pied Piper should then check that the received `state` matches the one in the cookies.

![Image 10: CSRF protection](https://stack-auth.com/images/blog/oauth/p10.png)

*   `state=random_string_123`: A randomly generated string to prevent CSRF attacks.

Attack #5: Eavesdropping access tokens
--------------------------------------

Endframe isn't giving up. They've come up with another plan:

1.  They teamed up with a genius developer called Jian Yang and created a "Hot dog or not" tool that detects hot dogs. Maliciously, it also sends the entire browser history to Endframe.
    *   (There are a number of other history sniffing or HTTP downgrade attacks that could pull this off, too.)
2.  Big Head thinks it's funny and installs it.
3.  Endframe now sees all the access tokens for all services that Big Head ever logged in with, by searching for URLs that look like `https://piedpiper.com/callback?access_token=access_token_123`.

There is a fix for this. We need to make sure that access tokens are never exchanged in browser URLs.

Hooli generates a short-lived "authorization code" and redirects back to Pied Piper with this code. Pied Piper then makes a POST request to another endpoint, which invalidates the authorization code and exchanges it for the access token.

This way, the access token never ends up in the browser history. We call this the _authorization code_ flow. It is more secure than the implicit flow, but we're still not done.

![Image 11: Authorization code flow](https://stack-auth.com/images/blog/oauth/p11.png)

*   `response_type=code`: Tells Hooli that we are using the authorization code flow, instead of the implicit flow.
*   `code=authorization_code_123`: The authorization code Hooli generated for Pied Piper.
*   `grant_type=authorization_code`: For the authorization code flow, this is always `authorization_code` (we won't cover the other grant types).

Attack #6: Eavesdropping authorization codes
--------------------------------------------

If Endframe eavesdrops the authorization code in real-time, they can exchange it for an access token very quickly, before Big Head's browser does.

1.  Big Head still has the "Hot dog or not" tool installed.
2.  As soon as Big Head connects his Hooli drive account, "Hot dog or not" fetches the authorization code from Big Head's browser history.
3.  In real time, faster than Big Head's browser can send the request, Endframe swoops in and sends a request to Hooli with Big Head's authorization code. They get the access token and Big Head's request fails.

Currently, anyone with the authorization code can exchange it for an access token. We need to ensure that only the person who initiated the request can do the exchange.

We do this by securely storing a secret on the client. We hash this secret, and send it to Hooli alongside the very first request. When exchanging the authorization code for the access token, we send the original secret to Hooli. Hooli then compares the hashes, proving that the request is coming from the same client.

This procedure is called _proof key for code exchange_ (PKCE).

![Image 12: PKCE flow](https://stack-auth.com/images/blog/oauth/p12.png)

*   `code_verifier=random_string_456`: The original random string Pied Piper sent to Hooli.
*   `code_challenge=hashed_string_123`: The hashed code verifier.

Is this secure? Not quite...

Attack #7: Redirect URI manipulation on trusted URIs
----------------------------------------------------

Imagine that Pied Piper has two registered redirect URIs:

*   `https://piedpiper.com/callback`
*   `https://piedpiper.com/share-files-callback`

The first one authorizes and compresses Hooli drive files, and the second one shares files publicly with other users. (This could also be the same endpoint with different query parameters.)

Even though we protect against Endframe replacing the redirect URI with something totally malicious (like `https://endframe.com`), if Endframe can intercept the request somehow, they can still modify the URI to point to the other endpoint.

The solution? Make the client send the current URI again when exchanging the authorization code for the access token. Hooli can then verify that the redirect URI matches the one in the original request.

![Image 13: Big Head sees the Hooli login screen](https://stack-auth.com/images/blog/oauth/p13.png)

The final flow
--------------

Congrats — we arrived at the OAuth 2.0 authorization code flow with PKCE, which is the accepted standard way to do third-party auth in browsers today.

![Image 14: PKCE flow](https://stack-auth.com/images/blog/oauth/p14.png)

Show description

1.  Big Head clicks the "Connect to Hooli drive" button on the Pied Piper website.
2.  Pied Piper generates two random strings `state=random_string_123` and `code_verifier=random_string_456` and stores them in a cookie or local storage.
3.  Pied Piper redirects Big Head to the Hooli website OAuth authorization endpoint `https://hooli.com/authorize` with the following parameters:
    *   `client_id=piedpiper`: This tells Hooli which app is asking for access (in this case, Pied Piper).
    *   `redirect_uri=https://piedpiper.com/callback`: This is where Hooli should send Big Head back to after he approves the connection.
    *   `scope=drive`: The permissions Pied Piper needs.
    *   `response_type=code`: This indicates that we want an authorization code.
    *   `state=random_string_123`: A random string to prevent CSRF attacks.
    *   `code_challenge=hashed_string_123`: The hashed code verifier.
4.  Hooli checks if the `redirect_uri` is registered with the `client_id`. If not, Hooli rejects the request.
5.  Hooli presents a login screen to Big Head.
6.  Big Head logs into his Hooli account and confirms that he wants to give Pied Piper access to his Hooli drive.
7.  Hooli redirects Big Head back to the Pied Piper callback URL `https://piedpiper.com/callback` with the following parameters:
    *   `code=authorization_code_123`: The authorization code Hooli generated for Pied Piper.
    *   `state=random_string_123`: The random string Pied Piper sent to Hooli.
8.  Pied Piper checks that the `state` matches the one they sent. If it doesn't, Pied Piper rejects the request.
9.  Pied Piper uses JavaScript to make a POST request to the Hooli token endpoint `https://hooli.com/token` with the following parameters:
    *   `client_id=piedpiper`: The client ID Pied Piper registered with Hooli.
    *   `code=authorization_code_123`: The authorization code Hooli generated for Pied Piper.
    *   `grant_type=authorization_code`: Specifies that this is an authorization code grant type (the other grant types are not going to be covered here).
    *   `redirect_uri=https://piedpiper.com/callback`: The redirect URI Pied Piper used in the original request.
    *   `code_verifier=random_string_456`: The original random string Pied Piper sent to Hooli.
10.  Hooli ensures the code is unused and still valid and the redirect URI is the same as the one in the original request, and the hashed `code_verifier` matches with the previous `code_challenge`. If not, Hooli rejects the request.
11.  Hooli generates an access token and returns it to Pied Piper in the response body:
    *   `access_token=access_token_123`: The access token Hooli generated for Pied Piper to access Big Head's Hooli drive.
12.  Pied Piper uses the access token to access Hooli's API `https://hooli.com/drive` with an authorization header like `Authorization: Bearer access_token_123`.

Some final notes
----------------

This is an informal explanation of the OAuth flow, and the actual specification is much longer. For example, client secrets, refresh tokens, client credentials flow, token grants, etc., are not covered here.

Furthermore, there are a lot of nitty-gritty details that are required for a secure implementation. You probably shouldn't implement your own OAuth client.

For diving deeper or if you want to implement OAuth in your apps, here are some good resources.

*   [The OAuth 2.0 Authorization Framework](https://datatracker.ietf.org/doc/html/rfc6749)
*   [OAuth 2.0 Threat Model and Security Considerations](https://datatracker.ietf.org/doc/html/rfc6819)
*   [OAuth 2.0 for Browser-Based Applications](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-browser-based-apps)
