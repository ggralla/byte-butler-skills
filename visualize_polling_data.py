from typing import Any
import pandas as pd
import matplotlib.pyplot as plt

def visualize_polling_data(data: pd.DataFrame, date_column: str, x_variable: str, y_variable: str) -> None:
    """
    Visualizes the polling data using plots and charts to show trends over time or relationships between variables.

    Args:
    - data: The input DataFrame containing the polling data.
    - date_column: The name of the column containing dates.
    - x_variable: The name of the variable to be plotted on the x-axis.
    - y_variable: The name of the variable to be plotted on the y-axis.

    Returns:
    None
    """
    # Plotting trends over time
    data[date_column] = pd.to_datetime(data[date_column].str.split(' - ', expand=True)[0], format='%m/%d')
    data = data.sort_values(date_column)
    plt.figure(figsize=(10, 6))
    plt.plot(data[date_column], data[x_variable], label=x_variable)
    plt.plot(data[date_column], data[y_variable], label=y_variable)
    plt.title(f'{x_variable} vs {y_variable} Polling Trends')
    plt.xlabel('Date')
    plt.ylabel('Percentage')
    plt.legend()
    plt.show()

    # Relationship between variables
    plt.figure(figsize=(10, 6))
    plt.scatter(data[x_variable], data[y_variable])
    plt.title(f'{x_variable} vs {y_variable} Polling Relationship')
    plt.xlabel(x_variable)
    plt.ylabel(y_variable)
    plt.show()


# Example usage:
data = pd.read_pickle('/workspaces/byte-butler/sample_data/election_polls.pkl')
visualize_polling_data(data, 'date', 'Trump', 'Biden')