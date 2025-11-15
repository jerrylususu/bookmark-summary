Title: Using the Web Monetization API for fun and profit

URL Source: https://blog.tomayac.com/2025/11/07/using-the-web-monetization-api-for-fun-and-profit/

Published Time: 2025-11-07T22:10:50.000Z

Markdown Content:
[](https://blog.tomayac.com/2025/11/07/using-the-web-monetization-api-for-fun-and-profit/)
I recently [spoke at JSConf Mexico](https://jsconfmx.org/speaker/W3Eio), where I spent a lot of time with the [Interledger Foundation](https://interledger.org/) folks in the hallway track and at the after party events, namely with [Ioana](https://www.linkedin.com/in/ioanachiorean/) (Engineering Manager) and [Marian](https://www.linkedin.com/in/marianvilla/) (DevRel) to talk about [Web Monetization](https://webmonetization.org/).

> Web Monetization gives publishers more revenue options and audiences more ways to sustain the content they love. Support can take many forms: from a one-time contribution to a continuous, pay-as-you-browse model. It all flows seamlessly while people engage with the content they love. Publishers earn the moment someone engages, while audiences contribute in real time, using a balance they control.

I encourage you all to give it a try! Install the [extension](https://chromewebstore.google.com/detail/web-monetization/oiabcfomehhigdepbbclppomkhlknpii) that polyfills the proposed Web standard, get a wallet (I went with [GateHub](https://gatehub.net/), which works in US Dollars and Euros), and then connect it to the extension.

You need to have funds in EUR (€) or USD ($). If you have crypto, it won't work, which I've found out by trial and error, as I was part of [Coil](https://coil.com/), the Web Monetization predecessor, which paid out in XRP.

Just to clarify, while you need a wallet—that typically is used for crypto—the actual transactions are all in real fiat money, Euro in my case.

As an extension user
--------------------

Connect your wallet and browse to a page that supports Web Monetization. You will notice whether a page is monetized when the extension has a green checkmark. My blog happens to be monetized.

![Image 1: The Web Monetization extensions's popup window.](https://blog.tomayac.com/images/bQdOCeEZsJ-368.png)

You can adjust how much you want to pay the site per hour and also send one-time payments. The money is "streamed" every minute, which you can observe in DevTools.

![Image 2: Chrome DevTools Network tab showing a POST request for a payment.](https://blog.tomayac.com/images/0QycKybhZq-368.png)

We actually have [code in Chromium](https://groups.google.com/a/chromium.org/d/msgid/blink-dev/d91487a5-108c-46e7-accd-d44b734a0b34%40igalia.com) to make native Web Monetization happen, implemented by Igalia and funded by the Interledger Foundation. I hope they can share the experiment results soon.

As a publisher
--------------

On your page, add a [payment link](https://webmonetization.org/developers/link-element/). You get the personalized payment pointer from your wallet. The following snippet shows mine.

`<link rel="monetization" href="https://ilp.gatehub.net/348218105/eur" />`
Then you're ready to receive payments. Here's me browsing my blog and seeing payments go out from and come in to my GateHub wallet. This is of course effectively a zero sum game, me paying myself. The 0.01 cent are the streamed payments that go out and then come in again. I tested a one-time payment as well. The 0.50 cents (not shown) was a successful one-time payment.

![Image 3: The GateHub wallet showing incoming and outgoing transactions.](https://blog.tomayac.com/images/Y_AlVbzaYz-368.png)

There's also a [JavaScript API](https://webmonetization.org/developers/interfaces/), so you can adjust the content of your page when your page notices that the user is paying.

```
window.addEventListener('monetization', (event) => {
  const { value, currency } = event.amountSent;
  console.log(`Browser sent ${currency} ${value}.`);
  const linkElem = event.target;
  console.log('for link element:', linkElem, linkElem.href);
});
```

For testing purposes, you can observe these `monetization` events in Chrome DevTools by pasting in the snippet above in the Console.

![Image 4: Chrome DevTools Console showing a  event.](https://blog.tomayac.com/images/bw6u89pJb1-368.png)

This way you could, for example, remove ads, or unlock an article when you notice a one-time payment. On my blog, I just show a "thank you" message for now.

![Image 5: Thank you message in the footer of my blog showing how much the user has paid.](https://blog.tomayac.com/images/eCIx1L8EWC-368.png)

I'm really bulli$h on this proposed standard. Hopefully someone else will try it and let me know how it goes. I truly and honestly believe that this could be the future for making the Web of tomorrow financially sustainable for publishers, big and small.