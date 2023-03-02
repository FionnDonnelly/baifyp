import openpyxl
import csv

# Open the Excel file
workbook = openpyxl.load_workbook('king.xlsx')

# Select the active worksheet
worksheet = workbook.active

# Initialize an empty array to store the values
values = []

# Iterate through each cell in the worksheet and append the value to the array
for row in worksheet.iter_rows():
    for cell in row:
        values.append(cell.value)

# Loop through every 204 values and group them together in the same cell
groups = []
for i in range(0, len(values), 204):
    # Create a list of values for the current group
    group = values[i:i+204]
    
    # Combine the first and last value of the group into a string
    group_string = str(group[0]) + "-" + str(group[-1])
    
    # Append the group string to the list of groups
    groups.append(group_string)

# Write the groups to a CSV file with a "," delimiter
with open('example.csv', 'w', newline='') as file:
    writer = csv.writer(file, delimiter=',')
    writer.writerow(groups)
