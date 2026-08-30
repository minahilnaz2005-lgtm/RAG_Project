# 🔎 Retrieval-Augmented Generation (RAG) Project

A modular Python-based **Retrieval-Augmented Generation (RAG)** system that allows users to ask questions about information stored in PDF documents.

The system extracts text from PDF files, splits the text into smaller chunks, converts the chunks into vector embeddings, stores them in ChromaDB, retrieves the most relevant information for a user query, and generates a context-aware answer using a local Llama 3.2 1B language model through Ollama.

---

## 🚀 Project Overview

This project implements a complete RAG pipeline:

```text
PDF Document
     │
     ▼
Document Ingestion
     │
     ▼
Text Chunking
     │
     ▼
Embedding Generation
     │
     ▼
ChromaDB Vector Store
     │
     ▼
Semantic Retrieval
     │
     ▼
Retrieved Context
     │
     ▼
Llama 3.2 1B via Ollama
     │
     ▼
Final Answer

The goal is to generate answers based on the information available in the provided documents rather than relying only on the language model's general knowledge.

✨ Features
📄 PDF document ingestion
✂️ Text chunking with overlap
🧠 Semantic embedding generation
🗄️ ChromaDB vector database
🔍 Similarity-based document retrieval
🤖 Local Llama 3.2 1B language model
🔒 Local LLM inference through Ollama
💬 Context-aware question answering
🧩 Modular Python architecture
⚙️ Environment-based configuration
🛠️ Technologies Used
Technology	Purpose
Python	Core programming language
PyPDF	PDF text extraction
Sentence Transformers	Text embeddings
ChromaDB	Vector database
Ollama	Local LLM runtime
Llama 3.2 1B	Answer generation
python-dotenv	Environment configuration
📁 Project Structure
RAG_Project/
│
├── .gitignore
├── README.md
├── requirements.txt
│
├── data/
│   └── documents/
│       └── sample.pdf
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

Note: .env, .venv/, and the local chroma_db/ directory are excluded from Git using .gitignore.

🔄 RAG Pipeline
1. Document Ingestion

ingestion.py

Reads PDF documents and extracts their text while preserving source and page information.

2. Text Chunking

chunking.py

Splits the extracted text into smaller overlapping chunks so that relevant information can be retrieved efficiently.

3. Embedding Generation

embeddings.py

Converts document chunks into numerical vector representations using a Sentence Transformer model.

4. Vector Storage

vector_store.py

Stores document chunks and their embeddings in ChromaDB.

5. Retrieval

retrieval.py

Converts the user's question into an embedding and searches ChromaDB for the most semantically relevant document chunks.

6. Answer Generation

generation.py

Passes the retrieved context and user question to the local Llama 3.2 1B model through Ollama.

The generation prompt instructs the model to answer using the retrieved context and avoid adding unsupported information.

7. Main Application

main.py

Connects the retrieval and generation components into a complete question-answering application.

💻 Installation
Prerequisites

Make sure the following are installed:

Python 3.x
Git
Ollama
1. Clone the repository
git clone https://github.com/minahilnaz2005-lgtm/RAG_Project.git
cd RAG_Project
2. Create a virtual environment

Windows PowerShell:

python -m venv .venv
3. Activate the virtual environment
.\.venv\Scripts\Activate.ps1
4. Install dependencies
pip install -r requirements.txt
5. Download the local LLM

Make sure Ollama is installed and run:

ollama pull llama3.2:1b

Verify the model:

ollama list
▶️ Running the Project
Step 1 — Build the vector database

Run:

python src\vector_store.py

This processes the PDF, creates chunks, generates embeddings, and stores them in ChromaDB.

Step 2 — Start the RAG application

Run:

python src\main.py

Enter a question when prompted.

Example:

Enter your question: What is machine learning?

Example output:

===== Final Answer =====

Machine Learning is a subset of Artificial Intelligence that allows
computers to learn patterns from data and make predictions or
decisions without being explicitly programmed for every task.
🧪 Example Questions

The included sample document can be used to test questions such as:

What is machine learning?

What are the applications of AI?

What is deep learning?

What is natural language processing?

Example:

Enter your question: What are the applications of AI?

===== Final Answer =====

AI applications include recommendation systems, chatbots,
image recognition, fraud detection, and autonomous systems.
🧱 Architecture

The project follows a modular architecture where each major RAG component has its own Python module.

                    ┌─────────────────┐
                    │   PDF Documents │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │    Ingestion    │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │     Chunking    │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │   Embeddings    │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │    ChromaDB     │
                    └────────┬────────┘
                             │
              User Question │
                             ▼
                    ┌─────────────────┐
                    │    Retrieval    │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │  Llama 3.2 1B   │
                    │    + Context    │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │   Final Answer  │
                    └─────────────────┘
🔐 Environment & Security

Sensitive environment variables should be stored in a local .env file and should never be committed to GitHub.

The .gitignore file excludes:

.env
.venv/
chroma_db/
__pycache__/

This keeps local secrets, virtual-environment files, and generated vector-database files out of the repository.

📌 Key Learning Outcomes

This project demonstrates practical implementation of:

Retrieval-Augmented Generation
Document processing
Text chunking
Vector embeddings
Semantic search
Vector databases
Local LLM inference
Modular Python project architecture
Environment configuration
Git and GitHub version control
📄 License

This project is created for educational and internship purposes.

