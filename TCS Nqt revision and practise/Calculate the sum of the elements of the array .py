# Calculate the sum of the elements of the array 

def array_sum(arr):
    total = 0
    
    for num in arr:
        total += num
    
    return total


# Example
arr = [1, 2, 3, 4, 5]
print("Sum of array:", array_sum(arr))