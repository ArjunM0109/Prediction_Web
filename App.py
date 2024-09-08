import streamlit as st
import pandas as pd
from state import *
from helper import *
from functions import *
from auth import *



initialize_session_state()

# Create a login form if not logged in
if not check_login():
    st.title("Team Prediction App")
    show_login()
else:
    st.sidebar.title('Dream Big, Achieve More')
   

    # Options for the dropdown
    options = ['Choose Your Option',"All-11", "All-7", "2 + 5", "4 + 7"]
    selected_option = st.sidebar.selectbox(" Select Prediction Format:", options)

    split_options = ["Single File", "10 Teams", "15 Teams", "20 Teams","25 Teams","30 Teams"]
    team_option = st.sidebar.selectbox(" Select Files Numbers:", split_options)

    dt_options = ["Select Your Team Type","7-Players Team","11-Players Team"]
    dt_count = st.sidebar.selectbox(" Select Team For Dream Count:", dt_options)




    if selected_option == 'Choose Your Option' and dt_count == "Select Your Team Type":
        st.write('Welcome to Bhabha Prediction App')
        st.header('Think More - Win More')
        st.header('Dream Big, Achieve More')





    if selected_option == 'All-11':
        st.header("Enter All Players Name For Predict 11 Players:")
        st.text_input("Enter name:", key='all_name_input')
        st.button("Add Name", key='add_all_button', on_click=add_all_name)
        
        if st.session_state.get('all_message'):
            st.error(st.session_state['all_message'])

        st.write("Entered Players Names:")
        for index, name in enumerate(st.session_state.get('all_names', [])):
            col1, col2, col3 = st.columns([1, 4, 1])
            with col1:
                st.write(index + 1)
            with col2:
                st.write(name)
            with col3:
                if st.button("Remove", key=f"all_{name}"):
                    remove_all_name(name)

        # Ensure at least 11 names are entered
        if len(st.session_state.all_names) >= 11:
            all_names_df = pd.DataFrame(st.session_state.all_names, columns=['Name'])
            all_names_df.index += 1

            
        if st.button('Print CSV (All Players Predicted)'):
            # Check if there are enough players to generate combinations
            if len(st.session_state.all_names) < 11:
                st.error("Not enough players to generate combinations. Please enter at least 11 players.")
            else:
                prd_file = create_All_pred_csv(st.session_state.all_names, 11)  # Assuming you want to use the same names for prediction
                st.write("### Prediction Combinations (All 11)")
                st.write('Total Number of Teams Generated:', prd_file.shape[0])
                if team_option == 'Single File':
                    single_file_name = 'single_file.csv'
                    prd_file.to_csv(single_file_name, index=False)
                    output_files = [single_file_name]
                    with open(single_file_name, 'rb') as f:
                        st.download_button(
                            label="Download Single File",
                            data=f,
                            file_name=single_file_name,
                            mime='text/csv'
                        )
                else:
                    num_teams = int(team_option.split()[0])
                    output_files = split_file(prd_file, num_teams)

                    # Individual download buttons for each file
                    for file in output_files:
                        with open(file, 'rb') as f:
                            st.download_button(
                                label=f"Download {file}",
                                data=f,
                                file_name=file,
                                mime='text/csv'
                            )
                    # Create and provide a download button for the ZIP file containing all CSV files
                    zip_buffer = create_zip(output_files)
                    st.download_button(
                        label="Download All Files (ZIP)",
                        data=zip_buffer,
                        file_name='all_files.zip',
                        mime='application/zip'
                    )





    if selected_option == "All-7":
        st.header("Enter All Players Name For Predict 7 Players:")
        st.text_input("Enter name:", key='all_name_input_7')
        st.button("Add Name", key='add_all_button_7', on_click=add_all_name_7)

        if st.session_state.get('all_message_7'):
            st.error(st.session_state['all_message_7'])

        st.write("Entered Players Names:")
        
        # Ensure the session state variable is initialized
        if 'all_names_7' not in st.session_state:
            st.session_state.all_names_7 = []

        for index, name in enumerate(st.session_state.all_names_7):
            col1, col2, col3 = st.columns([1, 4, 1])
            with col1:
                st.write(index + 1)
            with col2:
                st.write(name)
            with col3:
                if st.button("Remove", key=f"all_{name}_7"):
                    remove_all_name_7(name)

        # Ensure at least 8 names are entered (minimum more than 7)
        if len(st.session_state.all_names_7) > 7:
            all_names_df = pd.DataFrame(st.session_state.all_names_7, columns=['Name'])
            all_names_df.index += 1

        if st.button('Print CSV (All Players Predicted)'):
            # Check if there are enough players to generate combinations
            if len(st.session_state.all_names_7) < 7:  # Change this to all_names_7
                st.error("Not enough players to generate combinations. Please enter at least 7 players.")
            else:
                prd_file = create_All_pred_csv(st.session_state.all_names_7, 7)  # Assuming you want to use the same names for prediction
                st.write("### Prediction Combinations (All 11)")
                st.write('Total Number of Teams Generated:', prd_file.shape[0])
                if team_option == 'Single File':
                    single_file_name = 'single_file.csv'
                    prd_file.to_csv(single_file_name, index=False)
                    output_files = [single_file_name]
                    with open(single_file_name, 'rb') as f:
                        st.download_button(
                            label="Download Single File",
                            data=f,
                            file_name=single_file_name,
                            mime='text/csv'
                        )
                else:
                    num_teams = int(team_option.split()[0])
                    output_files = split_file(prd_file, num_teams)

                    # Individual download buttons for each file
                    for file in output_files:
                        with open(file, 'rb') as f:
                            st.download_button(
                                label=f"Download {file}",
                                data=f,
                                file_name=file,
                                mime='text/csv'
                            )
                    # Create and provide a download button for the ZIP file containing all CSV files
                    zip_buffer = create_zip(output_files)
                    st.download_button(
                        label="Download All Files (ZIP)",
                        data=zip_buffer,
                        file_name='all_files.zip',
                        mime='application/zip'
                    )






    if selected_option == "4 + 7":
        st.title("For 11 Player ( Formate 4 + 7 )")

        # Section for comman_4 players
        st.header("Enter 4 Comman Players name:")
        st.text_input("Enter name:", key='comman_name_input')
        st.button("Add Comman Name", on_click=add_comman_name)
        # Display any messages for comman_4 players
        if st.session_state.comman_message:
            st.error(st.session_state.comman_message)
        # Display the list of entered comman_4 players names with index numbers
        st.write("Entered Comman Players Names:")
        for index, name in enumerate(st.session_state.comman_names):
            col1, col2, col3 = st.columns([1, 4, 1])  # Create three columns for index, name, and remove button
            with col1:
                st.write(index + 1)  # Display the index (1-based)
            with col2:
                st.write(name)  # Display the name
            with col3:
                if st.button("Remove", key=f"comman_{name}"):  # Create a remove button for each name
                    remove_comman_name(name)
        # Update the DataFrame for comman_4 players
        st.session_state.comman_df = pd.DataFrame(st.session_state.comman_names, columns=['Name'])
        st.session_state.comman_df.index += 1  # Adjust index to start from 1
        # Display the DataFrame for comman_4 players if any names are entered
        if st.session_state.comman_df.shape[0] == 4:
            comman_4 = st.session_state.comman_df


        st.header("Enter more than 7 Prd Players name:")
        st.text_input("Enter name:", key='prd_name_input')
        st.button("Add Prd Name", on_click=add_prd_name)
        # Display any messages for prd_7 players
        if st.session_state.prd_message:
            st.error(st.session_state.prd_message)
        # Display the list of entered prd_7 players names with index numbers
        st.write("Entered Prd Players Names:")
        for index, name in enumerate(st.session_state.prd_names):
            col1, col2, col3 = st.columns([1, 4, 1])  # Create three columns for index, name, and remove button
            with col1:
                st.write(index + 1)  # Display the index (1-based)
            with col2:
                st.write(name)  # Display the name
            with col3:
                if st.button("Remove", key=f"prd_{name}"):  # Create a remove button for each name
                    remove_prd_name(name)
        # Update the DataFrame for prd_7 players
        st.session_state.prd_df = pd.DataFrame(st.session_state.prd_names, columns=['Name'])
        st.session_state.prd_df.index += 1  # Adjust index to start from 1
        # Display the DataFrame for prd_7 players if any names are entered
        if st.session_state.prd_df.shape[0] > 7:
            prd_7 = st.session_state.prd_df

        if st.button('generate predicted team'):
            prd_file = gen_comman(comman_4,prd_7,7)
            st.write("### Prediction Combinations :(4 + 7)")
            st.write('Total Number of Teams Generated:', prd_file.shape[0])
                        
            if team_option == 'Single File':
                single_file_name = 'single_file.csv'
                prd_file.to_csv(single_file_name, index=False)
                output_files = [single_file_name]
                with open(single_file_name, 'rb') as f:
                    st.download_button(
                    label="Download Single File",
                    data=f,
                    file_name=single_file_name,
                    mime='text/csv'
                    )
            else:
                num_teams = int(team_option.split()[0])
                output_files = split_file(prd_file, num_teams)

                # Individual download buttons for each file
                for file in output_files:
                    with open(file, 'rb') as f:
                        st.download_button(
                        label=f"Download {file}",
                        data=f,
                        file_name=file,
                        mime='text/csv'
                        )
            # Create and provide a download button for the ZIP file containing all CSV files
                zip_buffer = create_zip(output_files)
                st.download_button(
                    label="Download All Files (ZIP)",
                    data=zip_buffer,
                    file_name='all_files.zip',
                    mime='application/zip'
                    )
    


# Main code block for "2 + 5" format
    if selected_option ==  "2 + 5":
        st.title("For 7 Player (Format 2 + 5)")

        st.header("Enter 2 Comman Players name:")
        st.text_input("Enter name:", key='comman_name_input')
        st.button("Add Comman Name", key='add_comman_button', on_click=add_comman_name2)
        if st.session_state.get('comman_message_2'):
            st.error(st.session_state['comman_message_2'])

        st.write("Entered Comman Players Names:")
        for index, name in enumerate(st.session_state.get('comman_names_2', [])):
            col1, col2, col3 = st.columns([1, 4, 1])
            with col1:
                st.write(index + 1)
            with col2:
                st.write(name)
            with col3:
                if st.button("Remove", key=f"comman_{name}"):
                    remove_comman_name2(name)

        st.session_state.comman_df_2 = pd.DataFrame(st.session_state.get('comman_names_2', []), columns=['Name'])
        st.session_state.comman_df_2.index += 1
        comman_2 = st.session_state.comman_df_2 if st.session_state.comman_df_2.shape[0] == 2 else None

        st.header("Enter more than 5 Prd Players name:")
        st.text_input("Enter name:", key='prd_name_input')
        st.button("Add Prd Name", key='add_prd_button', on_click=add_prd_name2)
        if st.session_state.get('prd_message_2'):
            st.error(st.session_state['prd_message_2'])

        st.write("Entered Prd Players Names:")
        for index, name in enumerate(st.session_state.get('prd_names_2', [])):
            col1, col2, col3 = st.columns([1, 4, 1])
            with col1:
                st.write(index + 1)
            with col2:
                st.write(name)
            with col3:
                if st.button("Remove", key=f"prd_{name}"):
                    remove_prd_name2(name)

        st.session_state.prd_df_2 = pd.DataFrame(st.session_state.get('prd_names_2', []), columns=['Name'])
        st.session_state.prd_df_2.index += 1
        prd_5 = st.session_state.prd_df_2 if st.session_state.prd_df_2.shape[0] > 5 else None

       
        if st.button('generate predicted team'):
            prd_file = gen_comman(comman_2,prd_5,5)
            st.write("### Prediction Combinations :(4 + 7)")
            st.write('Total Number of Teams Generated:', prd_file.shape[0])
                        
            if team_option == 'Single File':
                single_file_name = 'single_file.csv'
                prd_file.to_csv(single_file_name, index=False)
                output_files = [single_file_name]
                with open(single_file_name, 'rb') as f:
                    st.download_button(
                    label="Download Single File",
                    data=f,
                    file_name=single_file_name,
                    mime='text/csv'
                    )
            else:
                num_teams = int(team_option.split()[0])
                output_files = split_file(prd_file, num_teams)

                # Individual download buttons for each file
                for file in output_files:
                    with open(file, 'rb') as f:
                        st.download_button(
                        label=f"Download {file}",
                        data=f,
                        file_name=file,
                        mime='text/csv'
                        )
            # Create and provide a download button for the ZIP file containing all CSV files
                zip_buffer = create_zip(output_files)
                st.download_button(
                    label="Download All Files (ZIP)",
                    data=zip_buffer,
                    file_name='all_files.zip',
                    mime='application/zip'
                    )


    



    if dt_count == "11-Players Team" and selected_option == "Choose Your Option":

        uploaded_file = st.file_uploader("Choose a CSV file", type=["csv"])

        if uploaded_file is not None:
            # Read the uploaded CSV file into a DataFrame
            df = pd.read_csv(uploaded_file)
            num_columns = df.shape[1]
    
            # Validate the number of columns
            if num_columns < 11 or num_columns > 11:
                st.error("Error: The uploaded CSV file must contain exactly 11 columns. Please select a correct format file.")
            else:
                # Get unique values across all columns
                unique_values = pd.unique(df.values.ravel('K'))
                
                options = unique_values
                # Create a multi-select dropdown
                selected_options = st.multiselect(
                    'Select Dream Players:',
                    options,
                )
                # Replace names with 'dt' in specific columns
                df.replace(selected_options, 'dt', inplace=True)
                df['Dream_count'] = df.apply(count_dt, axis=1)


                # Count Dream Players (6, 7, 8, 9, 10, 11)
                dt_6 = (df['Dream_count'] == 6).sum()
                dt_7 = (df['Dream_count'] == 7).sum()
                dt_8 = (df['Dream_count'] == 8).sum()
                dt_9 = (df['Dream_count'] == 9).sum()
                dt_10 = (df['Dream_count'] == 10).sum()
                dt_11 = (df['Dream_count'] == 11).sum()

                st.write('.........................................................................................')


                st.write('6-dt Players in team : ',dt_6)
                st.write('7-dt Players in team : ',dt_7)
                st.write('8-dt Players in team : ',dt_8)
                st.write('9-dt Players in team : ',dt_9)
                st.write('10-dt Players in team : ',dt_10)
                st.write('11-dt Players in team : ',dt_11)

                st.write('.........................................................................................')


                filtered_df = df[df['Dream_count'] > 5].reset_index(drop=False)
                sorted_filtered_df = filtered_df.sort_values('Dream_count')
                st.write()
                st.write(sorted_filtered_df.reset_index(drop=True))
        else:
            st.warning("Please upload a CSV file.")




    if dt_count == "7-Players Team" and selected_option == "Choose Your Option":

        uploaded_file = st.file_uploader("Choose a CSV file", type=["csv"])

        if uploaded_file is not None:
            # Read the uploaded CSV file into a DataFrame
            df = pd.read_csv(uploaded_file)
            num_columns = df.shape[1]
    
            # Validate the number of columns
            if num_columns < 7 or num_columns > 7:
                st.error("Error: The uploaded CSV file must contain exactly 7 columns. Please select a correct format file.")
            else:
                # Get unique values across all columns
                unique_values = pd.unique(df.values.ravel('K'))
                
                options = unique_values
                # Create a multi-select dropdown
                selected_options = st.multiselect(
                    'Select Dream Players:',
                    options,
                )
                # Replace names with 'dt' in specific columns
                df.replace(selected_options, 'dt', inplace=True)
                df['Dream_count'] = df.apply(count_dt, axis=1)


                # Count Dream Players (3,4,5,6,7)
                dt_3 = (df['Dream_count'] == 3).sum()
                dt_4 = (df['Dream_count'] == 4).sum()
                dt_5 = (df['Dream_count'] == 5).sum()
                dt_6 = (df['Dream_count'] == 6).sum()
                dt_7 = (df['Dream_count'] == 7).sum()

                st.write('.........................................................................................')


                st.write('3-dt Players in team : ',dt_3)
                st.write('4-dt Players in team : ',dt_4)
                st.write('5-dt Players in team : ',dt_5)
                st.write('6-dt Players in team : ',dt_6)
                st.write('7-dt Players in team : ',dt_7)

                st.write('.........................................................................................')


                filtered_df = df[df['Dream_count'] > 2].reset_index(drop=False)
                sorted_filtered_df = filtered_df.sort_values('Dream_count')
                st.write()
                st.write(sorted_filtered_df.reset_index(drop=True))
        else:
            st.warning("Please upload a CSV file.")