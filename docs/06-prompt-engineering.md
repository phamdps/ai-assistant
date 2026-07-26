# Lesson 6 — Prompt Engineering

Many people think Prompt Engineering is simply "writing good prompts." In reality, it's about **designing clear instructions that maximize the quality, consistency, and reliability of an LLM's output**.

## Learning Objectives

By the end of this lesson, you will be able to:

* Understand what Prompt Engineering is
* Differentiate between System, User, and Assistant prompts
* Use Zero-shot, One-shot, and Few-shot prompting
* Design prompts that produce reliable outputs
* Create structured outputs (JSON, Markdown, Tables)
* Apply prompt engineering in RAG systems
* Understand common prompting mistakes
* Follow prompt engineering best practices

---

# 1. What is Prompt Engineering?

A **prompt** is the input you provide to an LLM.

A prompt can be:

* A question
* An instruction
* A conversation
* A document
* A list of examples
* A combination of all of the above

Example:

```text
Explain what a Vector Database is.
```

This is a prompt.

---

Prompt Engineering is the process of **designing prompts that guide the LLM toward the desired behavior and output**.

Think of it like giving instructions to a very knowledgeable intern.

Consider these two requests:

❌ Poor instruction:

```text
Write about RAG.
```

The model doesn't know:

* How long?
* Beginner or expert?
* Formal or casual?
* Include examples?
* Markdown or plain text?

---

Better instruction:

```text
Explain Retrieval-Augmented Generation to a beginner.

Requirements:

- Less than 300 words
- Use one real-world example
- Avoid technical jargon
- Finish with three key takeaways
```

The second prompt gives the model enough context to produce a more targeted response.

---

# 2. Anatomy of a Prompt

A high-quality prompt usually contains four elements:

```text
Instruction

↓

Context

↓

Input

↓

Expected Output
```

Example:

```text
Instruction:
Summarize the document.

Context:
The audience is software engineers.

Input:
<document>

Output:
Bullet points with a maximum of 10 items.
```

This structure helps the model understand not only **what** to do, but **how** to present the result.

---

# 3. Types of Messages

Modern chat-based LLM APIs distinguish different message roles.

## System Message

The **System Message** defines the assistant's overall behavior.

Example:

```text
You are a cybersecurity expert.

Always explain concepts clearly.

If you are uncertain, say so.

Never invent information.
```

The system prompt acts as the "operating instructions" for the model.

---

## User Message

The user message contains the actual request.

Example:

```text
Explain ransomware.
```

---

## Assistant Message

Assistant messages are previous responses in the conversation.

Example:

```text
Ransomware is malicious software that encrypts files...
```

These previous exchanges become part of the conversation context.

---

# Conversation Structure

```text
System
      │
      ▼
User
      │
      ▼
Assistant
      │
      ▼
User
      │
      ▼
Assistant
```

Every new response is generated using the available conversation context.

---

# 4. Zero-Shot Prompting

Zero-shot means **no examples are provided**.

Example:

```text
Translate the following sentence into French.

I love AI.
```

The model relies on its prior training.

This is the simplest prompting style.

---

# 5. One-Shot Prompting

One-shot prompting provides **one example**.

```text
Example:

Input:
Hello

Output:
Bonjour

Now translate:

Good morning
```

The model infers the expected format from the example.

---

# 6. Few-Shot Prompting

Few-shot prompting provides several examples.

```text
Input:
Dog

Category:
Animal

Input:
Car

Category:
Vehicle

Input:
Apple

Category:
Fruit

Now classify:

Lion
```

The expected output is:

```text
Animal
```

The examples help the model recognize the desired pattern.

---

# 7. Role Prompting

You can ask the model to adopt a specific perspective.

Example:

```text
You are a senior Python developer.

Review the following code.

Suggest improvements.
```

Or:

```text
You are a university professor.

Explain embeddings to first-year students.
```

The role influences tone, level of detail, and style—but it does **not** give the model new knowledge.

---

# 8. Structured Output

Instead of free-form text, you can ask for a specific format.

Example:

```text
Return the answer as JSON.

{
  "name": "",
  "department": "",
  "email": ""
}
```

Or:

```text
Return the answer as a Markdown table.
```

Or:

```text
Return exactly three bullet points.
```

Structured outputs are especially useful when another application will consume the model's response.

---

# 9. Prompt Engineering in RAG

Let's connect this to what we've learned.

Suppose the vector database retrieves this chunk:

```text
Password Reset Procedure

1. Open the employee portal.
2. Click Forgot Password.
3. Verify your identity.
```

A weak prompt:

```text
Answer the question.
```

A stronger prompt:

```text
You are an IT support assistant.

Answer only using the provided context.

If the answer is not contained in the context, reply:

"I don't have enough information."

Context:

Password Reset Procedure

1. Open the employee portal.
2. Click Forgot Password.
3. Verify your identity.

Question:

How do I recover my password?
```

This prompt reduces the likelihood of unsupported or invented information.

---

# 10. Common Prompting Mistakes

### Mistake 1: Being Too Vague

❌

```text
Tell me about AI.
```

Better:

```text
Explain AI to a beginner in fewer than 300 words using one real-world example.
```

---

### Mistake 2: Combining Too Many Tasks

❌

```text
Summarize this PDF.

Translate it.

Generate Python code.

Create a quiz.

Write a poem.
```

Instead, break complex workflows into separate prompts.

---

### Mistake 3: Missing Output Format

Instead of:

```text
List the results.
```

Specify:

```text
Return a Markdown table with three columns:

Name

Department

Role
```

---

### Mistake 4: Assuming Knowledge That Isn't Present

In a RAG system:

```text
Answer the question.
```

A better instruction is:

```text
Answer only using the provided context.

If the context is insufficient, say so.
```

This makes the system more trustworthy.

---

# 11. Prompt Engineering Best Practices

When writing prompts:

* Be clear about the task.
* Provide relevant context.
* Specify the audience when appropriate.
* Define the desired output format.
* State any constraints (length, tone, style).
* Use examples when the task is complex.
* For RAG, instruct the model to rely on the retrieved context and acknowledge when information is missing.

---

# 12. Putting It All Together

Imagine you're building an HR assistant.

The prompt might look like this:

```text
System:

You are an HR assistant.

Answer only from the supplied context.

If the answer cannot be found, say:

"I don't have enough information."

Keep answers under 150 words.

Always include the policy page number if available.


Context:

Employee Handbook

Page 25

Employees receive 20 annual vacation days.


Question:

How many vacation days do employees receive?
```

A good response would be:

> Employees receive **20 annual vacation days** according to the Employee Handbook (Page 25).

This response is concise, grounded in the provided context, and includes the requested citation.

---

# Summary

Prompt Engineering is about giving the model the right instructions, context, and constraints.

```text
User Request
      │
      ▼
Clear Instructions
      │
      ▼
Relevant Context
      │
      ▼
Desired Format
      │
      ▼
LLM
      │
      ▼
Reliable Output
```

The better the prompt, the more likely the model is to produce useful and consistent results.

---

# Key Takeaways

* A prompt is more than a question—it includes instructions, context, and expected output.
* Chat-based LLMs typically use **System**, **User**, and **Assistant** messages.
* **Zero-shot**, **One-shot**, and **Few-shot** prompting are different ways of guiding the model.
* Structured outputs make responses easier for applications to process.
* In RAG systems, prompts should tell the LLM to rely on the retrieved context.
* Clear prompts improve consistency, but they cannot compensate for missing or incorrect information.

---

# Quiz

1. What is the purpose of a System Message?
2. When would you use Few-shot prompting instead of Zero-shot prompting?
3. Why is specifying an output format useful?
4. How does Prompt Engineering improve a RAG system?
5. Why should a RAG prompt instruct the model to answer only from the provided context?
6. Does assigning a role (such as "You are a lawyer") give the model new knowledge? Why or why not?

---

# Exercise

Imagine you're building a **Customer Support RAG Assistant** for an online retailer.

The retrieved context contains:

```text
Return Policy

Customers may return products within 30 days of purchase.

Items must be in their original condition.

Digital products are non-refundable.
```

Write a complete prompt that includes:

1. A **System Message** defining the assistant's behavior.
2. The **retrieved context**.
3. The **user's question**: *"Can I return an e-book after buying it?"*
4. Instructions telling the model what to do if the answer is not present in the context.

Try writing the full prompt yourself before checking the solution. This exercise mirrors how prompts are constructed in real-world RAG applications.

---

## Looking Ahead: Lesson 7 — Build a RAG System

You've now learned all the core concepts:

* **LLMs** generate text.
* **Embeddings** represent semantic meaning.
* **Vector databases** retrieve relevant information.
* **RAG** combines retrieval and generation.
* **Prompt engineering** tells the LLM how to use the retrieved information effectively.

In Lesson 7, we'll stop discussing concepts and start building. We'll create a complete RAG application in Python, step by step, loading documents, generating embeddings, storing them in a vector database, retrieving relevant chunks, and generating answers with an LLM. By the end, you'll have a working "Chat with Your Documents" application.
