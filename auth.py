import streamlit as st
from chromadb_utils import get_chromadb_client

client = get_chromadb_client()


# Define a collection for user data
user_collection = client.get_or_create_collection(
    name="users",
    metadata={"email": "string", "name": "string"}
)


def login_page():
    st.title("Login")
    st.write("Please log in using your email (mock Google OAuth).")

    # Mock Google login with a text input
    email = st.text_input("Enter your email (e.g., johndoe@gmail.com):", key="email_input")

    if st.button("Continue with Google"):
        if email:
            # Check if user already exists using a filter query
            user_data = user_collection.get(where={"email": email})  # Use 'where' to query by email
            if not user_data:
                # If new user, create an entry
                user_collection.add(ids=[email],  # Use the email as the unique ID
                                    documents=[{"email": email, "name": email.split("@")[0]}])
            st.session_state["user"] = email
            st.success(f"Welcome, {email.split('@')[0]}!")
            return True
        else:
            st.error("Please enter a valid email.")
    return False

def get_user():
    return st.session_state.get("user", None)
