import pandas as pd
import streamlit as st

st.title('Selamat Datang Di Dashboard Indikator Strategis Kota Jambi')
 
st.subheader('Daftar Data', divider='rainbow')
st.page_link("pages/1_Kependudukan.py", label="Kependudukan", icon="1️⃣")
st.page_link("pages/2_Tenaga_Kerja.py", label="Tenaga Kerja", icon="2️⃣")
st.page_link("pages/3_Kemiskinan.py", label="Kemiskinan", icon="3️⃣")
st.page_link("pages/4_Indeks_Pembangunan_Manusia.py", label="Indeks Pembangunan Manusia", icon="4️⃣")
st.page_link("pages/5_Inflasi.py", label="Inflasi", icon="5️⃣")
st.page_link("pages/6_Pertumbuhan_Ekonomi.py", label="Pertumbuhan Ekonomi", icon="6️⃣")
st.page_link("pages/7_Produk_Domestik_Regional_Bruto.py", label="Produk Domestik Regional Bruto", icon="7️⃣")
st.page_link("pages/8_Pendidikan.py", label="Pendidikan", icon="8️⃣")
st.page_link("pages/9_Kesehatan.py", label="Kesehatan", icon="9️⃣")