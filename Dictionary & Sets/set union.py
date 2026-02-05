s1 = {1,45,5}
s2 = (2,1,5,65,23)

# print(s1.union(s2))  it takes all the unique values from both the sets
# print(s1.intersection(s2)) shows overlapping values
# print(s1.difference(s2)) gives the left over element after difference of the sets
print({1,5}.issubset(s2)) # Checks if all elements of this set are in another.
print((s1).issuperset(s2)) #Checks if this set contains all elements of another.
print((s1).isdisjoint(s2)) # Checks if two sets have no elements in common.