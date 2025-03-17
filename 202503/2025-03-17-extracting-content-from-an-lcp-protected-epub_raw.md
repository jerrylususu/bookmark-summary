Title: Extracting content from an LCP "protected" ePub

URL Source: https://shkspr.mobi/blog/2025/03/towards-extracting-content-from-an-lcp-protected-epub/

Published Time: 2025-03-16T12:34:57+00:00

Markdown Content:
As Cory Doctorow once said "[Any time that someone puts a lock on something that belongs to you but won't give you the key, that lock's not there for you.](https://www.bbc.co.uk/news/business-12701664)"

But here's the thing with the LCP DRM scheme; they _do_ give you the key! As [I've written about previously](https://shkspr.mobi/blog/2025/03/some-thoughts-on-lcp-ebook-drm/), LCP mostly relies on the user entering their password (the key) when they want to read the book. Oh, there's some deep cryptographic magic in the background but, ultimately, the key is sat on your computer waiting to be found. Of course, cryptography is Very Hard™ which make retrieving the key almost impossible - so perhaps we can use a different technique to extract the unencrypted content?

One popular LCP app is [Thorium](https://thorium.edrlab.org/en/). It is an [Electron Web App](https://www.electronjs.org/). That means it is a bundled browser running JavaScript. That also means it can trivially be debugged. The code is running on your own computer, it doesn't touch anyone else's machine. There's no reverse engineering. No cracking of cryptographic secrets. No circumvention of any technical control. It doesn't reveal any [illegal numbers](https://en.wikipedia.org/wiki/Illegal_number). It doesn't jailbreak anything. We simply ask the reader to give us the content we've paid for - and it agrees.

[Here Be Dragons](https://shkspr.mobi/blog/2025/03/towards-extracting-content-from-an-lcp-protected-epub/#here-be-dragons)
--------------------------------------------------------------------------------------------------------------------------

This is a manual, error-prone, and tiresome process. This cannot be used to automatically remove DRM. I've only tested this on Linux. It must only be used on books that you have legally acquired. I am using it for research and private study.

This uses [Thorium 3.1.0 AppImage](https://github.com/edrlab/thorium-reader/releases/tag/v3.1.0).

First, extract the application:

 ![Image 1: BASH](https://shkspr.mobi/blog/wp-content/plugins/wp-geshi-highlight/svg/bash.svg) BASH`./Thorium-3.1.0.AppImage --appimage-extract`

That creates a directory called `squashfs-root` which contains all the app's code.

The Thorium app can be run with remote debugging enabled by using:

 ![Image 2: BASH](https://shkspr.mobi/blog/wp-content/plugins/wp-geshi-highlight/svg/bash.svg) BASH`./squashfs-root/thorium --remote-debugging-port=9223 --remote-allow-origins=*`

Within the Thorium app, open up the book you want to read.

Open up Chrome and go to `http://localhost:9223/` - you will see a list of Thorium windows. Click on the link which relates to your book.

In the Thorium book window, navigate through your book. In the debug window, you should see the text and images pop up.

![Image 3: Chrome debug screen.](https://shkspr.mobi/blog/wp-content/uploads/2025/03/debug-fs8.png.webp)

In the debug window's "Content" tab, you'll be able to see the images and HTML that the eBook contains.

[Images](https://shkspr.mobi/blog/2025/03/towards-extracting-content-from-an-lcp-protected-epub/#images)
--------------------------------------------------------------------------------------------------------

The images are the full resolution files decrypted from your ePub. They can be right-clicked and saved from the developer tools.

[Files](https://shkspr.mobi/blog/2025/03/towards-extracting-content-from-an-lcp-protected-epub/#files)
------------------------------------------------------------------------------------------------------

An ePub file is just a zipped collection of files. Get a copy of your ePub and rename it to `whatever.zip` then extract it. You will now be able to see the names of all the files - images, css, fonts, text, etc - but their contents will be encrypted, so you can't open them.

You can, however, give their filenames to the Electron app and it will read them for you.

[Images](https://shkspr.mobi/blog/2025/03/towards-extracting-content-from-an-lcp-protected-epub/#images)
--------------------------------------------------------------------------------------------------------

To get a Base64 encoded version of an image, run this command in the debug console:

 ![Image 4: JavaScript](https://shkspr.mobi/blog/wp-content/plugins/wp-geshi-highlight/svg/javascript.svg) JavaScript```
fetch("httpsr2://...--/xthoriumhttps/ip0.0.0.0/p/OEBPS/image/whatever.jpg") .then(response => response.arrayBuffer())  
  .then(buffer => {  
    let base64 = btoa(  
      new Uint8Array(buffer).reduce((data, byte) => data + String.fromCharCode(byte), '')  
    );  
    console.log(`data:image/jpeg;base64,${base64}`);  
  });
```

[Thorium uses the `httpsr2` URl scheme](https://github.com/w3c/epub-specs/issues/1888#issuecomment-958439051) - you can find the exact URl by looking at the content tab.

[CSS](https://shkspr.mobi/blog/2025/03/towards-extracting-content-from-an-lcp-protected-epub/#css)
--------------------------------------------------------------------------------------------------

The CSS can be read directly and printed to the console:

 ![Image 5: JavaScript](https://shkspr.mobi/blog/wp-content/plugins/wp-geshi-highlight/svg/javascript.svg) JavaScript```
fetch("httpsr2://....--/xthoriumhttps/ip0.0.0.0/p/OEBPS/css/styles.css").then(response => response.text())  
  .then(cssText => console.log(cssText));
```

However, it is _much_ larger than the original CSS - presumably because Thorium has injected its own directives in there.

Metadata like the [NCX](https://wiki.mobileread.com/wiki/NCX) and the [OPF](https://opensource.com/article/22/8/epub-file) can also be decrypted without problem:

 ![Image 6: JavaScript](https://shkspr.mobi/blog/wp-content/plugins/wp-geshi-highlight/svg/javascript.svg) JavaScript```
fetch("httpsr2://....--/xthoriumhttps/ip0.0.0.0/p/OEBPS/content.opf").then(response => response.text())  
  .then(metadata => console.log(metadata));
```

They have roughly the same filesize as their encrypted counterparts - so I don't think anything is missing from them.

[Fonts](https://shkspr.mobi/blog/2025/03/towards-extracting-content-from-an-lcp-protected-epub/#fonts)
------------------------------------------------------------------------------------------------------

If a font has been used in the document, it should be available. It can be grabbed as Base64 encoded text to the console using:

 ![Image 7: JavaScript](https://shkspr.mobi/blog/wp-content/plugins/wp-geshi-highlight/svg/javascript.svg) JavaScript```
fetch("httpsr2://....--/xthoriumhttps/ip0.0.0.0/p/OEBPS/font/Whatever.ttf") .then(response => response.arrayBuffer())  
  .then(buffer => {  
    let base64 = btoa(  
      new Uint8Array(buffer).reduce((data, byte) => data + String.fromCharCode(byte), '')  
    );  
    console.log(`${base64}`);  
  });
```

From there it can be copied into a new file and then decoded.

[Text](https://shkspr.mobi/blog/2025/03/towards-extracting-content-from-an-lcp-protected-epub/#text)
----------------------------------------------------------------------------------------------------

The HTML of the book is also visible on the Content tab. It is _not_ the original content from the ePub. It has a bunch of CSS and JS added to it. But, once you get to the body, you'll see something like:

 ![Image 8: HTML](https://shkspr.mobi/blog/wp-content/plugins/wp-geshi-highlight/svg/html5.svg) HTML```
<body>  
    <section epub:type="chapter" role="doc-chapter">  
        <h2 id="_idParaDest-7" class="ct"><a id="_idTextAnchor007"></a><span id="page75" role="doc-pagebreak" aria-label="75" epub:type="pagebreak"></span>Book Title</h2>  
        <div class="_idGenObjectLayout-1">  
            <figure class="Full-Cover-White">  
                <img class="_idGenObjectAttribute-1" src="image/cover.jpg" alt="" />  
            </figure>  
        </div>  
        <div id="page76" role="doc-pagebreak" aria-label="76" epub:type="pagebreak" />  
        <section class="summary"><h3 class="summary"><span class="border">SUMMARY</span></h3>   
        <p class="BT-Sans-left-align---p1">Lorem ipsum etc.</p>  
    </section>
```

Which looks like plain old ePub to me. You can use the `fetch` command as above, but you'll still get the verbose version of the xHTML.

[Putting it all together](https://shkspr.mobi/blog/2025/03/towards-extracting-content-from-an-lcp-protected-epub/#putting-it-all-together)
--------------------------------------------------------------------------------------------------------------------------------

If you've unzipped the original ePub, you'll see the internal directory structure. It should look something like this:

```
├── META-INF
│   └── container.xml
├── mimetype
└── OEBPS
    ├── content.opf
    ├── images
    │   ├── cover.jpg
    │   ├── image1.jpg
    │   └── image2.png
    ├── styles
    │   └── styles.css
    ├── content
    │   ├── 001-cover.xhtml
    │   ├── 002-about.xhtml
    │   ├── 003-title.xhtml
    │   ├── 004-chapter_01.xhtml
    │   ├── 005-chapter_02.xhtml
    │   └── 006-chapter_03.xhtml
    └── toc.ncx
```

Add the extracted files into that exact structure. Then zip them. Rename the .zip to .epub. That's it. You now have a DRM-free copy of the book that you purchased.

LCP 2.0 PDFs are also extractable. Again, you'll need to open your purchased PDF in Thorium with debug mode active. In the debugger, you should be able to find the URl for the decrypted PDF.

It can be fetched with:

 ![Image 9: JavaScript](https://shkspr.mobi/blog/wp-content/plugins/wp-geshi-highlight/svg/javascript.svg) JavaScript```
fetch("thoriumhttps://0.0.0.0/pub/..../publication.pdf") .then(response => response.arrayBuffer())  
  .then(buffer => {  
    let base64 = btoa(  
      new Uint8Array(buffer).reduce((data, byte) => data + String.fromCharCode(byte), '')  
    );  
    console.log(`${base64}`);  
  });
```

Copy the output and Base64 decode it. You'll have an unencumbered PDF.

[Next Steps](https://shkspr.mobi/blog/2025/03/towards-extracting-content-from-an-lcp-protected-epub/#next-steps)
----------------------------------------------------------------------------------------------------------------

That's probably about as far as I am competent to take this.

But, for now, [a solution exists](https://proofwiki.org/wiki/ProofWiki:Jokes/Physicist_Mathematician_and_Engineer_Jokes/Burning_Hotel#Variant_1). If I ever buy an ePub with LCP Profile 2.0 encryption, I'll be able to manually extract what I need from it - without reverse engineering the encryption scheme.

[Ethics](https://shkspr.mobi/blog/2025/03/towards-extracting-content-from-an-lcp-protected-epub/#ethics)
--------------------------------------------------------------------------------------------------------

Before I published this blog post, [I publicised my findings on Mastodon](https://mastodon.social/@Edent/114155981621627317). Shortly afterwards, I received a LinkedIn message from someone senior in the Readium consortium - the body which has created the LCP DRM.

They said:

> Hi Terence, You've found a way to hack LCP using Thorium. Bravo! We certainly didn't sufficiently protect the system, we are already working on that. From your Mastodon messages, you want to post your solution on your blog. This is what triggers my message. From a manual solution, others will create a one-click solution. As you say, LCP is a "reasonably inoffensive" protection. We managed to convince publishers (even big US publishers) to adopt a solution that is flexible for readers and appreciated by public libraries and booksellers. Our gains are re-injected in open-source software and open standards (work on EPUB and Web Publications). If the DRM does not succeed, harder DRMs (for users) will be tested. I let you think about that aspect

I did indeed think about that aspect. A day later I replied, saying:

> Thank you for your message. Because Readium doesn't freely licence its DRM, it has an adverse effect on me and other readers like me.
> 
> *   My eReader hardware is out of support from the manufacturer - it will never receive an update for LCP support.
> *   My reading software (KOReader) have publicly stated that they cannot afford the fees you charge and will not be certified by you.
> *   Kobo hardware cannot read LCP protected books.
> *   There is no guarantee that LCP compatible software will be released for future platforms.
> 
> In short, I want to read my books on _my_ choice of hardware and software; not yours. I believe that everyone deserves the right to read on their platform of choice without having to seek permission from a 3rd party. The technique I have discovered is basic. It is an unsophisticated use of your app's built-in debugging functionality. I have not reverse engineered your code, nor have I decrypted your secret keys. I will not be publishing any of your intellectual property. In the spirit of openness, I intend to publish my research this week, alongside our correspondence.

Their reply, shortly before publication, contained what I consider to be a crude attempt at emotional manipulation.

> Obviously, we are on different sides of the channel on the subject of DRMs. I agree there should be many more LCP-compliant apps and devices; one hundred is insufficient. KOReader never contacted us: I don't think they know how low the certification fee would be (pricing is visible on the EDRLab website). FBReader, another open-source reading app, supports LCP on its downloadable version. Kobo support is coming. Also, too few people know that certification is free for specialised devices (e.g. braille and audio devices from Hims or Humanware). We were planning to now focus on new accessibility features on our open-source Thorium Reader, better access to annotations for blind users and an advanced reading mode for dyslexic people. Too bad; disturbances around LCP will force us to focus on a new round of security measures, ensuring the technology stays useful for ebook lending (stop reading after some time) and as a protection against oversharing. You can, for sure, publish information relative to your discoveries to the extent UK laws allow. After study, we'll do our best to make the technology more robust. If your discourse represents a circumvention of this technical protection measure, we'll command a take-down as a standard procedure.

A bit of a self-own to admit that they failed to properly prioritise accessibility!

Rather than rebut all their points, I decided to keep my reply succinct.

> As you have raised the possibility of legal action, I think it is best that we terminate this conversation.

I sincerely believe that this post is a legitimate attempt to educate people about the deficiencies in Readium's DRM scheme. Both readers and publishers need to be aware that their Thorium app easily allows access to unprotected content.

I will, of course, publish any further correspondence related to this issue.
