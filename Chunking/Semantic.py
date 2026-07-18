from langchain_experimental.text_splitter import SemanticChunker
from langchain_huggingface import HuggingFaceEmbeddings
class SemanticChunking:
    def __init__(self):
        self.embeddings = HuggingFaceEmbeddings(
            model_name="intfloat/multilingual-e5-base"
        )
        self.chunker=SemanticChunker(
            self.embeddings
        )
    def chunk_text(self,pages):
        chunks=[]
        for page in pages:
            text=page["Content"]["text"]
            metadata=page["metadata"]
            page_chunks=self.chunker.create_documents(
                [text],
                metadatas=[metadata]
            )
            chunks.extend(page_chunks)
        return chunks

