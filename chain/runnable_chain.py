from langchain_core.runnables import RunnablePassthrough,RunnableLambda
from langchain_core.output_parsers import StrOutputParser
from LLM_SERVICE.llm import LLMService
from Prompts.prompts import RAG_PROMPT
from language_detect.detect import LanguageDetect
from reteriver.hybrid import RetrieverService
from Reranker.rerank_doc import RerankerService
class ChainService:
    def __init__(self):
        self.LLM=LLMService().get_llm()
        self.lang_detect=LanguageDetect()
        self.Rerank=RerankerService()
        self.reterive=RetrieverService().get_reteriver()
        
    def rerank_reterive(self,question):
        documents=self.reterive.invoke(question)
        reranked_documents=self.Rerank.rerank(query=question,documents=documents,top_k=5)
        return reranked_documents
        
        
        
    def get_chain(self):
        self.chain=(
            {
                "context":RunnableLambda(self.rerank_reterive),
                "question":RunnablePassthrough(),
                "query_language":RunnableLambda(lambda question:self.lang_detect.lang(question)),
            }
            |RAG_PROMPT
            |self.LLM
            |StrOutputParser()
            
            
 )
    def invoke_chain(self,question):
          chain=self.get_chain()
          return self.chain.invoke(question)
      
      
        