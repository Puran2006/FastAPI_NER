import streamlit as st
import requests
from requests.auth import HTTPBasicAuth

# FastAPI URL (Running Locally)
FASTAPI_URL = "http://localhost:8000/predict"
LOGS_URL = "http://localhost:8000/get_logs"

# Session State for Authentication
if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False
    st.session_state.username = ""
    st.session_state.password = ""

# Function to Call FastAPI for Prediction
def get_prediction(text):
    try:
        # Using stored username and password from session state for authentication
        response = requests.post(
            FASTAPI_URL,
            json={"text": text},
            auth=HTTPBasicAuth(st.session_state.username, st.session_state.password)
        )

        if response.status_code == 200:
            return response.json()
        else:
            st.error("Failed to get prediction. Check your credentials.")
            return None
    except Exception as e:
        st.error(f"Error occurred: {e}")
        return None
    
# Function to Call FastAPI for Logs
def get_logs():
    try:
        response = requests.get(
            LOGS_URL,
            auth=HTTPBasicAuth(st.session_state.username, st.session_state.password)
        )
        if response.status_code == 200:
            return response.json()
        else:
            st.error("Failed to fetch logs. Check your credentials.")
            return None
    except Exception as e:
        st.error(f"Error occurred: {e}")
        return None

# Function to Handle Login
def login_page():
    st.title("Login to Predict Entities")
    
    # Directly set session state values if not set yet
    if 'username' not in st.session_state or 'password' not in st.session_state:
        st.session_state.username = ""
        st.session_state.password = ""
    
    username = st.text_input("Username", value=st.session_state.username)
    password = st.text_input("Password", type="password", value=st.session_state.password)

    if st.button("Login"):
        # Test the API with provided credentials
        response = requests.post(
            FASTAPI_URL,
            json={"text": "test"},
            auth=HTTPBasicAuth(username, password)
        )

        if response.status_code == 200:
            st.session_state.authenticated = True
            st.session_state.username = username
            st.session_state.password = password
            st.success("Login Successful! Redirecting to Predict Page...")
            st.rerun()
        else:
            st.error("Invalid Credentials. Please try again.")

# Prediction Page (After Login)
def predict_page():
    st.title("Named Entity Recognition")
    st.write("Enter the text below to extract entities:")

    text = st.text_area("Input Text", height=150)
    if st.button("Predict"):
        if text.strip() == "":
            st.warning("Please enter some text to predict.")
        else:
            # Call the FastAPI /predict endpoint
            response = get_prediction(text)
            if response:
                st.success("Prediction Successful!")
                st.write(response)               
    if st.button("Show Logs"):
        logs_response = get_logs()
        if logs_response:
            st.success("Logs fetched successfully!")
            st.text_area("Logs", logs_response['logs'], height=300)

    # Logout Button
    if st.button("Logout"):
        st.session_state.authenticated = False
        st.rerun()

# Check Authentication
if not st.session_state.authenticated:
    login_page()
else:
    predict_page()
