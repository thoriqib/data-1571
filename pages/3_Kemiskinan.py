import pandas as pd
import streamlit as st

st.title('Kemiskinan')
 
with st.sidebar:
    option = st.selectbox(
        'Tahun Data',
        ("Semua",2021, 2022, 2023))

kemiskinan = {
    '2021': { 
        'Jumlah Penduduk Miskin (dalam ribuan)': 54.233, 
        'Persentase Penduduk Miskin (P0)': 9.02,
        'Indeks Kedalaman Kemiskinan (P1)': 1.418, 
        'Indeks Keparahan Kemiskinan (P2)': 0.344,
        'Garis Kemiskinan (Rp/Kapita/Bulan)': 563403},
    '2022': { 
        'Jumlah Penduduk Miskin (dalam ribuan)': 50.401, 
        'Persentase Penduduk Miskin (P0)': 8.33,
        'Indeks Kedalaman Kemiskinan (P1)': 1.186, 
        'Indeks Keparahan Kemiskinan (P2)': 0.25,
        'Garis Kemiskinan (Rp/Kapita/Bulan)': 605556},
    '2023': { 
        'Jumlah Penduduk Miskin (dalam ribuan)': 50.086, 
        'Persentase Penduduk Miskin (P0)': 8.24,
        'Indeks Kedalaman Kemiskinan (P1)': 1.31, 
        'Indeks Keparahan Kemiskinan (P2)': 0.322,
        'Garis Kemiskinan (Rp/Kapita/Bulan)': 667447},
}
 
df = pd.DataFrame(kemiskinan)
 
st.dataframe(data=df, use_container_width=True)

df1 = pd.DataFrame({
    'c1': [1, 2, 3, 4],
    'c2': [10, 20, 30, 40],
})
st.table(data=df1)

st.write('You selected:', option)
name = st.text_input(label='Nama lengkap', value='')
st.write('Nama: ', name)