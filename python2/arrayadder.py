import numpy as np

# Define the two arrays to add
array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])

# Add the two arrays element-wise
sum_array = array1 + array2

# Calculate the average of the sum of each element
avg_array = sum_array / 2

# Print the result array
print("The result array is:", avg_array)
