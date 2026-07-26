Excellent. 🎉 Lesson 4 is complete.

You have now built the **retrieval foundation** of modern AI assistants.

You understand:

* ✅ Embeddings convert meaning into vectors.
* ✅ Vector databases store and search those vectors.
* ✅ Semantic search finds relevant information.
* ✅ ChromaDB can act as a local vector database.
* ✅ Retrieval is the first half of RAG.

Now we combine everything.

# Lesson 5 — Retrieval-Augmented Generation (RAG)

## Learning Goal

Until now, our LLM only knows what it learned during training.

Example:

```text
User:
"What is our company's vacation policy?"

LLM:
"I don't know."
```

Why?

Because the company's documents were never part of the model's training data.

RAG solves this problem.

---

# What is RAG?

**Retrieval-Augmented Generation** means:

> Retrieve relevant information first, then ask the LLM to generate an answer using that information.

The pipeline:

```text
                 User Question

                       |
                       v

                Create Embedding

                       |
                       v

              Search Vector Database

                       |
                       v

              Retrieve Relevant Chunks

                       |
                       v

              Build Prompt

                       |
                       v

                    LLM

                       |
                       v

                 Final Answer
```

---

# Without RAG

```text
Question
   |
   v
LLM
   |
   v
Answer
```

The LLM only uses:

* Training data
* Conversation history

---

# With RAG

```text
Question

   +
   
Your Documents

   |

   v

LLM

   |

   v

Answer based on your data
```

---

# Real-world Examples

## Company AI Assistant

Documents:

```
employee_handbook.pdf
security_policy.pdf
benefits.pdf
```

User:

```
How many vacation days do employees receive?
```

RAG:

```
Retrieve vacation policy
        |
        v
Send policy + question to LLM
        |
        v
Answer
```

---

## Chat With Documents

Examples:

* Legal documents
* Research papers
* Product manuals
* Internal knowledge bases
* Customer support documents

---

# Lesson 5 Project Structure

Create:

```text
lessons/
└── 05-rag/
    |
    ├── README.md
    ├── requirements.txt
    |
    ├── config.py
    ├── embeddings.py
    ├── vector_store.py
    ├── retriever.py
    ├── llm.py
    ├── rag_pipeline.py
    ├── main.py
    |
    ├── documents/
    │   └── company_policy.txt
    |
    └── exercises/
        └── exercise1.py
```

---

# Architecture

Our application:

```text
                 main.py

                    |
                    v

             rag_pipeline.py

              /          \

             /            \

     Retriever             LLM

        |                    |

        v                    v

 Vector Database       Ollama/OpenAI

```

---

# Step 1 — Install Dependencies

Create:

```
requirements.txt
```

Content:

```txt
chromadb>=1.0.0
sentence-transformers>=3.0.0
openai>=1.95.0
python-dotenv>=1.1.0
requests>=2.32.0
```

Install:

```bash
pip install -r requirements.txt
```

---

# Step 2 — Create Knowledge Base

Create:

```
documents/company_policy.txt
```

Content:

```text
Company Vacation Policy

Employees receive 20 vacation days per year.

Unused vacation days can be carried over for up to 5 days.

Employees must request vacation at least two weeks in advance.

Remote work is allowed three days per week.

Employees receive health insurance after completing three months of employment.
```

---

# Step 3 — Configuration

Create:

```
config.py
```

```python
from dotenv import load_dotenv
import os


load_dotenv()


LLM_PROVIDER = os.getenv(
    "LLM_PROVIDER",
    "ollama"
)


OLLAMA_URL = os.getenv(
    "OLLAMA_URL",
    "http://localhost:11434"
)


OLLAMA_MODEL = os.getenv(
    "OLLAMA_MODEL",
    "llama3.2:3b"
)


OPENAI_API_KEY = os.getenv(
    "OPENAI_API_KEY"
)
```

---

# Step 4 — Embedding Module

Create:

```
embeddings.py
```

```python
from sentence_transformers import SentenceTransformer


class EmbeddingModel:


    def __init__(self):

        self.model = SentenceTransformer(
            "all-MiniLM-L6-v2"
        )


    def create_embedding(self, text):

        return self.model.encode(
            text
        ).tolist()
```

---

# Step 5 — Vector Store

Create:

```
vector_store.py
```

```python
import chromadb


class VectorStore:


    def __init__(self):

        client = chromadb.PersistentClient(
            path="./rag_database"
        )


        self.collection = (
            client.get_or_create_collection(
                "company_docs"
            )
        )


    def add_document(
        self,
        text,
        embedding
    ):

        self.collection.add(
            documents=[text],
            embeddings=[embedding],
            ids=["policy"]
        )


    def search(
        self,
        embedding,
        limit=3
    ):

        return self.collection.query(
            query_embeddings=[
                embedding
            ],
            n_results=limit
        )
```

---

# Step 6 — Retriever

Create:

```
retriever.py
```

```python
from embeddings import EmbeddingModel
from vector_store import VectorStore



class Retriever:


    def __init__(self):

        self.embedding = EmbeddingModel()

        self.database = VectorStore()



    def retrieve(self, question):

        vector = (
            self.embedding
            .create_embedding(question)
        )


        results = self.database.search(
            vector
        )


        return results["documents"][0]
```

---

# Step 7 — LLM Module

Create:

```
llm.py
```

```python
import requests

from config import (
    OLLAMA_URL,
    OLLAMA_MODEL
)



class LLM:


    def generate(self, prompt):

        response = requests.post(

            f"{OLLAMA_URL}/api/chat",

            json={

                "model": OLLAMA_MODEL,

                "stream": False,

                "messages":[

                    {
                        "role":"user",
                        "content":prompt
                    }

                ]

            }

        )


        return (
            response
            .json()
            ["message"]
            ["content"]
        )
```

---

# Step 8 — RAG Pipeline

Create:

```
rag_pipeline.py
```

```python
from retriever import Retriever
from llm import LLM



class RAGPipeline:


    def __init__(self):

        self.retriever = Retriever()

        self.llm = LLM()



    def answer(self, question):

        documents = (
            self.retriever
            .retrieve(question)
        )


        context = "\n".join(
            documents
        )


        prompt = f"""
You are a helpful assistant.

Answer only using the context.

Context:

{context}


Question:

{question}

"""


        return self.llm.generate(
            prompt
        )
```

---

# Step 9 — Main Application

Create:

```
main.py
```

```python
from rag_pipeline import RAGPipeline


def main():

    rag = RAGPipeline()


    while True:

        question = input(
            "\nQuestion:\n> "
        )


        if question == "quit":
            break


        answer = rag.answer(
            question
        )


        print(
            "\nAnswer:"
        )

        print(answer)



if __name__ == "__main__":
    main()
```

---

# Step 10 — Build the Knowledge Base

Before running the chatbot, add the document.

Create:

```
load_documents.py
```

```python
from embeddings import EmbeddingModel
from vector_store import VectorStore


text = open(
    "documents/company_policy.txt"
).read()


embedding = EmbeddingModel()


db = VectorStore()


db.add_document(
    text,
    embedding.create_embedding(text)
)


print(
    "Document indexed."
)
```

Run:

```bash
python load_documents.py
```

---

# Test RAG

Run:

```bash
python main.py
```

Ask:

```
How many vacation days do employees receive?
```

Expected:

```
Employees receive 20 vacation days per year.
```

Ask:

```
What is the company's policy about remote work?
```

Expected:

```
Remote work is allowed three days per week.
```

---

# What We Built

You now have a complete RAG system:

```text
                 Document

                    |
                    v

              Embedding Model

                    |
                    v

             Vector Database


                    ^


Question ----> Retriever


                    |

                    v


              Context + Question


                    |

                    v


                   LLM


                    |

                    v


                  Answer
```

---

# Exercise 1

Create a second document:

```
documents/product_manual.txt
```

Example:

```
The product supports WiFi 6.

Battery life is 12 hours.

The device includes a two-year warranty.
```

Modify the loader to index multiple documents.

Test:

```
How long is the warranty?
```

---

# Lesson 5 Questions

Answer:

### 1. Why does RAG reduce hallucination?

---

### 2. What is the difference between:

```
LLM knowledge
```

and

```
Retrieved knowledge
```

---

### 3. Where does the vector database fit in the RAG pipeline?

---

# Lesson 5 Outcome

After this lesson:

✅ You understand RAG architecture
✅ You built a document question-answering system
✅ You connected embeddings + vector database + LLM
✅ You created your first AI assistant

---

Next:

# Lesson 6 — Prompt Engineering

We will learn how to control the LLM:

* System prompts
* User prompts
* Few-shot prompting
* Chain-of-thought concepts
* Structured outputs
* Reliable AI responses

This is where we make our RAG assistant much smarter. 🚀
