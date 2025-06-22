Title: My First Open Source AI Generated Library

URL Source: https://simonwillison.net/2025/Jun/21/my-first-open-source-ai-generated-library/

Markdown Content:
**[My First Open Source AI Generated Library](https://lucumr.pocoo.org/2025/6/21/my-first-ai-library/)** ([via](https://bsky.app/profile/mitsuhiko.at/post/3ls4ov5fk7c2l "@mitsuhiko.at")) Armin Ronacher had Claude and Claude Code do almost _all of the work_ in building, testing, packaging and publishing a new Python library based on his design:

> *   It wrote ~1100 lines of code for the parser
> *   It wrote ~1000 lines of tests
> *   It configured the entire Python package, CI, PyPI publishing
> *   Generated a README, drafted a changelog, designed a logo, made it theme-aware
> *   Did multiple refactorings to make me happier

The project? [sloppy-xml-py](https://github.com/mitsuhiko/sloppy-xml-py), a lax XML parser (and violation of everything the XML Working Group hold sacred) which ironically is necessary because LLMs themselves frequently output "XML" that includes validation errors.

Claude's SVG logo design is actually pretty decent, turns out it can draw [more than just bad pelicans](https://simonwillison.net/2025/May/22/code-with-claude-live-blog/#live-update-357)!

![Image 1: Hand drawn style, orange rough rectangly containing < { s } > - then the text Sloppy XML below in black](https://static.simonwillison.net/static/2025/sloppy-xml.jpg)
I think experiments like this are a really valuable way to explore the capabilities of these models. Armin's conclusion:

> This was an experiment to see how far I could get with minimal manual effort, and to unstick myself from an annoying blocker. The result is good enough for my immediate use case and I also felt good enough to publish it to PyPI in case someone else has the same problem.
> 
> 
> Treat it as a curious side project which says more about what's possible today than what's necessarily advisable.

I'd like to present a slightly different conclusion here. The most interesting thing about this project is that **the code is good**.

My criteria for good code these days is the following:

1.   Solves a defined problem, well enough that I'm not tempted to solve it in a different way
2.   Uses minimal dependencies
3.   Clear and easy to understand
4.   Well tested, with tests prove that the code does what it's meant to do
5.   Comprehensive documentation
6.   Packaged and published in a way that makes it convenient for me to use
7.   Designed to be easy to maintain and make changes in the future

`sloppy-xml-py` fits all of those criteria. It's useful, well defined, [the code is readable](https://github.com/mitsuhiko/sloppy-xml-py/blob/main/sloppy_xml.py) with just about the right level of comments, everything is tested, the documentation explains everything I need to know, and it's been shipped to PyPI.

I'd be proud to have written this myself.

This example is _not_ an argument for replacing programmers with LLMs. The code is good because Armin is an expert programmer who stayed in full control throughout the process. As I wrote the other day, [a skilled individual with both deep domain understanding and deep understanding of the capabilities of the agent](https://simonwillison.net/2025/Jun/18/coding-agents/).
