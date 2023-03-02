import pandas as pd
import numpy as np

# Read data from excel file
df = pd.read_excel('king3.xlsx')

# Create an empty array for storing every 101st value
values = []

# Get the total number of rows in the data
num_rows = df.shape[0]

# Loop through the data, starting at the second row, and take every 101st value
i = 1
#for j in range(itt, 196):
step = 0
while i in range(step, num_rows, 101):
    value = df.iloc[i, 0]
    values.append(value)
    i = i+1

# Convert the list of values to a NumPy array
values_array = np.array(values)

# Print the array of values
print(values_array)

# Save the array of values to a text file
np.savetxt('output.txt', values_array)
