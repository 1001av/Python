# Repeat program 4 for a list of such words to be censored. 

words = ["Donkeys", "intelligent", "dumb", "smart"]
with open("Donkey.txt","r") as f:
    content = f.read()

for word in words:  # we will search for each word in words
    content = content.replace(word, "#"*len(word)) # un words ko unke jitne length ke # se replace kr do

with open("Donkey.txt", "w") as f:
    f.write(content)