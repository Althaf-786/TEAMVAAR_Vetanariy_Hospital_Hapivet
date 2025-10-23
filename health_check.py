import streamlit as st
from utils import send_image

BACKEND_URL = "http://127.0.0.1:8000/api/healthcheck"

def show():
    st.header("🐶 Animal Health Check")

    uploaded_file = st.file_uploader("Upload Pet Image", type=["jpg", "jpeg", "png"])
    if uploaded_file:
        st.image(uploaded_file, caption="Uploaded Image", use_container_width=True)
        if st.button("Check Health"):
            result = send_image(uploaded_file, f"{BACKEND_URL}/image")
            if result.get("error"):
                st.error(result["error"])
            else:
                st.success(f"Pet Name: {result.get('pet_name', 'Unknown')}")
                st.info(f"Status: {result.get('status', 'Unknown')}")
                st.warning(f"Probable Disease: {result.get('probable_disease', 'None')}")
