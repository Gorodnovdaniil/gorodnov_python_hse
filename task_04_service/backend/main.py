#!/usr/bin/env python3

#импорты

import pandas as pd
from pydantic import BaseModel
from datetime import date
from fastapi import FastAPI
import csv
from fastapi import HTTPException


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

    new_id = 1 if df.empty else int(df['id'].max()) + 1

    new_row = [new_id, record.timestep, record.consumption_eur,
               record.consumption_sib, record.price_eur, record.price_sib]

    with open('data.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(new_row)
    return {"message": "Record added", "id": new_id}


@app.delete("/records/{id}")
def delete_record(id: int):
    df = read_data()

    if id not in df['id'].values:
        raise HTTPException(status_code=404, detail="Item not found")

    df = df[df['id'] != id]
    to_data(df)
    
    return {"deleted_id": id}
