import csv

# Open the input CSV file in read mode
with open('updated_values.csv', 'r') as input_csv_file:
    # Create a CSV reader object
    csv_reader = csv.DictReader(input_csv_file)
    
    # Create a list to hold the cleaned data
    cleaned_data = []
    
    # Loop through each row in the CSV file
    for row in csv_reader:
        # Create a new row to hold the cleaned values
        cleaned_row = []
        
        # Loop through each value in the row
        for value in row:
            # Convert the value to a float and check if it's greater than or equal to 0
            if float(row[value]) >= 0:
                # If it's greater than or equal to 0, append it to the cleaned row
                cleaned_row.append(row[value])
        
        # Append the cleaned row to the cleaned data list
        cleaned_data.append(cleaned_row)

# Open the output CSV file in write mode
with open('cleaned_values.csv', 'w', newline='') as output_csv_file:
    fieldnames = ['Vce (V)',     'Ic (A)']
    csv_writer = csv.DictWriter(output_csv_file, fieldnames=fieldnames, delimiter=',')
    
    # Create a CSV writer object
    csv_writer = csv.writer(output_csv_file)
   
    
    # Loop through each row in the cleaned data list and write it to the output CSV file
    for row in cleaned_data:
        csv_writer.writerow(row)
