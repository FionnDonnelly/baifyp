import csv

with open ('poo.csv', 'r') as csv_file:
	csv_reader = csv.DictReader(csv_file)

	with open('updated_values.csv', 'w') as new_file:
		fieldnames = ['Vce (V)',     'Ic (A)']
		
		csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter=',')

		csv_writer.writeheader()

		for line in csv_reader:
			del line['Ib (A)']
			del line['Vbe (V)']
			del line['Vrc (V)']
			del line['Vrb (V)']
			csv_writer.writerow(line)
		