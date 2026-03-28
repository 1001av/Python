# Remove characters from a string except alphabets. 

def remove_characters(s):
    result = '' # initializing an empty string to store the result

    for char in s: # iterating through each character in the input string
        if char.isalpha(): # checking if the character is an alphabet
            result += char # if it's an alphabet, add it to the result string

    return result # return the final string with non-alphabet characters removed