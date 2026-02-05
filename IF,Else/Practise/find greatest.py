# Write a program to find the greatest of four numbers entered by the user. 
a = int(input("enter number: "))
b = int(input("enter number: "))
c = int(input("enter number: "))
d = int(input("enter number: "))

if a > b and a > c and a > d:
    print("a is greatest")
elif b > a and b > c and b > d:
    print("b is greatest")
elif c > a and c > b and c > d:
    print("c is greatest")
else:
    print("d is greatest")
