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
    
    with st.expander('NILAI LAB'):
        col1a, col2a = st.columns(2)
        with col1a: gdp  = st.number_input('gula darah puasa',1)
        with col1a: gds  = st.number_input('gula darah sewaktu',1)
        
    perkeni = func.perkeni(berat_badan=bb, tinggi_badan=tb, umur=umur, gender=gender, faktor_aktivitas=f_aktiv)   
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
   
if __name__ == "__main__":
    main()