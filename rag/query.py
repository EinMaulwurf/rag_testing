class RAGPipeline:
    def __init__(self, vector_store, llm):
        self.vector_store = vector_store
        self.llm = llm
    
    def query(self, question: str) -> str:
        context = self.vector_store.retrieve(question)
        prompt = f"Context:\n{'\n'.join(context)}\n\nQuestion: {question}\nAnswer:"
        return self.llm.generate(prompt)
