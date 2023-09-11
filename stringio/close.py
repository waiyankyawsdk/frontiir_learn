# Importing the StringIO module.
from io import StringIO


# The arbitrary string.
string ='Hello and welcome to GeeksForGeeks.'

# Using the StringIO method to
# set as file object.
file = StringIO(string)

# Reading the file.
print(file.read())
print(file.tell())

# Closing the file.
file.close()

# If we now perform any operation on the file
# it will raise an ValueError.

# This is to know whether the
# file is closed or not.
print("Is the file closed?", file.closed)
# file.seek(0)
# print(file.read())
# #ValueError: I/O operation on closed file
