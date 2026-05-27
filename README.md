# AI PDF Question Answering Assistant

An AI-powered Retrieval-Augmented Generation (RAG) application that allows users to upload PDFs and ask intelligent questions about document content.

## Features

- Upload PDF documents
- Ask questions from PDFs
- AI-generated answers
- Semantic search using embeddings
- FAISS vector database
- Streamlit web interface

## Tech Stack

- Python
- Streamlit
- LangChain
- FAISS
- Sentence Transformers
- OpenRouter API

## Project Architecture

PDF → Text Extraction → Chunking → Embeddings → FAISS → Retrieval → LLM Response

## Run Locally

```bash
pip install -r requirements.txt
python -m streamlit run app.py
