import chromadb

from config import CHROMA_DIR, COLLECTION_NAME
from embeddings import create_embeddings
from ingestion import load_documents
from chunking import create_chunks


# Persistent ChromaDB client
client = chromadb.PersistentClient(
    path=str(CHROMA_DIR)
)

collection = client.get_or_create_collection(
    name=COLLECTION_NAME
)


def store_documents(chunks, embeddings):
    """
    Chunks, embeddings, and metadata ko ChromaDB mein store karta hai.
    """

    ids = [
        f"{chunk['source']}_page_{chunk['page']}_chunk_{index}"
        for index, chunk in enumerate(chunks)
    ]

    documents = [chunk["text"] for chunk in chunks]

    metadatas = [
        {
            "source": chunk["source"],
            "page": chunk["page"]
        }
        for chunk in chunks
    ]

    collection.upsert(
        ids=ids,
        documents=documents,
        embeddings=embeddings.tolist(),
        metadatas=metadatas
    )

    print(f"Stored {len(chunks)} chunks in ChromaDB.")


if __name__ == "__main__":

    documents = load_documents()

    chunks = create_chunks(documents)

    embeddings = create_embeddings(chunks)

    store_documents(chunks, embeddings)