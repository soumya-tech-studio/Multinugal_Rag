from langchain_classic.retrievers import EnsembleRetriever
from langchain_community.retrievers import BM25Retriever

from chunk_storage.chunks  import ChunkStorage
from Vector_store.faiss import FaissVector

class RetrieverService:
    def __init__(self):
        self.chunk_storage= ChunkStorage()
        self.vector_store=FaissVector()
    def get_reteriver(self):
        chunks=self.chunk_storage.load()
        bm25_retriever=BM25Retriever.from_documents(
            chunks
        )
        bm25_retriever.k=5
        faiss_db=self.vector_store.get_store()
        faiss_retriever=faiss_db.as_retriever(
            search_kwargs={"k":5}
        )
        hybrid_reteriver= EnsembleRetriever(
            retrievers=[faiss_retriever,
            bm25_retriever],
            weights=[0.5,0.5]
            )
        return hybrid_reteriver
    
    