# dictionary is a list of key value pairs
# it is mutable(changes can be done)
# it is indexed (through keys)
# it is unordered
# it cannot contain duplicate keys
# dictionary is very helpfull to find a value through its key which is much easy than finding element in list through indexing
# you cant do indexing in a dictionary because it can directly store your values & you can find that value through its reference keys

d = {} # empty dictionary

marks = {
    "rohan": 100,
    "sohan": 56,
    "mohan": 27,
    "list": [1, 3, 5] # you can even put a list inside a dictionary

}
# print(marks, type(marks))
print(marks["list"]) 