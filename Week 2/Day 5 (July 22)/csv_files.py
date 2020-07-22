import csv

with open('ages.csv') as file:
    csv_reader = csv.reader(file, delimiter = ',')
    lines = 0
    sum_ages = 0

    for row in csv_reader:
        lines = lines + 1
        if lines != 1:
            sum_ages = sum_ages + int(row[1])


print(lines)
print(sum_ages/lines)
