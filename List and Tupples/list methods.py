# unlike string lists are mutable so any method perform will change the original list, whereas in string
# a new string is formed but the original doesent change

friends = ["apple", "orange", 1001, 23.456, False, "akash"]
print(friends)

friends.append("akhil") # append adds the new element in the last of the list
print(friends)

l1 = [3, 5, 7, 2, 9, 1]
# l1.sort()
# l1.reverse()
# l1.insert(3, 567)  #inserting at an index
# l1.pop(2) # pop out any index
# print(l1)

# print (l1.pop(2)) # now it will give you the poped out element as output

l1.remove(2)  # it removes the value of an element in the list
print(l1)
