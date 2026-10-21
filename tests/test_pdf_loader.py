from pathlib import Path
from fastapi import UploadFile
from Ingestion.pdf_loader import PDFLoader
def test_load_valid_pdf():
       loader = PDFLoader()
       file_path = Path("tests/pdf_data/sample_pdf.pdf")
       with open(file_path, "rb") as f:
            upload_file = UploadFile(
            filename=file_path.name,
            file=f
        )
            result=loader.load(upload_file,document_id="doc1")
       assert isinstance(result, list)
       assert len(result)==4
       assert result[0]["metadata"]["filetype"]=="pdf"
       assert result[0]["metadata"][ "source_type"]=="page"
       assert result[0]["metadata"]["page_no"] == 1
       assert "language" in result[0]["metadata"]
       assert "text" in result[0]["Content"]
       assert isinstance(result[0]["Content"]["text"], str)
       
       
       
        
