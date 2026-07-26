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