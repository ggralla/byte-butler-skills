import pandas as pd
from typing import List, Optional

def clean_poll_data(file_path: str, columns_to_keep: List[str], 
                    drop_missing: Optional[List[str]] = None) -> pd.DataFrame:
    """
    Cleans the polling data loaded from a pickle file.

    Parameters:
    - file_path: The file path to the pickle file of the dataset.
    - columns_to_keep: A list of column names that should be retained in the cleaned dataset.
    - drop_missing: Optional; A list of column names to check for missing values; 
                    rows with missing values in these columns will be dropped.

    Returns:
    - A cleaned DataFrame containing only the specified columns with appropriate types 
      and no missing values.
    """
    
    # Load the dataset
    df = pd.read_pickle(file_path)
    
    # Select relevant columns and make a copy
    df_clean = df[columns_to_keep].copy()
    
    # Handle missing values if specified
    if drop_missing:
        df_clean = df_clean.dropna(subset=drop_missing)
    
    # Convert data types for dates and numeric columns
    for column in df_clean.select_dtypes(include=['object']).columns:
        if 'date' in column.lower():
            df_clean[column] = pd.to_datetime(df_clean[column], errors='coerce')
        elif df_clean[column].dtype == 'object':
            df_clean[column] = pd.to_numeric(df_clean[column], errors='coerce')
    
    return df_clean

# Example usage of the function
file_path = '/workspace/4e3f4966-cf09-4258-a463-cb7ff26c37db.pkl'
columns_to_keep = [
    'poll_id', 'pollster', 'state', 
    'start_date', 'end_date', 
    'sponsor_candidate', 'endorsed_candidate_name',
    'sample_size', 'methodology', 
    'election_date', 'party',
    'candidate_name', 'pct'
]
drop_missing = ['pollster', 'state', 'start_date', 'end_date', 'sample_size']

# Clean the dataset
cleaned_data = clean_poll_data(file_path, columns_to_keep, drop_missing)

# Output for verification
print(cleaned_data.head())