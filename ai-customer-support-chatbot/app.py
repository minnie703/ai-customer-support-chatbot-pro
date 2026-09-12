import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)

from flask import Flask, render_template, request

from utils.pdf_reader import extract_text
from utils.chunker import create_chunks
from utils.vector_store import store_chunks, search_chunks
from utils.chatbot import ask_llm

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload():

    pdf = request.files["pdf"]

    filepath = os.path.join(
        UPLOAD_FOLDER,
        pdf.filename
    )

    pdf.save(filepath)

    text = extract_text(filepath)

    chunks = create_chunks(text)

    store_chunks(chunks)

    return render_template(
        "index.html",
        message="✅ PDF uploaded successfully!"
    )


@app.route("/ask", methods=["POST"])
def ask():

    question = request.form["question"]

    results = search_chunks(question)

    context = "\n".join(results)

    answer = ask_llm(
        context,
        question
    )

    return render_template(
        "index.html",
        question=question,
        answer=answer
    )


if __name__ == "__main__":
    app.run(debug=True)