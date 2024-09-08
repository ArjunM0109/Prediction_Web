import streamlit as st

def show_login():
    st.text_input("Username", key="username")
    st.text_input("Password", key="password", type="password")
    if st.button("Login"):
        st.session_state.logged_in = True

def check_login():
    return st.session_state.get('logged_in', False)
