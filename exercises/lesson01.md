# Lesson 01 – Introduction to LLMs

## Objective

Build your first application that communicates with an LLM.

## Features

- Supports OpenAI
- Supports Ollama
- Uses environment variables
- Interactive chat
- System prompts
- Error handling

## Installation

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it and install dependencies:

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

Choose your provider:

### Ollama

```text
LLM_PROVIDER=ollama
OLLAMA_MODEL=llama3.2
```

### OpenAI

```text
LLM_PROVIDER=openai
OPENAI_API_KEY=YOUR_KEY
```

Run:

```bash
python main.py
```

Run the exercise:

```bash
python exercises/exercise1.py
```
Installing **Llama 3.2** is straightforward with **Ollama**, which is the easiest way to run local LLMs. Since we'll use Ollama throughout the rest of the course, this is the recommended setup.

---

# Install Ollama

## Ubuntu / Debian

Run:

```bash
curl -fsSL https://ollama.com/install.sh | sh
```

Verify the installation:

```bash
ollama --version
```

You should see something like:

```text
ollama version 0.x.x
```

---

# Step 2: Start the Ollama service

Most installations start it automatically. If needed, run:

```bash
ollama serve
```

If it's already running, you'll see a message indicating the address (typically `http://localhost:11434`).

---

# Step 3: Download Llama 3.2

For the standard 3B model:

```bash
ollama pull llama3.2
```

Ollama will download the model, which may take a few minutes depending on your internet connection.

---

# Step 4: Verify the model

List installed models:

```bash
ollama list
```

Example output:

```text
NAME          ID          SIZE
llama3.2      xxxxxxxx    2.0 GB
```

---

# Step 5: Test the model

Run it interactively:

```bash
ollama run llama3.2
```

Example:

```text
>>> What is an embedding?
```

The model should generate a response.

Exit with:

```text
/bye
```

or press **Ctrl + D**.

---

# Step 6: Test the HTTP API

Check that the API is available:

```bash
curl http://localhost:11434/api/tags
```

You should receive JSON listing your installed models.

---

# Step 7: Configure your project

In your `.env` file:

```env
LLM_PROVIDER=ollama

OLLAMA_URL=http://localhost:11434

OLLAMA_MODEL=llama3.2
```

Now your Python code can use the local model.

---

# Hardware recommendations

| Model        | RAM (minimum) | Recommended |
| ------------ | ------------: | ----------: |
| Llama 3.2 1B |          4 GB |        8 GB |
| Llama 3.2 3B |          8 GB |      16 GB+ |

If your machine has limited memory, the **1B** model is a good choice for learning. The **3B** model generally provides better responses while remaining practical on many modern laptops.

---

# Useful Ollama commands

```bash
# List installed models
ollama list

# Download a model
ollama pull llama3.2

# Run a model
ollama run llama3.2

# Remove a model
ollama rm llama3.2

# Show installed version
ollama --version

# Start the server
ollama serve
```

---

## Recommendation for our course

For the exercises in this course, I'd suggest:

* **Development:** Ollama + `llama3.2` (local, no API cost)
* **Later comparisons:** OpenAI API (to compare response quality, latency, and cost)

This approach lets you complete every lesson locally while also understanding how to swap between local and cloud-hosted LLMs using the same application architecture.
