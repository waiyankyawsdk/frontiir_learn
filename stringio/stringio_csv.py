import csv
import io

exampleObject = io.StringIO() #creating object
writeCSV = csv.writer(exampleObject,delimiter=",")
 
# Writing the rows
writeCSV.writerows([["pythonpool", "stringIO","python"],["12", "23", "4"],["#", "%^", "^&"]])
                              
# Setting the cursor to the beginning of the csv file object
exampleObject.seek(0)
 
# Creating an iteration to print the rows of the csv file
for eachRow in exampleObject:
     print(eachRow)