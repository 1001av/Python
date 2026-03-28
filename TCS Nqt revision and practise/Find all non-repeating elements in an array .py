# Find all non-repeating elements in an array 

def find_non_repeating(arr):
    freq = {} # creating an empty dictionary to store the frequency of each element in the array
    non_repeating = [] # creating an empty list to store the non-repeating elements

    for num in arr:
        if num in freq:
            freq[num] += 1 # if the number is already in the frequency dictionary, increment its count
        else:
            freq[num] = 1 # if the number is not in the frequency dictionary, add it with a count of 1

    for num, count in freq.items(): # iterating through the frequency dictionary to find non-repeating elements
        if count == 1:    
            non_repeating.append(num) # if the count of the number is 1, it means it is a non-repeating element, so we add it to the non_repeating list

    return non_repeating

arr = [1, 2, 3, 1, 3, 6, 6]
print("Non-repeating elements:", find_non_repeating(arr))

#     CHATGPT ANSWER

def find_non_repeating(arr):
    freq = {} 
    
    # Count frequency
    for num in arr: 
        if num in freq:  
            freq[num] += 1
        else:
            freq[num] = 1

    # Collect elements with frequency 1
    result = []
    for key in freq:
        if freq[key] == 1:
            result.append(key)

    return result


# Example
arr = [1, 2, 3, 1, 3, 6, 6]
print("Non-repeating elements:", find_non_repeating(arr))