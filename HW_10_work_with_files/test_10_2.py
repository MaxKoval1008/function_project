import csv
rows = []
with open('test_10_2.txt', 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    fields = next(csvreader)
    for row in csvreader:
        rows.append(row)
    print("Total no. of rows: %d" % (csvreader.line_num))
for col in fields:
    print("%10s" % col, end='')
print()
for row in rows[:5]:
    for col in row:
        print("%10s"%col, sep='', end='')
    print()
