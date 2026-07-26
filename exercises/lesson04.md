Excellent. 🎉 Lesson 3 is complete.

You now understand one of the most important concepts in modern AI systems:

* ✅ Text can be converted into vectors.
* ✅ Similar meanings create similar vectors.
* ✅ Embeddings allow semantic search.
* ✅ We can compare meaning instead of exact words.

Now we move to the next layer:

# Lesson 4 — Vector Databases

## Learning Goal

In Lesson 3, we created embeddings.

We had:

```text
Document
    |
    v
Embedding Model
    |
    v
Vector
```

But we only stored vectors temporarily in memory.

Real AI applications need to store **millions or billions of vectors** and search them efficiently.

That is the job of a **Vector Database**.

---

# Why Do We Need Vector Databases?

Imagine a company has:

```
10,000 PDF documents

100,000 pages

millions of text chunks
```

A normal database search:

```sql
SELECT *
FROM documents
WHERE text LIKE '%machine learning%';
```

only finds exact words.

Problem:

User asks:

```
How do computers learn automatically?
```

Document says:

```
Machine learning allows systems to learn from examples.
```

Keyword search may fail.

---

A vector database searches by meaning:

```
User Question

      |
      v

Embedding

      |
      v

Vector Search

      |
      v

Similar Documents
```

---

# Vector Database Architecture

Visual model:

```text
                 Documents

                     |
                     v

              Text Chunking

                     |
                     v

             Embedding Model

                     |
                     v

              Vector Database

        +------------------------+
        |                        |
        |  Vector                |
        |  Metadata              |
        |  Original Text         |
        |                        |
        +------------------------+


                     ^
                     |
                User Query

                     |
                     v

             Similarity Search
```

---

# Lesson 4 Project Structure

Create:

```text
lessons/
└── 04-vector-databases/
    |
    ├── README.md
    ├── requirements.txt
    ├── build_vector_db.py
    ├── search.py
    ├── database.py
    |
    ├── sample_data/
    │   └── documents.txt
    |
    ├── chroma_db/
    |
    └── exercises/
        └── exercise1.py
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
```

Install:

```bash
pip install -r requirements.txt
```

---

# Step 2 — Understanding ChromaDB

We will use:

Chroma

It provides:

* Vector storage
* Similarity search
* Metadata storage
* Local persistence

Our flow:

```
Text

↓

Embedding Model

↓

ChromaDB

↓

Search
```

---

# Step 3 — Create Sample Documents

Create:

```
sample_data/documents.txt
```

Content:

```text
Python is a popular programming language used for software development.

Machine learning allows computers to learn patterns from data.

Artificial intelligence enables machines to perform tasks that normally require human intelligence.

Vector databases store numerical representations of information.

Large language models generate text by predicting the next token.
```

---

# Step 4 — Create Database Helper

Create:

```
database.py
```

Code:

```python
import chromadb


DB_PATH = "./chroma_db"


def get_database():

    client = chromadb.PersistentClient(
        path=DB_PATH
    )

    collection = client.get_or_create_collection(
        name="documents"
    )

    return collection
```

---

# Step 5 — Build Vector Database

Create:

```
build_vector_db.py
```

Code:

```python
from sentence_transformers import SentenceTransformer

from database import get_database


def load_documents():

    with open(
        "sample_data/documents.txt",
        "r"
    ) as file:

        text = file.read()

    documents = [
        line.strip()
        for line in text.split("\n")
        if line.strip()
    ]

    return documents



def main():

    print("Loading embedding model...")

    model = SentenceTransformer(
        "all-MiniLM-L6-v2"
    )


    documents = load_documents()


    embeddings = model.encode(
        documents
    )


    collection = get_database()


    collection.add(
        documents=documents,

        embeddings=[
            embedding.tolist()
            for embedding in embeddings
        ],

        ids=[
            str(i)
            for i in range(len(documents))
        ]
    )


    print(
        "Vector database created!"
    )


if __name__ == "__main__":
    main()
```

---

# Run

From:

```
04-vector-databases/
```

run:

```bash
python build_vector_db.py
```

Expected:

```
Loading embedding model...

Vector database created!
```

You should now see:

```
chroma_db/
```

created.

---

# Step 6 — Search the Vector Database

Create:

```
search.py
```

Code:

```python
from sentence_transformers import SentenceTransformer

from database import get_database



def main():

    model = SentenceTransformer(
        "all-MiniLM-L6-v2"
    )


    collection = get_database()


    query = input(
        "Ask a question:\n> "
    )


    query_embedding = model.encode(
        query
    )


    results = collection.query(

        query_embeddings=[
            query_embedding.tolist()
        ],

        n_results=3
    )


    print("\nResults:\n")


    for document in results["documents"][0]:

        print("- " + document)



if __name__ == "__main__":
    main()
```

---

# Test It

Run:

```bash
python search.py
```

Question:

```
How do computers learn?
```

Output:

```
- Machine learning allows computers to learn patterns from data.

- Artificial intelligence enables machines to perform tasks that normally require human intelligence.
```

---

# What Just Happened?

You created your first retrieval system:

```
Question

↓

Embedding

↓

Vector Database Search

↓

Relevant Documents
```

This is the retrieval part of RAG.

---

# Exercise 1

Create:

```
exercises/exercise1.py
```

Goal:

Add more documents.

Example:

```python
documents = [
    "Docker packages applications into containers.",
    "FastAPI is a Python web framework.",
    "PostgreSQL is a relational database."
]
```

Then:

1. Insert them into ChromaDB.
2. Search:

```
How do I create APIs in Python?
```

Observe which document is retrieved.

---

# Exercise Questions

## Question 1

Why can't we store only the original text?

---

## Question 2

What information does a vector database usually store?

Answer:

```
Vector
+
Original Text
+
Metadata
```

---

## Question 3

What is the difference between:

Traditional database:

```
exact match
```

and:

Vector database:

```
semantic similarity
```

---

# Lesson 4 Outcome

After this lesson you understand:

✅ What vector databases are
✅ Why embeddings are stored
✅ ChromaDB basics
✅ Vector indexing
✅ Similarity search
✅ Semantic retrieval

---

# Connection to Lesson 5

Now we have:

```
Lesson 2
LLM generates answers

        +

Lesson 3
Embeddings represent meaning

        +

Lesson 4
Vector database retrieves knowledge


        ↓


Lesson 5
RAG combines everything
```

Next lesson:

# Lesson 5 — Retrieval-Augmented Generation (RAG)

We will build the complete pipeline:

```
User Question

      ↓

Embedding

      ↓

Vector Database

      ↓

Relevant Documents

      ↓

Prompt Construction

      ↓

LLM

      ↓

Final Answer
```

This is where everything starts becoming a real AI assistant. 🚀
