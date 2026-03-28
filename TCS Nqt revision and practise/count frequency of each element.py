# Count the frequency of each element in an array 

def count_frequency(arr):
    freq = {} # creating an empty dictionary to store the frequency of each element in the array

    for num in arr:
        if num in freq: # if the number is already in the frequency dictionary, increment its count
            freq[num] += 1
        else:
            freq[num] = 1

    return freq


# Example
arr = [1, 2, 2, 3, 1, 4, 2]
result = count_frequency(arr)

print(result)