'''
Write a python function to print first n lines of the following pattern: 
*** 
**               
*                - for n = 3
'''
# USING FOR LOOP?]
# def pattern(n):
#         for i in range (1,n+1):
#             print("*"* ((n-i)+1), end="")
#             print("")
        
# n = int(input("enter here: "))
# print(pattern(n))

# this code can also be written by using RECURSION

def pattern(n):
      if (n == 0):
            return   
      else:
            print("*" * n)
            pattern(n-1)

pattern(3)