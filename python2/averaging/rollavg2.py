import pandas as pd

# Define the input and output filenames
input_filename = "data2.csv"
output_filename = "rolling_average_with_column_mean.csv"

# Read the input data from the CSV file
data = pd.read_csv(input_filename)

# Compute the mean of the entire column
column_mean = data.mean().values[0]

# Create a new Series object with the computed column mean and an index label of 'Column Mean'
rolling_average_with_mean = pd.Series(column_mean, index=['Column Mean'])

# Write the resulting Series object to a new CSV file
rolling_average_with_mean.to_csv(output_filename, index=False, header=['Column Mean'])
