from Ingestion.loaderregister import LoaderRegister
from unittest.mock import MagicMock
import pytest
def test_get_pdf_extractor():
    register=LoaderRegister()
      
    mock_loader=MagicMock()
    register.extractors[".pdf"]=mock_loader
    extractor=register.get_extractor("test.pdf","123")
    mock_loader.load.assert_called_once_with("test.pdf","123")
def test_get_docx_extractor():
    register=LoaderRegister()
    mock_loader=MagicMock()
    register.extractors[".docx"]=mock_loader
    extractor=register.get_extractor("test.docx","123")
    mock_loader.load.assert_called_once_with("test.docx","123")
def test_unsupported_file_type():
    register=LoaderRegister()
    with pytest.raises(ValueError):
        register.get_extractor("test.txt","123")
        
      
    
    
    
    
    

