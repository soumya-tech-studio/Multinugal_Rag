#  Multilingual RAG System

## About

This project is a multilingual Retrieval-Augmented Generation (RAG) system built to answer questions from user-provided documents instead of relying only on an LLM's existing knowledge.

It supports PDF and DOCX files, extracts text (including scanned documents using OCR), splits the content into meaningful chunks, stores embeddings in a FAISS vector database, retrieves relevant information using both semantic search and BM25, reranks the retrieved results with a Cross-Encoder, and uses the retrieved context to generate more accurate responses.

The project is built with a modular architecture so that each component can be developed, tested, and improved independently.

---

## Features

- Upload and process PDF and DOCX documents
- OCR support for scanned PDFs
- Semantic Chunking
- Multilingual document support
- FAISS vector database
- Hybrid retrieval using FAISS and BM25
- Cross-Encoder reranking
- FastAPI API for interacting with the system
  



---

## Project Structure

```
Chunking/
Ingestion/
Ingestion_pipeline/
LLM_SERVICE/
Reranker/
Vector_store/
api/
watcher/
```

---

## Tech Stack

- Python
- FastAPI
- LangChain
- FAISS
- Sentence Transformers
- BM25
- PyMuPDF
- EasyOCR

---

## Getting Started

```bash
git clone https://github.com/soumya-tech-studio/Multinugal_Rag.git

cd Multinugal_Rag

pip install -r requirements.txt

uvicorn api.main:app --reload
```

---

## Future Work

Some improvements I'd like to add in the future:

- CI/CD with GitHub Actions
- more methods fo chunking
- Docker support
- Better evaluation pipeline
- Cloud deployment
- Monitoring and logging

---

## Author

**Soumya**

