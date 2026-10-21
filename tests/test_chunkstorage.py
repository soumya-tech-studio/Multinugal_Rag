from chunk_storage.chunks import ChunkStorage
from langchain_core.documents import Document
def test_save_chunks():
    ChunkStorage.delete_all_chunks()
    chunks = [
        Document(
            page_content="Chunk One",
            metadata={"document_id": "doc1"}
        ),
        Document(
            page_content="Chunk Two",
            metadata={"document_id": "doc2"}
        )
    ]
    ChunkStorage.save(chunks)
    loaded_chunks=ChunkStorage.load()
    assert len(loaded_chunks)==2
    assert loaded_chunks[0].page_content=="Chunk One"
    assert loaded_chunks[1].metadata["document_id"]=="doc2"
def test_delete_chunks():
      ChunkStorage.delete_all_chunks()
      chunks = [
        Document(
            page_content="Chunk One",
            metadata={"document_id": "doc1"}
        ),
        Document(
            page_content="Chunk Two",
            metadata={"document_id": "doc2"}
        )
    ]
      ChunkStorage.save(chunks)
      ChunkStorage.delete_chunk("doc1")
      remaining_chunks=ChunkStorage.load()
      assert len(remaining_chunks)==1
      assert remaining_chunks[0].metadata["document_id"]=="doc2"
def test_delete_all_chunks():
      ChunkStorage.delete_all_chunks()
      chunks = [
        Document(
            page_content="Chunk One",
            metadata={"document_id": "doc1"}
        )
    ] 
      ChunkStorage.save(chunks)
      ChunkStorage.delete_all_chunks()
      assert ChunkStorage.FILE_PATH.exists() is False
      
        
      

    
    
    
    