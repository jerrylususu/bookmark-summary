Title: Cracking The Dave & Buster’s Anomaly | Rambo Codes

URL Source: https://rambo.codes/posts/2025-05-12-cracking-the-dave-and-busters-anomaly

Markdown Content:
I was listening to an episode of one of my favorite podcasts this weekend. The show is called [Search Engine](https://www.searchengine.show/), and every episode tries to answer a question that can’t be easily answered through an actual search engine (or even AI).

This episode grabbed my attention because it was about an iOS bug, and a really weird one.

The bug is that, if you try to send an audio message using the Messages app to someone who’s also using the Messages app, and that message happens to include the name “Dave and Buster’s”, the message will never be received.

In case you’re wondering, “Dave and Buster’s” is the name of a sports bar and restaurant in the United States.

At the time I’m writing this post, this bug is still happening, so you should be able to reproduce it. I reproduced it using two iPhones running iOS 18.5 RC. As long as your audio message contains the phrase “Dave and Buster’s”, the recipient will only see the “dot dot dot” animation for several seconds, and it will then eventually disappear. They will never get the audio message.

You can also watch the video below showing the bug in action:

Demo video.

Search Engine’s Investigation
-----------------------------

The bug sounded so outlandish when I first heard about it in the podcast that I decided to pause the episode, do my own investigation, then continue listening later. I didn’t want my investigation to be biased by whatever Search Engine was able to find out.

If you’d rather not have the episode spoiled, I strongly recommend pausing your read here, [listening to the episode](https://www.searchengine.show/the-dave-and-busters-anomaly/), then coming back later. PJ Vogt is a much better storyteller than I am, you will not regret listening to the episode!

Here’s a picture of Yoshi, my corgi, serving as a buffer between the paragraph above and the spoilers below…

![Image 1: A brown and white corgi is lying curled up on a gray dog bed, looking up with a relaxed but slightly sad expression. The floor is tiled, and the background includes a wall and a black metal gate.](https://rambo.codes/assets/img/cracking-the-dave-and-busters-anomaly/yoshi.jpg)
I was honestly kind of hoping that Search Engine wouldn’t have a definitive answer for the origin of the bug because it would make my investigation more interesting.

They ended up figuring out the general reason for why the name “Dave and Buster’s” breaks iMessage, with help from Alex Stamos. But as someone who speaks fluent iPhone, I wasn’t completely satisfied with the explanation.

To be clear, this is not a critique of the podcast. It is not a technical show, and there’s only so much depth you can go into on a podcast without it becoming incredibly boring, especially for those who are not that interested in the details.

My Investigation
----------------

The first thing I wanted to figure out was whether the problem occurred with the sender or the recipient. I had a hunch that the issue would be on the recipient side, since on the sender side the message would appear just fine, but the recipient would just see the “typing” animation until it eventually timed out.

So I plugged the recipient device into my Mac and captured the logs right after the device received the problematic message.

![Image 2: Screenshot of the Console app on macOS showing various logs from an iOS device](https://rambo.codes/assets/img/cracking-the-dave-and-busters-anomaly/recipient_logs.jpg)
As you can see, there’s an error being reported by `MessagesBlastDoorService`:

```
BlastDoor contained an explosion with error: 
BlastDoor.Explosion(
  domain: "com.apple.BlastDoor.TextMessage.Message", 
  errorType: "XHTMLParseFailure", 
  keyPath: nil
)
```

Shortly after that, there’s a similar message from `imagent`, basically replicating the issue reported by the BlastDoor service.

As soon as I saw the `XHTMLParseFailure` error, I immediately knew what was happening. If you’re more technically inclined, you may have figured it out as well, perhaps even before seeing that error message.

Something else you may have noticed is that when you send an audio message using the Messages app, the message includes a transcription of the audio. If you happen to pronounce the name “Dave and Buster’s” as someone would normally pronounce it, almost like it’s a single word, the transcription engine on iOS will recognize[¹](https://rambo.codes/posts/2025-05-12-cracking-the-dave-and-busters-anomaly#footnote-1) the brand name and correctly write it as “Dave & Buster’s” (with an ampersand).

You see, HTML is a markup language, it uses different tags to indicate to a browser or some other program how to interpret the contents of a message. XHTML is a stricter version of HTML that’s based on XML and allows custom tags, as long as the document is compatible with the XML standard.

The ampersand symbol has special meaning in HTML/XHTML. It’s used to indicate special characters that would normally be interpreted as code. For example, a paragraph in HTML is represented with `<p>`. But what if you want to actually have the less than or greater than sign in your text?

To achieve that, you use something called an HTML entity. For the less than sign `<`, you’d write `&lt;` instead. The same is true for the ampersand symbol itself. Because it has special meaning in HTML, if you actually want to display an ampersand symbol, you must write it as `&amp;`. This practice is often referred to as “escaping”.

I dug a bit deeper using a debugger and managed to capture the XHTML code that the recipient device was attempting to parse when it received the “Dave & Buster’s” message, which you can see below (formatting done by me):

```
<html>
<body>
    <FILE 
    name="Audio Message.caf"
    width="0"
    height="0"
    datasize="7206"
    uti-type="com.apple.coreaudio-format"
    inline-attachment="ia-0"
    audio-transcription="Dave & Buster's"
    />
</body>
</html>
```

The `audio-transcription` attribute includes the full transcription from the audio, and it clearly has the unescaped ampersand symbol.

TL;DR
-----

`MessagesBlastDoorService` uses `MBDXMLParserContext` (via `MBDHTMLToSuperParserContext`) to parse XHTML for the audio message. Ampersands have special meaning in XML/HTML and must be escaped, so the correct way to represent the transcription in HTML would have been `"Dave &amp; Buster's"`. Apple's transcription system is not doing that, causing the parser to attempt to detect a special code after the ampersand, and since there's no valid special code nor semicolon terminating what it thinks is an HTML entity, it detects an error and stops parsing the content.

Since BlastDoor [was designed](https://support.apple.com/en-gb/guide/security/secd3c881cee/web) to thwart hacking attempts, which frequently rely on faulty data parsing, it immediately stops what it's doing and just fails. That’s what causes the message to get stuck in the “dot dot dot” state, which eventually times out, and the message just disappears.

Is This a Security Vulnerability?
---------------------------------

On the surface, this does sound like it could be used to “hack” someone’s iPhone via a bad audio message transcription, but in reality what this bug demonstrates is that Apple’s BlastDoor mechanism is working as designed.

Many bad parsers would probably accept the incorrectly-formatted XHTML, but that sort of leniency when parsing data formats is often what ends up causing security issues.

By being pedantic about the formatting, BlastDoor is protecting the recipient from an exploit that would abuse that type of issue.

¹ In case you’re wondering, the issue will also be triggered by any other recognized brand name that contains an ampersand, such as “M&M’s”. The way speech recognition works on iOS is by first doing a rough pass based on the user’s utterances, then running it through essentially an autocorrect mechanism, which will recognize brand names and correct them to their “official” spelling.
