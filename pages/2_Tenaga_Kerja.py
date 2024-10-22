import pandas as pd
import streamlit as st

st.title('Tenaga Kerja')

tab1, tab2, tab3= st.tabs(["Konsep & Definisi", "Data", "Visualisasi"])
tenaga_kerja = {
    '2019': {'Tingkat Partisipasi Angkatan Kerja (TPAK)': 63.75, 
             'Tingkat Pengangguran Terbuka (TPT)': 6.72,
             'Jumlah Angkatan Kerja': 307022,
             'Jumlah Penduduk Bukan Angkatan Kerja' : 152340,
             'Jumlah Pengangguran': 20635,
             'Jumlah Penduduk Bekerja': 286387
            },
    '2020': {'Tingkat Partisipasi Angkatan Kerja (TPAK)': 65.99, 
             'Tingkat Pengangguran Terbuka (TPT)': 10.49,
             'Jumlah Angkatan Kerja': 296273,
             'Jumlah Penduduk Bukan Angkatan Kerja' : 165756,
             'Jumlah Pengangguran': 31068,
             'Jumlah Penduduk Bekerja': 265205
            },
    '2021': {'Tingkat Partisipasi Angkatan Kerja (TPAK)': 63.12, 
             'Tingkat Pengangguran Terbuka (TPT)': 10.66,
             'Jumlah Angkatan Kerja': 294349,
             'Jumlah Penduduk Bukan Angkatan Kerja' : 171996,
             'Jumlah Pengangguran': 31375,
             'Jumlah Penduduk Bekerja': 262974
            },
    '2022': {'Tingkat Partisipasi Angkatan Kerja (TPAK)': 64.52,
             'Tingkat Pengangguran Terbuka (TPT)': 8.95,
             'Jumlah Angkatan Kerja': 303517,
             'Jumlah Penduduk Bukan Angkatan Kerja' : 166898,
             'Jumlah Pengangguran':27158,
             'Jumlah Penduduk Bekerja': 276359
             },
    '2023': {'Tingkat Partisipasi Angkatan Kerja (TPAK)': 64.85, 
             'Tingkat Pengangguran Terbuka (TPT)': 8.27,
             'Jumlah Angkatan Kerja': 311048,
             'Jumlah Penduduk Bukan Angkatan Kerja' : 168620,
             'Jumlah Pengangguran': 25731,
             'Jumlah Penduduk Bekerja': 285317
            },
}
df = pd.DataFrame(tenaga_kerja)

with tab1:
    st.subheader('Bekerja')
    st.markdown("Bekerja adalah kegiatan ekonomi yang dilakukan seseorang dengan maksud memperoleh atau membantu memperoleh penghasilan atau keuntungan paling sedikit selama satu jam dalam seminggu yang lalu. Kegiatan tersebut termasuk pula kegiatan pekerja tak dibayar yang membantu dalam suatu usaha/kegiatan ekonomi.")

    st.subheader('Penduduk Usia Kerja')
    st.markdown('Penduduk usia kerja adalah penduduk berumur 15 tahun ke atas')
    
    st.subheader('Angkatan Kerja')
    st.markdown('Angkatan kerja adalah penduduk usia kerja yang bekerja dan pengangguran')
    
    st.subheader('Pengangguran')
    st.markdown('''Pengangguran adalah penduduk yang tidak bekerja, kegiatannya terdiri dari:
                
    • Sedang mencari pekerjaan.        
    • Sedang mempersiapkan usaha.      
    • Penduduk yang tidak mencari pekerjaan, karena alasan merasa tidak mungkin mendapatkan pekerjaan (putus asa).
    • Sudah mempunyai pekerjaan tetapi belum mulai bekerja''')

    st.subheader('Tingkat Partisipasi Angkatan Kerja (TPAK)')
    st.markdown('TPAK adalah persentase banyaknya angkatan kerja terhadap banyaknya penduduk usia kerja. TPAK mengindikasikan besarnya persentase penduduk usia kerja yang aktif secara ekonomi di suatu wilayah')

    st.subheader('Tingkat Pengangguran Terbuka (TPT)')
    st.markdown('Tingkat Pengangguran Terbuka (TPT) adalah rasio jumlah penganggur terbuka terhadap jumlah angkatan kerja.')
 
with tab2:
    st.dataframe(data=df, use_container_width=True)
    st.caption('Sumber: Badan Pusat Statistik (BPS)')

with tab3:
    row1 = st.container()
    with row1:
        st.subheader('Kondisi Ketenagakerjaan Kota Jambi 2023')
        col1, col2, col3 = st.columns(3)
        col1.metric("TPAK", df['2023'][0], round(df['2023'][0]-df['2022'][0],2))
        col2.metric("TPT", df['2023'][1], round(df['2023'][1]-df['2022'][1],2), delta_color="inverse")
        col3.metric("Angkatan Kerja", df['2023'][2], round(df['2023'][2]-df['2022'][2],2))
        col1.metric("Bukan Angkatan Kerja", df['2023'][3], round(df['2023'][3]-df['2022'][3],2))
        col2.metric("Pengangguran", df['2023'][4], round(df['2023'][4]-df['2022'][4],2), delta_color="inverse")
        col3.metric("Penduduk Bekerja", df['2023'][5], round(df['2023'][5]-df['2022'][5],2))
        st.caption('Catatan: Dibandingkan dengan tahun 2022')
    
    st.subheader('Tingkat Partisipasi Angkatan Kerja (TPAK)')
    st.bar_chart(df.iloc[0])
    st.subheader('Tingkat Perangguran Terbuka (TPT)')
    st.bar_chart(df.iloc[1])
    st.subheader('Jumlah Angkatan Kerja')
    st.bar_chart(df.iloc[2])
    st.subheader('Jumlah Penduduk Bukan Angkatan Kerja')
    st.bar_chart(df.iloc[3])
    st.subheader('Jumlah Pengangguran')
    st.bar_chart(df.iloc[4])
    st.subheader('Jumlah Penduduk Bekerja')
    st.bar_chart(df.iloc[5])
