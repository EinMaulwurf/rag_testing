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

Currently, only one file can be processed at a time. The file path is hardcoded in `main.py`.

## Usage

Run the main script:
```bash
python main.py
```

When prompted for a question, enter a query. With the attached example, you could try `What was the design of study S1?`.

Note that no "conversation" is being created, so every message is treated as a new query with no context from previous messages.

## Current Implementation

The system currently:
1. Loads a document from `documents/example.pdf`. This is a very recent paper ([arXiv](https://doi.org/10.48550/arXiv.2501.13228)) and therefore not in the training data of any LLM.
2. Processes the document and creates embeddings
3. Stores embeddings in a Chroma vector database
4. Uses RAG to augment LLM responses with relevant document context

## Limitations & TODOs

- The entire document processing pipeline runs on every execution. This could be optimized to only process new or changed documents.
- Add functionality to directly compare responses from different models for the same query to better evaluate performance differences.
- Create a conversational context where previous messages are considered in the current query.
- Handle multiple documents.
