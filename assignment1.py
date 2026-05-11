import streamlit as st
import pandas as pd 

pg = st.navigation([st.Page("page1.py"), st.Page("page2.py")])



pg.run()
DATA_PATH = "./data/SGJobData.csv"
@st.cache_data
def load_data(path):
    df = pd.read_csv(path)
    #df["month"] = pd.to_datetime(df["month"])
    return df

df = load_data(DATA_PATH)