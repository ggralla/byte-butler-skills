# filename: election_prediction_function.py
import pandas as pd

def predict_election_winner(data: pd.DataFrame) -> str:
    """
    Predict the winner of an election based on the provided dataset.

    Args:
    data (pd.DataFrame): DataFrame containing election poll data with columns: 'pollster', 'date', 'sample', 'moe', 'Trump', 'Biden', 'spread'.

    Returns:
    str: The predicted winner ('Trump', 'Biden', or 'Tie').
    """
    # Clean the 'sample' column and convert it to numerical values
    data['sample'] = pd.to_numeric(data['sample'].str.extract('(\d+)', expand=False), errors='coerce').fillna(0).astype(int)

    # Calculate the total scores for Trump and Biden
    data['Trump_score'] = data['Trump'] * data['sample'] / 100
    data['Biden_score'] = data['Biden'] * data['sample'] / 100

    # Sum the scores
    total_trump_score = data['Trump_score'].sum()
    total_biden_score = data['Biden_score'].sum()

    # Compare the total scores and determine the winner
    if total_trump_score > total_biden_score:
        return 'Trump'
    elif total_trump_score < total_biden_score:
        return 'Biden'
    else:
        return 'Tie'

# Example usage:
# Load the dataset
data = pd.read_pickle('/home/ec2-user/byte-butler/sample_data/election_polls.pkl')
# Call the function to predict the winner
predicted_winner = predict_election_winner(data)
print(predicted_winner)  # Output the predicted winner