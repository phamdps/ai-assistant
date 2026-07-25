# Course Outline

We'll cover the material in ten lessons:

1. **Introduction to Generative AI and LLMs**
2. **How LLMs Work**
3. **Embeddings and Semantic Search**
4. **Vector Databases**
5. **Retrieval-Augmented Generation (RAG)**
6. **Prompt Engineering**
7. **Building a Simple RAG Application**
8. **Advanced RAG Techniques**
9. **Deploying an AI Application**
10. **Capstone Project: AI Document Assistant**

Every lesson will include:

* Theory
* Visual explanation
* Practical examples
* Hands-on coding
* Quiz
* Mini-project

---

# Lesson 1: What Is an LLM?

## What does LLM stand for?

**LLM = Large Language Model**

A Large Language Model is an AI system trained to predict the next word (or, more precisely, the next token) in a sequence.

For example, if you type:

> The capital of France is

the model predicts:

> Paris

It does this not because it memorized that sentence exactly, but because it has learned statistical patterns from enormous amounts of text.

---

## Why is it called "Large"?

There are three reasons:

* It is trained on massive datasets (books, websites, articles, code, and more).
* It has billions or even trillions of parameters (the internal values learned during training).
* Training requires significant computing resources, often thousands of GPUs.

Examples:

| Model              |                   Approximate Parameters |
| ------------------ | ---------------------------------------: |
| GPT-2              |                                     1.5B |
| Llama 3 8B         |                                       8B |
| GPT-4-class models |                   Not publicly disclosed |
| DeepSeek           | Hundreds of billions (varies by version) |

---

## What Can an LLM Do?

An LLM can:

* Answer questions
* Write code
* Summarize documents
* Translate languages
* Explain concepts
* Draft emails
* Analyze text
* Generate SQL
* Help debug software

For example:

**Input**

> Explain recursion like I'm 10 years old.

**Output**

> Imagine standing between two mirrors. Each mirror reflects the other over and over. Recursion is similar—a function can call itself repeatedly until it reaches a stopping point.

---

# Is an LLM a Database?

**No.**

This is one of the most common misconceptions.

An LLM does **not** store facts like a database.

Instead, it stores patterns learned during training.

Think of the difference like this:

**Database**

* Stores exact records.
* Retrieves specific entries.
* Can be updated immediately.

**LLM**

* Learns statistical relationships.
* Generates likely responses.
* Cannot instantly learn new facts without additional mechanisms (such as RAG or retraining).

---

# How Does an LLM Respond?

Imagine you ask:

> Who invented Python?

The process looks like this:

```text
User Question
      │
      ▼
Convert text into tokens
      │
      ▼
LLM processes the tokens
      │
      ▼
Predict the next token
      │
      ▼
Generate the complete answer
```

Notice that the model doesn't "search Google." It predicts one token at a time based on its training and the current context.

---

# A Helpful Analogy

Imagine a student who has read **millions of books**.

If you ask:

> What is photosynthesis?

They don't search a library—they answer from what they've learned.

An LLM behaves similarly, except its "knowledge" comes from statistical training rather than human understanding.

---

# What an LLM Cannot Reliably Do

Suppose your company created a policy document yesterday.

If you ask:

> What is our new vacation policy?

A standalone LLM cannot reliably answer because it has never seen that document.

This limitation motivates **Retrieval-Augmented Generation (RAG)**, which we'll study later.

---

# Real-World Applications

LLMs power many kinds of software:

* Customer support chatbots
* Code assistants
* Document summarizers
* AI tutors
* Medical documentation assistants (with appropriate oversight)
* Legal document search tools
* Enterprise knowledge assistants

---

# Key Takeaways

* An **LLM** predicts the next token based on context.
* It learns patterns rather than storing exact records.
* It is excellent at language tasks but doesn't automatically know your private or newly created data.
* **RAG** extends an LLM by providing relevant external information at query time.

---

# Quick Quiz

Try answering these without looking back:

1. What does **LLM** stand for?
2. Why is it called "Large"?
3. Does an LLM store information like a database?
4. What is the primary task an LLM performs during text generation?
5. Why can't a standalone LLM answer questions about a document created yesterday?

You can reply with your answers (e.g., "1: ..., 2: ..."), and I'll review them.

### Looking Ahead

In **Lesson 2**, we'll dive into what happens inside an LLM:

* What are **tokens**?
* How does text become numbers?
* What are **embeddings**?
* How does the model actually "understand" language?
* Why are transformers the foundation of modern LLMs?

We'll move from conceptual understanding toward the mechanics that make LLMs work, laying the groundwork for RAG and vector databases.
