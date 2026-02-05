# 7. Write a program to find out the line number where python is present from ques 6. 

with open("log.txt")as f:
    lines = f.readlines()

lineNo = 1
for line in lines:
    if ("python" in line):
        print(f"yes it is present in line no: {lineNo}")
        break
    lineNo += 1

else:
        print("python is not present")

'''
This else belongs to the for loop, not the if.
In Python, a for-else construct means:
The else block runs only if the loop finishes without hitting a break.
'''

