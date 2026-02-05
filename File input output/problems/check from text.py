# 1. Write a program to read the text from a given file ‘poems.txt’ and find out 
# whether it contains the word ‘twinkle’. 


with  open("poems.txt") as f:
   lines = f.read()
   if ("twinkle" in lines):
     print("yes it has")
   else:
     print("this word is not present in the poem")