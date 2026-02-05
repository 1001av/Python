# Write a python program using function to convert Celsius to Fahrenheit. 

def FahToCel(f):
    return ((f - 32)*5)/9    

f = int(input("enter value: "))
print(round(FahToCel(f)))  # this will roundoff to nearest integer
print(round(FahToCel(f), 2))  #round will be used to round off to two decimal