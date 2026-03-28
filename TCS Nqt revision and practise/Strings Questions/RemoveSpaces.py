#  Remove spaces from a string. 

def remove_spaces(s):
    result = '' # initializing an empty string to store the result

    for char in s: # iterating through each character in the input string
        if not char.isspace(): # checking if the character is not a space
            result += char # if it's not a space, add it to the result string

    return result # return the final string with spaces removed
# Example usage
input_string = "Hello World"
print("String with spaces removed:", remove_spaces(input_string))   
