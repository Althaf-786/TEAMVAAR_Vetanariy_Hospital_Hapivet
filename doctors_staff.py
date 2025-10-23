import streamlit as st
from utils import post_request, get_request

BACKEND_URL = "http://127.0.0.1:8000/api"

def show():
    st.header("👩‍⚕️ Doctors & Staff")

    # Add Doctor
    with st.expander("Add Doctor"):
        name = st.text_input("Doctor Name")
        specialty = st.text_input("Specialty")
        available = st.checkbox("Available", value=True)

        if st.button("Add Doctor"):
            data = {"name": name, "specialty": specialty, "available": available}
            result = post_request(f"{BACKEND_URL}/doctors/add", data)
            st.success(f"Doctor Added: {result.get('name', 'Unknown')}")

    # Add Staff
    with st.expander("Add Staff"):
        name = st.text_input("Staff Name")
        role = st.text_input("Role")
        present = st.checkbox("Present", value=True)

        if st.button("Add Staff"):
            data = {"name": name, "role": role, "present": present}
            result = post_request(f"{BACKEND_URL}/staff/add", data)
            st.success(f"Staff Added: {result.get('name', 'Unknown')}")
