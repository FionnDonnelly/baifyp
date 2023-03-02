import pandas as pd

# Define the size of the window over which we'll compute the average
window_size = 101

# Define the input filename
input_filename = "king2.xlsx"

# Read the input data from the Excel file
data = pd.read_excel(input_filename)

# Compute the rolling average
rolling_average = data.iloc[::window_size, :].mean(axis=1)

# Print the rolling average to the console
print(rolling_average.mean())

