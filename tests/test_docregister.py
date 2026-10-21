from Registry.document_register import DocumentRegister
import sqlite3
from pathlib import Path
def test_create_connection_and_table(tmp_path):
    db_path=tmp_path/"test_metadata.db"
    register=DocumentRegister(str(db_path))
    conn=register.create_connection()
    cursor=conn.cursor()
    cursor.execute("""
                   select name from sqlite_master where type='table' and name='documents'
                   """)
    result=cursor.fetchone()
    conn.close()
    assert result is not None
    assert result[0]=='documents'
def test_register_document(tmp_path):
     db_path=tmp_path/"test_metadata.db"
     register=DocumentRegister(str(db_path))
     document_id=register.register_document(
         filename="sample.pdf",
        file_hash="abc123",
        file_type="pdf"
    )
     assert document_id is not None
     assert document_id>0
def test_document_exists(tmp_path):
     db_path=tmp_path/"test_metadata.db"
     register=DocumentRegister(str(db_path))
     register.register_document(
        filename="sample.pdf",
        file_hash="abc123",
        file_type="pdf"
    )
     assert register.document_exists("abc123") is True
     assert register.document_exists("not_exist") is False


def test_get_all_documents(tmp_path):
    db_path=tmp_path/"test_metadata.db"
    register=DocumentRegister(str(db_path))
    register.register_document(
        filename="sample1.pdf",
        file_hash="hash1",
        file_type="pdf"
    )

    register.register_document(
        filename="sample2.docx",
        file_hash="hash2",
        file_type="docx"
    )
    documents=register.get_all_documents()
    assert len(documents)==2
    assert documents[0]["filename"] == "sample2.docx"
    assert documents[1]["filename"] == "sample1.pdf"
  
def test_get_document_by_id(tmp_path):
     db_path=tmp_path/"test_metadata.db"
     register=DocumentRegister(str(db_path))
     
     document_id = register.register_document(
        filename="sample.pdf",
        file_hash="abc123",
        file_type="pdf"
    )
     document=register.get_document_by_id(document_id)
     assert document is not None
     assert document["document_id"] == document_id
     assert document["filename"] == "sample.pdf"
     assert document["file_type"] == "pdf"
     assert document["status"] == "uploaded"
def test_delete_document(tmp_path):
     db_path=tmp_path/"test_metadata.db"
     register=DocumentRegister(str(db_path))
     document_id = register.register_document(
        filename="sample.pdf",
        file_hash="abc123",
        file_type="pdf"
    )
     assert register.document_exists("abc123") is True
     register.delete_document(document_id)
     assert register.document_exists("abc123") is False
     assert register.get_document_by_id(document_id) is None
     



    
     
    
    
