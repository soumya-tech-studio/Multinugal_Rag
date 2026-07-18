import fitz
from .base import Loader
from page_processing.ocrprocessing import OCRProcessor
from page_processing.extract_text import text_extractor
from page_processing.classify_page import Page_Processor
from page_processing.table_extractor import TableExtractor
from page_processing.image_extractor import ImageExtractor
from page_processing.image_analyser import  ImageAnalyzer
from language_detect.detect import LanguageDetect

from pathlib import Path
class PDFLoader(Loader):
    def __init__(self,):
        self.ocr_processor=OCRProcessor()
        self.text_extractor=text_extractor()
        self.page_processor=Page_Processor()
        self.table_extractor=TableExtractor()
        self.image_extract=ImageExtractor()
        self.image_analyse=ImageAnalyzer()
        self.lang_detect=LanguageDetect()
        

    def load(self,file,document_id):
        temp_dir=Path("temp")
        temp_dir.mkdir(exist_ok=True)
        filename=Path(file.filename).name 
        
    
        
        pdf_path=temp_dir/filename
        with open(pdf_path,"wb") as f:
            f.write(file.file.read())
        pdf=fitz.open(pdf_path)
            
        pages_data=[]
        
        
        try:
            for page_id in range(len(pdf)):
              ocr_text=""
              page=pdf[page_id]
              text=self.text_extractor.extract_text(page)
              tables=self.table_extractor.extract_tables(pdf_path,page_id+1)

              
              image_count=len(page.get_images(full=True))
              page_info=self.page_processor.process_page(text,image_count)
              
              if self.ocr_processor and page_info["page_type"].lower() in ['mixed','scanned']:
                print("OCR RUNNING")
                ocr_text=self.ocr_processor.extract_text_from_image(page)
              images_metadata=[]
              image_text=[]
              if image_count>0 and page_info["page_type"].lower() in ['mixed','scanned']:
                  images=self.image_extract.image_extractor(page)
                  for idx, img in enumerate(images):
                      width,height=img.size
                      if width<100 or height<100:
                          continue
                      description=self.image_analyse.analyser_image(img)
                      image_text.append(description)
                
                      images_metadata.append({
                             "image_id": idx + 1,

                            "page_id": page_id + 1,

                            "width": width,

                            "height": height,

                            "description": description

                          
                          
                      })
              if isinstance(image_text, list):
                             image_text = "\n".join(image_text)
              final_text=" ".join([text,ocr_text,tables,image_text])
              language=self.lang_detect.lang(final_text)
                      
                      
                      
                  
                  
                  
                  
                  
                  
              
              meta={
                "document_id":document_id,
                "filename":filename,
                "page_no":page_id+1,

                "filetype":"pdf",
                "source_type":"page",
                "page_type": page_info["page_type"],
                "language":language,
                "has_table": len(tables) > 0,
                "has_image": image_count > 0,
                "text_length": len(final_text)
            }
              pages_data.append({
                "metadata":meta,
                "Content":{
                    "text":final_text,
                    "text_len":len(final_text),
                    "page_num":page_id+1,
                    "native_text": text,
                    "ocr_text": ocr_text,
                    "tables_text":tables,
                    "images_metadata":images_metadata,
                    "image_text":image_text
                    
                }   
              })
            
            
          
             
              
            
        
        finally:  
          pdf.close()
          #if pdf_path.exists():
                #pdf_path.unlink()
        return pages_data
          
        
        
    

        
    
    
