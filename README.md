# Document RAG Assistant

This project implements a Retrieval-Augmented Generation (RAG) system to enhance LLM responses with document context. One of the main goals is to evaluate how smaller language models perform compared to larger ones when augmented with RAG capabilities for document querying tasks.

## Setup

1. Clone the repository
2. Create a virtual environment and install dependencies:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```
3. Create a `.env` file based on `.env.example` and add your API keys:
   - OpenRouter API key (for LLM access)
   - OpenAI API key (for embeddings)

## Configuration

Most relevant settings can be configured in `config/settings.py`, including:
- LLM model selection
- Number of retrievals for RAG
- Other RAG parameters

## Usage

Run the main script:
```bash
python main.py
```

You can then query the attached document. Note that no "conversation" is being created, so every message is treated as a new query with no context from previous messages.

## Current Implementation

The system currently:
1. Loads documents from `documents/Bachelorthesis.pdf`
2. Processes the document and creates embeddings
3. Stores embeddings in a Chroma vector database
4. Uses RAG to augment LLM responses with relevant document context

## Limitations & TODOs

- The entire document processing pipeline runs on every execution. This could be optimized to only process new or changed documents.
- Add functionality to directly compare responses from different models for the same query to better evaluate performance differences.
- Create a conversational context where previous messages are considered in the current query.
