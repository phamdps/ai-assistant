## What we'll build

```
llm-rag-vector-db-study/
│
├── lessons/
│   ├── 01-introduction/
│   ├── 02-how-llms-work/
│   ├── 03-embeddings/
│   ├── 04-vector-databases/
│   ├── 05-rag/
│   ├── 06-prompt-engineering/
│   ├── 07-build-rag-system/
│   ├── 08-advanced-rag/
│   ├── 09-deployment/
│   └── 10-capstone/
│
├── datasets/
├── notebooks/
├── docs/
└── README.md
```

---

# What each lesson will contain

Each lesson will include:

```
lesson/
│
├── README.md
├── main.py
├── requirements.txt
├── .env.example
├── config.py
├── sample_data/
└── exercises/
```

Every lesson will be:

* Fully runnable
* Well commented
* Explained line by line
* Independent from the others (when practical)
* Incrementally more advanced

---

# Lesson 1 — Introduction to LLMs

**Goal**

Build your first OpenAI application.

You will learn:

* API connection
* Chat completion
* Message roles
* Temperature
* Basic prompt

Example:

```
User

↓

Python

↓

OpenAI API

↓

Response
```

Files:

```
01-introduction/
    README.md
    main.py
    config.py
```

---

# Lesson 2 — How LLMs Work

Build a tokenizer visualizer.

Features:

* Count tokens
* Show token IDs
* Estimate cost
* Context window calculator

You'll use:

* `tiktoken`

---

# Lesson 3 — Embeddings

Generate embeddings.

Features:

* Compare two sentences
* Compute cosine similarity
* Visualize vectors
* Semantic search demo

Libraries:

* NumPy
* OpenAI Embeddings

---

# Lesson 4 — Vector Database

Build your own document index.

Features:

* Load text
* Generate embeddings
* Store vectors
* Semantic search

Libraries:

* ChromaDB

---

# Lesson 5 — RAG

First complete RAG.

Pipeline:

```
Question

↓

Embedding

↓

Chroma

↓

Top Chunks

↓

GPT

↓

Answer
```

---

# Lesson 6 — Prompt Engineering

Experiment with prompts.

Compare:

* Zero-shot
* One-shot
* Few-shot
* System prompts
* JSON output
* Markdown output

The code will let you see how changing the prompt changes the model's response.

---

# Lesson 7 — Build a Complete RAG

A modular application.

```
loaders/

embeddings/

vectorstore/

retriever/

prompts/

llm/

chat.py
```

This resembles a production-ready architecture while remaining easy to understand.

---

# Lesson 8 — Advanced RAG

We'll implement:

* Multi-query retrieval
* Query rewriting
* Metadata filtering
* Re-ranking
* Context compression
* Hybrid retrieval (using available Python libraries)

You'll be able to compare retrieval strategies side by side.

---

# Lesson 9 — Deployment

We'll convert Lesson 7 into a service.

Features:

* FastAPI
* Swagger UI
* Docker
* Docker Compose
* Environment variables
* Logging
* Health check endpoint

You'll be able to start it with:

```bash
docker compose up
```

and access:

```
http://localhost:8000/docs
```

to test the API interactively.

---

# Lesson 10 — Capstone

This is the final project.

Features:

```
Upload PDFs

↓

Automatic indexing

↓

Vector DB

↓

Chat API

↓

Source citations

↓

Docker deployment
```

It will include:

* Modular architecture
* Logging
* Configuration
* Error handling
* Clean code
* GitHub-ready documentation
* Docker support

---

# Additional Features We'll Add

Across the lessons, we'll also cover:

* Unit tests with `pytest`
* Type hints
* Logging
* Configuration management
* Pydantic models
* Progress bars with `tqdm`
* Rich terminal output
* `.gitignore`
* GitHub Actions for basic CI
* Comprehensive README files
* Inline documentation

---

# Final Repository

By the end, your repository will look like this:

```
llm-rag-vector-db-study/
│
├── lessons/
│   ├── 01-introduction/
│   ├── 02-how-llms-work/
│   ├── 03-embeddings/
│   ├── 04-vector-databases/
│   ├── 05-rag/
│   ├── 06-prompt-engineering/
│   ├── 07-build-rag-system/
│   ├── 08-advanced-rag/
│   ├── 09-deployment/
│   └── 10-capstone/
│
├── datasets/
├── docs/
├── notebooks/
├── LICENSE
├── .gitignore
└── README.md
```

This won't just be a collection of examples—it will be a complete learning repository that demonstrates your progression from basic LLM usage to a production-inspired RAG application.

## How we'll proceed

I recommend building the exercises **one lesson at a time** rather than generating everything in one response. That allows us to:

1. Explain every line of code.
2. Run and test each project before moving on.
3. Improve the architecture as the course progresses.
4. Keep each lesson focused and easy to understand.

The result will be a polished, GitHub-quality repository instead of a large dump of code.
