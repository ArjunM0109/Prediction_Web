import streamlit as st
import pandas as pd
from state import *



# Function to check credentials
def check_credentials(username, password):
    valid_username = "Im_The_King_01"
    valid_password = "11223344"
    return username == valid_username and password == valid_password



# Function to add a name to comman_4 players
def add_comman_name():
    name = st.session_state.comman_name_input
    if name:  # Ensure the name is not empty
        if name in st.session_state.comman_names:
            st.session_state.comman_message = "You can't add duplicate names."
        else:
            if len(st.session_state.comman_names) < 4:
                st.session_state.comman_names.append(name)
                st.session_state.comman_name_input = ''  # Clear the input box
                st.session_state.comman_message = ""  # Clear any previous message
            else:
                st.session_state.comman_message = "You have already entered 4 names."
                # Create a DataFrame from the entered names
                st.session_state.comman_df = pd.DataFrame(st.session_state.comman_names, columns=['Name'])
                st.session_state.comman_df.index += 1  # Adjust index to start from 1

# Function to remove a name from comman_4 players
def remove_comman_name(name):
    st.session_state.comman_names.remove(name)
    # Update the DataFrame
    st.session_state.comman_df = pd.DataFrame(st.session_state.comman_names, columns=['Name'])
    st.session_state.comman_df.index += 1

# Function to add a name to prd_7 players
def add_prd_name():
    name = st.session_state.prd_name_input
    if name:  # Ensure the name is not empty
        if name in st.session_state.prd_names:
            st.session_state.prd_message = "You can't add duplicate names."
        else:
            st.session_state.prd_names.append(name)
            st.session_state.prd_name_input = ''  # Clear the input box
            st.session_state.prd_message = ""  # Clear any previous message
            # Create a DataFrame from the entered names
            st.session_state.prd_df = pd.DataFrame(st.session_state.prd_names, columns=['Name'])
            st.session_state.prd_df.index += 1  # Adjust index to start from 1

# Function to remove a name from prd_7 players
def remove_prd_name(name):
    st.session_state.prd_names.remove(name)
    # Update the DataFrame
    st.session_state.prd_df = pd.DataFrame(st.session_state.prd_names, columns=['Name'])
    st.session_state.prd_df.index += 1











def add_comman_name2():
    name = st.session_state.get('comman_name_input', "").strip()
    if name:
        names_list = st.session_state.get('comman_names_2', [])
        if name in names_list:
            st.session_state['comman_message_2'] = "Comman Player already exists!"
        elif len(names_list) < 2:
            names_list.append(name)
            st.session_state['comman_names_2'] = names_list
            st.session_state['comman_name_input'] = ''
            st.session_state['comman_message_2'] = ""
        else:
            st.session_state['comman_message_2'] = "Maximum 2 Comman Players reached!"
    else:
        st.session_state['comman_message_2'] = "Name cannot be empty!"

def remove_comman_name2(name):
    names_list = st.session_state.get('comman_names_2', [])
    if name in names_list:
        names_list.remove(name)
        st.session_state['comman_names_2'] = names_list
    else:
        st.session_state['comman_message_2'] = "Name not found!"

def add_prd_name2():
    name = st.session_state.get('prd_name_input', "").strip()
    if name:
        names_list = st.session_state.get('prd_names_2', [])
        if name in names_list:
            st.session_state['prd_message_2'] = "Prd Player already exists!"
        elif len(names_list) < 15:
            names_list.append(name)
            st.session_state['prd_names_2'] = names_list
            st.session_state['prd_name_input'] = ''
            st.session_state['prd_message_2'] = ""
        else:
            st.session_state['prd_message_2'] = "Maximum 5 Prd Players reached!"
    else:
        st.session_state['prd_message_2'] = "Name cannot be empty!"

def remove_prd_name2(name):
    names_list = st.session_state.get('prd_names_2', [])
    if name in names_list:
        names_list.remove(name)
        st.session_state['prd_names_2'] = names_list
    else:
        st.session_state['prd_message_2'] = "Name not found!"







def add_all_name():
    name = st.session_state.get('all_name_input', "").strip()
    if name:
        names_list = st.session_state.get('all_names', [])
        if name in names_list:
            st.session_state['all_message'] = "Player already exists!"
        elif len(names_list) < 18:
            names_list.append(name)
            st.session_state['all_names'] = names_list
            st.session_state['all_name_input'] = ''
            st.session_state['all_message'] = ""
        else:
            st.session_state['all_message'] = "Maximum 11 Players reached!"
    else:
        st.session_state['all_message'] = "Name cannot be empty!"

def remove_all_name(name):
    names_list = st.session_state.get('all_names', [])
    if name in names_list:
        names_list.remove(name)
        st.session_state['all_names'] = names_list
    else:
        st.session_state['all_message'] = "Name not found!"



def add_all_name_7():
    name = st.session_state.get('all_name_input_7', "").strip()
    if name:
        names_list = st.session_state.get('all_names_7', [])
        if name in names_list:
            st.session_state['all_message_7'] = "Player already exists!"
        else:
            names_list.append(name)
            st.session_state['all_names_7'] = names_list
            st.session_state['all_name_input_7'] = ''
            st.session_state['all_message_7'] = ""
    else:
        st.session_state['all_message_7'] = "Name cannot be empty!"

def remove_all_name_7(name):
    names_list = st.session_state.get('all_names_7', [])
    if name in names_list:
        names_list.remove(name)
        st.session_state['all_names_7'] = names_list
    else:
        st.session_state['all_message_7'] = "Name not found!"















def count_dt(row):
    return (row == 'dt').sum()