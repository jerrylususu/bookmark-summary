Title: Nomadic Infrastructure Design for AI workloads

URL Source: https://xeiaso.net/talks/2025/nomadic-compute/

Markdown Content:
Published on 01/27/2025, 2299 words, 9 minutes to read

How do you design a production-ready AI system to maximize effectiveness per dollar? How do you manage and reduce dependency lock-in? Moreover, how do you separate concerns between your compute, network, and storage? In this talk I'll be covering all of that and showing you how to design a production-worthy AI setup that lets you be nomadic between providers, hunting down deals as easily as possible.

Video
-----

Transcript
----------

![Image 53: Cadey is coffee](https://stickers.xeiaso.net/sticker/cadey/coffee)

<[**Cadey**](https://xeiaso.net/characters#cadey)\>

This is spoken word. It is not written like I write blogposts. It is reproduced here for your convenience.

![Image 54: The title slide of the talk. It shows the speaker name and the title.](https://cdn.xeiaso.net/file/christine-static/talks/2025/nomadic-compute/001.jpg)

The title slide of the talk. It shows the speaker name and the title.

Hi, I'm Xe. I work at Tigris Data, and I'm going to talk about the concept of nomadic infrastructure design for your AI workloads.

![Image 55: This is not a product demo.](https://cdn.xeiaso.net/file/christine-static/talks/2025/nomadic-compute/002.jpg)

This is not a product demo.

But disclaimer, this is not a product demo.

(Audience cheers)

This is thought leadership, which is a kind of product, I guess.

![Image 56: The three parts of a workload: compute, network, and storage.](https://cdn.xeiaso.net/file/christine-static/talks/2025/nomadic-compute/003.jpg)

The three parts of a workload: compute, network, and storage.

A workload has three basic parts. Compute, network, and storage. Compute is the part that does the number crunching or the linear algebra. The network is what connects all our computers together. It's why we have to update everything every fifth femtosecond. And storage is what remembers things for next time.

This is what you're billed on over time.

As I've been messing with new providers and trying to find cheap hacks to get my AI stuff working at absurdly low prices, I found a really weird thing.

![Image 57: Compute time is cheaper than storage time.](https://cdn.xeiaso.net/file/christine-static/talks/2025/nomadic-compute/005.jpg)

Compute time is cheaper than storage time.

Compute time is cheaper than storage time.

I don't know why this is the case. With Vast.ai, RunPod, all these bid-acquired GPU markets; spending time downloading things is cheaper than storing them for the next run.

![Image 58: Pricing details for a random 4090 in South Carolina.](https://cdn.xeiaso.net/file/christine-static/talks/2025/nomadic-compute/006.jpg)

Pricing details for a random 4090 in South Carolina.

Like, look at this. I selected a $40.90 in South Carolina at random. It costs two pennies per hour to run with 50 GB of local storage. Keeping that data around is one penny per hour. That's half of the price of the instance. Sure, there's probably some...creative financial decisions that go on into pricing things like this.

But if it takes 30 seconds to boot it and it costs like two cents an hour, it costs more to store things than it does to not store things. Really weird thing to think about.

![Image 59: How to cheat at infrastructure design.](https://cdn.xeiaso.net/file/christine-static/talks/2025/nomadic-compute/007.jpg)

How to cheat at infrastructure design.

So let's learn how to cheat an infrastructure design and find out why I am not allowed to be an SRE anymore. Asterisk.

![Image 60: A graph of Bluesky user activity.](https://cdn.xeiaso.net/file/christine-static/talks/2025/nomadic-compute/008.jpg)

A graph of Bluesky user activity.

So, the first thing that you can do is scale to zero because people don't use workloads when they're asleep. This graph has a sinusoidal wave and it's from bluesky when they blew up late last year. There's a peak in the middle of American daytime and then it all goes down to very low as the Americans go to sleep.

If you've ever worked in SRE stuff, you see this all the time. This is what your request rate looks like. This is what your active user account looks like. This is what healthy products look like. So if you just make your service turn off when nobody's using it, you already save 12 hours of runtime per day.

![Image 61: A green-haired anime woman immolating money and laughing.](https://cdn.xeiaso.net/file/christine-static/talks/2025/nomadic-compute/009.jpg)

A green-haired anime woman immolating money and laughing.

Like, remember, it may not be your money, but money is expensive now. The free tier is going to end. At some point, the hype will die out and the price of compute will reflect the price of acquiring the hardware.

Your AI workloads are dependencies. Without those workloads, your product is doomed. Those who control the infrastructure spice, control the infrastructure universe or whatever Frank Herbert said in Dune.

### Tradeoffs

![Image 62: The tradeoffs.](https://cdn.xeiaso.net/file/christine-static/talks/2025/nomadic-compute/010.jpg)

The tradeoffs.

So when you're cheating, it's all about making trade-offs. There are several factors that come into mind, but in my view, the biggest one is time because that's what you're billed on.

![Image 63: A list of the steps involved in a cold start of an AI workload.](https://cdn.xeiaso.net/file/christine-static/talks/2025/nomadic-compute/011.jpg)

A list of the steps involved in a cold start of an AI workload.

Specifically, cold start time or the time that it takes to go from the service not running to the service running. Here's an example of all of the steps involved in running a workload on some cloud provider somewhere.

Statistically, Docker is the universal package format of the internet. It's going to be in a Docker image that has to be pulled and video stuff is like gigabytes of random C++ libraries and a whole bunch of bytecode for GPUs that you don't have, but has to ship around anyway because who knows, you might run it on a 2060.

That gets pulled, extracted, it gets started. Your app boots up, realizes, "Oh, I don't have any models. I need to pull them down."

And then that time that it takes from pulling the models to loading the models is time where you're on the clock doing nothing useful. But once you get to the point where the models are loaded, you can inference them, do whatever it is and somehow make profit. But everything above that inference model step is effectively wasted time.

Depending on the platform you're using, this can cost you money doing nothing.

![Image 64: A perfectly normal drawing of Sonic the Hedgehog.](https://cdn.xeiaso.net/file/christine-static/talks/2025/nomadic-compute/012.jpg)

A perfectly normal drawing of Sonic the Hedgehog.

How can we make it fast? How can we give our infrastructure Sanic speed? Users don't care if you're trying to cheap out. They care about responsiveness. There's two ways to handle this and both are different ways of cheating.

![Image 65: Batch operations.](https://cdn.xeiaso.net/file/christine-static/talks/2025/nomadic-compute/013.jpg)

Batch operations.

One of the biggest ways to cheat is to make your workloads happen on a regular basis where you can do a whole bunch of stuff en masse. This is called batch operations. This is how the US financial system works. This is a horrifying thing. You bundle everything up into big batches and do them every 6, 12, 24 hours, whatever father time says you should do.

This is great. Let's say you have a wallpaper of the day app and you want to have it every wallpaper generated by AI for some reason. Statistically, if there's the wallpaper of the day, you don't need to run it more than once a day. So you can just have it cron job, start it up, generate the wallpaper, put it into storage somewhere. Mark it as ready for the world after it passes some basic filtering. Bob's your uncle, you're good.

This lets you run the most expensive part of your app on pennies for the dollar using any model that you want that you have the bytes for. So that you can't have your upstream infrastructure provider say, "Oh, we're going to turn off the model you're using. Good luck!"

![Image 66: Speed up downloads.](https://cdn.xeiaso.net/file/christine-static/talks/2025/nomadic-compute/014.jpg)

Speed up downloads.

But the other way to cheat is to speed up the cold start process. Let's look at that list again.

![Image 67: Another copy of the list of cold start operations.](https://cdn.xeiaso.net/file/christine-static/talks/2025/nomadic-compute/015.jpg)

Another copy of the list of cold start operations.

Pulling models is the slowest part because that's usually done by your Python program and Python is still single threaded in Anno Dominium two thousand and twenty-five. Your app has to sit there doing nothing waiting for the model to pull and get ready. This can take minutes if you're unlucky and take tens of minutes if you're really unlucky.

What if you could cheat by doing it in a phase where you're not billed? You could just put it into the Docker image with the runtime, right? So I did this and to my horror, it worked kind of well.

There's just like many problems.

![Image 68: Docker hates this](https://cdn.xeiaso.net/file/christine-static/talks/2025/nomadic-compute/017.jpg)

Docker hates this

Number one, Docker hates this. Docker absolutely despises this because the way that Docker works is that it's a bunch of tar balls in a trench coat, right? In order to pull a Docker image, you have to extract all the tar balls. It can only extract one of the tar balls at once because tar balls are weird.

And if you have a Flux dev, that's like a 12 billion parameter model. So we're talking about like 26 gigabytes of floating point numbers, including the model, the autoencoder and whatever else it has.

But this isn't time you have to pay for, but it is time that users may notice. But we're cheating, so you could just do it for batch operations.

If you want to do this anyways, here's a trick I learned:

Model weights don't change often. So what you can do is you can make a separate Docker image that has all of the model weights and then link those model weights into your runtime image.

```
FROM anu-registry.fly.dev/models/waifuwave AS models

FROM anu-registry.fly.dev/runners/comfyui:latest

COPY --link --from=models /opt/comfyui/models/checkpoints /opt/comfyui/models/checkpoints
COPY --link --from=models /opt/comfyui/models/embeddings /opt/comfyui/models/embeddings
COPY --link --from=models /opt/comfyui/models/loras /opt/comfyui/models/loras
COPY --link --from=models /opt/comfyui/models/vae /opt/comfyui/models/vae
```

![Image 69: Aoi is facepalm](https://stickers.xeiaso.net/sticker/aoi/facepalm)

<[**Aoi**](https://xeiaso.net/characters#aoi)\>

This works. I'm horrified.

You get to reuse these models between that because if you have a base stable diffusion checkpoint and each LoRA in a separate layer, you can just have those be there in the image by default. And if you need to download a separate LoRa, you can do that at runtime and only have to download like 150 megs instead of like 5 gigs. That's a lot faster.

And you can also reuse them between projects or workloads, which might be preferable depending on what you're doing.

![Image 70: The Docker Hub hates this](https://cdn.xeiaso.net/file/christine-static/talks/2025/nomadic-compute/019.jpg)

The Docker Hub hates this

Other big problem when you're doing this, the Docker Hub will not allow this. It has a maximum layer size of like 10 gigabytes and maximum image size of 10 gigabytes. And my testing that uses stable diffusion 1.5 from 2023 is an 11 gigabyte image.

GitHub's container registry barely tolerated it. I had to use my own registry. It's not that hard. Registries are basically asset flipping S3 and I work for a company that that is basically S3. So this is easy to do and I can tell you how to do it after the talk. I have stickers.

![Image 71: The upsides of doing this](https://cdn.xeiaso.net/file/christine-static/talks/2025/nomadic-compute/020.jpg)

The upsides of doing this

But the biggest upside of doing this horrific horrific crime is that your one deploy artifact has both your application code and your weights. This is something that doesn't sound like a big advantage until you've had your model get removed from hugging face or Civitai. And then you have a production incident that you can't easily resolve because nobody has the model cached.

![Image 72: Numa is disgust](https://stickers.xeiaso.net/sticker/numa/disgust)

<[**Numa**](https://xeiaso.net/characters#numa)\>

Ask me how I know.

![Image 73: The two of them meme edited to be 'one of them'](https://cdn.xeiaso.net/file/christine-static/talks/2025/nomadic-compute/021.jpg)

The two of them meme edited to be 'one of them'

And because there's just one of them, you don't have multiple artifacts to wrangle. You don't have to like have extra logic to download weights. It's amazing how much code you don't have to write when you don't have to write it.

![Image 74: The Nomadic Compute cover image having a robot hunting down deals](https://cdn.xeiaso.net/file/christine-static/talks/2025/nomadic-compute/022.jpg)

The Nomadic Compute cover image having a robot hunting down deals

But this is the key idea in a nomadic compute setup. Your workload ships with everything it needs so that it can start up quickly, head out to hunt whatever deals it can, get the job done and then head back to the cave to slumber or something. The metaphor fell apart. I'm sorry.

You also don't need to be beholden to any cloud provider because if you can execute AMD 64 byte code and you have an Nvidia GPU and there's a modern ish version of CUDA, it doesn't matter. Everything else is fungible. The only way that you'd really be locked in is if you're using local storage and remember we're trying to save money. So we're not.

So you can just use tools like [Skypilot](https://docs.skypilot.co/en/latest/docs/index.html). It just works.

![Image 75: Live demo](https://cdn.xeiaso.net/file/christine-static/talks/2025/nomadic-compute/023.jpg)

Live demo

Okay, so let's tempt God.

I am a very good at web design, so this is an HTML 1.0 form. My demo is a button on a page and if you click the button, you get anime women:

[![Image 76: A profile shot of a brown-haired anime woman looking up to the sky, made with Counterfeit v3.0](https://cdn.xeiaso.net/file/christine-static/talks/2025/nomadic-compute/waifu_00010_.jpg)](https://cdn.xeiaso.net/file/christine-static/talks/2025/nomadic-compute/waifu_00010_.jpg)

A profile shot of a brown-haired anime woman looking up to the sky, made with Counterfeit v3.0

See that was that was hallucinated by a GPU that spun up on demand and it'll shut down when we're done. I'm glad that worked.

![Image 77: List of special thanks](https://cdn.xeiaso.net/file/christine-static/talks/2025/nomadic-compute/024.jpg)

List of special thanks

Special thanks to all these people. You know what you did if you're on this list. You know what you didn't if you're not.

![Image 78: Final slide with Xe's contact info](https://cdn.xeiaso.net/file/christine-static/talks/2025/nomadic-compute/025.jpg)

Final slide with Xe's contact info

And with that, I've been Xe. If you have any questions, please ask. I don't bite.

* * *

Facts and circumstances may have changed since publication. Please contact me before jumping to conclusions if something seems wrong or unclear.

Tags:

View slides

Copyright 2012-2025 Xe Iaso. Any and all opinions listed here are my own and not representative of any of my employers, past, future, and/or present.

Served by xesite v4 (/app/xesite) with site version [dce820ad](https://github.com/Xe/site/commit/dce820ad49b10355a137911df5386d15fdb9ec9f) , source code available [here](https://github.com/Xe/site).
