import json

io = open("in.json","r")
string = io.read()
# json.loads(str)
dictionary = json.loads(string)

# or one-liner
# dictionary = json.loads(open("in.json","r").read())

print(dictionary)