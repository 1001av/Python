# What will be the length of following set s:
# (very famous question in interviews)
s = set() 
s.add(20) 
s.add(20.0) 
s.add('20') 
print(len(s)) # the length will be 2 because 20 and 20.0 are considered same in python, but '20' is different because it is a string