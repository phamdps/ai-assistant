# Lesson 01 - Introduction to LLMs

## Goal

Build your first application that communicates with an LLM.

By the end of this lesson you'll understand:

* Project structure
* OpenAI API
* Environment variables
* Chat Completions
* System/User messages
* Temperature
* Error handling
* Clean Python code

---

# Folder Structure

```text
lessons/
└── 01-introduction/
    ├── README.md
    ├── requirements.txt
    ├── .env.example
    ├── main.py
    ├── config.py
    ├── client.py
    ├── prompts.py
    └── exercises/
        └── exercise1.py
```

> **Note:** I recommend slightly expanding the original skeleton by adding `client.py` and `prompts.py`. This keeps responsibilities separated from the very beginning and establishes patterns we'll reuse in later lessons.

---

# File 1 — requirements.txt

```text
openai>=1.95.0
python-dotenv>=1.1.0
```

---

# File 2 — .env.example

```text
OPENAI_API_KEY=your_api_key_here
MODEL_NAME=gpt-5.5
```

---

# File 3 — config.py

```python
from dotenv import load_dotenv
import os

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
MODEL_NAME = os.getenv("MODEL_NAME", "gpt-5.5")

if not OPENAI_API_KEY:
    raise ValueError(
        "OPENAI_API_KEY not found. "
        "Please create a .env file."
    )
```

---

# File 4 — client.py

```python
from openai import OpenAI
from config import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)
```

---

# File 5 — prompts.py

```python
SYSTEM_PROMPT = """
You are an AI tutor.

Explain concepts clearly.

Use beginner-friendly language.

Keep responses concise.

If you don't know something,
say so instead of making it up.
"""
```

---

# File 6 — main.py

```python
from openai import APIError
from client import client
from config import MODEL_NAME
from prompts import SYSTEM_PROMPT


def chat(question: str) -> str:
    """
    Send a prompt to the LLM
    and return the response.
    """

    response = client.chat.completions.create(
        model=MODEL_NAME,
        temperature=0.7,
        messages=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT,
            },
            {
                "role": "user",
                "content": question,
            },
        ],
    )

    return response.choices[0].message.content


def main():

    print("=" * 50)
    print("Lesson 01 - Introduction to LLMs")
    print("=" * 50)

    question = input("\nAsk a question:\n> ")

    try:

        answer = chat(question)

        print("\nAssistant:\n")
        print(answer)

    except APIError as e:

        print(f"\nOpenAI API Error:\n{e}")

    except Exception as e:

        print(f"\nUnexpected Error:\n{e}")


if __name__ == "__main__":
    main()
```

---

# File 7 — exercises/exercise1.py

```python
"""
Exercise 1

Modify the system prompt so the AI becomes:

- a Python instructor
- a Linux expert
- a Database administrator

Observe how the answers change.
"""

from main import chat

question = "Explain what an API is."

print(chat(question))
```

---

# File 8 — README.md

````markdown
# Lesson 01 – Introduction to LLMs

## Objective

Build your first Python application that communicates with an LLM using the OpenAI API.

---

## Topics

- OpenAI SDK
- Environment Variables
- Chat Completions API
- System Prompt
- User Prompt
- Temperature
- Error Handling

---

## Installation

```bash
python -m venv .venv
```

Activate the virtual environment.

Install dependencies:

```bash
pip install -r requirements.txt
```

Copy:

```text
.env.example
```

to:

```text
.env
```

Add your API key.

---

## Run

```bash
python main.py
```

Example:

```
Ask a question:

What is Machine Learning?
```

---

## Expected Output

```
Machine learning is a branch of artificial intelligence...
```

---

## Exercise

Edit `prompts.py` and observe how changing the system prompt affects the responses.
````

---

# What Students Learn

By completing this lesson they will understand:

✔ Installing packages

✔ Environment variables

✔ Creating an OpenAI client

✔ Calling an LLM

✔ System prompts

✔ User prompts

✔ Model selection

✔ Temperature

✔ Basic error handling

✔ Clean project organization

---

# Sample Run

```text
==================================================
Lesson 01 - Introduction to LLMs
==================================================

Ask a question:
> What is an embedding?

Assistant:

An embedding is a numerical representation of data...
```

---

# Git Commit

A good commit message for this lesson would be:

```bash
git add .
git commit -m "Lesson 01: Build first LLM application using OpenAI API"
```

---

## A Small Improvement Before Lesson 2

Before moving on, I'd make one enhancement to the repository that will benefit every remaining lesson:

```text
lessons/
└── 01-introduction/
    ├── README.md
    ├── requirements.txt
    ├── .env.example
    ├── .gitignore
    ├── config.py
    ├── client.py
    ├── prompts.py
    ├── main.py
    └── exercises/
```

with a lesson-specific `.gitignore` such as:

```gitignore
.venv/
.env
__pycache__/
*.pyc
```

From Lesson 2 onward, we'll continue using this clean, modular structure. As the lessons become more advanced (especially Lessons 7–10), the same design principles will naturally scale into a production-style AI application.
