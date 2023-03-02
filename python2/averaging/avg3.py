import openpyxl
import csv

# Open the Excel file
workbook = openpyxl.load_workbook('king2.xlsx')

# Select the active worksheet
worksheet = workbook.active

# Initialize an empty array to store the values
values = []

# Iterate through each cell in the worksheet and append the value to the array
for row in worksheet.iter_rows():
    for cell in row:
        values.append(cell.value)

# Loop through every 204 values and group them together in the same cell
group_size = 200
groups = []
for i in range(0, len(values), group_size):
    # Create a list of values for the current group
    group = values[i:i+203]
    
    # Combine the values in the group into a comma-separated string
    group_string = ",".join(str(val) for val in group)
    
    # Append the group string to the list of groups
    groups.append(group_string)

# Write the groups to a CSV file with a "," delimiter
with open('example0.csv', 'w', newline='') as file:
    writer = csv.writer(file, delimiter=',')
    for group in groups:
        writer.writerow([group])
