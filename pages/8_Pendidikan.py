import pandas as pd
import streamlit as st

st.title('Pendidikan')
 
with st.sidebar:
    option = st.selectbox(
        'Tahun Data',
        ("Semua",2021, 2022, 2023))
 
st.header('Belum Tersedia')