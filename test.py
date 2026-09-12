from utils.pdf_reader import extract_text

text = extract_text("uploads/sample_resume.pdf")

print("TEXT LENGTH:", len(text))
print()
print(text[:500])