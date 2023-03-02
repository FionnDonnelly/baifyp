import pandas as pd
import numpy as np

# Read data from excel file
df = pd.read_excel('king3.xlsx')

# Create an empty array for storing every 101st value
values = []

# Get the total number of rows in the data
num_rows = df.shape[0]

# Initialize the index variable

# Loop through the data, starting at the second row, and take every 101st value
count=0
for j in range(0,49):
     
    i=0
    while i < num_rows:
        value = df.iloc[i+j, 0]
        values.append(value)
        i += 101
        
    


# Convert the list of values to a NumPy array
values_array = np.array(values)

# Print the array of values
print(values_array)

# Save the array of values to a text file
np.savetxt('output.txt', values_array)