# Rotate an array by K elements - Block Swap Algorithm 
def rotate_array(arr, k):
    n = len(arr)
    k = k % n  # Handle cases where k is larger than the array size 

    # Split the array into two blocks
    block1 = arr[:k] # this is the first block which contains the first k elements of the array
    block2 = arr[k:] # this is the second block which contains the remaining elements of the array after the first k elements

    # Swap the blocks
    arr[:] = block2 + block1

# Example usage
arr = [1, 2, 3, 4, 5, 6, 7]
k = 3
print("Original array:", arr)
rotate_array(arr, k)
print("Array after rotating by", k, "elements:", arr)

