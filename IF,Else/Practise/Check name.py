# Write a program to find out whether a given post is talking about “Akhil” or not. 

statement = input("Enter sentence: " )

if ("Akhil" in statement.lower()): # we use lower method to reduce whatever the statement in lower letter which can find the name irrespective of the letters notation
    print("Yes it is talking about me")
else :
    print("no it is not talking about me")