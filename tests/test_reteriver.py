from unittest.mock import MagicMock, patch

from reteriver.hybrid import RetrieverService
def test_get_retriever_success():
    service= RetrieverService()
    service.chunk_storage = MagicMock()
    service.vector_store = MagicMock()
    chunks=[
         MagicMock(),
         MagicMock()
        
    ]
    service.chunk_storage.load.return_value=chunks
    faiss_db= MagicMock()
    service.vector_store.get_store.return_value=faiss_db
    faiss_retriever= MagicMock()
    faiss_db.as_retriever.return_value=faiss_retriever
    with patch(
        "reteriver.hybrid.BM25Retriever.from_documents"
    ) as mock_bm25:
        with patch(
            "reteriver.hybrid.EnsembleRetriever"
            
        ) as mock_ensemble:
            bm25_retriever=MagicMock()
            mock_bm25.return_value=bm25_retriever
            result=service.get_reteriver()
    service.chunk_storage.load.assert_called_once()
    mock_bm25.asser_called_once_with(chunks)
    assert bm25_retriever.k==5
    service.vector_store.get_store.assert_called_once()
    faiss_db.as_retriever.assert_called_once_with(
        search_kwargs={"k": 5}

    )
      
    mock_ensemble.assert_called_once_with(
        retrievers=[faiss_retriever,bm25_retriever],
        weights=[0.5,0.5]
    )
    assert result==mock_ensemble.return_value
    
    
    
            
            
        
    
    
    
