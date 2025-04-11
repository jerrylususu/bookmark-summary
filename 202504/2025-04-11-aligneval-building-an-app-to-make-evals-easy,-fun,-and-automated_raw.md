Title: AlignEval: Building an App to Make Evals Easy, Fun, and Automated

URL Source: https://eugeneyan.com/writing/aligneval/

Published Time: 2024-10-27T00:00:00+00:00

Markdown Content:
Go to [aligneval.com](https://aligneval.com/) to start building your own LLM-evaluator; sample data included.

Every AI-powered product needs evals. But let’s face it—they’re a pain to build, hard to scale, and most teams get them wrong. As a result, many AI-powered experiences are bottlenecked on evals, sometimes delaying launches by weeks or even months.

I’ve spent the past year or so wrestling with product/task-specific evals. Testing different ways to [detect](https://eugeneyan.com/writing/abstractive/) hallucinations, [finetune](https://eugeneyan.com/writing/finetuning/) evaluators, and [evaluate](https://eugeneyan.com/writing/llm-evaluators/) LLM-based evaluators. There were dead ends. There were rabbit holes. But I learned [what works and what doesn’t](https://eugeneyan.com/writing/evals/).

And that’s why I’m excited to introduce [AlignEval](https://aligneval.com/), an app that makes evals easy and… fun? (Okay, I’ll settle for less painful.) It also tries to automate part of the process. AlignEval makes building LLM-evaluators as straightforward as four simple steps:

*   Upload a CSV file with columns for input and output.
*   Look at the data and label samples as pass or fail.
*   Define eval criteria, run the LLM-evaluator, check results.
*   Optimize the LLM-evaluator with dev-test splits.

Align AI to human. Calibrate human to AI. Repeat.[](https://eugeneyan.com/writing/aligneval/#align-ai-to-human-calibrate-human-to-ai-repeat)
--------------------------------------------------------------------------------------------------------------------------------

The key insight is that aligning AI to human preferences is only half the battle. To build effective evals, we must also **calibrate human criteria to AI output**.

Many teams make the mistake of crafting elaborate eval criteria without first **looking at the data**. It’s like theorizing about user experience and defects from the ivory tower, without doing error analysis. From [Who Validates the Validators](https://arxiv.org/abs/2404.12272): “_It is impossible to completely determine evaluation criteria prior to human judging of LLM outputs._”

This leads to two types of bad criteria. First, irrelevant criteria that are a waste of time, such as generic metrics (e.g., helpfulness) or very low probability defects (e.g., grammar, spelling). Second, unrealistic, unattainable criteria that the technology isn’t ready for, such as autonomous agents back in 2023. Either way, teams squander effort that would have been better invested in evaluating actual defects that occur with moderate frequency.

(I think out-of-the-box eval solutions fuel this problem, pushing generic criteria that are easy to plug and play but ignore the idiosyncrasies of your domain, product, and data.)

The way to solve this—and build useful evals—is to work backward from the data. That’s what [AlignEval](https://aligneval.com/) tries to do by putting data and metrics first, not preset criteria or LLMs.

Getting started: Upload some data[](https://eugeneyan.com/writing/aligneval/#getting-started-upload-some-data)
--------------------------------------------------------------------------------------------------------------

**To get started, upload a CSV file containing the following columns:**

*   **id**: Lets you match labeled and evaluated samples to your data
*   **input**: The context provided to the LLM to generate the output (e.g., text to classify, news to summarize, retrieved documents for answering questions)
*   **output**: What the LLM generates (e.g., classification label, summary, answer)
*   **label**: Your judgment on whether the output passes (0) or fails (1)

![Image 1: Instructions to upload a CSV file.](https://eugeneyan.com/assets/upload.jpg)

Instructions to upload a CSV file.

If you don’t have a CSV handy, [download a sample](https://aligneval.com/data/fib50.csv) based on the [Factual Inconsistency Benchmark](https://huggingface.co/datasets/r-three/fib). It contains 50 news articles, each with two summaries. One is factually consistent while the other is not. Perfect for AlignEval’s binary labeling task.

After uploading the CSV, you’ll see the data in a flexible table view. Adjust the width of the browser to control how wide or narrow you want the table and columns to be.

![Image 2: How the table view looks after uploading a CSV file.](https://eugeneyan.com/assets/table.jpg)

How the table view looks after uploading a CSV file.

Labeling mode: Look at the data[](https://eugeneyan.com/writing/aligneval/#labeling-mode-look-at-the-data)
----------------------------------------------------------------------------------------------------------

**In labeling mode, our only job is to look at the data.** AlignEval simplifies the process to a comparison between input and output fields. And for each sample, we only have to make a binary decision—pass or fail.

![Image 3: Instructions for labeling mode.](https://eugeneyan.com/assets/labeling.jpg)

Instructions for labeling mode.

Why binary labels? It leads to more accurate data, takes less time, and keeps cognitive load low. [DoorDash adopted a similar approach](https://eugeneyan.com/writing/content-moderation/#collecting-ground-truth-via-human-in-the-loop). Similarly, [Llama2](https://arxiv.org/abs/2307.09288) focused on collecting binary human preferences. The Llama2 authors also [shared at a meetup](https://www.youtube.com/live/CzR3OrOkM9w?si=gTrb6M44O941wrqb&t=913) that collecting binary preferences was much faster than writing samples for supervised finetuning.

What’s important is that we look at the data with an open mind, and not write criteria based on our priors. We should also resist the urge to prematurely define criteria. We need to first immerse ourselves in the data. This reduces the risk of hunting for nonexistent defects or chasing unrealistic expectations. By understanding what the LLM actually generates, we can define more meaningful, better-calibrated criteria.

Look at your data remix, courtesy of Jason Liu. Sign up for his next RAG course [here](https://maven.com/s/course/b9b1f32583).

After labeling 20 rows, we unlock evaluation mode. (While evaluation mode is available after 20 labels, I think it’s too little to understand the data well enough to define criteria, and too small a sample for evaluation. I suggest aiming for 50-100 before writing criteria and running evals. The more familiar you are with your data, the better your evals will be.)

Evaluation mode: Write criteria, evaluate the evaluator[](https://eugeneyan.com/writing/aligneval/#evaluation-mode-write-criteria-evaluate-the-evaluator)
--------------------------------------------------------------------------------------------------------------------------------

**After unlocking evaluation mode, we can now write our task-specific evaluation criteria.** Keep it simple: Evaluate on a single dimension and return either 0 (pass) or 1 (fail).

![Image 4: Instructions for evaluation mode.](https://eugeneyan.com/assets/evaluation.jpg)

Instructions for evaluation mode.

Here’s the prompt I use for factual inconsistency classification. We start with only two sentences that define what a pass or fail looks like. We can refine it after running the LLM-evaluator and examining the explanations and predictions.

![Image 5: Writing the prompt and selecting models and fields.](https://eugeneyan.com/assets/prompt.jpg)

Writing the prompt and selecting models and fields.

Next, we choose our model (gpt-4o-mini or claude-3-haiku) and input fields (both input and output, or output only). For most tasks, (e.g., classification, summarization, Q&A), we want to compare the output to the input. Nonetheless, for some tasks, like evaluating style guide adherence or tone of voice, we only need the output. Focusing solely on the output reduces token cost and latency while potentially improving performance.

**It’s also crucial to evaluate our LLM-evaluators against the labeled data.** Hit “Evaluate” and we’ll see metrics in the top right corner: sample size, recall, precision, F1, Cohen’s , and counts for true and false positives/negatives.

![Image 6: Metrics to evaluate the LLM-evaluator.](https://eugeneyan.com/assets/metrics.jpg)

Metrics to evaluate the LLM-evaluator.

If our sample size is low (e.g., 20), the metrics can fluctuate a lot, even when we rerun the same LLM-evaluator. This is due to LLM stochasticity. We can improve stability by labeling more data. Aim for at least 50 labeled samples which also unlocks optimization mode.

Optimization mode: Semi-automated improvements 🤞[](https://eugeneyan.com/writing/aligneval/#optimization-mode-semi-automated-improvements-)
--------------------------------------------------------------------------------------------------------------------------------

**Optimization mode is where the magic (hopefully) happens.** Click “Optimize” and let AlignEval do its thing to improve your LLM-evaluator. While it’s still in early beta, it’s achieved decent improvements for several use cases. (And no, it’s not dspy.)

![Image 7: Instructions for optimization mode.](https://eugeneyan.com/assets/optimization.jpg)

Instructions for optimization mode.

Under the hood, optimization splits the labeled data into dev and test sets. (Since we’re not training a model, we call it a development split instead of a training split.) It then runs trials on the dev set to improve F1, using the same LLM and fields from evaluation mode. After trials, the improved LLM-evaluator is evaled on the unseen test set. In the table below, F1 starts at 0.571, increases to 0.722 at trial 5 on dev, then gets F1=0.727 on test.

![Image 8: Metrics from optimization trials on all, dev, and test splits.](https://eugeneyan.com/assets/optimize-table.jpg)

Metrics from optimization trials on all, dev, and test splits.

Sometimes, the dev and test metrics diverge significantly. With the small sample size (25 per split, 50 in total), this likely stems from the dev split being unrepresentative of the full data distribution, including the test split. Thus, the LLM-evaluator may overfit on the dev set and fail to generalize to the test set.

To improve generalization across the dev and test splits, we can label more data, ensuring that it’s diverse and representative. To be diverse is to be balanced in both 0 and 1 labels, and the variety of inputs and outputs. To be representative is to be similar to real-world examples. We can also run multiple LLM-evaluators in parallel and ensemble their scores. [PoLL](https://arxiv.org/abs/2404.18796) showed that an ensemble of three smaller LLM-evaluators outperformed gpt-4.

For a visual walkthrough, here’s a demo where I look at and label 50 rows of data lol.

Behind the scenes: How AlignEval was built[](https://eugeneyan.com/writing/aligneval/#behind-the-scenes-how-aligneval-was-built)
--------------------------------------------------------------------------------------------------------------------------------

As a frontend development newbie (this is my first TypeScript app), I relied on the wisdom of the crowd, polling [Twitter](https://x.com/eugeneyan/status/1828447283811402006) and [LinkedIn](https://www.linkedin.com/posts/eugeneyan_if-you-were-building-a-small-web-app-today-activity-7234224078675439617-HX75/) for advice. I also [built the same app five times](https://eugeneyan.com/writing/web-frameworks/) to get a feel for several frameworks. Specifically, I tried FastHTML, Next.js, SvelteKit, and FastAPI + HTML (my go-to for prototyping).

From early prototypes, Next.js seemed to be a good fit. Intuitive, scalable, and the perfect excuse to learn TypeScript. And thanks to Cursor, my beginner questions were answered easily: What’s the difference between `const` and `let`? What is a `prop`? It also made it easier to build UX components and fix bugs 2-3x faster, keeping velocity and motivation high.

For the backend, Python + FastAPI was the obvious choice. Python’s ecosystem of data analysis and machine learning made it easier to experiment with optimization mode.

When it came to LLMs, I went with the smallest models from the biggest labs: gpt-4o-mini and claude-3-haiku (soon to be claude-3.5-haiku). They’re cheap, fast, and good enough for binary classification LLM-evaluators. It’s the perfect combo for a free app. And with each release, these small models just keep getting more and more capable.

For gpt-4o-mini, I used the [structured output](https://platform.openai.com/docs/guides/structured-outputs) functionality that’s still in beta. It allows users to define the desired output schema using Zod (JavaScript) or Pydantic (Python). Here’s an example in Javascript and its equivalent in Python:

```
import { z } from "zod";

const EvaluationResponse = z.object({
  explanation: z.string(),
  prediction: z.string().refine((val) => val === '0' || val === '1')
});
```

```
from pydantic import BaseModel

class EvaluationResponse(BaseModel):
  explanation: str
  prediction: str
```

For claude-3-haiku, I [defined the XML output](https://eugeneyan.com/writing/prompting/#structured-input-and-output) via the prompt. From what I’ve seen on the job and in AlignEval, this works 99.9% of the time. Here’s the prompt I used for AlignEval.

```
Evaluate the output based on the provided criteria. First, in the <sketchpad> provided, think through your evaluation step by step.

Then, provide a binary prediction (0 or 1) within <prediction>.
```

To decide on hosting, I conducted a [Twitter poll](https://x.com/eugeneyan/status/1828450401311764741) and consulted documentation for options like Dokku, Coolify, Vercel, etc. [Hamel’s write-up on Dokku](https://hamel.dev/blog/posts/dokku/) was particularly helpful. While I initially considered hosting the app on Hetzner with Dokku (another opportunity to learn something new), I ultimately decided to take the lazy path (read: prioritize ruthlessly) and start with hosting on Railway. It was a good decision.

Hosting on Railway has been a breeze. After setting up the project via their web UI and linking it via the CLI (`railway link`), pushing new updates is as simple as `railway up`. Each update takes one to two minutes. Railway also comes with several database options, including Postgres and Redis. While a VPS might be cheaper in the long run, at this stage, [YAGNI](https://en.wikipedia.org/wiki/You_aren%27t_gonna_need_it). Fiddling with a VPS would have been a distraction from improving the UX, implementing features, and figuring out optimization mode.

![Image 9: My simple Railway setup.](https://eugeneyan.com/assets/railway.jpg)

My simple Railway setup

> If you’d like to get started with Railway, please use my [affiliate code](https://railway.app/?referralCode=fMY11k)—it’ll help with hosting costs and keep AlignEval running!

Going from a laptop prototype to a public beta took some effort. The work included:

*   Splitting into Next.js frontend, FastAPI backend, migrating from SQLite to Postgres
*   Implementing real-time feedback for labeling, evaluation, and optimization
*   Adding features to simplify labeling (pass/fail buttons), customize models and fields (dropdowns, integration with model providers), and more
*   Improving the UI (as rough as it looks now, it was way worse before lol)
*   Squashing lots of bugs (and probably missing many more)

Here’s the to-do list I had; there were many more tasks and bugs that I neglected to track. Because I timeboxed the effort to October, a few items were not completed. But if AlignEval gains traction and proves useful, I might revisit the list.

```
## Todos
- [x] Split deployment into frontend and backend
  - https://help.railway.app/questions/how-to-expose-a-fast-api-backend-service-a1712631
  - https://help.railway.app/questions/econnrefused-when-calling-another-servic-5662d969#p-1
  - ~~[ ] Or consider something like this: https://vercel.com/templates/next.js/nextjs-fastapi-starter~~ (only works with Vercel)
- [x] Add external database (Railway Postgres)
- [x] Write interface to ensure compatibility between SQLite and Postgres
- [x] Connect label-app to Railway Postgres
- [x] Connect label-hpo to Railway Postgres
- [x] Show feedback to users while optimization is running
- [x] Update table names to use CSV file name
- [x] Add support for multiple tables
- [x] Replace tablename parameter with filename parameter
- [x] Uploading a CSV file with an existing name should return the existing table
- [x] Add llm-evaluator optimization to label-hpo
- [x] Add dropdown to select evaluation fields
- [x] Add ability to delete optimization table, with password
- [x] Add progress bar to gamify labeling, evaluation and optimization
- [x] Add buttons to click pass and fail
- [x] Add usage count (upload (files, rows), evaluate (files, rows), optimize (files, trials))
- [x] Add info button intro next to header to explain the site
- [x] Update favicon
- [x] Add support for OpenAI models
- [x] Add balanced val-test split for optimization
- [x] Add columns to optimization metrics: split (dev, test), model, evaluation_fields
- [x] Set max upload rows to env variable
- [ ] Fix bug where alert pops up: "Failed to handle optimization: Unexpected token '<', "<!DOCTYPE "... is not valid JSON"
  - Still pops up every now and then
- [x] Fix bug where evaluation alert pops up even when optimization is unlocked
- [x] Add popup to see full prompt
- [x] Add button to copy prompt
- [x] Add completion bar to optimization sticky
- [x] Make site look retro and like a game
- [x] Prompt users to rename sample data before downloading
- [x] Update delete optimization to reset optimization, and set password to Twitter handle
- [x] Add "don't show me this again" checkbox
- [ ] Improve how we poll for data
- [ ] Add button to donate with Stripe payment
- [ ] Add button to optimize more with Stripe payment

## Todos (OE)
- [x] Separate data definitions to definitions.ts
- [x] Separate fetch data queries to data.ts
- [x] Separate data mutations to actions.ts
- [x] Separate components into component.tsx under ui which are imported in page.tsx
```

• • •

Building AlignEval has been a ton of fun, and writing about the journey was a great way to reflect. It’s easily my favorite project of the year, because I got to build an app and learn a lot along the way. (That said, there’s still November and December to try to beat this.)

If you’re tired of spending days or weeks on evals and aligning LLM-evaluators, try [AlignEval](http://aligneval.com/). It’s designed to streamline your workflow and focus on what matters most:

*   Looking at the data and adding labels
*   Defining meaningful criteria
*   Evaluating the LLM-evaluator
*   Semi-automatically optimizing it

Here’s the [code](https://github.com/eugeneyan/align-app) in case you want to deploy your own instance. It’s my first TypeScript project, so feedback welcome! How could I have organized it better? What best practices should I have followed? And beyond the code, what have you found useful when building LLM-evaluators? Comment below or [DM me](https://x.com/eugeneyan).

Thanks to the incredible folks who made discussing this topic so much fun, and provided helpful feedback at early demos: Shreya Shankar, Hamel Husain, Kyle Corbitt, David Corbitt, Saumya Gandhi, Swyx, Eugene Cheah, and Dennis Taylor. And thanks to Hamel Husain for reading early drafts of this piece.

Further reading[](https://eugeneyan.com/writing/aligneval/#further-reading)
---------------------------------------------------------------------------

*   [Your AI Product Needs Evals](https://hamel.dev/blog/posts/evals/)
*   [Task-Specific LLM Evals that Do & Don’t Work](https://eugeneyan.com/writing/evals/)
*   [Who Validates the Validators](https://arxiv.org/abs/2404.12272)
*   [Evaluating the Effectiveness of LLM-Evaluators](https://eugeneyan.com/writing/llm-evaluators/)
*   [Creating a LLM-as-a-Judge That Drives Business Results](https://hamel.dev/llm-judge)

If you found this useful, please cite this write-up as:

> Yan, Ziyou. (Oct 2024). AlignEval: Building an App to Make Evals Easy, Fun, and Automated. eugeneyan.com. https://eugeneyan.com/writing/aligneval/.

or

```
@article{yan2024aligneval,
  title   = {AlignEval: Building an App to Make Evals Easy, Fun, and Automated},
  author  = {Yan, Ziyou},
  journal = {eugeneyan.com},
  year    = {2024},
  month   = {Oct},
  url     = {https://eugeneyan.com/writing/aligneval/}
}
```

Share on:
