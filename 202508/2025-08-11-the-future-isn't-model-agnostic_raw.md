Title: The Future Isn't Model Agnostic

URL Source: https://fly.io/blog/the-future-isn-t-model-agnostic/

Markdown Content:
Author![Image 1: Daniel Botha](https://fly.io/static/images/placeholder.webp)Name Daniel Botha ![Image 2: Fly whackamole](https://fly.io/blog/the-future-isn-t-model-agnostic/assets/Whack_A_Mole_.webp)

Image by[Annie Ruygt](https://annieruygtillustration.com/)

Your users don’t care that your AI project is model agnostic.

In my last project, I spent countless hours ensuring that the LLMs running my services could be swapped out as easily as possible. I couldn’t touch a device with an internet connection without hearing about the latest benchmark-breaking model and it felt like a clear priority to ensure I could hot swap models with minimal collateral damage.

So yeah. That was a waste of time.

The hype around new model announcements feels more manufactured with each release. In reality, improvements are becoming incremental. As major providers converge on the same baseline, the days of one company holding a decisive lead are numbered.

In a world of model parity, the differentiation moves entirely to the product layer. Winning isn’t about ensuring you’re using the best model, its about understanding your chosen model deeply enough to build experiences that feel magical. Knowing exactly how to prompt for consistency, which edge cases to avoid, and how to design workflows that play to your model’s particular strengths

Model agnosticism isn’t just inefficient, it’s misguided. Fact is, swapping out your model is not just changing an endpoint. It’s rewriting prompts, rerunning evals, users telling you things just feel… different. And if you’ve won users on the way it feels to use your product, that last one is a really big deal.

[](https://fly.io/blog/the-future-isn-t-model-agnostic/#model-lt-product)Model < Product
----------------------------------------------------------------------------------------

Recently, something happened that fully solidified this idea in my head. Claude Code is winning among people building real things with AI. We even have evangelists in the Fly.io engineering team, and those guys are weird smart. Elsewhere, whole communities have formed to share and compare claude.md’s and fight each other over which MCP servers are the coolest to use with Claude.

Enter stage right, Qwen 3 Coder. It takes Claude to the cleaners in benchmarks. But the response from the Claude Code user base? A collective meh.

This is nothing like 2024, when everyone would have dropped everything to get the hot new model running in Cursor. And it’s not because we’ve learned that benchmarks are performance theater for people who’ve never shipped a product.

It’s because products like Claude Code are irrefutable evidence that the model isn’t the product. We’ve felt it first hand when our pair programmer’s behaviour changes in subtle ways. The product is in the rituals. The trust. The predictability. It’s precisely because Claude Code’s model behavior, UI, and user expectations are so tightly coupled that its users don’t really care that a better model might exist.

I’m not trying to praise Anthropic here. The point is, engineering for model agnosticism is a trap that will eat up time that could be better spent … anywhere else.

Sure, if you’re building infra or anything else that lives close to the metal, model optionality still matters. But people trusting legwork to AI tools are building deeper relationships and expectations of their AI tools than they even care to admit. AI product success stories are written when products become invisible parts of users’ daily rituals, not showcases for engineering flexibility.

[](https://fly.io/blog/the-future-isn-t-model-agnostic/#make-one-model-your-own)Make One Model Your Own
-------------------------------------------------------------------------------------------------------

As builders, it’s time we stop hedging our bets and embrace the convergence reality. Every startup pitch deck with ‘model-agnostic’ as a feature should become a red flag for investors who understand product-market fit. Stop putting ‘works with any LLM’ in your one-liner. It screams ‘we don’t know what we’re building.’

If you’re still building model-agnostic AI tools in 2025, you’re optimizing for the wrong thing. Users don’t want flexibility; they want reliability. And in a converged model landscape, reliability comes from deep specialization, not broad compatibility.

Pick your model like you pick your therapist; for the long haul. Find the right model, tune deeply, get close enough to understand its quirks and make them work for you. Stop architecting for the mythical future where you’ll seamlessly swap models. That future doesn’t exist, and chasing it is costing you the present.

[](https://fly.io/blog/the-future-isn-t-model-agnostic/#bonus-level-all-in-on-one-model-means-all-out-on-eval)Bonus level: All-in On One Model Means All-out On Eval
--------------------------------------------------------------------------------------------------------------------------------------------------------------------

If any of this is landing for you, you’ll agree that we have to start thinking of model evaluation as architecture, not an afterthought. The good news is, rigorous model eval doesn’t have to be mind numbing anymore.

Turns out, games are really great eval tools! Now you can spin up your very own little [AI Town](https://github.com/fly-apps/ai-town_on_fly.io) on Fly.io with a single click deploy to test different models as pixel people in an evolving environment. I discuss the idea further in [Games as Model Eval: 1-Click Deploy AI Town on Fly.io](https://blog/games-as-model-eval/).

 Next post ↑ [Games as Model Eval: 1-Click Deploy AI Town on Fly.io](https://fly.io/blog/games-as-model-eval/) Previous post ↓ [Phoenix.new – The Remote AI Runtime for Phoenix](https://fly.io/blog/phoenix-new-the-remote-ai-runtime/)