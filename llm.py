from ollama import ChatResponse, chat


def query(prompt: str) -> str:
    response: ChatResponse = chat(
        model="llama3.2",
        messages=[
            {
                "role": "user",
                "content": prompt,
            },
        ],
    )
    return response.message.content
