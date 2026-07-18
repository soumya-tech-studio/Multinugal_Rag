class Page_Processor:
    MIN_TEXT_LENGTH = 50
    def process_page(self,text,image_count):
        text_length=len(text.strip()) if text else 0
        if text_length==0:
            page_type="Scanned" if image_count>0 else "Unknown"
        elif text_length<self.MIN_TEXT_LENGTH:
            page_type="Scanned" if image_count>0 else "Unknown"
        elif image_count>0:
            page_type="Mixed"
        else: 
            page_type="digital"
        return {
            "page_type": page_type,
            "text_length":text_length,
            "image_count": image_count
        }
            
            
        
        
        
            
    
    
    
    
    
        
        
        
        