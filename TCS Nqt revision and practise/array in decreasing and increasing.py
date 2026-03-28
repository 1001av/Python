# Rearrange the array in increasing-decreasing order 

def rearrange_array(arr):
    n = len(arr)
    
    # Step 1: Sort the array
    arr.sort()
    
    # Step 2: Find middle index
    mid = (n + 1) // 2  # for odd length, mid will be the middle element; for even length, mid will be the first element of the second half
    
    # Step 3: Split into two parts
    first_half = arr[:mid]          # increasing
    second_half = arr[mid:]         # will reverse
    
    # Step 4: Reverse second half
    second_half.reverse()
    
    # Step 5: Combine
    return first_half + second_half


# Example
arr = [5, 2, 9, 1, 6, 3]
result = rearrange_array(arr)

print("Rearranged array:", result)