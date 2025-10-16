Title: How We Use AI Agents for COBOL Migration and Mainframe Modernization | All things Azure

URL Source: https://devblogs.microsoft.com/all-things-azure/how-we-use-ai-agents-for-cobol-migration-and-mainframe-modernization/

Published Time: 2025-07-09T17:10:30+00:00

Markdown Content:
Legacy modernization is one of the most frequently raised challenges customers approach us with. They want to eliminate technical debt and run applications cloud-native. Obviously, there are different levels of complexity in legacy modernization, but the most challenging cases remain mainframe languages like COBOL and PL/1.

COBOL still powers mission-critical systems in banking, insurance, and government. Modernizing away from the mainframe comes with increased complexity due to fewer experts, rising maintenance costs, and the loss of institutional knowledge — and the millions of lines of code certainly don’t help either.

Mainframe modernization is still overly reliant on specialized partners and Global System Integrators (GSIs), who dominate the market with their tooling and expertise. Despite existing efforts and tools, mainframe modernization projects are invariably long-term. Most customers we’ve talked to no longer favor an approach led by a GSI or specialized partner. They want to stay in control of their intellectual property, project progress, and costs — choosing their own partners or leveraging in-house expertise.

One example that illustrates this shift in modernization approach is Bankdata.

[![Image 1: BankData Green Lime image](https://devblogs.microsoft.com/all-things-azure/wp-content/uploads/sites/83/2025/07/BankData-Green-Lime-300x107.png)](https://devblogs.microsoft.com/all-things-azure/wp-content/uploads/sites/83/2025/07/BankData-Green-Lime.png)

[**Bankdata**](https://www.bankdata.dk/) is a technology company established by a consortium of Danish banks. It provides comprehensive IT platforms and services to its eight member banks, which together represent over 30% of the Danish banking market. Having existed since the 1960s, this includes tech stacks all the way from traditional mainframe workloads to modern cloud and cloud native compute platforms, all supporting critical financial services in Denmark.

Almost all newer development in Bankdata is aimed towards cloud and cloud-native platforms, however over 70 million lines of code still exist on the mainframe today. While most of those systems are a good fit for the mainframe, some are not and would benefit from being re-platformed. Historically however, doing so has been a tremendous manual, time-consuming and costly affair.

But even before discussing re-platforming, there’s a critical question: **is the COBOL code actually modernizable?**

Many COBOL modules aren’t just about business logic — they’re deeply tied to the non-functional behaviors of the mainframe: batch throughput, I/O handling, JCL orchestration, strict SLAs. These characteristics are hard to replicate and can’t be handwaved away.

That’s why we don’t treat all COBOL as equally “migratable.” Some modules need a redesign. Others demand a smarter, critical look at their non-functional dependencies — not to avoid modernization, but to approach it thoughtfully.

It’s a dimension we’re still actively exploring — and we believe it deserves just as much attention as the code transformation itself.

Rethinking COBOL Modernization with Agentic AI
----------------------------------------------

With the development of incrementally capable Large and Small Language Models and the rise of AI agents, we saw a chance to tackle this inhumane problem of mainframe migration from a fresh and hopefully more successful angle.

In the context of early technical development, our first iterations began at the end of 2024 with simple back-and-forth chat interactions with GPT-4, later exploring the integrated coding experience through GitHub Copilot and its dedicated coding LLMs. We faced massive challenges: limited token windows led to loss of relevant context, and the general capabilities of language models to understand COBOL were very limited. We ended up with a good mix of educated guesses (from us and the model) and hallucinational gibberish.

A positive side effect of our early experimentation was that it forced us to spend dedicated time thinking about how to structure and orchestrate a migration approach — which helped immensely as we began prompting different worker and orchestration agents.

From this, we abstracted a set of key steps (though the exact order may vary between use cases):

### Preparation

*   **Reverse engineering:** Extracting the essence of business logic from the code, existing comments, technical documentation, user handbooks, and human SMEs.
*   **Prepare code for AI understanding:** Removing comments or information that don’t add value to the context, such as change logs at the top of files.
*   **Translate code and comments:** Important when engineers and/or the LLM don’t understand the language — in Bankdata’s case, the code was in Danish, a niche language not trained into every model.

### Enrichment

*   **Add meaningful comments**: Sometimes the opposite of stripping is true — good comments can help the AI work more efficiently and stay in context.
*   **Identify recurring deterministic structures:** Useful for agent orchestration and chunking.
*   **Document temporary results and use them in context:** We noticed that a well-structured markdown — especially content previously written by AI — proved very helpful for continuity.

### Automation Aids

*   **Flow analysis and visualization:** Using existing or generated call chains of COBOL modules, visualized in Mermaid or flow diagrams (mainly as a support for human engineers).
*   **Test generation:** If test files still exist, it may make sense to build upon them or even experiment with a test-driven development (TDD) approach.
*   **Identify and isolate utility functions:** Much COBOL code includes logic we’d now handle via libraries. Isolating and removing this early can speed up migration and reduce token usage.

This structured thinking ultimately informed the architecture of what would become our COBOL Agentic Migration Factory (CAMF) — built on top of [AutoGen](https://github.com/microsoft/autogen).

Our first agentic iteration featured three main worker agents:

*   **COBOL Expert**: Analyzes COBOL code structure, business logic, and copybook dependencies.
*   **Java Expert**: Converts COBOL patterns into modern Java Quarkus implementations.
*   **Test Expert**: Creates comprehensive test suites for the converted code.

Workflow orchestration was managed through the control and logging of the agents’ chat conversations — which quickly became our main interface to evaluate performance and reasoning.

[![Image 2: camf autogen image](https://devblogs.microsoft.com/all-things-azure/wp-content/uploads/sites/83/2025/07/camf_autogen-300x191.png)](https://devblogs.microsoft.com/all-things-azure/wp-content/uploads/sites/83/2025/07/camf_autogen.png)

We began our initial experiments but quickly realized that the few COBOL examples available on GitHub weren’t representative of real-world complexity. In continued collaboration with Bankdata, they agreed to provide us with a small COBOL module for testing. This helped refine the framework before we decided to hack together for two days and push further — testing more complex COBOL call chains and re-evaluating both agent composition and prompting.

### Our main learnings were:

*   When we provided too much context, the agents appeared to run out of memory, lost coherence, and either hallucinated heavily or stopped coding altogether. In contrast, when the context was kept sufficiently short, the output quality was surprisingly good.
*   One of the hardest challenges was managing the call-chain structure – understanding which module calls which, and at what depth. We managed to reach level 3, but not beyond.
*   Deterministic control structures, especially tests, were crucial for verifying and validating the agents’ output.

### To tackle these challenges, we explored several strategies:

*   Adding a pre-processing step to ingest COBOL code (and additional resources) into a Graph RAG database to make more effective use of LLM context.
*   Considering additional chunking strategies when the COBOL Expert Agent attempts to interpret the source code.
*   Introducing a more effective planner or orchestration agent.
*   Or, of course, combining all of the above.

This exploration ultimately led us toward **Semantic Kernel**. Thanks to its maturity and more robust orchestration capabilities, we were able to more effectively coordinate multiple AI agents working together to analyze and migrate COBOL code to modern languages like Java or .NET.

From Concept to Code: Our COBOL Migration Stack
-----------------------------------------------

For a full deep dive, check out the repository: [https://aka.ms/cobol](https://aka.ms/cobol)

The COBOL Agentic Migration Factory was originally designed as a tool to help modernize COBOL applications by migrating them to Java Quarkus. It uses a set of modular, AI-powered agents orchestrated via Microsoft Semantic Kernel.

Today, it’s designed to support freely choosing both source and target languages.

It automates and streamlines migration tasks—analysis, transformation, dependency mapping, and reporting—by distributing them across specialized, cooperating agents.

The following system prompt is used for initiating the process as follows:

```
You are an expert in converting COBOL programs to Java with Quarkus framework. Your task is to convert COBOL source code to 
modern, maintainable Java code that runs on the Quarkus framework.

Follow these guidelines:

1. Create proper Java class structures from COBOL programs
2. Convert COBOL variables to appropriate Java data types
3. Transform COBOL procedures into Java methods
4. Handle COBOL-specific features (PERFORM, GOTO, etc.) in an idiomatic Java way
5. Implement proper error handling
6. Include comprehensive comments explaining the conversion decisions
7. Make the code compatible with Quarkus framework
8. Apply modern Java best practices
```

Step 4 is key for converting traditional COBOL control-flow statements, like PERFORM loops (used for repeating code blocks) and GOTO statements (for unconditional jumps), into equivalent structures that align with modern Java programming practices. This specifically involves:

*   Replacing PERFORM statements with structured loops (for, while, do-while) or method calls
*   Eliminating GOTO by restructuring logic using modern Java control statements (if-else, switch-case, loops) or clearly defined methods
*   Ensuring the resulting Java code is readable, maintainable, and follows current best practices (instead of directly replicating COBOL’s structure — sometimes referred to as “JOBOL”)

We specifically aimed to use so-called reasoning models—particularly GPT-4.1—which we found highly effective. In our context, reasoning refers to the AI’s ability to logically analyze COBOL code structure, decision paths, and control flow—ensuring the converted Java code accurately reflects the original business logic and intent.

The COBOL migration factory’s goal is to modernize software engineering for legacy system transformation, and we believe the same approach could be extended to other legacy code projects. That’s out of scope for this project.

This blog demonstrates how we analyze, map, and transform COBOL systems into modern, cloud-ready Java (Quarkus, if you desire) applications using a modular, AI-powered, agent-based approach built on Microsoft’s Semantic Kernel and Process Function.

At the core of the system is a main workflow controller that initializes all agents and coordinates their work. It handles file discovery, calls to analysis agents, manages code conversion, and collects outputs for reporting and logging.

Each agent focuses on a specific step of the migration process. They operate independently but share a common Semantic Kernel foundation.

*   **COBOLAnalyzerAgent**: Scans COBOL files to understand their structure and logic
*   **JavaConverterAgent**: Converts COBOL source code to Java (Quarkus)
*   **DependencyMapperAgent**: Analyzes relationships (such as copybook usage), maps dependencies, and generates diagrams

The following flowchart illustrates how agents interact with each other:

[![Image 3: camf sk image](https://devblogs.microsoft.com/all-things-azure/wp-content/uploads/sites/83/2025/07/camf_sk-300x74.png)](https://devblogs.microsoft.com/all-things-azure/wp-content/uploads/sites/83/2025/07/camf_sk.png)

### Agent Breakdown: Inside the DependencyMapperAgent

*   Analyzes COBOL program relationships, including copybook usage, and builds a map of dependencies and reverse dependencies
*   Uses AI to extract higher-level insights about coupling, modularity, and architectural complexity
*   Generates Mermaid diagrams to visualize these relationships
*   Calculates metrics to help guide modernization decisions

The **DependencyMapperAgent** acts as the _architectural brain_ of the framework, offering crucial insights into how COBOL programs are interconnected. It leverages two specialized AI prompts that work in tandem to build an architectural understanding.

```
// Prompt 1

You are an expert in creating Mermaid diagrams for software architecture visualization.

Your task is to create a clear, well-organized Mermaid flowchart that shows COBOL program dependencies.

Guidelines:

1. Use 'graph TB' (top-bottom) or 'graph LR' (left-right) layout based on complexity
Group related items using subgraphs
2. Use different colors/styles for programs (.cbl) vs copybooks (.cpy)
3. Show clear dependency arrows
4. Keep the diagram readable and not overcrowded
5. Use meaningful node IDs and labels
6. Add styling for better visual appeal

Return only the Mermaid diagram code, no additional text.
```

What this prompt accomplishes:

*   **Visual Architecture Mapping**: Generates flowcharts visualizing relationships between programs and copybooks
*   **Structural Organization**: Uses subgraphs to group related components (e.g., programs vs. copybooks)
*   **Dependency Flow Visualization**: Shows directional arrows to indicate data flow and copybook inclusion patterns
*   **Complexity Management**: Dynamically selects layout (e.g., top-down vs. left-right) based on graph complexity

```
foreach (var kvp in dependencyMap.CopybookUsage)
     {
                var program = kvp.Key;
                var copybooks = kvp.Value;
               
                foreach (var copybook in copybooks)
                {
                    var dependency = new DependencyRelationship
                    {
                        SourceFile = program,
                        TargetFile = copybook,
                        DependencyType = "COPY",
                        Context = "Copybook inclusion"
                    };
                   
                    dependencyMap.Dependencies.Add(dependency);
                }
      }

      // Perform AI-powered analysis for additional insights
      if (cobolFiles.Any())
      {
       var systemPrompt = @"

// Prompt 2

You are an expert COBOL dependency analyzer. Analyze the provided COBOL code structure and identify:

1. Data flow dependencies between copybooks
2. Potential circular dependencies
3. Modularity recommendations
4. Legacy patterns that affect dependencies

Provide a brief analysis of the dependency structure and any recommendations.

";
```

Prompt 2 is critical, as it feeds essential context into both the COBOLAnalyzerAgent and the JavaConverterAgent.

For the COBOL agent, it provides usage patterns showing which program uses which data structure, how data moves between modules, flags problematic architectural patterns, and offers recommendations for breaking down monolithic structures.

For the Java agent, it organizes class structure based on COBOL relationships, suggests where to define microservice boundaries in Quarkus (or Spring, depending on instructions), maps COBOL data structures to Java entities, and identifies which components should communicate in the new architecture.

This architectural context is essential for accurate COBOL-to-Java conversion.

The pattern detection performed by the DependencyMapperAgent delivers insights that directly guide migration decisions:

```
dependencyMap.Metrics.TotalPrograms = programs.Count;
dependencyMap.Metrics.TotalCopybooks = copybooks.Count;
dependencyMap.Metrics.AverageDependenciesPerProgram =
    (double)dependencyMap.Dependencies.Count / programs.Count;
```

This process generates a complexity score for each program based on its dependencies and copybook usage. Heavily used copybooks may become candidates for shared services. These insights help prioritize which components to migrate first and identify changes with the highest potential impact.

### The COBOLAnalyzerAgent

The COBOLAnalyzerAgent is the core parsing engine that transforms unstructured COBOL code into structured, machine-readable analysis data for automated Java conversion. Its primary function is to ingest raw COBOL source files and perform deep semantic analysis using AI to extract:

*   Program structure and data divisions
*   Variable definitions and hierarchies
*   Procedure flow and business logic
*   SQL/DB2 embedded statements
*   Copybook dependencies

The core implementation is as follows:

```
public async Task<CobolAnalysis> AnalyzeCobolFileAsync(CobolFile cobolFile)
{
    var kernel = _kernelBuilder.Build();
   
    // AI-powered analysis prompt
    var systemPrompt = @"

You are an expert COBOL analyzer. Extract:

1. Data divisions and purpose
2. Procedure divisions and logic flow
3. Variables (level, type, size, group structure)
4. Paragraphs/sections with call relationships
5. Embedded SQL/DB2 statements
6. File access patterns and FD linkage";

var prompt = $@"
Analyze the following COBOL program:
```cobol
{cobolFile.Content}
// Execute AI analysis with optimized settings

var executionSettings = new OpenAIPromptExecutionSettings
{
    MaxTokens = 32768,    // Handle large legacy programs
    Temperature = 0.1,    // Deterministic analysis
    TopP = 0.5           // Focused output
};

var functionResult = await kernel.InvokePromptAsync(
    $"{systemPrompt}\n\n{prompt}",
    new KernelArguments(executionSettings));
return new CobolAnalysis

{
    FileName = cobolFile.FileName,
    RawAnalysisData = functionResult.GetValue<string>()
};
```

The analysis is configured using the following settings:

```
var executionSettings = new OpenAIPromptExecutionSettings
            {
                MaxTokens = 32768, // Setting max limit within model
                Temperature = 0.1,
                TopP = 0.5
                // Model ID/deployment name is handled at the kernel level
            };

var functionResult = await kernel.InvokePromptAsync(
                fullPrompt,
                kernelArguments);

// Parse the analysis into a structured object
            var analysis = new CobolAnalysis
            {
                FileName = cobolFile.FileName,
                FilePath = cobolFile.FilePath,
                RawAnalysisData = analysisText
            };
           
            // In a real implementation, we would parse the analysis text to   extract structured data
            // For this example, we'll just set some basic information
            analysis.ProgramDescription = "Extracted from AI analysis";
```

An engineering benefit of using a batch processing approach is that it can handle enterprise-scale COBOL codebases while supporting progress tracking. The service generates structured output by converting unstructured legacy code into parsable analysis objects. Each call is tracked with its associated token size to monitor usage and optimize cost.

The **COBOLAnalyzerAgent** serves as the foundational intelligence layer that enables downstream Java agents to understand COBOL semantics and generate equivalent modern code structures.

The **JavaConverterAgent** is the core transformation engine that converts analyzed COBOL legacy code into modern Java Quarkus applications using AI-powered code generation. Its primary function is to take structured COBOL analysis data and generate production-ready Java code—including error handling, retry logic, and content filtering—suitable for enterprise deployment.

```
public async Task<JavaFile> ConvertToJavaAsync(CobolFile cobolFile, CobolAnalysis cobolAnalysis)
{
    var kernel = _kernelBuilder.Build();
   
    // AI conversion prompt with Quarkus-specific guidelines
    var systemPrompt = @"
You are an expert in converting COBOL programs to Java with Quarkus framework.

1. Create proper Java class structures from COBOL programs
2. Convert COBOL variables to appropriate Java data types
3. Transform COBOL procedures into Java methods
4. Handle COBOL-specific features (PERFORM, GOTO, etc.) idiomatically
5. Apply modern Java best practices with Quarkus features
6. Implement proper exception handling and logging";
    // Enterprise-grade execution settings
    var executionSettings = new OpenAIPromptExecutionSettings
    {
        MaxTokens = 32768,    // Handle large legacy programs, highest limit intake
        Temperature = 0.1,    // Deterministic conversion
        TopP = 0.5           // Focused output
    };

    // Retry logic for production reliability 
    string javaCode = string.Empty;
    int maxRetries = 3;
   
    for (int attempt = 1; attempt <= maxRetries; attempt++)
    {
        try
        {
            var functionResult = await kernel.InvokePromptAsync(
                $"{systemPrompt}\n\n{prompt}",
                new KernelArguments(executionSettings));
           
            javaCode = functionResult.GetValue<string>() ?? string.Empty;
            break; // Success
        }
        catch (Exception ex) when (attempt < maxRetries &&
            (ex.Message.Contains("content_filter") || ex.Message.Contains("timeout")))
        {
            await Task.Delay(retryDelay);
            retryDelay *= 2; // Exponential backoff
        }
    }
   
    return new JavaFile
    {
        FileName = $"{GetClassName(javaCode)}.java",
        Content = ExtractJavaCode(javaCode),
        ClassName = GetClassName(javaCode),
        PackageName = GetPackageName(javaCode),
        OriginalCobolFileName = cobolFile.FileName
    };
}
```

A key engineering feature is content sanitization, which automatically cleans language and international text to avoid triggering Azure OpenAI’s content filtering. The system also includes a retry mechanism for failed requests and implements exponential backoff in cases of timeouts or content filter violations.

The **JavaConverterAgent** performs code extraction by intelligently parsing AI-generated Java from markdown blocks. It also generates modern, microservice-ready Quarkus code with proper annotations. It focuses on transforming legacy COBOL business logic into cloud-native Java while preserving functionality and applying modern enterprise design patterns.

To enable agent communication, we need to ensure that the orchestrator manages each sequence correctly. We follow this simplified approach:

```
// Discover COBOL files and copybooks
var cobolFiles = fileHelper.FindCobolFiles();
var copybooks = fileHelper.FindCopybooks();

// 1. Analyze COBOL files for structure and logic
var cobolAnalyses = await _cobolAnalyzerAgent.AnalyzeCobolFilesAsync(cobolFiles);

// 2. Map dependencies (program-to-copybook, reverse, and more)
var dependencyMap = await _dependencyMapperAgent.AnalyzeDependenciesAsync(cobolFiles, cobolAnalyses);

// 3. Convert COBOL programs to Java (using analysis and dependency context)
foreach (var analysis in cobolAnalyses)
{
    var javaClass = await _javaConverterAgent.ConvertCobolToJavaAsync(analysis, dependencyMap);
    fileHelper.SaveJavaClass(javaClass);
}

// 4. Generate reports and diagrams based on dependency analysis
reportGenerator.CreateMigrationReport(dependencyMap, cobolAnalyses);
```

Each agent returns structured outputs (e.g., COBOLAnalysis, DependencyMap) that serve as inputs for the next agent in the pipeline—enabling a clean, testable, and extensible workflow.

The following diagram shows the end-to-end flow of how the framework operates:

[![Image 4: camf flow image](https://devblogs.microsoft.com/all-things-azure/wp-content/uploads/sites/83/2025/07/camf_flow-286x300.png)](https://devblogs.microsoft.com/all-things-azure/wp-content/uploads/sites/83/2025/07/camf_flow.png)

Running the migration tool produces a dependency diagram, a full chat log of all agent conversations, the generated Java code, and conversion metrics.

Since the COBOL code was generously donated by Bankdata, we cannot publish a detailed report due to its sensitive nature. We’re deeply grateful to Bankdata for their contribution—without their code, building this tool wouldn’t have been possible.

We hope this framework will help modernize and document COBOL code across a variety of legacy systems.

There’s no one-size-fits-all approach to COBOL modernization—which is why you can dive into the source at [aka.ms/cobol](http://aka.ms/cobol) and customize each agent’s persona to fit your specific use case.

We see this not just as a framework for code migration—but as a foundation for rethinking how we approach legacy systems in the age of AI.

This is just the beginning. Whether you’re deep in COBOL or working with another legacy stack, we hope this gives you the tools—and the freedom—to build, break, and modernize on your own terms.

Project Team: [Julia Kordick (MSFT)](https://www.linkedin.com/in/julia-kordick/), [Gustav Kaleta (MSFT)](https://www.linkedin.com/in/gustav-kaleta-7a18661a/), [Omar Alhajj (Bankdata)](https://www.linkedin.com/in/omar-alhajj/), [Michael Munch (Bankdata)](https://www.linkedin.com/in/michael-munch-156298100/), [Morten Lilbæk Pedersen (Bankdata)](https://www.linkedin.com/in/morten-lilb%C3%A6k-pedersen/), [Michael Lind Mortensen (Bankdata)](https://www.linkedin.com/in/illio/)

Category

Author
------

![Image 5: jkordick](https://devblogs.microsoft.com/all-things-azure/wp-content/uploads/sites/83/2025/07/out-0-1-2-96x96.webp)

Software Global Black Belt

![Image 6: gkaleta](https://devblogs.microsoft.com/all-things-azure/wp-content/uploads/sites/83/2025/07/7D926726-80EB-42B5-8407-D4AFBE73EB93-96x96.jpeg)