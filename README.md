# Agentic RAG — LLM Zoomcamp Homework 1

Homework 1 of the [LLM Zoomcamp](https://github.com/DataTalksClub/llm-zoomcamp/) by DataTalksClub. Builds a RAG system from scratch over the course lesson pages, then turns it into an agent with function calling.

## What it does

- Fetches course lesson pages from GitHub using `gitsource`
- Indexes them with `minsearch` for full-text search
- Builds a RAG pipeline that retrieves relevant lessons and answers questions
- Chunks long lesson pages for more precise retrieval
- Turns the RAG into an agent that decides when and what to search using a `search` tool

## Project structure

```
.
├── hw01_agentic_rag.ipynb          # Main homework notebook
├── rag_helper_hw.py                # RAGBase class adapted for lesson content
├── homework.md                     # Homework instructions and questions
├── learning_code/
│   ├── 1_agentic_rag_notebook_Part1.ipynb
│   ├── 1_agentic_rag_notebook_Part2.ipynb
│   ├── ingest.py                   # FAQ data loading and index building
│   ├── rag_helper.py               # RAGBase class for FAQ schema
│   └── faq.db                      # SQLite FAQ database
└── pyproject.toml
```

## Setup

Requires Python 3.11+ and [uv](https://github.com/astral-sh/uv).

```bash
git clone <this-repo>
cd llm-zoomcamp-hw-01-agentic-rag
uv sync
```

Install extra dependencies:

```bash
uv add gitsource toyaikit
```

Set your LLM API key (Groq, OpenAI, or any compatible provider):

```bash
export GROQ_API_KEY="your-key-here"
# or
export OPENAI_API_KEY="your-key-here"
```

## Usage

Open and run `hw01_agentic_rag.ipynb` top to bottom. The notebook covers:

1. Fetching lesson pages from the course repo at commit `8c1834d`
2. Indexing with `minsearch` (`content` as text field, `filename` as keyword field)
3. Plain RAG over the full lesson pages
4. Chunked RAG (`size=2000`, `step=1000`) for more precise retrieval
5. Agentic loop with a `search` tool — the model decides when to search

## Notes on LLM providers

The homework recommends `gpt-5.4-mini` (OpenAI). If you're using a free provider, be aware of compatibility constraints:

- **Groq** (`llama-3.3-70b-versatile`) — works with `/chat/completions`, not `/responses`
- **toyaikit's `OpenAIResponsesRunner`** — requires a provider that supports the OpenAI `/responses` endpoint (currently only OpenAI itself)
- **Alternatives** — LangChain, LlamaIndex, PydanticAI, or a hand-written loop all work fine with Groq and other free providers

## Homework answers

| Question | Answer |
|---|---|
| Q1. Number of lesson pages | 72 |
| Q2. First search result filename | `01-agentic-rag/lessons/14-agentic-loop.md` |
| Q3. Input tokens (full pages) | ~7000 |
| Q4. Number of chunks | 295 |
| Q5. Token reduction with chunking | ~3× fewer |
| Q6. Agent search tool calls | ~4 |
