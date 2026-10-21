from Vector_store.faiss import  FaissVector
from langchain_core.documents import Document
def test_load_vector_store(tmp_path):
     documents = [
        Document(
            page_content="Python is a programming language.",
            metadata={"document_id": "doc1"}
        ),
        Document(
            page_content="Machine learning uses data.",
            metadata={"document_id": "doc2"}
        )
    ]
     store_path=tmp_path/"faiss_store"
     vector_store=FaissVector(index_path=str(store_path))
     vector_store.create(documents)
     new_vector_store=FaissVector(
         index_path=str(store_path)
     )
     new_vector_store=FaissVector(index_path=str(store_path))
     loaded_store=new_vector_store.load()
     assert loaded_store is not None
     assert len(loaded_store.docstore._dict)==2
     
def test_delete_document(tmp_path):
    documents = [
        Document(
            page_content="Python is a programming language.",
            metadata={"document_id": "doc1"}
        ),
        Document(
            page_content="Machine learning uses data.",
            metadata={"document_id": "doc2"}
        )
    ]
    store_path=tmp_path/"faiss_store"
    vector_store=FaissVector(index_path=str(store_path))
    vector_store.create(documents)
    vector_store.delete_document("doc1")
    loaded_store=vector_store.load()
    assert loaded_store is not None
    assert len(loaded_store.docstore._dict) == 1
    remaining_doc=list(loaded_store.docstore._dict.values())
    assert remaining_doc[0].metadata.get("document_id") == "doc2"
    

    
