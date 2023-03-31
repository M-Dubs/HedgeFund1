import pandas as pd
import numpy as np
import datetime as dt

# Read historical data into a pandas dataframe
data = pd.read_csv('historical_data.csv')

# Define the trading strategy
def trading_strategy(data):
    # Define the moving averages
    ma_short = data['Close'].rolling(window=10).mean()
    ma_long = data['Close'].rolling(window=50).mean()

    # Create a signal when the short-term moving average crosses above the long-term moving average
    data['Signal'] = np.where(ma_short > ma_long, 1, 0)

    # Calculate the daily returns
    data['Returns'] = data['Close'].pct_change()

    # Apply the signal to the returns to calculate the strategy returns
    data['Strategy_Returns'] = data['Signal'].shift(1) * data['Returns']

    # Calculate the cumulative returns
    data['Cumulative_Returns'] = (1 + data['Strategy_Returns']).cumprod()

    return data

# Backtest the trading strategy
backtest_data = trading_strategy(data)

# Plot the cumulative returns
backtest_data['Cumulative_Returns'].plot()
