import pandas as pd
import streamlit as st

st.title('Pertumbuhan Ekonomi')
 
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

with tab2:
    # option = st.selectbox("Pilih Tahun Data",("2024", "2023", "2022", "2021", "2020"))
    # df = pd.DataFrame(inflasi[option])
    # st.dataframe(data=df, use_container_width=True)
    st.caption('Sumber: Badan Pusat Statistik (BPS)')

with tab1:
    st.subheader('Visualisasi Belum Tersedia')