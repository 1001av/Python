# Remove all vowels from the string. 

def remove_vowels(s):
    vowels = 'aeiouAEIOU' # defining a string of vowels (both lowercase and uppercase)
    result = '' # initializing an empty string to store the result

    for char in s: # iterating through each character in the input string
        if char not in vowels: # checking if the character is not a vowel
            result += char # if it's not a vowel, add it to the result string

    return result # return the final string with vowels removed

# Example usage
input_string = "Hello World"
print("String with vowels removed:", remove_vowels(input_string))
