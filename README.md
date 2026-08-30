# Retrieval-Augmented Generation (RAG) Project

A Python-based Retrieval-Augmented Generation (RAG) system that reads information from PDF documents, creates embeddings, stores them in ChromaDB, retrieves relevant document chunks, and generates answers using a local Llama 3.2 1B language model.

## Project Overview

This project implements a complete RAG pipeline:

PDF Document
↓
Document Ingestion
↓
Text Chunking
↓
Embedding Generation
↓
Vector Storage
↓
Semantic Retrieval
↓
Local LLM Generation
↓
Final Answer

## Technologies Used

- Python
- PyPDF
- Sentence Transformers
- ChromaDB
- Ollama
- Llama 3.2 1B
- python-dotenv

## Project Structure

RAG_Project/
│
├── .env
├── .gitignore
├── README.md
├── requirements.txt
│
├── data/
│   └── documents/
│       └── sample.pdf
│
├── chroma_db/
│
└── src/
    ├── config.py
    ├── ingestion.py
    ├── chunking.py
    ├── embeddings.py
    ├── vector_store.py
    ├── retrieval.py
    ├── generation.py
    └── main.py
