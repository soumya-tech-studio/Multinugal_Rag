import camelot
class TableExtractor:
    def extract_tables(self,pdf_path,page_num):
        tables=camelot.read_pdf(pdf_path,pages=str(page_num))
        table_text=[]
        for table in tables:
            table_text.append(table.df.to_markdown(index=False))
        del tables
        return "\n\n".join(table_text)
        

    