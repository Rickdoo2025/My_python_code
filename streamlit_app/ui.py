import streamlit as st
import requests
import pandas as pd

API_BASE_URL = "http://127.0.0.1:8000"  # Make sure FastAPI is running

st.title("🎬 Actors Database Viewer")

# Sidebar for selecting type of data
option = st.sidebar.selectbox("Select Data Type", ["Actors", "Addresses", "Join Data"])

# Filter input (optional)
if option == "Actors":
    actor_id = st.text_input("Enter Actor ID(s) separated by commas (e.g., 1,2,3)")
    if st.button("Fetch Actors"):
        params = [("actor_id", aid.strip()) for aid in actor_id.split(",")] if actor_id else []
        response = requests.get(f"{API_BASE_URL}/actor", params=params)
        if response.ok:
            data = response.json()
            if isinstance(data, list) and data:
                st.dataframe(pd.DataFrame(data))
            elif isinstance(data, dict) and "error" in data:
                st.warning(data["error"])
            else:
                st.info("No data to display.")
        else:
            st.error("❌ Failed to fetch actor data.")

elif option == "Addresses":
    address_id = st.text_input("Enter Address ID (optional)")
    if st.button("Fetch Addresses"):
        params = {"address_id": address_id} if address_id else {}
        response = requests.get(f"{API_BASE_URL}/address", params=params)
        if response.ok:
            data = response.json()
            if isinstance(data, list) and data:
                st.dataframe(pd.DataFrame(data))
            elif isinstance(data, dict) and "error" in data:
                st.warning(data["error"])
            else:
                st.info("No data to display.")
        else:
            st.error("❌ Failed to fetch address data.")

elif option == "Join Data":
    actor_id = st.text_input("Enter Actor ID (optional)")
    address_id = st.text_input("Enter Address ID (optional)")
    if st.button("Fetch Join Data"):
        params = {}
        if actor_id:
            params["actor_id"] = actor_id
        if address_id:
            params["address_id"] = address_id
        response = requests.get(f"{API_BASE_URL}/join", params=params)
        if response.ok:
            data = response.json()
            if isinstance(data, list) and data:
                st.dataframe(pd.DataFrame(data))
            elif isinstance(data, dict) and "error" in data:
                st.warning(data["error"])
            else:
                st.info("No data to display.")
        else:
            st.error("❌ Failed to fetch joined data.")
