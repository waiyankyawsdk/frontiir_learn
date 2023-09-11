import io
import csv

new_out = io.StringIO()
new_dictionary = [{"emp_name": "OLava", "emp_id": "4567", "skills": "Python"},{"emp_2": "Suzane", "emp_id2": "1678", "skills": "Java"}]
new_path = open("test8.csv", "w")
l = csv.writer(new_path,new_out)
for m in new_dictionary:
    l.writerow([m])
con_csv = new_out.getvalue()
print(con_csv)
new_path.close()
