"""
Exercise 1

Experiment with System Prompts.

Try changing the AI's role and observe how
the answers change.
"""

from llm_client import LLMClient

client = LLMClient()

roles = [
    "You are a Python instructor.",
    "You are a Linux system administrator.",
    "You are a database expert.",
    "You are a cybersecurity consultant.",
]

question = "Explain what an API is."

for role in roles:

    print("=" * 70)
    print(role)
    print("=" * 70)

    answer = client.chat(role, question)

    print(answer)
    print()