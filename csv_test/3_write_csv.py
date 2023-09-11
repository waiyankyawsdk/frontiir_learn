import csv

with open('employee_file.csv', mode='w') as employee_file:
    employee_writer = csv.writer(employee_file, delimiter=',', quotechar="'", quoting=csv.QUOTE_NONNUMERIC)

    employee_writer.writerow([1,'John Smith', 'Accounting', 'November'])
    employee_writer.writerow([2,'Erica Meyers', 'IT', 'March'])