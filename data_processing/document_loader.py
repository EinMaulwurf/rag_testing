from pathlib import Path
from PyPDF2 import PdfReader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from config.settings import Settings

class DocumentLoader:
    @staticmethod
    def load_file(path: str) -> str:
        if path.endswith(".pdf"):
            reader = PdfReader(path)
            return " ".join([page.extract_text() for page in reader.pages])
        elif path.endswith(".txt"):
            return Path(path).read_text()
    
    @classmethod
    def chunk_text(cls, text: str, config: Settings) -> list[str]:
        splitter = RecursiveCharacterTextSplitter(
            chunk_size=config.chunk_size,
            chunk_overlap=config.chunk_overlap
        )
        return splitter.split_text(text)