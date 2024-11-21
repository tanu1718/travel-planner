import streamlit as st
import chromadb

# Initialize Chromadb Client
client = chromadb.Client()

# Define a collection for user data
user_collection = client.get_or_create_collection("users")

def login_page():
    st.title("Login")
    st.write("Login using your Google account.")

    # Mock Google login with a simple input
    email = st.text_input("Enter your email (mock Google OAuth):", key="email_input")
    if st.button("Continue with Google"):
        if email:
            # Check if user already exists
            user_data = user_collection.get({"email": email})
            if not user_data:
                # If new user, create an entry
                user_collection.insert({"email": email, "name": email.split("@")[0]})
            st.session_state["user"] = email
            st.success(f"Welcome, {email.split('@')[0]}!")
            return True
        else:
            st.error("Please enter a valid email.")
    return False

def get_user():
    return st.session_state.get("user", None)
