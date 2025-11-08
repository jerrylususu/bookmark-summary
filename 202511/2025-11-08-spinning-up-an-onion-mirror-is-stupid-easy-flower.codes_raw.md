Title: Spinning up an Onion Mirror is Stupid Easy

URL Source: https://flower.codes/2025/10/23/onion-mirror.html

Markdown Content:
I recently spun up a .onion mirror of this website.

Why? Because why not. And also because I can. Oh, and free speech and anti-censorship and all that jazz.

I'd like to pretend that it was some grand technological challenge, but if I'm being entirely candid, it was like 3 commands and 4 lines of configuration.

If you, too, would like to become a member of the dark web, here's how I did it:

0. Prerequisites [#](https://flower.codes/2025/10/23/onion-mirror.html#0-prerequisites)
---------------------------------------------------------------------------------------

Before we jump into the "how" of it all, I should probably provide a brief overview of what my stack looked like before I entered The Onionverse:

*   **Web Server**: I've been using [Caddy](https://caddyserver.com/) for a few years now, because it's significantly easier to configure than Nginx or Apache, and it has first-class support for modern web features like automatic HTTPS via Let's Encrypt.
*   **Hosting**: My site is hosted on a VPS from [DigitalOcean](https://www.digitalocean.com/), which gives me full control over the server environment. It's supposed to cost $4/mo, but I'm taking some classes at Ye Olde Community College, so I have a few years of credits to cover the cost.
*   **Operating System**: My server runs Debian. I like Debian. If you aren't using an apt-based distro, then you'll need to adjust the package installation commands accordingly (but the Tor and Caddy configurations should be the same).

1. Install Tor [#](https://flower.codes/2025/10/23/onion-mirror.html#1-install-tor)
-----------------------------------------------------------------------------------

First things first, we need to install Tor. On Debian, it's right in the default repositories:

sudo apt update
sudo apt install tor

2. Configure Tor [#](https://flower.codes/2025/10/23/onion-mirror.html#2-configure-tor)
---------------------------------------------------------------------------------------

Next, we need to configure Tor to create a hidden service for our website. Open the Tor configuration file (`/etc/tor/torrc`) in your favorite CLI text editor (it better be `vim`, or you are dead to me). I have no interest in running a relay or exit node on my VPS, so I made some minimal changes to the config file, which should look something like this (comments removed for clarity):

# Disable SOCKS proxy since we aren't making outbound connections
# through Tor
SocksPort 0

# Make sure Tor runs as a daemon (i.e. in the background)
RunAsDaemon 1

# Setup the hidden service on port 80, this is where we tell Tor to
# create a .onion service for our web server
HiddenServiceDir /var/lib/tor/hidden_service/
HiddenServicePort 80

# Disable inbound connections, since we aren't running a relay or
# exit node
ORPort 0

# Disable directory services, since we won't be mirroring directory
# information to other Tor nodes
DirPort 0

That's it. Everything else should be commented out using `#` characters.

3. Restart Tor [#](https://flower.codes/2025/10/23/onion-mirror.html#3-restart-tor)
-----------------------------------------------------------------------------------

Now we need to restart the Tor service to apply our changes:

sudo systemctl restart tor

4. Get Your .onion Address [#](https://flower.codes/2025/10/23/onion-mirror.html#4-get-your-onion-address)
----------------------------------------------------------------------------------------------------------

After Tor restarts, it will generate a new hidden service for us. We can find our new .onion address in the `HiddenServiceDir` we specified earlier (`/var/lib/tor/hidden_service/`). This directory is only readable by the `debian-tor` user, so we'll need to use `sudo` to read the `hostname` file inside:

sudo cat /var/lib/tor/hidden_service/hostname

What will be printed to the terminal is your new .onion address. It should look something like this:

jytkco7clxwj4hhzaydhk4kr3hwzsdzyvtsc6zn2ivog5uma5pxowzad.onion

5. Configure Caddy [#](https://flower.codes/2025/10/23/onion-mirror.html#5-configure-caddy)
-------------------------------------------------------------------------------------------

My Caddy server serves my website on port 80 without any IP or domain restrictions, so I don't need to make any changes to my Caddy configuration, however if you explicitly set up your Caddy server to only respond to certain domains or IP addresses, you'll need to add a new site block for your .onion address, which will look something like this:

http://jytkco7clxwj4hhzaydhk4kr3hwzsdzyvtsc6zn2ivog5uma5pxowzad.onion:80 {
  # Set up a reverse proxy, or serve static files, etc.
}

Because you can't get HTTPS certificates for .onion addresses, you'll need to serve your site over plain HTTP. I'm not sure if this is generally considered acceptable within the Tor network (maybe one of my tens of readers can enlighten me), but I don't require HTTPS for my site anyway, so it works for my purposes.

**Update (2025-10-31):**

I received an email yesterday from [immibis](https://www.immibis.com/) with some additional information about how Tor actually works, so I thought I'd share for anyone else who is also just dipping their toes into the onion:

> _This is considered perfectly acceptable. Tor already provides encryption between the end user's Tor daemon and your own, which is at least as good as TLS.
> 
> 
> The address is linked to the private key - which is also found in your hidden service directory next to the hostname - forever and always. Anyone who knows the private key of a .onion address can impersonate it, and anyone who doesn't know it, can't._

6. (Optional) Advertise Your .onion Address [#](https://flower.codes/2025/10/23/onion-mirror.html#6-optional-advertise-your-onion-address)
------------------------------------------------------------------------------------------------------------------------------------------

If you want people to find your .onion site, you'll need to advertise it somewhere. I'm a fan of subtlety, so I set up an `Onion-Location` header on my main site that points to my .onion address. This way, anyone visiting my regular site with a Tor-enabled browser will automatically be informed of the existence of my .onion mirror without any intrusive pop-ups, banners, or additional UI elements.

To do this, you'll want to add a header to your main Caddy site block like so:

header {
  Onion-Location http://jytkco7clxwj4hhzaydhk4kr3hwzsdzyvtsc6zn2ivog5uma5pxowzad.onion{uri}
}

The reason I tack on that `{uri}` at the end is so that if someone visits a specific page on my main site (e.g. `https://flower.codes/some-post`), the `Onion-Location` header will point them to the equivalent page on my .onion site (`http://jytkco7clxwj4hhzaydhk4kr3hwzsdzyvtsc6zn2ivog5uma5pxowzad.onion/some-post`), which (at least to me) adds some polish to the experience.

7. Profit! [#](https://flower.codes/2025/10/23/onion-mirror.html#7-profit)
--------------------------------------------------------------------------

Just kidding.

At this point, your .onion mirror should be up and running. You can test it out by visiting your .onion address in any Tor-enabled browser (like the [Tor Browser](https://www.torproject.org/download/) or even [Brave](https://brave.com/), which has built-in Tor support).

--

If you like this post or one of my projects, you can [buy me a coffee](https://www.buymeacoffee.com/zachflower), or [send me a note](mailto:zach@flower.codes). I'd love to hear from you!