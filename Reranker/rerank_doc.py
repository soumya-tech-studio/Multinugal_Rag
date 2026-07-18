from sentence_transformers import CrossEncoder
class RerankerService:
    def __init__(self, model_name: str = "cross-encoder/ms-marco-MiniLM-L-6-v2"):
        self.model=CrossEncoder(model_name)
    def rerank(self,query:str,documents:list,top_k:int=5):
        if not documents:
            return []
        pairs=[
            (query,doc.page_content)
            for doc in documents
        ]
        scores=self.model.predict(pairs)
        scored_documents=list(zip(documents,scores))
        scored_documents.sort(
            key =lambda x:x[1],
            reverse=True
        )
        reranked_doc=[
            doc
            for doc,score in scored_documents[:top_k]
        ]
        return reranked_doc
        

