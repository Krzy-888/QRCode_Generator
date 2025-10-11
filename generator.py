# Libraries
import streamlit as st
import qrcode as qr
#librarry connection test
#print(st.__name__)
st.title("🥰QR Code Generator")
st.balloons()
In_Path = st.text_input("**Path:**")
Options = ['Regular', 'Modified😱']
GenType = st.selectbox("**Select type:**",Options)
if In_Path != '':
    if GenType == 'Regular':
        st.text('ta-daaa!')
        qr_img = qr.make(In_Path)
        st.image(qr_img.get_image())
        
    else:
        st.text('commnig soon!')
        qr_img = qr_img = qr.make('XD')
        st.image(qr_img.get_image())
    Subm_Button = st.button('Download')
    if Subm_Button:
        qr_img.save('QR.png')