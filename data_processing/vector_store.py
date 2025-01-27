from chromadb import PersistentClient
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings
from config.settings import Settings

class VectorStore:
    def __init__(self, config: Settings):
        self.embeddings = OpenAIEmbeddings(
            model=config.embedding_model,
            openai_api_key=config.openai_api_key
        )
        self.client = Chroma(
            collection_name="docs",
            embedding_function=self.embeddings,
            client=PersistentClient(path="./chroma_db")
        )
    
    def add_documents(self, chunks: list[str]):
        self.client.add_texts(chunks)
    
    def retrieve(self, query: str) -> list[str]:
        results = self.client.similarity_search(query, k=self.config.n_retrievals)
        return [doc.page_content for doc in results]