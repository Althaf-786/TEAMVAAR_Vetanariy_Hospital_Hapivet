import streamlit as st
from pages import health_check, pets, appointments, doctors_staff, inventory, chatbot

st.set_page_config(page_title="AI Veterinary Hospital", layout="wide")
st.title("🐾 AI Veterinary Hospital Management System")

menu = ["Animal Health Check", "Pets", "Appointments", "Doctors & Staff", "Inventory", "Chatbot"]
choice = st.sidebar.selectbox("Menu", menu)

if choice == "Animal Health Check":
    health_check.show()
elif choice == "Pets":
    pets.show()
elif choice == "Appointments":
    appointments.show()
elif choice == "Doctors & Staff":
    doctors_staff.show()
elif choice == "Inventory":
    inventory.show()
elif choice == "Chatbot":
    chatbot.show()
