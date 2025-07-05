Title: Frequently Asked Questions (And Answers) About AI Evals – Hamel’s Blog

URL Source: https://hamel.dev/blog/posts/evals-faq/

Markdown Content:
This post curates the most common questions Shreya and I received while teaching 700+ engineers & PMs AI Evals. _Warning: These are sharp opinions about what works in most cases. They are not universal truths. Use your judgment._

* * *

**👉 _We are teaching our last and final cohort of our [AI Evals course](https://bit.ly/evals-ai) next month_**_(we have to get back to building). Here is a [35% discount code](https://bit.ly/evals-ai) for readers of this post._ 👈

* * *

Q: What are LLM Evals?[](https://hamel.dev/blog/posts/evals-faq/#q-what-are-llm-evals)
--------------------------------------------------------------------------------------

If you are **completely new** to product-specific LLM evals (not foundation model benchmarks), see these posts: [part 1](https://hamel.dev/evals), [part 2](https://hamel.dev/llm-judge/), [part 3](https://hamel.dev/field-guide). Otherwise, keep reading.

Q: Is RAG dead?[](https://hamel.dev/blog/posts/evals-faq/#q-is-rag-dead)
------------------------------------------------------------------------

Question: Should I avoid using RAG for my AI application after reading that [“RAG is dead”](https://pashpashpash.substack.com/p/why-i-no-longer-recommend-rag-for) for coding agents?

> Many developers are confused about when and how to use RAG after reading articles claiming “RAG is dead.” Understanding what RAG actually means versus the narrow marketing definitions will help you make better architectural decisions for your AI applications.

The viral article claiming RAG is dead specifically argues against using _naive vector database retrieval_ for autonomous coding agents, not RAG as a whole. This is a crucial distinction that many developers miss due to misleading marketing.

RAG simply means Retrieval-Augmented Generation - using retrieval to provide relevant context that improves your model’s output. The core principle remains essential: your LLM needs the right context to generate accurate answers. The question isn’t whether to use retrieval, but how to retrieve effectively.

For coding applications, naive vector similarity search often fails because code relationships are complex and contextual. Instead of abandoning retrieval entirely, modern coding assistants like Claude Code [still uses retrieval](https://x.com/pashmerepat/status/1926717705660375463?s=46) —they just employ agentic search instead of relying solely on vector databases, similar to how human developers work.

You have multiple retrieval strategies available, ranging from simple keyword matching to embedding similarity to LLM-powered relevance filtering. The optimal approach depends on your specific use case, data characteristics, and performance requirements. Many production systems combine multiple strategies or use multi-hop retrieval guided by LLM agents.

Unfortunately, “RAG” has become a buzzword with no shared definition. Some people use it to mean any retrieval system, others restrict it to vector databases. Focus on the ultimate goal: getting your LLM the context it needs to succeed. Whether that’s through vector search, agentic exploration, or hybrid approaches is a product and engineering decision.

Rather than following categorical advice to avoid or embrace RAG, experiment with different retrieval approaches and measure what works best for your application.

Q: Can I use the same model for both the main task and evaluation?[](https://hamel.dev/blog/posts/evals-faq/#q-can-i-use-the-same-model-for-both-the-main-task-and-evaluation)
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

For LLM-as-Judge selection, using the same model is usually fine because the judge is doing a different task than your main LLM pipeline. The judges we recommend building do [scoped binary classification tasks](https://hamel.dev/blog/posts/evals-faq/#q-why-do-you-recommend-binary-passfail-evaluations-instead-of-1-5-ratings-likert-scales). Focus on achieving high True Positive Rate (TPR) and True Negative Rate (TNR) with your judge on a held out labeled test set rather than avoiding the same model family. You can use these metrics on the test set to understand how well your judge is doing.

When selecting judge models, start with the most capable models available to establish strong alignment with human judgments. You can optimize for cost later once you’ve established reliable evaluation criteria. We do not recommend using the same model for open ended preferences or response quality (but we don’t recommend building judges this way in the first place!).

Q: How much time should I spend on model selection?[](https://hamel.dev/blog/posts/evals-faq/#q-how-much-time-should-i-spend-on-model-selection)
------------------------------------------------------------------------------------------------------------------------------------------------

Many developers fixate on model selection as the primary way to improve their LLM applications. Start with error analysis to understand your failure modes before considering model switching. As Hamel noted in office hours, “I suggest not thinking of switching model as the main axes of how to improve your system off the bat without evidence. Does error analysis suggest that your model is the problem?”

Q: Should I build a custom annotation tool or use something off-the-shelf?[](https://hamel.dev/blog/posts/evals-faq/#q-should-i-build-a-custom-annotation-tool-or-use-something-off-the-shelf)
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

**Build a custom annotation tool.** This is the single most impactful investment you can make for your AI evaluation workflow. With AI-assisted development tools like Cursor or Lovable, you can build a tailored interface in hours. I often find that teams with custom annotation tools iterate ~10x faster.

Custom tools excel because:

*   They show all your context from multiple systems in one place
*   They can render your data in a product specific way (images, widgets, markdown, buttons, etc.)
*   They’re designed for your specific workflow (custom filters, sorting, progress bars, etc.)

Off-the-shelf tools may be justified when you need to coordinate dozens of distributed annotators with enterprise access controls. Even then, many teams find the configuration overhead and limitations aren’t worth it.

[Isaac’s Anki flashcard annotation app](https://youtu.be/fA4pe9bE0LY) shows the power of custom tools—handling 400+ results per query with keyboard navigation and domain-specific evaluation criteria that would be nearly impossible to configure in a generic tool.

Q: Why do you recommend binary (pass/fail) evaluations instead of 1-5 ratings (Likert scales)?[](https://hamel.dev/blog/posts/evals-faq/#q-why-do-you-recommend-binary-passfail-evaluations-instead-of-1-5-ratings-likert-scales)
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

> Engineers often believe that Likert scales (1-5 ratings) provide more information than binary evaluations, allowing them to track gradual improvements. However, this added complexity often creates more problems than it solves in practice.

Binary evaluations force clearer thinking and more consistent labeling. Likert scales introduce significant challenges: the difference between adjacent points (like 3 vs 4) is subjective and inconsistent across annotators, detecting statistical differences requires larger sample sizes, and annotators often default to middle values to avoid making hard decisions.

Having binary options forces people to make a decision rather than hiding uncertainty in middle values. Binary decisions are also faster to make during error analysis - you don’t waste time debating whether something is a 3 or 4.

For tracking gradual improvements, consider measuring specific sub-components with their own binary checks rather than using a scale. For example, instead of rating factual accuracy 1-5, you could track “4 out of 5 expected facts included” as separate binary checks. This preserves the ability to measure progress while maintaining clear, objective criteria.

Start with binary labels to understand what ‘bad’ looks like. Numeric labels are advanced and usually not necessary.

Q: How do I debug multi-turn conversation traces?[](https://hamel.dev/blog/posts/evals-faq/#q-how-do-i-debug-multi-turn-conversation-traces)
--------------------------------------------------------------------------------------------------------------------------------------------

Start simple. Check if the whole conversation met the user’s goal with a pass/fail judgment. Look at the entire trace and focus on the first upstream failure. Read the user-visible parts first to understand if something went wrong. Only then dig into the technical details like tool calls and intermediate steps.

When you find a failure, reproduce it with the simplest possible test case. Here’s an example: suppose a shopping bot gives the wrong return policy on turn 4 of a conversation. Before diving into the full multi-turn complexity, simplify it to a single turn: “What is the return window for product X1000?” If it still fails, you’ve proven the error isn’t about conversation context - it’s likely a basic retrieval or knowledge issue you can debug more easily.

For generating test cases, you have two main approaches. First, you can simulate users with another LLM to create realistic multi-turn conversations. Second, use “N-1 testing” where you provide the first N-1 turns of a real conversation and test what happens next. The N-1 approach often works better since it uses actual conversation prefixes rather than fully synthetic interactions (but is less flexible and doesn’t test the full conversation). User simulation is getting better as models improve. Keep an eye on this space.

The key is balancing thoroughness with efficiency. Not every multi-turn failure requires multi-turn analysis.

Q: Should I build automated evaluators for every failure mode I find?[](https://hamel.dev/blog/posts/evals-faq/#q-should-i-build-automated-evaluators-for-every-failure-mode-i-find)
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Focus automated evaluators on failures that persist after fixing your prompts. Many teams discover their LLM doesn’t meet preferences they never actually specified - like wanting short responses, specific formatting, or step-by-step reasoning. Fix these obvious gaps first before building complex evaluation infrastructure.

Consider the cost hierarchy of different evaluator types. Simple assertions and reference-based checks (comparing against known correct answers) are cheap to build and maintain. LLM-as-Judge evaluators require 100+ labeled examples, ongoing weekly maintenance, and coordination between developers, PMs, and domain experts. This cost difference should shape your evaluation strategy.

Only build expensive evaluators for problems you’ll iterate on repeatedly. Since LLM-as-Judge comes with significant overhead, save it for persistent generalization failures - not issues you can fix trivially. Start with cheap code-based checks where possible: regex patterns, structural validation, or execution tests. Reserve complex evaluation for subjective qualities that can’t be captured by simple rules.

Q: How many people should annotate my LLM outputs?[](https://hamel.dev/blog/posts/evals-faq/#q-how-many-people-should-annotate-my-llm-outputs)
----------------------------------------------------------------------------------------------------------------------------------------------

For most small to medium-sized companies, appointing a single domain expert as a “benevolent dictator” is the most effective approach. This person—whether it’s a psychologist for a mental health chatbot, a lawyer for legal document analysis, or a customer service director for support automation—becomes the definitive voice on quality standards.

A single expert eliminates annotation conflicts and prevents the paralysis that comes from “too many cooks in the kitchen”. The benevolent dictator can incorporate input and feedback from others, but they drive the process. If you feel like you need five subject matter experts to judge a single interaction, it’s a sign your product scope might be too broad.

However, larger organizations or those operating across multiple domains (like a multinational company with different cultural contexts) may need multiple annotators. When you do use multiple people, you’ll need to measure their agreement using metrics like Cohen’s Kappa, which accounts for agreement beyond chance. However, use your judgment. Even in larger companies, a single expert is often enough.

Start with a benevolent dictator whenever feasible. Only add complexity when your domain demands it.

Q: What gaps in eval tooling should I be prepared to fill myself?[](https://hamel.dev/blog/posts/evals-faq/#q-what-gaps-in-eval-tooling-should-i-be-prepared-to-fill-myself)
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Most eval tools handle the basics well: logging complete traces, tracking metrics, prompt playgrounds, and annotation queues. These are table stakes. Here are four areas where you’ll likely need to supplement existing tools.

Watch for vendors addressing these gaps—it’s a strong signal they understand practitioner needs.

#### 1. Error Analysis and Pattern Discovery[](https://hamel.dev/blog/posts/evals-faq/#error-analysis-and-pattern-discovery)

After reviewing traces where your AI fails, can your tooling automatically cluster similar issues? For instance, if multiple traces show the assistant using casual language for luxury clients, you need something that recognizes this broader “persona-tone mismatch” pattern. We recommend building capabilities that use AI to suggest groupings, rewrite your observations into clearer failure taxonomies, help find similar cases through semantic search, etc.

#### 2. AI-Powered Assistance Throughout the Workflow[](https://hamel.dev/blog/posts/evals-faq/#ai-powered-assistance-throughout-the-workflow)

The most effective workflows use AI to accelerate every stage of evaluation. During error analysis, you want an LLM helping categorize your open-ended observations into coherent failure modes. For example, you might annotate several traces with notes like “wrong tone for investor,” “too casual for luxury buyer,” etc. Your tooling should recognize these as the same underlying pattern and suggest a unified “persona-tone mismatch” category.

You’ll also want AI assistance in proposing fixes. After identifying 20 cases where your assistant omits pet policies from property summaries, can your workflow analyze these failures and suggest specific prompt modifications? Can it draft refinements to your SQL generation instructions when it notices patterns of missing WHERE clauses?

Additionally, good workflows help you conduct data analysis of your annotations and traces. I like using notebooks with AI in-the-loop like [Julius](https://julius.ai/),[Hex](https://hex.tech/) or [SolveIt](https://solveit.fast.ai/). These help me discover insights like “location ambiguity errors spike 3x when users mention neighborhood names” or “tone mismatches occur 80% more often in email generation than other modalities.”

#### 3. Custom Evaluators Over Generic Metrics[](https://hamel.dev/blog/posts/evals-faq/#custom-evaluators-over-generic-metrics)

Be prepared to build most of your evaluators from scratch. Generic metrics like “hallucination score” or “helpfulness rating” rarely capture what actually matters for your application—like proposing unavailable showing times or omitting budget constraints from emails. In our experience, successful teams spend most of their effort on application-specific metrics.

#### 4. APIs That Support Custom Annotation Apps[](https://hamel.dev/blog/posts/evals-faq/#apis-that-support-custom-annotation-apps)

Custom annotation interfaces [work best for most teams](https://hamel.dev/blog/posts/evals-faq/#q-should-i-build-a-custom-annotation-tool-or-use-something-off-the-shelf). This requires observability platforms with thoughtful APIs. I often have to build my own libraries and abstractions just to make bulk data export manageable. You shouldn’t have to paginate through thousands of requests or handle timeout-prone endpoints just to get your data. Look for platforms that provide true bulk export capabilities and, crucially, APIs that let you write annotations back efficiently.

Q: What is the best approach for generating synthetic data?[](https://hamel.dev/blog/posts/evals-faq/#q-what-is-the-best-approach-for-generating-synthetic-data)
----------------------------------------------------------------------------------------------------------------------------------------------------------------

A common mistake is prompting an LLM to `"give me test queries"` without structure, resulting in generic, repetitive outputs. A structured approach using dimensions produces far better synthetic data for testing LLM applications.

**Start by defining dimensions**: categories that describe different aspects of user queries. Each dimension captures one type of variation in user behavior. For example:

*   For a recipe app, dimensions might include Dietary Restriction (_vegan_, _gluten-free_, _none_), Cuisine Type (_Italian_, _Asian_, _comfort food_), and Query Complexity (_simple request_, _multi-step_, _edge case_).
*   For a customer support bot, dimensions could be Issue Type (_billing_, _technical_, _general_), Customer Mood (_frustrated_, _neutral_, _happy_), and Prior Context (_new issue_, _follow-up_, _resolved_).

**Choose dimensions that target likely failure modes.** If you suspect your recipe app struggles with scaling ingredients for large groups or your support bot mishandles angry customers, make those dimensions. Use your application first—you need hypotheses about where failures occur. Without this, you’ll generate useless test data.

**Once you have dimensions, create tuples:** specific combinations selecting one value from each dimension. A tuple like (_Vegan_, _Italian_, _Multi-step_) represents a particular use case. Write 20 tuples manually to understand your problem space, then use an LLM to scale up.

The two-step generation process is important. First, have the LLM generate structured tuples. Then, in a separate prompt, convert each tuple to a natural language query. This separation prevents repetitive phrasing. For the vegan Italian tuple above, you might get `"I need a dairy-free lasagna recipe that I can prep the day before."`

**Don’t generate synthetic data for problems you can fix immediately.** If your prompt never mentions handling dietary restrictions, fix the prompt rather than generating hundreds of specialized queries. Save synthetic data for complex issues requiring iteration—like an LLM consistently failing at ingredient scaling math or misinterpreting ambiguous requests.

After iterating on your tuples and prompts, **run these synthetic queries through your actual system to capture full traces**. Sample 100 traces for error analysis. This number provides enough traces to manually review and identify failure patterns without being overwhelming. Rather than generating thousands of similar queries, ensure your 100 traces cover diverse combinations across your dimensions—this variety will reveal more failure modes than sheer volume.

Q: How do I approach evaluation when my system handles diverse user queries?[](https://hamel.dev/blog/posts/evals-faq/#q-how-do-i-approach-evaluation-when-my-system-handles-diverse-user-queries)
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

> Complex applications often support vastly different query patterns—from “What’s the return policy?” to “Compare pricing trends across regions for products matching these criteria.” Each query type exercises different system capabilities, leading to confusion on how to design eval criteria.

**_[Error Analysis](https://youtu.be/e2i6JbU2R-s?si=8p5XVxbBiioz69Xc) is all you need._** Your evaluation strategy should emerge from observed failure patterns (e.g.error analysis), not predetermined query classifications. Rather than creating a massive evaluation matrix covering every query type you can imagine, let your system’s actual behavior guide where you invest evaluation effort.

During error analysis, you’ll likely discover that certain query categories share failure patterns. For instance, all queries requiring temporal reasoning might struggle regardless of whether they’re simple lookups or complex aggregations. Similarly, queries that need to combine information from multiple sources might fail in consistent ways. These patterns discovered through error analysis should drive your evaluation priorities. It could be that query category is a fine way to group failures, but you don’t know that until you’ve analyzed your data.

To see an example of basic error analysis in action, [see this video](https://youtu.be/e2i6JbU2R-s?si=8p5XVxbBiioz69Xc).

* * *

**👉 _We are teaching our last and final cohort of our [AI Evals course](https://bit.ly/evals-ai) next month_**_(we have to get back to building). Here is a [35% discount code](https://bit.ly/evals-ai) for readers of this post._ 👈

* * *

Q: How do I choose the right chunk size for my document processing tasks?[](https://hamel.dev/blog/posts/evals-faq/#q-how-do-i-choose-the-right-chunk-size-for-my-document-processing-tasks)
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Unlike RAG, where chunks are optimized for retrieval, document processing assumes the model will see every chunk. The goal is to split text so the model can reason effectively without being overwhelmed. Even if a document fits within the context window, it might be better to break it up. Long inputs can degrade performance due to attention bottlenecks, especially in the middle of the context. Two task types require different strategies:

### 1. Fixed-Output Tasks → Large Chunks[](https://hamel.dev/blog/posts/evals-faq/#fixed-output-tasks-large-chunks)

These are tasks where the output length doesn’t grow with input: extracting a number, answering a specific question, classifying a section. For example:

*   “What’s the penalty clause in this contract?”
*   “What was the CEO’s salary in 2023?”

Use the largest chunk (with caveats) that likely contains the answer. This reduces the number of queries and avoids context fragmentation. However, avoid adding irrelevant text. Models are sensitive to distraction, especially with large inputs. The middle parts of a long input might be under-attended. Furthermore, if cost and latency are a bottleneck, you should consider preprocessing or filtering the document (via keyword search or a lightweight retriever) to isolate relevant sections before feeding a huge chunk.

### 2. Expansive-Output Tasks → Smaller Chunks[](https://hamel.dev/blog/posts/evals-faq/#expansive-output-tasks-smaller-chunks)

These include summarization, exhaustive extraction, or any task where output grows with input. For example:

*   “Summarize each section”
*   “List all customer complaints”

In these cases, smaller chunks help preserve reasoning quality and output completeness. The standard approach is to process each chunk independently, then aggregate results (e.g., map-reduce). When sizing your chunks, try to respect content boundaries like paragraphs, sections, or chapters. Chunking also helps mitigate output limits. By breaking the task into pieces, each piece’s output can stay within limits.

### General Guidance[](https://hamel.dev/blog/posts/evals-faq/#general-guidance)

It’s important to recognize **why chunk size affects results**. A larger chunk means the model has to reason over more information in one go – essentially, a heavier cognitive load. LLMs have limited capacity to **retain and correlate details across a long text**. If too much is packed in, the model might prioritize certain parts (commonly the beginning or end) and overlook or “forget” details in the middle. This can lead to overly coarse summaries or missed facts. In contrast, a smaller chunk bounds the problem: the model can pay full attention to that section. You are trading off **global context for local focus**.

No rule of thumb can perfectly determine the best chunk size for your use case – **you should validate with experiments**. The optimal chunk size can vary by domain and model. I treat chunk size as a hyperparameter to tune.

Q: How should I approach evaluating my RAG system?[](https://hamel.dev/blog/posts/evals-faq/#q-how-should-i-approach-evaluating-my-rag-system)
----------------------------------------------------------------------------------------------------------------------------------------------

RAG systems have two distinct components that require different evaluation approaches: retrieval and generation.

The retrieval component is a search problem. Evaluate it using traditional information retrieval (IR) metrics. Common examples include Recall@k (of all relevant documents, how many did you retrieve in the top k?), Precision@k (of the k documents retrieved, how many were relevant?), or MRR (how high up was the first relevant document?). The specific metrics you choose depend on your use case. These metrics are pure search metrics that measure whether you’re finding the right documents (more on this below).

To evaluate retrieval, create a dataset of queries paired with their relevant documents. Generate this synthetically by taking documents from your corpus, extracting key facts, then generating questions those facts would answer. This reverse process gives you query-document pairs for measuring retrieval performance without manual annotation.

For the generation component—how well the LLM uses retrieved context, whether it hallucinates, whether it answers the question—use the same evaluation procedures covered throughout this course: error analysis to identify failure modes, collecting human labels, building LLM-as-judge evaluators, and validating those judges against human annotations.

Jason Liu’s [“There Are Only 6 RAG Evals”](https://jxnl.co/writing/2025/05/19/there-are-only-6-rag-evals/) provides a framework that maps well to this separation. His Tier 1 covers traditional IR metrics for retrieval. Tiers 2 and 3 evaluate relationships between Question, Context, and Answer—like whether the context is relevant (C|Q), whether the answer is faithful to context (A|C), and whether the answer addresses the question (A|Q).

In addition to Jason’s six evals, error analysis on your specific data may reveal domain-specific failure modes that warrant their own metrics. For example, a medical RAG system might consistently fail to distinguish between drug dosages for adults versus children, or a legal RAG might confuse jurisdictional boundaries. These patterns emerge only through systematic review of actual failures. Once identified, you can create targeted evaluators for these specific issues beyond the general framework.

Finally, when implementing Jason’s Tier 2 and 3 metrics, don’t just use prompts off the shelf. The standard LLM-as-judge process requires several steps: error analysis, prompt iteration, creating labeled examples, and measuring your judge’s accuracy against human labels. Once you know your judge’s True Positive and True Negative rates, you can correct its estimates to determine the actual failure rate in your system. Skip this validation and your judges may not reflect your actual quality criteria.

In summary, debug retrieval first using IR metrics, then tackle generation quality using properly validated LLM judges.

Q: What makes a good custom interface for reviewing LLM outputs?[](https://hamel.dev/blog/posts/evals-faq/#q-what-makes-a-good-custom-interface-for-reviewing-llm-outputs)
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Great interfaces make human review fast, clear, and motivating. We recommend [building your own annotation tool](https://hamel.dev/blog/posts/evals-faq/#q-should-i-build-a-custom-annotation-tool-or-use-something-off-the-shelf) customized to your domain. The following features are possible enhancements we’ve seen work well, but you don’t need all of them. The screenshots shown are illustrative examples to clarify concepts. In practice, I rarely implement all these features in a single app. It’s ultimately a judgment call based on your specific needs and constraints.

**1. Render Traces Intelligently, Not Generically**: Present the trace in a way that’s intuitive for the domain. If you’re evaluating generated emails, render them to look like emails. If the output is code, use syntax highlighting. Allow the reviewer to see the full trace (user input, tool calls, and LLM reasoning), but keep less important details in collapsed sections that can be expanded. Here is an example of a custom annotation tool for reviewing real estate assistant emails:

![Image 1](https://hamel.dev/blog/posts/evals-faq/images/emailinterface1.png)

A custom interface for reviewing emails for a real estate assistant.

**2. Show Progress and Support Keyboard Navigation**: Keep reviewers in a state of flow by minimizing friction and motivating completion. Include progress indicators (e.g., “Trace 45 of 100”) to keep the review session bounded and encourage completion. Enable hotkeys for navigating between traces (e.g., N for next), applying labels, and saving notes quickly. Below is an illustration of these features:

![Image 2](https://hamel.dev/blog/posts/evals-faq/images/hotkey.png)

An annotation interface with a progress bar and hotkey guide

**4. Trace navigation through clustering, filtering, and search**: Allow reviewers to filter traces by metadata or search by keywords. Semantic search helps find conceptually similar problems. Clustering similar traces (like grouping by user persona) lets reviewers spot recurring issues and explore hypotheses. Below is an illustration of these features:

![Image 3](https://hamel.dev/blog/posts/evals-faq/images/group1.png)

Cluster view showing groups of emails, such as property-focused or client-focused examples. Reviewers can drill into a group to see individual traces.

**5. Prioritize labeling traces you think might be problematic**: Surface traces flagged by guardrails, CI failures, or automated evaluators for review. Provide buttons to take actions like adding to datasets, filing bugs, or re-running pipeline tests. Display relevant context (pipeline version, eval scores, reviewer info) directly in the interface to minimize context switching. Below is an illustration of these ideas:

![Image 4](https://hamel.dev/blog/posts/evals-faq/images/ci.png)

A trace view that allows you to quickly see auto-evaluator verdict, add traces to dataset or open issues. Also shows metadata like pipeline version, reviewer info, and more.

### General Principle: Keep it minimal[](https://hamel.dev/blog/posts/evals-faq/#general-principle-keep-it-minimal)

Keep your annotation interface minimal. Only incorporate these ideas if they provide a benefit that outweighs the additional complexity and maintenance overhead.

Q: How much of my development budget should I allocate to evals?[](https://hamel.dev/blog/posts/evals-faq/#q-how-much-of-my-development-budget-should-i-allocate-to-evals)
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

It’s important to recognize that evaluation is part of the development process rather than a di