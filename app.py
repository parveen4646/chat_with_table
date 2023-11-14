
import requests
from dotenv import load_dotenv
load_dotenv()
import os
from parsing_pdf import parse_pdf
import pandas as pd



API_URL = "https://api-inference.huggingface.co/models/google/tapas-base-finetuned-wtq"
headers = {"Authorization": "Bearer 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"}
def find(payload):
		response = requests.post(API_URL, headers=headers, json=payload)
		return response.json()

def table_parser(pdf_file_path,user_query):

	pages,table=parse_pdf(pdf_file_path)
	all_output=[]
	
	for i in pages:
		df='tabel' + str(i)
		df=pd.DataFrame(table[i][0],columns=table[i][0][0])
		df=df.iloc[1:,:]
		df_dict=df.to_dict(orient='list')

		output = find({
			"inputs": {
				"query": user_query,
				"table": df_dict
			},
		})
		all_output.append(output)
		
	return df,all_output