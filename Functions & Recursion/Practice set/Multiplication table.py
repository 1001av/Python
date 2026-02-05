#  Write a python function to print multiplication table of a given number.

def Table(n):
    for i in range(1,11):
        mul = n * i
        print(mul)
print(Table(5))