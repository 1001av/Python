#  Write a python program to rename a file to “renamed_by_ python.txt. 

with open("old.txt") as f:
    content1 = f.read()

with open("renamed_by_python.txt", "w") as f:
    f.write(content1)

# you can even use os model or can import shutil, with that you can even delete the old file