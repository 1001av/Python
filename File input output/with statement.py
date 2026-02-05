# f = open("file.txt")
# print(f.read())
# f.close() # but what if we dont want to write close statement, then we use with statement

# the same can be written using with statement like this:
with open("file.txt") as f:
    print(f.read())   # under the statement all operations take place and it automatically closes the function
