# tupple is like string, immutable
# a = () # empty tupple 
# a = (1,) # tupple with only one element needs a comma

a = (1,2,False,4,"rohan",2)
print(type(a))
print(a[2])
print(a[-5]) # negative indexing
print(a[1:4]) # slicing in tuple
print(a.count(2)) # count will give the number of times a specific element is written in a tupple
print(a.index(2))#  index will give the index of specific element, but if two same element are written then 
# it shows the index of the 1st occuring element only

# packing and unpacking in python
t = 1, 2, "Python"  # packing
a, b, c = t  # unpacking
print(a, b, c)  # output = 1 2 Python

# concatenation & repetation 
# concatenation
t1 = (1, 2)
t2 = (3, 4)
print(t1 + t2)  # (1, 2, 3, 4)

# repetation
print(t1 * 3)  # (1, 2, 1, 2, 1, 2)

# Built-in Functions
# len(t) → length of tuple
# max(t) / min(t) → largest/smallest element (works if elements are comparable)
x = (1,4,7,9,5,8)
print(max(x))
# sum(t) → sum of numeric elements
print(sum(x))
# sorted(t) → returns a sorted list (not a tuple)
print(sorted(x))
# tuple.count(x) → count occurrences
# tuple.index(x) → find index of first occurrence

#Tuples are often used in problems where you need to store pairs/triples (like coordinates, or (value, index) pairs). Since they’re immutable, they’re safe to use as keys in hash-based structures like dictionaries and sets.