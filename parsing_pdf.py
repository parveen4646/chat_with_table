import pdfplumber

import pandas as pd
def parse_pdf(pdf_file_path):
    pdf = pdfplumber.open(pdf_file_path)
    tabels_dict={}
    pages_with_tables=[]
    for i in range(0,len(pdf.pages)):
        if pdf.pages[i].extract_tables():
            table=pdf.pages[i].extract_tables()
            tabels_dict[i]=table
            pages_with_tables.append(i)

            return pages_with_tables,tabels_dict
   