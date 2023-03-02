import pandas as pd
import numpy as np

ass = pd.read_excel('king3.xlsx')

# Compute the rolling means in intervals of 101 data points
window_size = 101
rolling_means = []
for i in range(0, len(ass), window_size):
    data = ass.iloc[i:i+window_size, 0]
    rolling_means.append(np.mean(data))

# Convert the rolling means to a NumPy array
rolling_means_array = np.array(rolling_means)

# Save the rolling means array to a CSV file
output_filename = "pooshit.csv"
np.savetxt(output_filename, rolling_means_array, delimiter=",")

# Print a message to confirm the output file was created
print(f"Rolling means saved to {output_filename}")
