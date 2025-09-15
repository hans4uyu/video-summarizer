import streamlit as st

st.set_page_config(page_title="Video App", page_icon="🎥", layout="centered")

st.title("🎥 Video Processing App")

st.markdown(
    """
    Selamat datang!  
    Pilih menu di sidebar:
    - **Upload Video** → untuk unggah file video lokal  
    - **Link Video** → untuk masukkan link YouTube  
    """
)
