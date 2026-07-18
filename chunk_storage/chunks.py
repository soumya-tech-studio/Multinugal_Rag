import pickle
from pathlib import Path
class ChunkStorage:
    FILE_PATH=Path("data/chunk_storage.pkl")
    @classmethod
    def save(cls,new_chunks):
        all_chunks=[]
        if cls.FILE_PATH.exists():
            with open(cls.FILE_PATH,"rb") as f:
                all_chunks=pickle.load(f)
        all_chunks.extend(new_chunks)
        cls.FILE_PATH.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        with open(cls.FILE_PATH,"wb") as f:
            pickle.dump(all_chunks,f)
    @classmethod
    def load(cls):
        if not cls.FILE_PATH.exists():
            return []
        with open(cls.FILE_PATH,"rb") as f:
            return pickle.load(f)
    @classmethod
    def delete_chunk(cls,document_id):
        if not cls.FILE_PATH.exists():
            return
        chunks=cls.load()
        remaining_chunks=[chunk for chunk in chunks if chunk.metadata.get("document_id")!=document_id]
        with open(cls.FILE_PATH,"wb") as f:
            pickle.dump(remaining_chunks,f)
        print(f"Deleted chunks for document {document_id}.")
        print(f"Remaining chunks: {len(remaining_chunks)}")
    @classmethod
    def total_chunks(cls):
        return len(cls.load())
    @classmethod
    def delete_all_chunks(cls):
        if cls.FILE_PATH.exists():
            cls.FILE_PATH.unlink()
            print("Chunk storage deleted.")
    
            
             

    