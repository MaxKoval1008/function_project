import csv
fields = ['firstname', 'lastname', 'group']
rows = [
    ['Alex', 'Varkalov', 'Z-21'],
    ['Max', 'Ivanov', 'Z-21'],
]
filename = "students_info.csv"
with open(filename, 'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(fields)
    csvwriter.writerows(rows)
