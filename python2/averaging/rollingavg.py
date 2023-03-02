import csv

# Define the size of the window over which we'll compute the average
window_size = 101

# Define the input and output filenames
input_filename = "king2.csv"
output_filename = "rollavg.csv"

# Read the input data from the CSV file
with open(input_filename, "r") as input_file:
    reader = csv.reader(input_file)
    data = []
    for row in reader:
        if row[0]:
            data.append(float(row[0]))

# Compute the rolling average
rolling_average = [sum(data[i:i+window_size])/window_size for i in range(0, len(data)-window_size+1)]

# Write the output data to a new CSV file
with open(output_filename, "w") as output_file:
    writer = csv.writer(output_file)
    for value in rolling_average:
        writer.writerow([value])
