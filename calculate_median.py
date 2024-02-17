# filename: median_calculator.py
import pandas as pd

def calculate_median(data: pd.DataFrame, pollster: str = None) -> pd.Series:
    """
    Calculate the median value of a numeric column for a specific pollster or across the entire dataset.
    
    Args:
    data: A pandas DataFrame containing the dataset.
    pollster: A string representing the name of the pollster. If None, median is calculated across the entire dataset.
    
    Returns:
    A pandas Series containing the median values for 'Trump' and 'Biden' columns.
    """
    if pollster:
        median_value = data[data['pollster'] == pollster][['Trump', 'Biden']].median()
    else:
        median_value = data[['Trump', 'Biden']].median()
    return median_value

# Load the dataset
dataset = pd.read_pickle('/home/ec2-user/byte-butler/sample_data/election_polls.pkl')

# Call the function to calculate median value
print(calculate_median(dataset))
print(calculate_median(dataset, 'Morning Consult'))