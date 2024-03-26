import pandas as pd
import streamlit as st

st.title('Inflasi')
 
tab1, tab2, tab3= st.tabs(["Konsep & Definisi", "Data", "Visualisasi"])

with tab1:
    st.subheader('Inflasi')
    st.markdown("Kecenderungan naiknya harga barang dan jasa pada umumnya yang berlangsung secara terus menerus. Inflasi dihitung melalui IHK (Indeks Harga Konsumen). Inflasi terdiri dari inflasi month to month (bulanan), year to date (tahun berjalan) dan year on year (tahunan).")

    st.subheader('Indeks Harga Konsumen (IHK)')
    st.markdown('Indeks yang menghitung rata-rata perubahan harga dalam suatu periode, dari suatu kumpulan barang dan jasa yang dikonsumsi oleh penduduk/rumah tangga dalam kurun waktu tertentu.')
    
    st.subheader('Inflasi Year on Year (YoY)')
    st.markdown('Perbandingan IHK bulan n tahun berjalan dibanding IHK bulan yang sama pada tahun sebelumnya')

    st.subheader('Inflasi Month to Month (MtM)')
    st.markdown('Biasa disebut Inflasi Bulanan, dihitung melalui perbandingan IHK bulan berjalan dibanding dengan IHK bulan sebelumnya.')