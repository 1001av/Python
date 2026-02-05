#  Write a program to find out whether a student has passed or failed if it requires a 
# total of 40% and at least 33% in each subject to pass. Assume 3 subjects and 
# take marks as an input from the user. 

s1 = int(input("Enter Marks: " ))
s2 = int(input("Enter Marks: " ))
s3 = int(input("Enter Marks: " ))

#  check for total percentage
total_percentage = (100*(s1 + s2 + s3))/300
# now follow conditions
if (total_percentage >= 40 and s1 >= 33 and s2 >= 33 and s3 >= 33):
    print("you are passed: ", total_percentage)
else :
    print("you failed: ", total_percentage) 

