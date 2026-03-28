# # Find the average of all elements in an array 

# def average(arr):
#     total = sum(arr)  # Calculate the sum of the array elements
#     count = len(arr)  # Get the number of elements in the array
    
#     if count == 0:
#         return 0  # Avoid division by zero, return 0 for an empty array
    
#     return total / count  # Return the average

# # Example
# arr = [1, 2, 3, 4, 5]
# print("Average of array:", average(arr))

#                  or              

def find_average(arr):
    if len(arr) == 0:
        return 0
    
    total = 0
    for num in arr:
        total += num
    
    return total / len(arr)


# Example
arr = [10, 20, 30, 40, 50]
print("Average:", find_average(arr))