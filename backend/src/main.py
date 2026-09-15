from retrieval import retrieve_documents
from generation import generate_answer


def run_rag():
    print("\n===== RAG Question Answering System =====")

    query = input("\nEnter your question: ")

    # Step 1: Relevant documents retrieve karo
    results = retrieve_documents(query, top_k=2)

    retrieved_documents = results["documents"][0]

    # Step 2: Retrieved context se answer generate karo
    answer = generate_answer(
        query,
        retrieved_documents
    )

    print("\n===== Final Answer =====")
    print(answer)


if __name__ == "__main__":
    run_rag()