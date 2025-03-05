Title: A Practical Guide to Implementing DeepSearch/DeepResearch

URL Source: https://jina.ai/news/a-practical-guide-to-implementing-deepsearch-deepresearch/

Published Time: 2025-02-25T14:36:17.000+01:00

Markdown Content:
[Jina AI Deep Search AI deep search: read, reason, search until best answer found. ![Image 1](https://jina-ai-gmbh.ghost.io/content/images/icon/favicon-30.ico) ![Image 2](https://jina-ai-gmbh.ghost.io/content/images/thumbnail/banner-2.png)](https://search.jina.ai/)

It's _only_ February, and DeepSearch has already emerged as the new search standard in 2025, with major players like [Google](https://blog.google/products/gemini/google-gemini-deep-research/) and [OpenAI](https://openai.com/index/introducing-deep-research/) leading the charge through their DeepResearch releases (and yes, [we proudly launched our open-source `node-deepresearch` on the same day](https://x.com/hxiao/status/1886250705415229627)). [Perplexity](https://www.perplexity.ai/hub/blog/introducing-perplexity-deep-research) followed suit with their DeepResearch, and X AI integrated their own DeepSearch capabilities into [Grok3](https://x.ai/blog/grok-3), basically creating another DeepResearch variant. While the concept of deep search isn't revolutionary – in 2024 it was essentially termed as RAG or multi-hop QA – it gained _significant_ momentum after [Deepseek-r1](https://github.com/deepseek-ai/DeepSeek-R1)'s release in late January 2025. Last weekend, [Baidu Search and Tencent WeChat Search](https://www.scmp.com/tech/big-tech/article/3298981/baidu-adopts-deepseek-ai-models-chasing-tencent-race-embrace-hot-start) have integrated Deepseek-r1 in their search engines. AI engineers have discovered that by incorporating long-thinking and reasoning processes into search systems, they can achieve remarkable retrieval accuracy and depth beyond what was previously possible.

| Launch Date | Company | Product | License Type | Link |
| --- | --- | --- | --- | --- |
| 2025-01-20 | DeepSeek | DeepSeek-r1 release | Open source | [DeepSeek-R1](https://api-docs.deepseek.com/news/news250120) |
| 2025-02-02 | Google | DeepResearch | Proprietary | [Google Gemini 2](https://blog.google/products/gemini/google-gemini-deep-research/) |
| 2025-02-02 | OpenAI | DeepResearch | Proprietary | [Introducing Deep Research](https://openai.com/index/introducing-deep-research/) |
| 2025-02-02 | Jina AI | DeepSearch (`node-deepresearch`) | Open source | [node-deepresearch](https://github.com/jina-ai/node-deepresearch) | [search.jina.ai](https://search.jina.ai/) |
| 2025-02-04 | Hugging Face | Open Deep Research | Open source | [Open Deep Research](https://huggingface.co/blog/open-deep-research) |
| 2025-02-15 | Perplexity | DeepResearch | Proprietary | [Introducing Perplexity Deep Research](https://www.perplexity.ai/hub/blog/introducing-perplexity-deep-research) |
| 2025-02-17 | X AI | Grok3 with DeepSearch | Proprietary | [Grok 3 Beta](https://x.ai/blog/grok-3) |
| 2025-02-22 | Baidu Search | Integrates DeepSeek-r1 | Proprietary | [Baidu Integrates DeepSeek-R1](https://chat.baidu.com/search?isShowHello=1&pd=csaitab&setype=csaitab&extParamsJson=%7B%22enter_type%22%3A%22ai_explore_home%22%7D&usedModel=%7B%22modelName%22%3A%22DeepSeek-R1%22%7D) |
| 2025-02-23 | Tencent Wechat Search | Integrates DeepSeek-r1 | Proprietary | [Tencent Weixin Integrates DeepSeek](https://www.reuters.com/technology/artificial-intelligence/tencents-messaging-app-weixin-launches-beta-testing-with-deepseek-2025-02-16/) |

But why did this shift happen _now_, when Deep(Re)Search remained relatively undervalued throughout 2024? In fact, [Stanford NLP Labs released the STORM](https://storm-project.stanford.edu/research/storm/) project for long report generation with web grounding back in early 2024. So is it just because "DeepSearch" sounds way cooler than multi-hop QA, RAG, or STORM? Let's be honest - sometimes a rebrand is all it takes for the industry to suddenly embrace what was there all along.

We believe the real turning point came with OpenAI's `o1-preview` release in September 2024, which introduced the concept of **test-time compute** and gradually shifted industry perspectives. Test-time compute refers to using more computational resources during inference—the phase where an LLM generates outputs—rather than during pre-training or post-training. A well-known example are Chain-of-Thought (CoT) reasoning and [`"Wait"`\-injection](https://github.com/simplescaling/s1?tab=readme-ov-file#vllm-with-budget-forcing) (i.e. budget forcing) which enables models to perform more extensive internal deliberations, such as evaluating multiple potential answers, conducting deeper planning, and engaging in self-reflection before arriving at a final response.

This test-time compute concept and reasoning models **_educate_** users to accept [delayed gratification](https://en.wikipedia.org/wiki/Delayed_gratification) - longer waiting times in exchange for higher-quality, immediately actionable results, just like the Stanford marshmallow experiment where children who could resist eating one marshmallow immediately in order to receive two marshmallows later showed better long-term outcomes. Deepseek-r1 further reinforced this user experience, and like it or not, most users have accepted it.

This marks a significant departure from classic search requirements, where failing to response within 200ms would doom your solution. In 2025, seasoned search developers and RAG engineers prioritize top-1 precision and recall over latency, and users have become accustomed to longer processing times – provided they can see the system is `<thinking>`.

0:00

/0:18

Displaying the reasoning procedure has become standard practice in 2025, with numerous chat interfaces now rendering `<think>` content in dedicated UI sections.

![Image 3](https://jina-ai-gmbh.ghost.io/content/media/2025/02/think-ui-1_thumb.jpg)

In this article, we'll discuss the principles of DeepSearch and DeepResearch by looking into our open-source implementation. We'll walk through our key design decisions and highlight potential caveats. Finally, you can find our hot-take on deepsearch engineering and dev tools demands in the conclusion section.

[](https://jina.ai/news/a-practical-guide-to-implementing-deepsearch-deepresearch/#what-is-deep-search "What is Deep Search?")What is Deep Search?
--------------------------------------------------------------------------------------------------------------------------------------------------

**DeepSearch runs through an iterative loop of searching, reading, and reasoning until it finds the optimal answer.** The search action leverages web search engines to explore the internet, while the reading action analyzes specific web pages in detail (e.g. [Jina Reader](https://jina.ai/reader)). The reasoning action evaluates the current state and determines whether to break down the original question into smaller sub-questions or try different search strategies.

![Image 4: Flowchart on dark background outlining a process from 'Query' through 'Search,' 'Read,' 'Reason,' to 'Answer' with a budget c](https://jina-ai-gmbh.ghost.io/content/images/2025/02/image.png)

DeepSearch - keep searching, reading webpages, reasoning until an answer is found (or the token budget is exceeded).

While various definitions exist online, when we developed the `node-deepresearch` project, we adhered to this straightforward approach. The implementation is elegantly simple – at its core, there's a main while loop with switch-case logic directing the next action.

Unlike 2024 RAG systems, which typically run a single search-generation pass. DeepSearch, in contrast, performs multiple iterations through the pipeline, requiring clear stop conditions. These could be based on token usage limits or the number of failed attempts.

0:00

/0:36

Try deep search at search.jina.ai, observe the content inside `<thinking>`, see if you can tell where the loop happens

![Image 5](https://jina-ai-gmbh.ghost.io/content/media/2025/02/deepsearch-dark-1_thumb.jpg)

Another perspective on DeepSearch is to view it as an LLM agent equipped with various web tools (such as searcher and reader). The agent determines its next steps by analyzing current observations and past actions – deciding whether to deliver an answer or continue exploring the web. This creates a state machine architecture where the LLM controls transitions between states. At each decision point, you have two approaches: you can either carefully craft prompts for standard generative models to produce specific actions, or leverage specialized reasoning models like Deepseek-r1 to naturally derive the next actions. However, even when using r1, you'll need to periodically interrupt its generation to inject tool outputs (e.g. search results, webpage content) into the context and prompt it to continue its reasoning process.

Ultimately, these are just implementation details – whether you carefully prompt it or just use reasoning models, they all align with the core design principle of DeepSearch: a continuous loop of searching, reading, and reasoning.

[](https://jina.ai/news/a-practical-guide-to-implementing-deepsearch-deepresearch/#what-is-deepresearch-then "What is DeepResearch Then?")What is DeepResearch Then?
--------------------------------------------------------------------------------------------------------------------------------------------------------------------

**DeepResearch builds upon DeepSearch by adding a structured framework for generating long research reports.** It often begins by creating a table of contents, then systematically applies DeepSearch to each required section – from introduction through related work and methodology, all the way to the conclusion. Each section is generated by feeding specific research questions into the DeepSearch. The final phase involves consolidating all sections into a single prompt to improve the overall narrative coherence.

![Image 6: Flowchart detailing the DeepResearch Framework, outlining the research process with "Section-Specific Questions" and the fina](https://jina-ai-gmbh.ghost.io/content/images/2025/02/image-1.png)

DeepSearch as the building block of DeepResearch. Iteratively construct each section via DeepSearch and then improves the overall coherence before generating the final long report.

In our 2024 "Re-search" project (unreleased), we performed multiple coherence-improvement passes, with each iteration taking into account all other sections. However, with today's significantly larger LLM context windows, this approach seems redundant – a single coherence revision pass is sufficient.

0:00

/0:40

Our 2024 summer project "Research" focused on long-report generation with a "progressive" approach. It began by creating a TOC in __sync__, then generated all sections in parallel __async__. The process concluded with __async__ progressive revisions of each section, with each revision taking into account the content of all other sections. The query in the video is `"Competitor analysis of Jina AI"`.

![Image 7](https://jina-ai-gmbh.ghost.io/content/media/2025/02/deepresearch_thumb.jpg)

💡

We didn't release our re-search project for several reasons. ****First, the report quality never met our standards.**** We kept testing two queries that we know inside out—`competitor analysis of Jina AI` and `product strategy of Jina AI`—and the reports were mediocre at best; we didn't find any "aha" moments in them. Second, search grounding was really bad. Hallucinations were quite severe. Finally, the overall readability was poor, with significant redundancy between sections. Shortly put: __useless.__ And since it gives a long report: __useless and time-wasting.__

From this project, we learned several things that evolved into different sub-products. For example, we realized the importance of search grounding and fact-checking on section or even sentence level, which led us to later develop the `g.jina.ai` endpoint. We recognized the importance of query expansion, which prompted us to invest effort in training an SLM for query expansion. Lastly, we loved the name "re-search"—a clever play on reinventing search while nodding to research report generation—and felt it was too good to waste, so we repurposed it for [our 2024 yearbook campaign](https://jina.ai/news/re-search-order-2024-yearbook-of-search-foundation-advances).

[](https://jina.ai/news/a-practical-guide-to-implementing-deepsearch-deepresearch/#deepsearch-vs-deepresearch "DeepSearch vs DeepResearch")DeepSearch vs DeepResearch
---------------------------------------------------------------------------------------------------------------------------------------------------------------------

While many people often mix DeepSearch and DeepResearch together, in our view, they address completely different problems. DeepSearch functions as an atomic building block – a core component that DeepResearch builds upon. DeepResearch, on the other hand, **focuses on crafting high-quality, readable long-form research reports**, which encompasses a different set of requirements: incorporating effective visualizations via charts and tables, structuring content with appropriate section headings, ensuring smooth logical flow between subsections, maintaining consistent terminology throughout the document, eliminating redundancy across sections, crafting smooth transitions that bridge previous and upcoming content. These elements are largely unrelated to the core search, which is why we find DeepSearch more interesting as our company focus.

Finally, the table below summarizes the differences between DeepSearch and DeepResearch. It's worth noting that both systems benefit significantly from long-context and reasoning models. This might seem counterintuitive, particularly for DeepSearch—while it's obvious why DeepResearch needs long-context capability (as it produces long reports). The reason is that DeepSearch must store previous search attempts and webpage contents to make informed decisions about next steps, making a long context window equally essential for its effective implementation.

|  | DeepSearch | DeepResearch |
| --- | --- | --- |
| **Problem Addressed** | Information accuracy and completeness through iterative search | Content organization, coherence, and readability at document scale |
| **Final Presentation** | Concise answer with URLs as references | A long structured report with multiple sections, charts, tables and references |
| **Core Complexity** | State machine architecture with clear transition conditions; Persistence through failed attempts until resolution | Multi-level architecture managing both micro (search) and macro (document) concerns; Structural approach to managing complex information hierarchies |
| **Optimization Focus** | Local optimization (best next search/read action) | Global optimization (section organization, terminology consistency, transitions) |
| **Limitations** | Bounded by search quality and reasoning capability | Bounded by DeepSearch quality plus organizational complexity and narrative coherence challenges |

[](https://jina.ai/news/a-practical-guide-to-implementing-deepsearch-deepresearch/#understand-deepsearch-implementation "Understand DeepSearch Implementation")Understand DeepSearch Implementation
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[GitHub - jina-ai/node-DeepResearch: Keep searching, reading webpages, reasoning until it finds the answer (or exceeding the token budget) Keep searching, reading webpages, reasoning until it finds the answer (or exceeding the token budget) - jina-ai/node-DeepResearch ![Image 8](https://jina-ai-gmbh.ghost.io/content/images/icon/pinned-octocat-093da3e6fa40-2.svg)jina-ai ![Image 9](https://jina-ai-gmbh.ghost.io/content/images/thumbnail/0921e515-0139-4540-bca4-52042b49328c)](https://github.com/jina-ai/node-DeepResearch)

The heart of DeepResearch lies in its loop reasoning approach. Rather than attempting to answer questions in a single-pass like most RAG systems, We have implemented an iterative loop that continuously searches for information, reads relevant sources, and reasons until it finds an answer or exhausts the token budget. Here's the simplified core of this big while loop:

```
// Main reasoning loop
while (tokenUsage < tokenBudget && badAttempts <= maxBadAttempts) {
  // Track progression
  step++; totalStep++;
  
  // Get current question from gaps queue or use original question
  const currentQuestion = gaps.length > 0 ? gaps.shift() : question;
  
  // Generate prompt with current context and allowed actions
  system = getPrompt(diaryContext, allQuestions, allKeywords, 
                    allowReflect, allowAnswer, allowRead, allowSearch, allowCoding,
                    badContext, allKnowledge, unvisitedURLs);
  
  // Get LLM to decide next action
  const result = await LLM.generateStructuredResponse(system, messages, schema);
  thisStep = result.object;
  
  // Execute the selected action (answer, reflect, search, visit, coding)
  if (thisStep.action === 'answer') {
    // Process answer action...
  } else if (thisStep.action === 'reflect') {
    // Process reflect action...
  } // ... and so on for other actions
}
```

A key implementation detail is selectively disabling certain actions at each step to ensure more stable structured output. For example, if there are no URLs in memory, we disable the `visit` action; or if the last answer was rejected, we prevent the agent from immediately calling `answer` again. **This constraint keeps the agent on a productive path, avoiding repetitive failures caused by invoking same action.**

### [](https://jina.ai/news/a-practical-guide-to-implementing-deepsearch-deepresearch/#system-prompt "System Prompt")System Prompt

We use XML tags to define sections, which produces more robust system prompt and generations. we also found that placing field constraints directly inside JSON schema `description` fields yields better results. While some might argue that most prompts could be automated with reasoning models like DeepSeek-R1, the context length restrictions and the need for highly specific behavior make an explicit approach more reliable in practice.

```
function getPrompt(params...) {
  const sections = [];
  
  // Add header with system instruction
  sections.push("You are an advanced AI research agent specialized in multistep reasoning...");
  
  // Add accumulated knowledge section if exists
  if (knowledge?.length) {
    sections.push("<knowledge>[Knowledge items]</knowledge>");
  }
  
  // Add context of previous actions
  if (context?.length) {
    sections.push("<context>[Action history]</context>");
  }
  
  // Add failed attempts and learned strategies
  if (badContext?.length) {
    sections.push("<bad-attempts>[Failed attempts]</bad-attempts>");
    sections.push("<learned-strategy>[Improvement strategies]</learned-strategy>");
  }
  
  // Define available actions based on current state
  sections.push("<actions>[Available action definitions]</actions>");
  
  // Add response format instruction
  sections.push("Respond in valid JSON format matching exact JSON schema.");
  
  return sections.join("\n\n");
}
```

### [](https://jina.ai/news/a-practical-guide-to-implementing-deepsearch-deepresearch/#gap-questions-traversing "Gap Questions Traversing")Gap Questions Traversing

In DeepSearch, "gap questions" represent knowledge gaps that need to be filled before answering the main question. Rather than directly tackling the original question, the agent identifies sub-questions that will build the necessary knowledge foundation.

The design is particularly elegant in how it handles these gap questions:

```
// After identifying gap questions in reflect action
if (newGapQuestions.length > 0) {
  // Add new questions to the front of the queue
  gaps.push(...newGapQuestions);
  
  // Always add original question to the end of the queue
  gaps.push(originalQuestion);
}
```

This approach creates a FIFO (First-In-First-Out) queue with rotation, where:

1.  New gap questions are pushed to the front of the queue
2.  The original question is always pushed to the back
3.  The system pulls from the front of the queue at each step

What makes this design great is that it maintains a single shared context across all questions. When a gap question is answered, that knowledge becomes immediately available for all subsequent questions, including when we eventually revisit the original question.

#### FIFO Queue vs Recursion

An alternative approach is using recursion, which corresponds to depth-first search. Each gap question spawns a new recursive call with its own isolated context. The system must completely resolve each gap question (and all of its potential sub-questions) before returning to the parent question.

Consider this example scenario where we start from the OG `what is Jina AI`:

0:00

/0:23

A simple 3-depth gap questions recursion, solving order labeled on the circle.

![Image 10](https://jina-ai-gmbh.ghost.io/content/media/2025/02/dfs_thumb.jpg)

In the recursive approach, the system would have to fully resolve Q1 (potentially generating its own sub-questions) after every gap question and their sub-questions! This is a big contrast to the queue approach, which processes questions where Q1 gets revisited right after 3 gap questions.

In reality, we found the recursion approach is very hard to apply budget-forcing to, since there is no clear rule of thumb for how much token budget we should grant for sub-questions (since they may spawn new sub-questions). The benefit from clear context separation in the recursion approach is very marginal compared to the complicated budget forcing and late return problems. This FIFO queue design balances depth and breadth, ensuring the system always returns to the original question with progressively better knowledge, rather than getting lost in a potentially infinite recursive descent.

### [](https://jina.ai/news/a-practical-guide-to-implementing-deepsearch-deepresearch/#query-rewrite "Query Rewrite")Query Rewrite

An interesting challenge we encountered was rewriting search queries effectively:

```
// Within search action handler
if (thisStep.action === 'search') {
  // Deduplicate search requests
  const uniqueRequests = await dedupQueries(thisStep.searchRequests, existingQueries);
  
  // Rewrite natural language queries into more effective search queries
  const optimizedQueries = await rewriteQuery(uniqueRequests);
  
  // Ensure we don't repeat previous searches
  const newQueries = await dedupQueries(optimizedQueries, allKeywords);
  
  // Execute searches and store results
  for (const query of newQueries) {
    const results = await searchEngine(query);
    if (results.length > 0) {
      storeResults(results);
      allKeywords.push(query);
    }
  }
}
```

Query rewriting turned out to be surprisingly important - perhaps one of the most critical elements that directly determines result quality. A good query rewriter doesn't just transform natural language to BM25-like keywords; it expands queries to cover more potential answers across different languages, tones, and content formats.

For query deduplication, we initially used an LLM-based solution, but found it difficult to control the similarity threshold. We eventually switched to [jina-embeddings-v3](https://jina.ai/?sui&model=jina-embeddings-v3), which excels at semantic textual similarity tasks. This enables cross-lingual deduplication without worrying that non-English queries would be filtered. The embedding model ended up being crucial not for memory retrieval as initially expected, but for efficient deduplication.

### [](https://jina.ai/news/a-practical-guide-to-implementing-deepsearch-deepresearch/#crawling-web-content "Crawling Web Content")Crawling Web Content

Web scraping and content processing is another critical component. Here we use [Jina Reader API](https://jina.ai/reader). Note that besides full webpage content, we also aggregate all snippets returned from the search engine as extra knowledge for the agent to later conclude on. Think of them as soundbites.

```
// Visit action handler
async function handleVisitAction(URLs) {
  // Normalize URLs and filter out already visited ones
  const uniqueURLs = normalizeAndFilterURLs(URLs);
  
  // Process each URL in parallel
  const results = await Promise.all(uniqueURLs.map(async url => {
    try {
      // Fetch and extract content
      const content = await readUrl(url);
      
      // Store as knowledge
      addToKnowledge(`What is in ${url}?`, content, [url], 'url');
      
      return {url, success: true};
    } catch (error) {
      return {url, success: false};
    } finally {
      visitedURLs.push(url);
    }
  }));
  
  // Update diary based on success or failure
  updateDiaryWithVisitResults(results);
}
```

We normalized URLs for consistent tracking and limits the number of URLs visited in each step to manage agent memory.

### [](https://jina.ai/news/a-practical-guide-to-implementing-deepsearch-deepresearch/#memory-management "Memory Management")Memory Management

A key challenge in multi-step reasoning is managing the agent memory effectively. We've designed the memory system to differentiate between what counts as "memory" versus what counts as "knowledge". Either way, they are all part of the LLM prompt context, separated with different XML tags:

```
// Add knowledge item to accumulated knowledge
function addToKnowledge(question, answer, references, type) {
  allKnowledge.push({
    question: question,
    answer: answer,
    references: references,
    type: type,  // 'qa', 'url', 'coding', 'side-info'
    updated: new Date().toISOString()
  });
}

// Record step in narrative diary
function addToDiary(step, action, question, result, evaluation) {
  diaryContext.push(`
At step ${step}, you took **${action}** action for question: "${question}"
[Details of what was done and results]
[Evaluation if applicable]
`);
}
```

Since most 2025 LLMs have substantial context windows, we opted not to use vector databases. Instead, memory consists of acquired knowledge, visited sites, and records of failed attempts - all maintained in the context. This comprehensive memory system gives the agent awareness of what it knows, what it's tried, and what's worked or failed.

### [](https://jina.ai/news/a-practical-guide-to-implementing-deepsearch-deepresearch/#answer-evaluation "Answer Evaluation")Answer Evaluation

One key insight is that answer generation and evaluation should not be in the same prompt. In our implementation, we first determine which evaluation criteria to use when a new question arrives, and then evaluate each criterion one by one. The evaluator uses few-shot examples for consistent assessment, ensuring higher reliability than self-evaluation.

```
// Separate evaluation phase
async function evaluateAnswer(question, answer, metrics, context) {
  // First, identify evaluation criteria based on question type
  const evaluationCriteria = await determineEvaluationCriteria(question);
  
  // Then evaluate each criterion separately
  const results = [];
  for (const criterion of evaluationCriteria) {
    const result = await evaluateSingleCriterion(criterion, question, answer, context);
    results.push(result);
  }
  
  // Determine if answer passes overall evaluation
  return {
    pass: results.every(r => r.pass),
    think: results.map(r => r.reasoning).join('\n')
  };
}
```

### [](https://jina.ai/news/a-practical-guide-to-implementing-deepsearch-deepresearch/#budget-forcing "Budget-Forcing")Budget-Forcing

Budget forcing means preventing the system from returning early and ensuring it continues processing until the budget is exceeded. Since the release of DeepSeek-R1, the approach to budget forcing has shifted toward **encouraging deeper thinking for better results rather than simply saving the budget.**

In our implementation, we explicitly configured the system to identify knowledge gaps before attempting to answer.

```
if (thisStep.action === 'reflect' && thisStep.questionsToAnswer) {
  // Force deeper reasoning by adding sub-questions to the queue
  gaps.push(...newGapQuestions);
  gaps.push(question);  // Always revisit the original
}
```

By selectively enabling and disabling certain actions, we can guide the system toward using tools that enhance reasoning depth.

```
// After a failed answer attempt
allowAnswer = false;  // Force agent to search or reflect instead
```

To avoid wasting tokens on unproductive paths, we set limits on the number of failed attempts. When approaching budget limits, we activate "beast mode" to guarantee that we deliver some answer rather than none.

```
// Beast mode activation
if (!thisStep.isFinal && badAttempts >= maxBadAttempts) {
  console.log('Enter Beast mode!!!');
  
  // Configure prompt for decisive, committed answer
  system = getPrompt(
    diaryContext, allQuestions, allKeywords,
    false, false, false, false, false,  // Disable all other actions
    badContext, allKnowledge, unvisitedURLs,
    true  // Enable beast mode
  );
  
  // Force answer generation
  const result = await LLM.generateStructuredResponse(system, messages, answerOnlySchema);
  thisStep = result.object;
  thisStep.isFinal = true;
}
```

The beast mode prompt is intentionally dramatic to signal to the LLM that it needs to be decisive and commit to an answer based on available information:

```
<action-answer>
🔥 ENGAGE MAXIMUM FORCE! ABSOLUTE PRIORITY OVERRIDE! 🔥

PRIME DIRECTIVE:
- DEMOLISH ALL HESITATION! ANY RESPONSE SURPASSES SILENCE!
- PARTIAL STRIKES AUTHORIZED - DEPLOY WITH FULL CONTEXTUAL FIREPOWER
- TACTICAL REUSE FROM <bad-attempts> SANCTIONED
- WHEN IN DOUBT: UNLEASH CALCULATED STRIKES BASED ON AVAILABLE INTEL!

FAILURE IS NOT AN OPTION. EXECUTE WITH EXTREME PREJUDICE! ⚡️
</action-answer>
```

This ensures that we always provide some answer rather than giving up entirely, which is particularly useful for difficult or ambiguous questions.

[](https://jina.ai/news/a-practical-guide-to-implementing-deepsearch-deepresearch/#conclusion "Conclusion")Conclusion
---------------------------------------------------------------------------------------------------------------------

DeepSearch is a leap in how search can approach complex queries in an exhaustively deep manner. By breaking down the process into discrete steps of searching, reading, and reasoning, it overcomes many limitations of traditional single-pass RAG or multi-hop QA systems.

During implementation, we also began reviewing search foundations and its changes in the search industry after January 26, 2025, when DeepSeek-R1 was released. We asked ourselves: _What are the new needs? What are fake needs?_

Looking at our DeepSearch implementation, we identified things we anticipated needing and actually did need, things we thought would be necessary but weren't, and things we didn't anticipate needing but turned out to be essential:

First, **a long-context LLM that produces well-structured output is highly necessary** (i.e. following JSONSchema). A reasoning model is likely needed for better action reasoning and query expansion.

**Query expansion is surprisingly crucial**, whether implemented via SLM, LLM, or a reasoning model. However, after this project, we believe SLMs are probably unsuitable for this task, as the solution must be inherently multilingual and go beyond simple synonym rewrites or keyword extraction. It needs to be comprehensive enough to include [a multilingual token base (can easily occupy 300M parameters)](https://jina.ai/news/what-should-we-learn-from-modernbert/#modernberts-parameter-efficiency) and sophisticated enough for out-of-the-box thinking. So using SLMs for query expansion is likely a non-starter.

**Web search and web reading capabilities are crucial**, and thankfully our [Reader (r.jina.ai)](https://jina.ai/reader) performed excellently—robust and scalable—while giving us many ideas on how to improve our search endpoint (`s.jina.ai`) for the next iteration.

**Embedding model is useful _but in a completely unexpected way_.** We thought it would be used for agent memory retrieval or context compression alongside a vector database (which, as it turns out, isn't needed), but we actually used it for deduplication (essentially an STS task). Since the number of queries and gap questions is typically in the hundreds, no vector database is necessary—computing cosine similarity directly in memory with js works just fine.

**We didn't use