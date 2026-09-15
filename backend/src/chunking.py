from src.config import CHUNK_SIZE, CHUNK_OVERLAP


def create_chunks(documents):
    """
    Documents ko overlapping text chunks mein divide karta hai.
    """

    chunks = []

    for document in documents:
        text = document["text"]

        start = 0

        while start < len(text):

            end = start + CHUNK_SIZE

            chunk_text = text[start:end].strip()

            if chunk_text:
                chunks.append(
                    {
                        "text": chunk_text,
                        "source": document["source"],
                        "page": document["page"],
                    }
                )

            start += CHUNK_SIZE - CHUNK_OVERLAP

    print(f"Created {len(chunks)} chunks.")

    return chunks