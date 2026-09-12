from utils.pdf_reader import extract_text
from utils.chunker import create_chunks
from utils.vector_store import store_chunks
from utils.vector_store import search_chunks

print("Reading PDF...")

text = extract_text("uploads/sample_resume.pdf")

print("Creating chunks...")

chunks = create_chunks(text)

print("Storing chunks...")

store_chunks(chunks)

print("Searching...")

results = search_chunks(
    "What is attention?"
)

print(results)