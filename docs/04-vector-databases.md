# Lesson 4 — Vector Databases

Welcome to **Lesson 4**.

In **Lesson 3**, we learned that text can be converted into **embeddings** (vectors).

Now comes the obvious question:

> **Where do we store millions of embeddings, and how do we search them efficiently?**

That's exactly what a **Vector Database** is designed to do.

---

# Learning Objectives

By the end of this lesson, you will understand:

* What a Vector Database is
* Why traditional databases are not enough
* How similarity search works
* What metadata is
* The Vector Database workflow
* Popular Vector Databases
* How a Vector Database fits into a RAG pipeline

---

# 1. The Problem

Imagine your company has:

* 2 million documents
* 20 million document chunks
* Each chunk converted into a **1536-dimensional embedding**

Now a user asks:

> "How do I reset my password?"

You create an embedding for the question.

Now you must compare it against **20 million vectors**.

Without a specialized system, this would be extremely slow.

This is why Vector Databases exist.

---

# 2. What is a Vector Database?

A Vector Database is a database optimized to store and search **vectors** instead of traditional rows of text.

Traditional database:

| ID | Name  | Department |
| -: | ----- | ---------- |
|  1 | Alice | HR         |
|  2 | Bob   | IT         |

Vector database:

| ID | Embedding          | Metadata |
| -: | ------------------ | -------- |
|  1 | [0.12, -0.44, ...] | page=12  |
|  2 | [0.91, 0.18, ...]  | page=44  |

Notice that the primary searchable field is the **embedding vector**, not plain text.

---

# 3. Traditional Database vs Vector Database

Suppose your SQL database contains:

```text
Password Recovery Guide
```

A user searches:

```text
How do I reset my password?
```

Traditional SQL query:

```sql
SELECT *
FROM documents
WHERE title LIKE '%reset password%'
```

Result:

❌ Nothing found.

The words **reset** and **recovery** are different.

---

A Vector Database works differently.

It compares the **meaning** of the query against stored vectors.

```text
Reset Password

↓

Embedding

↓

Nearest Vector

↓

Password Recovery Guide
```

No exact keyword match is required.

---

# 4. The Basic Workflow

A Vector Database stores embeddings that have already been generated.

```text
PDF

↓

Chunk Text

↓

Embedding Model

↓

Vector

↓

Vector Database
```

Later:

```text
Question

↓

Embedding Model

↓

Query Vector

↓

Vector Database

↓

Most Similar Chunks
```

Notice that **the embedding model creates vectors**, while **the vector database stores and searches them**. These are separate responsibilities.

---

# 5. What Does the Database Actually Store?

A record typically contains:

```json
{
    "id": "doc_145",

    "embedding": [0.14, -0.88, 0.27, ...],

    "text":
    "Click Forgot Password to reset your password.",

    "metadata":
    {
        "page": 18,
        "source": "IT_Manual.pdf",
        "department": "IT"
    }
}
```

The embedding is used for similarity search.

The text is returned to the application after retrieval.

Metadata enables filtering.

---

# 6. Metadata

Metadata is additional information about a document.

Example:

```text
Employee Handbook

Metadata

Department: HR

Language: English

Year: 2025

Page: 82
```

Now imagine the user asks:

> Show only HR policies.

The Vector Database can first filter by:

```text
Department = HR
```

and then perform semantic search only within those documents.

This is much faster and more precise than searching the entire collection.

---

# 7. Similarity Search

This is the core feature of a Vector Database.

Suppose your query embedding is represented conceptually like this:

```text
Query

●
```

Stored embeddings:

```text
Vehicle Cluster

Car ●

Truck ●

Bus ●



Fruit Cluster

Apple ●

Banana ●
```

The database searches for the nearest vectors.

Result:

```text
Query

↓

Truck

↓

Car

↓

Bus
```

The actual mathematics (such as cosine similarity and Euclidean distance) will be explored in more detail when we discuss retrieval algorithms, but the key idea is that **nearby vectors represent similar meanings**.

---

# 8. Why Not Compare Every Vector?

Imagine:

* 50 million vectors
* Each vector has 1536 numbers

A naive search would compare the query vector against every stored vector.

```text
Query

↓

Compare

↓

Vector 1

↓

Vector 2

↓

Vector 3

↓

...

↓

Vector 50,000,000
```

This is called **brute-force search**.

It is accurate but becomes impractical as the dataset grows because every query must examine every stored vector.

---

# 9. Approximate Nearest Neighbor (ANN)

Modern vector databases solve this with **Approximate Nearest Neighbor (ANN)** search.

Instead of checking every vector, they organize vectors into efficient data structures so they can quickly find vectors that are *very likely* to be the closest.

Think of it like this:

Finding one house in a city.

Brute force:

```text
House 1

House 2

House 3

...

House 2,000,000
```

ANN:

```text
City

↓

District

↓

Street

↓

House
```

You don't inspect every house—you navigate toward the right neighborhood first.

The trade-off is important:

| Method      |     Speed |                                        Accuracy |
| ----------- | --------: | ----------------------------------------------: |
| Brute Force |      Slow |                                           Exact |
| ANN         | Very Fast | Approximately Exact (typically extremely close) |

For most AI applications, this tiny approximation is well worth the enormous speed gain.

---

# 10. Popular Vector Databases

Some of the most widely used options are:

| Database | Description                                             |
| -------- | ------------------------------------------------------- |
| Chroma   | Lightweight and great for learning or local development |
| Qdrant   | High-performance open-source vector database            |
| Pinecone | Fully managed cloud service                             |
| Weaviate | Open-source with hybrid search capabilities             |
| Milvus   | Designed for very large-scale deployments               |
| pgvector | PostgreSQL extension that adds vector search support    |

Each database provides APIs to insert vectors, search for similar vectors, and manage metadata.

---

# 11. Where the Vector Database Fits in RAG

Let's put everything together.

```text
                Documents
                    │
                    ▼
             Split into Chunks
                    │
                    ▼
           Embedding Model
                    │
                    ▼
            Vector Database
                    ▲
                    │
         User Question
                    │
                    ▼
           Embedding Model
                    │
                    ▼
         Similarity Search
                    │
                    ▼
      Relevant Document Chunks
                    │
                    ▼
                  LLM
                    │
                    ▼
              Final Answer
```

Notice the responsibilities:

* **Embedding Model** → Converts text into vectors.
* **Vector Database** → Stores vectors and retrieves the most similar ones.
* **LLM** → Reads the retrieved text and generates the final answer.

Each component has a distinct role.

---

# Key Takeaways

* A **Vector Database** stores embeddings rather than relying on keyword indexes.
* It performs **semantic similarity search**, not exact keyword matching.
* The **embedding model** creates vectors; the **vector database** stores and searches them.
* Metadata enables filtered searches, such as restricting results by department or document type.
* Modern vector databases use **Approximate Nearest Neighbor (ANN)** algorithms to make similarity search fast at scale.
* Vector databases are a fundamental building block of modern RAG systems.

---

# Quiz

1. What is the primary difference between a traditional SQL database and a vector database?
2. Why is keyword search often insufficient for AI applications?
3. What role does metadata play in a vector database?
4. Why don't vector databases compare every stored vector for each query?
5. What is Approximate Nearest Neighbor (ANN) search?
6. In a RAG pipeline, which component creates embeddings, which stores them, and which generates the final answer?

---

# Exercise

Imagine you're building an AI assistant for a university.

The university has these documents:

* Student Handbook
* Library Rules
* Scholarship Guide
* Course Registration Manual
* IT Support Manual

For each question below, identify:

1. Which document(s) should ideally be retrieved?
2. Why might keyword search fail?
3. Why would a vector database succeed?

Example questions:

* "How do I recover my student account?"
* "When can I sign up for classes?"
* "What financial aid is available?"
* "Can I borrow books for a month?"

---

## What's Next?

In **Lesson 5 — Retrieval-Augmented Generation (RAG)**, we'll connect everything we've learned:

* Lesson 2: **LLMs generate text**
* Lesson 3: **Embeddings capture meaning**
* Lesson 4: **Vector databases retrieve relevant information**

Now we'll combine these components into a complete RAG pipeline that allows an LLM to answer questions using your own documents. This is the architecture behind many modern enterprise AI assistants.
