from page_processing.classify_page import Page_Processor
def test_digital_page():
    processor=Page_Processor()
    text = "This is a digital page. " * 5
    result= processor.process_page(text,0)
    assert result["page_type"] == "digital"
    assert result["image_count"] == 0
    assert result["text_length"] >= 50
    
def  test_mixed_page():
      processor=Page_Processor()
      text = "This is a digital page. " * 5
      result= processor.process_page(text,2)
      assert result["page_type"] == "Mixed"
      assert result["image_count"] ==2
      assert result["text_length"] >= 50

def  test_Scanned_page():
      processor=Page_Processor()
      
      result= processor.process_page("",3)
      assert result["page_type"] == "Scanned"
      assert result["image_count"] ==3
      assert result["text_length"] == 0
      
def  test_mixed_page():
      processor=Page_Processor()
      
      result= processor.process_page("",0)
      assert result["page_type"] == "Unknown"
      assert result["image_count"] ==0
      assert result["text_length"] >= 0

    

    

    
    

