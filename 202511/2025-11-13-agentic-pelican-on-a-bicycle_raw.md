Title: Agentic Pelican on a Bicycle

URL Source: https://www.robert-glaser.de/agentic-pelican-on-a-bicycle/

Published Time: 2025-11-11T19:28:25.000Z

Markdown Content:
Simon Willison has been running his own informal model benchmark for years: [“Generate an SVG of a pelican riding a bicycle.”](https://simonwillison.net/tags/pelican-riding-a-bicycle/?ref=robert-glaser.de) It’s delightfully absurd—and surprisingly revealing. Even the model labs channel this benchmark in their marketing campaigns announcing new models.

Simon’s traditional approach is zero-shot: throw the prompt at the model, get SVG back. Maybe—if you’re lucky—you get something resembling a pelican on a bicycle.

Nowadays everyone is talking about agents. Models running in a loop using tools. Sometimes they have vision capabilities, too. They can look at what they just created, cringe a little, and try again. The agentic loop—generate, assess, improve—seems like a natural fit for such a task.

So I ran a different experiment: what if we let models iterate on their pelicans? What if they could see their own output and self-correct?

The Prompt
----------

```
Generate an SVG of a pelican riding a bicycle

- Convert the .svg to .jpg using chrome devtools, then look at the .jpg using your vision capabilities.
- Improve the .svg based on what you see in the .jpg and what's still to improve.
- Keep iterating in this loop until you're satisfied with the generated svg.
- Keep the .jpg for every iteration along the way.
```

Besides the file system and access to a command line, the models had access to [Chrome DevTools MCP server](https://github.com/ChromeDevTools/chrome-devtools-mcp?ref=robert-glaser.de) (for SVG-to-JPG conversion) and their own multimodal vision capabilities. They could see what they’d drawn, identify problems, and iterate. The loop continued until they declared satisfaction.

I used the Chrome DevTools MCP server to give every model the same rasterizer. Without this, models would fall back to whatever SVG-to-image conversion they prefer or have available locally—ImageMagick, Inkscape, browser screenshots, whatever. Standardizing the rendering removes one variable from the equation.

The prompt itself is deliberately minimal. I could have steered the iterative loop with more specific guidance—“focus on anatomical accuracy,” “prioritize mechanical realism,” “ensure visual balance.” But that would defeat the point. Simon’s original benchmark is beautifully unconstrained, and I wanted to preserve that spirit. The question isn’t “can models follow detailed improvement instructions?” It’s “when left to their own judgment, what do they choose to fix?”

The Models
----------

I tested six models across the frontier, all multimodal:

*   Claude Opus 4.1, Claude Sonnet 4.5, Claude Haiku 4.5, all with thinking
*   GPT-5 (on medium reasoning effort)
*   GPT-5-Codex (on medium reasoning effort)
*   Gemini 2.5 Pro

Each model decided independently when to stop iterating. Some made four passes. Others kept going for six. None knew when to quit.

The Results
-----------

Let’s see what happened. For each model, I’m showing the first attempt (left) and the final result (right) after self-correction.

### Claude Opus 4.1 (4 iterations)

![Image 1](https://www.robert-glaser.de/content/images/2025/11/pelican_bicycle_v1-1.svg)

![Image 2](https://www.robert-glaser.de/content/images/2025/11/pelican_bicycle_v4_final-1.svg)

Opus started with a serviceable pelican-bicycle combo and then did something interesting: it added realism. The final version has an actual bicycle chain connecting the pedals to the rear wheel. The wheels gained more spokes. The pelican’s proportions improved, and it got arms holding the handlebars. This wasn’t just “add more details”—it was “make this mechanically coherent.” Interestingly, we got the catch of the day on a special plate on the handlebars. Oh, and look at the street and the birds in the backdrop!

### Claude Sonnet 4.5 (4 iterations)

![Image 3](https://www.robert-glaser.de/content/images/2025/11/pelican-bicycle-v1-2.svg)

![Image 4](https://www.robert-glaser.de/content/images/2025/11/pelican-bicycle-v4-1.svg)

Sonnet took a more restrained approach. The changes between iterations were subtler—refinements to curves, adding shadows, and movement indicators. Adjustments to positioning. Improving the spokes. Improving the arms and handlebars. The final result is cleaner, but the core composition remained remarkably stable.

### Claude Haiku 4.5 (6 iterations)

![Image 5](https://www.robert-glaser.de/content/images/2025/11/iteration-1-1.jpg)

![Image 6](https://www.robert-glaser.de/content/images/2025/11/iteration-6-final-1.jpg)

Haiku took the longest journey—six full iterations. It kept tweaking, kept adjusting. The additional iterations didn’t necessarily produce a dramatically better result, but Haiku seemed determined to get every detail right before calling it done. So the pelican definitely received proper legs and feet.

### GPT-5 Medium (5 iterations)

![Image 7](https://www.robert-glaser.de/content/images/2025/11/pelican-01.jpg)

![Image 8](https://www.robert-glaser.de/content/images/2025/11/pelican-05.jpg)

GPT-5 Medium started with a recognizable pelican-bicycle scene and refined it over five iterations. The improvements were incremental—better proportions, clearer shapes—but the fundamental composition held steady throughout.

### GPT-5-Codex Medium (5 iterations)

![Image 9](https://www.robert-glaser.de/content/images/2025/11/pelican-bike-01.svg)

![Image 10](https://www.robert-glaser.de/content/images/2025/11/pelican-bike-05.svg)

Here’s where things get interesting. Its initial attempt was… let’s call it “abstract.” A sort of layer cake of pelican parts. And then, instead of simplifying, it doubled down. The final result added even more layers. More complexity. More parts. Whether this counts as “improvement” is a philosophical question I’m not qualified to answer.

### Gemini 2.5 Pro (6 iterations)

![Image 11](https://www.robert-glaser.de/content/images/2025/11/iteration-1.svg)

![Image 12](https://www.robert-glaser.de/content/images/2025/11/iteration-6-final-2.jpg)

Gemini was the outlier. Most models preserved their initial composition through iterations, making refinements but keeping the core structure mostly intact. Gemini actually changed the fundamental arrangement—the pelican’s pose, the bicycle’s orientation, the spatial relationship between them. Six iterations showed a bigger leap.

What Did We Learn?
------------------

The results are… mixed.

**The optimistic take**: Models like Opus 4.1 made genuinely thoughtful improvements. Adding a bicycle chain isn’t just decoration—it shows understanding of mechanical relationships. The wheel spokes, the adjusted proportions—these are signs of vision-driven refinement working as intended.

**The skeptical take**: Most models didn’t fundamentally change their approach. They tweaked. They adjusted. They added details. But the basic composition—pelican shape, bicycle shape, spatial relationship—was determined in iteration one and largely frozen thereafter.

**The confusing take**: Some models (looking at you, GPT-5-Codex) seemed to mistake “more complex” for “better.” The self-feedback loop amplified their initial artistic direction rather than correcting it. If your first draft is a layer cake of pelican parts, and your self-correction produces an even more elaborate layer cake... did the loop help? Of course, GPT-5-Codex is a fine-tune of GPT-5, optimized for engineering tasks. Could be that its strengths are not in broad visual capabilities.

The agentic approach definitely produces different results than zero-shot generation. Whether it produces _better_ results seems to depend heavily on the model’s ability to self-critique. Vision capabilities alone aren’t enough—you need something more: aesthetic judgment, mechanical reasoning, or at least the wisdom to know when to stop adding details.

Simon’s zero-shot benchmark reveals how well models handle unusual creative tasks on the first try. The agentic variant reveals something else: how well models can evaluate and improve their own creative output. Turns out, that’s a different skill entirely. But—somehow related?

* * *

_All test code and results available in the_[_GitHub_](https://github.com/youngbrioche/agentic-pelican-on-a-bicycle?ref=robert-glaser.de)_repository._