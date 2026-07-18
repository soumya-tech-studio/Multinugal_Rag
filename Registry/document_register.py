import sqlite3
from datetime import datetime
class DocumentRegister:
    def __init__(self,db_path="metadata.db"):
        self.db_path=db_path
        self.create_table()
    def create_connection(self):
        return sqlite3.connect(
            self.db_path
        )
    def create_table(self):
        conn=self.create_connection()
        cursor=conn.cursor()
        cursor.execute("""
            Create table if not exists documents(
                document_id integer primary key autoincrement,
                filename text not null,
                file_hash text unique not null,
                file_type text,
                upload_time text,
                status text, 
                page_count integer default 0,
                chunk_count integer default 0,
                language text,
                error_message text
            )
        """)
        conn.commit()
        conn.close()
    def register_document(
        self,filename,file_hash,file_type):
        conn=self.create_connection()
        cursor=conn.cursor()
        cursor.execute(
            """
            insert into documents(
                filename,
                file_hash,
                file_type,
                upload_time,
                status
                
            ) 
            values(
                ?,?,?,?,?
            )
        """ ,
             (filename,
         file_hash,
         file_type,
         datetime.now().isoformat(),
         "uploaded"
            
        ))
        document_id = cursor.lastrowid
        conn.commit()
        conn.close()
        return document_id
    def document_exists(
        self,file_hash
    ):
      conn=self.create_connection()
      cursor=conn.cursor()
      cursor.execute( """
                    select 1 from documents
                    where file_hash=?
                    """,
                    (file_hash,)
                    )
      result=cursor.fetchone()
      conn.close()
      return result is not None
    def update_status(self,document_id,status):
        conn=self.create_connection()
        cursor=conn.cursor()
        cursor.execute("""
                       update documents
                       set status=?
                       where document_id=?
                       """,(
                           status,
                           document_id
                           
                       )
        )
        conn.commit()
        conn.close()
    def update_page_count(self,pages,document_id):
        conn=self.create_connection()
        cursor=conn.cursor()
        cursor.execute("""
                       update documents
                       set page_count=?
                       where document_id=?
                       
                       """,(pages,
                            document_id
                           
                       ))
        conn.commit()
        conn.close()
        
        
    def update_error(self,error_message,document_id):
         conn=self.create_connection()
         cursor=conn.cursor()
         cursor.execute("""
                       update documents
                       set error_message=?
                       where document_id=?
                       
                       """,(error_message,
                            document_id
                           
                       ))
         conn.commit()
         conn.close()
         
    def get_all_documents(self):
        conn=self.create_connection()
        cursor=conn.cursor()
        cursor.execute("""
                       select
                        document_id,
                        filename,
                        status,
                        page_count,
                        upload_time
                        from documents
                        order by upload_time desc
            
                      """ )
        rows=cursor.fetchall()
        documents=[]
        
         
        for row in rows:
            documents.append({
                "document_id": row[0],
                "filename": row[1],
                "status": row[2],
                "page_count": row[3],
                "upload_time": row[4]
            })
        return documents
    def get_document_by_id(self,document_id):
         conn=self.create_connection()
         cursor=conn.cursor()
         cursor.execute("""
                        select
                         document_id,
                         filename,
                        status,
                         page_count,
                         upload_time,
                         file_type,
                        language,
                      chunk_count,
                      error_message
                      from documents
                      where document_id=?
           
            
                        """,(document_id,))
         row=cursor.fetchone()
         conn.close()
         if row is None:
             return None
         return{
             "document_id": row[0],
        "filename": row[1],
        "status": row[2],
        "page_count": row[3],
        "upload_time": row[4],
        "file_type": row[5],
        "language": row[6],
        "chunk_count": row[7],
        "error_message": row[8]
         }
    def delete_document(self,document_id):
         conn=self.create_connection()
         cursor=conn.cursor()
         cursor.execute("""
                        delete from documents
                        where document_id=?
                        """,(document_id,))
         conn.commit()
         conn.close()
         
         
        
        
        
       
       
        
    
        
        
        