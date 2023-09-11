# Importing the StringIO module.
from io import StringIO


# The arbitrary string.
string ='Hello and welcome to GeeksForGeeks.'

# Using the StringIO method
# to set as file object.
file = StringIO(string)

# Reading the initial file:
print(file.read())

# To set the cursor at 0.
file.seek(0)


# This will drop the file after
# index 18.
file.truncate(18)

# File after truncate.
print(file.read())
