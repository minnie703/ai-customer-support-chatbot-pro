import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)

from flask import Flask, render_template, request

from utils.vector_store import search_chunks
from utils.chatbot import ask_llm

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/ask", methods=["POST"])
def ask():

    question = request.form["question"]

    results = search_chunks(question)

    context = "\n".join(results)

    answer = ask_llm(context, question)

    return render_template(
        "index.html",
        question=question,
        answer=answer
    )


if __name__ == "__main__":
    app.run(debug=True)