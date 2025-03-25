from ollama import ChatResponse, chat


def query(prompt: str, model="llama3.2") -> str | None:
    response: ChatResponse = chat(
        model=model,
        messages=[
            {
                "role": "user",
                "content": prompt,
            },
        ],
    )

    return response.message.content


def mock_data():
    context = """
    If you’re on the hunt for a standout kopitiam in KL,  Selangor, Penang, or Johor (JB), look no further than Oriental Kopi. Our kopitiam offers a unique blend of traditional and modern flavours, ensuring a memorable experience with every visit.

    At Oriental Kopi, we pride ourselves on serving exceptional coffee and delightful homemade traditional toast in a welcoming atmosphere. Our kopitiam provides a cosy retreat to enjoy expertly brewed beverages and freshly prepared treats. From rich, aromatic coffees to delicious local pastries, we deliver a taste of excellence and comfort.

    Come and visit our Penang, Johor, Selangor, or KL kopitiam today!
    """
    context = context.strip()
    query = "Where can I find the kopitiam?"
    prompt = """
    You are a helpful AI assistant.
    You provide relevant answers based on the given context:

    ---
    {context}
    ---

    Answer only from the given context. Otherwise, say you don't know.
    Question: {question}
    Answer:
    """
    output = "You can find Oriental Kopi in KL, Selangor, Penang, or Johor (JB)."

    return query, context, prompt.format(question=query, context=context), output
