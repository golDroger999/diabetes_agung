import sys
sys.path.append('')
import streamlit as st
from datetime import date
import func


hide_streamlit_style="""<style> #MainMenu {visibility: hidden;} footer {visibility: hidden;} </style> """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)


# Create a streamlit app
def main():
    
    st.subheader('perkeni (diabetes)')
    with st.expander('ANTROPOMETRI'):
        col1, col2 = st.columns(2)
        col3, col4, col5 = st.columns(3)
    
        with col1 : nama   = st.text_input('masukan nama anda')         
        with col2 : tanggal = st.date_input('tanggal konseling :', date.today()) 
    
        with col3 :
            bb  = st.number_input('masukan berat badan',1)
            gender = st.selectbox('jenis kelamin', ('pria', 'wanita')) 
    
        with col4:
            tb = st.number_input('masukan tinggi badan',1)
            f_aktiv = st.selectbox('aktivitas', options=('bedrest','ringan', 'sedang', 'berat', 'sangat berat'))
        
        with col5 : 
            umur = st.number_input('masukan usia',1)
            # f_stress = st.number_input('faktor stress', 1.0)
    perkeni = func.perkeni(berat_badan=bb, tinggi_badan=tb, umur=umur, gender=gender, faktor_aktivitas=f_aktiv)   
    # with st.expander('NOTE PROMPT'):
    #     st.write('---------------------')    
    #     # st.subheader('diagnosa penyakit')
    #     keluhan = st.text_input(' DIAGNOSA PENYAKIT PROMPT EDITOR / NOTE')
    #     st.write('---------------------')
    #     biokimia = st.text_area('BIOKIMIA PROMPT EDITOR')
    #     st.write('---------------------')
    #     fisik_klinis = st.text_area('FISIK KLINIS PROMPT EDITOR ')
    #     st.write('---------------------')
    #     st.subheader('RIWAYAT ASUPAN GIZI')
    #     e, p, l, k = st.columns(4)
    #     with e: riwayat_energi = st.number_input('RIWAYAT ENERGI')
    #     with p: riwayat_protein = st.number_input('RIWAYAT PROTEIN')
    #     with l: riwayat_lemak = st.number_input('RIWAYAT LEMAK')
    #     with k: riwayat_karbo = st.number_input('RIWAYAT KARBO')
    #     st.write('---------------------')
        
        
        
    
    if st.button('ANALISA'):
            
        st.subheader('Hasil Perhitungan Gizi')
        with st.expander('HASIL PERHITUNGAN GIZI'):
            
            col1, col2, = st.columns(2)
            
            with col1:
                st.subheader('DATA UKUR')
                st.success(f'BERAT BADAN : {bb} kg')
                st.success(f'TINGGI BADAN : {tb} cm')
                st.success(f'GENDER/SEX : {gender}') 
                st.success(f'UMUR : {umur} tahun')
                st.success(f'IMT : {perkeni["imt"]}')
                st.success(f'BBI : {perkeni["bbi"]}')


            with col2:
                st.subheader('KEBUTUHAN')
                st.success(f'BEE : {perkeni["bmr"]}')
                st.success(f'TEE : {perkeni["energi"]}')
                st.success(f'PROTEIN : {perkeni["protein"]}')
                st.success(f'LEMAK : {perkeni["lemak"]}')
                st.success(f'KARBOHIDRAT : {perkeni["karbo"]}')
                # st.success(f'CAIRAN : {cairan}')
                
                
            # with col9:
            #     st.subheader('RIWAYAT')
            #     st.success(f'ENERGI : {riwayat_energi}')
            #     st.success(f'PROTEIN : {riwayat_protein}')
            #     st.success(f'LEMAK : {riwayat_lemak}')
            #     st.success(f'KARBOHIDRAT : {riwayat_karbo}')
              
            # st.success(modelbot(kata=keluhan))     
        with st.expander('KEBUTUHAN ZAT GIZI SEKALI MAKAN '):
                col3, col4, col5 = st.columns(3)
                with col3:
                    st.subheader('pagi')
                    st.success(f'ENERGI : {perkeni["energi_pagi"]}')
                    st.success(f'PROTEIN : {perkeni["protein_pagi"]}')
                    st.success(f'LEMAK : {perkeni["lemak_pagi"]}')
                    st.success(f'KARBOHIDRAT : {perkeni["karbo_pagi"]}') 

                with col4:
                    st.subheader('siang')
                    st.success(f'ENERGI : {perkeni["energi_pagi"]}')
                    st.success(f'PROTEIN : {perkeni["protein_pagi"]}')
                    st.success(f'LEMAK : {perkeni["lemak_pagi"]}')
                    st.success(f'KARBOHIDRAT : {perkeni["karbo_pagi"]}') 

                with col5:
                    st.subheader('malam')
                    st.success(f'ENERGI : {perkeni["energi_malam"]}')
                    st.success(f'PROTEIN : {perkeni["protein_malam"]}')
                    st.success(f'LEMAK : {perkeni["lemak_malam"]}')
                    st.success(f'KARBOHIDRAT : {perkeni["karbo_malam"]}') 
    
    #     try:                    
    #         penyakit = modelbot(keluhan)                
    #         with st.expander('LIHAT JAWABAN'):
    #             sound_file = BytesIO()
    #             tts = gTTS(f"{penyakit['response']}", lang='id')
    #             tts.write_to_fp(sound_file)
    #             st.success(f"({penyakit['tag']}):")
    #             st.success(f"({penyakit['akurasi']}):")
    #             st.audio(sound_file)
    #             st.markdown(f"<p style='text-align: justify;'>{penyakit['response']}</p>", unsafe_allow_html=True)
    #     except:
    #         st.write('none')
    #         pass                
        

                   
    #     hasil = klasifikasi_biokimia(biokimia)         
    #     if isinstance(hasil, dict):
    #         st.subheader('Hasil Klasifikasi Biokimia')
    #         for nama_biokimia, data in hasil.items():  
    #             with st.expander(f'{nama_biokimia}'):
    #                 st.info(nama_biokimia)
    #                 col6, col7, col8 =  st.columns(3)
    #                 with col6: st.success(f"Nilai: {data['nilai']}")
    #                 with col7: st.success(f"Kategori: {data['kategori']}")
    #                 with col8: st.success(f"rujukan: {data['rujukan']}")
    #                 if data['kategori'] != 'normal':
    #                     st.subheader('penjelasan')
    #                     sound_file = BytesIO()
    #                     tts = gTTS(f"{data['note']}", lang='id')
    #                     tts.write_to_fp(sound_file)
    #                     st.audio(sound_file)
    #                     st.write(f"<p style='text-align:justify'>{data['anjuran']}</p>", unsafe_allow_html=True)
                         
    #     fisik = klasifikasi_fisik_klinis(fisik_klinis)         
    #     if isinstance(fisik, dict):
    #         st.subheader('Hasil Klasifikasi Fisik Klinis')
    #         for nama_fisik_klinis, data in fisik.items():  
    #             with st.expander(f'{nama_fisik_klinis}'):
    #                 st.info(nama_fisik_klinis)
    #                 col6, col7, col8 =  st.columns(3)
    #                 with col6: st.success(f"Nilai: {data['nilai']}")
    #                 with col7: st.success(f"Kategori: {data['kategori']}")
    #                 with col8: st.success(f"rujukan: {data['rujukan']}")
    #                 if data['kategori'] != 'normal':
    #                     st.subheader('penjelasan')
    #                     sound_file = BytesIO()
    #                     tts = gTTS(f"{data['note']}", lang='id')
    #                     tts.write_to_fp(sound_file)
    #                     st.audio(sound_file)
    #                     st.write(f"<p style='text-align:justify'>{data['anjuran']}</p>", unsafe_allow_html=True)
                         

    
    # if st.button('LAPORAN'):
    #     antro = {
    #         'bbi' : int(bbi),
    #         'imt' : int(imt),
    #         'bb' : int(bb) 
    #     }
        
    #     hasil = klasifikasi_biokimia(biokimia)
    #     table=[]
    #     try:
    #         for nama_biokimia, data in hasil.items():
    #             table.append({
    #             'nama': nama_biokimia,
    #             'nilai': data['nilai'],
    #             'hasil': data['kategori'],
    #             'rujukan': data['rujukan'],
    #             'satuan' : data['satuan'],
    #             'rujukan' : data['rujukan'],
    #             'note' : data['note'],
    #             'anjuran' : data['anjuran']            
    #             })
    #     except:
    #         pass

    #     data_fk = klasifikasi_fisik_klinis(fisik_klinis)
    #     fk_table=[]
    #     try:
    #         for nama_fisik_klinis, data in data_fk.items():
    #             fk_table.append({
    #             'nama': nama_fisik_klinis,
    #             'nilai': data['nilai'],
    #             'hasil': data['kategori'],
    #             'rujukan': data['rujukan'],
    #             'satuan' : data['satuan'],
    #             'rujukan' : data['rujukan'],
    #             'note' : data['note'],
    #             'anjuran' : data['anjuran']            
    #             })
    #     except:
    #         pass
        
    #     generate_doc(nama, umur, bb, tb, f_aktiv, 
    #              gender, imt, bbi, bee, tee, protein, lemak, karbo, 
    #              energi_pagi, protein_pagi, lemak_pagi, karbo_pagi,
    #              energi_malam, protein_malam, lemak_malam, karbo_malam,
    #              keluhan,pembahasan="modelbot(kata=keluhan)", mikro=mikro, biokimia=table,
    #              antro=antro, fisik_klinis=fk_table)
        
    #     with open('generate.docx', 'rb') as f:
    #         st.download_button(label='Download Generated Document',
    #                             data=f,
    #                             file_name=f'{nama}.docx',
    #                             mime='application/vnd.openxmlformats-officedocument.wordprocessingml.document')


if __name__ == "__main__":
    main()