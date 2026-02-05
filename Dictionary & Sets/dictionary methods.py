marks = {
    "rohan": 100,
    "sohan": 56,
    "mohan": 27,
    "list": [1, 3, 5] # you can even put a list inside a dictionary

}
# print(marks.items()) # this gives key, value pairs inside a tuple, we can further use it by for loop
# print(marks.keys())
# print(marks.values())
# print(len(marks))  # this gives the length of marks
# marks.update({"rohan": 95, "john": 75}) # agr same key value pair hai to update hojayega, aur agr nhi hai to add ho jayega
# print(marks)

# get function & square indexing gives the same result, but in this case it gives different answers(asked in interviews)
# print(marks.get("rohan2"))  # prints none
# print(marks["rohan2"])  # returns an error

marks.pop("list")
print(marks)

