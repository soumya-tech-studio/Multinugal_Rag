from unittest.mock import MagicMock, patch
from Ingestion_pipeline import pipeline
from Ingestion_pipeline.pipeline import IngestionPipeline
import pytest
def test_ingest_success():
    pipeline=IngestionPipeline()
    pipeline.register = MagicMock()
    pipeline.pdf_loader = MagicMock()
    pipeline.chunker = MagicMock()
    pipeline.store = MagicMock()
    pipeline.chunk_storage = MagicMock()
    file=MagicMock()
    file.filename="sample.pdf"
    file.file=MagicMock()
    pipeline.register.document_exists.return_value=False
    pipeline.register.register_document.return_value="doc123"
    pipeline.pdf_loader.load.return_value = [
        {"page": 1, "text": "Hello"},
        {"page": 2, "text": "World"}
    ]

    pipeline.chunker.chunk_text.return_value = [
        {"chunk_id": "c1", "text": "Hello"},
        {"chunk_id": "c2", "text": "World"}
    ]
    with patch("Ingestion_pipeline.pipeline.generate_hash") as mock_hash:
        mock_hash.return_value="abc123"
        result=pipeline.ingest(file)
    assert result["document_id"]=="doc123"
    assert result["status"]=="Completed"
    mock_hash.assert_called_once_with(file)
    pipeline.register.register_document.assert_called_once()
    pipeline.pdf_loader.load.assert_called_once_with(file,"doc123")
    pipeline.chunker.chunk_text.assert_called_once()
    pipeline.store.create.assert_called_once()
    pipeline.chunk_storage.save.assert_called()
    pipeline.register.update_status.assert_any_call("doc123", status="Processing")
    pipeline.register.update_status.assert_any_call("doc123", status="Completed")
def test_duplicate_document():
    pipeline=IngestionPipeline()
    pipeline.register = MagicMock()
    pipeline.pdf_loader = MagicMock()
    pipeline.chunker = MagicMock()
    pipeline.store = MagicMock()
    pipeline.chunk_storage = MagicMock()
    file=MagicMock()
    file.filename="sample.pdf"
    file.file=MagicMock()
    pipeline.register.document_exists.return_value=True
    with patch("Ingestion_pipeline.pipeline.generate_hash") as mock_hash:
            mock_hash.return_value="abc123"
            result=pipeline.ingest(file)
    assert result["status"]=="Duplicate"
def test_ingest_exception():
    pipeline=IngestionPipeline()
    pipeline.register = MagicMock()
    pipeline.pdf_loader = MagicMock()
    pipeline.chunker = MagicMock()
    pipeline.store = MagicMock()
    pipeline.chunk_storage = MagicMock()
    file=MagicMock()
    file.filename="sample.pdf"
    file.file=MagicMock()
    pipeline.register.document_exists.return_value = False
    pipeline.register.register_document.return_value = "doc123"
def test_ingest_exception():
    pipeline=IngestionPipeline()
    pipeline.register = MagicMock()
    pipeline.pdf_loader = MagicMock()
    pipeline.chunker = MagicMock()
    pipeline.store = MagicMock()
    pipeline.chunk_storage = MagicMock()
    file=MagicMock()
    file.filename="sample.pdf"
    file.file=MagicMock()
    pipeline.register.document_exists.return_value = False
    pipeline.register.register_document.return_value = "doc123"
    pipeline.pdf_loader.load.side_effect=Exception("Failed to load PDF")
    with patch("Ingestion_pipeline.pipeline.generate_hash") as mock_hash:
                mock_hash.return_value="abc123"
                with pytest.raises(Exception,match="Failed to load PDF"):
                    pipeline.ingest(file)
def test_delete_document():
    pipeline = IngestionPipeline()
    pipeline.store = MagicMock()
    pipeline.chunk_storage = MagicMock()
    pipeline.register = MagicMock()
    pipeline.register.get_document_by_id.return_value={"filename": "sample.pdf"}
    pipeline.delete_document("doc123")
    pipeline.register.get_document_by_id.assert_called_once_with("doc123")
    pipeline.store.delete_document.assert_called_once_with("doc123")
    pipeline.chunk_storage.delete_chunk.assert_called_once_with("doc123")
    pipeline.register.delete_document.assert_called_once_with("doc123")
    
    
    
    
    
                    
                    
    
    
    
    
    
    
    
    
    
       
    
    
    
 

