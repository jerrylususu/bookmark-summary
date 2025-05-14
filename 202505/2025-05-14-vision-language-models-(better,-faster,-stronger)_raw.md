Title: Vision Language Models (Better, faster, stronger)

URL Source: https://huggingface.co/blog/vlms-2025

Markdown Content:
[Back to Articles](https://huggingface.co/blog)

[![Image 1: Merve Noyan's avatar](https://cdn-avatars.huggingface.co/v1/production/uploads/1648113222875-6141a88b3a0ec78603c9e784.png)](https://huggingface.co/merve)

[![Image 2: Sergio Paniego's avatar](https://cdn-avatars.huggingface.co/v1/production/uploads/61929226ded356549e20c5da/ONUjP2S5fUWd07BiFXm0i.jpeg)](https://huggingface.co/sergiopaniego)

[![Image 3: Aritra Roy Gosthipaty's avatar](https://cdn-avatars.huggingface.co/v1/production/uploads/608aabf24955d2bfc3cd99c6/T762Ut0Y-w0sZB2ynvfbJ.jpeg)](https://huggingface.co/ariG23498)

[![Image 4: Pedro Cuenca's avatar](https://cdn-avatars.huggingface.co/v1/production/uploads/1617264212503-603d25b75f9d390ab190b777.jpeg)](https://huggingface.co/pcuenq)

[![Image 5: Andres Marafioti's avatar](https://cdn-avatars.huggingface.co/v1/production/uploads/65d66b494bbd0d92b641cdbb/6-7dm7B-JxcoS1QlCPdMN.jpeg)](https://huggingface.co/andito)

[](https://huggingface.co/blog/vlms-2025#motivation)Motivation
--------------------------------------------------------------

Vision Language Models (VLMs) are the talk of the town. In [a previous blog post](https://huggingface.co/blog/vlms) (from _April 2024_), we talked a lot about VLMs. A major chunk was about [LLaVA](https://huggingface.co/papers/2304.08485), the first **successful** and **easily reproducible** open-source vision language model, along with tips on how to discover, evaluate, and fine-tune open models.

Since then, so much has changed. Models have become [smaller yet more powerful](https://huggingface.co/blog/smolvlm). We've seen the rise of new architectures and capabilities (reasoning, agency, long video understanding, etc.). In parallel, entirely new paradigms, such as multimodal Retrieval Augmented Generation (RAG) and multimodal agents have taken shape.

In this blog post, we’ll take a look back and unpack everything that happened with vision language models the past year. You’ll discover key changes, emerging trends, and notable developments.

> We highly recommend reading the first blog post if you want a good primer on how vision language models work.

[](https://huggingface.co/blog/vlms-2025#table-of-contents)Table of Contents
----------------------------------------------------------------------------

*   [New Model Trends](https://huggingface.co/blog/vlms-2025#new-model-trends)
    *   [Any-to-any models](https://huggingface.co/blog/vlms-2025#any-to-any-models)
    *   [Reasoning models](https://huggingface.co/blog/vlms-2025#reasoning-models)
    *   [Smol Yet Capable Models](https://huggingface.co/blog/vlms-2025#smol-yet-capable-models)
    *   [Mixture-of-Experts as Decoders](https://huggingface.co/blog/vlms-2025#mixture-of-experts-as-decoders)
    *   [Vision Language Action Models](https://huggingface.co/blog/vlms-2025#vision-language-action-models)
*   [Specialized Capabilities](https://huggingface.co/blog/vlms-2025#specialized-capabilities)
    *   [Object Detection, Segmentation, Counting with Vision Language Models](https://huggingface.co/blog/vlms-2025#object-detection-segmentation-counting-with-vision-language-models)
    *   [Multimodal Safety Models](https://huggingface.co/blog/vlms-2025#multimodal-safety-models)
    *   [Multimodal RAG: retrievers, rerankers](https://huggingface.co/blog/vlms-2025#multimodal-rag-retrievers-rerankers)
*   [Multimodal Agents](https://huggingface.co/blog/vlms-2025#multimodal-agents)
*   [Video Language Models](https://huggingface.co/blog/vlms-2025#video-language-models)
*   [New Alignment Techniques for Vision Language Models](https://huggingface.co/blog/vlms-2025#new-alignment-techniques-for-vision-language-models)
*   [New Benchmarks](https://huggingface.co/blog/vlms-2025#new-benchmarks)
    *   [MMT-Bench](https://huggingface.co/blog/vlms-2025#mmt-bench)
    *   [MMMU-Pro](https://huggingface.co/blog/vlms-2025#mmmu-pro)
*   [Extra: Our Model Picks](https://huggingface.co/blog/vlms-2025#extra-our-model-picks)
*   [Useful Resources](https://huggingface.co/blog/vlms-2025#useful-resources)

[](https://huggingface.co/blog/vlms-2025#new-model-trends)New model trends
--------------------------------------------------------------------------

In this section, we will look at the new types of VLMs. While some are absolutely new, others are improved versions of previous research.

[](https://huggingface.co/blog/vlms-2025#any-to-any-models)Any-to-any models
----------------------------------------------------------------------------

Any-to-any models, as the name suggests, are models that can take in any modality and output any modality (image, text, audio). They do it by aligning the modalities, where an input from one modality can be translated to another (e.g. the word “dog” would be associated with an image of a dog, or with the utterance of the word).

These models have multiple encoders (one for each modality) and then fuse the embeddings together to create a shared representation space. The decoders (multiple or single) use the shared latent space as input and decode into the modality of choice. Earliest attempt to build any-to-any models is [Chameleon by Meta](https://huggingface.co/collections/facebook/chameleon-668da9663f80d483b4c61f58), which can take in image and text and output image and text. Meta didn't release image generation capability, in this model, so the Alpha-VLLM has released [Lumina-mGPT](https://huggingface.co/collections/Alpha-VLLM/lumina-mgpt-family-66ae48a59a973eeae4513848), which has built image generation on top of Chameleon.

The latest and most capable any-to-any model, [Qwen 2.5 Omni](https://huggingface.co/collections/Qwen/qwen25-omni-67de1e5f0f9464dc6314b36e) (figure below) is a good example to understand the architecture of an any-to-any model.

[![Image 6: Qwen-Omni](https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/vlm2/qwen-omni.png)](https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/vlm2/qwen-omni.png)

Qwen2.5-Omni employs a novel "Thinker-Talker" architecture, where the "Thinker" handles text generation, and the "Talker" produces natural speech responses in a streaming manner. [MiniCPM-o 2.6](https://huggingface.co/openbmb/MiniCPM-o-2_6), an 8B parameter multimodal model is capable of understanding and generating content across vision, speech, and language modalities. [Janus-Pro-7B](https://huggingface.co/deepseek-ai/Janus-Pro-7B), introduced by DeepSeek AI, is a unified multimodal model that excels in both understanding and generating content across modalities. It features a decoupled visual encoding architecture, separating the processes for understanding and generation.

We suspect an uptick in the number of such models in the coming years. It is a well-known intuition that multimodal learning is the only way we can learn deep representations better. We have curated some any-to-any models and demos in [this collection](https://huggingface.co/collections/merve/any-to-any-models-6822042ee8eb7fb5e38f9b62).

### [](https://huggingface.co/blog/vlms-2025#reasoning-models)Reasoning Models

Reasoning models are models that can solve complex problems. We saw them first with large language models, and now vision language models. Until 2025, there was only one open-source multimodal reasoning model, [QVQ-72B-preview](https://huggingface.co/Qwen/QVQ-72B-Preview) by Qwen. It was an experimental model that was developed by the Alibaba Qwen team and came with many disclaimers.

This year there’s another player, [Kimi-VL-A3B-Thinking](https://huggingface.co/moonshotai/Kimi-VL-A3B-Thinking) by the Moonshot AI team. It consists of MoonViT (SigLIP-so-400M) as the image encoder and a Mixture-of-Experts (MoE) decoder with 16B total parameters and only 2.8B active parameters. The model is a long chain-of-thought fine-tuned and further aligned (reinforcement learning) version of the Kimi-VL base vision language model. You can try the model [here](https://huggingface.co/spaces/moonshotai/Kimi-VL-A3B-Thinking).

> The authors also released an instruction fine-tuned version called [Kimi-VL-A3B-Instruct](https://huggingface.co/moonshotai/Kimi-VL-A3B-Instruct).

[![Image 7: kimi-vl](https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/vlm2/kimi-vl.png)](https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/vlm2/kimi-vl.png) The model can take in long videos, PDFs, screenshots and more. It has agentic capabilities as well.

### [](https://huggingface.co/blog/vlms-2025#smol-yet-capable-models)Smol yet Capable Models

The community used to scale intelligence through the number of parameters, and then high-quality synthetic data. After a certain point, the benchmarks saturated and scaling models had diminishing returns. The community went to shrink larger models through various methods, like distillation. This makes sense because it reduces compute costs, simplifies deployment, and unlocks use cases like local execution, enhancing data privacy.

When we say small vision language models we often refer to models with less than 2B parameters that can be run on consumer GPUs. SmolVLM is a good example model family for smaller vision language models. Instead of shrinking larger models, went all the way and tried to fit models into tiny number of parameters like 256M, 500M and 2.2B. SmolVLM2, for instance, attempted to solve video understanding in these sizes and found 500M to be a good trade-off. At Hugging Face, we have built an iPhone application, HuggingSnap, to demonstrate that these model sizes can achieve video understanding on consumer devices.

Another striking model is [gemma3-4b-it](https://huggingface.co/google/gemma-3-4b-it) by Google DeepMind. It’s particularly exciting as it’s one of the smallest multimodal models to have 128k token context window, and supports 140+ languages. The model comes with the Gemma 3 family of models, with its largest model ranking first on Chatbot Arena at the time. The largest model was then distilled to a 1B variant.

Lastly, although not the smallest, [Qwen2.5-VL-3B-Instruct](https://huggingface.co/Qwen/Qwen2.5-VL-3B-Instruct) is worth noting. The model can do various tasks ranging from localization (object detection and pointing), to document understanding, to agentic tasks; with context length up to 32k tokens.

You can use small models through MLX and Llama.cpp integrations. For MLX, assuming you have it installed, you can get started with SmolVLM-500M-Instruct with this one liner:

```
python3 -m mlx_vlm.generate --model HuggingfaceTB/SmolVLM-500M-Instruct --max-tokens 400 --temp 0.0 --image https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/vlm_example.jpg --prompt "What is in this image?" 
```

You can get started with using [gemma-3-4b-it](https://huggingface.co/collections/google/gemma-3-release-67c6c6f89c4f76621268bb6d) model in GGUF format with llama.cpp through CLI with this one-liner:

```
llama-mtmd-cli -hf ggml-org/gemma-3-4b-it-GGUF  
```

You can also serve the same model as follows.

```
llama-server -hf ggml-org/gemma-3-4b-it-GGUF  
```

We would like to give a shoutout to [moondream2](https://huggingface.co/vikhyatk/moondream2) and [Florence-2](https://huggingface.co/collections/microsoft/florence-6669f44df0d87d9c3bfb76de) as they're earliest attempts for smallest vision language models. In this blog, we are covering primarily newer models (mostly models that came out after April 2024).

### [](https://huggingface.co/blog/vlms-2025#mixture-of-experts-as-decoders)Mixture-of-Experts as Decoders

Mixture of Expert (MoEs) models offer an _alternative_ to **dense** architectures by dynamically selecting and activating only the most relevant sub-models, termed "experts", to process a given input data segment. This selective activation (done by a router) mechanism has demonstrated the potential to substantially enhance model performance and operational efficiency while utilizing fewer computational resources.

MoEs are faster at inference than their similar parameter-dense counterparts because of the selective activation of a smaller slice of the network. They also converge quickly during training. Every good thing comes with a cost, as MoEs need more memory cost due to the entire model being on the GPU, even if a smaller chunk is used.

In the widely adopted Transformer architecture, MoE layers are most commonly integrated by replacing the standard Feed-Forward Network (FFN) layers within each Transformer block. Dense networks use the entire model to run an inference, while similarly sized MoE networks selectively activate some experts. This helps in better compute utilization and faster inference.

Vision language models that have mixture-of-experts decoders seem to have enhanced performance. For instance, Kimi-VL as of now is the most advanced open reasoning model that has a mixture-of-experts decoder. Mixture-of-Experts show promising results with [MoE-LLaVA](https://huggingface.co/papers/2401.15947)'s focus on efficiency and hallucination reduction and [DeepSeek-VL2](https://huggingface.co/deepseek-ai/deepseek-vl2)'s broad multimodal capabilities too. The latest version of Llama ([Llama 4](https://huggingface.co/collections/meta-llama/llama-4-67f0c30d9fe03840bc9d0164)) is an MoE with vision capabilities. MoE as a decoder is a promising research area, and we suspect an increase in models like these.

> To get a nice understanding of MoEs we recommend reading [this fantastic article](https://huggingface.co/blog/moe).

### [](https://huggingface.co/blog/vlms-2025#vision-language-action-models)Vision-Language-Action Models

VLMs are even making their mark in the field of robotics! There, they are known as Vision-language-action models (VLA). But don't be fooled, those are mainly VLMs with a little moustache and hat. VLAs take images and text instructions, and return text indicating actions for the robot to take directly. VLAs extend vision language models by adding action and state tokens to interact with and control physical environments. These extra tokens represent the system’s internal state (how it perceives the environment), actions (what it does based on commands), and time-related information (like the order of steps in a task). These tokens are appended to the vision language input to generate actions or policy.

VLAs are usually fine-tuned on top of a base VLM. Some people extend this definition further and define VLAs as any model interacting visually with a real or digital world. In this definition, VLAs can do UI navigation or be used in agentic workflows. But many people believe those applications fall in the VLM domain.

Great examples of VLAs are [π0](https://huggingface.co/lerobot/pi0) and π0-FAST, the first robotics foundation models by Physical Intelligence, ported to Hugging Face’s LeRobot library. These models are trained across 7 robotics platforms and 68 unique tasks. They show strong zero-shot and fine-tuned performance on complex, real-world activities such as laundry folding, table bussing, grocery bagging, box assembly, and object retrieval.

[GR00T N1](https://huggingface.co/nvidia/GR00T-N1-2B) is NVIDIA’s open VLA foundation model for generalist humanoid robots. It understands images and language, and turns them into actions, like moving its arms or following instructions, thanks to a system that combines smart reasoning with real-time movement control. GR00T N1 also builds on the LeRobot dataset format, the open standard created to simplify sharing and training on robot demonstrations.

[![Image 8: pi0](https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/vlm2/pi0.png)](https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/vlm2/pi0.png)

Taken from [the paper](https://www.physicalintelligence.company/download/pi0.pdf)

Now that we’ve looked at the latest VLM model innovations, let’s explore how more established capabilities have evolved.

[](https://huggingface.co/blog/vlms-2025#specialized-capabilities)Specialized Capabilities
------------------------------------------------------------------------------------------

### [](https://huggingface.co/blog/vlms-2025#object-detection-segmentation-counting-with-vision-language-models)Object Detection, Segmentation, Counting with Vision Language Models

As we’ve seen in earlier sections, VLMs enable _generalization_ over traditional computer vision tasks. Models can now take in images and a variety of prompts, such as open-ended text, and output structured text with localization tokens (for detection, segmentation and more).

Last year, [PaliGemma](https://huggingface.co/blog/paligemma) was the first model to attempt solving these tasks. The model takes in an image and text, where text is a description of an object of interest, along with a task prefix. The text prompt looks like “segment striped cat” or “detect bird on the roof”.

For detection, the model outputs the bounding box coordinates as _tokens_. For segmentation, on the other hand, the model outputs detection tokens and segmentation tokens. These segmentation tokens aren’t all the segmented pixel coordinates, but codebook indices that are decoded by a variational autoencoder trained to decode these tokens into valid segmentation masks (as shown in the figure below).

[![Image 9: PaliGemma3](https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/vlm2/pg2-seg.png)](https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/vlm2/pg2-seg.png)

Many models have been introduced to do localization tasks after PaliGemma. Late last year, an upgraded version of PaliGemma, PaliGemma 2, appeared with the same capabilities and better performance. Another model that came later was Molmo by Allen AI, which can point to instances with dots and count object instances.

[![Image 10: molmo](https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/vlm2/molmo-pointing.png)](https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/vlm2/molmo-pointing.png)

Qwen2.5-VL can also detect, point to, and count objects, and this includes UI elements as objects too!

[![Image 11: Qwen2.5VL](https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/vlm2/qwen3-gui.png)](https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/vlm2/qwen3-gui.png)

### [](https://huggingface.co/blog/vlms-2025#multimodal-safety-models)Multimodal Safety Models

Vision language models in production require **filtering** inputs and outputs to prevent jailbreaks and harmful outputs for compliance. Harmful content varies from inputs with violence to sexually explicit content. That’s where multimodal safety models come in: they are used before and after vision language models to filter their inputs and outputs. They are just like LLM safety models but with additional image input.

In early 2025, Google introduced the first open multimodal safety model, [ShieldGemma 2](https://huggingface.co/google/shieldgemma-2-4b-it). It is built on ShieldGemma, the text-only safety model. This model takes in images and content policies and returns whether an image is safe for a given policy. _Policy_ refers to a criterion in which the image is inappropriate. ShieldGemma 2 can also be used to filter outputs of image generation models.

[Llama Guard 4](https://huggingface.co/spaces/merve/llama-guard-4) by Meta, is a dense multimodal and multilingual safety model. It is densely pruned from Llama 4 Scout (a multimodal mixture-of-experts) with safety fine tuning.

[![Image 12: Llama Guard 4](https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/vlm2/llama-guard.png)](https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/vlm2/llama-guard.png)

The model can be used for text-only and multimodal inference. The model can also take in vision language model outputs, complete conversations, and filter them before sending them to the user.

### [](https://huggingface.co/blog/vlms-2025#multimodal-rag-retrievers-rerankers)Multimodal RAG: retrievers, rerankers

Now let’s look at how Retrieval Augmented Generation has evolved in the multimodal space. RAG for complex documents, usually formatted in PDF, is processed in three steps:

1.  parsing the document completely into text
2.  passing the plain text and the query to a retriever and a reranker to get the most relevant document
3.  passing the relevant context and query to an LLM

A traditional PDF parser consists of multiple elements to preserve the structure and visual elements in the document, such as _layout_, _tables_, _images_, _charts,_ all rendered into a markdown. But this setup can be hard to maintain.  
[![Image 13: Traditional Parsing](https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/vlm2/rag-1.png)](https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/vlm2/rag-1.png)

With the rise of vision language models, this issue was addressed: there are now multimodal retrievers and rerankers.

[![Image 14: Multimodal RAG](https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/vlm2/rag-2.png)](https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/vlm2/rag-2.png)

Multimodal retrievers take a stack of PDFs and a query as input and return the most relevant page numbers along with their confidence scores. The scores represent how likely the page contains the answer to the query, or how relevant the query is to the page. This bypasses the brittle parsing step.

The most relevant pages are then fed to the vision language model along with the query, and the VLM generates the answer.

There are two main **multimodal retriever architectures**:

1.  Document Screenshot Embedding (DSE, MCDSE)
2.  ColBERT-like models (ColPali, ColQwen2, ColSmolVLM)

DSE models consist of a text encoder and an image encoder, returning a single vector per query. The returned scores are softmax over the dot products of embeddings. They return a single vector per passage.

[![Image 15: DSE](https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/vlm2/dse.png)](https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/vlm2/dse.png)

Taken from [the paper](https://arxiv.org/pdf/2406.11251)

ColBERT-like models, like ColPali, are also dual encoder models, with a twist: ColPali has a vision language model as an image encoder, and a large language model as a text encoder. These models are inherently not encoders, but the models output embeddings, which are then passed to a “MaxSim”. The outputs are multiple vectors, one for each token, unlike DSE. In MaxSim, the similarity between each text token embedding and each image patch embedding is calculated, and this approach captures nuances better. Due to this reason, ColBERT-like models are less cost-efficient, have better performance.

Below you can see the indexing latency for ColPali. Since it’s just a single model, it’s also easier to maintain.

[![Image 16: ColPali](https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/vlm2/colpali.png)](https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/vlm2/colpali.png) Taken from [the paper](https://arxiv.org/pdf/2407.01449)

On Hugging Face Hub, you can find these models under the task “[Visual Document Retrieval](https://huggingface.co/models?pipeline_tag=visual-document-retrieval&sort=trending)”.

The most popular benchmark for this task is ViDoRe, which consists of documents in **English** and **French**, with documents varying from financial reports, scientific figures to administrative documents. Each example of ViDoRe has the document as image, a query and potential answers. The documents matched with the queries help with contrastive pre-training, so the ViDoRe train set is used to train new models.

[](https://huggingface.co/blog/vlms-2025#multimodal-agents)Multimodal Agents
----------------------------------------------------------------------------

Vision language models unlock many agentic workflows from chatting with documents to computer use. Here we will cover the latter since it requires more advanced agentic capabilities. Recently, there have been many vision language models releases that understand and operate over UIs. The latest one is UI-TARS-1.5 by ByteDance, which showed great results in operating over browser, computer and phone use. It can also do gameplay with reasoning, and operate in open world games. Another impactful release of this year is MAGMA-8B, it’s a foundation model for both UI navigation and physical interaction with the real world. Moreover, Qwen2.5-VL (especially its [32B variant](https://huggingface.co/Qwen/Qwen2.5-VL-32B-Instruct) as it is further trained on agentic tasks) and [Kimi-VL reasoning model](https://huggingface.co/collections/moonshotai/kimi-vl-a3b-67f67b6ac91d3b03d382dd85) are good in GUI agentic tasks.

At the beginning of 2025, we introduced smolagents, a new lightweight agentic library that implements the ReAct framework. Shortly after, we implemented vision language support for the library. This integration took place on two use cases:

*   At the beginning of the run, provide images for once. This is useful for document AI with tool use.
*   Dynamically retrieve images. This is useful for cases such as GUI control with VLM agents, where the agent repeatedly takes screenshots.

The library provides building blocks for the users to build their own agentic workflows with image understanding. We provide different scripts and single-line CLI commands to get the users started easily.

For the first case, assume we want an agent to describe documents (which is not very agentic, but good for minimal use cases). You can initialize the CodeAgent (an agent that writes its own code!) like the following:

```
agent = CodeAgent(tools=[], model=model) # no need for tools
agent.run("Describe these documents:", images=[document_1, document_2, document_3])
```

For the latter use case where we need an agent to get screenshots, we can define a callback to be executed at the end of each `ActionStep`. For your own use case where you need to get images dynamically, modify the callback however you’d like. We will not define it here in detail for simplicity. Optionally, you can read the blog post and the script itself at the end of this blog post. For now, let’s see how we initialize the agent with callbacks and browser control steps.

```
def save_screenshot(memory_step: ActionStep, agent: CodeAgent) -> None:
    """ 
    Takes screenshots and writes to observations.
"""
  png_bytes = driver.get_screenshot_as_png()
        memory_step.observations_images = [image.copy()]  # persist images to memory_step
    url_info = f"Current url: {driver.current_url}"
    memory_step.observations = (
        url_info if memory_step.observations is None else memory_step.observations + "\n" + url_info
    )
    return

agent = CodeAgent(
    tools=[go_back, close_popups, search_item_ctrl_f], # pass navigation tools
    model=model,
    additional_authorized_imports=["helium"],
    step_callbacks=[save_screenshot], # pass callback
)
```

You can simply try the whole example by running the following CLI command. It starts an agent with access to control over the web browser, powered by a vision language model to accomplish web automation tasks (please replace with the website you’d like to navigate to).

```
webagent "go to xyz.com/men, get to sale section, click the first clothing item you see. Get the product details, and the price, return them. note that I'm shopping from France"   
```

smolagents provides different model types, such as local transformers models, open-source models served using Inference Providers, or endpoints closed-source model providers. We encourage the use of open-source models as many agentic workflows currently require reasoning, which benefits from models with a large number of parameters. Qwen 2.5 VL as of April 2025 is a good candidate for agentic workflows, as the model is further trained on agentic tasks.

[](https://huggingface.co/blog/vlms-2025#video-language-models)Video Language Models
------------------------------------------------------------------------------------

Most vision language models these days can handle videos, because videos can be represented as a sequence of frames. However, video understanding is tricky because of the temporal relationship between frames and the large amount of frames, so different techniques are used to select a representative set of video frames.  
[![Image 17: Video LMs](https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/vlm2/video.png)](https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/vlm2/video.png)

Since last year, the community has weighed on different approaches and tricks to solve this problem.

A good example is the [LongVU model](https://huggingface.co/collections/Vision-CAIR/longvu-67181d2debabfc1eb050c21d) by Meta. It downsamples video frames by passing them to DINOv2 to pick the most similar ones to remove them, and then the model further refines frames by picking the most relevant frames according to the text query, where both the text and the frames are projected to the same space and similarity is calculated. [Qwen2.5VL](https://huggingface.co/collections/Qwen/qwen25-vl-6795ffac22b334a837c0f9a5) can handle long context and is adapted to dynamic FPS rates, as the model is trained with videos with different frame rates. Through extended multimodal RoPE, it understands the absolute time positions of frames, and can handle different rates and still understand the speed of the events happening in real life. Another model is [Gemma 3](https://huggingface.co/collections/google/gemma-3-release-67c6c6f89c4f76621268bb6d), which can accept video frames interleaved with timestamps in text prompt, e.g. “Frame 00.00: ..”, and is very performant for video understanding tasks.

[![Image 18: MRoPE](https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/vlm2/mrope.png)](https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/vlm2/mrope.png)  
Taken from [the paper](https://arxiv.org/pdf/2502.13923)

[](https://huggingface.co/blog/vlms-2025#new-alignment-techniques-for-vision-language-models)New Alignment Techniques for Vision Language Models
--------------------------------------------------------------------------------------------------------------------------------

**Preference optimization** is an alternative fine-tuning approach for language models that can also be extended to vision language models. Instead of relying on fixed labels, this method focuses on comparing and ranking candidate responses based on preferences. The [trl](https://huggingface.co/docs/trl/en/index) library offers support for direct preference optimization (DPO), including for VLMs.

Below is an example of how a preference dataset for DPO of a VLM fine-tuning is structured. Each entry consists of an image + question pair and two corresponding answers: one chosen and one rejected. The VLM is fine-tuned to generate responses aligned with the preferred (chosen) answer.

[![Image 19: DPO](https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/vlm2/dpo.png)](https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/vlm2/dpo.png)

An example dataset for this procedure is [RLAIF-V](https://huggingface.co/datasets/openbmb/RLAIF-V-Dataset), which contains over 83000 annotated samples formatted according to the structure described above. Each entry includes a list of images (usually one), a prompt, a chosen answer, and a rejected answer, just as expected by the DPOTrainer.  
There is a [RLAIF-V formatted](https://huggingface.co/datasets/HuggingFaceH4/rlaif-v_formatted) dataset, which is already formatted accordingly. Below is an example of a single sample:

```
{'images': [<PIL.JpegImagePlugin.JpegImageFile image mode=L size=980x812 at 0x154505570>],
 'prompt': [ { "content": [ { "text": null, "type": "image" }, { "text": "What should this catcher be using?", "type": "text" } ], "role": "user" } ],
 'rejected': [ { "content": [ { "text": "The catcher, identified by the number...", "type": "text" } ], "role": "assistant" } ],
 'chosen': [ { "content": [ { "text": "The catcher in the image should be using a baseball glove...", "type": "text" } ], "role": "assis