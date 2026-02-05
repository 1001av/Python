#  Write a program to print multiplication table of a given number using for loop.

n = int(input("enter no: " ))
for i in range (1,11):
    mul = i * n
    print(mul)

# with while 
# i = 1
# while (i < 11):
#     print(i * n)
#     i += 1