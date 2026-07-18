from pathlib import Path

from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document
from embeddings.embed import EmbeddingService
class FaissVector:
    def __init__(self,index_path:str="data/faiss_store"):
      self.index_path=Path(index_path)
      self.embedding=EmbeddingService().model
      self.vector_store=None
    def create(
        self,
        documents:list[Document]
    ):
        if self.index_path.exists():
              self.load()
              self.vector_store.add_documents(documents)
        else:
             self.vector_store = FAISS.from_documents(
            documents=documents,
            embedding=self.embedding
        )
        self.save()
        return self.vector_store
    def save(self):
        if self.vector_store is None:
            raise ValueError(
                "No "
            )
        self.index_path.mkdir(
            parents=True,
            exist_ok=True
            )
        self.vector_store.save_local(
            str(self.index_path)
            )
    def load(self):
        if not self.index_path.exists():
            raise FileNotFoundError(f"faise index not found at {self.index_path}")
        self.vector_store=FAISS.load_local(
            folder_path=str(self.index_path),
            embeddings=self.embedding,
            allow_dangerous_deserialization=True
            
        )
        return self.vector_store
   
    def get_store(self):
        if self.vector_store is None:
            self.load()
        return self.vector_store
    

    def delete_document(self,document_id):
        self.load()
        all_documents = list(self.vector_store.docstore._dict.values())
        remaining_documents = [doc for doc in all_documents if doc.metadata.get("document_id") != document_id]
        if len(remaining_documents) == 0:
            self.vector_store = None
            return
        self.vector_store = FAISS.from_documents(
            documents=remaining_documents,
            embedding=self.embedding
        )
        self.save()
        print(f"Deleted document {document_id} from FAISS.")
    

    
    
   

