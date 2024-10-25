import pandas as pd
import streamlit as st

st.title('Produk Domestik Regional Bruto')
 
tab1, tab2, tab3= st.tabs(["Konsep & Definisi", "Data", "Visualisasi"])

with tab1:
    st.subheader('Produk Domestik Regional Bruto')
    st.markdown("Produk Domestik Regional Bruto(PDRB) merupakan nilai tambah bruto seluruh barang dan jasa yang tercipta atau dihasilkan di wilayah domestik suatu negara yang timbul akibat berbagai aktivitas ekonomi dalam suatu periode tertentu tanpa memperhatikan apakah faktor produksi yang dimiliki residen atau non-residen. Penyusunan PDRB dapat dilakukan melalui 3 (tiga) pendekatan yaitu pendekatan produksi, pengeluaran, dan pendapatan yang disajikan atas dasar harga berlaku dan harga konstan (riil).")
    st.markdown("PDRB atas dasar harga berlaku atau dikenal dengan PDRB nominal disusun berdasarkan harga yang berlaku pada periode penghitungan, dan bertujuan untuk melihat struktur perekonomian. Sedangkan PDRB atas dasar harga konstan (riil)disusun berdasarkan harga pada tahun dasar dan bertujuan untuk mengukur pertumbuhan ekonomi.")
    

with tab2:
    # option = st.selectbox("Pilih Tahun Data",("2024", "2023", "2022", "2021", "2020"))
    # df = pd.DataFrame(inflasi[option])
    # st.dataframe(data=df, use_container_width=True)
    st.caption('Sumber: Badan Pusat Statistik (BPS)')

with tab3:
    st.subheader('Visualisasi Belum Tersedia')