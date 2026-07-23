from ollama import chat

MODEL = "qwen3:8b"


def ask(system_prompt: str, user_prompt: str):

    response = chat(
        model=MODEL,
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
        format="json",
    )

    return response.message.content