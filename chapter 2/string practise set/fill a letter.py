# Write a program to fill in a letter template given below with name and date. 
# letter = '''  
# Dear <|Name|>, 
# You are selected! 
# <|Date|> 
# ''' 

letter = ''' Dear <|Name|>, 
You are selected! 
<|Date|> '''  
print(letter.replace("<|Name|>", "Akhil").replace("<|Date|>", "10 january 2025"))

# we can use chaining function replace by replacing in the newly updated string 