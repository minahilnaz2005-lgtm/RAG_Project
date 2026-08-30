from pathlib import Path

import chromadb

from config import CHROMA_DIR, COLLECTION_NAME, TOP_K
from embeddings import model


# Persistent ChromaDB client
client = chromadb.PersistentClient(
    path=str(CHROMA_DIR)
)

collection = client.get_or_create_collection(
    name=COLLECTION_NAME
)


def retrieve_documents(query, top_k=TOP_K):
    """
    User query ke liye most relevant document chunks retrieve karta hai.
    """

    # Query ki embedding generate karo
    query_embedding = model.encode(
        query,
        normalize_embeddings=True
    ).tolist()

    # ChromaDB se similar chunks retrieve karo
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k
    )

    return results


if __name__ == "__main__":

    query = input("\nEnter your question: ")

    results = retrieve_documents(query)

    print("\n===== Retrieved Context =====")

    for index, document in enumerate(
        results["documents"][0],
        start=1
    ):

        metadata = results["metadatas"][0][index - 1]

        print(f"\n--- Result {index} ---")
        print(f"Source: {metadata['source']}")
        print(f"Page: {metadata['page']}")
        print(f"Text:\n{document}")