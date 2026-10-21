from pathlib import Path
from Ingestion.docx_loader import  DocxLoader
def test_laod_valid_docx():
    loader= DocxLoader()
    file_path=Path("tests/doc_data/sample.docx")
    with open(file_path,"rb") as file:
        result=loader.load(file,document_id="doc1")
    assert isinstance(result,list)
    assert len(result)==5
    assert result[0]["metadata"]["filetype"]=="docx"
    assert result[0]["metadata"][ "source_type"]=="paragraph"
    assert result[0][ "Content"]["text"]=="Welcome to Multilingual RAG."
    
    
    
    