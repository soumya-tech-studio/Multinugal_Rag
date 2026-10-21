from fastapi.testclient import TestClient
from unittest.mock import patch,MagicMock
with patch("chain.runnable_chain.RetrieverService"), \
     patch("chain.runnable_chain.LLMService"), \
     patch("chain.runnable_chain.RerankerService"), \
     patch("chain.runnable_chain.LanguageDetect"):
    from chain.runnable_chain import ChainService
    with patch.object(ChainService, "__init__", return_value=None):
        from fastapi.testclient import TestClient
        from api.main import app
      


from api.main import app
client=TestClient(app)

def test_home():
    response=client.get("/")
    assert response.status_code==200
    assert response.json()=={
        "message": "Welcome to Multilingual RAG"
    }
@patch("api.main.pipeline")
def test_upload_success(mock_pipeline):
    mock_pipeline.ingest.return_value=None
    response=client.post("/upload", files={"file": (
        "test.pdf",
        "fake pdf content",
        "application/pdf"
    )})
    assert response.status_code==200
    assert response.json()=={
        "message": "Document uploaded successfully"
    }
    mock_pipeline.ingest.assert_called_once()
    
@patch("api.main.pipeline")   
def test_upload_failure(mock_pipeline):
    mock_pipeline.ingest.side_effect=Exception("Upload failed")
    response=client.post("/upload", files={"file": (
            "test.pdf",
            "fake pdf content",
            "application/pdf"
    )})
    assert response.status_code==500
    assert "Upload failed" in response.json()["detail"]
@patch("api.main.DocumentRegister")
def test_get_document(mock_register):
    mock_register_instance=mock_register.return_value
    mock_register_instance.get_all_documents.return_value=[
        {
            "id": 1,
            "filename": "test.pdf"
        },
        {
            "id": 2,
            "filename": "sample.pdf"
        }
    ]

    response=client.get("/get_document")
    assert response.status_code==200
    data=response.json()
    assert data["count"]==2
    assert len(data["documents"])==2
    mock_register_instance.get_all_documents.assert_called_once()
@patch("api.main.DocumentRegister")
def test_document_by_id(mock_register):
    mock_register_instance=mock_register.return_value
    mock_register_instance.get_document_by_id.return_value={
        "id": 1,
        "filename": "test.pdf"
    }

    response=client.get("/document/1")
    assert response.status_code==200
    data=response.json()
    assert data["document"]["id"]==1
    assert data["document"]["filename"]== "test.pdf"
    mock_register_instance.get_document_by_id.assert_called_once()
@patch("api.main.DocumentRegister")
def test_document_by_id_not_found(mock_register):
    mock_register_instance=mock_register.return_value
    mock_register_instance.get_document_by_id.return_value=None
    response=client.get("/document/99")
    assert response.status_code==500
@patch("api.main.pipeline")
def test_delete_document(mock_pipeline):
    mock_pipeline.delete_document.return_value=None
    response=client.delete("/delete_document/1")
    assert response.status_code==200
    assert response.json()=={
        "message": "Document with ID 1 deleted successfully"
    }
    mock_pipeline.delete_document.assert_called_once_with(1)
@patch("api.main.chain")
def test_chain_invoke(mock_chain):
    mock_chain.invoke_chain.return_value="This is the answer."
    response=client.post("/ask",json={"question": "what is this document about?"})
    assert response.status_code==200
    data=response.json()
    assert data["question"]== "what is this document about?"
    assert data["answer"]== "This is the answer."
    mock_chain.invoke_chain.assert_called_once_with("what is this document about?")
@patch("api.main.chain")
def test_chain_invoke_failure(mock_chain):
    mock_chain.invoke_chain.side_effect=Exception("Failed to invoke chain")
    response=client.post("/ask",json={"question": "what is this document about?"})
    assert response.status_code==500
    assert "Failed to invoke chain" in response.json()["detail"]
    

    
    



    
    
    

    
