import streamlit as st
from utils import post_request

def show():
    st.title("🐶 Veterinary Appointment Booking")

    st.subheader("📅 Regular Appointment")
    pet_name = st.text_input("Pet Name")
    owner_name = st.text_input("Owner Name")
    date = st.date_input("Appointment Date")
    time = st.time_input("Appointment Time")
    doctor = st.selectbox("Choose Doctor", ["Dr. Meena", "Dr. Rajesh", "Dr. Anita"])

    if st.button("Book Appointment"):
        data = {
            "pet_name": pet_name,
            "owner_name": owner_name,
            "date": str(date),
            "time": str(time),
            "doctor": doctor,
            "emergency": False
        }
        result = post_request("http://127.0.0.1:8000/api/appointments/book", data)
        if "status" in result:
            st.success(f"✅ {result['status']} with {result['doctor']} on {result['slot']}")
        else:
            st.error(result.get("detail") or result.get("error", "Unknown error occurred"))

    st.markdown("---")
    st.subheader("🚨 Emergency Appointment")

    pet_name_em = st.text_input("Pet Name (Emergency)")
    owner_name_em = st.text_input("Owner Name (Emergency)")
    doctor_em = st.selectbox("Assign Doctor (Emergency)", ["Dr. Meena", "Dr. Rajesh", "On-Call Doctor"])

    if st.button("🚑 Book Emergency Slot"):
        data = {
            "pet_name": pet_name_em,
            "owner_name": owner_name_em,
            "doctor": doctor_em,
            "emergency": True
        }
        result = post_request("http://127.0.0.1:8000/api/appointments/emergency", data)
        if "status" in result:
            st.success(f"⚡ {result['status']} — {result['doctor']} assigned immediately!")
        else:
            st.error(result.get("detail") or result.get("error", "Unknown error occurred"))
