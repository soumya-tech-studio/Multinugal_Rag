from unittest.mock import MagicMock, patch

from Reranker.rerank_doc import RerankerService
def test_reranker_service():
    with patch("Reranker.rerank_doc.CrossEncoder") as mock_crossencoder:
        mock_model=MagicMock()
        mock_crossencoder.return_value=mock_model
        service=RerankerService()
        doc1=MagicMock()
        doc1.page_content = "Python is a programming language"

        doc2 = MagicMock()
        doc2.page_content = "Python can be used for machine learning"

        doc3 = MagicMock()
        doc3.page_content = "The weather is sunny today"
        docs=[doc1,doc2,doc3]
        mock_model.predict.return_value=[0.9,0.8,0.1]
        result=service.rerank("Tell me about Python",docs,top_k=2)
        mock_model.predict.assert_called_once_with([
             ("Tell me about Python", "Python is a programming language"),
            ("Tell me about Python", "Python can be used for machine learning"),
            ("Tell me about Python", "The weather is sunny today")
        ]
            
        )
        assert result==[doc1,doc2]
        
        


