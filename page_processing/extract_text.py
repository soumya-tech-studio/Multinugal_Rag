import re
class text_extractor:
    def extract_text(self,page):
        raw_text=page.get_text("text")
        if not raw_text:
            return ""
        text=raw_text.strip()
        text = re.sub(r"[ \t]+", " ", text)
        text=re.sub(r"\n{3,}","\n\n",text)
        if len(text)==0:
            return ""
        return text
    
   
    