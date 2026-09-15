from sentence_transformers import SentenceTransformer

from src.config import EMBEDDING_MODEL


# Embedding model load karo
model = SentenceTransformer(EMBEDDING_MODEL)


def create_embeddings(chunks):
    """
    Chunks ke liye embeddings generate karta hai.
    """

    texts = [chunk["text"] for chunk in chunks]

    embeddings = model.encode(
        texts,
        normalize_embeddings=True
    )

    return embeddings