import csv
try:
    with open('employee_id.csv',mode='w') as file:
        field_names = ['id','name','department','birth_month']
        csv_writer = csv.DictWriter(file,delimiter=',',quotechar='"',quoting=csv.QUOTE_MINIMAL,fieldnames=field_names)
        csv_writer.writeheader()
        csv_writer.writerow({'id': 1,'name': 'John Smith', 'department': 'Accounting', 'birth_month': 'November'})
        csv_writer.writerow({'id': 2,'name': 'Erica Meyers', 'department': 'IT', 'birth_month': 'March'})
except IOError as e:
    print(e)