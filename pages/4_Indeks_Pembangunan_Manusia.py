import pandas as pd
import streamlit as st

st.title('Indeks Pembangunan Manusia')

tab1, tab2, tab3= st.tabs(["Konsep & Definisi", "Data", "Visualisasi"])
    
ipm = {
    '2021': { 
        'Indeks Pembangunan Manusia (IPM)': 79.94, 
        'Umur Harapan Hidup (UHH)': 74.37,
        'Pengeluaran Per Kapita (Ribu Rupiah)': 12240, 
        'Rata-rata Lama Sekolah (RLS)': 11.20,
        'Harapan Lama Sekolah (HLS)': 15.37},
    '2022': { 
        'Indeks Pembangunan Manusia (IPM)': 80.38, 
        'Umur Harapan Hidup (UHH)': 74.61,
        'Pengeluaran Per Kapita (Ribu Rupiah)': 12597, 
        'Rata-rata Lama Sekolah (RLS)': 11.21,
        'Harapan Lama Sekolah (HLS)': 15.38},
    '2023': { 
        'Indeks Pembangunan Manusia (IPM)': 80.93, 
        'Umur Harapan Hidup (UHH)': 74.85,
        'Pengeluaran Per Kapita (Ribu Rupiah)': 12783, 
        'Rata-rata Lama Sekolah (RLS)': 11.32,
        'Harapan Lama Sekolah (HLS)': 15.83},
}
df = pd.DataFrame(ipm)

with tab1:
    st.subheader('Pengeluaran Per Kapita')
    st.markdown("Biaya yang dikeluarkan untuk konsumsi semua anggota rumah tangga selama sebulan dibagi dengan banyakanya anggota rumah tangga")

    st.subheader('Umur Harapan Hidup (UHH)')
    st.markdown('Rata – rata perkiraan banyak tahun yang dapat ditempuh oleh seseorang sejak lahir')
    
    st.subheader('Rata-rata Lama Sekolah (RLS)')
    st.markdown('Jumlah tahun belajar penduduk usia 15 tahun ke atas yang telah diselesaikan dalam pendidikan formal (tidak termasuk tahun yang mengulang)')

    st.subheader('Harapan Lama Sekolah (HLS)')
    st.markdown('Lamanya sekolah(dalam tahun) yang di harapkan akan dirasakan oleh anak pada umur tertentu di masa mendatang')
with tab2:
    st.dataframe(data=df, use_container_width=True)
    st.caption('Sumber: Badan Pusat Statistik (BPS)')
    st.caption('Catatan: Umur Harapan Hidup (UHH) menggunakan hasil Long Form Sensus Penduduk 2020 (SP2020)')
 
with tab3:
    row1 = st.container()
    with row1:
        st.subheader('IPM Kota Jambi 2023')
        col1, col2, col3 = st.columns(3)
        col1.metric("IPM", df['2023'][0], round(df['2023'][0]-df['2022'][0],2))
        col2.metric("UHH", df['2023'][1], round(df['2023'][1]-df['2022'][1],2))
        col3.metric("Pengeluaran Per Kapita (Ribu Rupiah)", df['2023'][2], round(df['2023'][2]-df['2022'][2],2))
        col1.metric("RLS", df['2023'][3], round(df['2023'][3]-df['2022'][3],2))
        col2.metric("HLS", df['2023'][4], round(df['2023'][4]-df['2022'][4],2))
        st.caption('Catatan: Dibandingkan dengan tahun 2022. Umur Harapan Hidup (UHH) menggunakan hasil Long Form Sensus Penduduk 2020 (SP2020)')
    
    st.subheader('Indeks Pembangunan Manusia (IPM)')
    st.bar_chart(df.iloc[0])
    st.subheader('Umur Harapan Hidup (UHH)')
    st.bar_chart(df.iloc[1])
    st.subheader('Pengeluaran Per Kapita (Ribu Rupiah)')
    st.bar_chart(df.iloc[2])
    st.subheader('Rata-rata Lama Sekolah (RLS)')
    st.bar_chart(df.iloc[3])
    st.subheader('Harapan Lama Sekolah (HLS)')
    st.bar_chart(df.iloc[4])