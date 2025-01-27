from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    openrouter_api_key: str
    openai_api_key: str
    embedding_model: str = "text-embedding-3-small"
    chunk_size: int = 1024  # Experiment with this
    chunk_overlap: int = 128
    n_retrievals: int = 3
    openrouter_model: str = "meta-llama/llama-3.2-3b-instruct" # or meta-llama/llama-3.3-70b-instruct as a larger model
    
    class Config:
        env_file = ".env"