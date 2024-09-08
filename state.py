import streamlit as st
import pandas as pd

def initialize_session_state():

    # Initialize session state for login
    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = False

    # Initialize session state for comman_4 players
    if 'comman_names' not in st.session_state:
        st.session_state.comman_names = []
    if 'comman_message' not in st.session_state:
        st.session_state.comman_message = ""
    if 'comman_df' not in st.session_state:
        st.session_state.comman_df = pd.DataFrame(columns=['Name'])  # Initialize an empty DataFrame

    # Initialize session state for prd_7 players
    if 'prd_names' not in st.session_state:
        st.session_state.prd_names = []
    if 'prd_message' not in st.session_state:
        st.session_state.prd_message = ""
    if 'prd_df' not in st.session_state:
        st.session_state.prd_df = pd.DataFrame(columns=['Name'])  # Initialize an empty DataFrame


   # Initialize session state for comman_2 players
    if 'comman_names_2' not in st.session_state:
        st.session_state.comman_names_2 = []
    if 'comman_message_2' not in st.session_state:
        st.session_state.comman_message_2 = ""
    if 'comman_df_2' not in st.session_state:
        st.session_state.comman_df_2 = pd.DataFrame(columns=['Name'])  # Initialize an empty DataFrame

    # Initialize session state for prd_7 players
    if 'prd_names_2' not in st.session_state:
        st.session_state.prd_names_2 = []
    if 'prd_message_2' not in st.session_state:
        st.session_state.prd_message_2 = ""
    if 'prd_df' not in st.session_state:
        st.session_state.prd_df_2 = pd.DataFrame(columns=['Name'])  # Initialize an empty DataFrame


    # Initialize session state for all 11 players
    if 'all_names' not in st.session_state:
        st.session_state.all_names = []
    if 'all_message' not in st.session_state:
        st.session_state.all_message = ""

    # Initialize session state for all 7 players
    if 'all_names_7' not in st.session_state:
        st.session_state.all_names_7 = []
    if 'all_message_7' not in st.session_state:
        st.session_state.all_message_7 = ""
