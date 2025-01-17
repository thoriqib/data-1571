import pandas as pd
import streamlit as st

st.title('Kemiskinan')
 
tab1, tab2, tab3= st.tabs(["Konsep & Definisi", "Data", "Visualisasi"])

kemiskinan = {
    '2020': { 
        'Jumlah Penduduk Miskin (dalam ribuan)': 50.44, 
        'Persentase Penduduk Miskin (P0)': 8.27,
        'Indeks Kedalaman Kemiskinan (P1)': 1.47, 
        'Indeks Keparahan Kemiskinan (P2)': 0.40,
        'Garis Kemiskinan (Rp/Kapita/Bulan)': 529090},
    '2021': { 
        'Jumlah Penduduk Miskin (dalam ribuan)': 54.23, 
        'Persentase Penduduk Miskin (P0)': 9.02,
        'Indeks Kedalaman Kemiskinan (P1)': 1.42, 
        'Indeks Keparahan Kemiskinan (P2)': 0.34,
        'Garis Kemiskinan (Rp/Kapita/Bulan)': 563403},
    '2022': { 
        'Jumlah Penduduk Miskin (dalam ribuan)': 50.40, 
        'Persentase Penduduk Miskin (P0)': 8.33,
        'Indeks Kedalaman Kemiskinan (P1)': 1.19, 
        'Indeks Keparahan Kemiskinan (P2)': 0.25,
        'Garis Kemiskinan (Rp/Kapita/Bulan)': 605556},
    '2023': { 
        'Jumlah Penduduk Miskin (dalam ribuan)': 50.09, 
        'Persentase Penduduk Miskin (P0)': 8.24,
        'Indeks Kedalaman Kemiskinan (P1)': 1.31, 
        'Indeks Keparahan Kemiskinan (P2)': 0.32,
        'Garis Kemiskinan (Rp/Kapita/Bulan)': 667447},
    '2024': { 
        'Jumlah Penduduk Miskin (dalam ribuan)': 47.25, 
        'Persentase Penduduk Miskin (P0)': 7.73,
        'Indeks Kedalaman Kemiskinan (P1)': 0.96, 
        'Indeks Keparahan Kemiskinan (P2)': 0.23,
        'Garis Kemiskinan (Rp/Kapita/Bulan)': 757014},
}

df = pd.DataFrame(kemiskinan)

with tab1:
    st.subheader('Penduduk Miskin')
    st.markdown("Penduduk dengan pengeluaran per kapita per bulan di bawah garis kemiskinan")

    st.subheader('Garis Kemiskinan')
    st.markdown('Suatu representasi dari jumlah rupiah minimum yang dibutuhkan untuk memenuhi kebutuhan pokok minimum makanan dan kebutuhan pokok bukan makanan. Garis Kemiskinan dipergunakan sebagai suatu batas untuk mengelompokkan penduduk menjadi miskin atau tidak miskin. Penduduk miskin adalah penduduk yang memiliki rata-rata pengeluaran per kapita per bulan di bawah Garis Kemiskinan')
    
    st.subheader('Indikator Kedalaman Kemiskinan (P1)')
    st.markdown('Indikator P1 merupakan ukuran rata-rata kesenjangan pengeluaran masing-masing penduduk miskin terhadap garis kemiskinan. Jika ditemukan angka P1 yang semakin mendekati 0, maka kondisi ini menunjukkan rata-rata pengeluaran penduduk miskin semakin mendekati Garis Kemiskinan.')

    st.subheader('Indikator Keparahan Kemiskinan (P2)')
    st.markdown('Indikator P2 memberikan gambaran penyebaran pengeluaran di antara penduduk miskin. Angka P2 yang semakin mendekati 0 menunjukkan ketimpangan pengeluaran penduduk miskin secara umum semakin kecil.')

with tab2:
    st.dataframe(data=df, use_container_width=True)
    st.caption('Sumber: Badan Pusat Statistik (BPS)')
 
with tab3:
    row1 = st.container()
    with row1:
        st.subheader('Indikator Kemiskinan Kota Jambi 2024')
        col1, col2, col3 = st.columns(3)
        col1.metric("Jumlah Penduduk Miskin", df['2024'][0], round(df['2024'][0]-df['2023'][0],2), delta_color="inverse")
        col2.metric("Persentase Penduduk Miskin (P0)", df['2024'][1], round(df['2024'][1]-df['2023'][1],2), delta_color="inverse")
        col3.metric("Indikator Kedalaman Kemiskinan (P1)", df['2024'][2], round(df['2024'][2]-df['2023'][2],2), delta_color="inverse")
        col1.metric("Indikator Keparahan Kemiskinan (P2)", df['2024'][3], round(df['2024'][3]-df['2023'][3],2), delta_color="inverse")
        col2.metric("Garis Kemiskinan", df['2024'][4], round(df['2024'][4]-df['2023'][4],2))
        st.caption('Catatan: Dibandingkan dengan tahun 2023')
    
    st.subheader('Jumlah Penduduk Miskin (dalam ribuan)')
    st.bar_chart(df.iloc[0])
    st.subheader('Persentase Penduduk Miskin (P0)')
    st.bar_chart(df.iloc[1])
    st.subheader('Indikator Kedalaman Kemiskinan (P1)')
    st.bar_chart(df.iloc[2])
    st.subheader('Indikator Keparahan Kemiskinan (P2)')
    st.bar_chart(df.iloc[3])
    st.subheader('Garis Kemiskinan')
    st.bar_chart(df.iloc[4])