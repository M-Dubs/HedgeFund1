import pandas as pd

# Load historical price data from CSV file
data = pd.read_csv('historical_data.csv')

# Calculate the 20-day and 50-day moving averages
data['MA20'] = data['Close'].rolling(window=20).mean()
data['MA50'] = data['Close'].rolling(window=50).mean()

# Initialize variables for tracking trades
position = None
entry_price = None
exit_price = None
profit = 0

# Loop through each day in the data set
for i in range(len(data)):

    # Check if the 20-day moving average is above the 50-day moving average
    if data['MA20'][i] > data['MA50'][i]:
        
        # If we are not already in a long position, enter the trade
        if position != 'LONG':
            position = 'LONG'
            entry_price = data['Close'][i]
            print('Entered long position at', entry_price)

    # Check if the 20-day moving average is below the 50-day moving average
    elif data['MA20'][i] < data['MA50'][i]:
        
        # If we are in a long position, exit the trade and calculate profit
        if position == 'LONG':
            position = None
            exit_price = data['Close'][i]
            profit += exit_price - entry_price
            print('Exited long position at', exit_price, 'with profit of', exit_price - entry_price)

# Print the total profit from the backtest
print('Total profit from backtest:', profit)
