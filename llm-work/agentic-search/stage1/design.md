# Stage 1: Agentic Search Prototype Design

## Goal
Implement a simple agentic search prototype to verify LLM's ability to autonomously call tools to solve problems.

## Core Components

### 1. Tools Definition (tools/)
- `keyword_search.py` - Keyword search
  - Search file names and content
  - Parameters: `query` (search term), `max_results` (default 10)
- `vector_search.py` - Vector search
  - Semantic retrieval based on existing `embeddings.sqlite`
  - Parameters: `query` (query text), `top_k` (default 5), `chunk_type` (multiple allowed)
- `text_reader.py` - Text range reading
  - Read specified file's line range
  - Parameters: `file_path` (file path), `start_line` (start line), `end_line` (end line)

### 2. Core Agent (core/)
- `agent.py` - Main agent logic
  - Maintain conversation history
  - Tool selection and calling loop
  - Answer generation and summarization
  - Limits: Max 10 tool calls, total token < 60k

### 3. Prototype Entry (stage1/)
- `prototype.py` - Prototype entry
  - Hardcoded test queries
  - Or accept command line argument `--query "xxx"`
  - Output complete reasoning process and final answer

## Workflow

```
User Query → Agent Analysis → Tool Selection → Tool Execution → Result Evaluation
          ↓
        Continue Search OR Generate Answer
          ↓
        Reach Limit or Complete → Return Answer
```

## Tool Calling Loop Logic

1. **Initial Analysis**: Based on user question, determine what information is needed
2. **Tool Selection**:
   - Find specific information → Vector search first, then text reading
   - Find files → Keyword search
   - Range queries → Vector search + keyword search
3. **Evaluate Feedback**: Based on tool return, decide next step
4. **Generate Answer**: Or continue searching

## Constraints

- **Tool call count**: Max 10 times
- **Token limit**: All context < 60k tokens
- **Text reading**: Max 200 lines per read
- **Top-k limit**: Vector search top_k ≤ 10

## Directory Structure

```
stage1/
├── prototype.py          # Prototype entry
├── tools/
│   ├── keyword_search.py
│   ├── vector_search.py
│   └── text_reader.py
└── core/
    └── agent.py
```

## Example Queries (Hardcoded Tests)

1. "Find all articles about LLM embeddings"
2. "What frontend technology articles are there in June 2024?"
3. "What are the best practices related to Embeddings?"

## Tech Stack

- **No LangChain**: Avoid over-complication
- **Reuse existing code**:
  - `embedding_store.py` - SQLite vector queries
  - Existing Markdown parsing logic
- **Simple and direct**: Use Python dict/JSON to pass state

## Output Format

- Show parameters and result summary for each tool call
- Final answer + source citations (file path, line numbers)
- Tool call statistics: count, token consumption
