# 4. Write a recursive function to calculate the sum of first n natural numbers. 

def SumOfN(n):
    if (n==1):   # base condition is necessary, if not used than recursion can go for infinitely
        return 1
    else:
        return (n + SumOfN(n-1))

n = int(input("enter: "))
print(SumOfN(n))