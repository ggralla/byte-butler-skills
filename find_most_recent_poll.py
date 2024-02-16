# filename: recent_poll.py
import pandas as pd

def find_most_recent_poll(data: pd.DataFrame) -> pd.Series:
    """
    Find the most recent poll in the dataset.

    Args:
    data: A pandas DataFrame containing the poll data with a 'date' column.

    Returns:
    A pandas Series representing the most recent poll.
    """
    # Convert the date column to datetime format
    data['date'] = data['date'].str.extract(r'(\d{1,2}/\d{1,2})').astype(str) + "/2021"
    data['date'] = pd.to_datetime(data['date'], format='%m/%d/%Y', errors='coerce')

    # Find the most recent poll
    most_recent_poll = data.loc[data['date'].idxmax()]
    
    return most_recent_poll

# Example usage
data = pd.read_pickle('/home/ec2-user/byte-butler/sample_data/election_polls.pkl')
most_recent = find_most_recent_poll(data)
print(most_recent)