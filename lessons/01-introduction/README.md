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