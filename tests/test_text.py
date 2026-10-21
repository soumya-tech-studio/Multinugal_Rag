import fitz
from pathlib import Path
from page_processing.extract_text import text_extractor
def test_extract_text():
    extractor=text_extractor()
    pdf = fitz.open(Path("tests/pdf_data/sample_pdf.pdf"))
    page=pdf[0]

    text=extractor.extract_text(page)
    pdf.close()
    assert isinstance(text,str)
    assert text != ""
    assert len(text) > 0
    assert "Welcome to Multilingual RAG" in text
    
    