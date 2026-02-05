# Write a program to calculate the grade of a student from his marks from the 
# following scheme: 
# 90 – 100 => Ex 
# 80 – 90 => A 
# 70 – 80 => B 
# 60 – 70  =>C 
# 50 – 60 => D 
# <50        
# => F

Marks = int(input("enter marks: " ))

if (Marks >= 0 and Marks < 50):
    print("F grade")
elif (Marks >= 50 and Marks < 60):
    print("D grade")
elif (Marks >= 60 and Marks < 70):
    print("C grade")
elif (Marks >= 70 and Marks < 80):
    print("B grade")
elif (Marks >= 80 and Marks < 90):
    print("A grade")
else:
    print("Excellent")
