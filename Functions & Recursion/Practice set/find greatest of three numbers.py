# 1. Write a program using functions to find greatest of three numbers.

def greatest (a, b, c):
    if(a > b and a > c):
        print("greatest no. is: ", a)
    elif(b > a and b > c):
        print("greatest no. is: ", b)
    else:
        print(c ," is the greatest") 
        
    return "done"

a = int(input("enter: "))
b = int(input("enter: "))
c = int(input("enter: "))
print(greatest(a, b, c))
    