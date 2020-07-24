import csv

with open('my_ideas.csv', 'w', newline='') as file:
    csv_writer = csv.writer(file, delimiter = ',')
    csv_writer.writerow(['Action', 'Deadline', 'Urgent?'])
    csv_writer.writerow(['Push ups', 'MAR02', 'No'])
    csv_writer.writerow(['Learn Python', 'AUG01', 'NO'])
    csv_writer.writerow(['Drink Water', 'JUL24', 'YES'])
