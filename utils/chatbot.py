import ollama

def ask_llm(context, question):

    prompt = f"""
You are a helpful customer support assistant.

Use ONLY the context below to answer.

Context:
{context}

Question:
{question}

Answer:
"""

    response = ollama.chat(
        model="llama3.2",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]