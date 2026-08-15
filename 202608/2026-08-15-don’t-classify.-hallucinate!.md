# Don’t classify. Hallucinate!
- URL: https://softwaredoug.com/blog/2026/08/10/hypothetical-classifications
- Added At: 2026-08-15 15:08:34
- Tags: #read #tips

## TL;DR
文章提出用大模型分类时，不让模型严格输出合法类目，而是放任其自由编造“假分类”，再用向量相似度映射回真实分类。这样省去每次发送巨大合法列表的token开销，突破schema限制，可用更小更便宜的模型，适合类别繁多的分类场景。

## Summary
这篇文章提出了一种用大语言模型做分类时更省事、更省钱的方法：**不要让模型严格输出系统里已有的合法分类，而是让它自由编造一些听起来合理的“假分类”，然后再用向量相似度把这些假分类“翻译”回真实分类。**

以电商搜索查询分类为例。比如 Wayfair 的 WANDS 数据集里，查询“wood coffee table”要归类到几百个真实类目之一，如：

- Furniture / Living Room Furniture / Coffee Tables & End Tables / Coffee Tables  
- Furniture / Bedroom Furniture / Dressers & Chests  
- Décor & Pillows / Decorative Pillows & Blankets / Throw Pillows  

传统做法是“结构化输出”：把所有合法类目列成一个巨大的 `Literal` 类型，让模型只能从这些选项里选。比如用 Pydantic 定义几百个合法值，然后调用 GPT 等模型去做分类。这个方法确实能用，但有几个问题：

1. **贵**：每次调用都要把几百个类目作为约束发给模型，token 消耗大。
2. **有上限**：一些服务对结构化输出的 schema 大小有限制。
3. **重**：需要维护一个巨大的合法值列表，并且每次请求都要带着它。

作者提出的替代方案是：**完全不发送合法分类列表，而是让一个小模型、甚至比较“笨”的模型去凭空编造分类**。例如给它一个提示：“请为查询 `brown coffee table` 发明一些全新的、你从未见过的家具/家居/五金分类。”模型可能会输出：

```
Furniture / Living Room / Tables / Coffee
```

这个分类在真实系统里根本不存在，看起来没用。但作者说：**这恰恰非常有用**。

接下来的关键步骤是：

1. 预先用真实分类集合（比如几百个 Wayfair 的真实类目）计算 embedding，得到一个向量库。
2. 让模型对查询编造出假分类，再计算这个假分类的 embedding。
3. 用假分类的 embedding 和真实分类的 embedding 做点积相似度计算，找出最接近的真实分类。

这样，上面编造的 `Furniture / Living Room / Tables / Coffee` 就会被映射到：

```
Furniture / Living Room Furniture / Coffee Tables & End Tables / Coffee Tables
```

这个方法的好处很明显：

- **可以用更小、更便宜的模型**来做“幻觉生成”，因为生成假分类不需要理解完整的真实 taxonomy。
- **不需要每次把几百个合法值发给模型**，省 token、突破 schema 大小限制。
- 分类任务被拆成了两步：先让模型自由生成候选，再用向量检索对齐到真实词汇表。本质上是用 embedding 相似度来“纠正”模型的幻觉，使其变成可控的分类。

简而言之，文章的核心思想是：**把“严格约束输出”换成“放任模型幻觉，然后用向量对齐到真实标签”**。这样既保留了 LLM 对语义的理解能力，又避免了每次携带巨大合法值集合的成本和限制，特别适合分类类别非常多、又希望用便宜小模型大规模做分类的场景。
