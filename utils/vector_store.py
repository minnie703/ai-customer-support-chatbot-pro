import chromadb

client = chromadb.PersistentClient(path="chroma_db")

collection = client.get_or_create_collection(
    name="documents"
)

def store_chunks(chunks):
    ids = [str(i) for i in range(len(chunks))]

    collection.add(
        documents=chunks,
        ids=ids
    )

def search_chunks(query, n_results=3):
    results = collection.query(
        query_texts=[query],
        n_results=n_results
    )

    return results["documents"][0]