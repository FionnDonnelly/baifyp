import csv
import numpy as np

# Define the file names and paths
file_paths = ['T1.csv', 'T2.csv']

# Define a dictionary to store the arrays for each file
file_arrays = {}

# Loop through each file and create an array for each
for file_path in file_paths:
    # Create an empty list to store the data for this file
    data = []
    # Open the file and read in the data
    with open(file_path, 'r') as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            data.append(row)
    # Store the data array in the dictionary using the file name as the key
    file_name = file_path.split('/')[-1].split('.')[0]
    file_arrays[file_name] = data

# Write the arrays to text files
for file_name, array in file_arrays.items():
    with open(f'{file_name}.txt', 'w') as txt_file:
        for row in array:
            txt_file.write(','.join(row) + '\n')
    print(f'Successfully wrote array for {file_name} to {file_name}.txt')

    # Define the two arrays to add
array1 = np.loadtxt('T1.csv', delimiter=',')
array2 = np.loadtxt('T3.csv', delimiter=',')

# Add the two arrays element-wise
sum_array = array1 + array2

# Calculate the average of the sum of each element
avg_array = sum_array / 2

# Print the result array
print("The result array is:", avg_array)

with open('avg_array.csv', 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    for row in avg_array:
        writer.writerow(row)

# Print a message to indicate that the file has been written
print("Successfully wrote avg_array to avg_array.csv")

