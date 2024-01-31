import streamlit as st
from PIL import Image

uploaded_image = st.file_uploader("Upload Image")

with st.expander("Start camera"):
    camera_image = st.camera_input("Camera")

if camera_image:
    img = Image.open(camera_image)
    gray_image = img.convert("L")
    st.image(gray_image)

if uploaded_image:
    img = Image.open(uploaded_image)
    gray_image = img.convert("L")
    st.image(gray_image)