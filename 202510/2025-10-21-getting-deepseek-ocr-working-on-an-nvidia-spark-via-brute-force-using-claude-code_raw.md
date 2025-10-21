Title: Getting DeepSeek-OCR working on an NVIDIA Spark via brute force using Claude Code

URL Source: https://simonwillison.net/2025/Oct/20/deepseek-ocr-claude-code/

Published Time: Tue, 21 Oct 2025 13:32:14 GMT

Markdown Content:
20th October 2025

DeepSeek released a new model yesterday: [DeepSeek-OCR](https://github.com/deepseek-ai/DeepSeek-OCR), a 6.6GB model fine-tuned specifically for OCR. They released it as model weights that run using PyTorch and CUDA. I got it running on the NVIDIA Spark by having Claude Code effectively brute force the challenge of getting it working on that particular hardware.

This small project (40 minutes this morning, most of which was Claude Code churning away while I had breakfast and did some other things) ties together a bunch of different concepts I’ve been exploring recently. I [designed an agentic loop](https://simonwillison.net/2025/Sep/30/designing-agentic-loops/) for the problem, gave Claude full permissions inside a Docker sandbox, embraced the [parallel agents lifestyle](https://simonwillison.net/2025/Oct/5/parallel-coding-agents/) and reused my [notes on the NVIDIA Spark](https://simonwillison.net/2025/Oct/14/nvidia-dgx-spark/) from last week.

I knew getting a PyTorch CUDA model running on the Spark was going to be a little frustrating, so I decided to outsource the entire process to Claude Code to see what would happen.

TLDR: It worked. It took four prompts (one long, three very short) to have Claude Code figure out everything necessary to run the new DeepSeek model on the NVIDIA Spark, OCR a document for me and produce _copious_ notes about the process.

#### The setup

I connected to the Spark from my Mac via SSH and started a new Docker container there:

docker run -it --gpus=all \
  -v /usr/local/cuda:/usr/local/cuda:ro \
  nvcr.io/nvidia/cuda:13.0.1-devel-ubuntu24.04 \
  bash

Then I installed npm and used that to install Claude Code:

apt-get update
DEBIAN_FRONTEND=noninteractive TZ=Etc/UTC apt-get install -y npm
npm install -g @anthropic-ai/claude-code

Then started Claude Code, telling it that it’s OK that it’s running as `root` because it’s in a sandbox:

IS_SANDBOX=1 claude --dangerously-skip-permissions

It provided me a URL to click on to authenticate with my Anthropic account.

#### The initial prompts

I kicked things off with this prompt:

> Create a folder deepseek-ocr and do everything else in that folder

Then I ran the following, providing links to both the GitHub repository and the Hugging Face model, providing a clue about NVIDIA ARM and giving it an image ([this one](https://static.simonwillison.net/static/2025/ft.jpeg), see [previous post](https://simonwillison.net/2025/Aug/29/the-perils-of-vibe-coding/)) that I wanted it to run OCR on.

> Your task is to get this working: [https://github.com/deepseek-ai/DeepSeek-OCR](https://github.com/deepseek-ai/DeepSeek-OCR)—it uses Hugging Face Transformers and models from [https://huggingface.co/deepseek-ai/DeepSeek-OCR](https://huggingface.co/deepseek-ai/DeepSeek-OCR)—you are running in a Docker container on an NVIDIA ARM device, first research your environment to check it will be possible to do this. Git clone both of those—you may need to enable LFS first. Make extensive notes as you go in a notes.md file which you should only ever append new notes to. At the end of this you should have scripts in the folder which can be run to both setup and then run the model against an example—use [https://static.simonwillison.net/static/2025/ft.jpeg](https://static.simonwillison.net/static/2025/ft.jpeg) as the example image that you OCR. As a final step create a detailed README.md file explaining the project and what you learned and how to run your code.

Note how I also told it to “make extensive notes as you go in a notes.md file which you should only ever append new notes to” so I’d have some useful notes at the end.

#### The follow-ups

It churned away for 13 minutes, and made a sequence of discoveries about the platform and the model and the difficulties of running PyTorch on it.

And then... [it gave up](https://github.com/simonw/research/blob/main/deepseek-ocr-nvidia-spark/claude-log.md#-assistant--2025-10-20-154706):

> **The NVIDIA GB10 GPU has compute capability sm_121, which is too new for PyTorch 2.5.1**
> 
> 
> *   PyTorch 2.5.1 supports: sm_50, sm_80, sm_86, sm_89, sm_90, sm_90a
> *   GB10 requires: sm_121
> *   Error: `CUDA error: no kernel image is available for execution on the device`
> 
> 
> Additionally, the model has hardcoded `.cuda()` calls, preventing CPU fallback without code modifications.

So I gave it some encouragement:

> Any other options that might help get CUDA working like using different versions of PyTorch that have available CUDA wheels for this platform? Have you checked to see what PyTorch versions already have these ARM CUDA wheels that would work here?

It ran this command to grep for all available PyTorch wheels on `download.pytorch.org` that match the ARM architecture:

curl -s https://download.pytorch.org/whl/torch/ | grep -o 'torch-[0-9.]*.*aarch64.whl' | sort -V | tail -20

... and that unblocked it.

> Excellent! I can see that PyTorch 2.9.0 has ARM64 wheels for CUDA 12.8, 12.9, and **CUDA 13.0** (cu130)! This is exactly what we need!

It installed the wheels it found and reported:

> Good news! PyTorch 2.9.0 can detect the GB10 GPU with CUDA capability 12.1 (sm_121), but it says the maximum supported is 12.0. However, it’s just a warning now instead of a hard error! Let’s try running inference: [...]

Then kept on churning for a bit, ignoring warnings, and managed to [run the model](https://github.com/simonw/research/blob/main/deepseek-ocr-nvidia-spark/claude-log.md#-user--2025-10-20-155056)! It loaded the image and ran this prompt:

```
<|grounding|>OCR this image.
```

And got back output that started like this:

```
<|ref|>The perils of vibe coding<|/ref|><|det|>[[352, 30, 624, 111]]<|/det|>
<|ref|>opt<|/ref|><|det|>[[970, 0, 994, 30]]<|/det|>
<|ref|>such<|/ref|><|det|>[[970, 24, 996, 58]]<|/det|>
<|ref|>days<|/ref|><|det|>[[970, 52, 996, 87]]<|/det|>
<|ref|>pavi<|/ref|><|det|>[[970, 85, 996, 118]]<|/det|>
<|ref|>TECHNOLOGY<|/ref|><|det|>[[33, 199, 127, 230]]<|/det|>
<|ref|>holds the promise of replacing program-<|/ref|><|det|>[[220, 170, 390, 210]]<|/det|>
<|ref|>mers - a profession of very well paid<|/ref|><|det|>[[220, 199, 390, 238]]<|/det|>
<|ref|>people.For another, the work can be<|/ref|><|det|>[[220, 228, 390, 267]]<|/det|>
```

Claude declared victory and pointed me to the [output/result.mmd](https://github.com/simonw/research/blob/main/deepseek-ocr-nvidia-spark/output/result.mmd?short_path=f43da6a) file, which contained only whitespace. So OCR had worked but the result had failed to be written correctly to disk.

I [said](https://github.com/simonw/research/blob/main/deepseek-ocr-nvidia-spark/claude-log.md#-user--2025-10-20-155826):

> That result.mmd file looks to be exclusively whitespace to me, try and get a better result there—the bounding box image was good though

Which caused Claude to [reconsider](https://github.com/simonw/research/blob/main/deepseek-ocr-nvidia-spark/claude-log.md#-assistant--2025-10-20-155900) the prompt it used:

> Maybe we need to use a different prompt. Looking at the README from DeepSeek-OCR, there are different prompts:
> 
> 
> *   `"<image>\n<|grounding|>Convert the document to markdown."`—for documents
> *   `"<image>\n<|grounding|>OCR this image."`—general OCR
> *   `"<image>\nFree OCR."`—without layouts
> 
> 
> The “grounding” mode seems to be focused on bounding boxes, which is why we got good bounding box results but the text output might be in a different format.
> 
> 
> Let me try running it again with a different prompt that’s more focused on text extraction rather than grounding.

It tried all of the prompt variants, [made a note about them](https://github.com/simonw/research/blob/main/deepseek-ocr-nvidia-spark/notes.md#text-output-improvement-2025-10-20-1601) and created a file called [PROMPTS_GUIDE.md](https://github.com/simonw/research/blob/main/deepseek-ocr-nvidia-spark/PROMPTS_GUIDE.md) with a bunch more details, including this comparison table:

> | Prompt | Speed | Text Quality | Structure | Coordinates | Best Use Case |
> | --- | --- | --- | --- | --- | --- |
> | **Free OCR** | ⚡⚡⚡ Fast | ⭐⭐⭐ Excellent | ⭐ Basic | ❌ No | **General OCR** |
> | Markdown | ⚡⚡ Medium | ⭐⭐⭐ Excellent | ⭐⭐⭐ Full | ⭐⭐ Partial | Documents |
> | Grounding | ⚡ Slow | ⭐⭐ Good | ⭐ Basic | ⭐⭐⭐ Full | Annotations |
> | Detailed | ⚡⚡⚡ Fastest | ⭐ N/A | ❌ N/A | ❌ No | Image analysis |

And this table under the heading “Performance Benchmarks”:

> Test image: 3503×1668 pixels (Financial Times article)
> 
> 
> | Prompt | Time | Output Size | Tokens |
> | --- | --- | --- | --- |
> | Free OCR | 24s | Clean text | 2257 |
> | Markdown | 39s | Formatted MD | 2257 + structure |
> | Grounding | 58s | Text + coords | 2257 + boxes |
> | Detailed | 9s | Description | ~300 |

My final prompt was this, to gather everything together into a zip file I could extract from the Docker container:

> Create a zip file with the output and output_text and all of the scripts and notes—but leave out the github repo and the huggingface repo directories

I added the contents of that zip file to my new [simonw/research](https://github.com/simonw/research) GitHub repo [in the deepseek-ocr-nvidia-spark](https://github.com/simonw/research/tree/main/deepseek-ocr-nvidia-spark) folder.

Claude really likes writing notes! Here’s the directory listing of that finished folder:

```
|-- download_test_image.sh
  |-- FINAL_SUMMARY.md
  |-- notes.md
  |-- output
  |   |-- images
  |   |-- result_with_boxes.jpg
  |   `-- result.mmd
  |-- output_text
  |   |-- detailed
  |   |   |-- images
  |   |   |-- result_with_boxes.jpg
  |   |   `-- result.mmd
  |   |-- free_ocr
  |   |   |-- images
  |   |   |-- result_with_boxes.jpg
  |   |   `-- result.mmd
  |   `-- markdown
  |       |-- images
  |       |   `-- 0.jpg
  |       |-- result_with_boxes.jpg
  |       `-- result.mmd
  |-- PROMPTS_GUIDE.md
  |-- README_SUCCESS.md
  |-- README.md
  |-- run_ocr_best.py
  |-- run_ocr_cpu_nocuda.py
  |-- run_ocr_cpu.py
  |-- run_ocr_text_focused.py
  |-- run_ocr.py
  |-- run_ocr.sh
  |-- setup.sh
  |-- SOLUTION.md
  |-- test_image.jpeg
  |-- TEXT_OUTPUT_SUMMARY.md
  `-- UPDATE_PYTORCH.md
```

#### Takeaways

My first prompt was at 15:31:07 (UTC). The final message from Claude Code came in at 16:10:03. That means it took less than 40 minutes start to finish, and I was only actively involved for about 5-10 minutes of that time. The rest of the time I was having breakfast and doing other things.

Having tried and failed to get PyTorch stuff working in the past, I count this as a _huge_ win. I’ll be using this process a whole lot more in the future.

How good were the actual results? There’s honestly so much material in the resulting notes created by Claude that I haven’t reviewed all of it. There may well be all sorts of errors in there, but it’s indisputable that it managed to run the model and made notes on how it did that such that I’ll be able to do the same thing in the future.

I think the key factors in executing this project successfully were the following:

1.   I gave it exactly what it needed: a Docker environment in the target hardware, instructions on where to get what it needed (the code and the model) and a clear goal for it to pursue. This is a great example of the pattern I described in [designing agentic loops](https://simonwillison.net/2025/Sep/30/designing-agentic-loops/).
2.   Running it in a Docker sandbox meant I could use `claude --dangerously-skip-permissions` and leave it running on its own. If I’d had to approve every command it wanted to run I would have got frustrated and quit the project after just a few minutes.
3.   I applied my own knowledge and experience when it got stuck. I was confident (based on [previous experiments](https://simonwillison.net/2025/Oct/14/nvidia-dgx-spark/#claude-code-for-everything) with the Spark) that a CUDA wheel for ARM64 existed that was likely to work, so when it gave up I prompted it to try again, leading to success.

Oh, and it looks like DeepSeek OCR is a pretty good model if you spend the time experimenting with different ways to run it.

#### Bonus: Using VS Code to monitor the container

A small TIL from today: I had kicked off the job running in the Docker container via SSH to the Spark when I realized it would be neat if I could easily monitor the files it was creating while it was running.

I [asked Claude.ai](https://claude.ai/share/68a0ebff-b586-4278-bd91-6b715a657d2b):

> I am running a Docker container on a remote machine, which I started over SSH
> 
> 
> How can I have my local VS Code on MacOS show me the filesystem in that docker container inside that remote machine, without restarting anything?

It gave me a set of steps that solved this exact problem:

1.   Install the VS Code “Remote SSH” and “Dev Containers” extensions
2.   Use “Remote-SSH: Connect to Host” to connect to the remote machine (on my Tailscale network that’s `spark@100.113.1.114`)
3.   In the window for that remote SSH session, run “Dev Containers: Attach to Running Container”—this shows a list of containers and you can select the one you want to attach to
4.   ... and that’s it! VS Code opens a new window providing full access to all of the files in that container. I opened up `notes.md` and watched it as Claude Code appended to it in real time.

At the end when I told Claude to create a zip file of the results I could select that in the VS Code file explorer and use the “Download” menu item to download it to my Mac.