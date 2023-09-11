# Importing the StringIO module.
from io import StringIO


# The arbitrary string.
string ='Hello and welcome to GeeksForGeeks.'

# Using the StringIO method to
# set aas file object.
file = StringIO(string)

# Here the cursor is at index 0.
print(file.tell())

# Cursor is set to index 20.
file.seek(20)

# Print the index of cursor
print(file.tell())
