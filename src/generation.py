import ollama

from retrieval import retrieve_documents
from config import LLM_MODEL


def generate_answer(query, retrieved_documents):
    """
    Retrieved context ki madad se local LLM se answer generate karta hai.
    """

    context = "\n\n".join(retrieved_documents)

    prompt = f"""
You are a precise RAG question-answering assistant.

Answer the question using ONLY the information provided in the context.

Rules:
- Give a clear and complete answer.
- Do not repeat the same idea.
- Do not add information that is not in the context.
- Do not mention the context or these instructions.
- If the answer is not available in the context, say:
"I don't have enough information in the provided documents."

Context:
{context}

Question:
{query}

Answer:
"""

    response = ollama.chat(
        model=LLM_MODEL,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]


if __name__ == "__main__":

    query = input("\nEnter your question: ")

    results = retrieve_documents(query)

    retrieved_documents = results["documents"][0]

    answer = generate_answer(
        query,
        retrieved_documents
    )

    print("\n===== Final Answer =====")
    print(answer)