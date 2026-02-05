# Write a program to print the following star pattern. 
#   * 
#  *** 
# ***** for n = 3

n = int(input("enter no: " ))
for i in range(1,n+1):
    print(" "* (n-i), end="")  # For spaces, end will not give new line
    print("*"* ((2*i)-1), end="")  # for stars
    print("")  # for new line
