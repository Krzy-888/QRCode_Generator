# Libraries
import streamlit as st
import qrcode as qr
from io import BytesIO

# UI
st.title("🥰QR Code Generator")
st.balloons()
In_Path = st.text_input("**Path:**")
Options = ['Regular', 'Modified😱']
GenType = st.selectbox("**Select type:**",Options)

# UI After providing path
if In_Path != '':
    # Creating memory bufor
    mem_buf = BytesIO()
    # Normal QR generation
    if GenType == 'Regular':
        st.text('ta-daaa!')
        qr_img = qr.make(In_Path)
        st.image(qr_img.get_image())
    
    # Advanced QR generator
    else:
        st.text('commnig soon!')
        qr_img = qr.make('XD')
        st.image(qr_img.get_image())
    
    # Image saving
    img = qr_img.get_image().save(mem_buf, format="PNG")
    byte_im = mem_buf.getvalue()
    st.download_button('Download', byte_im, 'QRCode.png', 'image/png')