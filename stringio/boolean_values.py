# Importing the StringIO module.
from io import StringIO


# The arbitrary string.
string ='Hello and welcome to GeeksForGeeks.'

# Using the StringIO method to
# set as file object.
file = StringIO(string)

# This will returns whether the file
# is interactive or not.
print("Is the file stream interactive?", file.isatty())

# This will returns whether the file is
# readable or not.
print("Is the file stream readable?", file.readable())

# This will returns whether the file supports
# writing or not.
print("Is the file stream writable?", file.writable())

# This will returns whether the file is
# seekable or not.
print("Is the file stream seekable?", file.seekable())

# This will returns whether the file is
# closed or not.
print("Is the file closed?", file.closed)
