# Lesson 7 — Build a RAG System

Rather than writing one large script, we'll build the application incrementally using the project structure we already created.


## Learning Objectives

By the end of this lesson, you will be able to:

* Build a complete RAG application from scratch.
* Load documents from multiple sources.
* Split documents into meaningful chunks.
* Generate embeddings.
* Store embeddings in a vector database.
* Perform semantic search.
* Build prompts using retrieved context.
* Generate answers using an LLM.
* Understand how every component interacts.
* Organize the code using a clean project architecture.

---

# What We Are Building

Our first application will be a **Chat with Your Documents** system.

Imagine a user uploads a PDF like:

```
Employee_Handbook.pdf
```

Then asks:

> How many vacation days do employees receive?

Our application should:

```
User
 │
 ▼
Ask Question
 │
 ▼
Search Documents
 │
 ▼
Retrieve Relevant Chunks
 │
 ▼
Send Context to LLM
 │
 ▼
Generate Answer
```

---

# Final Architecture

```text
                +----------------------+
                |      User            |
                +----------+-----------+
                           |
                           v
                +----------------------+
                |   User Question      |
                +----------+-----------+
                           |
                           v
                +----------------------+
                | Embedding Model       |
                +----------+-----------+
                           |
                           v
                +----------------------+
                | Vector Database       |
                +----------+-----------+
                           |
                   Top-K Chunks
                           |
                           v
                +----------------------+
                | Prompt Builder        |
                +----------+-----------+
                           |
                           v
                +----------------------+
                | LLM                   |
                +----------+-----------+
                           |
                           v
                +----------------------+
                | Final Answer          |
                +----------------------+
```

---

# Overall Development Roadmap

Instead of writing everything at once, we'll build it in stages.

| Step | Component           | Goal                                      |
| ---- | ------------------- | ----------------------------------------- |
| 1    | Environment Setup   | Install required libraries                |
| 2    | Load Documents      | Read PDFs and text files                  |
| 3    | Chunk Documents     | Split into manageable pieces              |
| 4    | Generate Embeddings | Convert chunks into vectors               |
| 5    | Store Vectors       | Save vectors in Chroma                    |
| 6    | Semantic Search     | Retrieve relevant chunks                  |
| 7    | Prompt Builder      | Combine context and question              |
| 8    | LLM Integration     | Generate answers                          |
| 9    | Chat Interface      | Interactive question answering            |
| 10   | Improvements        | Source citations, metadata, configuration |

Each step builds directly on the previous one.

---

# Project Structure

We'll use the repository structure you already created:

```text
llm-rag-vector-db-study/
│
├── src/
│   ├── loaders/
│   ├── embeddings/
│   ├── vectorstore/
│   ├── rag/
│   ├── prompts/
│   ├── llm/
│   └── utils/
│
├── datasets/
│
├── examples/
│
└── projects/
```

This organization keeps each responsibility separate.

---

# The RAG Pipeline

Every RAG application has **two major workflows**.

## Workflow 1 — Indexing

This prepares the knowledge base.

```text
Documents
     │
     ▼
Load
     │
     ▼
Chunk
     │
     ▼
Embedding
     │
     ▼
Vector Database
```

This usually runs when documents are added or updated.

---

## Workflow 2 — Query

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
Top Chunks
    │
    ▼
Prompt
    │
    ▼
LLM
    │
    ▼
Answer
```

---

# Our Technology Stack

To keep the focus on learning rather than infrastructure, we'll use:

| Component            | Tool                                                          |
| -------------------- | ------------------------------------------------------------- |
| Programming Language | Python                                                        |
| LLM                  | OpenAI GPT models *(can later be replaced with local models)* |
| Embedding Model      | OpenAI `text-embedding-3-small`                               |
| Vector Database      | ChromaDB                                                      |
| Document Loader      | LangChain Community                                           |
| PDF Parser           | PyPDF                                                         |
| Framework            | LangChain (initially, then we'll explain what it abstracts)   |

Later in the course, we'll discuss alternatives such as local embedding models and different vector databases.

---

# Data Flow

Here's the complete journey from document to answer.

```text
                     INDEXING

PDF
 │
 ▼
Read File
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
Store in ChromaDB


                     QUERY

Question
 │
 ▼
Generate Embedding
 │
 ▼
Search ChromaDB
 │
 ▼
Retrieve Top-K Chunks
 │
 ▼
Build Prompt
 │
 ▼
Send to GPT
 │
 ▼
Answer
```

---

# Component Responsibilities

Understanding each component's job is essential.

| Component       | Responsibility                           |
| --------------- | ---------------------------------------- |
| Loader          | Read documents                           |
| Text Splitter   | Divide large documents into chunks       |
| Embedding Model | Convert text into vectors                |
| Vector Database | Store and search vectors                 |
| Retriever       | Find relevant chunks                     |
| Prompt Builder  | Combine context with the user's question |
| LLM             | Generate the final response              |

Keeping these responsibilities separate makes the system easier to maintain and extend.

---

# What We Won't Do

Our first version is intentionally simple.

We will **not** include:

* Authentication
* User management
* Web interface
* Streaming responses
* Multiple vector databases
* Hybrid search
* Agent workflows

We'll add advanced features in later lessons after we've built a solid foundation.

---

# Expected Project Outcome

By the end of Lesson 7, you'll have an application that works like this:

```
--------------------------------------

Chat with Your Documents

--------------------------------------

Question:

How do I reset my password?

Searching...

Found 3 relevant document chunks...

Answer:

To reset your password:

1. Open the employee portal.
2. Click "Forgot Password."
3. Verify your identity.
4. Create a new password.

Source:
IT_Manual.pdf
Page 18
```

This is the same fundamental pattern used by many enterprise AI assistants.

---

# Lesson Plan

Because Lesson 7 is our **first coding lesson**, we'll divide it into several practical sessions:

| Session | Topic                           |
| ------- | ------------------------------- |
| 7.1     | Environment Setup               |
| 7.2     | Load Documents                  |
| 7.3     | Chunk Documents                 |
| 7.4     | Generate Embeddings             |
| 7.5     | Build the Vector Database       |
| 7.6     | Retrieve Relevant Chunks        |
| 7.7     | Connect the LLM                 |
| 7.8     | Build the Complete RAG Pipeline |
| 7.9     | Test the Application            |
| 7.10    | Refactor and Improve the Code   |

These are **sections within Lesson 7**, not new lessons. They help us build the application incrementally without being overwhelmed.

---

# Key Takeaways

* A production RAG application is built from **independent components**, each with a single responsibility.
* The application has two distinct workflows:

  * **Indexing**: prepare documents for search.
  * **Querying**: answer user questions.
* We'll build the system incrementally, validating each step before moving on.
* By the end of this lesson, you'll have a working **Chat with Your Documents** application that serves as the foundation for the advanced techniques we'll explore in Lessons 8–10.

---

## Before We Start Coding

From this point onward, the course changes from theory to implementation.

We'll write clean, modular, production-style Python code, explain **why** each piece exists, and connect it back to the concepts you've already learned. The goal isn't just to build a RAG application—it's to understand every layer of it so you can adapt, debug, and extend it confidently.
