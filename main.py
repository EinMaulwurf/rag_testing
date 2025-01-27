from config.settings import Settings
from data_processing.document_loader import DocumentLoader
from data_processing.vector_store import VectorStore
from rag.model import OpenRouterLLM
from rag.query import RAGPipeline

def main():
    config = Settings()
    # Initialize components
    loader = DocumentLoader()
    vector_store = VectorStore(config)
    llm = OpenRouterLLM(config)
    pipeline = RAGPipeline(vector_store, llm)
    
    # Load documents
    text = loader.load_file("Documents/example.pdf")
    chunks = loader.chunk_text(text, config)
    vector_store.add_documents(chunks)
    
    # Query loop
    while True:
        question = input("Your question: ")
        print(pipeline.query(question))

if __name__ == "__main__":
    main()