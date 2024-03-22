import pandas as pd
import streamlit as st

st.title('Indeks Pembangunan Manusia')
 
with st.sidebar:
    option = st.selectbox(
        'Tahun Data',
        ("Semua",2021, 2022, 2023))
    
ipm = {
    '2021': { 
        'Indeks Pembangunan Manusia (IPM)': 79.94, 
        'Umur Harapan Hidup (UHH)': 74.37,
        'Pengeluaran Per Kapita (Ribu Rupiah)': 12240, 
        'Rata-rata Lama Sekolah': 11.20,
        'Harapan Lama Sekolah': 15.37},
    '2022': { 
        'Indeks Pembangunan Manusia (IPM)': 80.38, 
        'Umur Harapan Hidup (UHH)': 74.61,
        'Pengeluaran Per Kapita (Ribu Rupiah)': 12597, 
        'Rata-rata Lama Sekolah': 11.21,
        'Harapan Lama Sekolah': 15.38},
    '2023': { 
        'Indeks Pembangunan Manusia (IPM)': 80.93, 
        'Umur Harapan Hidup (UHH)': 74.85,
        'Pengeluaran Per Kapita (Ribu Rupiah)': 12783, 
        'Rata-rata Lama Sekolah': 11.32,
        'Harapan Lama Sekolah': 667447},
}
 
df = pd.DataFrame(ipm)
 
st.dataframe(data=df, use_container_width=True)

df1 = pd.DataFrame({
    'c1': [1, 2, 3, 4],
    'c2': [10, 20, 30, 40],
})
st.table(data=df1)

st.write('You selected:', option)
name = st.text_input(label='Nama lengkap', value='')
st.write('Nama: ', name)