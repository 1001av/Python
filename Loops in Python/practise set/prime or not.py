# Write a program to find whether a given number is prime or not. 

n = int(input("enter no: " ))
for i in range (2,n):
    if (n % i == 0):
       print("Not Prime")
       break
else:
    print("prime")