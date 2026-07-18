from  Ingestion.docx_loader  import DocxLoader
from Ingestion.pdf_loader import PDFLoader

from pathlib import Path


class LoaderRegister:
    def __init__(self):
        self.extractors={
            ".pdf": PDFLoader(),
            ".docx": DocxLoader()
        }
    def get_extractor(self,file):

        
        path=Path(file)
        filetype=path.suffix
        loader=self.extractors.get(filetype)
        if loader is None:
            raise ValueError(f"Unsupported file type: {filetype}")
        doc_data=loader.load(file)
        return doc_data
    
    
        
                



         





    
        
        
        