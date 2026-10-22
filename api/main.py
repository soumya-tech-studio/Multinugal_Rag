from fastapi import FastAPI, UploadFile, File
from Ingestion_pipeline.pipeline import  IngestionPipeline
from Registry.document_register import DocumentRegister
from fastapi import status,HTTPException
from chain.runnable_chain import  ChainService
from pydantic import BaseModel
import traceback
app=FastAPI()
pipeline=IngestionPipeline()
chain=ChainService()
class AskRequest(BaseModel):
    question:str
    
@app.get("/")
def home():
    return {"message": "Welcome to Multilingual RAG"}
@app.post("/upload")
async def upload_file(file:UploadFile=File(...)):
    try:
    
      pipeline.ingest(file)
      return {
        "message": "Document uploaded successfully"
    }
    except Exception as e:
        print("=" * 50)
        print("UPLOAD ENDPOINT ERROR")
        traceback.print_exc()
        print("=" * 50)

        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Internal Server Error: {str(e)}"
        )
@app.get("/get_document",status_code=status.HTTP_200_OK)
def get_document():
    try:
        register= DocumentRegister()
        documents=register.get_all_documents()
        return{
            "count": len(documents),
            "documents": documents
        }
    except Exception as e:
        traceback.print_exc()
        print("ERROR:", e)
        return {"error": str(e)}
@app.get("/document/{document_id}",status_code=status.HTTP_200_OK)
def document_by_id(document_id:int):
    try:
        register= DocumentRegister()
        document=register.get_document_by_id(document_id)
        if document is None:
            raise HTTPException(
                 status_code=status.HTTP_404_NOT_FOUND,
                detail="Document not found"
            )
        return {
            "message": "Document fetched successfully",
            "document": document
        }
    except Exception as e:
        print("INSIDE EXCEPT")
        traceback.print_exc()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Internal Server Error: {str(e)}"
        )
@app.delete("/delete_document/{document_id}",status_code=status.HTTP_200_OK)  
def delete_doc(document_id:int):
    try:
        pipeline.delete_document(document_id)
        return{
            "message":f"Document with ID {document_id} deleted successfully"
        }
    except Exception as e:
        print("INSIDE EXCEPT")
        traceback.print_exc()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Internal Server Error: {str(e)}"
        )
@app.post("/ask",status_code=status.HTTP_200_OK)
def ask_question(request:AskRequest):
    try:
        answer=chain.invoke_chain(request.question)
        return{
            "question":request.question,
            "answer":answer
            
        }
    except Exception as e:
        traceback.print_exc()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Internal Server Error: {str(e)}"
        )
        
        
    