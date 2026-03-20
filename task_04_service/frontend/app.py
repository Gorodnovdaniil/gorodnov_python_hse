#!/usr/bin/env python3

import streamlit as st
import requests
import pandas as pd

API_URL = "http://127.0.0.1:8000"

response = requests.get(f"{API_URL}/records")
data = response.json()


df = pd.DataFrame(data)

st.dataframe(df)

with st.form("add_record"):
    timestep = st.date_input("Date (timestep)")
    consumption_eur = st.number_input("Consumption EUR", min_value=0)
    consumption_sib = st.number_input("Consumption SIB", min_value=0)
    price_eur = st.number_input("Price EUR", min_value=0.0)
    price_sib = st.number_input("Price SIB", min_value=0.0)
    
    submit = st.form_submit_button("Add Record")
    
    if submit:
        new_record = {
            "timestep": str(timestep),
            "consumption_eur": consumption_eur,
            "consumption_sib": consumption_sib,
            "price_eur": price_eur,
            "price_sib": price_sib
        }
        
        response = requests.post(f"{API_URL}/records", json=new_record)
        
        if response.status_code == 200:
            st.success("Record added!")
            st.rerun()
        else:
            st.error("Error adding record")


with st.form("delete_record"):
    record_id = st.number_input("ID to delete", min_value=1, step=1)
    submit = st.form_submit_button("Delete Record")
    
    if submit:
        response = requests.delete(f"{API_URL}/records/{int(record_id)}")
        
        if response.status_code == 200:
            st.success(f"Record {record_id} deleted!")
            st.rerun()
        else:
            st.error("Record not found")

#графики
if not df.empty:
    st.line_chart(df.tail(100).set_index('timestep')[["consumption_eur", "consumption_sib"]])
