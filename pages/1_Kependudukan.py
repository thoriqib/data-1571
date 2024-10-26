import pandas as pd
import streamlit as st

st.title('Kependudukan')
 
tab1, tab2, tab3= st.tabs(["Konsep & Definisi", "Data", "Visualisasi"])

with tab1:
    st.subheader('Penduduk')
    st.markdown("Penduduk dengan pengeluaran per kapita per bulan di bawah garis kemiskinan")

    st.subheader('Laju Pertumbuhan Penduduk')
    st.markdown('Suatu representasi dari jumlah rupiah minimum yang dibutuhkan untuk memenuhi kebutuhan pokok minimum makanan dan kebutuhan pokok bukan makanan. Garis Kemiskinan dipergunakan sebagai suatu batas untuk mengelompokkan penduduk menjadi miskin atau tidak miskin. Penduduk miskin adalah penduduk yang memiliki rata-rata pengeluaran per kapita per bulan di bawah Garis Kemiskinan')
    
    st.subheader('Kepadatan Penduduk')
    st.markdown('Indikator P1 merupakan ukuran rata-rata kesenjangan pengeluaran masing-masing penduduk miskin terhadap garis kemiskinan. Jika ditemukan angka P1 yang semakin mendekati 0, maka kondisi ini menunjukkan rata-rata pengeluaran penduduk miskin semakin mendekati Garis Kemiskinan.')

    st.subheader('Rasio Jenis Kelamin')
    st.markdown('Perbandingan antara jumlah penduduk')

with tab2:
    # st.dataframe(data=df, use_container_width=True)
    option = st.selectbox("Pilih Tahun Data",("2024", "2023", "2022", "2021", "2020", "2019", "2018", "2017"))
    url = "https://webapi.bps.go.id/v1/api/interoperabilitas/datasource/simdasi/id/25/tahun/"+option+"/id_tabel/WVRlTTcySlZDa3lUcFp6czNwbHl4QT09/wilayah/1571000/key/19cba23ac111b56c7871715f54140d88"
    df = pd.read_json(url)
    if df['data'][1]['status'] == 200:
        pddk = {}
        for i in df['data'][1]['kolom']: 
            temp = {}
            for j in df['data'][1]['data']:
                temp[j['label']] = j['variables'][i]['value']
            if i == "nzudy5elv7":
                pddk[df['data'][1]['kolom'][i]['nama_variabel']+' (ribu jiwa)'] = temp   
            else: pddk[df['data'][1]['kolom'][i]['nama_variabel']] = temp   
        pddk = pd.DataFrame(pddk)
        st.subheader('Data Kependudukan Tahun ' + option + ' Kota Jambi')
        st.dataframe(data=pddk, use_container_width=True)
    else : st.subheader('Data ' + option + ' Belum Tersedia')
    
    st.caption('Sumber: Badan Pusat Statistik (BPS)')
 
# with tab3:
#     row1 = st.container()
#     with row1:
#         st.subheader('Indikator Kemiskinan Kota Jambi 2023')
#         col1, col2, col3 = st.columns(3)
#         col1.metric("Jumlah Penduduk Miskin", df['2023'][0], round(df['2023'][0]-df['2022'][0],2), delta_color="inverse")
#         col2.metric("Persentase Penduduk Miskin (P0)", df['2023'][1], round(df['2023'][1]-df['2022'][1],2), delta_color="inverse")
#         col3.metric("Indikator Kedalaman Kemiskinan (P1)", df['2023'][2], round(df['2023'][2]-df['2022'][2],2))
#         col1.metric("Indikator Keparahan Kemiskinan (P2)", df['2023'][3], round(df['2023'][3]-df['2022'][3],2))
#         col2.metric("Garis Kemiskinan", df['2023'][4], round(df['2023'][4]-df['2022'][4],2))
#         st.caption('Catatan: Dibandingkan dengan tahun 2022')
    
#     st.subheader('Jumlah Penduduk Miskin (dalam ribuan)')
#     st.bar_chart(df.iloc[0])
#     st.subheader('Persentase Penduduk Miskin (P0)')
#     st.bar_chart(df.iloc[1])
#     st.subheader('Indikator Kedalaman Kemiskinan (P1)')
#     st.bar_chart(df.iloc[2])
#     st.subheader('Indikator Keparahan Kemiskinan (P2)')
#     st.bar_chart(df.iloc[3])
#     st.subheader('Garis Kemiskinan')
#     st.bar_chart(df.iloc[4])