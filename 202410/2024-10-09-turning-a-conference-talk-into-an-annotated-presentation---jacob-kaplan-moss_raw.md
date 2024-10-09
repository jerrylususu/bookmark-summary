Title: Turning a conference talk into an annotated presentation - Jacob Kaplan-Moss

URL Source: https://jacobian.org/til/talk-to-writeup-workflow/

Markdown Content:
I really like trying to publish written versions of conference talks – videos are great, but not everyone has the time or desire to watch. But in the past I’ve often not been able to make them happen – it’s just felt like a lot of work transcribing an entire talk, producing a writeup, etc. But modern AI tools have changed this, it’s now significantly easier.

*   Write my talk in Keynote.
    
*   Export slides from Keynote as a folder full of PNGs.
    
*   Use [Simon’s annotated presentation creator](https://til.simonwillison.net/tools/annotated-presentations) to quickly render a template using that folder full of images. The template I used for my Hugo blog was something like:
    
    ```
    {{< figure
         src="${filename}"
         alt="${escapeHTML(alt)}"
         class="slide" >}}
    ```
    
    I didn’t bother pasting in annotations here; I did that later directly in the Markdown file. I did use the tool’s OCR to generate alt text.
    
*   Downloaded the video of the talk from YouTube with [yt-dlp](https://github.com/yt-dlp/yt-dlp).
    
    The DjangoCon team shared a raw unedited video of the entire conference with us — the individual videos will be out soon — so I needed to just download my talk segment, which you can do with the `--download-sections` flag. The syntax is `"*{start},{end}"`, where `start` and `end` are expressed in sections.
    
    ```
    ❯ yt-dlp https://www.youtube.com/live/[REDACTED] --download-sections "*10800,12438"
    ```
    
*   Convert that video from MKV into MP4. I actually can never remember ffmpeg command line flags, so I used [llm-cmd](https://github.com/simonw/llm-cmd) which worked perfectly:
    
    ```
    ❯ llm cmd convert Tuesday\ Junior\ Ballroom.mkv from mkv into mp4
    > ffmpeg -i "Tuesday Junior Ballroom [1J3UqRQcxqA].mkv" -c copy "Tuesday Junior Ballroom [1J3UqRQcxqA].mp4"
    ...
    ```
    
*   Bring that video into [MacWhisper](https://goodsnooze.gumroad.com/l/macwhisper) and convert it into a transcript. I used the “Large V2” model, but today I’d probably use the “Turbo” model which should be a lot faster.
    
    This whole thing could have been much simpler if I had just the video of my talk – MacWhisper has a direct “transcribe youtube” feature, and I could have just pasted in the youtube URL and gone from there. I also could have probably gotten `yt-dlp` to download a different format, or just audio … but whatever, I’m sharing the actual commands I used because it’s interesting.
    
    You can see the [raw output from Whisper here](https://jacobian.org/2024/oct/8/dsf-one-million//transcript-raw-whisper.txt) – as you can see, it’s a really accurate transcript, but is also kind of a wall of text.
    
*   Clean this up into paragraphs using the [llm CLI](https://github.com/simonw/llm):
    
    ```
    ❯ cat transcript-raw-whisper.txt | \
      llm -s "Split the content of this transcript up into paragraphs with logical breaks.
              Add newlines between each paragraph." \
      > transcript-split-claude.txt"
    ```
    
    This uses my default model, which right now is [Claude 3.5 Sonnet](https://www.anthropic.com/news/claude-3-5-sonnet) (`claude-3-5-sonnet-20240620`).
    
    You can see [the cleaned up and organized transcript here](https://jacobian.org/2024/oct/8/dsf-one-million//transcript-split-claude.txt).
    
    Claude seems to do the best job not trying to re-write my content; by and large, the split up version is as I said it, just more logically grouped into paragraphs.
    
*   Manually copy and paste into the Markdown file.
    
*   Re-write and add extra notes and content as needed. I had also recorded a practice run, and transcribed that, so I had two different versions of the talk to read through, and I also had some bits that got cut for time (a longer quote from Sue Gardner’s piece), so I added this stuff back manually.
    
    I also spent some time re-writing – making the tone sound more like how I _write_, and less like how I _talk_. This close reading also helped make sure Claude hadn’t re-written my words, or added anything LLM-y (It mostly hadn’t, but I caught a couple of places where it had slightly changed what I said in ways that were not a huge deal but kinda clumsy and worth fixing.)
