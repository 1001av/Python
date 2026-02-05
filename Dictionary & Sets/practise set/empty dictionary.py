#  Create an empty dictionary. Allow 4 friends to enter their favorite language as 
# value and use key as their names. Assume that the names are unique. 

d = {}

n = input("enter name: ")
l = input("enter language: ")
d.update({n:l})

n = input("enter name: ")
l = input("enter language: ")
d.update({n:l})

n = input("enter name: ")
l = input("enter language: ")
d.update({n:l})

n = input("enter name: ")
l = input("enter language: ")
d.update({n:l})

print(d)

# Q7 If the names of 2 friends are same; what will happen to the program in problem 6?
# ans- just whatever the last value of that name will be shown to dictionary because it is updating continuously

# Q8  If languages of two friends are same; what will happen to the program in problem 6?
#  ans- nothing will change as values can be same but keys should be unique
