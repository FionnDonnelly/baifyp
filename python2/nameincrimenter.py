import csv
import numpy as np


for i in range (0,2):
    i = str(i)
    arrayname = 'T'+ i + '.csv'
    print(arrayname)
    arrays = np.loadtxt(arrayname, delimiter=',')
    print(arrays)


# Add the two arrays element-wise
sum_array = arrays 

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

