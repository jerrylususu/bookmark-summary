Title: Simple macOS script to extract text from images (OCR)

URL Source: https://evanhahn.com/mac-ocr-script/

Published Time: 2025-07-14T00:00:00+00:00

Markdown Content:
I wrote [a script](https://gitlab.com/EvanHahn/dotfiles/-/blob/f04ee7988ca9c3835a07b55033847bef793e9a08/home/bin/bin/ocr) that lets me run `ocr image.png` to extract text from images. This is useful for pulling text from screenshots, photos, and more.

It only works on macOS because it uses Apple’s proprietary text recognition API. (I’ve used [Frog](https://github.com/tenderowl/frog/) for OCR on Linux, which I believe uses [Tesseract](https://tesseract-ocr.github.io/) under the hood.)

Let’s say I want to extract text from this picture:

![Image 1: Photo of an e-reader, showing some text.](https://evanhahn.com/mac-ocr-script/photo.avif)

I run this command…

```
ocr /path/to/photo.jpg
```

…to get this output:

```
The author's reflections on his situation- Is
deceived by a promise of being delivered - His
despair at sailing for the West Indies-Arrives at
Montserrat, where he is sold to Mr. King-Various
interesting instances of oppression, cruelty, and
extortion, which the author saw practised upon
the slaves in the West Indies during his captivity
from the year 1763 to 1766- Address on it to the
planters.
```

As you can see, it isn’t perfect. For example, it messes up em dashes here. But this is usually good enough for me!

Here’s the script’s source code, which uses Swift and [Apple’s Vision framework](https://developer.apple.com/documentation/vision):

```
#!/usr/bin/env swift
import Foundation
import Vision

func die(_ msg: String) -> Never {
  fputs("\(msg)\n", stderr)
  exit(1)
}

if CommandLine.arguments.count != 2 {
  die("usage: ocr /path/to/image1.jpg")
}

let path = URL(fileURLWithPath: CommandLine.arguments[1])

var recognizeTextRequest = RecognizeTextRequest()
recognizeTextRequest.automaticallyDetectsLanguage = true
recognizeTextRequest.usesLanguageCorrection = true
recognizeTextRequest.recognitionLevel = .accurate

guard let observations = try? await recognizeTextRequest.perform(on: path) else {
  die("couldn't recognize text")
}

for observation in observations {
  if let candidate = observation.topCandidates(1).first {
    print(candidate.string)
  }
}
```

My script has one minor issue: if text recognition fails, it logs a nasty error to stdout. I couldn’t figure out how to stop this. I’m okay with that because this is a simple script for my own purposes, but if you have a fix, [please let me know](https://evanhahn.com/contact/).

Hope this is helpful to someone out there!
