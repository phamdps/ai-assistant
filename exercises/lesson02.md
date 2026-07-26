Great. 🎉 Lesson 1 is complete.

You have successfully built and tested:

* ✅ Your first LLM application
* ✅ Local LLM execution with Ollama
* ✅ Provider abstraction (Ollama/OpenAI)
* ✅ Environment configuration
* ✅ System prompts
* ✅ Prompt behavior experiments

Now we move to:

# Lesson 2 — How LLMs Work

## Learning Goal

In Lesson 1, we treated the LLM as a "black box":

```text
Question
   |
   v
LLM
   |
   v
Answer
```

Now we open the box and understand what happens internally.

We will learn:

1. How text becomes tokens
2. How tokens become numbers
3. How the model processes context
4. How transformers work at a high level
5. How the model predicts the next token
6. Context windows
7. Token costs and limitations

---

# Lesson 2 Project Structure

Create:

```text
lessons/
└── 02-how-llms-work/
    │
    ├── README.md
    ├── requirements.txt
    ├── tokenizer_demo.py
    ├── token_counter.py
    ├── context_window_demo.py
    └── exercises/
        └── exercise1.py
```

---

# Concept 1 — Text Is Not Input to an LLM

Humans see:

```
Hello, how are you?
```

The LLM does not.

The model sees:

```
[15496, 11, 703, 389, 345, 30]
```

These are **tokens**.

The pipeline:

```text
Human Text

      |
      v

Tokenizer

      |
      v

Token IDs

      |
      v

Neural Network

      |
      v

Next Token Prediction

      |
      v

Generated Text
```

---

# Concept 2 — Tokenization

Example:

Text:

```
Artificial intelligence is amazing.
```

might become:

```
Artificial
intelligence
is
amazing
.
```

or internally:

```
[15559, 4430, 318, 4998, 13]
```

The exact numbers depend on the tokenizer.

---

# Step 1 — Install Dependencies

Create:

```
lessons/02-how-llms-work/requirements.txt
```

Content:

```txt
tiktoken>=0.9.0
python-dotenv>=1.1.0
```

Install:

```bash
pip install -r requirements.txt
```

---

# Step 2 — tokenizer_demo.py

Create:

```
tokenizer_demo.py
```

Code:

```python
import tiktoken


def main():

    text = input(
        "Enter text to tokenize:\n> "
    )

    encoding = tiktoken.get_encoding(
        "cl100k_base"
    )

    tokens = encoding.encode(text)

    print("\nOriginal text:")
    print(text)

    print("\nToken IDs:")
    print(tokens)

    print("\nNumber of tokens:")
    print(len(tokens))

    print("\nDecoded tokens:")

    for token in tokens:
        print(
            token,
            "=>",
            encoding.decode([token])
        )


if __name__ == "__main__":
    main()
```

---

# Run

```bash
python tokenizer_demo.py
```

Example:

Input:

```
Hello world
```

Output:

```
Token IDs:

[9906, 1917]

Number of tokens:

2

Decoded tokens:

9906 => Hello
1917 => world
```

---

# Concept 3 — Why Tokens Matter

Every LLM has a context limit.

Example:

```
Model Context Window

|--------------------------|
|                          |
|  Input tokens            |
|                          |
|  +                       |
|                          |
|  Output tokens           |
|                          |
|--------------------------|

```

If the input is too large:

```
ERROR:

Context length exceeded
```

---

# Step 3 — token_counter.py

Create:

```
token_counter.py
```

Code:

```python
import tiktoken


def count_tokens(text):

    encoding = tiktoken.get_encoding(
        "cl100k_base"
    )

    tokens = encoding.encode(text)

    return len(tokens)


def main():

    text = """
    Large Language Models learn patterns
    from huge amounts of text data.
    """

    count = count_tokens(text)

    print(
        f"Token count: {count}"
    )


if __name__ == "__main__":
    main()
```

---

# Concept 4 — The Core Idea of an LLM

An LLM does not "think" like humans.

Its fundamental operation:

```
Given previous tokens:

"The capital of France is"

predict next token:

"Paris"
```

Mathematically:

```
P(next token | previous tokens)
```

Example:

Input:

```
The sky is
```

The model calculates:

```
blue     0.72
green    0.10
dark     0.05
red      0.01
```

Then selects a token.

---

# Concept 5 — Temperature

Temperature controls randomness.

Low temperature:

```
temperature = 0.1
```

Output:

```
The answer is always consistent.
```

High temperature:

```
temperature = 1.0
```

Output:

```
More creative and varied.
```

---

# Step 4 — context_window_demo.py

Create:

```python
def estimate_context(
        input_tokens,
        output_tokens,
        context_limit=4096
):

    total = input_tokens + output_tokens

    print(
        f"""
Input tokens:
{input_tokens}

Output tokens:
{output_tokens}

Total:
{total}

Context limit:
{context_limit}
"""
    )

    if total > context_limit:
        print(
            "WARNING: Context window exceeded!"
        )
    else:
        print(
            "OK: Within context window."
        )


if __name__ == "__main__":

    estimate_context(
        3000,
        1500
    )
```

---

# Exercise 1

Create:

```
exercises/exercise1.py
```

Task:

Experiment with tokenization.

Code:

```python
import tiktoken


encoding = tiktoken.get_encoding(
    "cl100k_base"
)


sentences = [
    "Hello",
    "Hello world",
    "Artificial Intelligence",
    "Artificial Intelligence is changing the world"
]


for sentence in sentences:

    tokens = encoding.encode(sentence)

    print("=" * 50)

    print(sentence)

    print(
        "Tokens:",
        tokens
    )

    print(
        "Count:",
        len(tokens)
    )
```

---

# Lesson 2 Exercise Questions

After running the code, answer:

### Question 1

Why does:

```
Hello
```

use fewer tokens than:

```
Artificial Intelligence
```

?

---

### Question 2

Why do LLMs need tokenization?

---

### Question 3

What happens when a conversation becomes longer than the model context window?

---

# Homework Challenge

Modify `tokenizer_demo.py`:

Ask the user for:

```
Maximum token limit:
```

Example:

```
Limit: 10 tokens
```

Then:

* Count the tokens.
* Warn if exceeded.

---

# Lesson 2 Outcome

After this lesson you should understand:

✅ Text → Tokens
✅ Tokens → Numbers
✅ Context windows
✅ Next-token prediction
✅ Temperature
✅ Why token limits exist

---

After completing the code, we'll continue to:

# Lesson 3 — Embeddings

where we move from:

> "How does an LLM understand text?"

to:

> "How can a computer compare the meaning of two pieces of text?"

That lesson is the foundation of Vector Databases and RAG.
