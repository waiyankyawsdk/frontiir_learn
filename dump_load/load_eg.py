import json
# json.load(_io)
io = open("in.json","r")
dictionary = json.load(io)

# or one-liner
# dictionary = json.load(open("in.json","r"))

print(dictionary)