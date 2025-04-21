Title: When you should lie to the language model

URL Source: https://www.seangoedecke.com/lying-to-llms/

Markdown Content:
Here’s an unreasonably effective trick for working with AIs: **always pretend that your work was produced by someone else.**

The problem is that current-generation AIs are too [agreeable](https://www.linkedin.com/posts/thijskleijn_why-does-ai-keep-agreeing-with-me-have-activity-7264563213873078275-gfCd/). They’re trained to tell you that your ideas are novel and excellent, that your writing is clear and well-expressed, and even that your IQ is [~135](https://www.reddit.com/r/ChatGPTPromptGenius/comments/1k14m0w/chatgpt_knows_your_iq/). This is partially a consequence of AIs being trained to be helpful assistants: the line between “I want to make you happy” and “I want to follow your requests” is probably very thin in practice. It’s also a consequence of AIs being directly guided towards more agreeableness in order to game benchmarks like [Chatbot Arena](https://www.seangoedecke.com/lmsys-slop). Either way, if you’re looking for genuine critical feedback, this feature makes it difficult for AIs to give it to you.

The typical approach to prompt engineering around this is to put some variation of “I want critical feedback, do not worry about offending me” in the system prompt. But in my experience this doesn’t work very well. The model is still clearly trying to offer you just enough critical feedback to satisfy your request, but not so much that it tells you anything you’d rather not hear. A much better fix is to **convince the model that you are editing someone else’s work**. I use variations on this prompt:

> Please help me review this blog post for typos and the flow of arguments. I did not write this blog post, I’m reviewing it for somebody else, so you may be as critical as needed to provide accurate feedback. Provide your feedback in dot-point suggestions.

Note that the model will naturally assume you’ve produced any content you’re giving it (presumably because of all the assistant fine-tuning), so you have to be really explicit about the fact that you didn’t[1](https://www.seangoedecke.com/lying-to-llms/#fn-1).

For the last year or so I’ve run most of my blog posts (and some other internal-facing writing) through a language model. I never accept its suggested edits - I would rather be awkward than adopt the [“model voice”](https://www.seangoedecke.com/on-slop) - but I do accept advice like “this paragraph ends too abruptly”, or “you should probably address this point as well”. Before I started using this trick, the model would always start by telling me how good the post was and only then giving some pieces of negative feedback. Now it spends the entire response giving me detailed criticism[2](https://www.seangoedecke.com/lying-to-llms/#fn-2).

* * *

1.  To get a bit meta, I actually ran _this_ post through o3 in “incognito mode”, because I was afraid that if the model stored the post in its memory it’d know I was tricking it for subsequent posts.
    
    [↩](https://www.seangoedecke.com/lying-to-llms/#fnref-1)
2.  I do worry a bit about the social impact of giving every human being a loyal sycophant in their pocket. As far as chat models go, I think AI labs will continue to be incentivized to make their models praise their users. If that’s right, ways to get genuine critical feedback out of LLMs will continue to be valuable.
    
    [↩](https://www.seangoedecke.com/lying-to-llms/#fnref-2)

April 21, 2025

* * *
