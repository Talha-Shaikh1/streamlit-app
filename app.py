import streamlit as st;
import pandas as pd

st.write("""
# My First App 
         *hello world!*
""")

uploaded_file = st.file_uploader("Upload a CSV file", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df)