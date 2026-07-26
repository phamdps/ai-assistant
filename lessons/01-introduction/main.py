from llm_client import LLMClient
from prompts import SYSTEM_PROMPT


def main():

    print("=" * 60)
    print("Lesson 01 - Introduction to LLMs")
    print("=" * 60)

    client = LLMClient()

    while True:

        question = input("\nAsk a question ('quit' to exit):\n> ")

        if question.lower() == "quit":
            break

        try:

            answer = client.chat(
                SYSTEM_PROMPT,
                question,
            )

            print("\nAssistant:\n")
            print(answer)

        except Exception as e:

            print(f"\nError:\n{e}")


if __name__ == "__main__":
    main()