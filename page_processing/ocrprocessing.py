
import fitz
import easyocr
import numpy as np
from PIL import Image
import io
class OCRProcessor:
    def __init__(self, language=None):
       if language is None:
            language = ["en", "te"]

       self.reader = easyocr.Reader(
            language,
            gpu=False)
    def extract_text_from_image(self,page):
        text=[]
        pix=page.get_pixmap(matrix=fitz.Matrix(2,2))
        img_bytes=pix.tobytes("png")
        image=Image.open(io.BytesIO(img_bytes))
        img_array=np.array(image)
        results=self.reader.readtext(img_array)

        text="\n".join([res[1] for res in results])
        return text
