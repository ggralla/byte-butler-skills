# filename: average_sample_size_function.py
import pandas as pd
from typing import Union

def calculate_average_sample_size(dataset: Union[str, pd.DataFrame]) -> float:
    """
    Calculate the average sample size from the given dataset.
    
    Args:
    - dataset: A file path or a pandas DataFrame containing the dataset with a 'sample' column.
    
    Returns:
    - The average sample size.
    """
    if isinstance(dataset, str):
        df = pd.read_pickle(dataset)
    elif isinstance(dataset, pd.DataFrame):
        df = dataset
    else:
        raise ValueError("The dataset should be a file path or a pandas DataFrame.")
    
    # Extract the sample size and remove any non-numeric characters
    df['sample'] = df['sample'].str.extract('(\d+)').astype(float)
    
    # Calculate the average sample size
    average_sample_size = df['sample'].mean()
    return average_sample_size