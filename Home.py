import streamlit as st

st.set_page_config(page_title="Data 1571", page_icon='BPS.png')

st.title('Selamat Datang Di Dashboard Indikator Strategis Kota Jambi')
 
st.subheader('Daftar Data', divider='rainbow')
st.page_link("pages/1_Kependudukan.py", label="Kependudukan", icon="1️⃣")
st.page_link("pages/2_Tenaga_Kerja.py", label="Tenaga Kerja", icon="2️⃣")
st.page_link("pages/3_Kemiskinan.py", label="Kemiskinan", icon="3️⃣")
st.page_link("pages/4_Indeks_Pembangunan_Manusia.py", label="Indeks Pembangunan Manusia", icon="4️⃣")
st.page_link("pages/5_Inflasi.py", label="Inflasi", icon="5️⃣")
st.page_link("pages/6_Produk_Domestik_Regional_Bruto.py", label="Produk Domestik Regional Bruto", icon="6️⃣")

