import pandas
data = pandas.read_csv('hr_data.csv',index_col='Employee',parse_dates=['Hired'],header = 0, names = ['Employee','Hired', 'Salary','Sick Days'])
print(data)
print(data['Hired'][0])
data.to_csv('hrdata_modified.csv')