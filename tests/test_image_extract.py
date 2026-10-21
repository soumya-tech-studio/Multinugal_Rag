from pathlib import Path
import fitz
from page_processing.image_extractor import ImageExtractor
def test_extract_images():
    extractor=ImageExtractor()
    pdf=fitz.open(Path(("tests/pdf_data/sample-5mb.pdf")))
    page=pdf[0]
    images=extractor. image_extractor(page)
    pdf.close()

    assert isinstance(images, list)
    assert len(images) > 0
    