# ResearchPeer

ResearchPeer is a Multi Agent AI application built using LangChain, Streamlit and Mistral AI. It combines an Action Based Agent with a Retrieval Augmented Generation (RAG) Agent, allowing users to either perform intelligent web research or ask questions directly from their own PDF documents.

The goal of this project was to understand how multiple AI agents can collaborate to solve different types of user queries while keeping the architecture modular and scalable.

## Features

### Research Agent

Performs end to end web research using multiple AI agents.

Workflow

User Query

↓

Search Agent

↓

Reader Agent

↓

Writer Chain

↓

Critic Chain

The Research Agent

Searches the web for recent information

Extracts detailed content from relevant sources

Generates a structured research report

Reviews and evaluates the generated report

Provides downloadable research output

## Document Intelligence Agent

The RAG Agent allows users to upload their own PDF and ask questions from it.

Workflow

Upload PDF

↓

Document Loader

↓

Text Splitter

↓

Embedding Model

↓

Chroma Vector Database

↓

Retriever

↓

Mistral LLM

↓

Answer Generation

The model only answers using information available inside the uploaded document.

## Tech Stack

Frontend

Streamlit

Backend

Python

LangChain

Mistral AI

Vector Database

ChromaDB

Embeddings

HuggingFace Sentence Transformers

Search

Tavily Search API

Document Processing

PyPDF

BeautifulSoup

Requests

## Project Structure

```
project/

app.py

agents.py

pipeline.py

rag.py

rag_pipeline.py

tools.py

requirements.txt

uploads/

chroma_db/
```

## Installation

Clone the repository

```bash
git clone <repository-url>

cd ResearchPeer
```

Create a virtual environment

```bash
python -m venv .venv
```

Activate the virtual environment

Windows

```bash
.venv\Scripts\activate
```

Linux or macOS

```bash
source .venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create a `.env` file

```env
MISTRAL_API_KEY=your_api_key

TAVILY_API_KEY=your_api_key
```

Run the application

```bash
streamlit run app.py
```

## Architecture

Research Agent

```
User

↓

Search Agent

↓

Reader Agent

↓

Writer Chain

↓

Critic Chain

↓

Research Report
```

Document Intelligence Agent

```
User

↓

Upload PDF

↓

Chunking

↓

Embeddings

↓

ChromaDB

↓

Retriever

↓

Mistral AI

↓

Answer
```

## Future Improvements

Support multiple PDFs

Session specific vector databases

Conversation memory

Citation based responses

Multiple embedding model support

Cloud vector database integration

## Author

Shivang Sharma
