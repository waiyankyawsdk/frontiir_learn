import csv

output = []
with open('csv_employee_birth.txt') as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter=',')
    for row in csv_reader:
        if row:
            try:
                data = int(row['id'])
                output.append("%i"%data)
            except ValueError:
                continue

if output:
    try:
        with open('employee_id.csv',mode='w') as employee_id_file:
            csv_writer = csv.writer(employee_id_file,delimiter=',',quotechar='"',quoting=csv.QUOTE_MINIMAL)
            csv_writer.writerows(output)
    except IOError as e:
        print(e)