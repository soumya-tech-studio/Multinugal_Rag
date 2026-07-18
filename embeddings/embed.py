from langchain_huggingface import HuggingFaceEmbeddings
class EmbeddingService:
    def __init__(self):
        self.model= HuggingFaceEmbeddings(
            model_name="intfloat/multilingual-e5-base"
        )
    def embed_text(self,query):
        return self.model.embed_query(query)
    def embed_documents(self,chunks):
        return self.model.embed_documents(chunks)
    
        
        
    