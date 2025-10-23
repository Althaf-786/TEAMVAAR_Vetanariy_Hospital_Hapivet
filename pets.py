import streamlit as st
from utils import post_request, get_request

BACKEND_URL = "http://127.0.0.1:8000/api/pets"

def show():
    st.header("🐾 Manage Pets")

    with st.expander("Add New Pet"):
        name = st.text_input("Pet Name")
        species = st.text_input("Species")
        breed = st.text_input("Breed")
        owner_name = st.text_input("Owner Name")
        owner_contact = st.text_input("Owner Contact")

        if st.button("Add Pet"):
            data = {
                "name": name,
                "species": species,
                "breed": breed,
                "owner_name": owner_name,
                "owner_contact": owner_contact
            }
            result = post_request(f"{BACKEND_URL}/add", data)
            st.success(f"Added Pet: {result.get('name', 'Unknown')}")
