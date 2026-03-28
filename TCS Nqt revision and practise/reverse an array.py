# Reverse a given array
arr = [1,2,3,4,5]
# method 1: Using slicing
reversed_arr = arr[::-1] # this is a slicing method which is used to reverse the array, it creates a new array with the elements in reverse order
print("Reversed array (Method 1):", reversed_arr)

# # method 2: Using the reverse() method # this method is used to reverse the array in place, it modifies the original array and does not return a new array
# arr_copy = arr.copy() # creating a copy of the original array to avoid modifying it
# arr_copy.reverse()
# print("Reversed array (Method 2):", arr_copy)

# # method 3: Using a loop # this method is used to reverse the array by iterating through the array from the last element to the first element and appending it to a new array
# reversed_arr = []
# for i in range(len(arr) - 1, -1, -1):
#     reversed_arr.append(arr[i])
# print("Reversed array (Method 3):", reversed_arr)