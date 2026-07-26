# Lesson 8 — Advanced RAG

However, if you deploy a system in a real company, you'll quickly discover that **basic RAG is often not enough**.

Enterprise systems need to handle:

* Millions of documents
* Ambiguous user questions
* Multiple document types
* Outdated information
* Different departments
* Better accuracy
* Faster retrieval
* Lower cost

This is where **Advanced RAG** comes in.

## Learning Objectives

By the end of this lesson, you will understand:

* Why Basic RAG has limitations
* Hybrid Search
* Query Expansion
* Query Rewriting
* Re-ranking
* Context Compression
* Parent-Child Retrieval
* Multi-Query Retrieval
* Self-RAG
* Agentic RAG
* Graph RAG
* Best practices for production systems

---

# 1. Why Basic RAG Isn't Enough

Let's review the Basic RAG pipeline.

```text
User Question
      │
      ▼
Embedding
      │
      ▼
Vector Database
      │
      ▼
Top-K Chunks
      │
      ▼
LLM
      │
      ▼
Answer
```

This works well for many cases.

But imagine a company with:

* 10 million documents
* 500 million chunks
* 30 departments
* Documents in multiple languages

A simple semantic search may retrieve irrelevant chunks or miss important information.

---

# Common Problems

### Problem 1 — Vocabulary Mismatch

Document:

```text
Vacation Policy
```

User asks:

```text
Annual Leave Rules
```

The meanings are similar, but retrieval quality depends on the embedding model and the indexed content.

---

### Problem 2 — Missing Context

Question:

> What is the maximum amount?

Without context:

* vacation amount?
* reimbursement amount?
* loan amount?

The retriever needs additional information to identify the correct documents.

---

### Problem 3 — Wrong Ranking

Top retrieved chunks:

```text
Chunk 1
Password Complexity

Chunk 2
Password Reset

Chunk 3
VPN Access
```

The answer may actually require **Chunk 2**, even if **Chunk 1** scored slightly higher.

---

# 2. Hybrid Search

Basic RAG uses **semantic search**.

Hybrid Search combines:

* Semantic Search (Embeddings)
* Keyword Search (e.g., BM25)

```text
                 User Question
                      │
          ┌───────────┴───────────┐
          ▼                       ▼
 Semantic Search          Keyword Search
          │                       │
          └───────────┬───────────┘
                      ▼
                Merge Results
                      │
                      ▼
                    LLM
```

---

## Why Hybrid Search?

Suppose the user asks:

> Error Code 0x80070005

Keyword search excels at exact identifiers like error codes.

Embedding search helps with conceptual questions.

Combining both often improves retrieval quality.

---

# 3. Query Expansion

Sometimes the user's wording is too limited.

Example:

User:

```text
Vacation
```

Expanded query:

```text
Vacation OR Annual Leave OR Paid Time Off (PTO)
```

This increases the chances of retrieving relevant documents.

Expansion can be done using synonym dictionaries or an LLM.

---

# 4. Query Rewriting

Sometimes users ask unclear questions.

Example:

```text
How much can I take?
```

The system can rewrite it as:

```text
How many annual vacation days can an employee take?
```

A clearer query often produces better retrieval results.

---

# 5. Multi-Query Retrieval

Instead of searching once, generate several related queries.

Original:

```text
How do I recover my password?
```

Generated queries:

```text
Reset password

Forgot password

Recover account

Password recovery
```

Each query searches independently.

The results are merged before being passed to the LLM.

```text
Question
     │
     ▼
Generate 4 Queries
     │
     ▼
4 Searches
     │
     ▼
Merge Results
     │
     ▼
LLM
```

---

# 6. Re-ranking

The vector database returns candidate chunks.

A second model evaluates them more carefully.

```text
Vector Search

↓

Top 20 Chunks

↓

Re-ranker

↓

Top 5 Chunks

↓

LLM
```

The first stage optimizes for speed.

The second stage optimizes for precision.

This is common in production systems.

---

# Example

Question:

> What is the maternity leave policy?

Vector search:

| Rank | Chunk             |
| ---- | ----------------- |
| 1    | Employee Benefits |
| 2    | Leave Policies    |
| 3    | Maternity Leave   |
| 4    | Payroll           |

A re-ranker may reorder them:

| Rank | Chunk             |
| ---- | ----------------- |
| 1    | Maternity Leave   |
| 2    | Leave Policies    |
| 3    | Employee Benefits |

The LLM now receives more relevant context.

---

# 7. Context Compression

Sometimes retrieval returns too much text.

Instead of sending everything:

```text
Chunk 1

500 words

Chunk 2

700 words

Chunk 3

900 words
```

Compress them:

```text
Important sentence

Important paragraph

Important table
```

This reduces:

* token usage
* latency
* cost

while keeping the most relevant information.

---

# 8. Parent–Child Retrieval

Documents are often chunked into small pieces.

Problem:

A small chunk may lack context.

Example:

Child chunk:

```text
Employees receive 20 days...
```

Missing:

> 20 days of **what**?

Solution:

```text
Search Child

↓

Retrieve Parent Section

↓

LLM
```

Search uses the fine-grained child chunk, but the larger parent section is provided to the model.

---

# 9. Metadata Filtering

Suppose the company has:

```text
HR

IT

Finance

Legal
```

A user asks:

> Vacation policy

Instead of searching every department:

```text
Department = HR
```

Then search only HR vectors.

This improves both speed and accuracy.

---

# 10. Self-RAG

Self-RAG adds self-evaluation.

```text
Question

↓

Retrieve

↓

LLM

↓

"Do I have enough information?"

↓

Yes → Answer

No → Retrieve Again
```

The model can decide whether additional retrieval is needed before responding.

---

# 11. Agentic RAG

Instead of a fixed pipeline, an AI agent chooses which tools to use.

```text
Question
     │
     ▼
AI Agent
     │
 ┌───┼─────────────┐
 ▼   ▼             ▼
RAG  SQL DB     Web Search
 │    │             │
 └────┴─────────────┘
          │
          ▼
         LLM
```

Example:

> Show my leave balance.

The agent might:

* query the HR database,
* retrieve policy documents,
* combine both,
* then generate an answer.

---

# 12. Graph RAG

Relationships matter.

Example:

```text
Alice

works for

Engineering

managed by

Bob

reports to

CEO
```

A graph database can retrieve connected entities and relationships, which are then provided to the LLM.

Graph RAG is particularly useful for domains with rich relationships, such as fraud detection, scientific knowledge, and organizational structures.

---

# 13. Comparing RAG Techniques

| Technique              | Purpose                      | Benefit                       |
| ---------------------- | ---------------------------- | ----------------------------- |
| Basic RAG              | Semantic retrieval           | Simple and effective          |
| Hybrid Search          | Keyword + semantic           | Better recall                 |
| Query Expansion        | Add related terms            | Broader retrieval             |
| Query Rewriting        | Clarify the query            | More precise retrieval        |
| Multi-Query            | Search multiple phrasings    | Higher recall                 |
| Re-ranking             | Improve candidate ordering   | Better precision              |
| Context Compression    | Reduce retrieved text        | Lower cost and latency        |
| Parent–Child Retrieval | Preserve context             | More complete answers         |
| Metadata Filtering     | Restrict search scope        | Faster, more relevant results |
| Self-RAG               | Evaluate retrieval quality   | Adaptive retrieval            |
| Agentic RAG            | Use multiple tools           | Flexible workflows            |
| Graph RAG              | Retrieve connected knowledge | Rich relationship reasoning   |

---

# A Production-Ready Architecture

```text
                    User Question
                          │
                          ▼
                  Query Rewriting
                          │
                          ▼
                Multi-Query Generator
                          │
                          ▼
          +-------------------------------+
          |                               |
          ▼                               ▼
  Semantic Search                 Keyword Search
          │                               │
          +---------------+---------------+
                          ▼
                     Merge Results
                          │
                          ▼
                      Re-ranker
                          │
                          ▼
                Context Compression
                          │
                          ▼
                   Prompt Builder
                          │
                          ▼
                         LLM
                          │
                          ▼
                    Final Response
```

Not every application needs all of these components. Choose techniques based on your requirements, data, and performance goals.

---

# Best Practices

For production RAG systems:

* Use a high-quality embedding model.
* Choose chunk sizes appropriate for your documents.
* Preserve metadata for filtering and citations.
* Consider hybrid search for technical or code-heavy content.
* Use re-ranking when precision matters.
* Compress context before sending it to the LLM.
* Monitor retrieval quality as well as answer quality.
* Evaluate your system with realistic user questions, not just ideal examples.

---

# Key Takeaways

* Basic RAG is a strong starting point but may not scale to complex enterprise needs.
* Hybrid search combines the strengths of keyword and semantic retrieval.
* Query rewriting and expansion can improve retrieval before searching.
* Re-ranking improves the quality of retrieved context.
* Context compression reduces cost without necessarily sacrificing answer quality.
* Agentic and Graph RAG extend retrieval beyond a single vector database.
* The best production systems often combine several of these techniques rather than relying on only one.

---

# Quiz

1. Why might Hybrid Search outperform semantic search alone?
2. What is the difference between Query Expansion and Query Rewriting?
3. Why is a re-ranker used after vector search?
4. How does Parent–Child Retrieval preserve context?
5. When would Metadata Filtering be especially useful?
6. What makes Agentic RAG different from a traditional RAG pipeline?
7. Why is Graph RAG valuable for highly connected data?

---

## Looking Ahead: Lesson 9 — Deployment

So far, you've learned how to **design and build** a RAG system. In the next lesson, we'll shift our focus to **deploying** it as a real application.

We'll cover:

* Structuring the application for production.
* Building a REST API with FastAPI.
* Managing configuration and secrets.
* Containerizing the application with Docker.
* Logging, monitoring, and error handling.
* Preparing your RAG system for cloud deployment.

By the end of Lesson 9, you'll understand how to move from a development prototype to a deployable, maintainable RAG service.
