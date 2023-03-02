import pandas as pd
import numpy as np

# Read the input data from the Excel file
ass = pd.read_excel('king3.xlsx')

# Define the window size for computing rolling means
window_size = 100

# Create an empty list to store the rolling means
rolling_means = []

# Create an empty list to store the data at each interval
interval_data = []

# Loop through the data in intervals of window_size
for i in range(0, len(ass), window_size):
    # Extract the data for the current interval
    data = ass.iloc[i:i+window_size, 0]

    # Append the interval data to the list
    interval_data.append(data)

    # Compute the rolling mean for the current interval
    rolling_mean = np.mean(data)

    # Append the rolling mean to the list
    rolling_means.append(rolling_mean)

# Convert the rolling means list to a NumPy array
rolling_means_array = np.array(rolling_means)

# Save the rolling means array to a CSV file
output_filename = "rolling_means.csv"
np.savetxt(output_filename, rolling_means_array, delimiter=",")

# Print a message to confirm the output file was created
print(f"Rolling means saved to {output_filename}")

# Save the interval data to a text file
data_filename = "data_intervals.txt"
with open(data_filename, "w") as f:
    for i, data in enumerate(interval_data):
        f.write(f"Interval {i+1}:\n")
        f.write(f"{data.to_string(index=False)}\n")
        f.write("\n")

# Print a message to confirm the output file was created
print(f"Interval data saved to {data_filename}")
