import csv

with open('csv_employee_birth.txt') as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter=',')

    output = []
    for row in csv_reader:
        if row:
            try:
                data = int(row['id'])
                output.append("%d"%data)
            except ValueError:
                continue
    print(output)
        # if count == 0:
        #     print(f'Column names are : {",".join(row)}')
        #     count+=1
        # else:
        #     print(f'\t{row[0]} works in the {row[1]} departments, born in {row[2]}')
        #     count+=1
    # print(f'Processed {count} lines.')