# Print all the duplicates in the input string

def print_duplicates(s):
    char_count = {} # creating an empty dictionary to store the count of each character in the string

    for char in s: # iterating through each character in the input string
        if char in char_count: # if the character is already in the dictionary, increment its count
            char_count[char] += 1
        else:
            char_count[char] = 1 # if it's not in the dictionary, add it with a count of 1

    duplicates = [char for char, count in char_count.items() if count > 1] # creating a list of characters that have a count greater than 1 (duplicates)

    return duplicates # return the list of duplicates

# Example usage
input_string = "programming"
print("Duplicates in the string:", print_duplicates(input_string))  