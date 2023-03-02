import pandas as pd
import numpy as np

p = input("Enter the row for averaging: ")
p = int(p)
output_filename =  input("Enter output file name: ")
# Read data from excel file
df = pd.read_excel('king.xlsx')

# Create an empty array for storing every 101st value
values = []

# Get the total number of rows in the data
num_rows = df.shape[0]

# Initialize the index variable

# Loop through the data, starting at the second row, and take every 101st value
count = 0
for j in range(0,90):
    i=0
    while i < num_rows:
        value = df.iloc[i+j, p]
        values.append(value)
        i += 101
        
      

# Convert the list of values to a NumPy array
values_array = np.array(values)


# Print the array of values
print(values_array)

# Save the array of values to a text file
np.savetxt('output.txt', values_array)


# Set the input and output file names
input_filename = "output.txt"

# Read the input data from the text file
with open(input_filename, 'r') as f:
    data_str = f.read()

data = pd.read_csv(input_filename)

# Compute the rolling means in intervals of 5 data points
window_size = 5
rolling_means = []
for i in range(0, len(data), window_size):
    rolling_means.append(np.mean(data.iloc[i:i+window_size], axis = 0))

# Convert the rolling means to a NumPy array
rolling_means_array = np.array(rolling_means)


# Save the rolling means array to a CSV file
np.savetxt(output_filename, rolling_means_array, delimiter=",")

# Print a message to confirm the output file was created
print(f"Rolling means saved to {output_filename}")
