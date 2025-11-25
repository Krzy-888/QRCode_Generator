# Libraries
import streamlit as st
import qrcode as qr
from io import BytesIO
from PIL import Image

# UI
st.set_page_config(page_title="QR Code Generator", layout="centered")
st.title("🥰QR Code Generator")
st.balloons()
In_Path = st.text_input("**Path:**")
Options = ['Regular', 'Custom Colors 🎨','Custom Colors + Logo 🖼️','Modified😱']
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
    elif GenType == 'Custom Colors 🎨':
        qr_class = qr.QRCode(version=1, box_size=10, border=4)
        col1, col2 = st.columns(2)
        with col1:
            Code_Color = st.color_picker("Code Color:","#000000")
        with col2:
            Backg_Color = st.color_picker("Background Color:","#FFFFFF")
        qr_class.add_data(In_Path)
        qr_img = qr_class.make_image(fill_color=Code_Color, back_color=Backg_Color)

    # QR Code with custom colors
    elif GenType == 'Custom Colors + Logo 🖼️':
        qr_class = qr.QRCode(version=1, box_size=10, border=4)
        col1, col2, col3 = st.columns(3)
        with col1:
            Code_Color = st.color_picker("Code Color:","#000000")
        with col2:
            Backg_Color = st.color_picker("Background Color:","#FFFFFF")
        with col3:
            Image_path = st.file_uploader("Add Image:")
        if Image_path is not None:
            Logo_img = Image.open(Image_path).resize((75,75), Image.LANCZOS)
            qr_class.add_data(In_Path)
            qr_img = qr_class.make_image(fill_color=Code_Color, back_color=Backg_Color)
            offset = ((qr_img.size[0] - 75) // 2, (qr_img.size[1] - 75) // 2)
            qr_img.paste(Logo_img, offset, mask=Logo_img.split()[3] if Logo_img.mode == 'RGBA' else None)
            # Image Visualization
            st.image(qr_img.get_image())

            # Image saving
            img = qr_img.get_image().save(mem_buf, format="PNG")
            byte_im = mem_buf.getvalue()
            st.download_button('Download', byte_im, 'QRCode.png', 'image/png')
        else:
            st.text('Waiting for Image! ⌛')

    # Advanced QR generator
    else:
        st.text('commnig soon!')
        qr_img = qr.make('XD')

    # Image Visualization
    if GenType != 'Custom Colors + Logo 🖼️':
        st.image(qr_img.get_image())

    # Image saving
    if GenType != 'Custom Colors + Logo 🖼️':
        img = qr_img.get_image().save(mem_buf, format="PNG")
        byte_im = mem_buf.getvalue()
        st.download_button('Download', byte_im, 'QRCode.png', 'image/png')