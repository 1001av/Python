#  Count number of vowels, consonants, spaces in a string. 

def count_vowels_consonants_spaces(s):
    vowels = 0
    consonants = 0
    spaces = 0

    for char in s:
        if char.lower() in 'aeiou': # checking if the character is a vowel (case-insensitive)
            vowels += 1
        elif char.isalpha(): # checking if the character is a consonant (i.e., an alphabet that is not a vowel)
            consonants += 1
        elif char.isspace(): # checking if the character is a space
            spaces += 1

    return vowels, consonants, spaces

# Example usage
input_string = "Hello World"
vowels, consonants, spaces = count_vowels_consonants_spaces(input_string)
print(f"Vowels: {vowels}, Consonants: {consonants}, Spaces: {spaces}")