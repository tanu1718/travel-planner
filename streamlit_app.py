import streamlit as st

# Ensure st.set_page_config is only called once
if "_set_page_config_called" not in st.session_state:
    st.set_page_config(page_title="Travel Partner", layout="wide")
    st.session_state["_set_page_config_called"] = True

# Import other modules AFTER setting the page configuration

homePage = st.Page("HomePage.py", title="HomePage", default=True)

# Navigation logic
pg = st.navigation([homePage])
pg.run()
