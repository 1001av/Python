f = open("file.txt")
# lines =  f.readlines()  # it returns a list, aap jitne baar is func ko chloege utni baar line repeat hogi
# print(lines, type(lines))

# line1 =  f.readline()  
# print(line1, type(line1))

# line2 =  f.readline()  
# print(line2, type(line2))

# line3 =  f.readline()  
# print(line3, type(line3))

# line4 =  f.readline()  
# print(line4, type(line4))

# line5 =  f.readline()  
# print(line5 == "")

# using while loop
line = f.readline()
while(line != ""):
    print(line)
    line = f.readline()

f.close()