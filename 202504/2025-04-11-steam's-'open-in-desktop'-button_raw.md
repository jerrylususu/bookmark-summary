Title: Steam's 'Open in Desktop' Button

URL Source: https://parsiya.net/blog/steam-open-desktop/

Markdown Content:
*   [Summary: How does it Work?](https://parsiya.net/blog/steam-open-desktop/#summary-how-does-it-work)
*   [How Can I Also See It?](https://parsiya.net/blog/steam-open-desktop/#how-can-i-also-see-it)
    *   [I Wanna See the WebSocket Messages](https://parsiya.net/blog/steam-open-desktop/#i-wanna-see-the-websocket-messages)
    *   [Protocol Handlers](https://parsiya.net/blog/steam-open-desktop/#protocol-handlers)
    *   [Why Use a WebSocket?](https://parsiya.net/blog/steam-open-desktop/#why-use-a-websocket)
*   [So How do I Find Bugs Here?](https://parsiya.net/blog/steam-open-desktop/#so-how-do-i-find-bugs-here)
    *   [How about You Show Us Some Actual Bugs!](https://parsiya.net/blog/steam-open-desktop/#how-about-you-show-us-some-actual-bugs)

This is not a bug, but some notes about the new Steam "Open in Desktop" button. I am going to show how to look for bugs in these kinds of browser-to-desktop interactions.

When you go to a game's Steam page in the browser, you get this button.

![Image 1: Game page](https://parsiya.net/blog/steam-open-desktop/01.png)

Clicking on it, will open the game page in the Steam desktop app.

Every time you see a web to app transition without any user notification, a security control has been circumvented. Whether this is good or bad is not the objective here.

Summary: How does it Work?[](https://parsiya.net/blog/steam-open-desktop/#summary-how-does-it-work)
---------------------------------------------------------------------------------------------------

1.  WebSocket connection from the web page to the Steam desktop app at `localhost:27060`.
2.  Web page passes a message like this to the desktop app.
    
    ```
     {
       "message": "OpenSteamURL",
       "url": "steam://openurl/https://store.steampowered.com/app/1517290/Battlefield_2042/?utm_bid=3546095213808494257",
       // removed
     }
    ```
    
3.  Steam desktop opens the page URL.

How Can I Also See It?[](https://parsiya.net/blog/steam-open-desktop/#how-can-i-also-see-it)
--------------------------------------------------------------------------------------------

There are only a few ways to bypass those browser security controls and it's almost always a WebSocket.

1.  Go to the BF 2042 page at [https://store.steampowered.com/app/1517290/Battlefield\_2042/](https://store.steampowered.com/app/1517290/Battlefield_2042/).
2.  `F12` to open Developer Tools (I assume you're using a Chromium based browser).
    1.  Edge annoyingly asks if you actually want to open DevTools. Check the box so it doesn't ask again.
3.  Switch to the `Network` tab.
4.  `ctrl + F5` to refresh the page.
5.  Click on `Open in Desktop`. Switch back to Dev Tools.
6.  There will be a bunch of junk here that we have to sift through.
    1.  Optionally, you could use Burp and filter these in `HTTP Proxy`.
7.  Click on the `Status` column to sort by the response status code.
8.  See this `101` on top? That's what we want.

![Image 2: WebSocket handshake](https://parsiya.net/blog/steam-open-desktop/02.png)

It's even conveniently named `openindesktopclient.js`. Click on it to see the header, request, response, and messages.

![Image 3: WebSocket handshake](https://parsiya.net/blog/steam-open-desktop/03.png)

[101](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/101) is the response code for switching protocols. While the [Protocol upgrade mechanism](https://developer.mozilla.org/en-US/docs/Web/HTTP/Protocol_upgrade_mechanism) is technically protocol agnostic, I have only seen it in WebSocket connections. Upon further searching, it looks like it can also be used to upgrade an [HTTP/1.1 connection to HTTP/2](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Upgrade).

I Wanna See the WebSocket Messages[](https://parsiya.net/blog/steam-open-desktop/#i-wanna-see-the-websocket-messages)
---------------------------------------------------------------------------------------------------------------------

You can click on the `Message` tab in the previous image or go the `Network` tab of DevTools Click `WS`. You can even filter messages by connection (which is supposedly useful if you have multiple ones in the same page which I've never seen).

![Image 4: WebSocket Messages](https://parsiya.net/blog/steam-open-desktop/04.png)

The 3rd message is the one that opens the page.

```
{
  "message": "OpenSteamURL",
  "url": "steam://openurl/https://store.steampowered.com/app/1517290/Battlefield_2042/?utm_bid=3546095213808494257",
  "universe": 1,
  "accountid": 0,
  "sequenceid": 2
}
```

If you want to see which process is doing this, run `netstat -anb` in an admin prompt and look for who is listening on `127.0.0.1:27060`. It's `steam.exe`.

Protocol Handlers[](https://parsiya.net/blog/steam-open-desktop/#protocol-handlers)
-----------------------------------------------------------------------------------

This is actually the Steam protocol handler. And that can also lead to [a bunch of RCEs.](https://parsiya.net/blog/2021-03-17-attack-surface-analysis-part-2-custom-protocol-handlers/ "a bunch of RCEs.")

1.  Close Steam. As in right-click on the taskbar icon and select `Exit Steam`.
2.  Run [Process Monitor](https://learn.microsoft.com/en-us/sysinternals/downloads/procmon).
3.  Press `F12` to open DevTools for this page and select the `Console` tab.
4.  Click on this link. Hover you mouse over it to see the actual link matches the caption.
    1.  [steam://openurl/https://store.steampowered.com/app/1517290/Battlefield\_2042/](steam://openurl/https://store.steampowered.com/app/1517290/Battlefield_2042/).
5.  See the browser pop-up that asks if you want to open Steam.
6.  If you click on `Open Steam`, Steam desktop will open and navigate the BF 2042 page.

You can see the protocol handler in the `Console` tab of DevTools.

![Image 5: Protocol handler in the Console tab](https://parsiya.net/blog/steam-open-desktop/05.png)

Steam is actually executed with this protocol handler as the parameter. Switch to Procmon and press `ctrl + t` or `Tools (menu) > Process Tree`. Procmon is cutting off the complete parameter in the screenshot.

![Image 6: Steam launched in Procmon](https://parsiya.net/blog/steam-open-desktop/06.png)

This blog is just trying to show where to look for these things. If you want to learn more please start with the following links:

1.  [Eric Lawrence's](https://twitter.com/ericlaw) (he also wrote Fiddler) excellent blog: [Web-to-App Communication: App Protocols](https://textslashplain.com/2019/08/29/web-to-app-communication-app-protocols/).
2.  [a Attack Surface Analysis - Part 2 - Custom Protocol Handlers](https://parsiya.net/blog/2021-03-17-attack-surface-analysis-part-2-custom-protocol-handlers/ "a Attack Surface Analysis - Part 2 - Custom Protocol Handlers").

Why Use a WebSocket?[](https://parsiya.net/blog/steam-open-desktop/#why-use-a-websocket)
----------------------------------------------------------------------------------------

A WebSocket is the most common way to bypass the annoying protocol handler dialog because **[it's not bound by the Same Origin Policy](https://parsiya.net/blog/2020-11-01-the-same-origin-policy-gone-wild/#websockets-are-not-bound-by-the-sop "it's not bound by the Same Origin Policy")**.

It's not always a WebSocket server. Here's a bug by [Jonathan Leitschuh](https://twitter.com/JLLeitschuh) where it turns out [Zoom was using a local web server](https://infosecwriteups.com/zoom-zero-day-4-million-webcams-maybe-an-rce-just-get-them-to-visit-your-website-ac75c83f4ef5) (that even remained on the machine after removing Zoom) to do "seamless transition."

So How do I Find Bugs Here?[](https://parsiya.net/blog/steam-open-desktop/#so-how-do-i-find-bugs-here)
------------------------------------------------------------------------------------------------------

The moment you see a local web server or WebSocket server, you need to open Burp and **change the `Origin` header**.

1.  Go to the website in Burp.
2.  Select the WebSocket handshake request (the one with the `101` response header).
3.  Send to Repeater. Hint: `ctrl + r` thanks to [Agarri's Burp course](https://hackademy.agarri.fr/syllabus).
4.  Switch to Repeater. Hint: `ctrl + shift + r`.
5.  Change the `Origin` header to something else like `https://example.net`.
6.  ???
7.  Click send.

If this goes through then you have a bug. You can connect to the local WebSocket server from any website and send requests.

But in this case, we cannot. Fiddle with the `Origin` header and see what is accepted. It's only `https://store.steampowered.com` and not even other subdomains.

![Image 7: Fiddling with the Origin header](https://parsiya.net/blog/steam-open-desktop/07.png)

This means it's not vulnerable (at least from this attack surface). This issue is so common that is even has its own specific CWE: [CWE-1385: Missing Origin Validation in WebSockets](https://cwe.mitre.org/data/definitions/1385.html).

Note the browser sets the `Origin` header and it cannot be modified by JavaScript because it's a [Forbidden Header](https://developer.mozilla.org/en-US/docs/Glossary/Forbidden_header_name).

**But what if I have a malicious local app?** If you're running a local app that wants to spoof the `Origin` header then you have bigger problems.

**But muh persistence tradecraft!** lol, shut up!

There are other way to do web-to-app communication apart from protocol handlers and WebSockets. See [Browser Architecture: Web-to-App Communication Overview](https://textslashplain.com/2019/08/28/browser-architecture-web-to-app-communication-overview/)

How about You Show Us Some Actual Bugs![](https://parsiya.net/blog/steam-open-desktop/#how-about-you-show-us-some-actual-bugs)
------------------------------------------------------------------------------------------------------------------------------

Here are a bunch of references:

1.  [Websites Can Run Arbitrary Code on Machines Running the ‘PlayStation Now’ Application](https://hackerone.com/reports/873614).
    1.  The images were not disclosed the report, but the H1 report starts from scratch and shows how to find an RCE in a local WebSocket server.
2.  [CVE-2021-43907 - Remote Code Execution in Visual Studio Code's Remote WSL Extension](https://parsiya.net/blog/2021-12-20-rce-in-visual-studio-codes-remote-wsl-for-fun-and-negative-profit/ "CVE-2021-43907 - Remote Code Execution in Visual Studio Code's Remote WSL Extension")
    1.  This is basically the same bug as before.
    2.  See me and a bunch of people from [HackerNews](https://blog.securityevaluators.com/websockets-not-bound-by-cors-does-this-mean-2e7819374acc) complain about MSRC.
3.  [localghost: Escaping the Browser Sandbox Without 0-Days](https://parsiya.net/blog/2020-08-13-localghost-escaping-the-browser-sandbox-without-0-days/ "localghost: Escaping the Browser Sandbox Without 0-Days")
4.  Tavis Ormandy found a similar issue in [Logitech Options](https://project-zero.issues.chromium.org/issues/42450729)
5.  [Full Steam Ahead: Remotely Executing Code in Modern Desktop Application Architectures](https://vimeo.com/335206831) by [Thomas Shadwell](https://twitter.com/zemnmez) in Infiltrate 2019.

Obviously, there's more, but I am le tired. Thanks for reading and you know where to find me.
