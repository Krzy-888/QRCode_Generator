# Libraries
import streamlit as st
import qrcode as qr
from io import BytesIO

# UI
st.set_page_config(page_title="QR Code Generator", layout="centered")
st.title("🥰QR Code Generator")
st.balloons()
In_Path = st.text_input("**Path:**")
Options = ['Regular', 'Custom Colors 🎨','Modified😱']
GenType = st.selectbox("**Select type:**",Options)

# UI After providing path
if In_Path != '':
    # Creating memory bufor
    mem_buf = BytesIO()
    # Normal QR generation
    if GenType == 'Regular':
        st.text('ta-daaa!')
        qr_img = qr.make(In_Path)

    # QR Code with custom colors
    if GenType == 'Custom Colors 🎨':
        qr_img = qr.QRCode(version=1, box_size=10, border=4)
        Code_Color = st.color_picker("Code Color:","#000000")
        Backg_Color = st.color_picker("Background Color:","#FFFFFF")
        qr_img = 

    # Advanced QR generator
    else:
        st.text('commnig soon!')
        qr_img = qr.make('XD')

    # Image Visualization
    st.image(qr_img.get_image())

    # Image saving
    img = qr_img.get_image().save(mem_buf, format="PNG")
    byte_im = mem_buf.getvalue()
    st.download_button('Download', byte_im, 'QRCode.png', 'image/png')