from docx import Document
from .base import Loader
class DocxLoader(Loader):
    def load(self,file,document_id):
        chunks=[]
        filename=file.name if hasattr(file,"name") else "unknown_docx"
        doc=Document(file)
        
        for para_id,para in enumerate(doc.paragraphs):
            text=para.text.strip()
            meta={
                "document_id":document_id,
                "filename":filename,
                "para_id":para_id+1,
                "filetype":"docx",
                "source_type": "paragraph"
            }
            chunks.append({
                "metadata":meta,
                "Content":{
                    "text":text,
                    "text_len":len(text),
                    "para_num":para_id+1
                }
            })
        return chunks
    
    