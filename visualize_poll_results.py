# filename: poll_visualization_function.py
import pandas as pd
import matplotlib.pyplot as plt
from pandas import DataFrame
from typing import Any

def visualize_poll_results(df: DataFrame, x_col: str, y_cols: list[str]) -> Any:
    """
    Visualizes the spread of the poll results over time using a line plot.

    Args:
    df (DataFrame): The input DataFrame containing poll data.
    x_col (str): The column name for the x-axis representing time (e.g., date).
    y_cols (list[str]): The column names for the y-axis representing the poll results to be plotted.

    Returns:
    None. Displays the line plot visualization.

    Example:
    visualize_poll_results(df, 'date', ['Trump', 'Biden'])
    """
    # Convert date to datetime
    df[x_col] = pd.to_datetime(df[x_col], errors='coerce')

    # Sort the dataframe by date
    df.sort_values(x_col, inplace=True)

    # Plot the poll results over time
    plt.figure(figsize=(12, 6))
    for col in y_cols:
        plt.plot(df[x_col], df[col], label=col, marker='o')
    plt.xlabel('Date')
    plt.ylabel('Percentage')
    plt.title('Poll Results Over Time')
    plt.legend()
    plt.show()

# Load the dataset
df = pd.read_pickle('/workspaces/byte-butler/sample_data/election_polls.pkl')

# Visualize the poll results over time
visualize_poll_results(df, 'date', ['Trump', 'Biden'])