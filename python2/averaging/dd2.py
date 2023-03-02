import pandas as pd
import numpy as np

ass = pd.read_excel('king3.xlsx')

data = ass.iloc[::101, 0]

data.to_csv('data2.csv', index=False)

input_filename = "data2.csv"

# Read the input data from the CSV file
data = pd.read_csv(input_filename)

# Compute the rolling means in intervals of 5 data points
window_size = 5
rolling_means = []
for i in range(0, len(data), window_size):
    rolling_means.append(np.mean(data.iloc[i:i+window_size]))

# Convert the rolling means to a NumPy array
rolling_means_array = np.array(rolling_means)

# Save the rolling means array to a CSV file
output_filename = "pooshit.csv"
np.savetxt(output_filename, rolling_means_array, delimiter=",")

# Print a message to confirm the output file was created
print(f"Rolling means saved to {output_filename}")