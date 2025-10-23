import streamlit as st
from utils import post_request

BACKEND_URL = "http://127.0.0.1:8000/api/chatbot"

def show():
    st.header("💬 Pet Chatbot")

    user_input = st.text_input("Ask about your pet (any language):")

    if st.button("Send"):
        data = {"message": user_input}
        result = post_request(f"{BACKEND_URL}/ask", data)
        if result.get("error"):
            st.error(result["error"])
        else:
            st.success(f"Bot: {result.get('response', 'Sorry, no answer available.')}")
