Title: DSPy下篇：兼论o1、Inference-time Compute和Reasoning - 铁蕾的个人博客

URL Source: http://zhangtielei.com/posts/blog-dspy-internals-3.html

Markdown Content:
[首页](http://zhangtielei.com/) \> [AI技术](http://zhangtielei.com/posts/ai.html) \> 正文

* * *

> 浮言易逝，唯有文字长存。  
> (今天继续聊聊AI技术)

约两周前，我用两篇文章介绍了DSPy的原理：

*   《[浅谈DSPy和自动化提示词工程（上）](https://mp.weixin.qq.com/s/gloYnaj5Q0ogOv9huyziqg)》
*   《[浅谈DSPy和自动化提示词工程（中）](https://mp.weixin.qq.com/s/VR_M_Gog5OPvtNKkAV6oZg)》

今天是第三篇，算是来完结一下这个话题。虽然DSPy在实用性上还存在非常多挑战，但是它的设计思想非常超前，也非常有意思。因此，现在我们结合AI领域的一些重要概念，做个思考总结。

### 技术方面的讨论

#### Training-time / Inference-time / Pre-inference time

在OpenAI的o1发布之后，业界开始关注**Inference-time Compute**。o1在inference的阶段，通过生成大量的reasoning tokens，来获得对于复杂问题的更强的推理能力（reasoning）。

Inference-time Compute这种说法，是相对于Training-time Compute来说的。并不是说o1不需要训练的算力，而是说，相对于以前的LLM来说，o1在inference阶段投入了更多的计算。这体现在，当用户输入一个问题之后，o1要花费更长的时间进行「思考」，其实也就是在生成最终答案之间，先生成了很多reasoning tokens。

显然，o1在进行Inference-time Compute时不会更新模型的weights。这跟Training-time Compute有本质的不同。

通过前面的两篇文章，大家应该已经知道了，DSPy的优化过程，一般来说是不会更新模型weights的。不过DSPy有个例外，它有专门用来做fine-tune的优化器 (Optimizer) ，确实会更新模型的weights。这和DSPy的工程设计思路有关，我们下面再讨论这个，现在暂时先忽略这种特殊情况。可以说，一般情况下DSPy的优化器是不会更新模型weights的。

那么，DSPy的优化器不更新模型weights，那它优化什么呢？其实是优化prompt。具体细分的话，这里面又主要包含两部分：一个是优化instruction，一个是优化few-shot（也被称为exemplar selection\[1\]）。

那DSPy的优化过程，算是Inference-time Compute吗？也算也不算。它确实不会更新模型weights，从这个角度来说，它确实是inference time的。但这个优化过程是发生在用户输入问题之前，而且是基于一个数据集批量做优化。从这个角度来说，它又跟模型训练过程很像。因此，DSPy官方有一个不一样的归类，称为**Pre-inference time Compute**\[2\]。这个命名表示，DSPy的优化过程通常发生在模型训练阶段之后，但却在真正的inference阶段之前。

稍微总结一下，从LLM整个生命周期来看，按照算力的投入阶段，细分成了三类：

*   Training-time Compute。包含预训练和各种fine-tuning。
*   Pre-inference time Compute。
*   Inference-time Compute。

我们在上一篇讨论时提到的自动化提示词工程 (APE) \[1\]，显然也是属于Pre-inference time Compute。

最后，很重要的一点是，以上这三类投入算力的方法并不是互斥的，它们相互之间可以结合。

#### DSPy与APE的区别

先说APE，它的运行需要5个元素：

*   一个标注好的数据集。
*   一个能自动执行的metric。
*   一个初始的提示词。作为优化起点。
*   一个meta-prompt。为了生成新提示词而使用的提示词。
*   一个优化算法。它以前面4个元素为输入，不断迭代优化，生成越来越好的提示词。一个典型的APE优化算法是大家比较熟悉的OPRO\[3\]。

DSPy包含了APE工程的大部分元素，但它不仅仅是APE，它是个很重的AI编程框架。DSPy的设计重心在于，它所关注的是一个由多个可自动优化的Module所组成的系统。当然，DSPy在具体优化每个Module的时候，可以使用任何现成的APE优化算法，比如可以调用OPRO。但DSPy的重心在于对系统进行整体优化。从这个角度来看，DSPy与TextGrad\[4\]的思路比较像。

在[上一篇文章](https://mp.weixin.qq.com/s/VR_M_Gog5OPvtNKkAV6oZg)中，我们已经看到，DSPy通过执行Bootstrap策略，自动化地生成中间结果数据，这就是它着眼于整体系统优化的一个体现。

#### Modular / Multi-Stage / CoT

在DSPy的论文中\[5\]，我们可以看到，它所关注的是类似**multi-stage pipelines**或**agents**这样的系统。这些系统试图将复杂的任务拆解成小的、易解决的任务，再分别交由LLM来完成。这些系统天然就是模块化的 (Modular)。

**Modular**是从空间维度来讲的，系统是由多个Module组成的。**Multi-stage**则是从时间维度来讲的，一个复杂任务可以先完成第一步，然后再完成下一步，依此类推。

既然DSPy关注的是对整个系统进行自动优化，但系统是复杂的，你就需要知道在一个系统的组成部分中，哪些是可优化的，哪些是不可优化的。因此，DSPy为了解决这个问题，它借鉴了pytorch中的`nn.Module`的概念抽象。据此，你可以很容易地将系统中那些可优化的Module识别出来。当然，这也包含那些Module的子Module，一层一层都识别出来。

一个包含多个Module的系统，它的执行过程大概率也是Multi-stage的。但Multi-stage的执行过程，却未必涉及到多个Module。比如，仅针对一个LLM，就可以做多步的reflection。

抽象来看，不同执行步骤之间，可能有依赖关系，也可能没有依赖关系。在复杂的情况下，它们会组成一个DAG (Directed Acyclic Graph)。

现在大家都很关注的o1，在给出答案之前，会给出一段很长的CoT思考过程。从**逻辑层面**来看，CoT的思考过程也可以说是Multi-stage的，因为这个过程包含多个步骤，而且思考步骤之间存在很强的依赖关系（因果关系）。但从**物理层面**来看，o1的CoT是在**一个**inference过程中生成出来的。

虽然在更细的粒度上，o1的reasoning tokens也是一个token一个token生成的，可以分为很多步，但在DSPy所关注的系统粒度上，这个CoT思考的过程不会被认为是Multi-stage的。按照业界的猜测和分析，现在大家已经知道，o1是一个model，而不是一个system。如果我们在微观的层面去看，model和system的界限有时候其实有点模糊。特别是对于一个auto-regressive model来说，在inference阶段其实有相当多的「system」层面的微观操作在执行。而且，估计o1在inference time生成大量reasoning tokens的过程中，还有一个经RL训练过的policy同时也在运行。但总体来说，按照惯常的说法，o1是一个model而不是一个system，是更合理的说法。

所以说，在DSPy的语境下，假设以DSPy的方式来集成o1，即使它的CoT思考过程再长，o1也是作为DSPy的一个Module而存在的（不会成为多个Module）。

#### 关于RL和Reasoning

RL是一种trial-and-error的方法，它通过不断试错来搜索未知空间的更多解。不管是DSPy还是其它APE方法，与这个过程有一点点相似之处。APE通过尝试更多的prompt来执行trial-and-error的过程；而DSPy在更大的尺度上去自动化地摸索更多执行路径。经典的EE难题 (Exploration–Exploitation) 在这里也会出现，是需要更好的APE或DSPy的优化器去解决的。

o1是把RL用到reasoning上的典型案例。在思考的宽度上，它需要探索更多的思考路径；在思考的深度上，它需要尝试更多的思考步骤。在思考的宽度和深度的提升上，RL都起到了关键作用。

DSPy对于多Module系统的优化，更多地体现在「探索宽度」上。比如，DSPy的MIPRO优化器\[6\]，通过生成few-shot候选集和instruction候选集来拓宽整个pipeline的执行路径。MIPRO优化器在这里所使用的policy，包含一种被称为_program-and-data-aware_的技术\[6\]。如我们在[上一篇文章](https://mp.weixin.qq.com/s/VR_M_Gog5OPvtNKkAV6oZg)中看到的，这种policy在生成instruction的时候会考虑对于程序本身和数据集的描述。

### 开发模式的启示

DSPy是AI时代一种非常新颖的设计方法，对于我们的工程开发模式来说，也有很大的借鉴意义。

#### 数据驱动的AI programming

在传统的软件工程开发中，工程师理解业务逻辑，然后据此编写代码。在LLM时代，用这种开发模式去维护系统和升级进化非常有挑战。LLM的执行并不是一个严格可控的过程，它输出结果的好坏取决于prompt的质量。如果LLM升级了，或者系统的pipeline改动了，或者系统所要应对的问题空间发生变化了，都可能面临重新调优整个系统的所有prompt的问题。

DSPy强调了一种新的AI编程范式，把重心放在数据上。用数据集加上算力，自动化地达成效果。在这种范式下，数据集的积累会成为核心资产，同时，metric也非常重要。在以前的机器学习场景中，几乎只有模型算法的开发是围绕着数据集和metric这两个元素进行的，而系统工程的开发仍然主要是对精确的逻辑进行编码。但在LLM时代，**Pre-inference time Compute**更像是一个全新的领域，使得**基于数据集和metric进行系统层面的优化**变得必要与可行。

#### 「活」的系统与统一的进化视角

在引入LLM之后，现代的AI系统中，每个Module都具备了一定的灵活可变的特性。这跟传统的软件系统不同。在传统的软件系统中，每个模块都是严丝合缝地精确执行，输入和输出都是被严格地提前定义出来的。但基于LLM的Module就不同了，它的行为不能够被完全预测。

这让整体系统看起来是一个「活」的系统，而不是一个「死」的系统。既然是「活」的系统，它就有一定的可调整的空间（具体体现为很多prompt可以被优化）。同样，除了prompt之外，让系统具备一定可调整空间的因素，还包含模型的weights。在这个视角下，DSPy把模型的fine-tuning也包含在了它对于优化器的设计当中（如`dspy.BootstrapFinetune`\[2\]）。

这是一种横跨Training-time Compute和Pre-inference time Compute的技术视角。对prompt的优化和对weights的优化，即使它们底层的实现差异很大，但在这种统一的视角之下，它们都被看做成了引导系统进化的一种途径。

#### 通过计算进行domian之间的迁移

在一些非常专业的垂直领域，类似这样一种情况还挺常见：往往最专业的经验都是在专家的脑子里。他能把这些经验表达出来一部分，但却很难通过某种方式一下子概括完整。那么，如果想让模型学会这些经验，或者依据这些经验开发出agents，都是面临非常多挑战的。

这时，假设我们在某些熟知的领域，已经建立起了某种有效的pipeline，比如某种agentic RAG的pipeline。现在，我们要把这个pipeline应用到另外一个垂直领域，只需要新领域的专家给出少量的例子作为数据集（几十到几百个例子），然后使用类似DSPy的Pre-inference time Compute方法去重新优化，就有可能将沉淀在这一pipeline中的成功要素从旧的领域迁移到新的领域。

另外，DSPy的Bootstrap策略，通过自动化地生成中间结果数据，减少了领域专家的数据标注量。针对复杂的Multi-stage任务，领域专家只需要标注端到端的数据集，而不需要为每个Module的中间执行过程进行人工标注。DSPy的Bootstrap策略，可以看做是一种生成合成数据的方式。

### DSPy存在的问题

在这一小节，我们对DSPy在实用中可能存在的一些问题进行讨论：

*   DSPy的Signature机制造成的体系间的不相容。DSPy对于LLM的调用，采用了一种全新的Signature机制。除非你的项目从第一天就开始使用DSPy，否则现有项目中的prompt基本上没法跟DSPy的Signature机制兼容。假设你的项目中已经有了一版prompt，效果也还行，这时候你如果想让DSPy帮你进一步提升prompt，是不可行的。
*   极致优化prompt的空间受限。还是因为DSPy的Signature机制，它将prompt隐藏到了背后。这导致prompt的形式被Signature的设计所限制，相对模板化。如果你想极致优化某个prompt，DSPy可能不是正确的工具。
*   meta-prompt的发挥余地太小。
*   DSPy预置的Metric还很不成熟。你大概率需要根据自己的应用场景自定义Metric。Metric如果定义不明确，或者实现不准确，结果真的很糟糕。
*   优化器的实现过于复杂，超参/变量太多，有点难以控制。

### 小结

借着对DSPy的技术分析，我们又结合AI领域的一些重要概念，做了相当广泛的讨论。面对各种新技术概念和新技术思想的出现、发展以及可能的炒作，我相信，只有具备工程师思维的人才能够更准确地把握和判断。过去有人说，软件吞噬世界。现在，如果我们问：AI会取代传统软件吗？显然，比较准确的说法是，**AI会产生越来越多的软件**。随着AI的普及，人们处理的问题规模、问题的深度、处理的效率，都会越来越提升。**这不是简单的取代，而是全新的创造**。

（正文完）

##### 参考文献：

*   \[1\] Heiko Hotz. 2024. [Automated Prompt Engineering: The Definitive Hands-On Guide](https://towardsdatascience.com/automated-prompt-engineering-the-definitive-hands-on-guide-1476c8cd3c50).
*   \[2\] [DSPy官网](https://dspy.ai/).
*   \[3\] Chengrun Yang, et al. 2023. [Large Language Models as Optimizers](https://arxiv.org/abs/2309.03409).
*   \[4\] [TextGrad: Automatic ‘‘Differentiation’’ via Text](https://github.com/zou-group/textgrad).
*   \[5\] Omar Khattab, et al. 2023. [DSPy: Compiling Declarative Language Model Calls into Self-Improving Pipelines](https://arxiv.org/abs/2310.03714).
*   \[6\] Krista Opsahl-Ong, Michael J Ryan, Josh Purtell, David Broman, Christopher Potts, Matei Zaharia, Omar Khattab. 2024. [Optimizing Instructions and Demonstrations for Multi-Stage Language Model Programs](https://arxiv.org/abs/2406.11695).

**其它精选文章**：

*   [技术变迁中的变与不变：如何更快地生成token？](https://mp.weixin.qq.com/s/BPnX0zOJr8PLAxlvKQBsxw)
*   [用统计学的观点看世界：从找不到东西说起](https://mp.weixin.qq.com/s/W6hSnQPiZD1tKAou3YgDQQ)
*   [从GraphRAG看信息的重新组织](https://mp.weixin.qq.com/s/lCjSlmuseG_3nQ9PiWfXnQ)
*   [企业AI智能体、数字化与行业分工](https://mp.weixin.qq.com/s/Uglj-w1nfe-ZmPGMGeZVfA)
*   [三个字节的历险](https://mp.weixin.qq.com/s/6Gyzfo4vF5mh59Xzvgm4UA)
*   [分布式领域最重要的一篇论文，到底讲了什么？](https://mp.weixin.qq.com/s/FZnJLPeTh-bV0amLO5CnoQ)
*   [内卷、汉明问题与认知迭代](https://mp.weixin.qq.com/s/rgKkJ5wI5G5BZ6lIJZj7WA)
*   [漫谈分布式系统、拜占庭将军问题与区块链](https://mp.weixin.qq.com/s/tngWdvoev8SQiyKt1gy5vw)
*   [深度学习、信息论与统计学](https://mp.weixin.qq.com/s/q8CfQzK5xZknD9gBMGkvNA)

**原创文章，转载请注明出处，并包含下面的二维码！否则拒绝转载！**  
**本文链接：**[http://zhangtielei.com/posts/blog-dspy-internals-3.html](http://zhangtielei.com/posts/blog-dspy-internals-3.html)  
**欢迎关注我的个人微博：微博上搜索我的名字「张铁蕾」。**

![Image 3: 我的微信公众号: tielei-blog (张铁蕾)](http://zhangtielei.com/assets/my_weixin_sign_sf_840.jpg)

* * *
