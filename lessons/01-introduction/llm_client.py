import requests

from openai import OpenAI

from config import (
    LLM_PROVIDER,
    OPENAI_API_KEY,
    OPENAI_MODEL,
    OLLAMA_MODEL,
    OLLAMA_URL,
)


class LLMClient:

    def __init__(self):

        if LLM_PROVIDER == "openai":

            if not OPENAI_API_KEY:
                raise ValueError("OPENAI_API_KEY not configured.")

            self.client = OpenAI(api_key=OPENAI_API_KEY)

    def chat(self, system_prompt: str, user_prompt: str):

        if LLM_PROVIDER == "openai":

            response = self.client.chat.completions.create(
                model=OPENAI_MODEL,
                temperature=0.7,
                messages=[
                    {
                        "role": "system",
                        "content": system_prompt,
                    },
                    {
                        "role": "user",
                        "content": user_prompt,
                    },
                ],
            )

            return response.choices[0].message.content

        payload = {
            "model": OLLAMA_MODEL,
            "stream": False,
            "messages": [
                {
                    "role": "system",
                    "content": system_prompt,
                },
                {
                    "role": "user",
                    "content": user_prompt,
                },
            ],
        }

        response = requests.post(
            f"{OLLAMA_URL}/api/chat",
            json=payload,
            timeout=120,
        )

        response.raise_for_status()

        return response.json()["message"]["content"]