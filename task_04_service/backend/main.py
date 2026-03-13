
#импорты

import pandas as pd
from pydantic import BaseModel
from datetime import date
from fastapi import FastAPI
import csv

#пайдантик 
class RecordCreate(BaseModel):
    timestep: date
    consumption_eur: int
    consumption_sib: int
    price_eur: float
    price_sib: float


#fastapi
app = FastAPI()

@app.get("/ping")
def ping():
    return {"status": "ok"}


#функции для csv
def read_data():
	df = pd.read_csv('data.csv')
	return df

def to_data(df):
	df.to_csv('data.csv', index=False)

#эндпоинты

@app.get("/records")
def get_records():
	df = read_data()
	return df.to_dict(orient="records")

@app.post("/records")
def add_record(record: RecordCreate):
	df = read_data()
	with open('data.csv', 'a', new_line = '') as f:
		writer = csv.writer(f)
    		writer.writerow(new_row)
	to_date(df)

@app.delete("/records/{id}")
def delete_record(id: int):
	df = read_data()
	df = df.drop(id)
	to_date(df)
