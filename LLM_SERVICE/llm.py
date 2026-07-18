from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

class LLMService:
    def __init__(self):
        load_dotenv()
        self.llm=ChatGoogleGenerativeAI(model="gemini-2.5-flash",temperature=0,max_retries=3)
    def get_llm(self):
        return self.llm

        