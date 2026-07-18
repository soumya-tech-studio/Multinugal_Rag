import google.generativeai as genai
from dotenv import load_dotenv
import os
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
class ImageAnalyzer:

    def __init__(self):

        genai.configure(
            api_key=GOOGLE_API_KEY
        )

        self.model = genai.GenerativeModel(
            "gemini-2.5-flash"
        )
    def analyser_image(self,image):
        
        prompt = """
Analyze this document image.

Extract:
- Languages detected
- Visible text (keep original language)
- Tables
- Charts and trends
- Diagrams and workflows
- Important facts, numbers and dates
- Summary

Do not translate any text.
Return structured output.
"""
        try:
            response=self.model.generate_content([prompt,image])
            return response.context
        except Exception as e:
             print(
                f"Image Analysis Error: {e}"
            )
             return ""
            
            
            
       
                            