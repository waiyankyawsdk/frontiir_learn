import csv

with open('csv_employee_birth.txt') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    count = 0
    for row in csv_reader:
        if count == 0:
            print(f'Column names are : {",".join(row)}')
            count+=1
        print(f'\t{row["name"]} works in the {row["department"]} departments, born in {row["birthday month"]}')
        count+=1
    print(f'Processed {count} lines.')