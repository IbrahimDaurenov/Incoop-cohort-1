import csv


def beauty_print(my_dict):
    for country in my_dict.keys():
        print(country + ' | ' + str(my_dict[country]))


def main():
    results = dict()

    with open('ugly_results.csv') as file:
        csv_reader = csv.reader(file, delimiter = ',')
        for row in csv_reader:
            if row[0][0:3] not in results.keys():
                results[row[0][0:3]] = int(row[1])
            else:
                results[row[0][0:3]] = results[row[0][0:3]] + int(row[1])
    beauty_print(results)



if __name__ == '__main__':
    main()
