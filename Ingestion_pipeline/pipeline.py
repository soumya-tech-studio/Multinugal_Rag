from Registry.document_register import DocumentRegister
from Ingestion.pdf_loader import PDFLoader
from utils.hash import generate_hash
from Chunking.Semantic import SemanticChunking
from Vector_store.faiss import FaissVector
from chunk_storage.chunks import ChunkStorage
from pathlib import Path
class IngestionPipeline:
    def __init__(self):
        self.pdf_loader=PDFLoader()
        self.register=DocumentRegister()
        self.chunker=SemanticChunking()
        self.store=FaissVector()
        self.chunk_storage=ChunkStorage()
    def ingest(self,file):
        try:
            print("=" * 50)
            print(f"Processing: {file.filename}")
            filehash=generate_hash(file)
            if self.register.document_exists(filehash):
                print("Duplicate document detected")
                return {
    "status": "Duplicate",
    "message": "Document already exists."
}
            document_id=self.register.register_document(
                filename=file.filename,
                file_hash=filehash,
                file_type=Path(file.filename).suffix.lstrip(".")
            )
            self.register.update_status(document_id,status="Processing")
            print(file.file.tell())
            file.file.seek(0)
            pages=self.pdf_loader.load(file,document_id)
            chunks=self.chunker.chunk_text(pages)
            self.chunk_storage.save(chunks)
            
            self.store.create(chunks)
            
            
            
            
            self.register.update_page_count(len(pages),document_id)
            self.register.update_status(document_id,status="Completed")
            print(
                f"Completed Processing {len(pages)} pages"
            )

            return {
    "document_id": document_id,
    "status": "Completed"
}
        except Exception as e:
            import traceback

            print("INSIDE EXCEPT")
            traceback.print_exc()
            print("FULL ERROR:", e)
            
            if "document_id" in locals():
                print(f"Error: {str(e)}")
                self.register.update_status(document_id,
                                            status="Failed")
                self.register.update_error(
                    document_id,
                    str(e)
                )
            raise 
    def delete_document(self,document_id):
        document=self.register.get_document_by_id(document_id)
        temp_dir=Path("temp")
        pdf_path=temp_dir/document["filename"]
        if pdf_path.exists():
            pdf_path.unlink()
        self.store.delete_document(document_id)
        self.register.delete_document(document_id)
        self.chunk_storage.delete_chunk(document_id)
        
        

        
                
            
            
            
            
            
            

                
