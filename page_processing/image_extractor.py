import fitz       
from PIL import Image
import io
class ImageExtractor:
    def image_extractor(self,page):
        images=[]
        for img in page.get_images(full=True):
            xref=img[0]
            pdf=page.parent
            base_img=pdf.extract_image(xref)
            img=base_img["image"]
            pil_image=Image.open(io.BytesIO(img)).convert("RGB")
            images.append(pil_image)
        return images
    
    