from utils.pdf_reader import extract_text
from utils.chunker import create_chunks

text = extract_text("uploads/sample_resume.pdf")

chunks = create_chunks(text)

print("TOTAL CHUNKS:", len(chunks))

print("\nFIRST CHUNK:\n")
print(chunks[0])