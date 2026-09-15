from pathlib import Path


# Project root directory
BASE_DIR = Path(__file__).resolve().parent.parent


# Data directories
DATA_DIR = BASE_DIR / "data"
DOCUMENTS_DIR = DATA_DIR / "documents"


# Vector database
CHROMA_DIR = BASE_DIR / "chroma_db"
COLLECTION_NAME = "rag_documents"


# Embedding model
EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"


# Local LLM
LLM_MODEL = "llama3.2:1b"

# Chunking settings
CHUNK_SIZE = 500
CHUNK_OVERLAP = 50


# Retrieval settings
TOP_K = 2