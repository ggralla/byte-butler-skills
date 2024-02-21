# filename: best_poll_finder.py
import pandas as pd

def find_best_poll(dataset_path: str) -> pd.Series:
    """
    Find the best poll based on the largest absolute spread value in the dataset.

    Args:
    dataset_path: The file path of the dataset to be loaded.

    Returns:
    A pandas Series containing the details of the best poll.
    """
    # Load the dataset
    df = pd.read_pickle(dataset_path)

    # Convert 'spread' column to numeric by extracting the numeric value
    df['spread'] = pd.to_numeric(df['spread'].str.replace(r'\D', ''), errors='coerce')

    # Replace NaN values in 'spread' column with 0
    df['spread'].fillna(0, inplace=True)

    # Find the best poll based on the largest absolute value in the 'spread' column
    best_poll = df.loc[abs(df['spread']).idxmax()]

    return best_poll

# Example usage:
dataset_file_path = '/home/ec2-user/byte-butler/sample_data/election_polls.pkl'
best_poll_result = find_best_poll(dataset_file_path)
print(best_poll_result)