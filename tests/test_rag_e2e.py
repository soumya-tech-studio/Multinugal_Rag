from pathlib import Path
from fastapi import UploadFile
from Ingestion_pipeline.pipeline import IngestionPipeline
from chain.runnable_chain import ChainService
def test_end_to_end_rag():
    pdf_path=Path("tests/test_data/rag_test.pdf")
    pipeline=IngestionPipeline()
    with open(pdf_path,"rb") as file:
        upload_file=UploadFile(
            filename="rag_test.pdf",
            file=file
        )
        result=pipeline.ingest(upload_file)
        print(pipeline.register.get_all_documents())

    assert result["status"]=="Completed"
    document_id=result["document_id"]
    try:
        chain=ChainService()
        query="Where is KIIT University located?"
        response=chain.invoke_chain(query)
        assert response is not None
        assert len(response.strip())>0
        assert "Bhubaneswar" in response
    finally:
        pipeline.delete_document(document_id)
        
        

        


        
        
        
        