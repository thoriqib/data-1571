import pandas as pd
import streamlit as st

st.title('Pendidikan')
 
with st.sidebar:
    option = st.selectbox(
        'Tahun Data',
        ("Semua",2021, 2022, 2023))
 
df = pd.DataFrame({
    'c1': [1, 2, 3, 4],
    'c2': [10, 20, 30, 40],
})
 
st.dataframe(data=df, width=500, height=150)

df1 = pd.DataFrame({
    'c1': [1, 2, 3, 4],
    'c2': [10, 20, 30, 40],
})
st.table(data=df1)

st.write('You selected:', option)
name = st.text_input(label='Nama lengkap', value='')
st.write('Nama: ', name)