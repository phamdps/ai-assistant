# Lesson 2 — How LLMs Work

## Learning Objectives

By the end of this lesson, you will understand:

* What happens when you type a prompt into ChatGPT.
* What a **token** is.
* Why LLMs work with tokens instead of words.
* How text is converted into numbers.
* What an embedding is (at a high level—we'll study it in depth in Lesson 3).
* How a Transformer processes information.
* What a context window is.
* How an LLM generates text one token at a time.

---

# The Journey of Your Prompt

Suppose you ask:

> **What is Retrieval-Augmented Generation?**

It seems like the model instantly understands your question.

In reality, several steps happen behind the scenes.

```text
User Prompt
     │
     ▼
Tokenization
     │
     ▼
Convert Tokens to IDs
     │
     ▼
Embedding Layer
     │
     ▼
Transformer Layers
     │
     ▼
Probability Distribution
     │
     ▼
Next Token
     │
     ▼
Repeat...
     │
     ▼
Final Answer
```

We'll study each step individually.

---

# Step 1 — Tokenization

The computer doesn't understand English, French, or any human language directly.

Instead, it breaks text into **tokens**.

A token is the smallest unit the model works with.

For example:

```text
Hello world!
```

might become:

```text
["Hello", " world", "!"]
```

Notice that the leading space in `" world"` is part of the token. Tokenizers are designed to efficiently encode common text patterns, not just split on spaces.

Another example:

```text
ChatGPT is amazing.
```

could become:

```text
["Chat", "G", "PT", " is", " amazing", "."]
```

**Important:** Tokens are **not always words**.

They can represent:

* Entire words
* Parts of words
* Punctuation
* Numbers
* Emojis
* Even whitespace

---

# Why Not Use Words?

Imagine storing every possible English word.

Now add:

* Medical terminology
* Programming languages
* Names
* Slang
* Multiple human languages

The vocabulary would become enormous.

Instead, LLMs use **subword tokenization**.

Example:

```text
unbelievable
```

might become:

```text
un
believ
able
```

This lets the model understand words it has never seen exactly before by composing them from familiar pieces.

---

# Token IDs

The model doesn't operate directly on text.

Each token is mapped to an integer.

Example:

```text
"Hello" → 15496
"world" → 995
"!" → 0
```

Internally, your sentence becomes something like:

```text
[15496, 995, 0]
```

At this point, the input is still just a sequence of IDs—not meaningful numerical representations yet.

---

# Step 2 — Embedding Layer

Now the model converts each token ID into a dense numerical vector.

For example:

```text
"Paris"
```

becomes something conceptually like:

```text
[0.21,
-0.83,
0.77,
...
0.12]
```

Real embedding vectors often contain hundreds or thousands of dimensions.

Think of an embedding as a **mathematical representation of meaning**.

Words with similar meanings tend to have vectors that are close together.

Example:

```text
King
Queen
Prince
Princess
```

These vectors occupy nearby regions of the embedding space because they are used in similar contexts.

> **Note:** We'll dedicate **Lesson 3** entirely to embeddings, vector spaces, and semantic similarity.

---

# Step 3 — The Transformer

This is the heart of the LLM.

Before Transformers, many language models struggled to remember information from earlier in a sentence or document.

Transformers solved this using a mechanism called **attention**.

Very roughly, the model asks:

> Which previous tokens are most relevant to understanding the current one?

Example:

```text
The cat chased the mouse because it was hungry.
```

When processing **"it"**, the model learns that "it" most likely refers to **the cat**, not the mouse.

Attention allows the model to weigh relationships across the entire context.

In a later lesson, we'll explore self-attention in detail.

---

# Step 4 — Predict the Next Token

After processing the input, the model doesn't generate a full sentence all at once.

Instead, it predicts the **next token**.

Example:

Input:

```text
The capital of France is
```

Possible next-token probabilities might look like:

| Token  | Probability |
| ------ | ----------: |
| Paris  |        0.91 |
| Lyon   |        0.04 |
| London |        0.02 |
| Berlin |        0.01 |
| Other  |        0.02 |

The model chooses (or samples) the next token according to these probabilities.

Suppose it selects:

```text
Paris
```

Now the input becomes:

```text
The capital of France is Paris
```

The entire process repeats to generate the next token.

---

# Autoregressive Generation

This repeated prediction process is called **autoregressive generation**.

The loop is:

```text
Predict next token
        ↓
Append token
        ↓
Predict again
        ↓
Append again
        ↓
Continue until finished
```

Every response from an LLM is generated this way.

---

# Context Window

The model doesn't remember your entire life or every conversation you've ever had.

It only processes a limited amount of recent input at once.

This limit is called the **context window**.

It includes:

* Your current prompt
* Relevant conversation history
* Any retrieved RAG documents
* System instructions

If the combined content exceeds the context window, older information may be omitted or summarized by the application.

---

# Putting It All Together

When you ask:

> Explain RAG simply.

The flow is:

```text
Prompt
   │
   ▼
Tokenizer
   │
   ▼
Token IDs
   │
   ▼
Embedding Layer
   │
   ▼
Transformer
   │
   ▼
Next Token Prediction
   │
   ▼
Generated Response
```

This entire pipeline executes extremely quickly, producing the interactive experience you're familiar with.

---

# Key Takeaways

* LLMs operate on **tokens**, not words.
* Tokens are converted into **integer IDs**.
* IDs are transformed into **embedding vectors**.
* Transformers use **attention** to understand relationships within the input.
* The model generates text **one token at a time**.
* The **context window** determines how much information the model can consider during generation.

---

# Mini Exercise

Take the sentence:

> **"Vector databases improve RAG systems."**

Try answering these questions:

1. Why might this sentence be split into more than five tokens?
2. Why do we convert tokens into IDs before creating embeddings?
3. Why are embeddings more useful than raw token IDs?
4. Why does the model generate one token at a time instead of the whole sentence?

Don't worry about perfect wording—focus on the underlying concepts.

---

### What's Next?

In **Lesson 3: Embeddings**, we'll explore one of the most important concepts in modern AI. You'll learn:

* What embeddings really are.
* How semantic similarity works.
* Why "car" and "automobile" are considered similar even though they're different words.
* How embeddings enable vector databases and RAG.

This lesson is the bridge between understanding LLMs and building practical AI retrieval systems.
