import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)

from utils.vector_store import search_chunks
from utils.chatbot import ask_llm

question = input("Ask a question: ")

results = search_chunks(question)

context = "\n".join(results)

answer = ask_llm(context, question)

print("\nANSWER:\n")
print(answer)