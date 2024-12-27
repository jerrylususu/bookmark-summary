Title: A black cat in 2032 bytes

URL Source: https://evanhahn.com/light-switch/

Published Time: 2024-12-26T00:00:00+00:00

Markdown Content:
[Taper](https://taper.badquar.to/) describes itself as “an online literary magazine for small computational pieces”. Submissions need to be 2048 bytes or fewer.

I submitted this little piece, [“Light Switch”](https://taper.badquar.to/13/light_switch.html), to their [13th issue](https://taper.badquar.to/13/):

The rest of this post describes how I did it.

Shrinking the image
-------------------

The black cat is the most significant part of the piece. It’s a highly-edited version of a photo I took:

![Image 15: The original photo of the cat.](https://evanhahn.com/light-switch/original.jpg)

This is a cute picture but it’s 2.5 megabytes, which is _over 1000 times too big_.

After a lot of editing, I crushed it down to a 502-byte PNG. Here’s what it looks like in the final submission:

![Image 16: The compressed image of the cat.](https://evanhahn.com/light-switch/compressed.png)

I went through several steps to achieve this.

1.  I started by using [iOS’s “lift a subject” feature](https://support.apple.com/guide/iphone/lift-a-subject-from-the-photo-background-iphfe4809658/ios) to isolate the cat and remove the background. I still needed to do some editing, but it was a helpful first pass.
2.  I used [Squoosh](https://squoosh.app/) to change the color palette to just black and transparent. Black-and-white PNGs are generally smaller because each pixel can be stored with just one bit (0 for black, 1 for white/transparent)[1](https://evanhahn.com/light-switch/#fn:1). I also shrunk the image to just 200×193.
3.  I made minor adjustments in [JS Paint](https://jspaint.app/). For example, the right eye looked weird after resizing and removing so many colors.
4.  [Zopfli](https://github.com/google/zopfli) helped me squeeze every last byte out of the image. I ran `zopflipng --iterations=1000 --filters=01234mepb --lossy_transparent uncompressed.png compressed.png`.

I’m sure there’s some tool that does all of those things at once, but I was happy using my hodgepodge of different tools.

Putting the image on the page
-----------------------------

Next, I needed to put the image on the page. I can’t load external resources, so I used a base64-encoded [data URL](https://developer.mozilla.org/en-US/docs/web/http/basics_of_http/data_urls).

The HTML looks something like this:

```
<img src="data:image/png;base64,iVBORw0KG..." />
```

This data URL is 694 bytes long. This was a big increase from 502 bytes. This concerned me and I had a few ideas for improvements:

*   Try another image format. Maybe GIF or WebP compress better in this scenario?
*   Store the binary data some other way. There’s likely something better than base64 out there. Maybe I could put the image in a string somehow?
*   Manually create the image. In this demo, I’m always drawing the exact same image every time. Maybe I could devise something more compact?

I vowed to address these concerns when they became a problem…they never did, and I stuck with the base64-encoded data URL.

I added [pixelated image rendering](https://developer.mozilla.org/en-US/docs/Web/CSS/image-rendering) and moved the image to the bottom-right of the screen.

Making the cat blink
--------------------

Now that I had the cat sitting still on the screen, I needed to make it a little more lifelike. I needed to make it blink.

After some enjoyable moments looking up GIFs of cats blinking, I settled on this solution:

![Image 17: The cat's blinking eyes.](https://evanhahn.com/light-switch/normal.gif) ![Image 18: How the cat's blinking eyes work: little circles representing the eyelids.](https://evanhahn.com/light-switch/debug.gif)

The cat has four eyelids, one for each eye. Each is a black circle that periodically moves over part of the eye. These circles sit on a [`<canvas>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/canvas) directly atop the image.

While I was developing it, I thought there was no way something so simple would work. But when I increased the speed, it looked totally fine! Yet another case where my primitive solution was good enough.

I added some additional polish to make the cat occasionally blink twice, which I felt made it look better.

Turning off the lights
----------------------

My partner recommended I add some additional pizzazz, so I added the ability to turn the lights on and off.

I immediately ran into a problem: the cat’s eyes are transparent in the image. This meant that I couldn’t change the background color without changing the color of the cat’s eyes, and I wanted the cat’s eyes to be visible in the dark.

![Image 19: The image of the cat on a brown background. Because the eyes are transparent, the cat's eyes are brown, which isn't what I wanted.](https://evanhahn.com/light-switch/compressed.png)

I tried making a new version of the image with yellow eyes. Unfortunately, this made the image too large, presumably because each pixel could no longer be encoded with a single bit.

My partner had another good suggestion: just put a yellow box behind the eyes. That’s what I did.

![Image 20: The cat image with the yellow eyes behind.](https://evanhahn.com/light-switch/yellow_eyes.png)

Another primitive solution that was very effective.

Shaving off bytes
-----------------

Taper doesn’t allow “pieces using exec or regex eval functions”, which rules out compressors like [RegPack](https://github.com/Siorki/RegPack/). In addition to the image compression I described above, I used a combination of tricks to keep my JavaScript under the size limit:

*   [Terser](https://terser.org/) for compressing JavaScript. This did most of the heavy lifting, but I needed to tweak its configuration for maximum effect.
*   Using element IDs. For example, if you have `<canvas id=c>` in your HTML, you can refer to it with `c` in your JavaScript.
*   Using `let` instead of `const`
*   Using arrow functions like `() => {}` instead of `function () {}`
*   Using event handlers like `el.onclick` instead of `el.addEventListener("click", ...)`
*   Using `7` instead of `2 * Math.PI`

I could’ve done much more, but these solutions were enough to keep me well under the 2048 byte limit with minimal effort.

Thank you
---------

If you’re curious, you can see [the source code here](https://git.sr.ht/~evanhahn/light-switch).

Make sure to [check out all the other great submissions on the Taper website](https://taper.badquar.to/13/)!

Thanks to my partner for constant help and suggestions, thanks to the Taper team for their hard work…and biggest thanks of all to Kyppie the cat, who is now world famous.
