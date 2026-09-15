from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from src.retrieval import retrieve_documents
from src.generation import generate_answer


app = FastAPI(
    title="RAG Question Answering API",
    description="API for the RAG question answering system",
    version="1.0.0"
)


# Allow React frontend to communicate with the backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class QuestionRequest(BaseModel):
    question: str


@app.get("/")
def root():
    return {
        "message": "RAG API is running"
    }


@app.post("/ask")
def ask_question(request: QuestionRequest):
    query = request.question.strip()

    if not query:
        return {
            "answer": "Please enter a question."
        }

    results = retrieve_documents(query, top_k=2)

    retrieved_documents = results["documents"][0]

    answer = generate_answer(
        query,
        retrieved_documents
    )

    return {
        "question": query,
        "answer": answer
    }