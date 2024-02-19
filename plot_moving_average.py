# filename: moving_average_graph_function.py
import pandas as pd
import matplotlib.pyplot as plt
from typing import List

def plot_moving_average(data: pd.DataFrame, date_column: str, value_column: str, window_size: int, label: str):
    """
    Plot the moving average of a value column from a pandas DataFrame.

    Args:
    data (pd.DataFrame): The input DataFrame containing the data
    date_column (str): The name of the column containing dates for the x-axis
    value_column (str): The name of the column containing the values for which to calculate the moving average
    window_size (int): The size of the window for the moving average
    label (str): The label for the value in the plot legend

    Returns:
    None
    """
    # Convert date column to datetime
    data[date_column] = pd.to_datetime(data[date_column], errors='coerce')

    # Calculate the moving average
    ma_column = f'{value_column}_MA'
    data[ma_column] = data[value_column].rolling(window=window_size).mean()

    # Plot the moving average
    plt.figure(figsize=(10, 6))
    plt.plot(data[date_column], data[ma_column], label=f'{label} Moving Average', color='blue')
    plt.scatter(data[date_column], data[value_column], label=f'{label} Poll Result', color='green')
    plt.xlabel('Date')
    plt.ylabel('Value')
    plt.title(f'{label} Poll Results and Moving Average')
    plt.legend()
    plt.show()

# Load the dataset
df = pd.read_pickle('/workspaces/byte-butler/sample_data/election_polls.pkl')

# Plot the moving average for the Biden poll results
plot_moving_average(df, 'date', 'Biden', 3, 'Biden')