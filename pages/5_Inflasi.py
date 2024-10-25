import pandas as pd
import requests
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

with tab2:
    id_tahun = ''
    option = st.selectbox("Pilih Tahun Data",("2024", "2023", "2022", "2021", "2020"))

    match option:
        case '2024':
            id_tahun = '124'
        case '2023':
            id_tahun = '123'
        case '2022':
            id_tahun = '122'
        case '2021':
            id_tahun = '121'
        case '2020':
            id_tahun = '120'

    st.subheader('Inflasi Bulan ke Bulan (M to M), '+option)
    with st.expander("Inflasi Bulan ke Bulan (M to M)"):
        api_url = "https://webapi.bps.go.id/v1/api/list/model/data/lang/ind/domain/1571/var/165/key/19cba23ac111b56c7871715f54140d88"

        # Mengambil data dari API
        response = requests.get(api_url)

        if response.status_code == 200:
            data = response.json()  # Konversi respons ke format JSON
        else:
            st.error(f"Failed to fetch data. Status code: {response.status_code}")
        vervar = data['vervar']
        datacontent = data['datacontent']
        bulan = data['turtahun']

        temp = {}
        inflasi = {}
        for i in bulan:
            temp = {}
            for j in vervar:
                try:
                    temp.update({j['label']: datacontent[str(j['val'])+'1650'+id_tahun+str(i['val'])]}) 
                except KeyError:
                    temp.update({j['label']: 0 }) 
            inflasi.update({i['label']: temp})  
        df = pd.DataFrame(inflasi)
        st.dataframe(data=df, use_container_width=True)
        st.caption('Sumber: Badan Pusat Statistik (BPS)')

    st.subheader('Inflasi Tahun ke Tahun (Y to Y), '+option)
    with st.expander("Inflasi Tahun ke Tahun (Y to Y)"):
        api_url1 = "https://webapi.bps.go.id/v1/api/list/model/data/lang/ind/domain/1571/var/114/key/19cba23ac111b56c7871715f54140d88"

        # Mengambil data dari API
        response1 = requests.get(api_url1)

        if response1.status_code == 200:
            data1 = response1.json()  # Konversi respons ke format JSON
        else:
            st.error(f"Failed to fetch data. Status code: {response1.status_code}")
        vervar = data['vervar']
        datacontent1 = data1['datacontent']
        bulan = data['turtahun']

        temp = {}
        inflasi1 = {}
        for i in bulan:
            temp = {}
            for j in vervar:
                try:
                    temp.update({j['label']: datacontent1[str(j['val'])+'1140'+id_tahun+str(i['val'])]}) 
                except KeyError:
                    temp.update({j['label']: 0 }) 
            inflasi1.update({i['label']: temp})  
        df1 = pd.DataFrame(inflasi1)
        st.dataframe(data=df1, use_container_width=True)
        st.caption('Sumber: Badan Pusat Statistik (BPS)')


    st.subheader('Inflasi Tahun Kalender (Y to D), '+option)
    with st.expander("Inflasi Tahun Kalender (Y to D)"):
        api_url2 = "https://webapi.bps.go.id/v1/api/list/model/data/lang/ind/domain/1571/var/164/key/19cba23ac111b56c7871715f54140d88"

        # Mengambil data dari API
        response2 = requests.get(api_url2)

        if response2.status_code == 200:
            data2 = response2.json()  # Konversi respons ke format JSON
        else:
            st.error(f"Failed to fetch data. Status code: {response2.status_code}")
        vervar = data['vervar']
        datacontent2 = data2['datacontent']
        bulan = data['turtahun']

        temp = {}
        inflasi1 = {}
        for i in bulan:
            temp = {}
            for j in vervar:
                try:
                    temp.update({j['label']: datacontent2[str(j['val'])+'1640'+id_tahun+str(i['val'])]}) 
                except KeyError:
                    temp.update({j['label']: 0 }) 
            inflasi1.update({i['label']: temp})  
        df1 = pd.DataFrame(inflasi1)
        st.dataframe(data=df1, use_container_width=True)
        st.caption('Sumber: Badan Pusat Statistik (BPS)')

with tab3:
    st.subheader('Visualisasi Belum Tersedia')