'''
Write a program to generate multiplication tables from 2 to 20 and write it to the 
different files. Place these files in a folder for a 13 – year old.
'''

def MutliplicationTable(n):
    table = ""       # create an empty table
    for i in range(1,11):
        table += f"{n} X {i} = {n * i}\n"  # put values in the table

    with open(f"tables/table {n}.txt", "w") as f:  # open a folder which consists of multiple files of {n} tables and use write"w" function
        f.write(table)  # now write the updated value in the table

for i in range(2,21):   # call the function for each table(2 - 21)
    MutliplicationTable(i)
