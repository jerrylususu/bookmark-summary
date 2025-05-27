Title: Introducing Marin: An Open Lab for Building Foundation Models

URL Source: http://marin.community/blog/2025/05/19/announcement/

Published Time: 2025-05-19T00:00:00+00:00

Markdown Content:
![Image 1: Logo](https://marin.community/assets/images/logo.webp)
_Developing models together, openly_

19 May 2025
Introducing Marin: An Open Lab for Building Foundation Models
-------------------------------------------------------------

David Hall

Ahmed Ahmed, Christopher Chou, Abhinav Garg, Rohith Kuditipudi, Will Held, Nikil Ravi, Herumb Shandilya, Jason Wang

Jason Bolton, Siddharth Karamcheti, Suhas Kotha, Tony Lee, Nelson Liu, Joel Niklaus, Ashwin Ramaswami, Kamyar Salahi, Kaiyue Wen, Chi Heem Wong, Sherry Yang, Ivan Zhou

Percy Liang

* * *

Open-source _software_ is a success story: It powers the world’s digital infrastructure. It allows anyone in the world to contribute based on merit. It leads to greater innovation, collaboration, and security.

Open-source AI is not there yet. We have open-weight models (e.g., Llama, DeepSeek, Gemma), sometimes mistakenly called open-source models, but the code and data (recipe) used to produce the model are not released. There has been a movement over the last few years to build [open-source](https://opensource.org/ai/open-source-ai-definition) models. [Eleuther AI](https://www.eleuther.ai/), [Allen Institute for AI (AI2)](https://allenai.org/), [Hugging Face](https://huggingface.co/), [BigScience](https://bigscience.huggingface.co/), [BigCode](https://www.bigcode-project.org/), [LAION](https://laion.ai/), [DataComp-LM](https://www.datacomp.ai/dclm/), [MAP-Neo](https://map-neo.github.io/), [LLM360](https://www.llm360.ai/), [Together AI](https://www.together.ai/), [NVIDIA](https://www.nvidia.com/), and others have taken the path (so far) less traveled. These teams not only have released model weights, but also the code and data recipe used to produce the model. These assets have enabled others (including Marin!) to build their own models and push forward innovation.

![Image 2: Marin](https://marin.community/assets/images/posts/announcement-open.png)

We would like to go one step further. In open-source software, it is easy for anyone to download the code, extend it, and contribute back to the community. This is because over the last two decades, the community has developed mature tools: versioned code hosting (e.g., GitHub), continuous integration, and governance strategies. Such infrastructure doesn’t exist yet for the development of foundation models. You can’t train locally, and you can’t just log into someone else’s GPU or TPU cluster.

A new form of openness
----------------------

Marin is an **open lab**, in which the research and development of models is completely transparent from day 1 (that’s today). We leverage GitHub to organize the open lab’s efforts, piggybacking off of tools and processes developed for open-source software. Here’s how it works:

1.   Each **experiment** (whether it be on the wishlist, currently running, or completed) is tracked by a **GitHub issue**—see an [example](https://github.com/marin-community/marin/issues/1183). These GitHub issues serve as form of mini-[preregistration](https://en.wikipedia.org/wiki/Preregistration_(science)), which declares the hypotheses and goals upfront.

2.   To run an experiment, someone (anyone) submits a pull request (PR) specifying what concretely needs to be run. Not only does the [Marin codebase](https://github.com/marin-community/marin/) contain our training and data processing code, **experiments are also declared in code** (see [an example](https://github.com/marin-community/marin/blob/main/experiments/exp1183_olmoe.py)).

3.   The PR can be reviewed by anyone (in the spirit of [OpenReview](https://openreview.net/) for papers). The community can have a lively debate about experimental design, bikeshed details, whatever. Because the actual code is available, one can drill down into as much detail as one wants.

4.   Once the PR is approved, the experiment is launched. Anyone can watch the execution live ([example](https://marin.community/data-browser/experiment/?path=gs%3A%2F%2Fmarin-us-west4%2Fexperiments%2Fexp1183_olmoe-f9d291.json)), which has links to [WandB](https://wandb.ai/marin-community/marin/reports/MoE-vs-Dense-1b--VmlldzoxMjgzMzI4OQ). Any analysis and insights are collected back into the GitHub issue.

This is a new way to do research that’s more scientific and more inclusive. We normalize making mistakes (which we all make—see [all the things we messed up on our 8B run](https://marin.readthedocs.io/en/latest/reports/marin-8b-retro/)). Any negative results are in the open. There is no cherry picking. There is no ambiguity about what was run. Everything is reproducible, declared in code, and open to the community to see.

![Image 3: Marin](https://marin.community/assets/images/posts/announcement-flow.png)

Experiments and models
----------------------

Having built the infrastructure for the open lab, what do we use it for? We are driven by the fundamental research question: **how do we build the best model with a fixed resource budget**? Here, “best” captures some notion of accuracy, and “resources” captures both compute and data (human labor).

There is both a tension and synergy between scientific understanding and engineering the best model. This is reflected in a bifurcation in our experiments:

1.   We performed **controlled** small-scale ablation experiments to understand one small piece of the puzzle at a time. For example, we investigated different [architectures](https://github.com/marin-community/marin/issues/1183), [optimizers](https://github.com/marin-community/marin/issues/1290), [quality classifiers](https://github.com/marin-community/marin/issues/1290), [regularization methods](https://github.com/marin-community/marin/issues/935), and so on. We built new datasets using improved [HTML to text](https://marin.readthedocs.io/en/latest/reports/markdownified-datasets/) and started doing [crawling](https://github.com/marin-community/marin/issues/968). We fit [scaling laws](https://github.com/marin-community/marin/issues/780). These experiments have the ethos of the [Stanford Language Modeling from Scratch (CS336)](https://cs336.stanford.edu/) class, in which we study every component of the language modeling pipeline.

2.   We also performed a few **YOLO** runs which eventually led to our best models. We documented our journey in the [Marin 8B retrospective](https://marin.readthedocs.io/en/latest/reports/marin-8b-retro/), which is reminiscent of the [OPT logbook](https://github.com/facebookresearch/metaseq/blob/main/projects/OPT/chronicles/OPT175B_Logbook.pdf) (though our TPUs were nice and thankfully we didn’t have to deal with all those hardware issues). In these YOLO runs, we encountered bugs along the way and discovered new revelations about datasets, learning rates, regularization…but we just adjusted our training and kept on going. Once in a while, we would peel off to do a controlled experiment ([example](https://github.com/marin-community/marin/issues/950)), which then informed us how to continue.

In the end, we ended up training [Marin 8B Base (deeper-starling)](https://huggingface.co/marin-community/marin-8b-base/tree/deeper-starling), with a Llama architecture (dense Transformer) for 12.7T tokens (see the [full reproducible execution](https://marin.community/data-browser/experiment/?path=gs%3A//marin-us-central2/experiments/exp600_tootsie-4699e2.json)!). On **14 out of 19 standard base model evals (MMLU, HellaSwag, GPQA, etc.), Marin 8B Base outperforms Llama 3.1 8B Base** (see [full results table](https://marin.readthedocs.io/en/latest/reports/marin-8b-retro/#base-model-results)), but one must always be careful about interpreting evals due to [train-test overlap](https://github.com/marin-community/marin/issues/1321) and the non-trivial impact of prompting differences.

We also performed supervised fine-tuning (SFT) of Marin 8B Base for ~5B tokens to produce [Marin 8B Instruct (deeper-starling-05-15)](https://huggingface.co/marin-community/marin-8b-instruct/tree/deeper-starling-05-15). This model outperforms OLMo 2 on standard instruct model evals, but still fall short of [Llama 3.1 Tulu](https://arxiv.org/abs/2411.15124)—see [full results table](https://marin.readthedocs.io/en/latest/reports/marin-8b-retro/#sft-evals). Considering that, unlike Llama 3.1 Tulu, we have not yet done any reinforcement learning from feedback (RLHF), not even DPO, we are optimistic that we can still improve the instruct model substantially.

But don’t take our word for it—try out these models yourself! You can download both from [Hugging Face](https://huggingface.co/marin-community) or try out Marin 8B Instruct at [Together AI](https://api.together.ai/playground/v2/chat/marin-community/marin-8b-instruct). Please provide feedback either by submitting a [GitHub issue](https://github.com/marin-community/marin/issues/new/choose) or posting in our [Discord](https://discord.gg/J9CTk7pqcM). Or in the spirit of true open-source, you can try fixing it yourself at our [Datashop](https://marin.readthedocs.io/en/latest/tutorials/datashop/).

Speedrun for the AI researcher 🏃
---------------------------------

![Image 4: Marin](https://marin.community/assets/images/posts/announcement-speedrun.png)

As an open-source project, anyone can contribute in any way to Marin. However, to add structure to these contributions, we lean on **leaderboards**, which have a long history of driving progress in AI. Most AI leaderboards are about benchmarking a final model, system, or product. However, we want to incentivize algorithmic innovation.

We draw inspiration from the [nanogpt speedrun](https://github.com/KellerJordan/modded-nanogpt?tab=readme-ov-file#world-record-history), which solicits submissions from the community to “train a neural network to ≤3.28 validation loss on FineWeb using 8x NVIDIA H100s” in the shortest time. Progress has been incredible: in the span of a year, the training time has dropped from 5.8 hours to just under 3 minutes.

However, it is well known that some ideas work well only at small scales, so it’s not clear which of these ideas matter at larger scale. The [Marin Speedrun](https://marin.community/speedrun/) accepts submissions at multiple compute budgets. This allows researchers to participate at whatever compute budget is available to them. We also encourage using a scaling suite of different compute budgets, so that can fit scaling laws and assess a method based on how well it scales (what is the slope?) rather than how good it is at any one scale.

You are encouraged to try out new architectures, optimizers, and even data filtering strategies. For the initial submission, participants will use their own compute and report the metrics (in a pull request along with the code). Over time, we will offer promising submissions free compute to scale up.

Check out this [example submission](https://github.com/marin-community/marin/blob/main/experiments/speedrun/llama_75m_adamax/llama_75m_adamax.py) and get started with this [tutorial](https://marin.readthedocs.io/en/latest/tutorials/submitting-speedrun/)!

Datashop for the domain expert 🛠️
----------------------------------

Language models can in principle do anything, but in practice they have holes. An effective way to fill these holes is to curate relevant data. We have set up [Datashop](https://marin.readthedocs.io/en/latest/tutorials/datashop/) to do this. Suppose you would like the Marin 8B model to improve its capabilities along some dimension (e.g., chemistry). Using Datashop, you can upload a dataset or craft a prompt that uses an existing LM to curate a relevant dataset. As before, the proposed experiment is codified in Python, submitted as a pull request, reviewed, and then executed live. Here is an [example](https://github.com/marin-community/marin/issues/963) of how Datashop can be used. Datashop is a great way for domain experts, who might not necessarily have the AI infrastructure setup to contribute to making the model better. More specifically:

1.   You specify a prompt describing the type of data you want to obtain (e.g., [FineMath prompt](https://github.com/marin-community/marin/blob/91b86a710664bed75c61e109c740852c4dcf60ad/experiments/exp963_cascade_finemath.py#L13)).
2.   We then prompt an LM (e.g., Llama 3 70B) to classify a subset of documents.
3.   We use the (document, adherence to your criterion) examples produced by the LM to train a linear or BERT classifier.
4.   We then run this classifier on all the documents and choose the ones that are classified positive beyond some threshold ([selected examples](https://marin.community/data-browser/view/?paths=%5B%22gs%3A%2F%2Fmarin-us-east1%2Fdocuments%2Fquality_filtering%2Fdatashop%2Fdatashop-dclm-pretraining-subset-finemath-cascade-phase-2-f42d44%2Flocal-shard_0_of_10%2Fshard_00000000_processed.jsonl.zst%22%5D)) (negatives are just drawn from the background dataset).
5.   Once you have the dataset, you can fine-tune a model on it! Or you can run a controlled [annealing experiment](https://marin.readthedocs.io/en/latest/tutorials/annealing-experiment/) to evaluate it for inclusion during midtraining.

See the full [execution](https://marin.community/data-browser/experiment?path=gs%3A%2F%2Fmarin-us-east1%2Fexperiments%2Fexp963_cascade_finemath-fa55e6.json) of the FineMath replication experiment.

![Image 5: Datashop](https://marin.community/assets/images/posts/announcement-datashop-diagram.png)

The future of AI should be open-source in the strongest sense: researchers and developers alike should be able to not just use AI, but to contribute directly back to it. We have built Marin, an open lab, that provides the infrastructure to help make this happen. Of course training strong foundation models requires significant resources, and building communities is hard. Nonetheless, we must try. We have benefited greatly from an open Internet, open-source software, Wikipedia, and many assets in the public domain. At one point, these were also crazy ideas that were more likely to fail than to succeed.

This is the beginning of the Marin journey. There is so much to do: we’d like to [try efficient linear attention architectures](https://github.com/marin-community/marin/issues/1313), [add long context support](https://github.com/marin-community/marin/issues/1314), improve performance on other domains like [legal reasoning](https://github.com/marin-community/marin/issues/1267), support more languages, support multimodality, enhance reasoning with RL-based post-training, and all the ideas you have that we haven’t thought of. Come join us ([Discord](https://discord.gg/J9CTk7pqcM), [GitHub](https://github.com/marin-community/marin/)) and let us deepen our scientific understanding and build the best models together!

Acknowledgements
----------------

So many people and organizations have supported Marin, to whom we are greatly indebted:

*   First, we would like to thank Zak Stone and the [Google TPU Research Cloud (TRC)](https://sites.research.google/trc/) team. Nearly all of the compute used for Marin comes from TRC. This project might not have even gotten started without their support.
*   The Google JAX team, especially Roy Frostig, Sharad Vikram, Matthew Johnson, Yash Katariya, and Skye Wanderman-Milne, and Allen Wang from the TPU team helped us make good use of our TPU allocation.
*   The Anyscale team, especially Robert Nishihara and Richard Liaw, helped us with Ray, which Marin builds on.
*   We would like to thank Matthew Ding, Kevin Klyman, Russell Power, and Cathy Zhou for their contributions to the project.
*   This work originated from the [Stanford Center for Research on Foundation Models (CRFM)](https://crfm.stanford.edu/) and the [Human-Centered AI Institute (HAI)](https://hai.stanford.edu/). We are grateful for their support and fostering the belief that academia has an important role to play in the era of industrialized AI.
*   We would also like to thank the many people, including members of the [Stanford AI Lab](https://ai.stanford.edu/) and [Stanford NLP group](https://nlp.stanford.edu/), who have given advice and contributed valuable discussions.
*   Thanks to the Together AI team for [hosting](https://api.together.ai/playground/v2/chat/marin-community/marin-8b-instruct) the Marin 8B Instruct model.
*   We would also like to thank [Weights And Biases](https://wandb.ai/site/) for logging our many, many experiments.
*   Finally, we would like to give a big shoutout to the open-source community, without which Marin would simply be impossible. Organizations such as [EleutherAI](https://www.eleuther.ai/), [Allen Institute for AI (AI2)](https://allenai.org/), [Hugging Face](https://huggingface.co/), [BigScience](https://bigscience.huggingface.co/), [BigCode](https://www.bigcode-project.org/), [LAION](https://laion.ai/), [DataComp-LM](https://www.datacomp.ai/dclm/), [MAP-Neo](https://map-neo.github.io/), [LLM360](https://www.llm360.ai/), [Together AI](https://www.together.ai/), [NVIDIA](https://www.nvidia.com/), and many others, have been hugely inspirational in paving the way towards truly open-source foundation models. They have released tools and datasets that have directly benefited Marin, and we can only hope to give back to the community through our efforts.
