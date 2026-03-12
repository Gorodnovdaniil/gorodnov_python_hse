
#импорты

import pandas as pd
from pydantic import BaseModel
from datetime import date
from fastapi import FastAPI


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
def post_records():
	df = read_data()
	
