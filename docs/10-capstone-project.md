# 🎓 Lesson 10 — Capstone Project

Congratulations!

You've reached the final lesson of the course.

Let's look at what you've accomplished:

| Lesson  | Topic                          | Status    |
| ------- | ------------------------------ | --------- |
| ✅ 01   | Introduction to LLMs           | Completed |
| ✅ 02   | How LLMs Work                  | Completed |
| ✅ 03   | Embeddings                     | Completed |
| ✅ 04   | Vector Databases               | Completed |
| ✅ 05   | Retrieval-Augmented Generation | Completed |
| ✅ 06   | Prompt Engineering             | Completed |
| ✅ 07   | Build a RAG System             | Completed |
| ✅ 08   | Advanced RAG                   | Completed |
| ✅ 09   | Deployment                     | Completed |
| 🚀 10   | Capstone Project               | Current   |

This lesson isn't about learning a new concept.

It's about **bringing everything together into one complete application**.

---

# Capstone Goal

We'll build a **Production-Ready AI Knowledge Assistant**.

Instead of creating a chatbot that only answers general questions, we'll build an application that can answer questions from your own documents.

Imagine a company has:

* HR Policies
* Employee Handbook
* IT Documentation
* Security Manual
* Product Documentation
* Company Wiki
* PDF Files
* Word Documents

Employees should be able to ask:

> "How many vacation days do I receive?"

or

> "How do I reset my VPN password?"

or

> "Where is the onboarding checklist?"

The AI should answer using the company's documents rather than relying only on its pretrained knowledge.

---

# Final Architecture

Everything you've learned now fits together.

```text
                          User
                           │
                           ▼
                    Web / REST API
                           │
                           ▼
                    FastAPI Backend
                           │
              ┌────────────┴────────────┐
              ▼                         ▼
        RAG Pipeline               Authentication
              │
              ▼
      Query Embedding
              │
              ▼
        Vector Database
              │
              ▼
    Retrieve Relevant Chunks
              │
              ▼
       Prompt Construction
              │
              ▼
             LLM
              │
              ▼
       Generated Answer
              │
              ▼
      Source References
```

This architecture resembles the core of many enterprise AI assistants.

---

# Technologies We'll Use

| Component       | Technology                                       |
| --------------- | ------------------------------------------------ |
| Language        | Python                                           |
| API             | FastAPI                                          |
| LLM             | OpenAI GPT (replaceable with local models later) |
| Embeddings      | OpenAI `text-embedding-3-small`                  |
| Vector Database | ChromaDB                                         |
| Document Loader | LangChain Community                              |
| PDF Parser      | PyPDF                                            |
| Environment     | Python Virtual Environment                       |
| Configuration   | `.env`                                           |
| Deployment      | Docker                                           |
| Version Control | Git & GitHub                                     |

---

# Project Structure

```text
ai-knowledge-assistant/
│
├── app/
│   ├── api/
│   ├── config/
│   ├── embeddings/
│   ├── llm/
│   ├── loaders/
│   ├── prompts/
│   ├── rag/
│   ├── services/
│   ├── vectorstore/
│   └── utils/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── documents/
│
├── tests/
│
├── logs/
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .env.example
├── README.md
└── main.py
```

This structure separates responsibilities, making the project easier to maintain and extend.

---

# Features

Our final application will support:

* Document ingestion
* PDF support
* Word document support
* Plain text support
* Automatic chunking
* Embedding generation
* Vector storage
* Semantic search
* RAG
* Prompt engineering
* Source citations
* REST API
* Docker deployment
* Logging
* Configuration management
* Error handling

---

# Complete Workflow

## Phase 1 — Indexing

```text
Documents
      │
      ▼
Load Documents
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
```

This prepares the knowledge base.

---

## Phase 2 — Question Answering

```text
User Question
      │
      ▼
Generate Embedding
      │
      ▼
Similarity Search
      │
      ▼
Retrieve Top-K Chunks
      │
      ▼
Build Prompt
      │
      ▼
GPT
      │
      ▼
Final Answer
```

---

# Data Flow

```text
User
 │
 ▼
FastAPI
 │
 ▼
Embedding Model
 │
 ▼
Vector Database
 │
 ▼
Top-K Chunks
 │
 ▼
Prompt Builder
 │
 ▼
GPT
 │
 ▼
Response
```

Each component has a single responsibility.

---

# Future Improvements

A real-world project rarely stops at version 1.

Potential enhancements include:

### Hybrid Search

Combine semantic and keyword search.

---

### Re-ranking

Improve the order of retrieved documents before sending them to the LLM.

---

### Local LLMs

Replace cloud models with local models such as:

* Llama
* Mistral
* Gemma

---

### Local Embeddings

Replace cloud embeddings with local models such as:

* BGE
* E5
* Nomic Embed

---

### Multiple File Types

Support:

* Excel
* PowerPoint
* HTML
* Markdown
* JSON

---

### User Authentication

Add:

* Login
* Roles
* Permissions

---

### Conversation Memory

Allow users to continue multi-turn conversations while maintaining context.

---

### Feedback System

Enable users to rate responses so the retrieval pipeline can be evaluated and improved over time.

---

# Real-World Use Cases

The same architecture can power many applications:

| Industry        | Example                         |
| --------------- | ------------------------------- |
| Healthcare      | Clinical guidelines assistant   |
| Legal           | Contract search assistant       |
| Finance         | Policy and compliance assistant |
| Education       | Course materials assistant      |
| Manufacturing   | Equipment manuals assistant     |
| Retail          | Product knowledge assistant     |
| Government      | Regulation search assistant     |
| Human Resources | Employee handbook assistant     |

The underlying RAG architecture remains largely the same; only the documents and domain change.

---

# Skills You've Acquired

By completing this course, you can now explain:

### LLMs

* Tokenization
* Embeddings
* Transformers
* Context windows
* Next-token prediction

---

### Embeddings

* Vector representations
* Semantic similarity
* Embedding models

---

### Vector Databases

* Storage
* Similarity search
* Metadata
* Approximate Nearest Neighbor (ANN)

---

### RAG

* Document indexing
* Retrieval
* Prompt construction
* Grounded generation

---

### Prompt Engineering

* System prompts
* User prompts
* Few-shot prompting
* Structured outputs

---

### Advanced RAG

* Hybrid search
* Query rewriting
* Re-ranking
* Context compression
* Agentic RAG
* Graph RAG

---

### Deployment

* FastAPI
* Docker
* Logging
* Monitoring
* CI/CD
* Production architecture

---

# What to Learn Next

This course gives you a solid foundation. From here, you can explore more specialized topics.

### AI Agents

Learn how autonomous systems can:

* Plan tasks
* Use tools
* Make decisions
* Coordinate multiple LLM calls

---

### Model Fine-Tuning

Study:

* Supervised Fine-Tuning (SFT)
* Parameter-Efficient Fine-Tuning (PEFT)
* LoRA
* QLoRA

---

### Model Evaluation

Learn how to measure:

* Retrieval quality
* Response quality
* Hallucination rates
* Latency
* Cost

---

### Model Serving

Explore serving local models with tools such as:

* Ollama
* vLLM
* Text Generation Inference (TGI)

---

### Multimodal AI

Extend RAG systems to work with:

* Images
* Audio
* Video
* Tables
* Charts

---

# Final Summary

Here's the complete picture:

```text
               Documents
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
            Vector Database
                    ▲
                    │
             User Question
                    │
                    ▼
           Generate Embedding
                    │
                    ▼
          Semantic Retrieval
                    │
                    ▼
            Relevant Chunks
                    │
                    ▼
            Prompt Builder
                    │
                    ▼
                   LLM
                    │
                    ▼
             Final Answer
                    │
                    ▼
             Source Citations
```

This is the end-to-end workflow you've been building toward throughout the course.

---

# Final Project Challenge

Now it's your turn.

Build an AI Knowledge Assistant that:

* Accepts PDF, DOCX, and TXT documents.
* Indexes them into a vector database.
* Provides a REST API for question answering.
* Returns answers with source citations.
* Uses Docker for deployment.
* Includes logging and error handling.
* Stores configuration in environment variables.
* Has a clear, modular project structure.
* Includes a comprehensive `README.md`.
* Is published on GitHub.

This project will demonstrate not only your understanding of LLMs, embeddings, vector databases, and RAG, but also your ability to apply software engineering practices to build a maintainable AI application.

---

# Congratulations! 🎉

You have completed the **LLM, RAG, and Vector Database** course.

You now understand the concepts behind modern AI assistants and have a roadmap for building and deploying your own.

One recommendation, though: **don't stop here**.

The best way to deepen your understanding is to keep iterating on the capstone. Add features, replace components (try a different vector database or embedding model), benchmark retrieval quality, and deploy it. Each improvement will reinforce the concepts you've learned and expose you to the practical trade-offs that every real-world AI application must address.

You've built the foundation. Now it's time to turn it into experience. 🚀


