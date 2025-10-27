Title: How I Coding? (Oct 2025 Edition)

URL Source: https://xuanwo.io/2025/07-how-i-coding-oct-2025-edition/

Markdown Content:
Just one week after I published my [Setp 2025 edition of How I vibe coding](https://xuanwo.io/2025/06-how-i-vibe-coding-sept-2025-edition/), Anthropic released Claude Sonnet 4.5. That's a quick reminder that in this field, SOTA doesn't stay still. This post updates my mindset after a month with the new model.

Mindset
-------

There is one addition to my mindset: **slow is fast**.

The more time I spend on coding, the more I realize that **attention** is my most important resource. The bottleneck is increasingly becoming which task I choose to focus on. Faster models don’t necessarily make people more productive, they consume attention rather than free up capacity.

There is a matrix around quality and speed: `{high, low} * {quality, speed}`. Obviously we should avoid low quality and low speed, but high quality and high speed is not achievable. The tradeoff then comes down to choosing quality or speed, that’s the question.

My understanding now is that quality is the most important thing. It's more acceptable to me that a model is slow but produces high quality results. At the current stage, attention is my most valuable resource, and I need to allocate it wisely. A slow but correct model consumes less of my attention and lets me focus on finding the right path. A fast but flawed model drains all my attention just to fix its errors, remove unnecessary comments and tests, or correct the lies it keeps telling.

The improvement brought by model updates seems smaller and smaller. Claude Sonnet 4.5 may be better than Claude Sonnet 4, but still not as good as Claude Opus 4.1. I believe people like Claude Sonnet 4.5 mainly because it is much cheaper and faster than Claude Opus 4.1. People said that Claude Sonnet 4.5 is good enough. But I don't think so after stuck in a dead loop for long time. Now I care more about quality than cost (both in money and time).

A fast model that drains my attention is slower in the long run. Slow models that get things right free me to think, and that’s what real speed feels like.

Toolset
-------

No change, still using [codex](https://github.com/openai/codex), [xlaude](https://github.com/Xuanwo/xlaude) and [zed](https://zed.dev/).

_More details could be found at [Setp 2025 edition](https://xuanwo.io/2025/06-how-i-vibe-coding-sept-2025-edition/)_

One experiment I tried this month is using Codex via Cloud, Slack, and GitHub. Here are my thoughts:

### Codex From Cloud

It’s tempting to spawn tasks over the cloud, just delegate and walk away. I can monitor progress from my browser or phone, which feels convenient.

But it doesn’t work well for me because:

*   Setting up the environment is still hard and time consuming. There are many assumptions about tools that should be available in context. Some projects require complex setups for multiple services, which Codex doesn’t handle well.
*   The runtime environment has very limited resources. Building and compiling Rust code is painfully slow.

As a result, I rarely use Cloud Codex for real tasks. The only useful cases I’ve found are for asking questions and exploring codebases—like querying the system as if it were an architect. These tasks aren’t time sensitive, so running them in the cloud feels cozy. I just check the results later.

### Codex From Slack

I integrated Codex into our team’s Slack. But it’s still at a very early stage: It’s just a quick shortcut to start a new task. All you get are two notifications: “I’m running” and “I’m finished.” It can’t submit PRs directly from Slack, can’t comment on results in chat, and can’t hold a conversation. Every operation requires clicking through to the Cloud task page.

This design makes Slack Codex integration far less useful than I expected. I haven’t tried Cursor yet, does it work better?

### Codex From GitHub

Codex also has GitHub integration: you can enable Codex reviews and request changes. But again, it’s essentially just a way to trigger a Cloud Codex task. The overall UX is underwhelming.

That said, I’ve noticed that Codex’s code reviews are surprisingly high quality. It catches real, important bugs in PRs, not the meaningless nitpicks that GitHub Copilot often delivers. When everything looks fine, it just leaves a simple 👍. I like this approach.

The maintainer still needs to review PRs themselves, but CodeX reviews have at least been helpful instead of adding more work for maintainers. I believe it’s already a big improvement.

Tips
----

### Subscription-based plans have become mainstream

Today, [Kimi announced a coding plan for users](https://mp.weixin.qq.com/s/uC9bZX8fPwNj1mYALdv5yQ). Nearly all major model providers have shifted to subscription-based models. I believe this is the trend. Just like how everyone now uses mobile data plans instead of paying per GB. That’s human nature: people prefer predictable, affordable pricing.

This shift also pushes service providers to improve cost efficiency and quality. I’m not overly concerned about providers “dumbing down” their services because the market is fiercely competitive. Reducing quality means losing users to competitors.

### Focus on SOTA

One of my friends complains there’s too much new stuff to keep up with every day. I agree. It’s true. But you can allocate your attention wisely: focus only on SOTA models and use the best available in your daily work. Don’t get caught up in debates over whether Model A is better than Model B on Task X.

We are developers. Our attention is our most valuable resource. Allocate it carefully. It’s not our job to hunt down the absolute best models, the market will reveal them. Sometimes it’s unclear what’s truly the best, but SOTA is easy to identify. As of now, the top choices are OpenAI, Anthropic, and Google. I’m not including Qwen since Qwen3 Max isn’t affordable for coding use. Pick one from these three based on your preference.

Reevaluate this decision every one to three months. At other times, you’re still a developer. AI news should occupy no more than 10% of your input information. Focus instead on your language, tools, frameworks, and industry trends.

* * *

Hope you're enjoying the coding as before.