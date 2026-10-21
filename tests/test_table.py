from pathlib import Path
from page_processing.table_extractor import TableExtractor
def test_extract_table():
    table=TableExtractor()
    pdf_path = Path("tests/pdf_data/sample_table.pdf")
    tables=table.extract_tables(pdf_path,1)
    assert isinstance(tables, str)
    assert tables != ""
    assert "Alice" in tables
    assert "Bob" in tables
    assert "Delhi" in tables
    
    