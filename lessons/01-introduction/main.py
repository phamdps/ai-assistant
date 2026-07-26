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