# Importing the StringIO module.
from io import StringIO


# The arbitrary string.
string ='Hello and welcome to GeeksForGeeks.'

# Using the StringIO method
# to set as file object.
file = StringIO(string)

# Reading the file:
print(file.read())

# Now if we again want to read
# the file it shows empty file
# because the cursor is set to
# the last index.


# This does not print anything
# because the function returns an
# empty string.
print(file.read())

# Hence to set the cursor position
# to read or write the file again
# we use seek().We can pass any index
# here form(0 to len(file))
file.seek(0)

# Now we can able to read the file again()
print(file.read())
