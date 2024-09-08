import pandas as pd
import zipfile
import itertools
from io import BytesIO

def gen_comman(comman,prd,n):
    df = pd.DataFrame(comman, columns=['Common Players'])
    df2 = pd.DataFrame(prd, columns=['Prediction'])
    common_players = comman['Name'].tolist()  # Common players
    players = prd['Name'].tolist()            # Prediction players

    # Generate combinations of players from the predictions
    combinations = list(itertools.combinations(players, n))

    # Create a DataFrame for the predictions
    prd_df = pd.DataFrame(combinations)

    # Insert the common players as the first columns
    for i in range(len(common_players)):
        prd_df.insert(i, f'Player-{i + 1}', common_players[i])

    # Set the column names
    predicted_columns = [f'Predicted Player-{i+1 + len(common_players)}' for i in range(n)]
    prd_df.columns = [f'Player-{i + 1}' for i in range(len(common_players))] + predicted_columns

    return prd_df


def create_All_pred_csv(names,n):
    df = pd.DataFrame(names, columns=['Common Players'])
    players = df['Common Players'].tolist()  # Common players

    # Generate combinations of players from the predictions
    combinations = list(itertools.combinations(players, n))

    # Create a DataFrame for the predictions
    prd_df = pd.DataFrame(combinations)

    # Set the column names
    prd_df.columns = [f'Predicted Player-{i+1}' for i in range(n)]

    return prd_df

# Function to split files
def split_file(file, n):
    rows_per_file = n
    num_files = len(file) // rows_per_file + (1 if len(file) % rows_per_file != 0 else 0)
    output = []

    for i in range(num_files):
        start_row = i * rows_per_file
        end_row = (i + 1) * rows_per_file
        chunk = file.iloc[start_row:end_row]
        output_file = f'output_{i + 1}.csv'
        chunk.to_csv(output_file, index=False)
        output.append(output_file)

    return output


def create_zip(files):
    # Create a ZIP file from the list of files
    buffer = BytesIO()
    with zipfile.ZipFile(buffer, 'w') as zip_file:
        for file in files:
            zip_file.write(file)
    buffer.seek(0)
    return buffer
