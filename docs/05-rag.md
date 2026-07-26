# Lesson 5 — Retrieval-Augmented Generation (RAG)

## Learning Objectives

By the end of this lesson, you will understand:

* What Retrieval-Augmented Generation (RAG) is
* Why RAG is needed
* The complete RAG architecture
* Every component in a RAG pipeline
* The document indexing process
* The query process
* Different types of RAG
* Advantages and limitations of RAG
* Best practices for building a RAG application

---

# 1. What is Retrieval-Augmented Generation?

Let's break the name into two parts.

**Retrieval**

Retrieve the most relevant information from an external knowledge source.

**Generation**

Use an LLM to generate an answer based on the retrieved information.

Together:

> **RAG = Retrieve relevant information first, then let the LLM generate an answer using that information.**

Instead of relying only on what the model learned during training, we provide it with fresh, private, or domain-specific knowledge at the time of the request.

---

# 2. Why Do We Need RAG?

Imagine you work for a company.

The company has:

* Employee Handbook
* HR Policies
* IT Manual
* Security Guidelines
* Internal Wiki

A new employee asks:

> "How many vacation days do I get?"

A standalone LLM cannot reliably answer because:

* The handbook is private.
* The policy may have changed recently.
* The information wasn't part of the model's training.

Without RAG:

```text
User
 │
 ▼
LLM
 │
 ▼
"I don't know"
or
Hallucinated Answer
```

With RAG:

```text
User
 │
 ▼
Retrieve Handbook
 │
 ▼
LLM
 │
 ▼
Correct Answer
```

This is the key benefit of RAG: **grounding** the model's response in real documents.

---

# 3. The Big Picture

A RAG system has two major phases:

```text
          INDEXING (Offline)

Documents
     │
     ▼
Chunking
     │
     ▼
Embeddings
     │
     ▼
Vector Database


          QUERYING (Online)

User Question
     │
     ▼
Embedding
     │
     ▼
Vector Search
     │
     ▼
Relevant Chunks
     │
     ▼
LLM
     │
     ▼
Answer
```

Notice something important:

**Documents are embedded only once**, during indexing.

Each user question is embedded at query time.

---

# 4. RAG Has Two Pipelines

Many beginners think RAG is one process.

Actually, there are **two separate pipelines**.

## Pipeline 1 — Indexing

This prepares your knowledge base.

```text
PDF
 │
 ▼
Extract Text
 │
 ▼
Split into Chunks
 │
 ▼
Generate Embeddings
 │
 ▼
Store in Vector Database
```

This might happen:

* once a day
* when a document changes
* when new files are uploaded

---

## Pipeline 2 — Query

This happens every time a user asks a question.

```text
Question
 │
 ▼
Embedding
 │
 ▼
Similarity Search
 │
 ▼
Top Matching Chunks
 │
 ▼
Prompt Construction
 │
 ▼
LLM
 │
 ▼
Answer
```

---

# 5. Step-by-Step RAG Workflow

Let's imagine we have an IT manual.

The document contains:

```text
Password Reset Procedure

1. Open the employee portal.
2. Click Forgot Password.
3. Verify your identity.
4. Create a new password.
```

---

## Step 1 — Load Documents

```text
IT_Manual.pdf
```

---

## Step 2 — Extract Text

```text
Password Reset Procedure

1. Open the employee portal...
```

---

## Step 3 — Chunking

Large documents are split into smaller pieces.

Example:

```text
Chunk 1

Password Reset Procedure

Open the employee portal...
```

```text
Chunk 2

Verify your identity...
```

```text
Chunk 3

Create a strong password...
```

We'll discuss chunking strategies in more detail later because they have a major impact on retrieval quality.

---

## Step 4 — Generate Embeddings

Each chunk becomes a vector.

```text
Chunk 1
     │
     ▼
Embedding

[0.18, -0.33, ...]
```

---

## Step 5 — Store in Vector Database

Now the vector database stores something like:

| Chunk   | Embedding | Metadata |
| ------- | --------- | -------- |
| Chunk 1 | Vector    | Page 12  |
| Chunk 2 | Vector    | Page 13  |
| Chunk 3 | Vector    | Page 14  |

---

## Step 6 — User Asks a Question

```text
How do I recover my password?
```

---

## Step 7 — Embed the Question

```text
Question

↓

Embedding
```

Now both the document chunks and the user's question are represented in the same vector space.

---

## Step 8 — Similarity Search

The vector database compares the question vector against stored vectors.

Result:

```text
Top 3 Chunks

Chunk 1

Chunk 2

Chunk 3
```

These chunks are semantically related to the question.

---

## Step 9 — Prompt Construction

This is one of the most important steps.

The application builds a prompt for the LLM.

Example:

```text
System:

Answer only using the provided context.

Context:

Password Reset Procedure

1. Open the employee portal.
2. Click Forgot Password.
3. Verify your identity.
4. Create a new password.

Question:

How do I recover my password?
```

Notice that the LLM is **not searching** the database. It simply receives the retrieved context as part of the prompt.

---

## Step 10 — LLM Generates the Answer

The LLM reads:

* the instructions,
* the retrieved context,
* the user's question,

and produces:

> To recover your password, open the employee portal, click **Forgot Password**, verify your identity, and create a new password.

This answer is grounded in the retrieved document.

---

# 6. Complete Architecture

```text
                 OFFLINE

        Documents (PDF, DOCX, TXT)
                    │
                    ▼
             Load Documents
                    │
                    ▼
              Split into Chunks
                    │
                    ▼
           Generate Embeddings
                    │
                    ▼
           Store in Vector DB


                 ONLINE

              User Question
                    │
                    ▼
          Generate Embedding
                    │
                    ▼
        Search Vector Database
                    │
                    ▼
        Retrieve Top-K Chunks
                    │
                    ▼
         Build Prompt with Context
                    │
                    ▼
                   LLM
                    │
                    ▼
             Final Response
```

This diagram captures the entire lifecycle of a basic RAG system.

---

# 7. Why Not Send the Whole PDF?

Suppose you have:

* 500-page manual
* 2,000-page legal contract
* 10,000-page documentation

Sending the entire document to the LLM would be:

* expensive,
* slow,
* limited by the model's context window.

Instead, RAG retrieves only the **most relevant chunks**.

---

# 8. Benefits of RAG

RAG offers several advantages:

* Uses private documents without retraining the LLM.
* Incorporates updated information immediately after re-indexing.
* Reduces hallucinations by grounding responses in retrieved content.
* Keeps prompts smaller by retrieving only relevant chunks.
* Enables citation of document sources if metadata is included.

---

# 9. Limitations of RAG

RAG is powerful, but it is not perfect.

Challenges include:

* Poor chunking can split important information.
* Weak embeddings may retrieve irrelevant chunks.
* If the correct chunk is not retrieved, the LLM cannot answer accurately.
* Very large knowledge bases require efficient indexing and retrieval strategies.
* Retrieved context may exceed the model's context window if too much is included.

This is why the quality of retrieval is just as important as the quality of the LLM.

---

# 10. Types of RAG

As systems become more advanced, the retrieval process can be enhanced.

| Type           | Description                                                                              |
| -------------- | ---------------------------------------------------------------------------------------- |
| Basic RAG      | Retrieve similar chunks, then generate an answer.                                        |
| Hybrid RAG     | Combine semantic search with keyword search.                                             |
| Multi-Step RAG | Perform multiple retrieval rounds before answering.                                      |
| Graph RAG      | Retrieve information using relationships in a knowledge graph.                           |
| Agentic RAG    | An AI agent decides when and how to retrieve information, possibly using multiple tools. |

We'll explore these advanced techniques in **Lesson 8**.

---

# 11. Best Practices

When building a RAG system:

* Choose an embedding model suited to your domain.
* Split documents into meaningful chunks.
* Preserve metadata such as page numbers and document names.
* Retrieve a reasonable number of chunks (often called **Top-K**).
* Give the LLM clear instructions to answer using only the provided context.
* Include citations when possible.

---

# Summary

Let's connect everything you've learned across Lessons 2–5.

```text
User Question
      │
      ▼
Embedding Model
      │
      ▼
Question Vector
      │
      ▼
Vector Database
      │
      ▼
Retrieve Top-K Chunks
      │
      ▼
Prompt Builder
      │
      ▼
LLM
      │
      ▼
Grounded Answer
```

Each component has a clear responsibility:

| Component       | Responsibility                                     |
| --------------- | -------------------------------------------------- |
| Embedding Model | Convert text into vectors                          |
| Vector Database | Store and retrieve similar vectors                 |
| Prompt Builder  | Combine retrieved context with the user's question |
| LLM             | Generate a natural-language answer                 |

---

# Key Takeaways

* **RAG** combines retrieval and generation.
* The system has two pipelines: **Indexing** and **Querying**.
* Documents are embedded once; questions are embedded for each query.
* Vector databases retrieve relevant chunks using semantic similarity.
* The LLM answers based on the retrieved context, rather than relying solely on its training.
* High-quality retrieval is essential for high-quality answers.

---

# Quiz

1. What does **Retrieval-Augmented Generation** mean?
2. Why are there two pipelines in a RAG system?
3. Why are documents chunked before creating embeddings?
4. What is the role of the vector database during a user query?
5. Why doesn't the LLM directly search the database?
6. What happens if the correct document chunk is never retrieved?
7. Why is RAG generally preferred over retraining an LLM whenever company documents change?

---

# Exercise

You're building a RAG system for a hospital with these documents:

* Emergency Procedures
* Medication Guide
* Patient Admission Policy
* Surgical Safety Checklist
* Infection Control Manual

A doctor asks:

> "What should I do before performing surgery?"

Describe the complete RAG pipeline:

1. What happens during the indexing phase?
2. What happens after the doctor asks the question?
3. Which components are involved at each step?
4. How does the final answer reach the doctor?

Draw the workflow yourself before looking back at the lesson. If you can recreate the pipeline from memory, you've understood the core architecture behind modern enterprise AI assistants.

---

## Looking Ahead: Lesson 6 — Prompt Engineering

So far, we've built the **data pipeline**:

* LLMs generate text.
* Embeddings represent meaning.
* Vector databases retrieve relevant information.
* RAG brings these pieces together.

Next, we'll learn how to communicate effectively with the LLM itself. In **Lesson 6**, we'll explore prompt engineering, including system prompts, user prompts, few-shot prompting, structured outputs, and techniques for making LLM responses more reliable and consistent.
