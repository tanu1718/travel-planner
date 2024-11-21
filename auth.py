import streamlit as st
from chromadb_utils import get_chromadb_client

# Initialize ChromaDB client
client = get_chromadb_client()

# Create or get the users collection
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
            try:
                # Check if the user already exists
                user_data = user_collection.get(where={"email": email})  # Query using 'where'
                if len(user_data["ids"]) == 0:  # No existing user
                    # Add new user
                    user_collection.add(
                        ids=[email],  # Use email as the unique ID
                        documents=[{"email": email, "name": email.split("@")[0]}]
                    )
                    st.info("New user added to the database.")
                else:
                    st.info("Welcome back! You are already in the database.")

                # Save the user session
                st.session_state["user"] = email
                st.success(f"Welcome, {email.split('@')[0]}!")
                return True
            except Exception as e:
                st.error(f"Error during login: {e}")
        else:
            st.error("Please enter a valid email.")
    return False


def get_user():
    return st.session_state.get("user", None)
