# Write a program to mine a log file and find out whether it contains ‘python’.
word = input("enter the word to find: ")
with open("log.txt") as f:
    content = f.read()

if (word in content):
    print("yes it is present")
else:
    print("No, it is not present")