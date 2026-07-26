Excellent. 🎉 Lesson 2 is complete.

You have now learned the first internal layer of LLMs:

* ✅ Text is converted into tokens.
* ✅ Tokens become numerical IDs.
* ✅ LLMs predict the next token.
* ✅ Context windows limit how much information a model can process.
* ✅ Temperature controls randomness.

Now we move to one of the most important concepts in modern AI applications:

# Lesson 3 — Embeddings

## Learning Goal

In Lesson 2 we learned:

> How an LLM processes text.

Now we learn:

> How a computer can understand the **meaning** of text.

This is the foundation for:

* Semantic search
* Recommendation systems
* Vector databases
* RAG systems
* AI assistants

---

# The Problem

Computers do not understand meaning.

For example:

Sentence A:

```
I love my dog.
```

Sentence B:

```
My puppy is amazing.
```

A human understands these are related.

But computers see:

```
I love my dog.
```

and:

```
My puppy is amazing.
```

as completely different characters.

We need a way to convert text into numbers that preserve meaning.

That is what embeddings do.

---

# What Is an Embedding?

An embedding is a numerical representation of meaning.

Example:

Text:

```
I love my dog.
```

becomes:

```
[
0.023,
-0.154,
0.821,
0.442,
...
]
```

A real embedding may contain hundreds or thousands of numbers.

The important idea:

Similar meanings → similar vectors

---

# Visual Concept

```text
                 Vector Space


              dog

               *
              / \
             /   \
            /     \


     puppy *       * kitten


                         cat


Different meanings are farther apart.
Similar meanings are closer together.
```

---

# Lesson 3 Project Structure

Create:

```text
lessons/
└── 03-embeddings/
    │
    ├── README.md
    ├── requirements.txt
    ├── embedding_demo.py
    ├── cosine_similarity.py
    ├── semantic_search.py
    │
    ├── sample_data/
    │   └── documents.txt
    │
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
numpy>=2.0.0
sentence-transformers>=3.0.0
scikit-learn>=1.5.0
```

Install:

```bash
pip install -r requirements.txt
```

---

# Step 2 — Understanding Embedding Models

We will use:

```
sentence-transformers
```

This allows us to run embedding models locally.

The model:

```
all-MiniLM-L6-v2
```

creates a vector of:

```
384 dimensions
```

Example:

Input:

```
The dog is playing.
```

Output:

```
[
0.021,
-0.034,
0.112,
...
]
```

---

# Step 3 — embedding_demo.py

Create:

```python
from sentence_transformers import SentenceTransformer


def main():

    model = SentenceTransformer(
        "all-MiniLM-L6-v2"
    )


    sentences = [
        "I love my dog.",
        "My puppy is wonderful.",
        "The weather is sunny today."
    ]


    embeddings = model.encode(
        sentences
    )


    for sentence, vector in zip(
        sentences,
        embeddings
    ):

        print("=" * 60)

        print("Text:")
        print(sentence)

        print()

        print("Vector size:")
        print(len(vector))

        print()

        print("First 10 values:")
        print(vector[:10])


if __name__ == "__main__":
    main()
```

Run:

```bash
python embedding_demo.py
```

Example output:

```
Text:
I love my dog.

Vector size:
384

First 10 values:

[
0.021,
-0.045,
0.112,
...
]
```

---

# Step 4 — Measuring Similarity

Now we have vectors.

How do we compare them?

We use:

## Cosine Similarity

The idea:

```
Same direction = similar meaning

Different direction = different meaning
```

Example:

```
        Vector A

          *
         /
        /
       /
      *

Vector B


Angle is small
=
high similarity
```

---

# cosine_similarity.py

Create:

```python
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


def main():

    model = SentenceTransformer(
        "all-MiniLM-L6-v2"
    )


    sentences = [
        "I love my dog.",
        "My puppy is amazing.",
        "I enjoy programming."
    ]


    vectors = model.encode(
        sentences
    )


    similarity = cosine_similarity(
        vectors
    )


    print(similarity)


if __name__ == "__main__":
    main()
```

---

Expected output:

```
[
[1.00, 0.75, 0.20],
[0.75, 1.00, 0.18],
[0.20, 0.18, 1.00]
]
```

Meaning:

```
I love my dog.
        |
        |
My puppy is amazing.

are semantically close.
```

---

# Step 5 — Semantic Search

Now we build the first version of search.

Traditional search:

```
keyword matching
```

Example:

Query:

```
car
```

Find:

```
car
```

but maybe misses:

```
automobile
vehicle
```

---

Embedding search:

Query:

```
car
```

Finds:

```
automobile
vehicle
transportation
```

because the meanings are close.

---

# sample_data/documents.txt

Create:

```
Python is a programming language.

Machine learning allows computers to learn from data.

Dogs are popular household pets.

The Earth revolves around the Sun.

Artificial intelligence is changing technology.
```

---

# semantic_search.py

```python
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


def main():

    model = SentenceTransformer(
        "all-MiniLM-L6-v2"
    )


    documents = [
        "Python is a programming language.",
        "Machine learning learns from data.",
        "Dogs are common pets.",
        "The Earth revolves around the Sun.",
        "Artificial intelligence changes technology."
    ]


    query = (
        "How computers learn automatically"
    )


    doc_vectors = model.encode(
        documents
    )

    query_vector = model.encode(
        [query]
    )


    scores = cosine_similarity(
        query_vector,
        doc_vectors
    )[0]


    results = sorted(
        zip(documents, scores),
        key=lambda x: x[1],
        reverse=True
    )


    print("Query:")
    print(query)

    print("\nResults:")

    for doc, score in results:

        print(
            f"{score:.3f} -> {doc}"
        )


if __name__ == "__main__":
    main()
```

---

Example output:

```
Query:
How computers learn automatically


Results:

0.82 -> Machine learning learns from data.
0.70 -> Artificial intelligence changes technology.
0.25 -> Python is a programming language.
```

---

# Exercise 1

Create:

```
exercises/exercise1.py
```

Task:

Create a semantic similarity tester.

Input:

```
Sentence 1:
I like cats

Sentence 2:
I love kittens
```

Output:

```
Similarity:
0.82
```

---

# Exercise Questions

Answer these:

### Question 1

Why is this useful?

```
Text
 ↓
Embedding
 ↓
Vector
```

---

### Question 2

Why can't we simply compare words?

Example:

```
car
automobile
```

---

### Question 3

What happens if two sentences have similar meaning but different words?

---

# Lesson 3 Outcome

After this lesson you understand:

✅ What embeddings are
✅ How text becomes vectors
✅ Vector dimensions
✅ Semantic similarity
✅ Cosine similarity
✅ Semantic search

---

## Connection to the next lessons

Now we have:

```
Lesson 2
LLM understands tokens

        +

Lesson 3
Text becomes vectors

        ↓

Lesson 4
Store and search vectors efficiently
```

Next:

# Lesson 4 — Vector Databases

We will build our first real knowledge retrieval system using:

* ChromaDB
* Vector storage
* Similarity search
* Document indexing

This is the direct foundation of RAG.
