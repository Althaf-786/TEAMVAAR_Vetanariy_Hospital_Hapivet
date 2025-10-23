import streamlit as st
from utils import post_request, get_request

BACKEND_URL = "http://127.0.0.1:8000/api/inventory"

def show():
    st.header("📦 Inventory Management")

    with st.expander("Add Item"):
        item = st.text_input("Item Name")
        quantity = st.number_input("Quantity", min_value=0, step=1)
        expiry = st.date_input("Expiry Date")

        if st.button("Add Item"):
            data = {"item": item, "quantity": quantity, "expiry": str(expiry)}
            result = post_request(f"{BACKEND_URL}/add", data)
            st.success(f"Inventory Item Added: {result.get('item', 'Unknown')}")

    # Show inventory
    if st.button("View Inventory"):
        inventory_list = get_request(f"{BACKEND_URL}/list")
        if inventory_list.get("error"):
            st.error(inventory_list["error"])
        else:
            for inv in inventory_list.get("inventory", []):
                st.write(f"{inv['item']} - Qty: {inv['quantity']} - Expiry: {inv['expiry']}")
