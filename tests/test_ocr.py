from pathlib import Path
import fitz
from page_processing.ocrprocessing import OCRProcessor
def test_extract_text_from_image():
    ocr=OCRProcessor()
    pdf=fitz.open(Path("tests/pdf_data/test-ocr.pdf"))
    page=pdf[0]
    text=ocr.extract_text_from_image(page)
    assert isinstance(text,str)
    assert text != ""
    assert "This" in text
    assert "file" in text
    
    
    