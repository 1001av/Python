# Write a program to find whether a given username contains less than 10 
# characters or not. 

username = input("enter name: " )
if (len(username) < 10):# len function gives the length of the string, if it is less than 10 then it is approved otherwise not approved
    print("yes, approved")
else:
    print("no, not approved")