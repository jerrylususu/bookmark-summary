Title: Building Python tools with a one-shot prompt using uv run and Claude Projects

URL Source: https://simonwillison.net/2024/Dec/19/one-shot-python-tools/

Markdown Content:
19th December 2024

I’ve written a lot about how I’ve been using Claude to build one-shot HTML+JavaScript applications [via Claude Artifacts](https://simonwillison.net/tags/claude-artifacts/). I recently started using a similar pattern to create one-shot Python utilities, using a custom Claude Project combined with the dependency management capabilities of [uv](https://github.com/astral-sh/uv).

(In LLM jargon a “one-shot” prompt is a prompt that produces the complete desired result on the first attempt.)

I’ll start with an example of a tool I built that way.

I had another round of battle with Amazon S3 today trying to figure out why a file in one of my buckets couldn’t be accessed via a public URL.

Out of frustration I prompted Claude with a variant of the following ([full transcript here](https://gist.github.com/simonw/9f69cf35889b0445b80eeed691d44504)):

> `I can't access the file at EXAMPLE_S3_URL. Write me a Python CLI tool using Click and boto3 which takes a URL of that form and then uses EVERY single boto3 trick in the book to try and debug why the file is returning a 404`

It wrote me [this script](https://github.com/simonw/tools/blob/main/python/debug_s3_access.py), which gave me exactly what I needed. I ran it like this:

uv run debug\_s3\_access.py \\
  https://test-public-bucket-simonw.s3.us-east-1.amazonaws.com/0f550b7b28264d7ea2b3d360e3381a95.jpg

![Image 5: Terminal screenshot showing S3 access analysis results. Command: '$ uv run http://tools.simonwillison.net/python/debug_s3_access.py url-to-image' followed by detailed output showing bucket exists (Yes), region (default), key exists (Yes), bucket policy (AllowAllGetObject), bucket owner (swillison), versioning (Not enabled), content type (image/jpeg), size (71683 bytes), last modified (2024-12-19 03:43:30+00:00) and public access settings (all False)](https://static.simonwillison.net/static/2024/debug-s3.jpg)

You can [see the text output here](https://github.com/simonw/tools/tree/main/python#debug_s3_accesspy).

#### Inline dependencies and uv run [#](https://simonwillison.net/2024/Dec/19/one-shot-python-tools/#inline-dependencies-and-uv-run)

Crucially, I didn’t have to take any extra steps to install any of the dependencies that the script needed. That’s because the script starts with this magic comment:

\# /// script
\# requires-python = "\>\=3.12"
\# dependencies = \[
\#     "click",
\#     "boto3",
\#     "urllib3",
\#     "rich",
\# \]
\# ///

This is an example of [inline script dependencies](https://docs.astral.sh/uv/guides/scripts/#declaring-script-dependencies), a feature described in [PEP 723](https://peps.python.org/pep-0723/) and implemented by `uv run`. Running the script causes `uv` to create a temporary virtual environment with those dependencies installed, a process that takes just a few milliseconds once the `uv` cache has been populated.

This even works if the script is specified by a URL! Anyone with `uv` installed can run the following command (provided you trust me not to have replaced the script with something malicious) to debug one of their own S3 buckets:

uv run http://tools.simonwillison.net/python/debug\_s3\_access.py \\
  https://test-public-bucket-simonw.s3.us-east-1.amazonaws.com/0f550b7b28264d7ea2b3d360e3381a95.jpg

#### Writing these with the help of a Claude Project [#](https://simonwillison.net/2024/Dec/19/one-shot-python-tools/#writing-these-with-the-help-of-a-claude-project)

The reason I can one-shot scripts like this now is that I’ve set up a [Claude Project](https://www.anthropic.com/news/projects) called “Python app”. Projects can have custom instructions, and I used those to “teach” Claude how to take advantage of inline script dependencies:

> You write Python tools as single files. They always start with this comment:
> 
> \# /// script
> \# requires-python = "\>\=3.12"
> \# ///
> 
> These files can include dependencies on libraries such as Click. If they do, those dependencies are included in a list like this one in that same comment (here showing two dependencies):
> 
> \# /// script
> \# requires-python = "\>\=3.12"
> \# dependencies = \[
> \#     "click",
> \#     "sqlite-utils",
> \# \]
> \# ///

That’s everything Claude needs to reliably knock out full-featured Python tools as single scripts which can be run directly using whatever dependencies Claude chose to include.

I didn’t suggest that Claude use [rich](https://github.com/Textualize/rich) for the `debug_s3_access.py` script earlier but it decided to use it anyway!

I’ve only recently started experimenting with this pattern but it seems to work _really_ well. Here’s another example—my prompt was:

> `Starlette web app that provides an API where you pass in ?url= and it strips all HTML tags and returns just the text, using beautifulsoup`

Here’s [the chat transcript](https://gist.github.com/simonw/08957a1490ebde1ea38b4a8374989cf8) and [the raw code it produced](https://gist.githubusercontent.com/simonw/08957a1490ebde1ea38b4a8374989cf8/raw/143ee24dc65ca109b094b72e8b8c494369e763d6/strip_html.py). You can run that server directly on your machine (it uses port 8000) like this:

uv run https://gist.githubusercontent.com/simonw/08957a1490ebde1ea38b4a8374989cf8/raw/143ee24dc65ca109b094b72e8b8c494369e763d6/strip\_html.py

Then visit `http://127.0.0.1:8000/?url=https://simonwillison.net/` to see it in action.

#### Custom instructions [#](https://simonwillison.net/2024/Dec/19/one-shot-python-tools/#custom-instructions)

The pattern here that’s most interesting to me is using custom instructions or system prompts to show LLMs how to implement new patterns that may not exist in their training data. `uv run` is less than a year old, but providing just a short example is enough to get the models to write code that takes advantage of its capabilities.

I have a similar set of custom instructions I use for creating single page HTML and JavaScript tools, again running in a Claude Project:

> Never use React in artifacts—always plain HTML and vanilla JavaScript and CSS with minimal dependencies.
> 
> CSS should be indented with two spaces and should start like this:
> 
> <style\>
> \* {
>   box-sizing: border-box;
> }
> 
> Inputs and textareas should be font size 16px. Font should always prefer Helvetica.
> 
> JavaScript should be two space indents and start like this:
> 
> <script type\="module"\>
> // code in here should not be indented at the first level
