def SumNatural (n):
    sum = ((n*(n+1))//2)  # for getting only integer values after dividing use // instead of / which avoids unnecessary conversion with int
    return sum

n = int(input("enter: " ))
print(SumNatural(n))
