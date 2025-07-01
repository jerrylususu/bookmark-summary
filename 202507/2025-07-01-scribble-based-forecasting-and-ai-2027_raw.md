Title: Scribble-based forecasting and AI 2027

URL Source: https://dynomight.net/scribbles/

Published Time: 2025-06-30T00:00:00+00:00

Markdown Content:
[AI 2027](https://ai-2027.com/) forecasts that AGI could plausibly arrive as early as 2027. I recently spent some time looking at both the [timelines forecast](https://ai-2027.com/research/timelines-forecast) and some critiques [[1](https://thezvi.wordpress.com/2025/04/08/ai-2027-responses/), [2](https://secondthoughts.ai/p/ai-2027), [3](https://titotal.substack.com/p/a-deep-critique-of-ai-2027s-bad-timeline)].

Initially, I was interested in technical issues. What’s the best super-exponential curve? How much probability should it have? But I found myself drawn to a more basic question. Namely, how much value is the math really contributing?

This provides an excuse for a general rant. Say you want to forecast something. It could be when your hair will go gray or if Taiwan will be self-governing in 2050. Whatever. Here’s one way to do it:

1.   Think hard.
2.   Make up some numbers.

Don’t laugh—that’s the classic method. Alternatively, you could use math:

1.   Think hard.
2.   Make up a formal model / math / simulation.
3.   Make up some numbers.
4.   Plug those numbers into the formal model.

People are often skeptical of intuition-based forecasts because, “Those are just some numbers you made up.” Math-based forecasts are hard to argue with. But that’s not because they lack made-up numbers. It’s because the meaning of those numbers is mediated by a bunch of math.

So which is better, intuition or math? In what situations?

Here, I’ll look at that question and how it applies to AI 2027. Then I’ll build a new AI forecast using my personal favorite method of “plot the data and scribble a bunch of curves on top of it”. Then I’ll show you a little tool to make your own artisanal scribble-based AI forecast.

Two kinds of forecasts
----------------------

To get a sense of the big picture, let’s look at two different forecasting problems.

First, here’s a forecast (based on the [IPCC 2023 report](https://www.ipcc.ch/report/ar6/syr/downloads/report/IPCC_AR6_SYR_FullVolume.pdf)) for Earth’s temperature. There are two curves, corresponding to different assumptions about future greenhouse gas emissions.

![Image 1](https://dynomight.net/img/scribbles/ipcc_big.svg)

Those curves look unassuming. But there are a lot of moving parts behind them. These kinds of forecasts model atmospheric pressure, humidity, clouds, sea currents, sea surface temperature, soil moisture, vegetation, snow and ice cover, surface albedo, population growth, economic growth, energy, and land use. They also model the interactions between all those things.

That’s hard. But we basically understand how all of it works, and we’ve spent a ludicrous amount of effort carefully building the models. If you want to forecast global surface temperature change, this is how I’d suggest you do it. Your brain can’t compete, because it can’t grind through all those interactions like a computer can.

OK, but here’s something else I’d really like to forecast: Where is this blue line going to go?

![Image 2](https://dynomight.net/img/scribbles/nukes.svg)

You _could_ forecast this using a “mechanistic model” like with climate above. To do that, you’d want to model the probability Iran develops a nuclear weapon and what Saudi Arabia / Turkey / Egypt might do in response. And you’d want to do the same thing for Poland / South Korea / Japan and their neighbors. You’d also want to model future changes in demographics, technology, politics, technology, economics, military conflicts, etc.

In _principle_, that would be the best method. As with climate, there are too many plausible futures for your tiny brain to work through. But building that model would be very hard, because it basically requires you to model the whole world. And if there’s an error anywhere, it could have serious consequences.

In practice, I’d put more trust in intuition. A talented human (or [AI](https://dynomight.net/predictions/)?) forecaster would probably take an [outside view](https://en.wikipedia.org/wiki/Reference_class_forecasting) like, “Over the last 80 years, the number of countries has gone up by 9, so in 2105, it might be around 18.” Then, they’d consider adjusting for things like, “Will other countries might learn from the example of North Korea?” or “Will chemical enrichment methods become practical?”

Intuition can’t churn through possible futures the way a simulation can. But if you don’t _have_ a reliable simulator, maybe that’s OK.

Broadly speaking, math/simulation-based forecasts shine when the phenomena you’re interested in has two properties.

1.   It evolves according to some well-understood rule-set.
2.   The _behavior_ of the ruleset is relatively complex.

The first is important because if you don’t have a good model for the ruleset (or at least your _uncertainty_ about the ruleset), how will you build a reliable simulator? The second is important because if the behavior is simple, why do you even need a simulator?

The ideal thing to forecast with math is something like [Conway’s game of life](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life). Simple known rules, huge emergent complexity. The worst thing to forecast with math is something like the probability that Jesus Christ returns next year. You could make up some math for that, but what would be the point?

The AI 2027 forecast
--------------------

This post is (ostensibly) about AI 2027. So how does their forecast work? They actually have several forecasts, but here I’ll focus on the [Time horizon extension](https://ai-2027.com/research/timelines-forecast#method-1-time-horizon-extension) model.

That forecast builds on a [recent METR report](https://arxiv.org/pdf/2503.14499). They took a set of AIs released over the past 6 years, and had them attempt a set of tasks of varying difficulty. They had humans perform those same tasks. Each AI was rated according to the human task length that it could successfully finish 50% of the time.

![Image 3](https://dynomight.net/img/scribbles/figure1.svg)

The AI 2027 team figured that if an AI could successfully complete long-enough tasks of this type, then the AI would be capable of itself carrying AI research, and AGI would not be far away. Quantitatively, they suggest that the necessary task length is probably somewhere between 1 month and 10 years. They also suggest you’d need a success rate of 80% (rather than 50% in the above figure).

So, very roughly speaking, the forecast is based on predicting how long it will take these dots to get up to one of the horizontal lines:

![Image 4](https://dynomight.net/img/scribbles/curves.svg)

 (It's a bit more complicated than that, but that's the core idea.) 
Technical notes:

*   The AI 2027 team raises the success rate to 80%, rather than 50% in the original figure from the METR report. That’s why the dots in the above figure are a bit lower.
*   I made the above graph using the [data](https://github.com/titotal1993/AI2027critique/blob/main/AI2027polished.ipynb) that [titotal](https://titotal.substack.com/p/a-deep-critique-of-ai-2027s-bad-timeline) extracted from the AI 2027 figures.
*   The AI 2027 forecast creates a _distribution_ over the threshold that needs to be reached rather than considering fixed thresholds.
*   The AI 2027 forecast also adds an adjustment based on the theory that companies have internal models that are better than they release externally. They also add another adjustment on the theory that public-facing models are using limited compute to save money. In effect, these add a bit of vertical lift to all the points.

I think this framing is great. Instead of an abstract discussion about the arrival of AGI, suddenly we’re talking about how quickly a particular set of real measurements will increase. You can argue if “80% success at a 1-year task horizon” really means AGI is imminent. But that’s kind of the point—no matter what you think about broader issues, surely we’d all like to know how fast those dots are going to go up.

So how fast will they go up? You could imagine building a mechanistic model or simulation. To do that, you’d probably want to model things like:

*   How quickly is the data + compute + money being put into AI increasing?
*   How quickly is compute getting cheaper?
*   How quickly is algorithmic progress happening?
*   How does data + compute + algorithmic progress translate into improvements on the METR metrics?
*   How long will those trends hold? How do all those things interact with each other? How do they interact with AI progress itself.

In principle, that makes a lot of sense. Some people predict a future where compute keeps getting cheaper [pretty slowly](https://ourworldindata.org/grapher/gpu-price-performance) and we run out of data and new algorithmic ideas and loss functions stop translating to real-world performance and investment drops off and everything slows down. Other people predict a future where GPUs accelerate and we keep finding better algorithms and AI grows the economy so quickly that AI investment increases forever and we spiral into a singularity. In between those extremes are many other scenarios. A formal model could churn through all of them much better than a human brain.

But the AI 2027 forecast is not like that. It doesn’t have separate variables for compute / money / algorithmic progress. It (basically) just models the best METR score per year.

That’s not _bad_, exactly. But I must admit that I don’t quite see the point of a formal mathematical model in this case. It’s (basically) just forecasting how quickly a single variable goes up on a graph. The model doesn’t reflect any firm knowledge about subtle behavior other than that the curve will probably go up.

In a way, I think this makes the AI 2027 forecast seem _weaker_ than it actually is. Math is hard. There are lots of technicalities to argue with. But their broader point doesn’t need math. Say you accept their premise that 80% success on tasks that take humans 1 year means that AGI is imminent. Then you should believe AGI is around the corner _unless those dots slow down_. An argument that their math is flawed doesn’t imply that the dots are going to stop going up.

Scribble-based forecasting
--------------------------

So, what’s going to happen with those dots? The ultimate outside view is probably to not think at all and just draw a straight line. When I do that, I get something like this:

![Image 5](https://dynomight.net/img/scribbles/curves_with_lines.svg)

I guess that’s not terrible. But personally, I feel like it’s plausible that the recent acceleration continues. I also think it’s plausible that in a couple of years we stop spending ever-larger sums on training AI models and things slow down. And for a _forecast_, I want probabilities.

So I took the above dots and I scribbled 50 different curves on top, corresponding to what I felt were 50 plausible futures:

![Image 6](https://dynomight.net/img/scribbles/50lines.png)

Then I treated those lines as a probability distribution over possible futures. For each of the 1 month, 1 year, and 10 year task-horizon thresholds, I calculated what percentage of the lines had crossed over that threshold by a given year.

![Image 7](https://dynomight.net/img/scribbles/cdf.png)

Or, here’s a summary as a table:

| Threshold | 10th Percentile | 50th Percentile | 90th Percentile | % Reached by 2050 |
| --- | --- | --- | --- | --- |
| 1 month | 2028.7 | 2032.3 | 2039.3 | 94% |
| 1 year | 2029.5 | 2034.8 | 2041.4 | 88% |
| 10 year | 2029.2 | 2037.7 | 2045.0 | 54% |

My scribbles may or may not be good. But I think the _exercise_ of drawing the scribbles is great, because it forces you to be completely explicit about what you’re predicting.

I recommend it. In fact, I recommend it so strongly that I’ve created a little tool that you can use to [do your own scribbling](https://dynomight.net/img/scribbles/tool.html). It will automatically generate a plot and table like you see above. You can import or export your scribbles in CSV format. (Mine are [here](https://dynomight.net/img/scribbles/50lines.csv) if you want to use them as a starting point.)

Here’s a little video:

While scribbling, you may reflect on the fact that the tool you’re using is 100% AI-generated.
