#  Remove duplicates from a sorted array 

def remove_duplicates(arr):
    if len(arr) == 0:
        return 0

    i = 0  # pointer for unique elements

    for j in range(1, len(arr)): 
        if arr[j] != arr[i]: # if the current element is different from the last unique element
            i += 1 
            arr[i] = arr[j] # move the unique element to the next position

    return i + 1  # new length


# Example
arr = [1, 1, 2, 2, 3, 4, 4]

new_length = remove_duplicates(arr)

print("Array after removing duplicates:", arr[:new_length])
print("New length:", new_length)

# ------------------another approach using set data structure-----------------------

arr = [1, 1, 2, 2, 3, 4, 4]
seen = set()
duplicate = set()

for i in arr:
    if i in seen:
        duplicate.add(i)
    else:
        seen.add(i)
print(list(seen))
print(len(list(seen)))
print(list(duplicate))