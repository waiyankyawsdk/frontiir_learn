import pandas
data = pandas.read_csv('hr_data.csv',index_col='Name',parse_dates=['Hire Date'])
print(data)
print(data['Hire Date'][0])