# 10. Write a program to print multiplication table of n using for loops in reversed 
# order.

n = int(input("enter no: " ))
for i in range(1,11):
    print(f"{n} X {11 - i} = {n*(11-i)}")



# using normal method
# n = int(input("enter no: " ))
# for i in range (1,11):
#     mul = n * (11 - i)
#     print(mul)
